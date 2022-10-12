'''
# `google_redis_instance`

Refer to the Terraform Registory for docs: [`google_redis_instance`](https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance).
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


class GoogleRedisInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance google_redis_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        memory_size_gb: jsii.Number,
        name: builtins.str,
        alternative_location_id: typing.Optional[builtins.str] = None,
        auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        authorized_network: typing.Optional[builtins.str] = None,
        connect_mode: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        location_id: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["GoogleRedisInstanceMaintenancePolicy", typing.Dict[str, typing.Any]]] = None,
        maintenance_schedule: typing.Optional[typing.Union["GoogleRedisInstanceMaintenanceSchedule", typing.Dict[str, typing.Any]]] = None,
        persistence_config: typing.Optional[typing.Union["GoogleRedisInstancePersistenceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        read_replicas_mode: typing.Optional[builtins.str] = None,
        redis_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redis_version: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        reserved_ip_range: typing.Optional[builtins.str] = None,
        secondary_ip_range: typing.Optional[builtins.str] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleRedisInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        transit_encryption_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance google_redis_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param memory_size_gb: Redis memory size in GiB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#memory_size_gb GoogleRedisInstance#memory_size_gb}
        :param name: The ID of the instance or a fully qualified identifier for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#name GoogleRedisInstance#name}
        :param alternative_location_id: Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones. If provided, it must be a different zone from the one provided in [locationId]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#alternative_location_id GoogleRedisInstance#alternative_location_id}
        :param auth_enabled: Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#auth_enabled GoogleRedisInstance#auth_enabled}
        :param authorized_network: The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default network will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#authorized_network GoogleRedisInstance#authorized_network}
        :param connect_mode: The connection mode of the Redis instance. Default value: "DIRECT_PEERING" Possible values: ["DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#connect_mode GoogleRedisInstance#connect_mode}
        :param customer_managed_key: Optional. The KMS key reference that you want to use to encrypt the data at rest for this Redis instance. If this is provided, CMEK is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#customer_managed_key GoogleRedisInstance#customer_managed_key}
        :param display_name: An arbitrary and optional user-provided name for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#display_name GoogleRedisInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#id GoogleRedisInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels to represent user provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#labels GoogleRedisInstance#labels}
        :param location_id: The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If [alternativeLocationId] is also provided, it must be different from [locationId]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#location_id GoogleRedisInstance#location_id}
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_policy GoogleRedisInstance#maintenance_policy}
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_schedule GoogleRedisInstance#maintenance_schedule}
        :param persistence_config: persistence_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_config GoogleRedisInstance#persistence_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#project GoogleRedisInstance#project}.
        :param read_replicas_mode: Optional. Read replica mode. Can only be specified when trying to create the instance. If not set, Memorystore Redis backend will default to READ_REPLICAS_DISABLED. - READ_REPLICAS_DISABLED: If disabled, read endpoint will not be provided and the instance cannot scale up or down the number of replicas. - READ_REPLICAS_ENABLED: If enabled, read endpoint will be provided and the instance can scale up and down the number of replicas. Possible values: ["READ_REPLICAS_DISABLED", "READ_REPLICAS_ENABLED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#read_replicas_mode GoogleRedisInstance#read_replicas_mode}
        :param redis_configs: Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for the list of supported parameters: https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_configs GoogleRedisInstance#redis_configs}
        :param redis_version: The version of Redis software. If not provided, latest supported version will be used. Please check the API documentation linked at the top for the latest valid values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_version GoogleRedisInstance#redis_version}
        :param region: The name of the Redis region of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#region GoogleRedisInstance#region}
        :param replica_count: Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#replica_count GoogleRedisInstance#replica_count}
        :param reserved_ip_range: The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets in an authorized network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#reserved_ip_range GoogleRedisInstance#reserved_ip_range}
        :param secondary_ip_range: Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#secondary_ip_range GoogleRedisInstance#secondary_ip_range}
        :param tier: The service tier of the instance. Must be one of these values:. - BASIC: standalone instance - STANDARD_HA: highly available primary/replica instances Default value: "BASIC" Possible values: ["BASIC", "STANDARD_HA"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#tier GoogleRedisInstance#tier}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#timeouts GoogleRedisInstance#timeouts}
        :param transit_encryption_mode: The TLS mode of the Redis instance, If not provided, TLS is disabled for the instance. - SERVER_AUTHENTICATION: Client to Server traffic encryption enabled with server authentication Default value: "DISABLED" Possible values: ["SERVER_AUTHENTICATION", "DISABLED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#transit_encryption_mode GoogleRedisInstance#transit_encryption_mode}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleRedisInstanceConfig(
            memory_size_gb=memory_size_gb,
            name=name,
            alternative_location_id=alternative_location_id,
            auth_enabled=auth_enabled,
            authorized_network=authorized_network,
            connect_mode=connect_mode,
            customer_managed_key=customer_managed_key,
            display_name=display_name,
            id=id,
            labels=labels,
            location_id=location_id,
            maintenance_policy=maintenance_policy,
            maintenance_schedule=maintenance_schedule,
            persistence_config=persistence_config,
            project=project,
            read_replicas_mode=read_replicas_mode,
            redis_configs=redis_configs,
            redis_version=redis_version,
            region=region,
            replica_count=replica_count,
            reserved_ip_range=reserved_ip_range,
            secondary_ip_range=secondary_ip_range,
            tier=tier,
            timeouts=timeouts,
            transit_encryption_mode=transit_encryption_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMaintenancePolicy")
    def put_maintenance_policy(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        weekly_maintenance_window: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param description: Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#description GoogleRedisInstance#description}
        :param weekly_maintenance_window: weekly_maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#weekly_maintenance_window GoogleRedisInstance#weekly_maintenance_window}
        '''
        value = GoogleRedisInstanceMaintenancePolicy(
            description=description,
            weekly_maintenance_window=weekly_maintenance_window,
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenancePolicy", [value]))

    @jsii.member(jsii_name="putMaintenanceSchedule")
    def put_maintenance_schedule(self) -> None:
        value = GoogleRedisInstanceMaintenanceSchedule()

        return typing.cast(None, jsii.invoke(self, "putMaintenanceSchedule", [value]))

    @jsii.member(jsii_name="putPersistenceConfig")
    def put_persistence_config(
        self,
        *,
        rdb_snapshot_period: builtins.str,
        persistence_mode: typing.Optional[builtins.str] = None,
        rdb_snapshot_start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rdb_snapshot_period: Optional. Available snapshot periods for scheduling. - ONE_HOUR: Snapshot every 1 hour. - SIX_HOURS: Snapshot every 6 hours. - TWELVE_HOURS: Snapshot every 12 hours. - TWENTY_FOUR_HOURS: Snapshot every 24 horus. Possible values: ["ONE_HOUR", "SIX_HOURS", "TWELVE_HOURS", "TWENTY_FOUR_HOURS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_period GoogleRedisInstance#rdb_snapshot_period}
        :param persistence_mode: Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. - DISABLED: Persistence is disabled for the instance, and any existing snapshots are deleted. - RDB: RDB based Persistence is enabled. Possible values: ["DISABLED", "RDB"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_mode GoogleRedisInstance#persistence_mode}
        :param rdb_snapshot_start_time: Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_start_time GoogleRedisInstance#rdb_snapshot_start_time}
        '''
        value = GoogleRedisInstancePersistenceConfig(
            rdb_snapshot_period=rdb_snapshot_period,
            persistence_mode=persistence_mode,
            rdb_snapshot_start_time=rdb_snapshot_start_time,
        )

        return typing.cast(None, jsii.invoke(self, "putPersistenceConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#create GoogleRedisInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#delete GoogleRedisInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#update GoogleRedisInstance#update}.
        '''
        value = GoogleRedisInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlternativeLocationId")
    def reset_alternative_location_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternativeLocationId", []))

    @jsii.member(jsii_name="resetAuthEnabled")
    def reset_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthEnabled", []))

    @jsii.member(jsii_name="resetAuthorizedNetwork")
    def reset_authorized_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizedNetwork", []))

    @jsii.member(jsii_name="resetConnectMode")
    def reset_connect_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectMode", []))

    @jsii.member(jsii_name="resetCustomerManagedKey")
    def reset_customer_managed_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKey", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLocationId")
    def reset_location_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationId", []))

    @jsii.member(jsii_name="resetMaintenancePolicy")
    def reset_maintenance_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenancePolicy", []))

    @jsii.member(jsii_name="resetMaintenanceSchedule")
    def reset_maintenance_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceSchedule", []))

    @jsii.member(jsii_name="resetPersistenceConfig")
    def reset_persistence_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistenceConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetReadReplicasMode")
    def reset_read_replicas_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadReplicasMode", []))

    @jsii.member(jsii_name="resetRedisConfigs")
    def reset_redis_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisConfigs", []))

    @jsii.member(jsii_name="resetRedisVersion")
    def reset_redis_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisVersion", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetReplicaCount")
    def reset_replica_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicaCount", []))

    @jsii.member(jsii_name="resetReservedIpRange")
    def reset_reserved_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservedIpRange", []))

    @jsii.member(jsii_name="resetSecondaryIpRange")
    def reset_secondary_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryIpRange", []))

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransitEncryptionMode")
    def reset_transit_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryptionMode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authString")
    def auth_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authString"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="currentLocationId")
    def current_location_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentLocationId"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicy")
    def maintenance_policy(
        self,
    ) -> "GoogleRedisInstanceMaintenancePolicyOutputReference":
        return typing.cast("GoogleRedisInstanceMaintenancePolicyOutputReference", jsii.get(self, "maintenancePolicy"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceSchedule")
    def maintenance_schedule(
        self,
    ) -> "GoogleRedisInstanceMaintenanceScheduleOutputReference":
        return typing.cast("GoogleRedisInstanceMaintenanceScheduleOutputReference", jsii.get(self, "maintenanceSchedule"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> "GoogleRedisInstanceNodesList":
        return typing.cast("GoogleRedisInstanceNodesList", jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="persistenceConfig")
    def persistence_config(
        self,
    ) -> "GoogleRedisInstancePersistenceConfigOutputReference":
        return typing.cast("GoogleRedisInstancePersistenceConfigOutputReference", jsii.get(self, "persistenceConfig"))

    @builtins.property
    @jsii.member(jsii_name="persistenceIamIdentity")
    def persistence_iam_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistenceIamIdentity"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="readEndpoint")
    def read_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="readEndpointPort")
    def read_endpoint_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="serverCaCerts")
    def server_ca_certs(self) -> "GoogleRedisInstanceServerCaCertsList":
        return typing.cast("GoogleRedisInstanceServerCaCertsList", jsii.get(self, "serverCaCerts"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleRedisInstanceTimeoutsOutputReference":
        return typing.cast("GoogleRedisInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alternativeLocationIdInput")
    def alternative_location_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alternativeLocationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authEnabledInput")
    def auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "authEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizedNetworkInput")
    def authorized_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizedNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="connectModeInput")
    def connect_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectModeInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyInput")
    def customer_managed_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationIdInput")
    def location_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicyInput")
    def maintenance_policy_input(
        self,
    ) -> typing.Optional["GoogleRedisInstanceMaintenancePolicy"]:
        return typing.cast(typing.Optional["GoogleRedisInstanceMaintenancePolicy"], jsii.get(self, "maintenancePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceScheduleInput")
    def maintenance_schedule_input(
        self,
    ) -> typing.Optional["GoogleRedisInstanceMaintenanceSchedule"]:
        return typing.cast(typing.Optional["GoogleRedisInstanceMaintenanceSchedule"], jsii.get(self, "maintenanceScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySizeGbInput")
    def memory_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="persistenceConfigInput")
    def persistence_config_input(
        self,
    ) -> typing.Optional["GoogleRedisInstancePersistenceConfig"]:
        return typing.cast(typing.Optional["GoogleRedisInstancePersistenceConfig"], jsii.get(self, "persistenceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="readReplicasModeInput")
    def read_replicas_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readReplicasModeInput"))

    @builtins.property
    @jsii.member(jsii_name="redisConfigsInput")
    def redis_configs_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "redisConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="redisVersionInput")
    def redis_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redisVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaCountInput")
    def replica_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicaCountInput"))

    @builtins.property
    @jsii.member(jsii_name="reservedIpRangeInput")
    def reserved_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reservedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryIpRangeInput")
    def secondary_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleRedisInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleRedisInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionModeInput")
    def transit_encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitEncryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="alternativeLocationId")
    def alternative_location_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alternativeLocationId"))

    @alternative_location_id.setter
    def alternative_location_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "alternative_location_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alternativeLocationId", value)

    @builtins.property
    @jsii.member(jsii_name="authEnabled")
    def auth_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "authEnabled"))

    @auth_enabled.setter
    def auth_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "auth_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedNetwork")
    def authorized_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizedNetwork"))

    @authorized_network.setter
    def authorized_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "authorized_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="connectMode")
    def connect_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectMode"))

    @connect_mode.setter
    def connect_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "connect_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectMode", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerManagedKey"))

    @customer_managed_key.setter
    def customer_managed_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "customer_managed_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKey", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="locationId")
    def location_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationId"))

    @location_id.setter
    def location_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "location_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationId", value)

    @builtins.property
    @jsii.member(jsii_name="memorySizeGb")
    def memory_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySizeGb"))

    @memory_size_gb.setter
    def memory_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "memory_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="readReplicasMode")
    def read_replicas_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readReplicasMode"))

    @read_replicas_mode.setter
    def read_replicas_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "read_replicas_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readReplicasMode", value)

    @builtins.property
    @jsii.member(jsii_name="redisConfigs")
    def redis_configs(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "redisConfigs"))

    @redis_configs.setter
    def redis_configs(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "redis_configs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redisConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="redisVersion")
    def redis_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redisVersion"))

    @redis_version.setter
    def redis_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "redis_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redisVersion", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="replicaCount")
    def replica_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicaCount"))

    @replica_count.setter
    def replica_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "replica_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaCount", value)

    @builtins.property
    @jsii.member(jsii_name="reservedIpRange")
    def reserved_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reservedIpRange"))

    @reserved_ip_range.setter
    def reserved_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "reserved_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservedIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryIpRange")
    def secondary_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryIpRange"))

    @secondary_ip_range.setter
    def secondary_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "secondary_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionMode")
    def transit_encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitEncryptionMode"))

    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstance, "transit_encryption_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "memory_size_gb": "memorySizeGb",
        "name": "name",
        "alternative_location_id": "alternativeLocationId",
        "auth_enabled": "authEnabled",
        "authorized_network": "authorizedNetwork",
        "connect_mode": "connectMode",
        "customer_managed_key": "customerManagedKey",
        "display_name": "displayName",
        "id": "id",
        "labels": "labels",
        "location_id": "locationId",
        "maintenance_policy": "maintenancePolicy",
        "maintenance_schedule": "maintenanceSchedule",
        "persistence_config": "persistenceConfig",
        "project": "project",
        "read_replicas_mode": "readReplicasMode",
        "redis_configs": "redisConfigs",
        "redis_version": "redisVersion",
        "region": "region",
        "replica_count": "replicaCount",
        "reserved_ip_range": "reservedIpRange",
        "secondary_ip_range": "secondaryIpRange",
        "tier": "tier",
        "timeouts": "timeouts",
        "transit_encryption_mode": "transitEncryptionMode",
    },
)
class GoogleRedisInstanceConfig(cdktf.TerraformMetaArguments):
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
        memory_size_gb: jsii.Number,
        name: builtins.str,
        alternative_location_id: typing.Optional[builtins.str] = None,
        auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        authorized_network: typing.Optional[builtins.str] = None,
        connect_mode: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        location_id: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["GoogleRedisInstanceMaintenancePolicy", typing.Dict[str, typing.Any]]] = None,
        maintenance_schedule: typing.Optional[typing.Union["GoogleRedisInstanceMaintenanceSchedule", typing.Dict[str, typing.Any]]] = None,
        persistence_config: typing.Optional[typing.Union["GoogleRedisInstancePersistenceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        read_replicas_mode: typing.Optional[builtins.str] = None,
        redis_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redis_version: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        reserved_ip_range: typing.Optional[builtins.str] = None,
        secondary_ip_range: typing.Optional[builtins.str] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleRedisInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        transit_encryption_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param memory_size_gb: Redis memory size in GiB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#memory_size_gb GoogleRedisInstance#memory_size_gb}
        :param name: The ID of the instance or a fully qualified identifier for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#name GoogleRedisInstance#name}
        :param alternative_location_id: Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones. If provided, it must be a different zone from the one provided in [locationId]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#alternative_location_id GoogleRedisInstance#alternative_location_id}
        :param auth_enabled: Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#auth_enabled GoogleRedisInstance#auth_enabled}
        :param authorized_network: The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default network will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#authorized_network GoogleRedisInstance#authorized_network}
        :param connect_mode: The connection mode of the Redis instance. Default value: "DIRECT_PEERING" Possible values: ["DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#connect_mode GoogleRedisInstance#connect_mode}
        :param customer_managed_key: Optional. The KMS key reference that you want to use to encrypt the data at rest for this Redis instance. If this is provided, CMEK is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#customer_managed_key GoogleRedisInstance#customer_managed_key}
        :param display_name: An arbitrary and optional user-provided name for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#display_name GoogleRedisInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#id GoogleRedisInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels to represent user provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#labels GoogleRedisInstance#labels}
        :param location_id: The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If [alternativeLocationId] is also provided, it must be different from [locationId]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#location_id GoogleRedisInstance#location_id}
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_policy GoogleRedisInstance#maintenance_policy}
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_schedule GoogleRedisInstance#maintenance_schedule}
        :param persistence_config: persistence_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_config GoogleRedisInstance#persistence_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#project GoogleRedisInstance#project}.
        :param read_replicas_mode: Optional. Read replica mode. Can only be specified when trying to create the instance. If not set, Memorystore Redis backend will default to READ_REPLICAS_DISABLED. - READ_REPLICAS_DISABLED: If disabled, read endpoint will not be provided and the instance cannot scale up or down the number of replicas. - READ_REPLICAS_ENABLED: If enabled, read endpoint will be provided and the instance can scale up and down the number of replicas. Possible values: ["READ_REPLICAS_DISABLED", "READ_REPLICAS_ENABLED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#read_replicas_mode GoogleRedisInstance#read_replicas_mode}
        :param redis_configs: Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for the list of supported parameters: https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_configs GoogleRedisInstance#redis_configs}
        :param redis_version: The version of Redis software. If not provided, latest supported version will be used. Please check the API documentation linked at the top for the latest valid values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_version GoogleRedisInstance#redis_version}
        :param region: The name of the Redis region of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#region GoogleRedisInstance#region}
        :param replica_count: Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#replica_count GoogleRedisInstance#replica_count}
        :param reserved_ip_range: The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing subnets in an authorized network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#reserved_ip_range GoogleRedisInstance#reserved_ip_range}
        :param secondary_ip_range: Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#secondary_ip_range GoogleRedisInstance#secondary_ip_range}
        :param tier: The service tier of the instance. Must be one of these values:. - BASIC: standalone instance - STANDARD_HA: highly available primary/replica instances Default value: "BASIC" Possible values: ["BASIC", "STANDARD_HA"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#tier GoogleRedisInstance#tier}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#timeouts GoogleRedisInstance#timeouts}
        :param transit_encryption_mode: The TLS mode of the Redis instance, If not provided, TLS is disabled for the instance. - SERVER_AUTHENTICATION: Client to Server traffic encryption enabled with server authentication Default value: "DISABLED" Possible values: ["SERVER_AUTHENTICATION", "DISABLED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#transit_encryption_mode GoogleRedisInstance#transit_encryption_mode}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(maintenance_policy, dict):
            maintenance_policy = GoogleRedisInstanceMaintenancePolicy(**maintenance_policy)
        if isinstance(maintenance_schedule, dict):
            maintenance_schedule = GoogleRedisInstanceMaintenanceSchedule(**maintenance_schedule)
        if isinstance(persistence_config, dict):
            persistence_config = GoogleRedisInstancePersistenceConfig(**persistence_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleRedisInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument memory_size_gb", value=memory_size_gb, expected_type=type_hints["memory_size_gb"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alternative_location_id", value=alternative_location_id, expected_type=type_hints["alternative_location_id"])
            check_type(argname="argument auth_enabled", value=auth_enabled, expected_type=type_hints["auth_enabled"])
            check_type(argname="argument authorized_network", value=authorized_network, expected_type=type_hints["authorized_network"])
            check_type(argname="argument connect_mode", value=connect_mode, expected_type=type_hints["connect_mode"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument location_id", value=location_id, expected_type=type_hints["location_id"])
            check_type(argname="argument maintenance_policy", value=maintenance_policy, expected_type=type_hints["maintenance_policy"])
            check_type(argname="argument maintenance_schedule", value=maintenance_schedule, expected_type=type_hints["maintenance_schedule"])
            check_type(argname="argument persistence_config", value=persistence_config, expected_type=type_hints["persistence_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument read_replicas_mode", value=read_replicas_mode, expected_type=type_hints["read_replicas_mode"])
            check_type(argname="argument redis_configs", value=redis_configs, expected_type=type_hints["redis_configs"])
            check_type(argname="argument redis_version", value=redis_version, expected_type=type_hints["redis_version"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument reserved_ip_range", value=reserved_ip_range, expected_type=type_hints["reserved_ip_range"])
            check_type(argname="argument secondary_ip_range", value=secondary_ip_range, expected_type=type_hints["secondary_ip_range"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transit_encryption_mode", value=transit_encryption_mode, expected_type=type_hints["transit_encryption_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "memory_size_gb": memory_size_gb,
            "name": name,
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
        if alternative_location_id is not None:
            self._values["alternative_location_id"] = alternative_location_id
        if auth_enabled is not None:
            self._values["auth_enabled"] = auth_enabled
        if authorized_network is not None:
            self._values["authorized_network"] = authorized_network
        if connect_mode is not None:
            self._values["connect_mode"] = connect_mode
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if location_id is not None:
            self._values["location_id"] = location_id
        if maintenance_policy is not None:
            self._values["maintenance_policy"] = maintenance_policy
        if maintenance_schedule is not None:
            self._values["maintenance_schedule"] = maintenance_schedule
        if persistence_config is not None:
            self._values["persistence_config"] = persistence_config
        if project is not None:
            self._values["project"] = project
        if read_replicas_mode is not None:
            self._values["read_replicas_mode"] = read_replicas_mode
        if redis_configs is not None:
            self._values["redis_configs"] = redis_configs
        if redis_version is not None:
            self._values["redis_version"] = redis_version
        if region is not None:
            self._values["region"] = region
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if reserved_ip_range is not None:
            self._values["reserved_ip_range"] = reserved_ip_range
        if secondary_ip_range is not None:
            self._values["secondary_ip_range"] = secondary_ip_range
        if tier is not None:
            self._values["tier"] = tier
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transit_encryption_mode is not None:
            self._values["transit_encryption_mode"] = transit_encryption_mode

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
    def memory_size_gb(self) -> jsii.Number:
        '''Redis memory size in GiB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#memory_size_gb GoogleRedisInstance#memory_size_gb}
        '''
        result = self._values.get("memory_size_gb")
        assert result is not None, "Required property 'memory_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The ID of the instance or a fully qualified identifier for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#name GoogleRedisInstance#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alternative_location_id(self) -> typing.Optional[builtins.str]:
        '''Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two zones.

        If provided, it must be a different zone from the one provided in
        [locationId].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#alternative_location_id GoogleRedisInstance#alternative_location_id}
        '''
        result = self._values.get("alternative_location_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Indicates whether OSS Redis AUTH is enabled for the
        instance. If set to "true" AUTH is enabled on the instance.
        Default value is "false" meaning AUTH is disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#auth_enabled GoogleRedisInstance#auth_enabled}
        '''
        result = self._values.get("auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def authorized_network(self) -> typing.Optional[builtins.str]:
        '''The full name of the Google Compute Engine network to which the instance is connected.

        If left unspecified, the default network
        will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#authorized_network GoogleRedisInstance#authorized_network}
        '''
        result = self._values.get("authorized_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connect_mode(self) -> typing.Optional[builtins.str]:
        '''The connection mode of the Redis instance. Default value: "DIRECT_PEERING" Possible values: ["DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#connect_mode GoogleRedisInstance#connect_mode}
        '''
        result = self._values.get("connect_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The KMS key reference that you want to use to encrypt the data at rest for this Redis
        instance. If this is provided, CMEK is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#customer_managed_key GoogleRedisInstance#customer_managed_key}
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''An arbitrary and optional user-provided name for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#display_name GoogleRedisInstance#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#id GoogleRedisInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Resource labels to represent user provided metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#labels GoogleRedisInstance#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def location_id(self) -> typing.Optional[builtins.str]:
        '''The zone where the instance will be provisioned.

        If not provided,
        the service will choose a zone for the instance. For STANDARD_HA tier,
        instances will be created across two zones for protection against
        zonal failures. If [alternativeLocationId] is also provided, it must
        be different from [locationId].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#location_id GoogleRedisInstance#location_id}
        '''
        result = self._values.get("location_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_policy(
        self,
    ) -> typing.Optional["GoogleRedisInstanceMaintenancePolicy"]:
        '''maintenance_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_policy GoogleRedisInstance#maintenance_policy}
        '''
        result = self._values.get("maintenance_policy")
        return typing.cast(typing.Optional["GoogleRedisInstanceMaintenancePolicy"], result)

    @builtins.property
    def maintenance_schedule(
        self,
    ) -> typing.Optional["GoogleRedisInstanceMaintenanceSchedule"]:
        '''maintenance_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#maintenance_schedule GoogleRedisInstance#maintenance_schedule}
        '''
        result = self._values.get("maintenance_schedule")
        return typing.cast(typing.Optional["GoogleRedisInstanceMaintenanceSchedule"], result)

    @builtins.property
    def persistence_config(
        self,
    ) -> typing.Optional["GoogleRedisInstancePersistenceConfig"]:
        '''persistence_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_config GoogleRedisInstance#persistence_config}
        '''
        result = self._values.get("persistence_config")
        return typing.cast(typing.Optional["GoogleRedisInstancePersistenceConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#project GoogleRedisInstance#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_replicas_mode(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Read replica mode. Can only be specified when trying to create the instance.
        If not set, Memorystore Redis backend will default to READ_REPLICAS_DISABLED.

        - READ_REPLICAS_DISABLED: If disabled, read endpoint will not be provided and the
          instance cannot scale up or down the number of replicas.
        - READ_REPLICAS_ENABLED: If enabled, read endpoint will be provided and the instance
          can scale up and down the number of replicas. Possible values: ["READ_REPLICAS_DISABLED", "READ_REPLICAS_ENABLED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#read_replicas_mode GoogleRedisInstance#read_replicas_mode}
        '''
        result = self._values.get("read_replicas_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redis_configs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for the list of supported parameters: https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_configs GoogleRedisInstance#redis_configs}
        '''
        result = self._values.get("redis_configs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def redis_version(self) -> typing.Optional[builtins.str]:
        '''The version of Redis software.

        If not provided, latest supported
        version will be used. Please check the API documentation linked
        at the top for the latest valid values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#redis_version GoogleRedisInstance#redis_version}
        '''
        result = self._values.get("redis_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The name of the Redis region of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#region GoogleRedisInstance#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        The number of replica nodes. The valid range for the Standard Tier with
        read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled
        for a Standard Tier instance, the only valid value is 1 and the default is 1.
        The valid value for basic tier is 0 and the default is also 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#replica_count GoogleRedisInstance#replica_count}
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reserved_ip_range(self) -> typing.Optional[builtins.str]:
        '''The CIDR range of internal addresses that are reserved for this instance.

        If not provided, the service will choose an unused /29
        block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
        unique and non-overlapping with existing subnets in an authorized
        network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#reserved_ip_range GoogleRedisInstance#reserved_ip_range}
        '''
        result = self._values.get("reserved_ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_ip_range(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Additional IP range for node placement. Required when enabling read replicas on
        an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or
        "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address
        range associated with the private service access connection, or "auto".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#secondary_ip_range GoogleRedisInstance#secondary_ip_range}
        '''
        result = self._values.get("secondary_ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''The service tier of the instance. Must be one of these values:.

        - BASIC: standalone instance
        - STANDARD_HA: highly available primary/replica instances Default value: "BASIC" Possible values: ["BASIC", "STANDARD_HA"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#tier GoogleRedisInstance#tier}
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleRedisInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#timeouts GoogleRedisInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleRedisInstanceTimeouts"], result)

    @builtins.property
    def transit_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''The TLS mode of the Redis instance, If not provided, TLS is disabled for the instance.

        - SERVER_AUTHENTICATION: Client to Server traffic encryption enabled with server authentication Default value: "DISABLED" Possible values: ["SERVER_AUTHENTICATION", "DISABLED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#transit_encryption_mode GoogleRedisInstance#transit_encryption_mode}
        '''
        result = self._values.get("transit_encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "weekly_maintenance_window": "weeklyMaintenanceWindow",
    },
)
class GoogleRedisInstanceMaintenancePolicy:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        weekly_maintenance_window: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param description: Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#description GoogleRedisInstance#description}
        :param weekly_maintenance_window: weekly_maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#weekly_maintenance_window GoogleRedisInstance#weekly_maintenance_window}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicy.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument weekly_maintenance_window", value=weekly_maintenance_window, expected_type=type_hints["weekly_maintenance_window"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if weekly_maintenance_window is not None:
            self._values["weekly_maintenance_window"] = weekly_maintenance_window

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#description GoogleRedisInstance#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_maintenance_window(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow"]]]:
        '''weekly_maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#weekly_maintenance_window GoogleRedisInstance#weekly_maintenance_window}
        '''
        result = self._values.get("weekly_maintenance_window")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceMaintenancePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceMaintenancePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeeklyMaintenanceWindow")
    def put_weekly_maintenance_window(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyOutputReference.put_weekly_maintenance_window)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeeklyMaintenanceWindow", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetWeeklyMaintenanceWindow")
    def reset_weekly_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyMaintenanceWindow", []))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindow")
    def weekly_maintenance_window(
        self,
    ) -> "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList":
        return typing.cast("GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList", jsii.get(self, "weeklyMaintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindowInput")
    def weekly_maintenance_window_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow"]]], jsii.get(self, "weeklyMaintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleRedisInstanceMaintenancePolicy]:
        return typing.cast(typing.Optional[GoogleRedisInstanceMaintenancePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleRedisInstanceMaintenancePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "start_time": "startTime"},
)
class GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow:
    def __init__(
        self,
        *,
        day: builtins.str,
        start_time: typing.Union["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param day: Required. The day of week that maintenance updates occur. - DAY_OF_WEEK_UNSPECIFIED: The day of the week is unspecified. - MONDAY: Monday - TUESDAY: Tuesday - WEDNESDAY: Wednesday - THURSDAY: Thursday - FRIDAY: Friday - SATURDAY: Saturday - SUNDAY: Sunday Possible values: ["DAY_OF_WEEK_UNSPECIFIED", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#day GoogleRedisInstance#day}
        :param start_time: start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#start_time GoogleRedisInstance#start_time}
        '''
        if isinstance(start_time, dict):
            start_time = GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(**start_time)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "start_time": start_time,
        }

    @builtins.property
    def day(self) -> builtins.str:
        '''Required. The day of week that maintenance updates occur.

        - DAY_OF_WEEK_UNSPECIFIED: The day of the week is unspecified.
        - MONDAY: Monday
        - TUESDAY: Tuesday
        - WEDNESDAY: Wednesday
        - THURSDAY: Thursday
        - FRIDAY: Friday
        - SATURDAY: Saturday
        - SUNDAY: Sunday Possible values: ["DAY_OF_WEEK_UNSPECIFIED", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#day GoogleRedisInstance#day}
        '''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(
        self,
    ) -> "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime":
        '''start_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#start_time GoogleRedisInstance#start_time}
        '''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast("GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStartTime")
    def put_start_time(
        self,
        *,
        hours: typing.Optional[jsii.Number] = None,
        minutes: typing.Optional[jsii.Number] = None,
        nanos: typing.Optional[jsii.Number] = None,
        seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#hours GoogleRedisInstance#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#minutes GoogleRedisInstance#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#nanos GoogleRedisInstance#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#seconds GoogleRedisInstance#seconds}
        '''
        value = GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(
            hours=hours, minutes=minutes, nanos=nanos, seconds=seconds
        )

        return typing.cast(None, jsii.invoke(self, "putStartTime", [value]))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(
        self,
    ) -> "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference":
        return typing.cast("GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference", jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(
        self,
    ) -> typing.Optional["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime"]:
        return typing.cast(typing.Optional["GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime"], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "day"))

    @day.setter
    def day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime",
    jsii_struct_bases=[],
    name_mapping={
        "hours": "hours",
        "minutes": "minutes",
        "nanos": "nanos",
        "seconds": "seconds",
    },
)
class GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime:
    def __init__(
        self,
        *,
        hours: typing.Optional[jsii.Number] = None,
        minutes: typing.Optional[jsii.Number] = None,
        nanos: typing.Optional[jsii.Number] = None,
        seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#hours GoogleRedisInstance#hours}
        :param minutes: Minutes of hour of day. Must be from 0 to 59. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#minutes GoogleRedisInstance#minutes}
        :param nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#nanos GoogleRedisInstance#nanos}
        :param seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#seconds GoogleRedisInstance#seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime.__init__)
            check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hours is not None:
            self._values["hours"] = hours
        if minutes is not None:
            self._values["minutes"] = minutes
        if nanos is not None:
            self._values["nanos"] = nanos
        if seconds is not None:
            self._values["seconds"] = seconds

    @builtins.property
    def hours(self) -> typing.Optional[jsii.Number]:
        '''Hours of day in 24 hour format.

        Should be from 0 to 23.
        An API may choose to allow the value "24:00:00" for scenarios like business closing time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#hours GoogleRedisInstance#hours}
        '''
        result = self._values.get("hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minutes(self) -> typing.Optional[jsii.Number]:
        '''Minutes of hour of day. Must be from 0 to 59.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#minutes GoogleRedisInstance#minutes}
        '''
        result = self._values.get("minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#nanos GoogleRedisInstance#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seconds(self) -> typing.Optional[jsii.Number]:
        '''Seconds of minutes of the time.

        Must normally be from 0 to 59.
        An API may allow the value 60 if it allows leap-seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#seconds GoogleRedisInstance#seconds}
        '''
        result = self._values.get("seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHours")
    def reset_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHours", []))

    @jsii.member(jsii_name="resetMinutes")
    def reset_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinutes", []))

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @jsii.member(jsii_name="resetSeconds")
    def reset_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="hoursInput")
    def hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hoursInput"))

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @hours.setter
    def hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference, "hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hours", value)

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference, "minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime]:
        return typing.cast(typing.Optional[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenanceSchedule",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleRedisInstanceMaintenanceSchedule:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceMaintenanceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceMaintenanceScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceMaintenanceScheduleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceMaintenanceScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @builtins.property
    @jsii.member(jsii_name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleDeadlineTime"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleRedisInstanceMaintenanceSchedule]:
        return typing.cast(typing.Optional[GoogleRedisInstanceMaintenanceSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleRedisInstanceMaintenanceSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceMaintenanceScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceNodes",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleRedisInstanceNodes:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceNodesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceNodesList",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceNodesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleRedisInstanceNodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceNodesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleRedisInstanceNodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceNodesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceNodesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceNodesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleRedisInstanceNodesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceNodesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceNodesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleRedisInstanceNodes]:
        return typing.cast(typing.Optional[GoogleRedisInstanceNodes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleRedisInstanceNodes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceNodesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstancePersistenceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "rdb_snapshot_period": "rdbSnapshotPeriod",
        "persistence_mode": "persistenceMode",
        "rdb_snapshot_start_time": "rdbSnapshotStartTime",
    },
)
class GoogleRedisInstancePersistenceConfig:
    def __init__(
        self,
        *,
        rdb_snapshot_period: builtins.str,
        persistence_mode: typing.Optional[builtins.str] = None,
        rdb_snapshot_start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rdb_snapshot_period: Optional. Available snapshot periods for scheduling. - ONE_HOUR: Snapshot every 1 hour. - SIX_HOURS: Snapshot every 6 hours. - TWELVE_HOURS: Snapshot every 12 hours. - TWENTY_FOUR_HOURS: Snapshot every 24 horus. Possible values: ["ONE_HOUR", "SIX_HOURS", "TWELVE_HOURS", "TWENTY_FOUR_HOURS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_period GoogleRedisInstance#rdb_snapshot_period}
        :param persistence_mode: Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. - DISABLED: Persistence is disabled for the instance, and any existing snapshots are deleted. - RDB: RDB based Persistence is enabled. Possible values: ["DISABLED", "RDB"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_mode GoogleRedisInstance#persistence_mode}
        :param rdb_snapshot_start_time: Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_start_time GoogleRedisInstance#rdb_snapshot_start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstancePersistenceConfig.__init__)
            check_type(argname="argument rdb_snapshot_period", value=rdb_snapshot_period, expected_type=type_hints["rdb_snapshot_period"])
            check_type(argname="argument persistence_mode", value=persistence_mode, expected_type=type_hints["persistence_mode"])
            check_type(argname="argument rdb_snapshot_start_time", value=rdb_snapshot_start_time, expected_type=type_hints["rdb_snapshot_start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "rdb_snapshot_period": rdb_snapshot_period,
        }
        if persistence_mode is not None:
            self._values["persistence_mode"] = persistence_mode
        if rdb_snapshot_start_time is not None:
            self._values["rdb_snapshot_start_time"] = rdb_snapshot_start_time

    @builtins.property
    def rdb_snapshot_period(self) -> builtins.str:
        '''Optional. Available snapshot periods for scheduling.

        - ONE_HOUR:	Snapshot every 1 hour.
        - SIX_HOURS:	Snapshot every 6 hours.
        - TWELVE_HOURS:	Snapshot every 12 hours.
        - TWENTY_FOUR_HOURS:	Snapshot every 24 horus. Possible values: ["ONE_HOUR", "SIX_HOURS", "TWELVE_HOURS", "TWENTY_FOUR_HOURS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_period GoogleRedisInstance#rdb_snapshot_period}
        '''
        result = self._values.get("rdb_snapshot_period")
        assert result is not None, "Required property 'rdb_snapshot_period' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def persistence_mode(self) -> typing.Optional[builtins.str]:
        '''Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used.

        - DISABLED: 	Persistence is disabled for the instance, and any existing snapshots are deleted.
        - RDB: RDB based Persistence is enabled. Possible values: ["DISABLED", "RDB"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#persistence_mode GoogleRedisInstance#persistence_mode}
        '''
        result = self._values.get("persistence_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rdb_snapshot_start_time(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Date and time that the first snapshot was/will be attempted,
        and to which future snapshots will be aligned. If not provided,
        the current time will be used.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution
        and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#rdb_snapshot_start_time GoogleRedisInstance#rdb_snapshot_start_time}
        '''
        result = self._values.get("rdb_snapshot_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstancePersistenceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstancePersistenceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstancePersistenceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstancePersistenceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPersistenceMode")
    def reset_persistence_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistenceMode", []))

    @jsii.member(jsii_name="resetRdbSnapshotStartTime")
    def reset_rdb_snapshot_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdbSnapshotStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="rdbNextSnapshotTime")
    def rdb_next_snapshot_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rdbNextSnapshotTime"))

    @builtins.property
    @jsii.member(jsii_name="persistenceModeInput")
    def persistence_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "persistenceModeInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbSnapshotPeriodInput")
    def rdb_snapshot_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rdbSnapshotPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbSnapshotStartTimeInput")
    def rdb_snapshot_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rdbSnapshotStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="persistenceMode")
    def persistence_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistenceMode"))

    @persistence_mode.setter
    def persistence_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstancePersistenceConfigOutputReference, "persistence_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistenceMode", value)

    @builtins.property
    @jsii.member(jsii_name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rdbSnapshotPeriod"))

    @rdb_snapshot_period.setter
    def rdb_snapshot_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstancePersistenceConfigOutputReference, "rdb_snapshot_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbSnapshotPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rdbSnapshotStartTime"))

    @rdb_snapshot_start_time.setter
    def rdb_snapshot_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstancePersistenceConfigOutputReference, "rdb_snapshot_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbSnapshotStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleRedisInstancePersistenceConfig]:
        return typing.cast(typing.Optional[GoogleRedisInstancePersistenceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleRedisInstancePersistenceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstancePersistenceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceServerCaCerts",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleRedisInstanceServerCaCerts:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceServerCaCerts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceServerCaCertsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceServerCaCertsList",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceServerCaCertsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleRedisInstanceServerCaCertsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceServerCaCertsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleRedisInstanceServerCaCertsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceServerCaCertsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceServerCaCertsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceServerCaCertsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleRedisInstanceServerCaCertsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceServerCaCertsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceServerCaCertsOutputReference.__init__)
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
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expireTime"))

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serialNumber"))

    @builtins.property
    @jsii.member(jsii_name="sha1Fingerprint")
    def sha1_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha1Fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleRedisInstanceServerCaCerts]:
        return typing.cast(typing.Optional[GoogleRedisInstanceServerCaCerts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleRedisInstanceServerCaCerts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceServerCaCertsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleRedisInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#create GoogleRedisInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#delete GoogleRedisInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#update GoogleRedisInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleRedisInstanceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#create GoogleRedisInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#delete GoogleRedisInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_redis_instance#update GoogleRedisInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleRedisInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleRedisInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleRedisInstance.GoogleRedisInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleRedisInstanceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleRedisInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleRedisInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleRedisInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleRedisInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleRedisInstance",
    "GoogleRedisInstanceConfig",
    "GoogleRedisInstanceMaintenancePolicy",
    "GoogleRedisInstanceMaintenancePolicyOutputReference",
    "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindow",
    "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowList",
    "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowOutputReference",
    "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime",
    "GoogleRedisInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeOutputReference",
    "GoogleRedisInstanceMaintenanceSchedule",
    "GoogleRedisInstanceMaintenanceScheduleOutputReference",
    "GoogleRedisInstanceNodes",
    "GoogleRedisInstanceNodesList",
    "GoogleRedisInstanceNodesOutputReference",
    "GoogleRedisInstancePersistenceConfig",
    "GoogleRedisInstancePersistenceConfigOutputReference",
    "GoogleRedisInstanceServerCaCerts",
    "GoogleRedisInstanceServerCaCertsList",
    "GoogleRedisInstanceServerCaCertsOutputReference",
    "GoogleRedisInstanceTimeouts",
    "GoogleRedisInstanceTimeoutsOutputReference",
]

publication.publish()
