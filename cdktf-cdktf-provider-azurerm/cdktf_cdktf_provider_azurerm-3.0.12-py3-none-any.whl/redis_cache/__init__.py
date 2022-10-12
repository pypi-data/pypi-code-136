'''
# `azurerm_redis_cache`

Refer to the Terraform Registory for docs: [`azurerm_redis_cache`](https://www.terraform.io/docs/providers/azurerm/r/redis_cache).
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


class RedisCache(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCache",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache azurerm_redis_cache}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        capacity: jsii.Number,
        family: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        enable_non_ssl_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["RedisCacheIdentity", typing.Dict[str, typing.Any]]] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        patch_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RedisCachePatchSchedule", typing.Dict[str, typing.Any]]]]] = None,
        private_static_ip_address: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        redis_configuration: typing.Optional[typing.Union["RedisCacheRedisConfiguration", typing.Dict[str, typing.Any]]] = None,
        redis_version: typing.Optional[builtins.str] = None,
        replicas_per_master: typing.Optional[jsii.Number] = None,
        replicas_per_primary: typing.Optional[jsii.Number] = None,
        shard_count: typing.Optional[jsii.Number] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenant_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RedisCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache azurerm_redis_cache} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#capacity RedisCache#capacity}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#family RedisCache#family}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#location RedisCache#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#name RedisCache#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#resource_group_name RedisCache#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#sku_name RedisCache#sku_name}.
        :param enable_non_ssl_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_non_ssl_port RedisCache#enable_non_ssl_port}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#id RedisCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity RedisCache#identity}
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#minimum_tls_version RedisCache#minimum_tls_version}.
        :param patch_schedule: patch_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#patch_schedule RedisCache#patch_schedule}
        :param private_static_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#private_static_ip_address RedisCache#private_static_ip_address}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#public_network_access_enabled RedisCache#public_network_access_enabled}.
        :param redis_configuration: redis_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_configuration RedisCache#redis_configuration}
        :param redis_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_version RedisCache#redis_version}.
        :param replicas_per_master: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_master RedisCache#replicas_per_master}.
        :param replicas_per_primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_primary RedisCache#replicas_per_primary}.
        :param shard_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#shard_count RedisCache#shard_count}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#subnet_id RedisCache#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tags RedisCache#tags}.
        :param tenant_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tenant_settings RedisCache#tenant_settings}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#timeouts RedisCache#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#zones RedisCache#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCache.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RedisCacheConfig(
            capacity=capacity,
            family=family,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            enable_non_ssl_port=enable_non_ssl_port,
            id=id,
            identity=identity,
            minimum_tls_version=minimum_tls_version,
            patch_schedule=patch_schedule,
            private_static_ip_address=private_static_ip_address,
            public_network_access_enabled=public_network_access_enabled,
            redis_configuration=redis_configuration,
            redis_version=redis_version,
            replicas_per_master=replicas_per_master,
            replicas_per_primary=replicas_per_primary,
            shard_count=shard_count,
            subnet_id=subnet_id,
            tags=tags,
            tenant_settings=tenant_settings,
            timeouts=timeouts,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#type RedisCache#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity_ids RedisCache#identity_ids}.
        '''
        value = RedisCacheIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putPatchSchedule")
    def put_patch_schedule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RedisCachePatchSchedule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCache.put_patch_schedule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPatchSchedule", [value]))

    @jsii.member(jsii_name="putRedisConfiguration")
    def put_redis_configuration(
        self,
        *,
        aof_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aof_storage_connection_string0: typing.Optional[builtins.str] = None,
        aof_storage_connection_string1: typing.Optional[builtins.str] = None,
        enable_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maxfragmentationmemory_reserved: typing.Optional[jsii.Number] = None,
        maxmemory_delta: typing.Optional[jsii.Number] = None,
        maxmemory_policy: typing.Optional[builtins.str] = None,
        maxmemory_reserved: typing.Optional[jsii.Number] = None,
        notify_keyspace_events: typing.Optional[builtins.str] = None,
        rdb_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rdb_backup_frequency: typing.Optional[jsii.Number] = None,
        rdb_backup_max_snapshot_count: typing.Optional[jsii.Number] = None,
        rdb_storage_connection_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aof_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_backup_enabled RedisCache#aof_backup_enabled}.
        :param aof_storage_connection_string0: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_0 RedisCache#aof_storage_connection_string_0}.
        :param aof_storage_connection_string1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_1 RedisCache#aof_storage_connection_string_1}.
        :param enable_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_authentication RedisCache#enable_authentication}.
        :param maxfragmentationmemory_reserved: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxfragmentationmemory_reserved RedisCache#maxfragmentationmemory_reserved}.
        :param maxmemory_delta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_delta RedisCache#maxmemory_delta}.
        :param maxmemory_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_policy RedisCache#maxmemory_policy}.
        :param maxmemory_reserved: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_reserved RedisCache#maxmemory_reserved}.
        :param notify_keyspace_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#notify_keyspace_events RedisCache#notify_keyspace_events}.
        :param rdb_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_enabled RedisCache#rdb_backup_enabled}.
        :param rdb_backup_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_frequency RedisCache#rdb_backup_frequency}.
        :param rdb_backup_max_snapshot_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_max_snapshot_count RedisCache#rdb_backup_max_snapshot_count}.
        :param rdb_storage_connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_storage_connection_string RedisCache#rdb_storage_connection_string}.
        '''
        value = RedisCacheRedisConfiguration(
            aof_backup_enabled=aof_backup_enabled,
            aof_storage_connection_string0=aof_storage_connection_string0,
            aof_storage_connection_string1=aof_storage_connection_string1,
            enable_authentication=enable_authentication,
            maxfragmentationmemory_reserved=maxfragmentationmemory_reserved,
            maxmemory_delta=maxmemory_delta,
            maxmemory_policy=maxmemory_policy,
            maxmemory_reserved=maxmemory_reserved,
            notify_keyspace_events=notify_keyspace_events,
            rdb_backup_enabled=rdb_backup_enabled,
            rdb_backup_frequency=rdb_backup_frequency,
            rdb_backup_max_snapshot_count=rdb_backup_max_snapshot_count,
            rdb_storage_connection_string=rdb_storage_connection_string,
        )

        return typing.cast(None, jsii.invoke(self, "putRedisConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#create RedisCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#delete RedisCache#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#read RedisCache#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#update RedisCache#update}.
        '''
        value = RedisCacheTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnableNonSslPort")
    def reset_enable_non_ssl_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNonSslPort", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetPatchSchedule")
    def reset_patch_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatchSchedule", []))

    @jsii.member(jsii_name="resetPrivateStaticIpAddress")
    def reset_private_static_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateStaticIpAddress", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetRedisConfiguration")
    def reset_redis_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisConfiguration", []))

    @jsii.member(jsii_name="resetRedisVersion")
    def reset_redis_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisVersion", []))

    @jsii.member(jsii_name="resetReplicasPerMaster")
    def reset_replicas_per_master(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicasPerMaster", []))

    @jsii.member(jsii_name="resetReplicasPerPrimary")
    def reset_replicas_per_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicasPerPrimary", []))

    @jsii.member(jsii_name="resetShardCount")
    def reset_shard_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShardCount", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTenantSettings")
    def reset_tenant_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantSettings", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "RedisCacheIdentityOutputReference":
        return typing.cast("RedisCacheIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="patchSchedule")
    def patch_schedule(self) -> "RedisCachePatchScheduleList":
        return typing.cast("RedisCachePatchScheduleList", jsii.get(self, "patchSchedule"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="primaryAccessKey")
    def primary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="primaryConnectionString")
    def primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="redisConfiguration")
    def redis_configuration(self) -> "RedisCacheRedisConfigurationOutputReference":
        return typing.cast("RedisCacheRedisConfigurationOutputReference", jsii.get(self, "redisConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="secondaryAccessKey")
    def secondary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryConnectionString")
    def secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="sslPort")
    def ssl_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sslPort"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "RedisCacheTimeoutsOutputReference":
        return typing.cast("RedisCacheTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNonSslPortInput")
    def enable_non_ssl_port_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableNonSslPortInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["RedisCacheIdentity"]:
        return typing.cast(typing.Optional["RedisCacheIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patchScheduleInput")
    def patch_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RedisCachePatchSchedule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RedisCachePatchSchedule"]]], jsii.get(self, "patchScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="privateStaticIpAddressInput")
    def private_static_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateStaticIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="redisConfigurationInput")
    def redis_configuration_input(
        self,
    ) -> typing.Optional["RedisCacheRedisConfiguration"]:
        return typing.cast(typing.Optional["RedisCacheRedisConfiguration"], jsii.get(self, "redisConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="redisVersionInput")
    def redis_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redisVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicasPerMasterInput")
    def replicas_per_master_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerMasterInput"))

    @builtins.property
    @jsii.member(jsii_name="replicasPerPrimaryInput")
    def replicas_per_primary_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerPrimaryInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="shardCountInput")
    def shard_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shardCountInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantSettingsInput")
    def tenant_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tenantSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["RedisCacheTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["RedisCacheTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="enableNonSslPort")
    def enable_non_ssl_port(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableNonSslPort"))

    @enable_non_ssl_port.setter
    def enable_non_ssl_port(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "enable_non_ssl_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNonSslPort", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateStaticIpAddress")
    def private_static_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateStaticIpAddress"))

    @private_static_ip_address.setter
    def private_static_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "private_static_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateStaticIpAddress", value)

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
            type_hints = typing.get_type_hints(getattr(RedisCache, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="redisVersion")
    def redis_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redisVersion"))

    @redis_version.setter
    def redis_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "redis_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redisVersion", value)

    @builtins.property
    @jsii.member(jsii_name="replicasPerMaster")
    def replicas_per_master(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicasPerMaster"))

    @replicas_per_master.setter
    def replicas_per_master(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "replicas_per_master").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicasPerMaster", value)

    @builtins.property
    @jsii.member(jsii_name="replicasPerPrimary")
    def replicas_per_primary(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicasPerPrimary"))

    @replicas_per_primary.setter
    def replicas_per_primary(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "replicas_per_primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicasPerPrimary", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="shardCount")
    def shard_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shardCount"))

    @shard_count.setter
    def shard_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "shard_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardCount", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tenantSettings")
    def tenant_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tenantSettings"))

    @tenant_settings.setter
    def tenant_settings(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "tenant_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantSettings", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCache, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capacity": "capacity",
        "family": "family",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "enable_non_ssl_port": "enableNonSslPort",
        "id": "id",
        "identity": "identity",
        "minimum_tls_version": "minimumTlsVersion",
        "patch_schedule": "patchSchedule",
        "private_static_ip_address": "privateStaticIpAddress",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "redis_configuration": "redisConfiguration",
        "redis_version": "redisVersion",
        "replicas_per_master": "replicasPerMaster",
        "replicas_per_primary": "replicasPerPrimary",
        "shard_count": "shardCount",
        "subnet_id": "subnetId",
        "tags": "tags",
        "tenant_settings": "tenantSettings",
        "timeouts": "timeouts",
        "zones": "zones",
    },
)
class RedisCacheConfig(cdktf.TerraformMetaArguments):
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
        capacity: jsii.Number,
        family: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        enable_non_ssl_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["RedisCacheIdentity", typing.Dict[str, typing.Any]]] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        patch_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RedisCachePatchSchedule", typing.Dict[str, typing.Any]]]]] = None,
        private_static_ip_address: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        redis_configuration: typing.Optional[typing.Union["RedisCacheRedisConfiguration", typing.Dict[str, typing.Any]]] = None,
        redis_version: typing.Optional[builtins.str] = None,
        replicas_per_master: typing.Optional[jsii.Number] = None,
        replicas_per_primary: typing.Optional[jsii.Number] = None,
        shard_count: typing.Optional[jsii.Number] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenant_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RedisCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#capacity RedisCache#capacity}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#family RedisCache#family}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#location RedisCache#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#name RedisCache#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#resource_group_name RedisCache#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#sku_name RedisCache#sku_name}.
        :param enable_non_ssl_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_non_ssl_port RedisCache#enable_non_ssl_port}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#id RedisCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity RedisCache#identity}
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#minimum_tls_version RedisCache#minimum_tls_version}.
        :param patch_schedule: patch_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#patch_schedule RedisCache#patch_schedule}
        :param private_static_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#private_static_ip_address RedisCache#private_static_ip_address}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#public_network_access_enabled RedisCache#public_network_access_enabled}.
        :param redis_configuration: redis_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_configuration RedisCache#redis_configuration}
        :param redis_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_version RedisCache#redis_version}.
        :param replicas_per_master: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_master RedisCache#replicas_per_master}.
        :param replicas_per_primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_primary RedisCache#replicas_per_primary}.
        :param shard_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#shard_count RedisCache#shard_count}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#subnet_id RedisCache#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tags RedisCache#tags}.
        :param tenant_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tenant_settings RedisCache#tenant_settings}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#timeouts RedisCache#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#zones RedisCache#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = RedisCacheIdentity(**identity)
        if isinstance(redis_configuration, dict):
            redis_configuration = RedisCacheRedisConfiguration(**redis_configuration)
        if isinstance(timeouts, dict):
            timeouts = RedisCacheTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(RedisCacheConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument enable_non_ssl_port", value=enable_non_ssl_port, expected_type=type_hints["enable_non_ssl_port"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument patch_schedule", value=patch_schedule, expected_type=type_hints["patch_schedule"])
            check_type(argname="argument private_static_ip_address", value=private_static_ip_address, expected_type=type_hints["private_static_ip_address"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument redis_configuration", value=redis_configuration, expected_type=type_hints["redis_configuration"])
            check_type(argname="argument redis_version", value=redis_version, expected_type=type_hints["redis_version"])
            check_type(argname="argument replicas_per_master", value=replicas_per_master, expected_type=type_hints["replicas_per_master"])
            check_type(argname="argument replicas_per_primary", value=replicas_per_primary, expected_type=type_hints["replicas_per_primary"])
            check_type(argname="argument shard_count", value=shard_count, expected_type=type_hints["shard_count"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tenant_settings", value=tenant_settings, expected_type=type_hints["tenant_settings"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "family": family,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
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
        if enable_non_ssl_port is not None:
            self._values["enable_non_ssl_port"] = enable_non_ssl_port
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if patch_schedule is not None:
            self._values["patch_schedule"] = patch_schedule
        if private_static_ip_address is not None:
            self._values["private_static_ip_address"] = private_static_ip_address
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if redis_configuration is not None:
            self._values["redis_configuration"] = redis_configuration
        if redis_version is not None:
            self._values["redis_version"] = redis_version
        if replicas_per_master is not None:
            self._values["replicas_per_master"] = replicas_per_master
        if replicas_per_primary is not None:
            self._values["replicas_per_primary"] = replicas_per_primary
        if shard_count is not None:
            self._values["shard_count"] = shard_count
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if tenant_settings is not None:
            self._values["tenant_settings"] = tenant_settings
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zones is not None:
            self._values["zones"] = zones

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
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#capacity RedisCache#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#family RedisCache#family}.'''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#location RedisCache#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#name RedisCache#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#resource_group_name RedisCache#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#sku_name RedisCache#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_non_ssl_port(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_non_ssl_port RedisCache#enable_non_ssl_port}.'''
        result = self._values.get("enable_non_ssl_port")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#id RedisCache#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["RedisCacheIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity RedisCache#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["RedisCacheIdentity"], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#minimum_tls_version RedisCache#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def patch_schedule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RedisCachePatchSchedule"]]]:
        '''patch_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#patch_schedule RedisCache#patch_schedule}
        '''
        result = self._values.get("patch_schedule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RedisCachePatchSchedule"]]], result)

    @builtins.property
    def private_static_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#private_static_ip_address RedisCache#private_static_ip_address}.'''
        result = self._values.get("private_static_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#public_network_access_enabled RedisCache#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def redis_configuration(self) -> typing.Optional["RedisCacheRedisConfiguration"]:
        '''redis_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_configuration RedisCache#redis_configuration}
        '''
        result = self._values.get("redis_configuration")
        return typing.cast(typing.Optional["RedisCacheRedisConfiguration"], result)

    @builtins.property
    def redis_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#redis_version RedisCache#redis_version}.'''
        result = self._values.get("redis_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicas_per_master(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_master RedisCache#replicas_per_master}.'''
        result = self._values.get("replicas_per_master")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replicas_per_primary(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#replicas_per_primary RedisCache#replicas_per_primary}.'''
        result = self._values.get("replicas_per_primary")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shard_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#shard_count RedisCache#shard_count}.'''
        result = self._values.get("shard_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#subnet_id RedisCache#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tags RedisCache#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tenant_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#tenant_settings RedisCache#tenant_settings}.'''
        result = self._values.get("tenant_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["RedisCacheTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#timeouts RedisCache#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["RedisCacheTimeouts"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#zones RedisCache#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisCacheConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class RedisCacheIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#type RedisCache#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity_ids RedisCache#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCacheIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#type RedisCache#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#identity_ids RedisCache#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisCacheIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RedisCacheIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheIdentityOutputReference",
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
            type_hints = typing.get_type_hints(RedisCacheIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(RedisCacheIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RedisCacheIdentity]:
        return typing.cast(typing.Optional[RedisCacheIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RedisCacheIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCachePatchSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "maintenance_window": "maintenanceWindow",
        "start_hour_utc": "startHourUtc",
    },
)
class RedisCachePatchSchedule:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        maintenance_window: typing.Optional[builtins.str] = None,
        start_hour_utc: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#day_of_week RedisCache#day_of_week}.
        :param maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maintenance_window RedisCache#maintenance_window}.
        :param start_hour_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#start_hour_utc RedisCache#start_hour_utc}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCachePatchSchedule.__init__)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument start_hour_utc", value=start_hour_utc, expected_type=type_hints["start_hour_utc"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
        }
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if start_hour_utc is not None:
            self._values["start_hour_utc"] = start_hour_utc

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#day_of_week RedisCache#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maintenance_window RedisCache#maintenance_window}.'''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_hour_utc(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#start_hour_utc RedisCache#start_hour_utc}.'''
        result = self._values.get("start_hour_utc")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisCachePatchSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RedisCachePatchScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCachePatchScheduleList",
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
            type_hints = typing.get_type_hints(RedisCachePatchScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RedisCachePatchScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCachePatchScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RedisCachePatchScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RedisCachePatchSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RedisCachePatchSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RedisCachePatchSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RedisCachePatchScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCachePatchScheduleOutputReference",
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
            type_hints = typing.get_type_hints(RedisCachePatchScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetStartHourUtc")
    def reset_start_hour_utc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartHourUtc", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="startHourUtcInput")
    def start_hour_utc_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startHourUtcInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleOutputReference, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleOutputReference, "maintenance_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="startHourUtc")
    def start_hour_utc(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startHourUtc"))

    @start_hour_utc.setter
    def start_hour_utc(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleOutputReference, "start_hour_utc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startHourUtc", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RedisCachePatchSchedule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RedisCachePatchSchedule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RedisCachePatchSchedule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCachePatchScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheRedisConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "aof_backup_enabled": "aofBackupEnabled",
        "aof_storage_connection_string0": "aofStorageConnectionString0",
        "aof_storage_connection_string1": "aofStorageConnectionString1",
        "enable_authentication": "enableAuthentication",
        "maxfragmentationmemory_reserved": "maxfragmentationmemoryReserved",
        "maxmemory_delta": "maxmemoryDelta",
        "maxmemory_policy": "maxmemoryPolicy",
        "maxmemory_reserved": "maxmemoryReserved",
        "notify_keyspace_events": "notifyKeyspaceEvents",
        "rdb_backup_enabled": "rdbBackupEnabled",
        "rdb_backup_frequency": "rdbBackupFrequency",
        "rdb_backup_max_snapshot_count": "rdbBackupMaxSnapshotCount",
        "rdb_storage_connection_string": "rdbStorageConnectionString",
    },
)
class RedisCacheRedisConfiguration:
    def __init__(
        self,
        *,
        aof_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aof_storage_connection_string0: typing.Optional[builtins.str] = None,
        aof_storage_connection_string1: typing.Optional[builtins.str] = None,
        enable_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maxfragmentationmemory_reserved: typing.Optional[jsii.Number] = None,
        maxmemory_delta: typing.Optional[jsii.Number] = None,
        maxmemory_policy: typing.Optional[builtins.str] = None,
        maxmemory_reserved: typing.Optional[jsii.Number] = None,
        notify_keyspace_events: typing.Optional[builtins.str] = None,
        rdb_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rdb_backup_frequency: typing.Optional[jsii.Number] = None,
        rdb_backup_max_snapshot_count: typing.Optional[jsii.Number] = None,
        rdb_storage_connection_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aof_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_backup_enabled RedisCache#aof_backup_enabled}.
        :param aof_storage_connection_string0: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_0 RedisCache#aof_storage_connection_string_0}.
        :param aof_storage_connection_string1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_1 RedisCache#aof_storage_connection_string_1}.
        :param enable_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_authentication RedisCache#enable_authentication}.
        :param maxfragmentationmemory_reserved: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxfragmentationmemory_reserved RedisCache#maxfragmentationmemory_reserved}.
        :param maxmemory_delta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_delta RedisCache#maxmemory_delta}.
        :param maxmemory_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_policy RedisCache#maxmemory_policy}.
        :param maxmemory_reserved: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_reserved RedisCache#maxmemory_reserved}.
        :param notify_keyspace_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#notify_keyspace_events RedisCache#notify_keyspace_events}.
        :param rdb_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_enabled RedisCache#rdb_backup_enabled}.
        :param rdb_backup_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_frequency RedisCache#rdb_backup_frequency}.
        :param rdb_backup_max_snapshot_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_max_snapshot_count RedisCache#rdb_backup_max_snapshot_count}.
        :param rdb_storage_connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_storage_connection_string RedisCache#rdb_storage_connection_string}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCacheRedisConfiguration.__init__)
            check_type(argname="argument aof_backup_enabled", value=aof_backup_enabled, expected_type=type_hints["aof_backup_enabled"])
            check_type(argname="argument aof_storage_connection_string0", value=aof_storage_connection_string0, expected_type=type_hints["aof_storage_connection_string0"])
            check_type(argname="argument aof_storage_connection_string1", value=aof_storage_connection_string1, expected_type=type_hints["aof_storage_connection_string1"])
            check_type(argname="argument enable_authentication", value=enable_authentication, expected_type=type_hints["enable_authentication"])
            check_type(argname="argument maxfragmentationmemory_reserved", value=maxfragmentationmemory_reserved, expected_type=type_hints["maxfragmentationmemory_reserved"])
            check_type(argname="argument maxmemory_delta", value=maxmemory_delta, expected_type=type_hints["maxmemory_delta"])
            check_type(argname="argument maxmemory_policy", value=maxmemory_policy, expected_type=type_hints["maxmemory_policy"])
            check_type(argname="argument maxmemory_reserved", value=maxmemory_reserved, expected_type=type_hints["maxmemory_reserved"])
            check_type(argname="argument notify_keyspace_events", value=notify_keyspace_events, expected_type=type_hints["notify_keyspace_events"])
            check_type(argname="argument rdb_backup_enabled", value=rdb_backup_enabled, expected_type=type_hints["rdb_backup_enabled"])
            check_type(argname="argument rdb_backup_frequency", value=rdb_backup_frequency, expected_type=type_hints["rdb_backup_frequency"])
            check_type(argname="argument rdb_backup_max_snapshot_count", value=rdb_backup_max_snapshot_count, expected_type=type_hints["rdb_backup_max_snapshot_count"])
            check_type(argname="argument rdb_storage_connection_string", value=rdb_storage_connection_string, expected_type=type_hints["rdb_storage_connection_string"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aof_backup_enabled is not None:
            self._values["aof_backup_enabled"] = aof_backup_enabled
        if aof_storage_connection_string0 is not None:
            self._values["aof_storage_connection_string0"] = aof_storage_connection_string0
        if aof_storage_connection_string1 is not None:
            self._values["aof_storage_connection_string1"] = aof_storage_connection_string1
        if enable_authentication is not None:
            self._values["enable_authentication"] = enable_authentication
        if maxfragmentationmemory_reserved is not None:
            self._values["maxfragmentationmemory_reserved"] = maxfragmentationmemory_reserved
        if maxmemory_delta is not None:
            self._values["maxmemory_delta"] = maxmemory_delta
        if maxmemory_policy is not None:
            self._values["maxmemory_policy"] = maxmemory_policy
        if maxmemory_reserved is not None:
            self._values["maxmemory_reserved"] = maxmemory_reserved
        if notify_keyspace_events is not None:
            self._values["notify_keyspace_events"] = notify_keyspace_events
        if rdb_backup_enabled is not None:
            self._values["rdb_backup_enabled"] = rdb_backup_enabled
        if rdb_backup_frequency is not None:
            self._values["rdb_backup_frequency"] = rdb_backup_frequency
        if rdb_backup_max_snapshot_count is not None:
            self._values["rdb_backup_max_snapshot_count"] = rdb_backup_max_snapshot_count
        if rdb_storage_connection_string is not None:
            self._values["rdb_storage_connection_string"] = rdb_storage_connection_string

    @builtins.property
    def aof_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_backup_enabled RedisCache#aof_backup_enabled}.'''
        result = self._values.get("aof_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aof_storage_connection_string0(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_0 RedisCache#aof_storage_connection_string_0}.'''
        result = self._values.get("aof_storage_connection_string0")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aof_storage_connection_string1(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#aof_storage_connection_string_1 RedisCache#aof_storage_connection_string_1}.'''
        result = self._values.get("aof_storage_connection_string1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#enable_authentication RedisCache#enable_authentication}.'''
        result = self._values.get("enable_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def maxfragmentationmemory_reserved(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxfragmentationmemory_reserved RedisCache#maxfragmentationmemory_reserved}.'''
        result = self._values.get("maxfragmentationmemory_reserved")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maxmemory_delta(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_delta RedisCache#maxmemory_delta}.'''
        result = self._values.get("maxmemory_delta")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maxmemory_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_policy RedisCache#maxmemory_policy}.'''
        result = self._values.get("maxmemory_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maxmemory_reserved(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#maxmemory_reserved RedisCache#maxmemory_reserved}.'''
        result = self._values.get("maxmemory_reserved")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notify_keyspace_events(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#notify_keyspace_events RedisCache#notify_keyspace_events}.'''
        result = self._values.get("notify_keyspace_events")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rdb_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_enabled RedisCache#rdb_backup_enabled}.'''
        result = self._values.get("rdb_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rdb_backup_frequency(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_frequency RedisCache#rdb_backup_frequency}.'''
        result = self._values.get("rdb_backup_frequency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rdb_backup_max_snapshot_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_backup_max_snapshot_count RedisCache#rdb_backup_max_snapshot_count}.'''
        result = self._values.get("rdb_backup_max_snapshot_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rdb_storage_connection_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#rdb_storage_connection_string RedisCache#rdb_storage_connection_string}.'''
        result = self._values.get("rdb_storage_connection_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisCacheRedisConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RedisCacheRedisConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheRedisConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(RedisCacheRedisConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAofBackupEnabled")
    def reset_aof_backup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAofBackupEnabled", []))

    @jsii.member(jsii_name="resetAofStorageConnectionString0")
    def reset_aof_storage_connection_string0(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAofStorageConnectionString0", []))

    @jsii.member(jsii_name="resetAofStorageConnectionString1")
    def reset_aof_storage_connection_string1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAofStorageConnectionString1", []))

    @jsii.member(jsii_name="resetEnableAuthentication")
    def reset_enable_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAuthentication", []))

    @jsii.member(jsii_name="resetMaxfragmentationmemoryReserved")
    def reset_maxfragmentationmemory_reserved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxfragmentationmemoryReserved", []))

    @jsii.member(jsii_name="resetMaxmemoryDelta")
    def reset_maxmemory_delta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxmemoryDelta", []))

    @jsii.member(jsii_name="resetMaxmemoryPolicy")
    def reset_maxmemory_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxmemoryPolicy", []))

    @jsii.member(jsii_name="resetMaxmemoryReserved")
    def reset_maxmemory_reserved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxmemoryReserved", []))

    @jsii.member(jsii_name="resetNotifyKeyspaceEvents")
    def reset_notify_keyspace_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyKeyspaceEvents", []))

    @jsii.member(jsii_name="resetRdbBackupEnabled")
    def reset_rdb_backup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdbBackupEnabled", []))

    @jsii.member(jsii_name="resetRdbBackupFrequency")
    def reset_rdb_backup_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdbBackupFrequency", []))

    @jsii.member(jsii_name="resetRdbBackupMaxSnapshotCount")
    def reset_rdb_backup_max_snapshot_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdbBackupMaxSnapshotCount", []))

    @jsii.member(jsii_name="resetRdbStorageConnectionString")
    def reset_rdb_storage_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdbStorageConnectionString", []))

    @builtins.property
    @jsii.member(jsii_name="maxclients")
    def maxclients(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxclients"))

    @builtins.property
    @jsii.member(jsii_name="aofBackupEnabledInput")
    def aof_backup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "aofBackupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="aofStorageConnectionString0Input")
    def aof_storage_connection_string0_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aofStorageConnectionString0Input"))

    @builtins.property
    @jsii.member(jsii_name="aofStorageConnectionString1Input")
    def aof_storage_connection_string1_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aofStorageConnectionString1Input"))

    @builtins.property
    @jsii.member(jsii_name="enableAuthenticationInput")
    def enable_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxfragmentationmemoryReservedInput")
    def maxfragmentationmemory_reserved_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxfragmentationmemoryReservedInput"))

    @builtins.property
    @jsii.member(jsii_name="maxmemoryDeltaInput")
    def maxmemory_delta_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxmemoryDeltaInput"))

    @builtins.property
    @jsii.member(jsii_name="maxmemoryPolicyInput")
    def maxmemory_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxmemoryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxmemoryReservedInput")
    def maxmemory_reserved_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxmemoryReservedInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyKeyspaceEventsInput")
    def notify_keyspace_events_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notifyKeyspaceEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbBackupEnabledInput")
    def rdb_backup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rdbBackupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbBackupFrequencyInput")
    def rdb_backup_frequency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rdbBackupFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbBackupMaxSnapshotCountInput")
    def rdb_backup_max_snapshot_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rdbBackupMaxSnapshotCountInput"))

    @builtins.property
    @jsii.member(jsii_name="rdbStorageConnectionStringInput")
    def rdb_storage_connection_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rdbStorageConnectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="aofBackupEnabled")
    def aof_backup_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "aofBackupEnabled"))

    @aof_backup_enabled.setter
    def aof_backup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "aof_backup_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aofBackupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="aofStorageConnectionString0")
    def aof_storage_connection_string0(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aofStorageConnectionString0"))

    @aof_storage_connection_string0.setter
    def aof_storage_connection_string0(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "aof_storage_connection_string0").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aofStorageConnectionString0", value)

    @builtins.property
    @jsii.member(jsii_name="aofStorageConnectionString1")
    def aof_storage_connection_string1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aofStorageConnectionString1"))

    @aof_storage_connection_string1.setter
    def aof_storage_connection_string1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "aof_storage_connection_string1").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aofStorageConnectionString1", value)

    @builtins.property
    @jsii.member(jsii_name="enableAuthentication")
    def enable_authentication(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAuthentication"))

    @enable_authentication.setter
    def enable_authentication(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "enable_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="maxfragmentationmemoryReserved")
    def maxfragmentationmemory_reserved(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxfragmentationmemoryReserved"))

    @maxfragmentationmemory_reserved.setter
    def maxfragmentationmemory_reserved(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "maxfragmentationmemory_reserved").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxfragmentationmemoryReserved", value)

    @builtins.property
    @jsii.member(jsii_name="maxmemoryDelta")
    def maxmemory_delta(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxmemoryDelta"))

    @maxmemory_delta.setter
    def maxmemory_delta(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "maxmemory_delta").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxmemoryDelta", value)

    @builtins.property
    @jsii.member(jsii_name="maxmemoryPolicy")
    def maxmemory_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxmemoryPolicy"))

    @maxmemory_policy.setter
    def maxmemory_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "maxmemory_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxmemoryPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="maxmemoryReserved")
    def maxmemory_reserved(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxmemoryReserved"))

    @maxmemory_reserved.setter
    def maxmemory_reserved(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "maxmemory_reserved").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxmemoryReserved", value)

    @builtins.property
    @jsii.member(jsii_name="notifyKeyspaceEvents")
    def notify_keyspace_events(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notifyKeyspaceEvents"))

    @notify_keyspace_events.setter
    def notify_keyspace_events(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "notify_keyspace_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyKeyspaceEvents", value)

    @builtins.property
    @jsii.member(jsii_name="rdbBackupEnabled")
    def rdb_backup_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rdbBackupEnabled"))

    @rdb_backup_enabled.setter
    def rdb_backup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "rdb_backup_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbBackupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="rdbBackupFrequency")
    def rdb_backup_frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rdbBackupFrequency"))

    @rdb_backup_frequency.setter
    def rdb_backup_frequency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "rdb_backup_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbBackupFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="rdbBackupMaxSnapshotCount")
    def rdb_backup_max_snapshot_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rdbBackupMaxSnapshotCount"))

    @rdb_backup_max_snapshot_count.setter
    def rdb_backup_max_snapshot_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "rdb_backup_max_snapshot_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbBackupMaxSnapshotCount", value)

    @builtins.property
    @jsii.member(jsii_name="rdbStorageConnectionString")
    def rdb_storage_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rdbStorageConnectionString"))

    @rdb_storage_connection_string.setter
    def rdb_storage_connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "rdb_storage_connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdbStorageConnectionString", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RedisCacheRedisConfiguration]:
        return typing.cast(typing.Optional[RedisCacheRedisConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RedisCacheRedisConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheRedisConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class RedisCacheTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#create RedisCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#delete RedisCache#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#read RedisCache#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#update RedisCache#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisCacheTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#create RedisCache#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#delete RedisCache#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#read RedisCache#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/redis_cache#update RedisCache#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisCacheTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RedisCacheTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.redisCache.RedisCacheTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(RedisCacheTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(RedisCacheTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RedisCacheTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RedisCacheTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RedisCacheTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RedisCacheTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RedisCache",
    "RedisCacheConfig",
    "RedisCacheIdentity",
    "RedisCacheIdentityOutputReference",
    "RedisCachePatchSchedule",
    "RedisCachePatchScheduleList",
    "RedisCachePatchScheduleOutputReference",
    "RedisCacheRedisConfiguration",
    "RedisCacheRedisConfigurationOutputReference",
    "RedisCacheTimeouts",
    "RedisCacheTimeoutsOutputReference",
]

publication.publish()
