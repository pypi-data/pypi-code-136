'''
# `upcloud_managed_database_postgresql`

Refer to the Terraform Registory for docs: [`upcloud_managed_database_postgresql`](https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql).
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


class ManagedDatabasePostgresql(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresql",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql upcloud_managed_database_postgresql}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        plan: builtins.str,
        zone: builtins.str,
        id: typing.Optional[builtins.str] = None,
        maintenance_window_dow: typing.Optional[builtins.str] = None,
        maintenance_window_time: typing.Optional[builtins.str] = None,
        powered: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        properties: typing.Optional[typing.Union["ManagedDatabasePostgresqlProperties", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql upcloud_managed_database_postgresql} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the service. The name is used as a prefix for the logical hostname. Must be unique within an account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#name ManagedDatabasePostgresql#name}
        :param plan: Service plan to use. This determines how much resources the instance will have. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#plan ManagedDatabasePostgresql#plan}
        :param zone: Zone where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#zone ManagedDatabasePostgresql#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#id ManagedDatabasePostgresql#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window_dow: Maintenance window day of week. Lower case weekday name (monday, tuesday, ...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_dow ManagedDatabasePostgresql#maintenance_window_dow}
        :param maintenance_window_time: Maintenance window UTC time in hh:mm:ss format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_time ManagedDatabasePostgresql#maintenance_window_time}
        :param powered: The administrative power state of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#powered ManagedDatabasePostgresql#powered}
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#properties ManagedDatabasePostgresql#properties}
        :param title: Title of a managed database instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#title ManagedDatabasePostgresql#title}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresql.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedDatabasePostgresqlConfig(
            name=name,
            plan=plan,
            zone=zone,
            id=id,
            maintenance_window_dow=maintenance_window_dow,
            maintenance_window_time=maintenance_window_time,
            powered=powered,
            properties=properties,
            title=title,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putProperties")
    def put_properties(
        self,
        *,
        admin_password: typing.Optional[builtins.str] = None,
        admin_username: typing.Optional[builtins.str] = None,
        automatic_utility_network_ip_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autovacuum_analyze_scale_factor: typing.Optional[jsii.Number] = None,
        autovacuum_analyze_threshold: typing.Optional[jsii.Number] = None,
        autovacuum_freeze_max_age: typing.Optional[jsii.Number] = None,
        autovacuum_max_workers: typing.Optional[jsii.Number] = None,
        autovacuum_naptime: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_cost_delay: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_cost_limit: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_scale_factor: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_threshold: typing.Optional[jsii.Number] = None,
        backup_hour: typing.Optional[jsii.Number] = None,
        backup_minute: typing.Optional[jsii.Number] = None,
        bgwriter_delay: typing.Optional[jsii.Number] = None,
        bgwriter_flush_after: typing.Optional[jsii.Number] = None,
        bgwriter_lru_maxpages: typing.Optional[jsii.Number] = None,
        bgwriter_lru_multiplier: typing.Optional[jsii.Number] = None,
        deadlock_timeout: typing.Optional[jsii.Number] = None,
        idle_in_transaction_session_timeout: typing.Optional[jsii.Number] = None,
        ip_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        jit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_autovacuum_min_duration: typing.Optional[jsii.Number] = None,
        log_error_verbosity: typing.Optional[builtins.str] = None,
        log_line_prefix: typing.Optional[builtins.str] = None,
        log_min_duration_statement: typing.Optional[jsii.Number] = None,
        max_files_per_process: typing.Optional[jsii.Number] = None,
        max_locks_per_transaction: typing.Optional[jsii.Number] = None,
        max_logical_replication_workers: typing.Optional[jsii.Number] = None,
        max_parallel_workers: typing.Optional[jsii.Number] = None,
        max_parallel_workers_per_gather: typing.Optional[jsii.Number] = None,
        max_pred_locks_per_transaction: typing.Optional[jsii.Number] = None,
        max_prepared_transactions: typing.Optional[jsii.Number] = None,
        max_replication_slots: typing.Optional[jsii.Number] = None,
        max_stack_depth: typing.Optional[jsii.Number] = None,
        max_standby_archive_delay: typing.Optional[jsii.Number] = None,
        max_standby_streaming_delay: typing.Optional[jsii.Number] = None,
        max_wal_senders: typing.Optional[jsii.Number] = None,
        max_worker_processes: typing.Optional[jsii.Number] = None,
        migration: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesMigration", typing.Dict[str, typing.Any]]] = None,
        pgbouncer: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesPgbouncer", typing.Dict[str, typing.Any]]] = None,
        pglookout: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesPglookout", typing.Dict[str, typing.Any]]] = None,
        pg_partman_bgw_interval: typing.Optional[jsii.Number] = None,
        pg_partman_bgw_role: typing.Optional[builtins.str] = None,
        pg_read_replica: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pg_service_to_fork_from: typing.Optional[builtins.str] = None,
        pg_stat_statements_track: typing.Optional[builtins.str] = None,
        public_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shared_buffers_percentage: typing.Optional[jsii.Number] = None,
        synchronous_replication: typing.Optional[builtins.str] = None,
        temp_file_limit: typing.Optional[jsii.Number] = None,
        timescaledb: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesTimescaledb", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        track_activity_query_size: typing.Optional[jsii.Number] = None,
        track_commit_timestamp: typing.Optional[builtins.str] = None,
        track_functions: typing.Optional[builtins.str] = None,
        track_io_timing: typing.Optional[builtins.str] = None,
        variant: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        wal_sender_timeout: typing.Optional[jsii.Number] = None,
        wal_writer_delay: typing.Optional[jsii.Number] = None,
        work_mem: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param admin_password: Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_password ManagedDatabasePostgresql#admin_password}
        :param admin_username: Custom username for admin user. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_username ManagedDatabasePostgresql#admin_username}
        :param automatic_utility_network_ip_filter: Automatic utility network IP Filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#automatic_utility_network_ip_filter ManagedDatabasePostgresql#automatic_utility_network_ip_filter}
        :param autovacuum_analyze_scale_factor: autovacuum_analyze_scale_factor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_scale_factor ManagedDatabasePostgresql#autovacuum_analyze_scale_factor}
        :param autovacuum_analyze_threshold: autovacuum_analyze_threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_threshold ManagedDatabasePostgresql#autovacuum_analyze_threshold}
        :param autovacuum_freeze_max_age: autovacuum_freeze_max_age. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_freeze_max_age ManagedDatabasePostgresql#autovacuum_freeze_max_age}
        :param autovacuum_max_workers: autovacuum_max_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_max_workers ManagedDatabasePostgresql#autovacuum_max_workers}
        :param autovacuum_naptime: autovacuum_naptime. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_naptime ManagedDatabasePostgresql#autovacuum_naptime}
        :param autovacuum_vacuum_cost_delay: autovacuum_vacuum_cost_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_delay ManagedDatabasePostgresql#autovacuum_vacuum_cost_delay}
        :param autovacuum_vacuum_cost_limit: autovacuum_vacuum_cost_limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_limit ManagedDatabasePostgresql#autovacuum_vacuum_cost_limit}
        :param autovacuum_vacuum_scale_factor: autovacuum_vacuum_scale_factor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_scale_factor ManagedDatabasePostgresql#autovacuum_vacuum_scale_factor}
        :param autovacuum_vacuum_threshold: autovacuum_vacuum_threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_threshold ManagedDatabasePostgresql#autovacuum_vacuum_threshold}
        :param backup_hour: The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_hour ManagedDatabasePostgresql#backup_hour}
        :param backup_minute: The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_minute ManagedDatabasePostgresql#backup_minute}
        :param bgwriter_delay: bgwriter_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_delay ManagedDatabasePostgresql#bgwriter_delay}
        :param bgwriter_flush_after: bgwriter_flush_after. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_flush_after ManagedDatabasePostgresql#bgwriter_flush_after}
        :param bgwriter_lru_maxpages: bgwriter_lru_maxpages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_maxpages ManagedDatabasePostgresql#bgwriter_lru_maxpages}
        :param bgwriter_lru_multiplier: bgwriter_lru_multiplier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_multiplier ManagedDatabasePostgresql#bgwriter_lru_multiplier}
        :param deadlock_timeout: deadlock_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#deadlock_timeout ManagedDatabasePostgresql#deadlock_timeout}
        :param idle_in_transaction_session_timeout: idle_in_transaction_session_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#idle_in_transaction_session_timeout ManagedDatabasePostgresql#idle_in_transaction_session_timeout}
        :param ip_filter: IP filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ip_filter ManagedDatabasePostgresql#ip_filter}
        :param jit: jit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#jit ManagedDatabasePostgresql#jit}
        :param log_autovacuum_min_duration: log_autovacuum_min_duration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_autovacuum_min_duration ManagedDatabasePostgresql#log_autovacuum_min_duration}
        :param log_error_verbosity: log_error_verbosity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_error_verbosity ManagedDatabasePostgresql#log_error_verbosity}
        :param log_line_prefix: log_line_prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_line_prefix ManagedDatabasePostgresql#log_line_prefix}
        :param log_min_duration_statement: log_min_duration_statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_min_duration_statement ManagedDatabasePostgresql#log_min_duration_statement}
        :param max_files_per_process: max_files_per_process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_files_per_process ManagedDatabasePostgresql#max_files_per_process}
        :param max_locks_per_transaction: max_locks_per_transaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_locks_per_transaction ManagedDatabasePostgresql#max_locks_per_transaction}
        :param max_logical_replication_workers: max_logical_replication_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_logical_replication_workers ManagedDatabasePostgresql#max_logical_replication_workers}
        :param max_parallel_workers: max_parallel_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers ManagedDatabasePostgresql#max_parallel_workers}
        :param max_parallel_workers_per_gather: max_parallel_workers_per_gather. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers_per_gather ManagedDatabasePostgresql#max_parallel_workers_per_gather}
        :param max_pred_locks_per_transaction: max_pred_locks_per_transaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_pred_locks_per_transaction ManagedDatabasePostgresql#max_pred_locks_per_transaction}
        :param max_prepared_transactions: max_prepared_transactions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_prepared_transactions ManagedDatabasePostgresql#max_prepared_transactions}
        :param max_replication_slots: max_replication_slots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_replication_slots ManagedDatabasePostgresql#max_replication_slots}
        :param max_stack_depth: max_stack_depth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_stack_depth ManagedDatabasePostgresql#max_stack_depth}
        :param max_standby_archive_delay: max_standby_archive_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_archive_delay ManagedDatabasePostgresql#max_standby_archive_delay}
        :param max_standby_streaming_delay: max_standby_streaming_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_streaming_delay ManagedDatabasePostgresql#max_standby_streaming_delay}
        :param max_wal_senders: max_wal_senders. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_wal_senders ManagedDatabasePostgresql#max_wal_senders}
        :param max_worker_processes: max_worker_processes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_worker_processes ManagedDatabasePostgresql#max_worker_processes}
        :param migration: migration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#migration ManagedDatabasePostgresql#migration}
        :param pgbouncer: pgbouncer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pgbouncer ManagedDatabasePostgresql#pgbouncer}
        :param pglookout: pglookout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pglookout ManagedDatabasePostgresql#pglookout}
        :param pg_partman_bgw_interval: pg_partman_bgw.interval. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_interval ManagedDatabasePostgresql#pg_partman_bgw_interval}
        :param pg_partman_bgw_role: pg_partman_bgw.role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_role ManagedDatabasePostgresql#pg_partman_bgw_role}
        :param pg_read_replica: Should the service which is being forked be a read replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_read_replica ManagedDatabasePostgresql#pg_read_replica}
        :param pg_service_to_fork_from: Name of the PG Service from which to fork (deprecated, use service_to_fork_from). This has effect only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_service_to_fork_from ManagedDatabasePostgresql#pg_service_to_fork_from}
        :param pg_stat_statements_track: pg_stat_statements.track. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_stat_statements_track ManagedDatabasePostgresql#pg_stat_statements_track}
        :param public_access: Public Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#public_access ManagedDatabasePostgresql#public_access}
        :param shared_buffers_percentage: shared_buffers_percentage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#shared_buffers_percentage ManagedDatabasePostgresql#shared_buffers_percentage}
        :param synchronous_replication: Synchronous replication type. Note that the service plan also needs to support synchronous replication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#synchronous_replication ManagedDatabasePostgresql#synchronous_replication}
        :param temp_file_limit: temp_file_limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#temp_file_limit ManagedDatabasePostgresql#temp_file_limit}
        :param timescaledb: timescaledb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timescaledb ManagedDatabasePostgresql#timescaledb}
        :param timezone: timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timezone ManagedDatabasePostgresql#timezone}
        :param track_activity_query_size: track_activity_query_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_activity_query_size ManagedDatabasePostgresql#track_activity_query_size}
        :param track_commit_timestamp: track_commit_timestamp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_commit_timestamp ManagedDatabasePostgresql#track_commit_timestamp}
        :param track_functions: track_functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_functions ManagedDatabasePostgresql#track_functions}
        :param track_io_timing: track_io_timing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_io_timing ManagedDatabasePostgresql#track_io_timing}
        :param variant: Variant of the PostgreSQL service, may affect the features that are exposed by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#variant ManagedDatabasePostgresql#variant}
        :param version: PostgreSQL major version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#version ManagedDatabasePostgresql#version}
        :param wal_sender_timeout: wal_sender_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_sender_timeout ManagedDatabasePostgresql#wal_sender_timeout}
        :param wal_writer_delay: wal_writer_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_writer_delay ManagedDatabasePostgresql#wal_writer_delay}
        :param work_mem: work_mem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#work_mem ManagedDatabasePostgresql#work_mem}
        '''
        value = ManagedDatabasePostgresqlProperties(
            admin_password=admin_password,
            admin_username=admin_username,
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            autovacuum_analyze_scale_factor=autovacuum_analyze_scale_factor,
            autovacuum_analyze_threshold=autovacuum_analyze_threshold,
            autovacuum_freeze_max_age=autovacuum_freeze_max_age,
            autovacuum_max_workers=autovacuum_max_workers,
            autovacuum_naptime=autovacuum_naptime,
            autovacuum_vacuum_cost_delay=autovacuum_vacuum_cost_delay,
            autovacuum_vacuum_cost_limit=autovacuum_vacuum_cost_limit,
            autovacuum_vacuum_scale_factor=autovacuum_vacuum_scale_factor,
            autovacuum_vacuum_threshold=autovacuum_vacuum_threshold,
            backup_hour=backup_hour,
            backup_minute=backup_minute,
            bgwriter_delay=bgwriter_delay,
            bgwriter_flush_after=bgwriter_flush_after,
            bgwriter_lru_maxpages=bgwriter_lru_maxpages,
            bgwriter_lru_multiplier=bgwriter_lru_multiplier,
            deadlock_timeout=deadlock_timeout,
            idle_in_transaction_session_timeout=idle_in_transaction_session_timeout,
            ip_filter=ip_filter,
            jit=jit,
            log_autovacuum_min_duration=log_autovacuum_min_duration,
            log_error_verbosity=log_error_verbosity,
            log_line_prefix=log_line_prefix,
            log_min_duration_statement=log_min_duration_statement,
            max_files_per_process=max_files_per_process,
            max_locks_per_transaction=max_locks_per_transaction,
            max_logical_replication_workers=max_logical_replication_workers,
            max_parallel_workers=max_parallel_workers,
            max_parallel_workers_per_gather=max_parallel_workers_per_gather,
            max_pred_locks_per_transaction=max_pred_locks_per_transaction,
            max_prepared_transactions=max_prepared_transactions,
            max_replication_slots=max_replication_slots,
            max_stack_depth=max_stack_depth,
            max_standby_archive_delay=max_standby_archive_delay,
            max_standby_streaming_delay=max_standby_streaming_delay,
            max_wal_senders=max_wal_senders,
            max_worker_processes=max_worker_processes,
            migration=migration,
            pgbouncer=pgbouncer,
            pglookout=pglookout,
            pg_partman_bgw_interval=pg_partman_bgw_interval,
            pg_partman_bgw_role=pg_partman_bgw_role,
            pg_read_replica=pg_read_replica,
            pg_service_to_fork_from=pg_service_to_fork_from,
            pg_stat_statements_track=pg_stat_statements_track,
            public_access=public_access,
            shared_buffers_percentage=shared_buffers_percentage,
            synchronous_replication=synchronous_replication,
            temp_file_limit=temp_file_limit,
            timescaledb=timescaledb,
            timezone=timezone,
            track_activity_query_size=track_activity_query_size,
            track_commit_timestamp=track_commit_timestamp,
            track_functions=track_functions,
            track_io_timing=track_io_timing,
            variant=variant,
            version=version,
            wal_sender_timeout=wal_sender_timeout,
            wal_writer_delay=wal_writer_delay,
            work_mem=work_mem,
        )

        return typing.cast(None, jsii.invoke(self, "putProperties", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceWindowDow")
    def reset_maintenance_window_dow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindowDow", []))

    @jsii.member(jsii_name="resetMaintenanceWindowTime")
    def reset_maintenance_window_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindowTime", []))

    @jsii.member(jsii_name="resetPowered")
    def reset_powered(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPowered", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(self) -> "ManagedDatabasePostgresqlComponentsList":
        return typing.cast("ManagedDatabasePostgresqlComponentsList", jsii.get(self, "components"))

    @builtins.property
    @jsii.member(jsii_name="nodeStates")
    def node_states(self) -> "ManagedDatabasePostgresqlNodeStatesList":
        return typing.cast("ManagedDatabasePostgresqlNodeStatesList", jsii.get(self, "nodeStates"))

    @builtins.property
    @jsii.member(jsii_name="primaryDatabase")
    def primary_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryDatabase"))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> "ManagedDatabasePostgresqlPropertiesOutputReference":
        return typing.cast("ManagedDatabasePostgresqlPropertiesOutputReference", jsii.get(self, "properties"))

    @builtins.property
    @jsii.member(jsii_name="serviceHost")
    def service_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceHost"))

    @builtins.property
    @jsii.member(jsii_name="servicePassword")
    def service_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePassword"))

    @builtins.property
    @jsii.member(jsii_name="servicePort")
    def service_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePort"))

    @builtins.property
    @jsii.member(jsii_name="serviceUri")
    def service_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUri"))

    @builtins.property
    @jsii.member(jsii_name="serviceUsername")
    def service_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUsername"))

    @builtins.property
    @jsii.member(jsii_name="sslmode")
    def sslmode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslmode"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDowInput")
    def maintenance_window_dow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowDowInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTimeInput")
    def maintenance_window_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="poweredInput")
    def powered_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "poweredInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlProperties"]:
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlProperties"], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDow")
    def maintenance_window_dow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowDow"))

    @maintenance_window_dow.setter
    def maintenance_window_dow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "maintenance_window_dow").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowDow", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTime")
    def maintenance_window_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowTime"))

    @maintenance_window_time.setter
    def maintenance_window_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "maintenance_window_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowTime", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="powered")
    def powered(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "powered"))

    @powered.setter
    def powered(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "powered").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "powered", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresql, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlComponents",
    jsii_struct_bases=[],
    name_mapping={},
)
class ManagedDatabasePostgresqlComponents:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlComponentsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlComponentsList",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlComponentsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedDatabasePostgresqlComponentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlComponentsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedDatabasePostgresqlComponentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlComponentsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlComponentsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlComponentsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ManagedDatabasePostgresqlComponentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlComponentsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlComponentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="route")
    def route(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "route"))

    @builtins.property
    @jsii.member(jsii_name="usage")
    def usage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usage"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabasePostgresqlComponents]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlComponents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlComponents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlComponentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlConfig",
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
        "plan": "plan",
        "zone": "zone",
        "id": "id",
        "maintenance_window_dow": "maintenanceWindowDow",
        "maintenance_window_time": "maintenanceWindowTime",
        "powered": "powered",
        "properties": "properties",
        "title": "title",
    },
)
class ManagedDatabasePostgresqlConfig(cdktf.TerraformMetaArguments):
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
        plan: builtins.str,
        zone: builtins.str,
        id: typing.Optional[builtins.str] = None,
        maintenance_window_dow: typing.Optional[builtins.str] = None,
        maintenance_window_time: typing.Optional[builtins.str] = None,
        powered: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        properties: typing.Optional[typing.Union["ManagedDatabasePostgresqlProperties", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the service. The name is used as a prefix for the logical hostname. Must be unique within an account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#name ManagedDatabasePostgresql#name}
        :param plan: Service plan to use. This determines how much resources the instance will have. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#plan ManagedDatabasePostgresql#plan}
        :param zone: Zone where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#zone ManagedDatabasePostgresql#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#id ManagedDatabasePostgresql#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window_dow: Maintenance window day of week. Lower case weekday name (monday, tuesday, ...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_dow ManagedDatabasePostgresql#maintenance_window_dow}
        :param maintenance_window_time: Maintenance window UTC time in hh:mm:ss format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_time ManagedDatabasePostgresql#maintenance_window_time}
        :param powered: The administrative power state of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#powered ManagedDatabasePostgresql#powered}
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#properties ManagedDatabasePostgresql#properties}
        :param title: Title of a managed database instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#title ManagedDatabasePostgresql#title}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(properties, dict):
            properties = ManagedDatabasePostgresqlProperties(**properties)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_window_dow", value=maintenance_window_dow, expected_type=type_hints["maintenance_window_dow"])
            check_type(argname="argument maintenance_window_time", value=maintenance_window_time, expected_type=type_hints["maintenance_window_time"])
            check_type(argname="argument powered", value=powered, expected_type=type_hints["powered"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "plan": plan,
            "zone": zone,
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
        if maintenance_window_dow is not None:
            self._values["maintenance_window_dow"] = maintenance_window_dow
        if maintenance_window_time is not None:
            self._values["maintenance_window_time"] = maintenance_window_time
        if powered is not None:
            self._values["powered"] = powered
        if properties is not None:
            self._values["properties"] = properties
        if title is not None:
            self._values["title"] = title

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
        '''Name of the service.

        The name is used as a prefix for the logical hostname. Must be unique within an account

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#name ManagedDatabasePostgresql#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plan(self) -> builtins.str:
        '''Service plan to use. This determines how much resources the instance will have.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#plan ManagedDatabasePostgresql#plan}
        '''
        result = self._values.get("plan")
        assert result is not None, "Required property 'plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''Zone where the instance resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#zone ManagedDatabasePostgresql#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#id ManagedDatabasePostgresql#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window_dow(self) -> typing.Optional[builtins.str]:
        '''Maintenance window day of week. Lower case weekday name (monday, tuesday, ...).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_dow ManagedDatabasePostgresql#maintenance_window_dow}
        '''
        result = self._values.get("maintenance_window_dow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window_time(self) -> typing.Optional[builtins.str]:
        '''Maintenance window UTC time in hh:mm:ss format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#maintenance_window_time ManagedDatabasePostgresql#maintenance_window_time}
        '''
        result = self._values.get("maintenance_window_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def powered(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The administrative power state of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#powered ManagedDatabasePostgresql#powered}
        '''
        result = self._values.get("powered")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def properties(self) -> typing.Optional["ManagedDatabasePostgresqlProperties"]:
        '''properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#properties ManagedDatabasePostgresql#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlProperties"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of a managed database instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#title ManagedDatabasePostgresql#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlNodeStates",
    jsii_struct_bases=[],
    name_mapping={},
)
class ManagedDatabasePostgresqlNodeStates:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlNodeStates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlNodeStatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlNodeStatesList",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlNodeStatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedDatabasePostgresqlNodeStatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlNodeStatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedDatabasePostgresqlNodeStatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlNodeStatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlNodeStatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlNodeStatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ManagedDatabasePostgresqlNodeStatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlNodeStatesOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlNodeStatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabasePostgresqlNodeStates]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlNodeStates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlNodeStates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlNodeStatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlProperties",
    jsii_struct_bases=[],
    name_mapping={
        "admin_password": "adminPassword",
        "admin_username": "adminUsername",
        "automatic_utility_network_ip_filter": "automaticUtilityNetworkIpFilter",
        "autovacuum_analyze_scale_factor": "autovacuumAnalyzeScaleFactor",
        "autovacuum_analyze_threshold": "autovacuumAnalyzeThreshold",
        "autovacuum_freeze_max_age": "autovacuumFreezeMaxAge",
        "autovacuum_max_workers": "autovacuumMaxWorkers",
        "autovacuum_naptime": "autovacuumNaptime",
        "autovacuum_vacuum_cost_delay": "autovacuumVacuumCostDelay",
        "autovacuum_vacuum_cost_limit": "autovacuumVacuumCostLimit",
        "autovacuum_vacuum_scale_factor": "autovacuumVacuumScaleFactor",
        "autovacuum_vacuum_threshold": "autovacuumVacuumThreshold",
        "backup_hour": "backupHour",
        "backup_minute": "backupMinute",
        "bgwriter_delay": "bgwriterDelay",
        "bgwriter_flush_after": "bgwriterFlushAfter",
        "bgwriter_lru_maxpages": "bgwriterLruMaxpages",
        "bgwriter_lru_multiplier": "bgwriterLruMultiplier",
        "deadlock_timeout": "deadlockTimeout",
        "idle_in_transaction_session_timeout": "idleInTransactionSessionTimeout",
        "ip_filter": "ipFilter",
        "jit": "jit",
        "log_autovacuum_min_duration": "logAutovacuumMinDuration",
        "log_error_verbosity": "logErrorVerbosity",
        "log_line_prefix": "logLinePrefix",
        "log_min_duration_statement": "logMinDurationStatement",
        "max_files_per_process": "maxFilesPerProcess",
        "max_locks_per_transaction": "maxLocksPerTransaction",
        "max_logical_replication_workers": "maxLogicalReplicationWorkers",
        "max_parallel_workers": "maxParallelWorkers",
        "max_parallel_workers_per_gather": "maxParallelWorkersPerGather",
        "max_pred_locks_per_transaction": "maxPredLocksPerTransaction",
        "max_prepared_transactions": "maxPreparedTransactions",
        "max_replication_slots": "maxReplicationSlots",
        "max_stack_depth": "maxStackDepth",
        "max_standby_archive_delay": "maxStandbyArchiveDelay",
        "max_standby_streaming_delay": "maxStandbyStreamingDelay",
        "max_wal_senders": "maxWalSenders",
        "max_worker_processes": "maxWorkerProcesses",
        "migration": "migration",
        "pgbouncer": "pgbouncer",
        "pglookout": "pglookout",
        "pg_partman_bgw_interval": "pgPartmanBgwInterval",
        "pg_partman_bgw_role": "pgPartmanBgwRole",
        "pg_read_replica": "pgReadReplica",
        "pg_service_to_fork_from": "pgServiceToForkFrom",
        "pg_stat_statements_track": "pgStatStatementsTrack",
        "public_access": "publicAccess",
        "shared_buffers_percentage": "sharedBuffersPercentage",
        "synchronous_replication": "synchronousReplication",
        "temp_file_limit": "tempFileLimit",
        "timescaledb": "timescaledb",
        "timezone": "timezone",
        "track_activity_query_size": "trackActivityQuerySize",
        "track_commit_timestamp": "trackCommitTimestamp",
        "track_functions": "trackFunctions",
        "track_io_timing": "trackIoTiming",
        "variant": "variant",
        "version": "version",
        "wal_sender_timeout": "walSenderTimeout",
        "wal_writer_delay": "walWriterDelay",
        "work_mem": "workMem",
    },
)
class ManagedDatabasePostgresqlProperties:
    def __init__(
        self,
        *,
        admin_password: typing.Optional[builtins.str] = None,
        admin_username: typing.Optional[builtins.str] = None,
        automatic_utility_network_ip_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autovacuum_analyze_scale_factor: typing.Optional[jsii.Number] = None,
        autovacuum_analyze_threshold: typing.Optional[jsii.Number] = None,
        autovacuum_freeze_max_age: typing.Optional[jsii.Number] = None,
        autovacuum_max_workers: typing.Optional[jsii.Number] = None,
        autovacuum_naptime: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_cost_delay: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_cost_limit: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_scale_factor: typing.Optional[jsii.Number] = None,
        autovacuum_vacuum_threshold: typing.Optional[jsii.Number] = None,
        backup_hour: typing.Optional[jsii.Number] = None,
        backup_minute: typing.Optional[jsii.Number] = None,
        bgwriter_delay: typing.Optional[jsii.Number] = None,
        bgwriter_flush_after: typing.Optional[jsii.Number] = None,
        bgwriter_lru_maxpages: typing.Optional[jsii.Number] = None,
        bgwriter_lru_multiplier: typing.Optional[jsii.Number] = None,
        deadlock_timeout: typing.Optional[jsii.Number] = None,
        idle_in_transaction_session_timeout: typing.Optional[jsii.Number] = None,
        ip_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        jit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_autovacuum_min_duration: typing.Optional[jsii.Number] = None,
        log_error_verbosity: typing.Optional[builtins.str] = None,
        log_line_prefix: typing.Optional[builtins.str] = None,
        log_min_duration_statement: typing.Optional[jsii.Number] = None,
        max_files_per_process: typing.Optional[jsii.Number] = None,
        max_locks_per_transaction: typing.Optional[jsii.Number] = None,
        max_logical_replication_workers: typing.Optional[jsii.Number] = None,
        max_parallel_workers: typing.Optional[jsii.Number] = None,
        max_parallel_workers_per_gather: typing.Optional[jsii.Number] = None,
        max_pred_locks_per_transaction: typing.Optional[jsii.Number] = None,
        max_prepared_transactions: typing.Optional[jsii.Number] = None,
        max_replication_slots: typing.Optional[jsii.Number] = None,
        max_stack_depth: typing.Optional[jsii.Number] = None,
        max_standby_archive_delay: typing.Optional[jsii.Number] = None,
        max_standby_streaming_delay: typing.Optional[jsii.Number] = None,
        max_wal_senders: typing.Optional[jsii.Number] = None,
        max_worker_processes: typing.Optional[jsii.Number] = None,
        migration: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesMigration", typing.Dict[str, typing.Any]]] = None,
        pgbouncer: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesPgbouncer", typing.Dict[str, typing.Any]]] = None,
        pglookout: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesPglookout", typing.Dict[str, typing.Any]]] = None,
        pg_partman_bgw_interval: typing.Optional[jsii.Number] = None,
        pg_partman_bgw_role: typing.Optional[builtins.str] = None,
        pg_read_replica: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pg_service_to_fork_from: typing.Optional[builtins.str] = None,
        pg_stat_statements_track: typing.Optional[builtins.str] = None,
        public_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shared_buffers_percentage: typing.Optional[jsii.Number] = None,
        synchronous_replication: typing.Optional[builtins.str] = None,
        temp_file_limit: typing.Optional[jsii.Number] = None,
        timescaledb: typing.Optional[typing.Union["ManagedDatabasePostgresqlPropertiesTimescaledb", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        track_activity_query_size: typing.Optional[jsii.Number] = None,
        track_commit_timestamp: typing.Optional[builtins.str] = None,
        track_functions: typing.Optional[builtins.str] = None,
        track_io_timing: typing.Optional[builtins.str] = None,
        variant: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        wal_sender_timeout: typing.Optional[jsii.Number] = None,
        wal_writer_delay: typing.Optional[jsii.Number] = None,
        work_mem: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param admin_password: Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_password ManagedDatabasePostgresql#admin_password}
        :param admin_username: Custom username for admin user. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_username ManagedDatabasePostgresql#admin_username}
        :param automatic_utility_network_ip_filter: Automatic utility network IP Filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#automatic_utility_network_ip_filter ManagedDatabasePostgresql#automatic_utility_network_ip_filter}
        :param autovacuum_analyze_scale_factor: autovacuum_analyze_scale_factor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_scale_factor ManagedDatabasePostgresql#autovacuum_analyze_scale_factor}
        :param autovacuum_analyze_threshold: autovacuum_analyze_threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_threshold ManagedDatabasePostgresql#autovacuum_analyze_threshold}
        :param autovacuum_freeze_max_age: autovacuum_freeze_max_age. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_freeze_max_age ManagedDatabasePostgresql#autovacuum_freeze_max_age}
        :param autovacuum_max_workers: autovacuum_max_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_max_workers ManagedDatabasePostgresql#autovacuum_max_workers}
        :param autovacuum_naptime: autovacuum_naptime. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_naptime ManagedDatabasePostgresql#autovacuum_naptime}
        :param autovacuum_vacuum_cost_delay: autovacuum_vacuum_cost_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_delay ManagedDatabasePostgresql#autovacuum_vacuum_cost_delay}
        :param autovacuum_vacuum_cost_limit: autovacuum_vacuum_cost_limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_limit ManagedDatabasePostgresql#autovacuum_vacuum_cost_limit}
        :param autovacuum_vacuum_scale_factor: autovacuum_vacuum_scale_factor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_scale_factor ManagedDatabasePostgresql#autovacuum_vacuum_scale_factor}
        :param autovacuum_vacuum_threshold: autovacuum_vacuum_threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_threshold ManagedDatabasePostgresql#autovacuum_vacuum_threshold}
        :param backup_hour: The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_hour ManagedDatabasePostgresql#backup_hour}
        :param backup_minute: The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_minute ManagedDatabasePostgresql#backup_minute}
        :param bgwriter_delay: bgwriter_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_delay ManagedDatabasePostgresql#bgwriter_delay}
        :param bgwriter_flush_after: bgwriter_flush_after. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_flush_after ManagedDatabasePostgresql#bgwriter_flush_after}
        :param bgwriter_lru_maxpages: bgwriter_lru_maxpages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_maxpages ManagedDatabasePostgresql#bgwriter_lru_maxpages}
        :param bgwriter_lru_multiplier: bgwriter_lru_multiplier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_multiplier ManagedDatabasePostgresql#bgwriter_lru_multiplier}
        :param deadlock_timeout: deadlock_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#deadlock_timeout ManagedDatabasePostgresql#deadlock_timeout}
        :param idle_in_transaction_session_timeout: idle_in_transaction_session_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#idle_in_transaction_session_timeout ManagedDatabasePostgresql#idle_in_transaction_session_timeout}
        :param ip_filter: IP filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ip_filter ManagedDatabasePostgresql#ip_filter}
        :param jit: jit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#jit ManagedDatabasePostgresql#jit}
        :param log_autovacuum_min_duration: log_autovacuum_min_duration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_autovacuum_min_duration ManagedDatabasePostgresql#log_autovacuum_min_duration}
        :param log_error_verbosity: log_error_verbosity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_error_verbosity ManagedDatabasePostgresql#log_error_verbosity}
        :param log_line_prefix: log_line_prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_line_prefix ManagedDatabasePostgresql#log_line_prefix}
        :param log_min_duration_statement: log_min_duration_statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_min_duration_statement ManagedDatabasePostgresql#log_min_duration_statement}
        :param max_files_per_process: max_files_per_process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_files_per_process ManagedDatabasePostgresql#max_files_per_process}
        :param max_locks_per_transaction: max_locks_per_transaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_locks_per_transaction ManagedDatabasePostgresql#max_locks_per_transaction}
        :param max_logical_replication_workers: max_logical_replication_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_logical_replication_workers ManagedDatabasePostgresql#max_logical_replication_workers}
        :param max_parallel_workers: max_parallel_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers ManagedDatabasePostgresql#max_parallel_workers}
        :param max_parallel_workers_per_gather: max_parallel_workers_per_gather. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers_per_gather ManagedDatabasePostgresql#max_parallel_workers_per_gather}
        :param max_pred_locks_per_transaction: max_pred_locks_per_transaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_pred_locks_per_transaction ManagedDatabasePostgresql#max_pred_locks_per_transaction}
        :param max_prepared_transactions: max_prepared_transactions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_prepared_transactions ManagedDatabasePostgresql#max_prepared_transactions}
        :param max_replication_slots: max_replication_slots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_replication_slots ManagedDatabasePostgresql#max_replication_slots}
        :param max_stack_depth: max_stack_depth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_stack_depth ManagedDatabasePostgresql#max_stack_depth}
        :param max_standby_archive_delay: max_standby_archive_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_archive_delay ManagedDatabasePostgresql#max_standby_archive_delay}
        :param max_standby_streaming_delay: max_standby_streaming_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_streaming_delay ManagedDatabasePostgresql#max_standby_streaming_delay}
        :param max_wal_senders: max_wal_senders. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_wal_senders ManagedDatabasePostgresql#max_wal_senders}
        :param max_worker_processes: max_worker_processes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_worker_processes ManagedDatabasePostgresql#max_worker_processes}
        :param migration: migration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#migration ManagedDatabasePostgresql#migration}
        :param pgbouncer: pgbouncer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pgbouncer ManagedDatabasePostgresql#pgbouncer}
        :param pglookout: pglookout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pglookout ManagedDatabasePostgresql#pglookout}
        :param pg_partman_bgw_interval: pg_partman_bgw.interval. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_interval ManagedDatabasePostgresql#pg_partman_bgw_interval}
        :param pg_partman_bgw_role: pg_partman_bgw.role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_role ManagedDatabasePostgresql#pg_partman_bgw_role}
        :param pg_read_replica: Should the service which is being forked be a read replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_read_replica ManagedDatabasePostgresql#pg_read_replica}
        :param pg_service_to_fork_from: Name of the PG Service from which to fork (deprecated, use service_to_fork_from). This has effect only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_service_to_fork_from ManagedDatabasePostgresql#pg_service_to_fork_from}
        :param pg_stat_statements_track: pg_stat_statements.track. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_stat_statements_track ManagedDatabasePostgresql#pg_stat_statements_track}
        :param public_access: Public Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#public_access ManagedDatabasePostgresql#public_access}
        :param shared_buffers_percentage: shared_buffers_percentage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#shared_buffers_percentage ManagedDatabasePostgresql#shared_buffers_percentage}
        :param synchronous_replication: Synchronous replication type. Note that the service plan also needs to support synchronous replication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#synchronous_replication ManagedDatabasePostgresql#synchronous_replication}
        :param temp_file_limit: temp_file_limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#temp_file_limit ManagedDatabasePostgresql#temp_file_limit}
        :param timescaledb: timescaledb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timescaledb ManagedDatabasePostgresql#timescaledb}
        :param timezone: timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timezone ManagedDatabasePostgresql#timezone}
        :param track_activity_query_size: track_activity_query_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_activity_query_size ManagedDatabasePostgresql#track_activity_query_size}
        :param track_commit_timestamp: track_commit_timestamp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_commit_timestamp ManagedDatabasePostgresql#track_commit_timestamp}
        :param track_functions: track_functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_functions ManagedDatabasePostgresql#track_functions}
        :param track_io_timing: track_io_timing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_io_timing ManagedDatabasePostgresql#track_io_timing}
        :param variant: Variant of the PostgreSQL service, may affect the features that are exposed by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#variant ManagedDatabasePostgresql#variant}
        :param version: PostgreSQL major version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#version ManagedDatabasePostgresql#version}
        :param wal_sender_timeout: wal_sender_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_sender_timeout ManagedDatabasePostgresql#wal_sender_timeout}
        :param wal_writer_delay: wal_writer_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_writer_delay ManagedDatabasePostgresql#wal_writer_delay}
        :param work_mem: work_mem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#work_mem ManagedDatabasePostgresql#work_mem}
        '''
        if isinstance(migration, dict):
            migration = ManagedDatabasePostgresqlPropertiesMigration(**migration)
        if isinstance(pgbouncer, dict):
            pgbouncer = ManagedDatabasePostgresqlPropertiesPgbouncer(**pgbouncer)
        if isinstance(pglookout, dict):
            pglookout = ManagedDatabasePostgresqlPropertiesPglookout(**pglookout)
        if isinstance(timescaledb, dict):
            timescaledb = ManagedDatabasePostgresqlPropertiesTimescaledb(**timescaledb)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlProperties.__init__)
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument automatic_utility_network_ip_filter", value=automatic_utility_network_ip_filter, expected_type=type_hints["automatic_utility_network_ip_filter"])
            check_type(argname="argument autovacuum_analyze_scale_factor", value=autovacuum_analyze_scale_factor, expected_type=type_hints["autovacuum_analyze_scale_factor"])
            check_type(argname="argument autovacuum_analyze_threshold", value=autovacuum_analyze_threshold, expected_type=type_hints["autovacuum_analyze_threshold"])
            check_type(argname="argument autovacuum_freeze_max_age", value=autovacuum_freeze_max_age, expected_type=type_hints["autovacuum_freeze_max_age"])
            check_type(argname="argument autovacuum_max_workers", value=autovacuum_max_workers, expected_type=type_hints["autovacuum_max_workers"])
            check_type(argname="argument autovacuum_naptime", value=autovacuum_naptime, expected_type=type_hints["autovacuum_naptime"])
            check_type(argname="argument autovacuum_vacuum_cost_delay", value=autovacuum_vacuum_cost_delay, expected_type=type_hints["autovacuum_vacuum_cost_delay"])
            check_type(argname="argument autovacuum_vacuum_cost_limit", value=autovacuum_vacuum_cost_limit, expected_type=type_hints["autovacuum_vacuum_cost_limit"])
            check_type(argname="argument autovacuum_vacuum_scale_factor", value=autovacuum_vacuum_scale_factor, expected_type=type_hints["autovacuum_vacuum_scale_factor"])
            check_type(argname="argument autovacuum_vacuum_threshold", value=autovacuum_vacuum_threshold, expected_type=type_hints["autovacuum_vacuum_threshold"])
            check_type(argname="argument backup_hour", value=backup_hour, expected_type=type_hints["backup_hour"])
            check_type(argname="argument backup_minute", value=backup_minute, expected_type=type_hints["backup_minute"])
            check_type(argname="argument bgwriter_delay", value=bgwriter_delay, expected_type=type_hints["bgwriter_delay"])
            check_type(argname="argument bgwriter_flush_after", value=bgwriter_flush_after, expected_type=type_hints["bgwriter_flush_after"])
            check_type(argname="argument bgwriter_lru_maxpages", value=bgwriter_lru_maxpages, expected_type=type_hints["bgwriter_lru_maxpages"])
            check_type(argname="argument bgwriter_lru_multiplier", value=bgwriter_lru_multiplier, expected_type=type_hints["bgwriter_lru_multiplier"])
            check_type(argname="argument deadlock_timeout", value=deadlock_timeout, expected_type=type_hints["deadlock_timeout"])
            check_type(argname="argument idle_in_transaction_session_timeout", value=idle_in_transaction_session_timeout, expected_type=type_hints["idle_in_transaction_session_timeout"])
            check_type(argname="argument ip_filter", value=ip_filter, expected_type=type_hints["ip_filter"])
            check_type(argname="argument jit", value=jit, expected_type=type_hints["jit"])
            check_type(argname="argument log_autovacuum_min_duration", value=log_autovacuum_min_duration, expected_type=type_hints["log_autovacuum_min_duration"])
            check_type(argname="argument log_error_verbosity", value=log_error_verbosity, expected_type=type_hints["log_error_verbosity"])
            check_type(argname="argument log_line_prefix", value=log_line_prefix, expected_type=type_hints["log_line_prefix"])
            check_type(argname="argument log_min_duration_statement", value=log_min_duration_statement, expected_type=type_hints["log_min_duration_statement"])
            check_type(argname="argument max_files_per_process", value=max_files_per_process, expected_type=type_hints["max_files_per_process"])
            check_type(argname="argument max_locks_per_transaction", value=max_locks_per_transaction, expected_type=type_hints["max_locks_per_transaction"])
            check_type(argname="argument max_logical_replication_workers", value=max_logical_replication_workers, expected_type=type_hints["max_logical_replication_workers"])
            check_type(argname="argument max_parallel_workers", value=max_parallel_workers, expected_type=type_hints["max_parallel_workers"])
            check_type(argname="argument max_parallel_workers_per_gather", value=max_parallel_workers_per_gather, expected_type=type_hints["max_parallel_workers_per_gather"])
            check_type(argname="argument max_pred_locks_per_transaction", value=max_pred_locks_per_transaction, expected_type=type_hints["max_pred_locks_per_transaction"])
            check_type(argname="argument max_prepared_transactions", value=max_prepared_transactions, expected_type=type_hints["max_prepared_transactions"])
            check_type(argname="argument max_replication_slots", value=max_replication_slots, expected_type=type_hints["max_replication_slots"])
            check_type(argname="argument max_stack_depth", value=max_stack_depth, expected_type=type_hints["max_stack_depth"])
            check_type(argname="argument max_standby_archive_delay", value=max_standby_archive_delay, expected_type=type_hints["max_standby_archive_delay"])
            check_type(argname="argument max_standby_streaming_delay", value=max_standby_streaming_delay, expected_type=type_hints["max_standby_streaming_delay"])
            check_type(argname="argument max_wal_senders", value=max_wal_senders, expected_type=type_hints["max_wal_senders"])
            check_type(argname="argument max_worker_processes", value=max_worker_processes, expected_type=type_hints["max_worker_processes"])
            check_type(argname="argument migration", value=migration, expected_type=type_hints["migration"])
            check_type(argname="argument pgbouncer", value=pgbouncer, expected_type=type_hints["pgbouncer"])
            check_type(argname="argument pglookout", value=pglookout, expected_type=type_hints["pglookout"])
            check_type(argname="argument pg_partman_bgw_interval", value=pg_partman_bgw_interval, expected_type=type_hints["pg_partman_bgw_interval"])
            check_type(argname="argument pg_partman_bgw_role", value=pg_partman_bgw_role, expected_type=type_hints["pg_partman_bgw_role"])
            check_type(argname="argument pg_read_replica", value=pg_read_replica, expected_type=type_hints["pg_read_replica"])
            check_type(argname="argument pg_service_to_fork_from", value=pg_service_to_fork_from, expected_type=type_hints["pg_service_to_fork_from"])
            check_type(argname="argument pg_stat_statements_track", value=pg_stat_statements_track, expected_type=type_hints["pg_stat_statements_track"])
            check_type(argname="argument public_access", value=public_access, expected_type=type_hints["public_access"])
            check_type(argname="argument shared_buffers_percentage", value=shared_buffers_percentage, expected_type=type_hints["shared_buffers_percentage"])
            check_type(argname="argument synchronous_replication", value=synchronous_replication, expected_type=type_hints["synchronous_replication"])
            check_type(argname="argument temp_file_limit", value=temp_file_limit, expected_type=type_hints["temp_file_limit"])
            check_type(argname="argument timescaledb", value=timescaledb, expected_type=type_hints["timescaledb"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument track_activity_query_size", value=track_activity_query_size, expected_type=type_hints["track_activity_query_size"])
            check_type(argname="argument track_commit_timestamp", value=track_commit_timestamp, expected_type=type_hints["track_commit_timestamp"])
            check_type(argname="argument track_functions", value=track_functions, expected_type=type_hints["track_functions"])
            check_type(argname="argument track_io_timing", value=track_io_timing, expected_type=type_hints["track_io_timing"])
            check_type(argname="argument variant", value=variant, expected_type=type_hints["variant"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument wal_sender_timeout", value=wal_sender_timeout, expected_type=type_hints["wal_sender_timeout"])
            check_type(argname="argument wal_writer_delay", value=wal_writer_delay, expected_type=type_hints["wal_writer_delay"])
            check_type(argname="argument work_mem", value=work_mem, expected_type=type_hints["work_mem"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_username is not None:
            self._values["admin_username"] = admin_username
        if automatic_utility_network_ip_filter is not None:
            self._values["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if autovacuum_analyze_scale_factor is not None:
            self._values["autovacuum_analyze_scale_factor"] = autovacuum_analyze_scale_factor
        if autovacuum_analyze_threshold is not None:
            self._values["autovacuum_analyze_threshold"] = autovacuum_analyze_threshold
        if autovacuum_freeze_max_age is not None:
            self._values["autovacuum_freeze_max_age"] = autovacuum_freeze_max_age
        if autovacuum_max_workers is not None:
            self._values["autovacuum_max_workers"] = autovacuum_max_workers
        if autovacuum_naptime is not None:
            self._values["autovacuum_naptime"] = autovacuum_naptime
        if autovacuum_vacuum_cost_delay is not None:
            self._values["autovacuum_vacuum_cost_delay"] = autovacuum_vacuum_cost_delay
        if autovacuum_vacuum_cost_limit is not None:
            self._values["autovacuum_vacuum_cost_limit"] = autovacuum_vacuum_cost_limit
        if autovacuum_vacuum_scale_factor is not None:
            self._values["autovacuum_vacuum_scale_factor"] = autovacuum_vacuum_scale_factor
        if autovacuum_vacuum_threshold is not None:
            self._values["autovacuum_vacuum_threshold"] = autovacuum_vacuum_threshold
        if backup_hour is not None:
            self._values["backup_hour"] = backup_hour
        if backup_minute is not None:
            self._values["backup_minute"] = backup_minute
        if bgwriter_delay is not None:
            self._values["bgwriter_delay"] = bgwriter_delay
        if bgwriter_flush_after is not None:
            self._values["bgwriter_flush_after"] = bgwriter_flush_after
        if bgwriter_lru_maxpages is not None:
            self._values["bgwriter_lru_maxpages"] = bgwriter_lru_maxpages
        if bgwriter_lru_multiplier is not None:
            self._values["bgwriter_lru_multiplier"] = bgwriter_lru_multiplier
        if deadlock_timeout is not None:
            self._values["deadlock_timeout"] = deadlock_timeout
        if idle_in_transaction_session_timeout is not None:
            self._values["idle_in_transaction_session_timeout"] = idle_in_transaction_session_timeout
        if ip_filter is not None:
            self._values["ip_filter"] = ip_filter
        if jit is not None:
            self._values["jit"] = jit
        if log_autovacuum_min_duration is not None:
            self._values["log_autovacuum_min_duration"] = log_autovacuum_min_duration
        if log_error_verbosity is not None:
            self._values["log_error_verbosity"] = log_error_verbosity
        if log_line_prefix is not None:
            self._values["log_line_prefix"] = log_line_prefix
        if log_min_duration_statement is not None:
            self._values["log_min_duration_statement"] = log_min_duration_statement
        if max_files_per_process is not None:
            self._values["max_files_per_process"] = max_files_per_process
        if max_locks_per_transaction is not None:
            self._values["max_locks_per_transaction"] = max_locks_per_transaction
        if max_logical_replication_workers is not None:
            self._values["max_logical_replication_workers"] = max_logical_replication_workers
        if max_parallel_workers is not None:
            self._values["max_parallel_workers"] = max_parallel_workers
        if max_parallel_workers_per_gather is not None:
            self._values["max_parallel_workers_per_gather"] = max_parallel_workers_per_gather
        if max_pred_locks_per_transaction is not None:
            self._values["max_pred_locks_per_transaction"] = max_pred_locks_per_transaction
        if max_prepared_transactions is not None:
            self._values["max_prepared_transactions"] = max_prepared_transactions
        if max_replication_slots is not None:
            self._values["max_replication_slots"] = max_replication_slots
        if max_stack_depth is not None:
            self._values["max_stack_depth"] = max_stack_depth
        if max_standby_archive_delay is not None:
            self._values["max_standby_archive_delay"] = max_standby_archive_delay
        if max_standby_streaming_delay is not None:
            self._values["max_standby_streaming_delay"] = max_standby_streaming_delay
        if max_wal_senders is not None:
            self._values["max_wal_senders"] = max_wal_senders
        if max_worker_processes is not None:
            self._values["max_worker_processes"] = max_worker_processes
        if migration is not None:
            self._values["migration"] = migration
        if pgbouncer is not None:
            self._values["pgbouncer"] = pgbouncer
        if pglookout is not None:
            self._values["pglookout"] = pglookout
        if pg_partman_bgw_interval is not None:
            self._values["pg_partman_bgw_interval"] = pg_partman_bgw_interval
        if pg_partman_bgw_role is not None:
            self._values["pg_partman_bgw_role"] = pg_partman_bgw_role
        if pg_read_replica is not None:
            self._values["pg_read_replica"] = pg_read_replica
        if pg_service_to_fork_from is not None:
            self._values["pg_service_to_fork_from"] = pg_service_to_fork_from
        if pg_stat_statements_track is not None:
            self._values["pg_stat_statements_track"] = pg_stat_statements_track
        if public_access is not None:
            self._values["public_access"] = public_access
        if shared_buffers_percentage is not None:
            self._values["shared_buffers_percentage"] = shared_buffers_percentage
        if synchronous_replication is not None:
            self._values["synchronous_replication"] = synchronous_replication
        if temp_file_limit is not None:
            self._values["temp_file_limit"] = temp_file_limit
        if timescaledb is not None:
            self._values["timescaledb"] = timescaledb
        if timezone is not None:
            self._values["timezone"] = timezone
        if track_activity_query_size is not None:
            self._values["track_activity_query_size"] = track_activity_query_size
        if track_commit_timestamp is not None:
            self._values["track_commit_timestamp"] = track_commit_timestamp
        if track_functions is not None:
            self._values["track_functions"] = track_functions
        if track_io_timing is not None:
            self._values["track_io_timing"] = track_io_timing
        if variant is not None:
            self._values["variant"] = variant
        if version is not None:
            self._values["version"] = version
        if wal_sender_timeout is not None:
            self._values["wal_sender_timeout"] = wal_sender_timeout
        if wal_writer_delay is not None:
            self._values["wal_writer_delay"] = wal_writer_delay
        if work_mem is not None:
            self._values["work_mem"] = work_mem

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Custom password for admin user.

        Defaults to random string. This must be set only when a new service is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_password ManagedDatabasePostgresql#admin_password}
        '''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''Custom username for admin user. This must be set only when a new service is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#admin_username ManagedDatabasePostgresql#admin_username}
        '''
        result = self._values.get("admin_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_utility_network_ip_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Automatic utility network IP Filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#automatic_utility_network_ip_filter ManagedDatabasePostgresql#automatic_utility_network_ip_filter}
        '''
        result = self._values.get("automatic_utility_network_ip_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autovacuum_analyze_scale_factor(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_analyze_scale_factor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_scale_factor ManagedDatabasePostgresql#autovacuum_analyze_scale_factor}
        '''
        result = self._values.get("autovacuum_analyze_scale_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_analyze_threshold(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_analyze_threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_analyze_threshold ManagedDatabasePostgresql#autovacuum_analyze_threshold}
        '''
        result = self._values.get("autovacuum_analyze_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_freeze_max_age(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_freeze_max_age.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_freeze_max_age ManagedDatabasePostgresql#autovacuum_freeze_max_age}
        '''
        result = self._values.get("autovacuum_freeze_max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_max_workers(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_max_workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_max_workers ManagedDatabasePostgresql#autovacuum_max_workers}
        '''
        result = self._values.get("autovacuum_max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_naptime(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_naptime.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_naptime ManagedDatabasePostgresql#autovacuum_naptime}
        '''
        result = self._values.get("autovacuum_naptime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_vacuum_cost_delay(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_vacuum_cost_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_delay ManagedDatabasePostgresql#autovacuum_vacuum_cost_delay}
        '''
        result = self._values.get("autovacuum_vacuum_cost_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_vacuum_cost_limit(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_vacuum_cost_limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_cost_limit ManagedDatabasePostgresql#autovacuum_vacuum_cost_limit}
        '''
        result = self._values.get("autovacuum_vacuum_cost_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_vacuum_scale_factor(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_vacuum_scale_factor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_scale_factor ManagedDatabasePostgresql#autovacuum_vacuum_scale_factor}
        '''
        result = self._values.get("autovacuum_vacuum_scale_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autovacuum_vacuum_threshold(self) -> typing.Optional[jsii.Number]:
        '''autovacuum_vacuum_threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autovacuum_vacuum_threshold ManagedDatabasePostgresql#autovacuum_vacuum_threshold}
        '''
        result = self._values.get("autovacuum_vacuum_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_hour(self) -> typing.Optional[jsii.Number]:
        '''The hour of day (in UTC) when backup for the service is started.

        New backup is only started if previous backup has already completed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_hour ManagedDatabasePostgresql#backup_hour}
        '''
        result = self._values.get("backup_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_minute(self) -> typing.Optional[jsii.Number]:
        '''The minute of an hour when backup for the service is started.

        New backup is only started if previous backup has already completed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#backup_minute ManagedDatabasePostgresql#backup_minute}
        '''
        result = self._values.get("backup_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bgwriter_delay(self) -> typing.Optional[jsii.Number]:
        '''bgwriter_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_delay ManagedDatabasePostgresql#bgwriter_delay}
        '''
        result = self._values.get("bgwriter_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bgwriter_flush_after(self) -> typing.Optional[jsii.Number]:
        '''bgwriter_flush_after.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_flush_after ManagedDatabasePostgresql#bgwriter_flush_after}
        '''
        result = self._values.get("bgwriter_flush_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bgwriter_lru_maxpages(self) -> typing.Optional[jsii.Number]:
        '''bgwriter_lru_maxpages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_maxpages ManagedDatabasePostgresql#bgwriter_lru_maxpages}
        '''
        result = self._values.get("bgwriter_lru_maxpages")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bgwriter_lru_multiplier(self) -> typing.Optional[jsii.Number]:
        '''bgwriter_lru_multiplier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#bgwriter_lru_multiplier ManagedDatabasePostgresql#bgwriter_lru_multiplier}
        '''
        result = self._values.get("bgwriter_lru_multiplier")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deadlock_timeout(self) -> typing.Optional[jsii.Number]:
        '''deadlock_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#deadlock_timeout ManagedDatabasePostgresql#deadlock_timeout}
        '''
        result = self._values.get("deadlock_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_in_transaction_session_timeout(self) -> typing.Optional[jsii.Number]:
        '''idle_in_transaction_session_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#idle_in_transaction_session_timeout ManagedDatabasePostgresql#idle_in_transaction_session_timeout}
        '''
        result = self._values.get("idle_in_transaction_session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip_filter(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IP filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ip_filter ManagedDatabasePostgresql#ip_filter}
        '''
        result = self._values.get("ip_filter")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jit(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''jit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#jit ManagedDatabasePostgresql#jit}
        '''
        result = self._values.get("jit")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_autovacuum_min_duration(self) -> typing.Optional[jsii.Number]:
        '''log_autovacuum_min_duration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_autovacuum_min_duration ManagedDatabasePostgresql#log_autovacuum_min_duration}
        '''
        result = self._values.get("log_autovacuum_min_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def log_error_verbosity(self) -> typing.Optional[builtins.str]:
        '''log_error_verbosity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_error_verbosity ManagedDatabasePostgresql#log_error_verbosity}
        '''
        result = self._values.get("log_error_verbosity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_line_prefix(self) -> typing.Optional[builtins.str]:
        '''log_line_prefix.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_line_prefix ManagedDatabasePostgresql#log_line_prefix}
        '''
        result = self._values.get("log_line_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_min_duration_statement(self) -> typing.Optional[jsii.Number]:
        '''log_min_duration_statement.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#log_min_duration_statement ManagedDatabasePostgresql#log_min_duration_statement}
        '''
        result = self._values.get("log_min_duration_statement")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_files_per_process(self) -> typing.Optional[jsii.Number]:
        '''max_files_per_process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_files_per_process ManagedDatabasePostgresql#max_files_per_process}
        '''
        result = self._values.get("max_files_per_process")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_locks_per_transaction(self) -> typing.Optional[jsii.Number]:
        '''max_locks_per_transaction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_locks_per_transaction ManagedDatabasePostgresql#max_locks_per_transaction}
        '''
        result = self._values.get("max_locks_per_transaction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_logical_replication_workers(self) -> typing.Optional[jsii.Number]:
        '''max_logical_replication_workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_logical_replication_workers ManagedDatabasePostgresql#max_logical_replication_workers}
        '''
        result = self._values.get("max_logical_replication_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_parallel_workers(self) -> typing.Optional[jsii.Number]:
        '''max_parallel_workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers ManagedDatabasePostgresql#max_parallel_workers}
        '''
        result = self._values.get("max_parallel_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_parallel_workers_per_gather(self) -> typing.Optional[jsii.Number]:
        '''max_parallel_workers_per_gather.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_parallel_workers_per_gather ManagedDatabasePostgresql#max_parallel_workers_per_gather}
        '''
        result = self._values.get("max_parallel_workers_per_gather")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_pred_locks_per_transaction(self) -> typing.Optional[jsii.Number]:
        '''max_pred_locks_per_transaction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_pred_locks_per_transaction ManagedDatabasePostgresql#max_pred_locks_per_transaction}
        '''
        result = self._values.get("max_pred_locks_per_transaction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_prepared_transactions(self) -> typing.Optional[jsii.Number]:
        '''max_prepared_transactions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_prepared_transactions ManagedDatabasePostgresql#max_prepared_transactions}
        '''
        result = self._values.get("max_prepared_transactions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_replication_slots(self) -> typing.Optional[jsii.Number]:
        '''max_replication_slots.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_replication_slots ManagedDatabasePostgresql#max_replication_slots}
        '''
        result = self._values.get("max_replication_slots")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_stack_depth(self) -> typing.Optional[jsii.Number]:
        '''max_stack_depth.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_stack_depth ManagedDatabasePostgresql#max_stack_depth}
        '''
        result = self._values.get("max_stack_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_standby_archive_delay(self) -> typing.Optional[jsii.Number]:
        '''max_standby_archive_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_archive_delay ManagedDatabasePostgresql#max_standby_archive_delay}
        '''
        result = self._values.get("max_standby_archive_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_standby_streaming_delay(self) -> typing.Optional[jsii.Number]:
        '''max_standby_streaming_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_standby_streaming_delay ManagedDatabasePostgresql#max_standby_streaming_delay}
        '''
        result = self._values.get("max_standby_streaming_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_wal_senders(self) -> typing.Optional[jsii.Number]:
        '''max_wal_senders.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_wal_senders ManagedDatabasePostgresql#max_wal_senders}
        '''
        result = self._values.get("max_wal_senders")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_worker_processes(self) -> typing.Optional[jsii.Number]:
        '''max_worker_processes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_worker_processes ManagedDatabasePostgresql#max_worker_processes}
        '''
        result = self._values.get("max_worker_processes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def migration(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesMigration"]:
        '''migration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#migration ManagedDatabasePostgresql#migration}
        '''
        result = self._values.get("migration")
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesMigration"], result)

    @builtins.property
    def pgbouncer(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesPgbouncer"]:
        '''pgbouncer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pgbouncer ManagedDatabasePostgresql#pgbouncer}
        '''
        result = self._values.get("pgbouncer")
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesPgbouncer"], result)

    @builtins.property
    def pglookout(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesPglookout"]:
        '''pglookout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pglookout ManagedDatabasePostgresql#pglookout}
        '''
        result = self._values.get("pglookout")
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesPglookout"], result)

    @builtins.property
    def pg_partman_bgw_interval(self) -> typing.Optional[jsii.Number]:
        '''pg_partman_bgw.interval.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_interval ManagedDatabasePostgresql#pg_partman_bgw_interval}
        '''
        result = self._values.get("pg_partman_bgw_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pg_partman_bgw_role(self) -> typing.Optional[builtins.str]:
        '''pg_partman_bgw.role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_partman_bgw_role ManagedDatabasePostgresql#pg_partman_bgw_role}
        '''
        result = self._values.get("pg_partman_bgw_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pg_read_replica(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the service which is being forked be a read replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_read_replica ManagedDatabasePostgresql#pg_read_replica}
        '''
        result = self._values.get("pg_read_replica")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pg_service_to_fork_from(self) -> typing.Optional[builtins.str]:
        '''Name of the PG Service from which to fork (deprecated, use service_to_fork_from).

        This has effect only when a new service is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_service_to_fork_from ManagedDatabasePostgresql#pg_service_to_fork_from}
        '''
        result = self._values.get("pg_service_to_fork_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pg_stat_statements_track(self) -> typing.Optional[builtins.str]:
        '''pg_stat_statements.track.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#pg_stat_statements_track ManagedDatabasePostgresql#pg_stat_statements_track}
        '''
        result = self._values.get("pg_stat_statements_track")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Public Access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#public_access ManagedDatabasePostgresql#public_access}
        '''
        result = self._values.get("public_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def shared_buffers_percentage(self) -> typing.Optional[jsii.Number]:
        '''shared_buffers_percentage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#shared_buffers_percentage ManagedDatabasePostgresql#shared_buffers_percentage}
        '''
        result = self._values.get("shared_buffers_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def synchronous_replication(self) -> typing.Optional[builtins.str]:
        '''Synchronous replication type. Note that the service plan also needs to support synchronous replication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#synchronous_replication ManagedDatabasePostgresql#synchronous_replication}
        '''
        result = self._values.get("synchronous_replication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temp_file_limit(self) -> typing.Optional[jsii.Number]:
        '''temp_file_limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#temp_file_limit ManagedDatabasePostgresql#temp_file_limit}
        '''
        result = self._values.get("temp_file_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timescaledb(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesTimescaledb"]:
        '''timescaledb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timescaledb ManagedDatabasePostgresql#timescaledb}
        '''
        result = self._values.get("timescaledb")
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesTimescaledb"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#timezone ManagedDatabasePostgresql#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def track_activity_query_size(self) -> typing.Optional[jsii.Number]:
        '''track_activity_query_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_activity_query_size ManagedDatabasePostgresql#track_activity_query_size}
        '''
        result = self._values.get("track_activity_query_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def track_commit_timestamp(self) -> typing.Optional[builtins.str]:
        '''track_commit_timestamp.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_commit_timestamp ManagedDatabasePostgresql#track_commit_timestamp}
        '''
        result = self._values.get("track_commit_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def track_functions(self) -> typing.Optional[builtins.str]:
        '''track_functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_functions ManagedDatabasePostgresql#track_functions}
        '''
        result = self._values.get("track_functions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def track_io_timing(self) -> typing.Optional[builtins.str]:
        '''track_io_timing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#track_io_timing ManagedDatabasePostgresql#track_io_timing}
        '''
        result = self._values.get("track_io_timing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variant(self) -> typing.Optional[builtins.str]:
        '''Variant of the PostgreSQL service, may affect the features that are exposed by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#variant ManagedDatabasePostgresql#variant}
        '''
        result = self._values.get("variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''PostgreSQL major version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#version ManagedDatabasePostgresql#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wal_sender_timeout(self) -> typing.Optional[jsii.Number]:
        '''wal_sender_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_sender_timeout ManagedDatabasePostgresql#wal_sender_timeout}
        '''
        result = self._values.get("wal_sender_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wal_writer_delay(self) -> typing.Optional[jsii.Number]:
        '''wal_writer_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#wal_writer_delay ManagedDatabasePostgresql#wal_writer_delay}
        '''
        result = self._values.get("wal_writer_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def work_mem(self) -> typing.Optional[jsii.Number]:
        '''work_mem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#work_mem ManagedDatabasePostgresql#work_mem}
        '''
        result = self._values.get("work_mem")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesMigration",
    jsii_struct_bases=[],
    name_mapping={
        "dbname": "dbname",
        "host": "host",
        "ignore_dbs": "ignoreDbs",
        "password": "password",
        "port": "port",
        "ssl": "ssl",
        "username": "username",
    },
)
class ManagedDatabasePostgresqlPropertiesMigration:
    def __init__(
        self,
        *,
        dbname: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        ignore_dbs: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dbname: Database name for bootstrapping the initial connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#dbname ManagedDatabasePostgresql#dbname}
        :param host: Hostname or IP address of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#host ManagedDatabasePostgresql#host}
        :param ignore_dbs: Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_dbs ManagedDatabasePostgresql#ignore_dbs}
        :param password: Password for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#password ManagedDatabasePostgresql#password}
        :param port: Port number of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#port ManagedDatabasePostgresql#port}
        :param ssl: The server where to migrate data from is secured with SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ssl ManagedDatabasePostgresql#ssl}
        :param username: User name for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#username ManagedDatabasePostgresql#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesMigration.__init__)
            check_type(argname="argument dbname", value=dbname, expected_type=type_hints["dbname"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument ignore_dbs", value=ignore_dbs, expected_type=type_hints["ignore_dbs"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dbname is not None:
            self._values["dbname"] = dbname
        if host is not None:
            self._values["host"] = host
        if ignore_dbs is not None:
            self._values["ignore_dbs"] = ignore_dbs
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if ssl is not None:
            self._values["ssl"] = ssl
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def dbname(self) -> typing.Optional[builtins.str]:
        '''Database name for bootstrapping the initial connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#dbname ManagedDatabasePostgresql#dbname}
        '''
        result = self._values.get("dbname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Hostname or IP address of the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#host ManagedDatabasePostgresql#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_dbs(self) -> typing.Optional[builtins.str]:
        '''Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_dbs ManagedDatabasePostgresql#ignore_dbs}
        '''
        result = self._values.get("ignore_dbs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for authentication with the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#password ManagedDatabasePostgresql#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port number of the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#port ManagedDatabasePostgresql#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssl(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The server where to migrate data from is secured with SSL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ssl ManagedDatabasePostgresql#ssl}
        '''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''User name for authentication with the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#username ManagedDatabasePostgresql#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlPropertiesMigration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlPropertiesMigrationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesMigrationOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesMigrationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDbname")
    def reset_dbname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbname", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetIgnoreDbs")
    def reset_ignore_dbs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreDbs", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="dbnameInput")
    def dbname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbnameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreDbsInput")
    def ignore_dbs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ignoreDbsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbname")
    def dbname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbname"))

    @dbname.setter
    def dbname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "dbname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbname", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreDbs")
    def ignore_dbs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ignoreDbs"))

    @ignore_dbs.setter
    def ignore_dbs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "ignore_dbs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreDbs", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDatabasePostgresqlPropertiesMigration]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlPropertiesMigration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlPropertiesMigration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedDatabasePostgresqlPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMigration")
    def put_migration(
        self,
        *,
        dbname: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        ignore_dbs: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dbname: Database name for bootstrapping the initial connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#dbname ManagedDatabasePostgresql#dbname}
        :param host: Hostname or IP address of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#host ManagedDatabasePostgresql#host}
        :param ignore_dbs: Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_dbs ManagedDatabasePostgresql#ignore_dbs}
        :param password: Password for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#password ManagedDatabasePostgresql#password}
        :param port: Port number of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#port ManagedDatabasePostgresql#port}
        :param ssl: The server where to migrate data from is secured with SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ssl ManagedDatabasePostgresql#ssl}
        :param username: User name for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#username ManagedDatabasePostgresql#username}
        '''
        value = ManagedDatabasePostgresqlPropertiesMigration(
            dbname=dbname,
            host=host,
            ignore_dbs=ignore_dbs,
            password=password,
            port=port,
            ssl=ssl,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putMigration", [value]))

    @jsii.member(jsii_name="putPgbouncer")
    def put_pgbouncer(
        self,
        *,
        autodb_idle_timeout: typing.Optional[jsii.Number] = None,
        autodb_max_db_connections: typing.Optional[jsii.Number] = None,
        autodb_pool_mode: typing.Optional[builtins.str] = None,
        autodb_pool_size: typing.Optional[jsii.Number] = None,
        ignore_startup_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_pool_size: typing.Optional[jsii.Number] = None,
        server_idle_timeout: typing.Optional[jsii.Number] = None,
        server_lifetime: typing.Optional[jsii.Number] = None,
        server_reset_query_always: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param autodb_idle_timeout: If the automatically created database pools have been unused this many seconds, they are freed. If 0 then timeout is disabled. [seconds] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_idle_timeout ManagedDatabasePostgresql#autodb_idle_timeout}
        :param autodb_max_db_connections: Do not allow more than this many server connections per database (regardless of user). Setting it to 0 means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_max_db_connections ManagedDatabasePostgresql#autodb_max_db_connections}
        :param autodb_pool_mode: PGBouncer pool mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_mode ManagedDatabasePostgresql#autodb_pool_mode}
        :param autodb_pool_size: If non-zero then create automatically a pool of that size per user when a pool doesn't exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_size ManagedDatabasePostgresql#autodb_pool_size}
        :param ignore_startup_parameters: List of parameters to ignore when given in startup packet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_startup_parameters ManagedDatabasePostgresql#ignore_startup_parameters}
        :param min_pool_size: Add more server connections to pool if below this number. Improves behavior when usual load comes suddenly back after period of total inactivity. The value is effectively capped at the pool size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#min_pool_size ManagedDatabasePostgresql#min_pool_size}
        :param server_idle_timeout: If a server connection has been idle more than this many seconds it will be dropped. If 0 then timeout is disabled. [seconds] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_idle_timeout ManagedDatabasePostgresql#server_idle_timeout}
        :param server_lifetime: The pooler will close an unused server connection that has been connected longer than this. [seconds]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_lifetime ManagedDatabasePostgresql#server_lifetime}
        :param server_reset_query_always: Run server_reset_query (DISCARD ALL) in all pooling modes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_reset_query_always ManagedDatabasePostgresql#server_reset_query_always}
        '''
        value = ManagedDatabasePostgresqlPropertiesPgbouncer(
            autodb_idle_timeout=autodb_idle_timeout,
            autodb_max_db_connections=autodb_max_db_connections,
            autodb_pool_mode=autodb_pool_mode,
            autodb_pool_size=autodb_pool_size,
            ignore_startup_parameters=ignore_startup_parameters,
            min_pool_size=min_pool_size,
            server_idle_timeout=server_idle_timeout,
            server_lifetime=server_lifetime,
            server_reset_query_always=server_reset_query_always,
        )

        return typing.cast(None, jsii.invoke(self, "putPgbouncer", [value]))

    @jsii.member(jsii_name="putPglookout")
    def put_pglookout(
        self,
        *,
        max_failover_replication_time_lag: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_failover_replication_time_lag: max_failover_replication_time_lag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_failover_replication_time_lag ManagedDatabasePostgresql#max_failover_replication_time_lag}
        '''
        value = ManagedDatabasePostgresqlPropertiesPglookout(
            max_failover_replication_time_lag=max_failover_replication_time_lag
        )

        return typing.cast(None, jsii.invoke(self, "putPglookout", [value]))

    @jsii.member(jsii_name="putTimescaledb")
    def put_timescaledb(
        self,
        *,
        max_background_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_background_workers: timescaledb.max_background_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_background_workers ManagedDatabasePostgresql#max_background_workers}
        '''
        value = ManagedDatabasePostgresqlPropertiesTimescaledb(
            max_background_workers=max_background_workers
        )

        return typing.cast(None, jsii.invoke(self, "putTimescaledb", [value]))

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetAdminUsername")
    def reset_admin_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminUsername", []))

    @jsii.member(jsii_name="resetAutomaticUtilityNetworkIpFilter")
    def reset_automatic_utility_network_ip_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticUtilityNetworkIpFilter", []))

    @jsii.member(jsii_name="resetAutovacuumAnalyzeScaleFactor")
    def reset_autovacuum_analyze_scale_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumAnalyzeScaleFactor", []))

    @jsii.member(jsii_name="resetAutovacuumAnalyzeThreshold")
    def reset_autovacuum_analyze_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumAnalyzeThreshold", []))

    @jsii.member(jsii_name="resetAutovacuumFreezeMaxAge")
    def reset_autovacuum_freeze_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumFreezeMaxAge", []))

    @jsii.member(jsii_name="resetAutovacuumMaxWorkers")
    def reset_autovacuum_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumMaxWorkers", []))

    @jsii.member(jsii_name="resetAutovacuumNaptime")
    def reset_autovacuum_naptime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumNaptime", []))

    @jsii.member(jsii_name="resetAutovacuumVacuumCostDelay")
    def reset_autovacuum_vacuum_cost_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumVacuumCostDelay", []))

    @jsii.member(jsii_name="resetAutovacuumVacuumCostLimit")
    def reset_autovacuum_vacuum_cost_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumVacuumCostLimit", []))

    @jsii.member(jsii_name="resetAutovacuumVacuumScaleFactor")
    def reset_autovacuum_vacuum_scale_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumVacuumScaleFactor", []))

    @jsii.member(jsii_name="resetAutovacuumVacuumThreshold")
    def reset_autovacuum_vacuum_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutovacuumVacuumThreshold", []))

    @jsii.member(jsii_name="resetBackupHour")
    def reset_backup_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupHour", []))

    @jsii.member(jsii_name="resetBackupMinute")
    def reset_backup_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupMinute", []))

    @jsii.member(jsii_name="resetBgwriterDelay")
    def reset_bgwriter_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgwriterDelay", []))

    @jsii.member(jsii_name="resetBgwriterFlushAfter")
    def reset_bgwriter_flush_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgwriterFlushAfter", []))

    @jsii.member(jsii_name="resetBgwriterLruMaxpages")
    def reset_bgwriter_lru_maxpages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgwriterLruMaxpages", []))

    @jsii.member(jsii_name="resetBgwriterLruMultiplier")
    def reset_bgwriter_lru_multiplier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgwriterLruMultiplier", []))

    @jsii.member(jsii_name="resetDeadlockTimeout")
    def reset_deadlock_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadlockTimeout", []))

    @jsii.member(jsii_name="resetIdleInTransactionSessionTimeout")
    def reset_idle_in_transaction_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleInTransactionSessionTimeout", []))

    @jsii.member(jsii_name="resetIpFilter")
    def reset_ip_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFilter", []))

    @jsii.member(jsii_name="resetJit")
    def reset_jit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJit", []))

    @jsii.member(jsii_name="resetLogAutovacuumMinDuration")
    def reset_log_autovacuum_min_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogAutovacuumMinDuration", []))

    @jsii.member(jsii_name="resetLogErrorVerbosity")
    def reset_log_error_verbosity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogErrorVerbosity", []))

    @jsii.member(jsii_name="resetLogLinePrefix")
    def reset_log_line_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLinePrefix", []))

    @jsii.member(jsii_name="resetLogMinDurationStatement")
    def reset_log_min_duration_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogMinDurationStatement", []))

    @jsii.member(jsii_name="resetMaxFilesPerProcess")
    def reset_max_files_per_process(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFilesPerProcess", []))

    @jsii.member(jsii_name="resetMaxLocksPerTransaction")
    def reset_max_locks_per_transaction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLocksPerTransaction", []))

    @jsii.member(jsii_name="resetMaxLogicalReplicationWorkers")
    def reset_max_logical_replication_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLogicalReplicationWorkers", []))

    @jsii.member(jsii_name="resetMaxParallelWorkers")
    def reset_max_parallel_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxParallelWorkers", []))

    @jsii.member(jsii_name="resetMaxParallelWorkersPerGather")
    def reset_max_parallel_workers_per_gather(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxParallelWorkersPerGather", []))

    @jsii.member(jsii_name="resetMaxPredLocksPerTransaction")
    def reset_max_pred_locks_per_transaction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPredLocksPerTransaction", []))

    @jsii.member(jsii_name="resetMaxPreparedTransactions")
    def reset_max_prepared_transactions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPreparedTransactions", []))

    @jsii.member(jsii_name="resetMaxReplicationSlots")
    def reset_max_replication_slots(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxReplicationSlots", []))

    @jsii.member(jsii_name="resetMaxStackDepth")
    def reset_max_stack_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxStackDepth", []))

    @jsii.member(jsii_name="resetMaxStandbyArchiveDelay")
    def reset_max_standby_archive_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxStandbyArchiveDelay", []))

    @jsii.member(jsii_name="resetMaxStandbyStreamingDelay")
    def reset_max_standby_streaming_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxStandbyStreamingDelay", []))

    @jsii.member(jsii_name="resetMaxWalSenders")
    def reset_max_wal_senders(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWalSenders", []))

    @jsii.member(jsii_name="resetMaxWorkerProcesses")
    def reset_max_worker_processes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkerProcesses", []))

    @jsii.member(jsii_name="resetMigration")
    def reset_migration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMigration", []))

    @jsii.member(jsii_name="resetPgbouncer")
    def reset_pgbouncer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgbouncer", []))

    @jsii.member(jsii_name="resetPglookout")
    def reset_pglookout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPglookout", []))

    @jsii.member(jsii_name="resetPgPartmanBgwInterval")
    def reset_pg_partman_bgw_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgPartmanBgwInterval", []))

    @jsii.member(jsii_name="resetPgPartmanBgwRole")
    def reset_pg_partman_bgw_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgPartmanBgwRole", []))

    @jsii.member(jsii_name="resetPgReadReplica")
    def reset_pg_read_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgReadReplica", []))

    @jsii.member(jsii_name="resetPgServiceToForkFrom")
    def reset_pg_service_to_fork_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgServiceToForkFrom", []))

    @jsii.member(jsii_name="resetPgStatStatementsTrack")
    def reset_pg_stat_statements_track(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgStatStatementsTrack", []))

    @jsii.member(jsii_name="resetPublicAccess")
    def reset_public_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccess", []))

    @jsii.member(jsii_name="resetSharedBuffersPercentage")
    def reset_shared_buffers_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedBuffersPercentage", []))

    @jsii.member(jsii_name="resetSynchronousReplication")
    def reset_synchronous_replication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSynchronousReplication", []))

    @jsii.member(jsii_name="resetTempFileLimit")
    def reset_temp_file_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTempFileLimit", []))

    @jsii.member(jsii_name="resetTimescaledb")
    def reset_timescaledb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimescaledb", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetTrackActivityQuerySize")
    def reset_track_activity_query_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackActivityQuerySize", []))

    @jsii.member(jsii_name="resetTrackCommitTimestamp")
    def reset_track_commit_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackCommitTimestamp", []))

    @jsii.member(jsii_name="resetTrackFunctions")
    def reset_track_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackFunctions", []))

    @jsii.member(jsii_name="resetTrackIoTiming")
    def reset_track_io_timing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackIoTiming", []))

    @jsii.member(jsii_name="resetVariant")
    def reset_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariant", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetWalSenderTimeout")
    def reset_wal_sender_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWalSenderTimeout", []))

    @jsii.member(jsii_name="resetWalWriterDelay")
    def reset_wal_writer_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWalWriterDelay", []))

    @jsii.member(jsii_name="resetWorkMem")
    def reset_work_mem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkMem", []))

    @builtins.property
    @jsii.member(jsii_name="migration")
    def migration(self) -> ManagedDatabasePostgresqlPropertiesMigrationOutputReference:
        return typing.cast(ManagedDatabasePostgresqlPropertiesMigrationOutputReference, jsii.get(self, "migration"))

    @builtins.property
    @jsii.member(jsii_name="pgbouncer")
    def pgbouncer(
        self,
    ) -> "ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference":
        return typing.cast("ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference", jsii.get(self, "pgbouncer"))

    @builtins.property
    @jsii.member(jsii_name="pglookout")
    def pglookout(
        self,
    ) -> "ManagedDatabasePostgresqlPropertiesPglookoutOutputReference":
        return typing.cast("ManagedDatabasePostgresqlPropertiesPglookoutOutputReference", jsii.get(self, "pglookout"))

    @builtins.property
    @jsii.member(jsii_name="timescaledb")
    def timescaledb(
        self,
    ) -> "ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference":
        return typing.cast("ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference", jsii.get(self, "timescaledb"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticUtilityNetworkIpFilterInput")
    def automatic_utility_network_ip_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticUtilityNetworkIpFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumAnalyzeScaleFactorInput")
    def autovacuum_analyze_scale_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumAnalyzeScaleFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumAnalyzeThresholdInput")
    def autovacuum_analyze_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumAnalyzeThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumFreezeMaxAgeInput")
    def autovacuum_freeze_max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumFreezeMaxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumMaxWorkersInput")
    def autovacuum_max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumMaxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumNaptimeInput")
    def autovacuum_naptime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumNaptimeInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumCostDelayInput")
    def autovacuum_vacuum_cost_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumVacuumCostDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumCostLimitInput")
    def autovacuum_vacuum_cost_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumVacuumCostLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumScaleFactorInput")
    def autovacuum_vacuum_scale_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumVacuumScaleFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumThresholdInput")
    def autovacuum_vacuum_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autovacuumVacuumThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="backupHourInput")
    def backup_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupHourInput"))

    @builtins.property
    @jsii.member(jsii_name="backupMinuteInput")
    def backup_minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupMinuteInput"))

    @builtins.property
    @jsii.member(jsii_name="bgwriterDelayInput")
    def bgwriter_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bgwriterDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="bgwriterFlushAfterInput")
    def bgwriter_flush_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bgwriterFlushAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="bgwriterLruMaxpagesInput")
    def bgwriter_lru_maxpages_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bgwriterLruMaxpagesInput"))

    @builtins.property
    @jsii.member(jsii_name="bgwriterLruMultiplierInput")
    def bgwriter_lru_multiplier_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bgwriterLruMultiplierInput"))

    @builtins.property
    @jsii.member(jsii_name="deadlockTimeoutInput")
    def deadlock_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deadlockTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idleInTransactionSessionTimeoutInput")
    def idle_in_transaction_session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleInTransactionSessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFilterInput")
    def ip_filter_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="jitInput")
    def jit_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "jitInput"))

    @builtins.property
    @jsii.member(jsii_name="logAutovacuumMinDurationInput")
    def log_autovacuum_min_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logAutovacuumMinDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="logErrorVerbosityInput")
    def log_error_verbosity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logErrorVerbosityInput"))

    @builtins.property
    @jsii.member(jsii_name="logLinePrefixInput")
    def log_line_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLinePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="logMinDurationStatementInput")
    def log_min_duration_statement_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logMinDurationStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFilesPerProcessInput")
    def max_files_per_process_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFilesPerProcessInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLocksPerTransactionInput")
    def max_locks_per_transaction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLocksPerTransactionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLogicalReplicationWorkersInput")
    def max_logical_replication_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLogicalReplicationWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxParallelWorkersInput")
    def max_parallel_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxParallelWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxParallelWorkersPerGatherInput")
    def max_parallel_workers_per_gather_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxParallelWorkersPerGatherInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPredLocksPerTransactionInput")
    def max_pred_locks_per_transaction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPredLocksPerTransactionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPreparedTransactionsInput")
    def max_prepared_transactions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPreparedTransactionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicationSlotsInput")
    def max_replication_slots_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxReplicationSlotsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxStackDepthInput")
    def max_stack_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxStackDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="maxStandbyArchiveDelayInput")
    def max_standby_archive_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxStandbyArchiveDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="maxStandbyStreamingDelayInput")
    def max_standby_streaming_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxStandbyStreamingDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWalSendersInput")
    def max_wal_senders_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWalSendersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkerProcessesInput")
    def max_worker_processes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkerProcessesInput"))

    @builtins.property
    @jsii.member(jsii_name="migrationInput")
    def migration_input(
        self,
    ) -> typing.Optional[ManagedDatabasePostgresqlPropertiesMigration]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlPropertiesMigration], jsii.get(self, "migrationInput"))

    @builtins.property
    @jsii.member(jsii_name="pgbouncerInput")
    def pgbouncer_input(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesPgbouncer"]:
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesPgbouncer"], jsii.get(self, "pgbouncerInput"))

    @builtins.property
    @jsii.member(jsii_name="pglookoutInput")
    def pglookout_input(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesPglookout"]:
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesPglookout"], jsii.get(self, "pglookoutInput"))

    @builtins.property
    @jsii.member(jsii_name="pgPartmanBgwIntervalInput")
    def pg_partman_bgw_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pgPartmanBgwIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pgPartmanBgwRoleInput")
    def pg_partman_bgw_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pgPartmanBgwRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="pgReadReplicaInput")
    def pg_read_replica_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pgReadReplicaInput"))

    @builtins.property
    @jsii.member(jsii_name="pgServiceToForkFromInput")
    def pg_service_to_fork_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pgServiceToForkFromInput"))

    @builtins.property
    @jsii.member(jsii_name="pgStatStatementsTrackInput")
    def pg_stat_statements_track_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pgStatStatementsTrackInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessInput")
    def public_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedBuffersPercentageInput")
    def shared_buffers_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sharedBuffersPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="synchronousReplicationInput")
    def synchronous_replication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "synchronousReplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="tempFileLimitInput")
    def temp_file_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tempFileLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="timescaledbInput")
    def timescaledb_input(
        self,
    ) -> typing.Optional["ManagedDatabasePostgresqlPropertiesTimescaledb"]:
        return typing.cast(typing.Optional["ManagedDatabasePostgresqlPropertiesTimescaledb"], jsii.get(self, "timescaledbInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="trackActivityQuerySizeInput")
    def track_activity_query_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trackActivityQuerySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="trackCommitTimestampInput")
    def track_commit_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trackCommitTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="trackFunctionsInput")
    def track_functions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trackFunctionsInput"))

    @builtins.property
    @jsii.member(jsii_name="trackIoTimingInput")
    def track_io_timing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trackIoTimingInput"))

    @builtins.property
    @jsii.member(jsii_name="variantInput")
    def variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variantInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="walSenderTimeoutInput")
    def wal_sender_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "walSenderTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="walWriterDelayInput")
    def wal_writer_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "walWriterDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="workMemInput")
    def work_mem_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workMemInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="automaticUtilityNetworkIpFilter")
    def automatic_utility_network_ip_filter(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticUtilityNetworkIpFilter"))

    @automatic_utility_network_ip_filter.setter
    def automatic_utility_network_ip_filter(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "automatic_utility_network_ip_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticUtilityNetworkIpFilter", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumAnalyzeScaleFactor")
    def autovacuum_analyze_scale_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumAnalyzeScaleFactor"))

    @autovacuum_analyze_scale_factor.setter
    def autovacuum_analyze_scale_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_analyze_scale_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumAnalyzeScaleFactor", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumAnalyzeThreshold")
    def autovacuum_analyze_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumAnalyzeThreshold"))

    @autovacuum_analyze_threshold.setter
    def autovacuum_analyze_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_analyze_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumAnalyzeThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumFreezeMaxAge")
    def autovacuum_freeze_max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumFreezeMaxAge"))

    @autovacuum_freeze_max_age.setter
    def autovacuum_freeze_max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_freeze_max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumFreezeMaxAge", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumMaxWorkers")
    def autovacuum_max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumMaxWorkers"))

    @autovacuum_max_workers.setter
    def autovacuum_max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_max_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumMaxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumNaptime")
    def autovacuum_naptime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumNaptime"))

    @autovacuum_naptime.setter
    def autovacuum_naptime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_naptime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumNaptime", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumCostDelay")
    def autovacuum_vacuum_cost_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumVacuumCostDelay"))

    @autovacuum_vacuum_cost_delay.setter
    def autovacuum_vacuum_cost_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_vacuum_cost_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumVacuumCostDelay", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumCostLimit")
    def autovacuum_vacuum_cost_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumVacuumCostLimit"))

    @autovacuum_vacuum_cost_limit.setter
    def autovacuum_vacuum_cost_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_vacuum_cost_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumVacuumCostLimit", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumScaleFactor")
    def autovacuum_vacuum_scale_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumVacuumScaleFactor"))

    @autovacuum_vacuum_scale_factor.setter
    def autovacuum_vacuum_scale_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_vacuum_scale_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumVacuumScaleFactor", value)

    @builtins.property
    @jsii.member(jsii_name="autovacuumVacuumThreshold")
    def autovacuum_vacuum_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autovacuumVacuumThreshold"))

    @autovacuum_vacuum_threshold.setter
    def autovacuum_vacuum_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "autovacuum_vacuum_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autovacuumVacuumThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="backupHour")
    def backup_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupHour"))

    @backup_hour.setter
    def backup_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "backup_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupHour", value)

    @builtins.property
    @jsii.member(jsii_name="backupMinute")
    def backup_minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupMinute"))

    @backup_minute.setter
    def backup_minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "backup_minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupMinute", value)

    @builtins.property
    @jsii.member(jsii_name="bgwriterDelay")
    def bgwriter_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bgwriterDelay"))

    @bgwriter_delay.setter
    def bgwriter_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "bgwriter_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgwriterDelay", value)

    @builtins.property
    @jsii.member(jsii_name="bgwriterFlushAfter")
    def bgwriter_flush_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bgwriterFlushAfter"))

    @bgwriter_flush_after.setter
    def bgwriter_flush_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "bgwriter_flush_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgwriterFlushAfter", value)

    @builtins.property
    @jsii.member(jsii_name="bgwriterLruMaxpages")
    def bgwriter_lru_maxpages(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bgwriterLruMaxpages"))

    @bgwriter_lru_maxpages.setter
    def bgwriter_lru_maxpages(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "bgwriter_lru_maxpages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgwriterLruMaxpages", value)

    @builtins.property
    @jsii.member(jsii_name="bgwriterLruMultiplier")
    def bgwriter_lru_multiplier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bgwriterLruMultiplier"))

    @bgwriter_lru_multiplier.setter
    def bgwriter_lru_multiplier(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "bgwriter_lru_multiplier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgwriterLruMultiplier", value)

    @builtins.property
    @jsii.member(jsii_name="deadlockTimeout")
    def deadlock_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deadlockTimeout"))

    @deadlock_timeout.setter
    def deadlock_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "deadlock_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadlockTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="idleInTransactionSessionTimeout")
    def idle_in_transaction_session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleInTransactionSessionTimeout"))

    @idle_in_transaction_session_timeout.setter
    def idle_in_transaction_session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "idle_in_transaction_session_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleInTransactionSessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="ipFilter")
    def ip_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipFilter"))

    @ip_filter.setter
    def ip_filter(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "ip_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipFilter", value)

    @builtins.property
    @jsii.member(jsii_name="jit")
    def jit(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "jit"))

    @jit.setter
    def jit(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "jit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jit", value)

    @builtins.property
    @jsii.member(jsii_name="logAutovacuumMinDuration")
    def log_autovacuum_min_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logAutovacuumMinDuration"))

    @log_autovacuum_min_duration.setter
    def log_autovacuum_min_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "log_autovacuum_min_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAutovacuumMinDuration", value)

    @builtins.property
    @jsii.member(jsii_name="logErrorVerbosity")
    def log_error_verbosity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logErrorVerbosity"))

    @log_error_verbosity.setter
    def log_error_verbosity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "log_error_verbosity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logErrorVerbosity", value)

    @builtins.property
    @jsii.member(jsii_name="logLinePrefix")
    def log_line_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLinePrefix"))

    @log_line_prefix.setter
    def log_line_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "log_line_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLinePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="logMinDurationStatement")
    def log_min_duration_statement(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logMinDurationStatement"))

    @log_min_duration_statement.setter
    def log_min_duration_statement(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "log_min_duration_statement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logMinDurationStatement", value)

    @builtins.property
    @jsii.member(jsii_name="maxFilesPerProcess")
    def max_files_per_process(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFilesPerProcess"))

    @max_files_per_process.setter
    def max_files_per_process(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_files_per_process").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFilesPerProcess", value)

    @builtins.property
    @jsii.member(jsii_name="maxLocksPerTransaction")
    def max_locks_per_transaction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLocksPerTransaction"))

    @max_locks_per_transaction.setter
    def max_locks_per_transaction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_locks_per_transaction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLocksPerTransaction", value)

    @builtins.property
    @jsii.member(jsii_name="maxLogicalReplicationWorkers")
    def max_logical_replication_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLogicalReplicationWorkers"))

    @max_logical_replication_workers.setter
    def max_logical_replication_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_logical_replication_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLogicalReplicationWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="maxParallelWorkers")
    def max_parallel_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxParallelWorkers"))

    @max_parallel_workers.setter
    def max_parallel_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_parallel_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxParallelWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="maxParallelWorkersPerGather")
    def max_parallel_workers_per_gather(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxParallelWorkersPerGather"))

    @max_parallel_workers_per_gather.setter
    def max_parallel_workers_per_gather(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_parallel_workers_per_gather").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxParallelWorkersPerGather", value)

    @builtins.property
    @jsii.member(jsii_name="maxPredLocksPerTransaction")
    def max_pred_locks_per_transaction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPredLocksPerTransaction"))

    @max_pred_locks_per_transaction.setter
    def max_pred_locks_per_transaction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_pred_locks_per_transaction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPredLocksPerTransaction", value)

    @builtins.property
    @jsii.member(jsii_name="maxPreparedTransactions")
    def max_prepared_transactions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPreparedTransactions"))

    @max_prepared_transactions.setter
    def max_prepared_transactions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_prepared_transactions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPreparedTransactions", value)

    @builtins.property
    @jsii.member(jsii_name="maxReplicationSlots")
    def max_replication_slots(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxReplicationSlots"))

    @max_replication_slots.setter
    def max_replication_slots(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_replication_slots").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxReplicationSlots", value)

    @builtins.property
    @jsii.member(jsii_name="maxStackDepth")
    def max_stack_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxStackDepth"))

    @max_stack_depth.setter
    def max_stack_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_stack_depth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxStackDepth", value)

    @builtins.property
    @jsii.member(jsii_name="maxStandbyArchiveDelay")
    def max_standby_archive_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxStandbyArchiveDelay"))

    @max_standby_archive_delay.setter
    def max_standby_archive_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_standby_archive_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxStandbyArchiveDelay", value)

    @builtins.property
    @jsii.member(jsii_name="maxStandbyStreamingDelay")
    def max_standby_streaming_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxStandbyStreamingDelay"))

    @max_standby_streaming_delay.setter
    def max_standby_streaming_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_standby_streaming_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxStandbyStreamingDelay", value)

    @builtins.property
    @jsii.member(jsii_name="maxWalSenders")
    def max_wal_senders(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWalSenders"))

    @max_wal_senders.setter
    def max_wal_senders(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_wal_senders").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWalSenders", value)

    @builtins.property
    @jsii.member(jsii_name="maxWorkerProcesses")
    def max_worker_processes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkerProcesses"))

    @max_worker_processes.setter
    def max_worker_processes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "max_worker_processes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkerProcesses", value)

    @builtins.property
    @jsii.member(jsii_name="pgPartmanBgwInterval")
    def pg_partman_bgw_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pgPartmanBgwInterval"))

    @pg_partman_bgw_interval.setter
    def pg_partman_bgw_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "pg_partman_bgw_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgPartmanBgwInterval", value)

    @builtins.property
    @jsii.member(jsii_name="pgPartmanBgwRole")
    def pg_partman_bgw_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pgPartmanBgwRole"))

    @pg_partman_bgw_role.setter
    def pg_partman_bgw_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "pg_partman_bgw_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgPartmanBgwRole", value)

    @builtins.property
    @jsii.member(jsii_name="pgReadReplica")
    def pg_read_replica(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pgReadReplica"))

    @pg_read_replica.setter
    def pg_read_replica(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "pg_read_replica").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgReadReplica", value)

    @builtins.property
    @jsii.member(jsii_name="pgServiceToForkFrom")
    def pg_service_to_fork_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pgServiceToForkFrom"))

    @pg_service_to_fork_from.setter
    def pg_service_to_fork_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "pg_service_to_fork_from").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgServiceToForkFrom", value)

    @builtins.property
    @jsii.member(jsii_name="pgStatStatementsTrack")
    def pg_stat_statements_track(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pgStatStatementsTrack"))

    @pg_stat_statements_track.setter
    def pg_stat_statements_track(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "pg_stat_statements_track").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgStatStatementsTrack", value)

    @builtins.property
    @jsii.member(jsii_name="publicAccess")
    def public_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicAccess"))

    @public_access.setter
    def public_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "public_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAccess", value)

    @builtins.property
    @jsii.member(jsii_name="sharedBuffersPercentage")
    def shared_buffers_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sharedBuffersPercentage"))

    @shared_buffers_percentage.setter
    def shared_buffers_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "shared_buffers_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedBuffersPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="synchronousReplication")
    def synchronous_replication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "synchronousReplication"))

    @synchronous_replication.setter
    def synchronous_replication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "synchronous_replication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synchronousReplication", value)

    @builtins.property
    @jsii.member(jsii_name="tempFileLimit")
    def temp_file_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tempFileLimit"))

    @temp_file_limit.setter
    def temp_file_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "temp_file_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tempFileLimit", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="trackActivityQuerySize")
    def track_activity_query_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "trackActivityQuerySize"))

    @track_activity_query_size.setter
    def track_activity_query_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "track_activity_query_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackActivityQuerySize", value)

    @builtins.property
    @jsii.member(jsii_name="trackCommitTimestamp")
    def track_commit_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackCommitTimestamp"))

    @track_commit_timestamp.setter
    def track_commit_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "track_commit_timestamp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackCommitTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="trackFunctions")
    def track_functions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackFunctions"))

    @track_functions.setter
    def track_functions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "track_functions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackFunctions", value)

    @builtins.property
    @jsii.member(jsii_name="trackIoTiming")
    def track_io_timing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackIoTiming"))

    @track_io_timing.setter
    def track_io_timing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "track_io_timing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackIoTiming", value)

    @builtins.property
    @jsii.member(jsii_name="variant")
    def variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variant"))

    @variant.setter
    def variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variant", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="walSenderTimeout")
    def wal_sender_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "walSenderTimeout"))

    @wal_sender_timeout.setter
    def wal_sender_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "wal_sender_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "walSenderTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="walWriterDelay")
    def wal_writer_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "walWriterDelay"))

    @wal_writer_delay.setter
    def wal_writer_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "wal_writer_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "walWriterDelay", value)

    @builtins.property
    @jsii.member(jsii_name="workMem")
    def work_mem(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workMem"))

    @work_mem.setter
    def work_mem(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "work_mem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workMem", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabasePostgresqlProperties]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesPgbouncer",
    jsii_struct_bases=[],
    name_mapping={
        "autodb_idle_timeout": "autodbIdleTimeout",
        "autodb_max_db_connections": "autodbMaxDbConnections",
        "autodb_pool_mode": "autodbPoolMode",
        "autodb_pool_size": "autodbPoolSize",
        "ignore_startup_parameters": "ignoreStartupParameters",
        "min_pool_size": "minPoolSize",
        "server_idle_timeout": "serverIdleTimeout",
        "server_lifetime": "serverLifetime",
        "server_reset_query_always": "serverResetQueryAlways",
    },
)
class ManagedDatabasePostgresqlPropertiesPgbouncer:
    def __init__(
        self,
        *,
        autodb_idle_timeout: typing.Optional[jsii.Number] = None,
        autodb_max_db_connections: typing.Optional[jsii.Number] = None,
        autodb_pool_mode: typing.Optional[builtins.str] = None,
        autodb_pool_size: typing.Optional[jsii.Number] = None,
        ignore_startup_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_pool_size: typing.Optional[jsii.Number] = None,
        server_idle_timeout: typing.Optional[jsii.Number] = None,
        server_lifetime: typing.Optional[jsii.Number] = None,
        server_reset_query_always: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param autodb_idle_timeout: If the automatically created database pools have been unused this many seconds, they are freed. If 0 then timeout is disabled. [seconds] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_idle_timeout ManagedDatabasePostgresql#autodb_idle_timeout}
        :param autodb_max_db_connections: Do not allow more than this many server connections per database (regardless of user). Setting it to 0 means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_max_db_connections ManagedDatabasePostgresql#autodb_max_db_connections}
        :param autodb_pool_mode: PGBouncer pool mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_mode ManagedDatabasePostgresql#autodb_pool_mode}
        :param autodb_pool_size: If non-zero then create automatically a pool of that size per user when a pool doesn't exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_size ManagedDatabasePostgresql#autodb_pool_size}
        :param ignore_startup_parameters: List of parameters to ignore when given in startup packet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_startup_parameters ManagedDatabasePostgresql#ignore_startup_parameters}
        :param min_pool_size: Add more server connections to pool if below this number. Improves behavior when usual load comes suddenly back after period of total inactivity. The value is effectively capped at the pool size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#min_pool_size ManagedDatabasePostgresql#min_pool_size}
        :param server_idle_timeout: If a server connection has been idle more than this many seconds it will be dropped. If 0 then timeout is disabled. [seconds] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_idle_timeout ManagedDatabasePostgresql#server_idle_timeout}
        :param server_lifetime: The pooler will close an unused server connection that has been connected longer than this. [seconds]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_lifetime ManagedDatabasePostgresql#server_lifetime}
        :param server_reset_query_always: Run server_reset_query (DISCARD ALL) in all pooling modes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_reset_query_always ManagedDatabasePostgresql#server_reset_query_always}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesPgbouncer.__init__)
            check_type(argname="argument autodb_idle_timeout", value=autodb_idle_timeout, expected_type=type_hints["autodb_idle_timeout"])
            check_type(argname="argument autodb_max_db_connections", value=autodb_max_db_connections, expected_type=type_hints["autodb_max_db_connections"])
            check_type(argname="argument autodb_pool_mode", value=autodb_pool_mode, expected_type=type_hints["autodb_pool_mode"])
            check_type(argname="argument autodb_pool_size", value=autodb_pool_size, expected_type=type_hints["autodb_pool_size"])
            check_type(argname="argument ignore_startup_parameters", value=ignore_startup_parameters, expected_type=type_hints["ignore_startup_parameters"])
            check_type(argname="argument min_pool_size", value=min_pool_size, expected_type=type_hints["min_pool_size"])
            check_type(argname="argument server_idle_timeout", value=server_idle_timeout, expected_type=type_hints["server_idle_timeout"])
            check_type(argname="argument server_lifetime", value=server_lifetime, expected_type=type_hints["server_lifetime"])
            check_type(argname="argument server_reset_query_always", value=server_reset_query_always, expected_type=type_hints["server_reset_query_always"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autodb_idle_timeout is not None:
            self._values["autodb_idle_timeout"] = autodb_idle_timeout
        if autodb_max_db_connections is not None:
            self._values["autodb_max_db_connections"] = autodb_max_db_connections
        if autodb_pool_mode is not None:
            self._values["autodb_pool_mode"] = autodb_pool_mode
        if autodb_pool_size is not None:
            self._values["autodb_pool_size"] = autodb_pool_size
        if ignore_startup_parameters is not None:
            self._values["ignore_startup_parameters"] = ignore_startup_parameters
        if min_pool_size is not None:
            self._values["min_pool_size"] = min_pool_size
        if server_idle_timeout is not None:
            self._values["server_idle_timeout"] = server_idle_timeout
        if server_lifetime is not None:
            self._values["server_lifetime"] = server_lifetime
        if server_reset_query_always is not None:
            self._values["server_reset_query_always"] = server_reset_query_always

    @builtins.property
    def autodb_idle_timeout(self) -> typing.Optional[jsii.Number]:
        '''If the automatically created database pools have been unused this many seconds, they are freed.

        If 0 then timeout is disabled. [seconds]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_idle_timeout ManagedDatabasePostgresql#autodb_idle_timeout}
        '''
        result = self._values.get("autodb_idle_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autodb_max_db_connections(self) -> typing.Optional[jsii.Number]:
        '''Do not allow more than this many server connections per database (regardless of user).

        Setting it to 0 means unlimited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_max_db_connections ManagedDatabasePostgresql#autodb_max_db_connections}
        '''
        result = self._values.get("autodb_max_db_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autodb_pool_mode(self) -> typing.Optional[builtins.str]:
        '''PGBouncer pool mode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_mode ManagedDatabasePostgresql#autodb_pool_mode}
        '''
        result = self._values.get("autodb_pool_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def autodb_pool_size(self) -> typing.Optional[jsii.Number]:
        '''If non-zero then create automatically a pool of that size per user when a pool doesn't exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#autodb_pool_size ManagedDatabasePostgresql#autodb_pool_size}
        '''
        result = self._values.get("autodb_pool_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_startup_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of parameters to ignore when given in startup packet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#ignore_startup_parameters ManagedDatabasePostgresql#ignore_startup_parameters}
        '''
        result = self._values.get("ignore_startup_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def min_pool_size(self) -> typing.Optional[jsii.Number]:
        '''Add more server connections to pool if below this number.

        Improves behavior when usual load comes suddenly back after period of total inactivity. The value is effectively capped at the pool size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#min_pool_size ManagedDatabasePostgresql#min_pool_size}
        '''
        result = self._values.get("min_pool_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_idle_timeout(self) -> typing.Optional[jsii.Number]:
        '''If a server connection has been idle more than this many seconds it will be dropped.

        If 0 then timeout is disabled. [seconds]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_idle_timeout ManagedDatabasePostgresql#server_idle_timeout}
        '''
        result = self._values.get("server_idle_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_lifetime(self) -> typing.Optional[jsii.Number]:
        '''The pooler will close an unused server connection that has been connected longer than this. [seconds].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_lifetime ManagedDatabasePostgresql#server_lifetime}
        '''
        result = self._values.get("server_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_reset_query_always(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Run server_reset_query (DISCARD ALL) in all pooling modes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#server_reset_query_always ManagedDatabasePostgresql#server_reset_query_always}
        '''
        result = self._values.get("server_reset_query_always")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlPropertiesPgbouncer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutodbIdleTimeout")
    def reset_autodb_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutodbIdleTimeout", []))

    @jsii.member(jsii_name="resetAutodbMaxDbConnections")
    def reset_autodb_max_db_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutodbMaxDbConnections", []))

    @jsii.member(jsii_name="resetAutodbPoolMode")
    def reset_autodb_pool_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutodbPoolMode", []))

    @jsii.member(jsii_name="resetAutodbPoolSize")
    def reset_autodb_pool_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutodbPoolSize", []))

    @jsii.member(jsii_name="resetIgnoreStartupParameters")
    def reset_ignore_startup_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreStartupParameters", []))

    @jsii.member(jsii_name="resetMinPoolSize")
    def reset_min_pool_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinPoolSize", []))

    @jsii.member(jsii_name="resetServerIdleTimeout")
    def reset_server_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerIdleTimeout", []))

    @jsii.member(jsii_name="resetServerLifetime")
    def reset_server_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerLifetime", []))

    @jsii.member(jsii_name="resetServerResetQueryAlways")
    def reset_server_reset_query_always(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerResetQueryAlways", []))

    @builtins.property
    @jsii.member(jsii_name="autodbIdleTimeoutInput")
    def autodb_idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autodbIdleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="autodbMaxDbConnectionsInput")
    def autodb_max_db_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autodbMaxDbConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="autodbPoolModeInput")
    def autodb_pool_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autodbPoolModeInput"))

    @builtins.property
    @jsii.member(jsii_name="autodbPoolSizeInput")
    def autodb_pool_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autodbPoolSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreStartupParametersInput")
    def ignore_startup_parameters_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreStartupParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="minPoolSizeInput")
    def min_pool_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minPoolSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIdleTimeoutInput")
    def server_idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverIdleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="serverLifetimeInput")
    def server_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverResetQueryAlwaysInput")
    def server_reset_query_always_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serverResetQueryAlwaysInput"))

    @builtins.property
    @jsii.member(jsii_name="autodbIdleTimeout")
    def autodb_idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autodbIdleTimeout"))

    @autodb_idle_timeout.setter
    def autodb_idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "autodb_idle_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodbIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="autodbMaxDbConnections")
    def autodb_max_db_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autodbMaxDbConnections"))

    @autodb_max_db_connections.setter
    def autodb_max_db_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "autodb_max_db_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodbMaxDbConnections", value)

    @builtins.property
    @jsii.member(jsii_name="autodbPoolMode")
    def autodb_pool_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autodbPoolMode"))

    @autodb_pool_mode.setter
    def autodb_pool_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "autodb_pool_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodbPoolMode", value)

    @builtins.property
    @jsii.member(jsii_name="autodbPoolSize")
    def autodb_pool_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autodbPoolSize"))

    @autodb_pool_size.setter
    def autodb_pool_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "autodb_pool_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodbPoolSize", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreStartupParameters")
    def ignore_startup_parameters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ignoreStartupParameters"))

    @ignore_startup_parameters.setter
    def ignore_startup_parameters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "ignore_startup_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreStartupParameters", value)

    @builtins.property
    @jsii.member(jsii_name="minPoolSize")
    def min_pool_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minPoolSize"))

    @min_pool_size.setter
    def min_pool_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "min_pool_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minPoolSize", value)

    @builtins.property
    @jsii.member(jsii_name="serverIdleTimeout")
    def server_idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverIdleTimeout"))

    @server_idle_timeout.setter
    def server_idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "server_idle_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="serverLifetime")
    def server_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverLifetime"))

    @server_lifetime.setter
    def server_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "server_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="serverResetQueryAlways")
    def server_reset_query_always(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serverResetQueryAlways"))

    @server_reset_query_always.setter
    def server_reset_query_always(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "server_reset_query_always").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverResetQueryAlways", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDatabasePostgresqlPropertiesPgbouncer]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlPropertiesPgbouncer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlPropertiesPgbouncer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesPglookout",
    jsii_struct_bases=[],
    name_mapping={
        "max_failover_replication_time_lag": "maxFailoverReplicationTimeLag",
    },
)
class ManagedDatabasePostgresqlPropertiesPglookout:
    def __init__(
        self,
        *,
        max_failover_replication_time_lag: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_failover_replication_time_lag: max_failover_replication_time_lag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_failover_replication_time_lag ManagedDatabasePostgresql#max_failover_replication_time_lag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesPglookout.__init__)
            check_type(argname="argument max_failover_replication_time_lag", value=max_failover_replication_time_lag, expected_type=type_hints["max_failover_replication_time_lag"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_failover_replication_time_lag is not None:
            self._values["max_failover_replication_time_lag"] = max_failover_replication_time_lag

    @builtins.property
    def max_failover_replication_time_lag(self) -> typing.Optional[jsii.Number]:
        '''max_failover_replication_time_lag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_failover_replication_time_lag ManagedDatabasePostgresql#max_failover_replication_time_lag}
        '''
        result = self._values.get("max_failover_replication_time_lag")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlPropertiesPglookout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlPropertiesPglookoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesPglookoutOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesPglookoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxFailoverReplicationTimeLag")
    def reset_max_failover_replication_time_lag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailoverReplicationTimeLag", []))

    @builtins.property
    @jsii.member(jsii_name="maxFailoverReplicationTimeLagInput")
    def max_failover_replication_time_lag_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFailoverReplicationTimeLagInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailoverReplicationTimeLag")
    def max_failover_replication_time_lag(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailoverReplicationTimeLag"))

    @max_failover_replication_time_lag.setter
    def max_failover_replication_time_lag(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPglookoutOutputReference, "max_failover_replication_time_lag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailoverReplicationTimeLag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDatabasePostgresqlPropertiesPglookout]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlPropertiesPglookout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlPropertiesPglookout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesPglookoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesTimescaledb",
    jsii_struct_bases=[],
    name_mapping={"max_background_workers": "maxBackgroundWorkers"},
)
class ManagedDatabasePostgresqlPropertiesTimescaledb:
    def __init__(
        self,
        *,
        max_background_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_background_workers: timescaledb.max_background_workers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_background_workers ManagedDatabasePostgresql#max_background_workers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesTimescaledb.__init__)
            check_type(argname="argument max_background_workers", value=max_background_workers, expected_type=type_hints["max_background_workers"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_background_workers is not None:
            self._values["max_background_workers"] = max_background_workers

    @builtins.property
    def max_background_workers(self) -> typing.Optional[jsii.Number]:
        '''timescaledb.max_background_workers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_postgresql#max_background_workers ManagedDatabasePostgresql#max_background_workers}
        '''
        result = self._values.get("max_background_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabasePostgresqlPropertiesTimescaledb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabasePostgresql.ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxBackgroundWorkers")
    def reset_max_background_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBackgroundWorkers", []))

    @builtins.property
    @jsii.member(jsii_name="maxBackgroundWorkersInput")
    def max_background_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBackgroundWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBackgroundWorkers")
    def max_background_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBackgroundWorkers"))

    @max_background_workers.setter
    def max_background_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference, "max_background_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBackgroundWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDatabasePostgresqlPropertiesTimescaledb]:
        return typing.cast(typing.Optional[ManagedDatabasePostgresqlPropertiesTimescaledb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabasePostgresqlPropertiesTimescaledb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedDatabasePostgresql",
    "ManagedDatabasePostgresqlComponents",
    "ManagedDatabasePostgresqlComponentsList",
    "ManagedDatabasePostgresqlComponentsOutputReference",
    "ManagedDatabasePostgresqlConfig",
    "ManagedDatabasePostgresqlNodeStates",
    "ManagedDatabasePostgresqlNodeStatesList",
    "ManagedDatabasePostgresqlNodeStatesOutputReference",
    "ManagedDatabasePostgresqlProperties",
    "ManagedDatabasePostgresqlPropertiesMigration",
    "ManagedDatabasePostgresqlPropertiesMigrationOutputReference",
    "ManagedDatabasePostgresqlPropertiesOutputReference",
    "ManagedDatabasePostgresqlPropertiesPgbouncer",
    "ManagedDatabasePostgresqlPropertiesPgbouncerOutputReference",
    "ManagedDatabasePostgresqlPropertiesPglookout",
    "ManagedDatabasePostgresqlPropertiesPglookoutOutputReference",
    "ManagedDatabasePostgresqlPropertiesTimescaledb",
    "ManagedDatabasePostgresqlPropertiesTimescaledbOutputReference",
]

publication.publish()
