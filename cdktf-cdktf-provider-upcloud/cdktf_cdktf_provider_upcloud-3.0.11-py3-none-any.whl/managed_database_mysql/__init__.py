'''
# `upcloud_managed_database_mysql`

Refer to the Terraform Registory for docs: [`upcloud_managed_database_mysql`](https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql).
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


class ManagedDatabaseMysql(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysql",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql upcloud_managed_database_mysql}.'''

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
        properties: typing.Optional[typing.Union["ManagedDatabaseMysqlProperties", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql upcloud_managed_database_mysql} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the service. The name is used as a prefix for the logical hostname. Must be unique within an account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#name ManagedDatabaseMysql#name}
        :param plan: Service plan to use. This determines how much resources the instance will have. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#plan ManagedDatabaseMysql#plan}
        :param zone: Zone where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#zone ManagedDatabaseMysql#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#id ManagedDatabaseMysql#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window_dow: Maintenance window day of week. Lower case weekday name (monday, tuesday, ...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_dow ManagedDatabaseMysql#maintenance_window_dow}
        :param maintenance_window_time: Maintenance window UTC time in hh:mm:ss format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_time ManagedDatabaseMysql#maintenance_window_time}
        :param powered: The administrative power state of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#powered ManagedDatabaseMysql#powered}
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#properties ManagedDatabaseMysql#properties}
        :param title: Title of a managed database instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#title ManagedDatabaseMysql#title}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysql.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedDatabaseMysqlConfig(
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
        backup_hour: typing.Optional[jsii.Number] = None,
        backup_minute: typing.Optional[jsii.Number] = None,
        binlog_retention_period: typing.Optional[jsii.Number] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        default_time_zone: typing.Optional[builtins.str] = None,
        group_concat_max_len: typing.Optional[jsii.Number] = None,
        information_schema_stats_expiry: typing.Optional[jsii.Number] = None,
        innodb_ft_min_token_size: typing.Optional[jsii.Number] = None,
        innodb_ft_server_stopword_table: typing.Optional[builtins.str] = None,
        innodb_lock_wait_timeout: typing.Optional[jsii.Number] = None,
        innodb_log_buffer_size: typing.Optional[jsii.Number] = None,
        innodb_online_alter_log_max_size: typing.Optional[jsii.Number] = None,
        innodb_print_all_deadlocks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        innodb_rollback_on_timeout: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        interactive_timeout: typing.Optional[jsii.Number] = None,
        internal_tmp_mem_storage_engine: typing.Optional[builtins.str] = None,
        ip_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        long_query_time: typing.Optional[jsii.Number] = None,
        max_allowed_packet: typing.Optional[jsii.Number] = None,
        max_heap_table_size: typing.Optional[jsii.Number] = None,
        migration: typing.Optional[typing.Union["ManagedDatabaseMysqlPropertiesMigration", typing.Dict[str, typing.Any]]] = None,
        net_read_timeout: typing.Optional[jsii.Number] = None,
        net_write_timeout: typing.Optional[jsii.Number] = None,
        public_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        slow_query_log: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sort_buffer_size: typing.Optional[jsii.Number] = None,
        sql_mode: typing.Optional[builtins.str] = None,
        sql_require_primary_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tmp_table_size: typing.Optional[jsii.Number] = None,
        version: typing.Optional[builtins.str] = None,
        wait_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param admin_password: Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_password ManagedDatabaseMysql#admin_password}
        :param admin_username: Custom username for admin user. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_username ManagedDatabaseMysql#admin_username}
        :param automatic_utility_network_ip_filter: Automatic utility network IP Filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#automatic_utility_network_ip_filter ManagedDatabaseMysql#automatic_utility_network_ip_filter}
        :param backup_hour: The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_hour ManagedDatabaseMysql#backup_hour}
        :param backup_minute: The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_minute ManagedDatabaseMysql#backup_minute}
        :param binlog_retention_period: The minimum amount of time in seconds to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#binlog_retention_period ManagedDatabaseMysql#binlog_retention_period}
        :param connect_timeout: connect_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#connect_timeout ManagedDatabaseMysql#connect_timeout}
        :param default_time_zone: default_time_zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#default_time_zone ManagedDatabaseMysql#default_time_zone}
        :param group_concat_max_len: group_concat_max_len. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#group_concat_max_len ManagedDatabaseMysql#group_concat_max_len}
        :param information_schema_stats_expiry: information_schema_stats_expiry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#information_schema_stats_expiry ManagedDatabaseMysql#information_schema_stats_expiry}
        :param innodb_ft_min_token_size: innodb_ft_min_token_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_min_token_size ManagedDatabaseMysql#innodb_ft_min_token_size}
        :param innodb_ft_server_stopword_table: innodb_ft_server_stopword_table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_server_stopword_table ManagedDatabaseMysql#innodb_ft_server_stopword_table}
        :param innodb_lock_wait_timeout: innodb_lock_wait_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_lock_wait_timeout ManagedDatabaseMysql#innodb_lock_wait_timeout}
        :param innodb_log_buffer_size: innodb_log_buffer_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_log_buffer_size ManagedDatabaseMysql#innodb_log_buffer_size}
        :param innodb_online_alter_log_max_size: innodb_online_alter_log_max_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_online_alter_log_max_size ManagedDatabaseMysql#innodb_online_alter_log_max_size}
        :param innodb_print_all_deadlocks: innodb_print_all_deadlocks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_print_all_deadlocks ManagedDatabaseMysql#innodb_print_all_deadlocks}
        :param innodb_rollback_on_timeout: innodb_rollback_on_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_rollback_on_timeout ManagedDatabaseMysql#innodb_rollback_on_timeout}
        :param interactive_timeout: interactive_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#interactive_timeout ManagedDatabaseMysql#interactive_timeout}
        :param internal_tmp_mem_storage_engine: internal_tmp_mem_storage_engine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#internal_tmp_mem_storage_engine ManagedDatabaseMysql#internal_tmp_mem_storage_engine}
        :param ip_filter: IP filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ip_filter ManagedDatabaseMysql#ip_filter}
        :param long_query_time: long_query_time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#long_query_time ManagedDatabaseMysql#long_query_time}
        :param max_allowed_packet: max_allowed_packet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_allowed_packet ManagedDatabaseMysql#max_allowed_packet}
        :param max_heap_table_size: max_heap_table_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_heap_table_size ManagedDatabaseMysql#max_heap_table_size}
        :param migration: migration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#migration ManagedDatabaseMysql#migration}
        :param net_read_timeout: net_read_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_read_timeout ManagedDatabaseMysql#net_read_timeout}
        :param net_write_timeout: net_write_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_write_timeout ManagedDatabaseMysql#net_write_timeout}
        :param public_access: Public Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#public_access ManagedDatabaseMysql#public_access}
        :param slow_query_log: slow_query_log. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#slow_query_log ManagedDatabaseMysql#slow_query_log}
        :param sort_buffer_size: sort_buffer_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sort_buffer_size ManagedDatabaseMysql#sort_buffer_size}
        :param sql_mode: sql_mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_mode ManagedDatabaseMysql#sql_mode}
        :param sql_require_primary_key: sql_require_primary_key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_require_primary_key ManagedDatabaseMysql#sql_require_primary_key}
        :param tmp_table_size: tmp_table_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#tmp_table_size ManagedDatabaseMysql#tmp_table_size}
        :param version: MySQL major version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#version ManagedDatabaseMysql#version}
        :param wait_timeout: wait_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#wait_timeout ManagedDatabaseMysql#wait_timeout}
        '''
        value = ManagedDatabaseMysqlProperties(
            admin_password=admin_password,
            admin_username=admin_username,
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            backup_hour=backup_hour,
            backup_minute=backup_minute,
            binlog_retention_period=binlog_retention_period,
            connect_timeout=connect_timeout,
            default_time_zone=default_time_zone,
            group_concat_max_len=group_concat_max_len,
            information_schema_stats_expiry=information_schema_stats_expiry,
            innodb_ft_min_token_size=innodb_ft_min_token_size,
            innodb_ft_server_stopword_table=innodb_ft_server_stopword_table,
            innodb_lock_wait_timeout=innodb_lock_wait_timeout,
            innodb_log_buffer_size=innodb_log_buffer_size,
            innodb_online_alter_log_max_size=innodb_online_alter_log_max_size,
            innodb_print_all_deadlocks=innodb_print_all_deadlocks,
            innodb_rollback_on_timeout=innodb_rollback_on_timeout,
            interactive_timeout=interactive_timeout,
            internal_tmp_mem_storage_engine=internal_tmp_mem_storage_engine,
            ip_filter=ip_filter,
            long_query_time=long_query_time,
            max_allowed_packet=max_allowed_packet,
            max_heap_table_size=max_heap_table_size,
            migration=migration,
            net_read_timeout=net_read_timeout,
            net_write_timeout=net_write_timeout,
            public_access=public_access,
            slow_query_log=slow_query_log,
            sort_buffer_size=sort_buffer_size,
            sql_mode=sql_mode,
            sql_require_primary_key=sql_require_primary_key,
            tmp_table_size=tmp_table_size,
            version=version,
            wait_timeout=wait_timeout,
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
    def components(self) -> "ManagedDatabaseMysqlComponentsList":
        return typing.cast("ManagedDatabaseMysqlComponentsList", jsii.get(self, "components"))

    @builtins.property
    @jsii.member(jsii_name="nodeStates")
    def node_states(self) -> "ManagedDatabaseMysqlNodeStatesList":
        return typing.cast("ManagedDatabaseMysqlNodeStatesList", jsii.get(self, "nodeStates"))

    @builtins.property
    @jsii.member(jsii_name="primaryDatabase")
    def primary_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryDatabase"))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> "ManagedDatabaseMysqlPropertiesOutputReference":
        return typing.cast("ManagedDatabaseMysqlPropertiesOutputReference", jsii.get(self, "properties"))

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
    def properties_input(self) -> typing.Optional["ManagedDatabaseMysqlProperties"]:
        return typing.cast(typing.Optional["ManagedDatabaseMysqlProperties"], jsii.get(self, "propertiesInput"))

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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDow")
    def maintenance_window_dow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowDow"))

    @maintenance_window_dow.setter
    def maintenance_window_dow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "maintenance_window_dow").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowDow", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTime")
    def maintenance_window_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowTime"))

    @maintenance_window_time.setter
    def maintenance_window_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "maintenance_window_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowTime", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="powered")
    def powered(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "powered"))

    @powered.setter
    def powered(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "powered").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "powered", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysql, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlComponents",
    jsii_struct_bases=[],
    name_mapping={},
)
class ManagedDatabaseMysqlComponents:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseMysqlComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabaseMysqlComponentsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlComponentsList",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlComponentsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedDatabaseMysqlComponentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlComponentsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedDatabaseMysqlComponentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlComponentsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlComponentsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlComponentsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ManagedDatabaseMysqlComponentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlComponentsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlComponentsOutputReference.__init__)
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
    def internal_value(self) -> typing.Optional[ManagedDatabaseMysqlComponents]:
        return typing.cast(typing.Optional[ManagedDatabaseMysqlComponents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseMysqlComponents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlComponentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlConfig",
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
class ManagedDatabaseMysqlConfig(cdktf.TerraformMetaArguments):
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
        properties: typing.Optional[typing.Union["ManagedDatabaseMysqlProperties", typing.Dict[str, typing.Any]]] = None,
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
        :param name: Name of the service. The name is used as a prefix for the logical hostname. Must be unique within an account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#name ManagedDatabaseMysql#name}
        :param plan: Service plan to use. This determines how much resources the instance will have. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#plan ManagedDatabaseMysql#plan}
        :param zone: Zone where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#zone ManagedDatabaseMysql#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#id ManagedDatabaseMysql#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window_dow: Maintenance window day of week. Lower case weekday name (monday, tuesday, ...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_dow ManagedDatabaseMysql#maintenance_window_dow}
        :param maintenance_window_time: Maintenance window UTC time in hh:mm:ss format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_time ManagedDatabaseMysql#maintenance_window_time}
        :param powered: The administrative power state of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#powered ManagedDatabaseMysql#powered}
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#properties ManagedDatabaseMysql#properties}
        :param title: Title of a managed database instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#title ManagedDatabaseMysql#title}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(properties, dict):
            properties = ManagedDatabaseMysqlProperties(**properties)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlConfig.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#name ManagedDatabaseMysql#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plan(self) -> builtins.str:
        '''Service plan to use. This determines how much resources the instance will have.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#plan ManagedDatabaseMysql#plan}
        '''
        result = self._values.get("plan")
        assert result is not None, "Required property 'plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''Zone where the instance resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#zone ManagedDatabaseMysql#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#id ManagedDatabaseMysql#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window_dow(self) -> typing.Optional[builtins.str]:
        '''Maintenance window day of week. Lower case weekday name (monday, tuesday, ...).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_dow ManagedDatabaseMysql#maintenance_window_dow}
        '''
        result = self._values.get("maintenance_window_dow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window_time(self) -> typing.Optional[builtins.str]:
        '''Maintenance window UTC time in hh:mm:ss format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#maintenance_window_time ManagedDatabaseMysql#maintenance_window_time}
        '''
        result = self._values.get("maintenance_window_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def powered(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The administrative power state of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#powered ManagedDatabaseMysql#powered}
        '''
        result = self._values.get("powered")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def properties(self) -> typing.Optional["ManagedDatabaseMysqlProperties"]:
        '''properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#properties ManagedDatabaseMysql#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional["ManagedDatabaseMysqlProperties"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of a managed database instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#title ManagedDatabaseMysql#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseMysqlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlNodeStates",
    jsii_struct_bases=[],
    name_mapping={},
)
class ManagedDatabaseMysqlNodeStates:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseMysqlNodeStates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabaseMysqlNodeStatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlNodeStatesList",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlNodeStatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedDatabaseMysqlNodeStatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlNodeStatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedDatabaseMysqlNodeStatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlNodeStatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlNodeStatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlNodeStatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ManagedDatabaseMysqlNodeStatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlNodeStatesOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlNodeStatesOutputReference.__init__)
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
    def internal_value(self) -> typing.Optional[ManagedDatabaseMysqlNodeStates]:
        return typing.cast(typing.Optional[ManagedDatabaseMysqlNodeStates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseMysqlNodeStates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlNodeStatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlProperties",
    jsii_struct_bases=[],
    name_mapping={
        "admin_password": "adminPassword",
        "admin_username": "adminUsername",
        "automatic_utility_network_ip_filter": "automaticUtilityNetworkIpFilter",
        "backup_hour": "backupHour",
        "backup_minute": "backupMinute",
        "binlog_retention_period": "binlogRetentionPeriod",
        "connect_timeout": "connectTimeout",
        "default_time_zone": "defaultTimeZone",
        "group_concat_max_len": "groupConcatMaxLen",
        "information_schema_stats_expiry": "informationSchemaStatsExpiry",
        "innodb_ft_min_token_size": "innodbFtMinTokenSize",
        "innodb_ft_server_stopword_table": "innodbFtServerStopwordTable",
        "innodb_lock_wait_timeout": "innodbLockWaitTimeout",
        "innodb_log_buffer_size": "innodbLogBufferSize",
        "innodb_online_alter_log_max_size": "innodbOnlineAlterLogMaxSize",
        "innodb_print_all_deadlocks": "innodbPrintAllDeadlocks",
        "innodb_rollback_on_timeout": "innodbRollbackOnTimeout",
        "interactive_timeout": "interactiveTimeout",
        "internal_tmp_mem_storage_engine": "internalTmpMemStorageEngine",
        "ip_filter": "ipFilter",
        "long_query_time": "longQueryTime",
        "max_allowed_packet": "maxAllowedPacket",
        "max_heap_table_size": "maxHeapTableSize",
        "migration": "migration",
        "net_read_timeout": "netReadTimeout",
        "net_write_timeout": "netWriteTimeout",
        "public_access": "publicAccess",
        "slow_query_log": "slowQueryLog",
        "sort_buffer_size": "sortBufferSize",
        "sql_mode": "sqlMode",
        "sql_require_primary_key": "sqlRequirePrimaryKey",
        "tmp_table_size": "tmpTableSize",
        "version": "version",
        "wait_timeout": "waitTimeout",
    },
)
class ManagedDatabaseMysqlProperties:
    def __init__(
        self,
        *,
        admin_password: typing.Optional[builtins.str] = None,
        admin_username: typing.Optional[builtins.str] = None,
        automatic_utility_network_ip_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backup_hour: typing.Optional[jsii.Number] = None,
        backup_minute: typing.Optional[jsii.Number] = None,
        binlog_retention_period: typing.Optional[jsii.Number] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        default_time_zone: typing.Optional[builtins.str] = None,
        group_concat_max_len: typing.Optional[jsii.Number] = None,
        information_schema_stats_expiry: typing.Optional[jsii.Number] = None,
        innodb_ft_min_token_size: typing.Optional[jsii.Number] = None,
        innodb_ft_server_stopword_table: typing.Optional[builtins.str] = None,
        innodb_lock_wait_timeout: typing.Optional[jsii.Number] = None,
        innodb_log_buffer_size: typing.Optional[jsii.Number] = None,
        innodb_online_alter_log_max_size: typing.Optional[jsii.Number] = None,
        innodb_print_all_deadlocks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        innodb_rollback_on_timeout: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        interactive_timeout: typing.Optional[jsii.Number] = None,
        internal_tmp_mem_storage_engine: typing.Optional[builtins.str] = None,
        ip_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        long_query_time: typing.Optional[jsii.Number] = None,
        max_allowed_packet: typing.Optional[jsii.Number] = None,
        max_heap_table_size: typing.Optional[jsii.Number] = None,
        migration: typing.Optional[typing.Union["ManagedDatabaseMysqlPropertiesMigration", typing.Dict[str, typing.Any]]] = None,
        net_read_timeout: typing.Optional[jsii.Number] = None,
        net_write_timeout: typing.Optional[jsii.Number] = None,
        public_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        slow_query_log: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sort_buffer_size: typing.Optional[jsii.Number] = None,
        sql_mode: typing.Optional[builtins.str] = None,
        sql_require_primary_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tmp_table_size: typing.Optional[jsii.Number] = None,
        version: typing.Optional[builtins.str] = None,
        wait_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param admin_password: Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_password ManagedDatabaseMysql#admin_password}
        :param admin_username: Custom username for admin user. This must be set only when a new service is being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_username ManagedDatabaseMysql#admin_username}
        :param automatic_utility_network_ip_filter: Automatic utility network IP Filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#automatic_utility_network_ip_filter ManagedDatabaseMysql#automatic_utility_network_ip_filter}
        :param backup_hour: The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_hour ManagedDatabaseMysql#backup_hour}
        :param backup_minute: The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_minute ManagedDatabaseMysql#backup_minute}
        :param binlog_retention_period: The minimum amount of time in seconds to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#binlog_retention_period ManagedDatabaseMysql#binlog_retention_period}
        :param connect_timeout: connect_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#connect_timeout ManagedDatabaseMysql#connect_timeout}
        :param default_time_zone: default_time_zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#default_time_zone ManagedDatabaseMysql#default_time_zone}
        :param group_concat_max_len: group_concat_max_len. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#group_concat_max_len ManagedDatabaseMysql#group_concat_max_len}
        :param information_schema_stats_expiry: information_schema_stats_expiry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#information_schema_stats_expiry ManagedDatabaseMysql#information_schema_stats_expiry}
        :param innodb_ft_min_token_size: innodb_ft_min_token_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_min_token_size ManagedDatabaseMysql#innodb_ft_min_token_size}
        :param innodb_ft_server_stopword_table: innodb_ft_server_stopword_table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_server_stopword_table ManagedDatabaseMysql#innodb_ft_server_stopword_table}
        :param innodb_lock_wait_timeout: innodb_lock_wait_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_lock_wait_timeout ManagedDatabaseMysql#innodb_lock_wait_timeout}
        :param innodb_log_buffer_size: innodb_log_buffer_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_log_buffer_size ManagedDatabaseMysql#innodb_log_buffer_size}
        :param innodb_online_alter_log_max_size: innodb_online_alter_log_max_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_online_alter_log_max_size ManagedDatabaseMysql#innodb_online_alter_log_max_size}
        :param innodb_print_all_deadlocks: innodb_print_all_deadlocks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_print_all_deadlocks ManagedDatabaseMysql#innodb_print_all_deadlocks}
        :param innodb_rollback_on_timeout: innodb_rollback_on_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_rollback_on_timeout ManagedDatabaseMysql#innodb_rollback_on_timeout}
        :param interactive_timeout: interactive_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#interactive_timeout ManagedDatabaseMysql#interactive_timeout}
        :param internal_tmp_mem_storage_engine: internal_tmp_mem_storage_engine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#internal_tmp_mem_storage_engine ManagedDatabaseMysql#internal_tmp_mem_storage_engine}
        :param ip_filter: IP filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ip_filter ManagedDatabaseMysql#ip_filter}
        :param long_query_time: long_query_time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#long_query_time ManagedDatabaseMysql#long_query_time}
        :param max_allowed_packet: max_allowed_packet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_allowed_packet ManagedDatabaseMysql#max_allowed_packet}
        :param max_heap_table_size: max_heap_table_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_heap_table_size ManagedDatabaseMysql#max_heap_table_size}
        :param migration: migration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#migration ManagedDatabaseMysql#migration}
        :param net_read_timeout: net_read_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_read_timeout ManagedDatabaseMysql#net_read_timeout}
        :param net_write_timeout: net_write_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_write_timeout ManagedDatabaseMysql#net_write_timeout}
        :param public_access: Public Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#public_access ManagedDatabaseMysql#public_access}
        :param slow_query_log: slow_query_log. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#slow_query_log ManagedDatabaseMysql#slow_query_log}
        :param sort_buffer_size: sort_buffer_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sort_buffer_size ManagedDatabaseMysql#sort_buffer_size}
        :param sql_mode: sql_mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_mode ManagedDatabaseMysql#sql_mode}
        :param sql_require_primary_key: sql_require_primary_key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_require_primary_key ManagedDatabaseMysql#sql_require_primary_key}
        :param tmp_table_size: tmp_table_size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#tmp_table_size ManagedDatabaseMysql#tmp_table_size}
        :param version: MySQL major version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#version ManagedDatabaseMysql#version}
        :param wait_timeout: wait_timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#wait_timeout ManagedDatabaseMysql#wait_timeout}
        '''
        if isinstance(migration, dict):
            migration = ManagedDatabaseMysqlPropertiesMigration(**migration)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlProperties.__init__)
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument automatic_utility_network_ip_filter", value=automatic_utility_network_ip_filter, expected_type=type_hints["automatic_utility_network_ip_filter"])
            check_type(argname="argument backup_hour", value=backup_hour, expected_type=type_hints["backup_hour"])
            check_type(argname="argument backup_minute", value=backup_minute, expected_type=type_hints["backup_minute"])
            check_type(argname="argument binlog_retention_period", value=binlog_retention_period, expected_type=type_hints["binlog_retention_period"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument default_time_zone", value=default_time_zone, expected_type=type_hints["default_time_zone"])
            check_type(argname="argument group_concat_max_len", value=group_concat_max_len, expected_type=type_hints["group_concat_max_len"])
            check_type(argname="argument information_schema_stats_expiry", value=information_schema_stats_expiry, expected_type=type_hints["information_schema_stats_expiry"])
            check_type(argname="argument innodb_ft_min_token_size", value=innodb_ft_min_token_size, expected_type=type_hints["innodb_ft_min_token_size"])
            check_type(argname="argument innodb_ft_server_stopword_table", value=innodb_ft_server_stopword_table, expected_type=type_hints["innodb_ft_server_stopword_table"])
            check_type(argname="argument innodb_lock_wait_timeout", value=innodb_lock_wait_timeout, expected_type=type_hints["innodb_lock_wait_timeout"])
            check_type(argname="argument innodb_log_buffer_size", value=innodb_log_buffer_size, expected_type=type_hints["innodb_log_buffer_size"])
            check_type(argname="argument innodb_online_alter_log_max_size", value=innodb_online_alter_log_max_size, expected_type=type_hints["innodb_online_alter_log_max_size"])
            check_type(argname="argument innodb_print_all_deadlocks", value=innodb_print_all_deadlocks, expected_type=type_hints["innodb_print_all_deadlocks"])
            check_type(argname="argument innodb_rollback_on_timeout", value=innodb_rollback_on_timeout, expected_type=type_hints["innodb_rollback_on_timeout"])
            check_type(argname="argument interactive_timeout", value=interactive_timeout, expected_type=type_hints["interactive_timeout"])
            check_type(argname="argument internal_tmp_mem_storage_engine", value=internal_tmp_mem_storage_engine, expected_type=type_hints["internal_tmp_mem_storage_engine"])
            check_type(argname="argument ip_filter", value=ip_filter, expected_type=type_hints["ip_filter"])
            check_type(argname="argument long_query_time", value=long_query_time, expected_type=type_hints["long_query_time"])
            check_type(argname="argument max_allowed_packet", value=max_allowed_packet, expected_type=type_hints["max_allowed_packet"])
            check_type(argname="argument max_heap_table_size", value=max_heap_table_size, expected_type=type_hints["max_heap_table_size"])
            check_type(argname="argument migration", value=migration, expected_type=type_hints["migration"])
            check_type(argname="argument net_read_timeout", value=net_read_timeout, expected_type=type_hints["net_read_timeout"])
            check_type(argname="argument net_write_timeout", value=net_write_timeout, expected_type=type_hints["net_write_timeout"])
            check_type(argname="argument public_access", value=public_access, expected_type=type_hints["public_access"])
            check_type(argname="argument slow_query_log", value=slow_query_log, expected_type=type_hints["slow_query_log"])
            check_type(argname="argument sort_buffer_size", value=sort_buffer_size, expected_type=type_hints["sort_buffer_size"])
            check_type(argname="argument sql_mode", value=sql_mode, expected_type=type_hints["sql_mode"])
            check_type(argname="argument sql_require_primary_key", value=sql_require_primary_key, expected_type=type_hints["sql_require_primary_key"])
            check_type(argname="argument tmp_table_size", value=tmp_table_size, expected_type=type_hints["tmp_table_size"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument wait_timeout", value=wait_timeout, expected_type=type_hints["wait_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_username is not None:
            self._values["admin_username"] = admin_username
        if automatic_utility_network_ip_filter is not None:
            self._values["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if backup_hour is not None:
            self._values["backup_hour"] = backup_hour
        if backup_minute is not None:
            self._values["backup_minute"] = backup_minute
        if binlog_retention_period is not None:
            self._values["binlog_retention_period"] = binlog_retention_period
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if default_time_zone is not None:
            self._values["default_time_zone"] = default_time_zone
        if group_concat_max_len is not None:
            self._values["group_concat_max_len"] = group_concat_max_len
        if information_schema_stats_expiry is not None:
            self._values["information_schema_stats_expiry"] = information_schema_stats_expiry
        if innodb_ft_min_token_size is not None:
            self._values["innodb_ft_min_token_size"] = innodb_ft_min_token_size
        if innodb_ft_server_stopword_table is not None:
            self._values["innodb_ft_server_stopword_table"] = innodb_ft_server_stopword_table
        if innodb_lock_wait_timeout is not None:
            self._values["innodb_lock_wait_timeout"] = innodb_lock_wait_timeout
        if innodb_log_buffer_size is not None:
            self._values["innodb_log_buffer_size"] = innodb_log_buffer_size
        if innodb_online_alter_log_max_size is not None:
            self._values["innodb_online_alter_log_max_size"] = innodb_online_alter_log_max_size
        if innodb_print_all_deadlocks is not None:
            self._values["innodb_print_all_deadlocks"] = innodb_print_all_deadlocks
        if innodb_rollback_on_timeout is not None:
            self._values["innodb_rollback_on_timeout"] = innodb_rollback_on_timeout
        if interactive_timeout is not None:
            self._values["interactive_timeout"] = interactive_timeout
        if internal_tmp_mem_storage_engine is not None:
            self._values["internal_tmp_mem_storage_engine"] = internal_tmp_mem_storage_engine
        if ip_filter is not None:
            self._values["ip_filter"] = ip_filter
        if long_query_time is not None:
            self._values["long_query_time"] = long_query_time
        if max_allowed_packet is not None:
            self._values["max_allowed_packet"] = max_allowed_packet
        if max_heap_table_size is not None:
            self._values["max_heap_table_size"] = max_heap_table_size
        if migration is not None:
            self._values["migration"] = migration
        if net_read_timeout is not None:
            self._values["net_read_timeout"] = net_read_timeout
        if net_write_timeout is not None:
            self._values["net_write_timeout"] = net_write_timeout
        if public_access is not None:
            self._values["public_access"] = public_access
        if slow_query_log is not None:
            self._values["slow_query_log"] = slow_query_log
        if sort_buffer_size is not None:
            self._values["sort_buffer_size"] = sort_buffer_size
        if sql_mode is not None:
            self._values["sql_mode"] = sql_mode
        if sql_require_primary_key is not None:
            self._values["sql_require_primary_key"] = sql_require_primary_key
        if tmp_table_size is not None:
            self._values["tmp_table_size"] = tmp_table_size
        if version is not None:
            self._values["version"] = version
        if wait_timeout is not None:
            self._values["wait_timeout"] = wait_timeout

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Custom password for admin user.

        Defaults to random string. This must be set only when a new service is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_password ManagedDatabaseMysql#admin_password}
        '''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''Custom username for admin user. This must be set only when a new service is being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#admin_username ManagedDatabaseMysql#admin_username}
        '''
        result = self._values.get("admin_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_utility_network_ip_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Automatic utility network IP Filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#automatic_utility_network_ip_filter ManagedDatabaseMysql#automatic_utility_network_ip_filter}
        '''
        result = self._values.get("automatic_utility_network_ip_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backup_hour(self) -> typing.Optional[jsii.Number]:
        '''The hour of day (in UTC) when backup for the service is started.

        New backup is only started if previous backup has already completed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_hour ManagedDatabaseMysql#backup_hour}
        '''
        result = self._values.get("backup_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_minute(self) -> typing.Optional[jsii.Number]:
        '''The minute of an hour when backup for the service is started.

        New backup is only started if previous backup has already completed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#backup_minute ManagedDatabaseMysql#backup_minute}
        '''
        result = self._values.get("backup_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def binlog_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The minimum amount of time in seconds to keep binlog entries before deletion.

        This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#binlog_retention_period ManagedDatabaseMysql#binlog_retention_period}
        '''
        result = self._values.get("binlog_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''connect_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#connect_timeout ManagedDatabaseMysql#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_time_zone(self) -> typing.Optional[builtins.str]:
        '''default_time_zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#default_time_zone ManagedDatabaseMysql#default_time_zone}
        '''
        result = self._values.get("default_time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_concat_max_len(self) -> typing.Optional[jsii.Number]:
        '''group_concat_max_len.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#group_concat_max_len ManagedDatabaseMysql#group_concat_max_len}
        '''
        result = self._values.get("group_concat_max_len")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def information_schema_stats_expiry(self) -> typing.Optional[jsii.Number]:
        '''information_schema_stats_expiry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#information_schema_stats_expiry ManagedDatabaseMysql#information_schema_stats_expiry}
        '''
        result = self._values.get("information_schema_stats_expiry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def innodb_ft_min_token_size(self) -> typing.Optional[jsii.Number]:
        '''innodb_ft_min_token_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_min_token_size ManagedDatabaseMysql#innodb_ft_min_token_size}
        '''
        result = self._values.get("innodb_ft_min_token_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def innodb_ft_server_stopword_table(self) -> typing.Optional[builtins.str]:
        '''innodb_ft_server_stopword_table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_ft_server_stopword_table ManagedDatabaseMysql#innodb_ft_server_stopword_table}
        '''
        result = self._values.get("innodb_ft_server_stopword_table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def innodb_lock_wait_timeout(self) -> typing.Optional[jsii.Number]:
        '''innodb_lock_wait_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_lock_wait_timeout ManagedDatabaseMysql#innodb_lock_wait_timeout}
        '''
        result = self._values.get("innodb_lock_wait_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def innodb_log_buffer_size(self) -> typing.Optional[jsii.Number]:
        '''innodb_log_buffer_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_log_buffer_size ManagedDatabaseMysql#innodb_log_buffer_size}
        '''
        result = self._values.get("innodb_log_buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def innodb_online_alter_log_max_size(self) -> typing.Optional[jsii.Number]:
        '''innodb_online_alter_log_max_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_online_alter_log_max_size ManagedDatabaseMysql#innodb_online_alter_log_max_size}
        '''
        result = self._values.get("innodb_online_alter_log_max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def innodb_print_all_deadlocks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''innodb_print_all_deadlocks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_print_all_deadlocks ManagedDatabaseMysql#innodb_print_all_deadlocks}
        '''
        result = self._values.get("innodb_print_all_deadlocks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def innodb_rollback_on_timeout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''innodb_rollback_on_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#innodb_rollback_on_timeout ManagedDatabaseMysql#innodb_rollback_on_timeout}
        '''
        result = self._values.get("innodb_rollback_on_timeout")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def interactive_timeout(self) -> typing.Optional[jsii.Number]:
        '''interactive_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#interactive_timeout ManagedDatabaseMysql#interactive_timeout}
        '''
        result = self._values.get("interactive_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def internal_tmp_mem_storage_engine(self) -> typing.Optional[builtins.str]:
        '''internal_tmp_mem_storage_engine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#internal_tmp_mem_storage_engine ManagedDatabaseMysql#internal_tmp_mem_storage_engine}
        '''
        result = self._values.get("internal_tmp_mem_storage_engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_filter(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IP filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ip_filter ManagedDatabaseMysql#ip_filter}
        '''
        result = self._values.get("ip_filter")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def long_query_time(self) -> typing.Optional[jsii.Number]:
        '''long_query_time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#long_query_time ManagedDatabaseMysql#long_query_time}
        '''
        result = self._values.get("long_query_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_allowed_packet(self) -> typing.Optional[jsii.Number]:
        '''max_allowed_packet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_allowed_packet ManagedDatabaseMysql#max_allowed_packet}
        '''
        result = self._values.get("max_allowed_packet")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_heap_table_size(self) -> typing.Optional[jsii.Number]:
        '''max_heap_table_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#max_heap_table_size ManagedDatabaseMysql#max_heap_table_size}
        '''
        result = self._values.get("max_heap_table_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def migration(self) -> typing.Optional["ManagedDatabaseMysqlPropertiesMigration"]:
        '''migration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#migration ManagedDatabaseMysql#migration}
        '''
        result = self._values.get("migration")
        return typing.cast(typing.Optional["ManagedDatabaseMysqlPropertiesMigration"], result)

    @builtins.property
    def net_read_timeout(self) -> typing.Optional[jsii.Number]:
        '''net_read_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_read_timeout ManagedDatabaseMysql#net_read_timeout}
        '''
        result = self._values.get("net_read_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_write_timeout(self) -> typing.Optional[jsii.Number]:
        '''net_write_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#net_write_timeout ManagedDatabaseMysql#net_write_timeout}
        '''
        result = self._values.get("net_write_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def public_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Public Access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#public_access ManagedDatabaseMysql#public_access}
        '''
        result = self._values.get("public_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def slow_query_log(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''slow_query_log.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#slow_query_log ManagedDatabaseMysql#slow_query_log}
        '''
        result = self._values.get("slow_query_log")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sort_buffer_size(self) -> typing.Optional[jsii.Number]:
        '''sort_buffer_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sort_buffer_size ManagedDatabaseMysql#sort_buffer_size}
        '''
        result = self._values.get("sort_buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sql_mode(self) -> typing.Optional[builtins.str]:
        '''sql_mode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_mode ManagedDatabaseMysql#sql_mode}
        '''
        result = self._values.get("sql_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_require_primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''sql_require_primary_key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#sql_require_primary_key ManagedDatabaseMysql#sql_require_primary_key}
        '''
        result = self._values.get("sql_require_primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tmp_table_size(self) -> typing.Optional[jsii.Number]:
        '''tmp_table_size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#tmp_table_size ManagedDatabaseMysql#tmp_table_size}
        '''
        result = self._values.get("tmp_table_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''MySQL major version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#version ManagedDatabaseMysql#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_timeout(self) -> typing.Optional[jsii.Number]:
        '''wait_timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#wait_timeout ManagedDatabaseMysql#wait_timeout}
        '''
        result = self._values.get("wait_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseMysqlProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlPropertiesMigration",
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
class ManagedDatabaseMysqlPropertiesMigration:
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
        :param dbname: Database name for bootstrapping the initial connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#dbname ManagedDatabaseMysql#dbname}
        :param host: Hostname or IP address of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#host ManagedDatabaseMysql#host}
        :param ignore_dbs: Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ignore_dbs ManagedDatabaseMysql#ignore_dbs}
        :param password: Password for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#password ManagedDatabaseMysql#password}
        :param port: Port number of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#port ManagedDatabaseMysql#port}
        :param ssl: The server where to migrate data from is secured with SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ssl ManagedDatabaseMysql#ssl}
        :param username: User name for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#username ManagedDatabaseMysql#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlPropertiesMigration.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#dbname ManagedDatabaseMysql#dbname}
        '''
        result = self._values.get("dbname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Hostname or IP address of the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#host ManagedDatabaseMysql#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_dbs(self) -> typing.Optional[builtins.str]:
        '''Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ignore_dbs ManagedDatabaseMysql#ignore_dbs}
        '''
        result = self._values.get("ignore_dbs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for authentication with the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#password ManagedDatabaseMysql#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port number of the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#port ManagedDatabaseMysql#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssl(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The server where to migrate data from is secured with SSL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ssl ManagedDatabaseMysql#ssl}
        '''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''User name for authentication with the server where to migrate data from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#username ManagedDatabaseMysql#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseMysqlPropertiesMigration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabaseMysqlPropertiesMigrationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlPropertiesMigrationOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlPropertiesMigrationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "dbname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbname", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreDbs")
    def ignore_dbs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ignoreDbs"))

    @ignore_dbs.setter
    def ignore_dbs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "ignore_dbs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreDbs", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDatabaseMysqlPropertiesMigration]:
        return typing.cast(typing.Optional[ManagedDatabaseMysqlPropertiesMigration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseMysqlPropertiesMigration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesMigrationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedDatabaseMysqlPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseMysql.ManagedDatabaseMysqlPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDatabaseMysqlPropertiesOutputReference.__init__)
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
        :param dbname: Database name for bootstrapping the initial connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#dbname ManagedDatabaseMysql#dbname}
        :param host: Hostname or IP address of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#host ManagedDatabaseMysql#host}
        :param ignore_dbs: Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ignore_dbs ManagedDatabaseMysql#ignore_dbs}
        :param password: Password for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#password ManagedDatabaseMysql#password}
        :param port: Port number of the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#port ManagedDatabaseMysql#port}
        :param ssl: The server where to migrate data from is secured with SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#ssl ManagedDatabaseMysql#ssl}
        :param username: User name for authentication with the server where to migrate data from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_mysql#username ManagedDatabaseMysql#username}
        '''
        value = ManagedDatabaseMysqlPropertiesMigration(
            dbname=dbname,
            host=host,
            ignore_dbs=ignore_dbs,
            password=password,
            port=port,
            ssl=ssl,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putMigration", [value]))

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetAdminUsername")
    def reset_admin_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminUsername", []))

    @jsii.member(jsii_name="resetAutomaticUtilityNetworkIpFilter")
    def reset_automatic_utility_network_ip_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticUtilityNetworkIpFilter", []))

    @jsii.member(jsii_name="resetBackupHour")
    def reset_backup_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupHour", []))

    @jsii.member(jsii_name="resetBackupMinute")
    def reset_backup_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupMinute", []))

    @jsii.member(jsii_name="resetBinlogRetentionPeriod")
    def reset_binlog_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinlogRetentionPeriod", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetDefaultTimeZone")
    def reset_default_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTimeZone", []))

    @jsii.member(jsii_name="resetGroupConcatMaxLen")
    def reset_group_concat_max_len(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupConcatMaxLen", []))

    @jsii.member(jsii_name="resetInformationSchemaStatsExpiry")
    def reset_information_schema_stats_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInformationSchemaStatsExpiry", []))

    @jsii.member(jsii_name="resetInnodbFtMinTokenSize")
    def reset_innodb_ft_min_token_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbFtMinTokenSize", []))

    @jsii.member(jsii_name="resetInnodbFtServerStopwordTable")
    def reset_innodb_ft_server_stopword_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbFtServerStopwordTable", []))

    @jsii.member(jsii_name="resetInnodbLockWaitTimeout")
    def reset_innodb_lock_wait_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbLockWaitTimeout", []))

    @jsii.member(jsii_name="resetInnodbLogBufferSize")
    def reset_innodb_log_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbLogBufferSize", []))

    @jsii.member(jsii_name="resetInnodbOnlineAlterLogMaxSize")
    def reset_innodb_online_alter_log_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbOnlineAlterLogMaxSize", []))

    @jsii.member(jsii_name="resetInnodbPrintAllDeadlocks")
    def reset_innodb_print_all_deadlocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbPrintAllDeadlocks", []))

    @jsii.member(jsii_name="resetInnodbRollbackOnTimeout")
    def reset_innodb_rollback_on_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInnodbRollbackOnTimeout", []))

    @jsii.member(jsii_name="resetInteractiveTimeout")
    def reset_interactive_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInteractiveTimeout", []))

    @jsii.member(jsii_name="resetInternalTmpMemStorageEngine")
    def reset_internal_tmp_mem_storage_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalTmpMemStorageEngine", []))

    @jsii.member(jsii_name="resetIpFilter")
    def reset_ip_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFilter", []))

    @jsii.member(jsii_name="resetLongQueryTime")
    def reset_long_query_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongQueryTime", []))

    @jsii.member(jsii_name="resetMaxAllowedPacket")
    def reset_max_allowed_packet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAllowedPacket", []))

    @jsii.member(jsii_name="resetMaxHeapTableSize")
    def reset_max_heap_table_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeapTableSize", []))

    @jsii.member(jsii_name="resetMigration")
    def reset_migration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMigration", []))

    @jsii.member(jsii_name="resetNetReadTimeout")
    def reset_net_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetReadTimeout", []))

    @jsii.member(jsii_name="resetNetWriteTimeout")
    def reset_net_write_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetWriteTimeout", []))

    @jsii.member(jsii_name="resetPublicAccess")
    def reset_public_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccess", []))

    @jsii.member(jsii_name="resetSlowQueryLog")
    def reset_slow_query_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowQueryLog", []))

    @jsii.member(jsii_name="resetSortBufferSize")
    def reset_sort_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortBufferSize", []))

    @jsii.member(jsii_name="resetSqlMode")
    def reset_sql_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlMode", []))

    @jsii.member(jsii_name="resetSqlRequirePrimaryKey")
    def reset_sql_require_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlRequirePrimaryKey", []))

    @jsii.member(jsii_name="resetTmpTableSize")
    def reset_tmp_table_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTmpTableSize", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetWaitTimeout")
    def reset_wait_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="migration")
    def migration(self) -> ManagedDatabaseMysqlPropertiesMigrationOutputReference:
        return typing.cast(ManagedDatabaseMysqlPropertiesMigrationOutputReference, jsii.get(self, "migration"))

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
    @jsii.member(jsii_name="backupHourInput")
    def backup_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupHourInput"))

    @builtins.property
    @jsii.member(jsii_name="backupMinuteInput")
    def backup_minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupMinuteInput"))

    @builtins.property
    @jsii.member(jsii_name="binlogRetentionPeriodInput")
    def binlog_retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "binlogRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeZoneInput")
    def default_time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTimeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="groupConcatMaxLenInput")
    def group_concat_max_len_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupConcatMaxLenInput"))

    @builtins.property
    @jsii.member(jsii_name="informationSchemaStatsExpiryInput")
    def information_schema_stats_expiry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "informationSchemaStatsExpiryInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbFtMinTokenSizeInput")
    def innodb_ft_min_token_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "innodbFtMinTokenSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbFtServerStopwordTableInput")
    def innodb_ft_server_stopword_table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "innodbFtServerStopwordTableInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbLockWaitTimeoutInput")
    def innodb_lock_wait_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "innodbLockWaitTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbLogBufferSizeInput")
    def innodb_log_buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "innodbLogBufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbOnlineAlterLogMaxSizeInput")
    def innodb_online_alter_log_max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "innodbOnlineAlterLogMaxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbPrintAllDeadlocksInput")
    def innodb_print_all_deadlocks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "innodbPrintAllDeadlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="innodbRollbackOnTimeoutInput")
    def innodb_rollback_on_timeout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "innodbRollbackOnTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="interactiveTimeoutInput")
    def interactive_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "interactiveTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="internalTmpMemStorageEngineInput")
    def internal_tmp_mem_storage_engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internalTmpMemStorageEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFilterInput")
    def ip_filter_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="longQueryTimeInput")
    def long_query_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longQueryTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAllowedPacketInput")
    def max_allowed_packet_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAllowedPacketInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeapTableSizeInput")
    def max_heap_table_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxHeapTableSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="migrationInput")
    def migration_input(
        self,
    ) -> typing.Optional[ManagedDatabaseMysqlPropertiesMigration]:
        return typing.cast(typing.Optional[ManagedDatabaseMysqlPropertiesMigration], jsii.get(self, "migrationInput"))

    @builtins.property
    @jsii.member(jsii_name="netReadTimeoutInput")
    def net_read_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netReadTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="netWriteTimeoutInput")
    def net_write_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netWriteTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessInput")
    def public_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="slowQueryLogInput")
    def slow_query_log_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "slowQueryLogInput"))

    @builtins.property
    @jsii.member(jsii_name="sortBufferSizeInput")
    def sort_buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sortBufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlModeInput")
    def sql_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlRequirePrimaryKeyInput")
    def sql_require_primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sqlRequirePrimaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tmpTableSizeInput")
    def tmp_table_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tmpTableSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimeoutInput")
    def wait_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "admin_username").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "automatic_utility_network_ip_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticUtilityNetworkIpFilter", value)

    @builtins.property
    @jsii.member(jsii_name="backupHour")
    def backup_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupHour"))

    @backup_hour.setter
    def backup_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "backup_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupHour", value)

    @builtins.property
    @jsii.member(jsii_name="backupMinute")
    def backup_minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupMinute"))

    @backup_minute.setter
    def backup_minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "backup_minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupMinute", value)

    @builtins.property
    @jsii.member(jsii_name="binlogRetentionPeriod")
    def binlog_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "binlogRetentionPeriod"))

    @binlog_retention_period.setter
    def binlog_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "binlog_retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "binlogRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTimeZone")
    def default_time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTimeZone"))

    @default_time_zone.setter
    def default_time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "default_time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTimeZone", value)

    @builtins.property
    @jsii.member(jsii_name="groupConcatMaxLen")
    def group_concat_max_len(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupConcatMaxLen"))

    @group_concat_max_len.setter
    def group_concat_max_len(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "group_concat_max_len").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupConcatMaxLen", value)

    @builtins.property
    @jsii.member(jsii_name="informationSchemaStatsExpiry")
    def information_schema_stats_expiry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "informationSchemaStatsExpiry"))

    @information_schema_stats_expiry.setter
    def information_schema_stats_expiry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "information_schema_stats_expiry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "informationSchemaStatsExpiry", value)

    @builtins.property
    @jsii.member(jsii_name="innodbFtMinTokenSize")
    def innodb_ft_min_token_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "innodbFtMinTokenSize"))

    @innodb_ft_min_token_size.setter
    def innodb_ft_min_token_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_ft_min_token_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbFtMinTokenSize", value)

    @builtins.property
    @jsii.member(jsii_name="innodbFtServerStopwordTable")
    def innodb_ft_server_stopword_table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "innodbFtServerStopwordTable"))

    @innodb_ft_server_stopword_table.setter
    def innodb_ft_server_stopword_table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_ft_server_stopword_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbFtServerStopwordTable", value)

    @builtins.property
    @jsii.member(jsii_name="innodbLockWaitTimeout")
    def innodb_lock_wait_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "innodbLockWaitTimeout"))

    @innodb_lock_wait_timeout.setter
    def innodb_lock_wait_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_lock_wait_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbLockWaitTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="innodbLogBufferSize")
    def innodb_log_buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "innodbLogBufferSize"))

    @innodb_log_buffer_size.setter
    def innodb_log_buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_log_buffer_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbLogBufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="innodbOnlineAlterLogMaxSize")
    def innodb_online_alter_log_max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "innodbOnlineAlterLogMaxSize"))

    @innodb_online_alter_log_max_size.setter
    def innodb_online_alter_log_max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_online_alter_log_max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbOnlineAlterLogMaxSize", value)

    @builtins.property
    @jsii.member(jsii_name="innodbPrintAllDeadlocks")
    def innodb_print_all_deadlocks(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "innodbPrintAllDeadlocks"))

    @innodb_print_all_deadlocks.setter
    def innodb_print_all_deadlocks(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_print_all_deadlocks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbPrintAllDeadlocks", value)

    @builtins.property
    @jsii.member(jsii_name="innodbRollbackOnTimeout")
    def innodb_rollback_on_timeout(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "innodbRollbackOnTimeout"))

    @innodb_rollback_on_timeout.setter
    def innodb_rollback_on_timeout(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "innodb_rollback_on_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "innodbRollbackOnTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="interactiveTimeout")
    def interactive_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interactiveTimeout"))

    @interactive_timeout.setter
    def interactive_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "interactive_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interactiveTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalTmpMemStorageEngine")
    def internal_tmp_mem_storage_engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalTmpMemStorageEngine"))

    @internal_tmp_mem_storage_engine.setter
    def internal_tmp_mem_storage_engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "internal_tmp_mem_storage_engine").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalTmpMemStorageEngine", value)

    @builtins.property
    @jsii.member(jsii_name="ipFilter")
    def ip_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipFilter"))

    @ip_filter.setter
    def ip_filter(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "ip_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipFilter", value)

    @builtins.property
    @jsii.member(jsii_name="longQueryTime")
    def long_query_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longQueryTime"))

    @long_query_time.setter
    def long_query_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "long_query_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longQueryTime", value)

    @builtins.property
    @jsii.member(jsii_name="maxAllowedPacket")
    def max_allowed_packet(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAllowedPacket"))

    @max_allowed_packet.setter
    def max_allowed_packet(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "max_allowed_packet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAllowedPacket", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeapTableSize")
    def max_heap_table_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxHeapTableSize"))

    @max_heap_table_size.setter
    def max_heap_table_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "max_heap_table_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeapTableSize", value)

    @builtins.property
    @jsii.member(jsii_name="netReadTimeout")
    def net_read_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netReadTimeout"))

    @net_read_timeout.setter
    def net_read_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "net_read_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netReadTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="netWriteTimeout")
    def net_write_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netWriteTimeout"))

    @net_write_timeout.setter
    def net_write_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "net_write_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netWriteTimeout", value)

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
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "public_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAccess", value)

    @builtins.property
    @jsii.member(jsii_name="slowQueryLog")
    def slow_query_log(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "slowQueryLog"))

    @slow_query_log.setter
    def slow_query_log(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "slow_query_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slowQueryLog", value)

    @builtins.property
    @jsii.member(jsii_name="sortBufferSize")
    def sort_buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sortBufferSize"))

    @sort_buffer_size.setter
    def sort_buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "sort_buffer_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortBufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="sqlMode")
    def sql_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlMode"))

    @sql_mode.setter
    def sql_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "sql_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlMode", value)

    @builtins.property
    @jsii.member(jsii_name="sqlRequirePrimaryKey")
    def sql_require_primary_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sqlRequirePrimaryKey"))

    @sql_require_primary_key.setter
    def sql_require_primary_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "sql_require_primary_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlRequirePrimaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="tmpTableSize")
    def tmp_table_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tmpTableSize"))

    @tmp_table_size.setter
    def tmp_table_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "tmp_table_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tmpTableSize", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="waitTimeout")
    def wait_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitTimeout"))

    @wait_timeout.setter
    def wait_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "wait_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabaseMysqlProperties]:
        return typing.cast(typing.Optional[ManagedDatabaseMysqlProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseMysqlProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDatabaseMysqlPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedDatabaseMysql",
    "ManagedDatabaseMysqlComponents",
    "ManagedDatabaseMysqlComponentsList",
    "ManagedDatabaseMysqlComponentsOutputReference",
    "ManagedDatabaseMysqlConfig",
    "ManagedDatabaseMysqlNodeStates",
    "ManagedDatabaseMysqlNodeStatesList",
    "ManagedDatabaseMysqlNodeStatesOutputReference",
    "ManagedDatabaseMysqlProperties",
    "ManagedDatabaseMysqlPropertiesMigration",
    "ManagedDatabaseMysqlPropertiesMigrationOutputReference",
    "ManagedDatabaseMysqlPropertiesOutputReference",
]

publication.publish()
