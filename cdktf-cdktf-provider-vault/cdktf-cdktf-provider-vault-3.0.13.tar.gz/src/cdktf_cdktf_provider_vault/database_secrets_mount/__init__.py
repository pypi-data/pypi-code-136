'''
# `vault_database_secrets_mount`

Refer to the Terraform Registory for docs: [`vault_database_secrets_mount`](https://www.terraform.io/docs/providers/vault/r/database_secrets_mount).
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


class DatabaseSecretsMount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount vault_database_secrets_mount}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        path: builtins.str,
        allowed_managed_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_request_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_response_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        cassandra: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountCassandra", typing.Dict[str, typing.Any]]]]] = None,
        couchbase: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountCouchbase", typing.Dict[str, typing.Any]]]]] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        elasticsearch: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountElasticsearch", typing.Dict[str, typing.Any]]]]] = None,
        external_entropy_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hana: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountHana", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        influxdb: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountInfluxdb", typing.Dict[str, typing.Any]]]]] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        mongodb: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodb", typing.Dict[str, typing.Any]]]]] = None,
        mongodbatlas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodbatlas", typing.Dict[str, typing.Any]]]]] = None,
        mssql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMssql", typing.Dict[str, typing.Any]]]]] = None,
        mysql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysql", typing.Dict[str, typing.Any]]]]] = None,
        mysql_aurora: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlAurora", typing.Dict[str, typing.Any]]]]] = None,
        mysql_legacy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlLegacy", typing.Dict[str, typing.Any]]]]] = None,
        mysql_rds: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlRds", typing.Dict[str, typing.Any]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oracle: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountOracle", typing.Dict[str, typing.Any]]]]] = None,
        postgresql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountPostgresql", typing.Dict[str, typing.Any]]]]] = None,
        redis_elasticache: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedisElasticache", typing.Dict[str, typing.Any]]]]] = None,
        redshift: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedshift", typing.Dict[str, typing.Any]]]]] = None,
        seal_wrap: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snowflake: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountSnowflake", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount vault_database_secrets_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param path: Where the secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#path DatabaseSecretsMount#path}
        :param allowed_managed_keys: List of managed key registry entry names that the mount in question is allowed to access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_managed_keys DatabaseSecretsMount#allowed_managed_keys}
        :param audit_non_hmac_request_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the request data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_request_keys DatabaseSecretsMount#audit_non_hmac_request_keys}
        :param audit_non_hmac_response_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the response data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_response_keys DatabaseSecretsMount#audit_non_hmac_response_keys}
        :param cassandra: cassandra block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#cassandra DatabaseSecretsMount#cassandra}
        :param couchbase: couchbase block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#couchbase DatabaseSecretsMount#couchbase}
        :param default_lease_ttl_seconds: Default lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#default_lease_ttl_seconds DatabaseSecretsMount#default_lease_ttl_seconds}
        :param description: Human-friendly description of the mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#description DatabaseSecretsMount#description}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#elasticsearch DatabaseSecretsMount#elasticsearch}
        :param external_entropy_access: Enable the secrets engine to access Vault's external entropy source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#external_entropy_access DatabaseSecretsMount#external_entropy_access}
        :param hana: hana block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hana DatabaseSecretsMount#hana}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#id DatabaseSecretsMount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param influxdb: influxdb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#influxdb DatabaseSecretsMount#influxdb}
        :param local: Local mount flag that can be explicitly set to true to enforce local mount in HA environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#local DatabaseSecretsMount#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_lease_ttl_seconds DatabaseSecretsMount#max_lease_ttl_seconds}
        :param mongodb: mongodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodb DatabaseSecretsMount#mongodb}
        :param mongodbatlas: mongodbatlas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodbatlas DatabaseSecretsMount#mongodbatlas}
        :param mssql: mssql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mssql DatabaseSecretsMount#mssql}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql DatabaseSecretsMount#mysql}
        :param mysql_aurora: mysql_aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_aurora DatabaseSecretsMount#mysql_aurora}
        :param mysql_legacy: mysql_legacy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_legacy DatabaseSecretsMount#mysql_legacy}
        :param mysql_rds: mysql_rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_rds DatabaseSecretsMount#mysql_rds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#namespace DatabaseSecretsMount#namespace}
        :param options: Specifies mount type specific options that are passed to the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#options DatabaseSecretsMount#options}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#oracle DatabaseSecretsMount#oracle}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#postgresql DatabaseSecretsMount#postgresql}
        :param redis_elasticache: redis_elasticache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redis_elasticache DatabaseSecretsMount#redis_elasticache}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redshift DatabaseSecretsMount#redshift}
        :param seal_wrap: Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#seal_wrap DatabaseSecretsMount#seal_wrap}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#snowflake DatabaseSecretsMount#snowflake}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseSecretsMountConfig(
            path=path,
            allowed_managed_keys=allowed_managed_keys,
            audit_non_hmac_request_keys=audit_non_hmac_request_keys,
            audit_non_hmac_response_keys=audit_non_hmac_response_keys,
            cassandra=cassandra,
            couchbase=couchbase,
            default_lease_ttl_seconds=default_lease_ttl_seconds,
            description=description,
            elasticsearch=elasticsearch,
            external_entropy_access=external_entropy_access,
            hana=hana,
            id=id,
            influxdb=influxdb,
            local=local,
            max_lease_ttl_seconds=max_lease_ttl_seconds,
            mongodb=mongodb,
            mongodbatlas=mongodbatlas,
            mssql=mssql,
            mysql=mysql,
            mysql_aurora=mysql_aurora,
            mysql_legacy=mysql_legacy,
            mysql_rds=mysql_rds,
            namespace=namespace,
            options=options,
            oracle=oracle,
            postgresql=postgresql,
            redis_elasticache=redis_elasticache,
            redshift=redshift,
            seal_wrap=seal_wrap,
            snowflake=snowflake,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCassandra")
    def put_cassandra(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountCassandra", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_cassandra)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCassandra", [value]))

    @jsii.member(jsii_name="putCouchbase")
    def put_couchbase(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountCouchbase", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_couchbase)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCouchbase", [value]))

    @jsii.member(jsii_name="putElasticsearch")
    def put_elasticsearch(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountElasticsearch", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_elasticsearch)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElasticsearch", [value]))

    @jsii.member(jsii_name="putHana")
    def put_hana(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountHana", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_hana)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHana", [value]))

    @jsii.member(jsii_name="putInfluxdb")
    def put_influxdb(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountInfluxdb", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_influxdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInfluxdb", [value]))

    @jsii.member(jsii_name="putMongodb")
    def put_mongodb(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodb", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mongodb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMongodb", [value]))

    @jsii.member(jsii_name="putMongodbatlas")
    def put_mongodbatlas(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodbatlas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mongodbatlas)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMongodbatlas", [value]))

    @jsii.member(jsii_name="putMssql")
    def put_mssql(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMssql", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mssql)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMssql", [value]))

    @jsii.member(jsii_name="putMysql")
    def put_mysql(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysql", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mysql)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysql", [value]))

    @jsii.member(jsii_name="putMysqlAurora")
    def put_mysql_aurora(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlAurora", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mysql_aurora)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlAurora", [value]))

    @jsii.member(jsii_name="putMysqlLegacy")
    def put_mysql_legacy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlLegacy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mysql_legacy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlLegacy", [value]))

    @jsii.member(jsii_name="putMysqlRds")
    def put_mysql_rds(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlRds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_mysql_rds)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlRds", [value]))

    @jsii.member(jsii_name="putOracle")
    def put_oracle(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountOracle", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_oracle)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracle", [value]))

    @jsii.member(jsii_name="putPostgresql")
    def put_postgresql(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountPostgresql", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_postgresql)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresql", [value]))

    @jsii.member(jsii_name="putRedisElasticache")
    def put_redis_elasticache(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedisElasticache", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_redis_elasticache)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRedisElasticache", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedshift", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_redshift)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountSnowflake", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMount.put_snowflake)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="resetAllowedManagedKeys")
    def reset_allowed_managed_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedManagedKeys", []))

    @jsii.member(jsii_name="resetAuditNonHmacRequestKeys")
    def reset_audit_non_hmac_request_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacRequestKeys", []))

    @jsii.member(jsii_name="resetAuditNonHmacResponseKeys")
    def reset_audit_non_hmac_response_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacResponseKeys", []))

    @jsii.member(jsii_name="resetCassandra")
    def reset_cassandra(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCassandra", []))

    @jsii.member(jsii_name="resetCouchbase")
    def reset_couchbase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCouchbase", []))

    @jsii.member(jsii_name="resetDefaultLeaseTtlSeconds")
    def reset_default_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetElasticsearch")
    def reset_elasticsearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearch", []))

    @jsii.member(jsii_name="resetExternalEntropyAccess")
    def reset_external_entropy_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEntropyAccess", []))

    @jsii.member(jsii_name="resetHana")
    def reset_hana(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHana", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInfluxdb")
    def reset_influxdb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfluxdb", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetMaxLeaseTtlSeconds")
    def reset_max_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetMongodb")
    def reset_mongodb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodb", []))

    @jsii.member(jsii_name="resetMongodbatlas")
    def reset_mongodbatlas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbatlas", []))

    @jsii.member(jsii_name="resetMssql")
    def reset_mssql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMssql", []))

    @jsii.member(jsii_name="resetMysql")
    def reset_mysql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysql", []))

    @jsii.member(jsii_name="resetMysqlAurora")
    def reset_mysql_aurora(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlAurora", []))

    @jsii.member(jsii_name="resetMysqlLegacy")
    def reset_mysql_legacy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlLegacy", []))

    @jsii.member(jsii_name="resetMysqlRds")
    def reset_mysql_rds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlRds", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetOracle")
    def reset_oracle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracle", []))

    @jsii.member(jsii_name="resetPostgresql")
    def reset_postgresql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresql", []))

    @jsii.member(jsii_name="resetRedisElasticache")
    def reset_redis_elasticache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisElasticache", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetSealWrap")
    def reset_seal_wrap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSealWrap", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessor")
    def accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessor"))

    @builtins.property
    @jsii.member(jsii_name="cassandra")
    def cassandra(self) -> "DatabaseSecretsMountCassandraList":
        return typing.cast("DatabaseSecretsMountCassandraList", jsii.get(self, "cassandra"))

    @builtins.property
    @jsii.member(jsii_name="couchbase")
    def couchbase(self) -> "DatabaseSecretsMountCouchbaseList":
        return typing.cast("DatabaseSecretsMountCouchbaseList", jsii.get(self, "couchbase"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearch")
    def elasticsearch(self) -> "DatabaseSecretsMountElasticsearchList":
        return typing.cast("DatabaseSecretsMountElasticsearchList", jsii.get(self, "elasticsearch"))

    @builtins.property
    @jsii.member(jsii_name="engineCount")
    def engine_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "engineCount"))

    @builtins.property
    @jsii.member(jsii_name="hana")
    def hana(self) -> "DatabaseSecretsMountHanaList":
        return typing.cast("DatabaseSecretsMountHanaList", jsii.get(self, "hana"))

    @builtins.property
    @jsii.member(jsii_name="influxdb")
    def influxdb(self) -> "DatabaseSecretsMountInfluxdbList":
        return typing.cast("DatabaseSecretsMountInfluxdbList", jsii.get(self, "influxdb"))

    @builtins.property
    @jsii.member(jsii_name="mongodb")
    def mongodb(self) -> "DatabaseSecretsMountMongodbList":
        return typing.cast("DatabaseSecretsMountMongodbList", jsii.get(self, "mongodb"))

    @builtins.property
    @jsii.member(jsii_name="mongodbatlas")
    def mongodbatlas(self) -> "DatabaseSecretsMountMongodbatlasList":
        return typing.cast("DatabaseSecretsMountMongodbatlasList", jsii.get(self, "mongodbatlas"))

    @builtins.property
    @jsii.member(jsii_name="mssql")
    def mssql(self) -> "DatabaseSecretsMountMssqlList":
        return typing.cast("DatabaseSecretsMountMssqlList", jsii.get(self, "mssql"))

    @builtins.property
    @jsii.member(jsii_name="mysql")
    def mysql(self) -> "DatabaseSecretsMountMysqlList":
        return typing.cast("DatabaseSecretsMountMysqlList", jsii.get(self, "mysql"))

    @builtins.property
    @jsii.member(jsii_name="mysqlAurora")
    def mysql_aurora(self) -> "DatabaseSecretsMountMysqlAuroraList":
        return typing.cast("DatabaseSecretsMountMysqlAuroraList", jsii.get(self, "mysqlAurora"))

    @builtins.property
    @jsii.member(jsii_name="mysqlLegacy")
    def mysql_legacy(self) -> "DatabaseSecretsMountMysqlLegacyList":
        return typing.cast("DatabaseSecretsMountMysqlLegacyList", jsii.get(self, "mysqlLegacy"))

    @builtins.property
    @jsii.member(jsii_name="mysqlRds")
    def mysql_rds(self) -> "DatabaseSecretsMountMysqlRdsList":
        return typing.cast("DatabaseSecretsMountMysqlRdsList", jsii.get(self, "mysqlRds"))

    @builtins.property
    @jsii.member(jsii_name="oracle")
    def oracle(self) -> "DatabaseSecretsMountOracleList":
        return typing.cast("DatabaseSecretsMountOracleList", jsii.get(self, "oracle"))

    @builtins.property
    @jsii.member(jsii_name="postgresql")
    def postgresql(self) -> "DatabaseSecretsMountPostgresqlList":
        return typing.cast("DatabaseSecretsMountPostgresqlList", jsii.get(self, "postgresql"))

    @builtins.property
    @jsii.member(jsii_name="redisElasticache")
    def redis_elasticache(self) -> "DatabaseSecretsMountRedisElasticacheList":
        return typing.cast("DatabaseSecretsMountRedisElasticacheList", jsii.get(self, "redisElasticache"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(self) -> "DatabaseSecretsMountRedshiftList":
        return typing.cast("DatabaseSecretsMountRedshiftList", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(self) -> "DatabaseSecretsMountSnowflakeList":
        return typing.cast("DatabaseSecretsMountSnowflakeList", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="allowedManagedKeysInput")
    def allowed_managed_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedManagedKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacRequestKeysInput")
    def audit_non_hmac_request_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auditNonHmacRequestKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacResponseKeysInput")
    def audit_non_hmac_response_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auditNonHmacResponseKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="cassandraInput")
    def cassandra_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCassandra"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCassandra"]]], jsii.get(self, "cassandraInput"))

    @builtins.property
    @jsii.member(jsii_name="couchbaseInput")
    def couchbase_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCouchbase"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCouchbase"]]], jsii.get(self, "couchbaseInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSecondsInput")
    def default_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchInput")
    def elasticsearch_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountElasticsearch"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountElasticsearch"]]], jsii.get(self, "elasticsearchInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEntropyAccessInput")
    def external_entropy_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "externalEntropyAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="hanaInput")
    def hana_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountHana"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountHana"]]], jsii.get(self, "hanaInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="influxdbInput")
    def influxdb_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountInfluxdb"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountInfluxdb"]]], jsii.get(self, "influxdbInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSecondsInput")
    def max_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbatlasInput")
    def mongodbatlas_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodbatlas"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodbatlas"]]], jsii.get(self, "mongodbatlasInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbInput")
    def mongodb_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodb"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodb"]]], jsii.get(self, "mongodbInput"))

    @builtins.property
    @jsii.member(jsii_name="mssqlInput")
    def mssql_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMssql"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMssql"]]], jsii.get(self, "mssqlInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlAuroraInput")
    def mysql_aurora_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlAurora"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlAurora"]]], jsii.get(self, "mysqlAuroraInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlInput")
    def mysql_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysql"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysql"]]], jsii.get(self, "mysqlInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlLegacyInput")
    def mysql_legacy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlLegacy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlLegacy"]]], jsii.get(self, "mysqlLegacyInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlRdsInput")
    def mysql_rds_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlRds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlRds"]]], jsii.get(self, "mysqlRdsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleInput")
    def oracle_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountOracle"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountOracle"]]], jsii.get(self, "oracleInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlInput")
    def postgresql_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountPostgresql"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountPostgresql"]]], jsii.get(self, "postgresqlInput"))

    @builtins.property
    @jsii.member(jsii_name="redisElasticacheInput")
    def redis_elasticache_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedisElasticache"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedisElasticache"]]], jsii.get(self, "redisElasticacheInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedshift"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedshift"]]], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="sealWrapInput")
    def seal_wrap_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sealWrapInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountSnowflake"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountSnowflake"]]], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedManagedKeys")
    def allowed_managed_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedManagedKeys"))

    @allowed_managed_keys.setter
    def allowed_managed_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "allowed_managed_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedManagedKeys", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacRequestKeys")
    def audit_non_hmac_request_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacRequestKeys"))

    @audit_non_hmac_request_keys.setter
    def audit_non_hmac_request_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "audit_non_hmac_request_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacRequestKeys", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacResponseKeys")
    def audit_non_hmac_response_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacResponseKeys"))

    @audit_non_hmac_response_keys.setter
    def audit_non_hmac_response_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "audit_non_hmac_response_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacResponseKeys", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultLeaseTtlSeconds"))

    @default_lease_ttl_seconds.setter
    def default_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "default_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalEntropyAccess")
    def external_entropy_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "externalEntropyAccess"))

    @external_entropy_access.setter
    def external_entropy_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "external_entropy_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalEntropyAccess", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLeaseTtlSeconds"))

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "max_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="sealWrap")
    def seal_wrap(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sealWrap"))

    @seal_wrap.setter
    def seal_wrap(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMount, "seal_wrap").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sealWrap", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCassandra",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connect_timeout": "connectTimeout",
        "data": "data",
        "hosts": "hosts",
        "insecure_tls": "insecureTls",
        "password": "password",
        "pem_bundle": "pemBundle",
        "pem_json": "pemJson",
        "plugin_name": "pluginName",
        "port": "port",
        "protocol_version": "protocolVersion",
        "root_rotation_statements": "rootRotationStatements",
        "tls": "tls",
        "username": "username",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountCassandra:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol_version: typing.Optional[jsii.Number] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connect_timeout DatabaseSecretsMount#connect_timeout}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param hosts: Cassandra hosts to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hosts DatabaseSecretsMount#hosts}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        :param password: The password to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_bundle DatabaseSecretsMount#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_json DatabaseSecretsMount#pem_json}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param port: The transport port to use to connect to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#port DatabaseSecretsMount#port}
        :param protocol_version: The CQL protocol version to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#protocol_version DatabaseSecretsMount#protocol_version}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param tls: Whether to use TLS when connecting to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        :param username: The username to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountCassandra.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument pem_bundle", value=pem_bundle, expected_type=type_hints["pem_bundle"])
            check_type(argname="argument pem_json", value=pem_json, expected_type=type_hints["pem_json"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if data is not None:
            self._values["data"] = data
        if hosts is not None:
            self._values["hosts"] = hosts
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if password is not None:
            self._values["password"] = password
        if pem_bundle is not None:
            self._values["pem_bundle"] = pem_bundle
        if pem_json is not None:
            self._values["pem_json"] = pem_json
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if port is not None:
            self._values["port"] = port
        if protocol_version is not None:
            self._values["protocol_version"] = protocol_version
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if tls is not None:
            self._values["tls"] = tls
        if username is not None:
            self._values["username"] = username
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to use as a connection timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connect_timeout DatabaseSecretsMount#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Cassandra hosts to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hosts DatabaseSecretsMount#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use when authenticating with Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_bundle(self) -> typing.Optional[builtins.str]:
        '''Concatenated PEM blocks containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_bundle DatabaseSecretsMount#pem_bundle}
        '''
        result = self._values.get("pem_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_json(self) -> typing.Optional[builtins.str]:
        '''Specifies JSON containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_json DatabaseSecretsMount#pem_json}
        '''
        result = self._values.get("pem_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The transport port to use to connect to Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#port DatabaseSecretsMount#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol_version(self) -> typing.Optional[jsii.Number]:
        '''The CQL protocol version to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#protocol_version DatabaseSecretsMount#protocol_version}
        '''
        result = self._values.get("protocol_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to use TLS when connecting to Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use when authenticating with Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountCassandra(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountCassandraList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCassandraList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountCassandraList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountCassandraOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountCassandraList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountCassandraOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCassandra]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCassandra]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCassandra]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountCassandraOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCassandraOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountCassandraOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPemBundle")
    def reset_pem_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemBundle", []))

    @jsii.member(jsii_name="resetPemJson")
    def reset_pem_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemJson", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocolVersion")
    def reset_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocolVersion", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureTlsInput")
    def insecure_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pemBundleInput")
    def pem_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="pemJsonInput")
    def pem_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolVersionInput")
    def protocol_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "protocolVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="insecureTls")
    def insecure_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureTls"))

    @insecure_tls.setter
    def insecure_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pemBundle")
    def pem_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemBundle"))

    @pem_bundle.setter
    def pem_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "pem_bundle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemBundle", value)

    @builtins.property
    @jsii.member(jsii_name="pemJson")
    def pem_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemJson"))

    @pem_json.setter
    def pem_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "pem_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemJson", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocolVersion")
    def protocol_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocolVersion"))

    @protocol_version.setter
    def protocol_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "protocol_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountCassandra, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountCassandra, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountCassandra, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCassandraOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "path": "path",
        "allowed_managed_keys": "allowedManagedKeys",
        "audit_non_hmac_request_keys": "auditNonHmacRequestKeys",
        "audit_non_hmac_response_keys": "auditNonHmacResponseKeys",
        "cassandra": "cassandra",
        "couchbase": "couchbase",
        "default_lease_ttl_seconds": "defaultLeaseTtlSeconds",
        "description": "description",
        "elasticsearch": "elasticsearch",
        "external_entropy_access": "externalEntropyAccess",
        "hana": "hana",
        "id": "id",
        "influxdb": "influxdb",
        "local": "local",
        "max_lease_ttl_seconds": "maxLeaseTtlSeconds",
        "mongodb": "mongodb",
        "mongodbatlas": "mongodbatlas",
        "mssql": "mssql",
        "mysql": "mysql",
        "mysql_aurora": "mysqlAurora",
        "mysql_legacy": "mysqlLegacy",
        "mysql_rds": "mysqlRds",
        "namespace": "namespace",
        "options": "options",
        "oracle": "oracle",
        "postgresql": "postgresql",
        "redis_elasticache": "redisElasticache",
        "redshift": "redshift",
        "seal_wrap": "sealWrap",
        "snowflake": "snowflake",
    },
)
class DatabaseSecretsMountConfig(cdktf.TerraformMetaArguments):
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
        path: builtins.str,
        allowed_managed_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_request_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_response_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        cassandra: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DatabaseSecretsMountCassandra, typing.Dict[str, typing.Any]]]]] = None,
        couchbase: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountCouchbase", typing.Dict[str, typing.Any]]]]] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        elasticsearch: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountElasticsearch", typing.Dict[str, typing.Any]]]]] = None,
        external_entropy_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hana: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountHana", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        influxdb: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountInfluxdb", typing.Dict[str, typing.Any]]]]] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        mongodb: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodb", typing.Dict[str, typing.Any]]]]] = None,
        mongodbatlas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMongodbatlas", typing.Dict[str, typing.Any]]]]] = None,
        mssql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMssql", typing.Dict[str, typing.Any]]]]] = None,
        mysql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysql", typing.Dict[str, typing.Any]]]]] = None,
        mysql_aurora: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlAurora", typing.Dict[str, typing.Any]]]]] = None,
        mysql_legacy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlLegacy", typing.Dict[str, typing.Any]]]]] = None,
        mysql_rds: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountMysqlRds", typing.Dict[str, typing.Any]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oracle: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountOracle", typing.Dict[str, typing.Any]]]]] = None,
        postgresql: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountPostgresql", typing.Dict[str, typing.Any]]]]] = None,
        redis_elasticache: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedisElasticache", typing.Dict[str, typing.Any]]]]] = None,
        redshift: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountRedshift", typing.Dict[str, typing.Any]]]]] = None,
        seal_wrap: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snowflake: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseSecretsMountSnowflake", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param path: Where the secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#path DatabaseSecretsMount#path}
        :param allowed_managed_keys: List of managed key registry entry names that the mount in question is allowed to access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_managed_keys DatabaseSecretsMount#allowed_managed_keys}
        :param audit_non_hmac_request_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the request data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_request_keys DatabaseSecretsMount#audit_non_hmac_request_keys}
        :param audit_non_hmac_response_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the response data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_response_keys DatabaseSecretsMount#audit_non_hmac_response_keys}
        :param cassandra: cassandra block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#cassandra DatabaseSecretsMount#cassandra}
        :param couchbase: couchbase block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#couchbase DatabaseSecretsMount#couchbase}
        :param default_lease_ttl_seconds: Default lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#default_lease_ttl_seconds DatabaseSecretsMount#default_lease_ttl_seconds}
        :param description: Human-friendly description of the mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#description DatabaseSecretsMount#description}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#elasticsearch DatabaseSecretsMount#elasticsearch}
        :param external_entropy_access: Enable the secrets engine to access Vault's external entropy source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#external_entropy_access DatabaseSecretsMount#external_entropy_access}
        :param hana: hana block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hana DatabaseSecretsMount#hana}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#id DatabaseSecretsMount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param influxdb: influxdb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#influxdb DatabaseSecretsMount#influxdb}
        :param local: Local mount flag that can be explicitly set to true to enforce local mount in HA environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#local DatabaseSecretsMount#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_lease_ttl_seconds DatabaseSecretsMount#max_lease_ttl_seconds}
        :param mongodb: mongodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodb DatabaseSecretsMount#mongodb}
        :param mongodbatlas: mongodbatlas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodbatlas DatabaseSecretsMount#mongodbatlas}
        :param mssql: mssql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mssql DatabaseSecretsMount#mssql}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql DatabaseSecretsMount#mysql}
        :param mysql_aurora: mysql_aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_aurora DatabaseSecretsMount#mysql_aurora}
        :param mysql_legacy: mysql_legacy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_legacy DatabaseSecretsMount#mysql_legacy}
        :param mysql_rds: mysql_rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_rds DatabaseSecretsMount#mysql_rds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#namespace DatabaseSecretsMount#namespace}
        :param options: Specifies mount type specific options that are passed to the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#options DatabaseSecretsMount#options}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#oracle DatabaseSecretsMount#oracle}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#postgresql DatabaseSecretsMount#postgresql}
        :param redis_elasticache: redis_elasticache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redis_elasticache DatabaseSecretsMount#redis_elasticache}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redshift DatabaseSecretsMount#redshift}
        :param seal_wrap: Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#seal_wrap DatabaseSecretsMount#seal_wrap}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#snowflake DatabaseSecretsMount#snowflake}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument allowed_managed_keys", value=allowed_managed_keys, expected_type=type_hints["allowed_managed_keys"])
            check_type(argname="argument audit_non_hmac_request_keys", value=audit_non_hmac_request_keys, expected_type=type_hints["audit_non_hmac_request_keys"])
            check_type(argname="argument audit_non_hmac_response_keys", value=audit_non_hmac_response_keys, expected_type=type_hints["audit_non_hmac_response_keys"])
            check_type(argname="argument cassandra", value=cassandra, expected_type=type_hints["cassandra"])
            check_type(argname="argument couchbase", value=couchbase, expected_type=type_hints["couchbase"])
            check_type(argname="argument default_lease_ttl_seconds", value=default_lease_ttl_seconds, expected_type=type_hints["default_lease_ttl_seconds"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
            check_type(argname="argument external_entropy_access", value=external_entropy_access, expected_type=type_hints["external_entropy_access"])
            check_type(argname="argument hana", value=hana, expected_type=type_hints["hana"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument influxdb", value=influxdb, expected_type=type_hints["influxdb"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument max_lease_ttl_seconds", value=max_lease_ttl_seconds, expected_type=type_hints["max_lease_ttl_seconds"])
            check_type(argname="argument mongodb", value=mongodb, expected_type=type_hints["mongodb"])
            check_type(argname="argument mongodbatlas", value=mongodbatlas, expected_type=type_hints["mongodbatlas"])
            check_type(argname="argument mssql", value=mssql, expected_type=type_hints["mssql"])
            check_type(argname="argument mysql", value=mysql, expected_type=type_hints["mysql"])
            check_type(argname="argument mysql_aurora", value=mysql_aurora, expected_type=type_hints["mysql_aurora"])
            check_type(argname="argument mysql_legacy", value=mysql_legacy, expected_type=type_hints["mysql_legacy"])
            check_type(argname="argument mysql_rds", value=mysql_rds, expected_type=type_hints["mysql_rds"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument oracle", value=oracle, expected_type=type_hints["oracle"])
            check_type(argname="argument postgresql", value=postgresql, expected_type=type_hints["postgresql"])
            check_type(argname="argument redis_elasticache", value=redis_elasticache, expected_type=type_hints["redis_elasticache"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument seal_wrap", value=seal_wrap, expected_type=type_hints["seal_wrap"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
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
        if allowed_managed_keys is not None:
            self._values["allowed_managed_keys"] = allowed_managed_keys
        if audit_non_hmac_request_keys is not None:
            self._values["audit_non_hmac_request_keys"] = audit_non_hmac_request_keys
        if audit_non_hmac_response_keys is not None:
            self._values["audit_non_hmac_response_keys"] = audit_non_hmac_response_keys
        if cassandra is not None:
            self._values["cassandra"] = cassandra
        if couchbase is not None:
            self._values["couchbase"] = couchbase
        if default_lease_ttl_seconds is not None:
            self._values["default_lease_ttl_seconds"] = default_lease_ttl_seconds
        if description is not None:
            self._values["description"] = description
        if elasticsearch is not None:
            self._values["elasticsearch"] = elasticsearch
        if external_entropy_access is not None:
            self._values["external_entropy_access"] = external_entropy_access
        if hana is not None:
            self._values["hana"] = hana
        if id is not None:
            self._values["id"] = id
        if influxdb is not None:
            self._values["influxdb"] = influxdb
        if local is not None:
            self._values["local"] = local
        if max_lease_ttl_seconds is not None:
            self._values["max_lease_ttl_seconds"] = max_lease_ttl_seconds
        if mongodb is not None:
            self._values["mongodb"] = mongodb
        if mongodbatlas is not None:
            self._values["mongodbatlas"] = mongodbatlas
        if mssql is not None:
            self._values["mssql"] = mssql
        if mysql is not None:
            self._values["mysql"] = mysql
        if mysql_aurora is not None:
            self._values["mysql_aurora"] = mysql_aurora
        if mysql_legacy is not None:
            self._values["mysql_legacy"] = mysql_legacy
        if mysql_rds is not None:
            self._values["mysql_rds"] = mysql_rds
        if namespace is not None:
            self._values["namespace"] = namespace
        if options is not None:
            self._values["options"] = options
        if oracle is not None:
            self._values["oracle"] = oracle
        if postgresql is not None:
            self._values["postgresql"] = postgresql
        if redis_elasticache is not None:
            self._values["redis_elasticache"] = redis_elasticache
        if redshift is not None:
            self._values["redshift"] = redshift
        if seal_wrap is not None:
            self._values["seal_wrap"] = seal_wrap
        if snowflake is not None:
            self._values["snowflake"] = snowflake

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
    def path(self) -> builtins.str:
        '''Where the secret backend will be mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#path DatabaseSecretsMount#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_managed_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of managed key registry entry names that the mount in question is allowed to access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_managed_keys DatabaseSecretsMount#allowed_managed_keys}
        '''
        result = self._values.get("allowed_managed_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_request_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of keys that will not be HMAC'd by audit devices in the request data object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_request_keys DatabaseSecretsMount#audit_non_hmac_request_keys}
        '''
        result = self._values.get("audit_non_hmac_request_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_response_keys(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of keys that will not be HMAC'd by audit devices in the response data object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#audit_non_hmac_response_keys DatabaseSecretsMount#audit_non_hmac_response_keys}
        '''
        result = self._values.get("audit_non_hmac_response_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cassandra(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCassandra]]]:
        '''cassandra block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#cassandra DatabaseSecretsMount#cassandra}
        '''
        result = self._values.get("cassandra")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCassandra]]], result)

    @builtins.property
    def couchbase(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCouchbase"]]]:
        '''couchbase block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#couchbase DatabaseSecretsMount#couchbase}
        '''
        result = self._values.get("couchbase")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountCouchbase"]]], result)

    @builtins.property
    def default_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Default lease duration for tokens and secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#default_lease_ttl_seconds DatabaseSecretsMount#default_lease_ttl_seconds}
        '''
        result = self._values.get("default_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-friendly description of the mount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#description DatabaseSecretsMount#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountElasticsearch"]]]:
        '''elasticsearch block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#elasticsearch DatabaseSecretsMount#elasticsearch}
        '''
        result = self._values.get("elasticsearch")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountElasticsearch"]]], result)

    @builtins.property
    def external_entropy_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the secrets engine to access Vault's external entropy source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#external_entropy_access DatabaseSecretsMount#external_entropy_access}
        '''
        result = self._values.get("external_entropy_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hana(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountHana"]]]:
        '''hana block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hana DatabaseSecretsMount#hana}
        '''
        result = self._values.get("hana")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountHana"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#id DatabaseSecretsMount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def influxdb(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountInfluxdb"]]]:
        '''influxdb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#influxdb DatabaseSecretsMount#influxdb}
        '''
        result = self._values.get("influxdb")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountInfluxdb"]]], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Local mount flag that can be explicitly set to true to enforce local mount in HA environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#local DatabaseSecretsMount#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum possible lease duration for tokens and secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_lease_ttl_seconds DatabaseSecretsMount#max_lease_ttl_seconds}
        '''
        result = self._values.get("max_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mongodb(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodb"]]]:
        '''mongodb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodb DatabaseSecretsMount#mongodb}
        '''
        result = self._values.get("mongodb")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodb"]]], result)

    @builtins.property
    def mongodbatlas(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodbatlas"]]]:
        '''mongodbatlas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mongodbatlas DatabaseSecretsMount#mongodbatlas}
        '''
        result = self._values.get("mongodbatlas")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMongodbatlas"]]], result)

    @builtins.property
    def mssql(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMssql"]]]:
        '''mssql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mssql DatabaseSecretsMount#mssql}
        '''
        result = self._values.get("mssql")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMssql"]]], result)

    @builtins.property
    def mysql(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysql"]]]:
        '''mysql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql DatabaseSecretsMount#mysql}
        '''
        result = self._values.get("mysql")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysql"]]], result)

    @builtins.property
    def mysql_aurora(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlAurora"]]]:
        '''mysql_aurora block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_aurora DatabaseSecretsMount#mysql_aurora}
        '''
        result = self._values.get("mysql_aurora")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlAurora"]]], result)

    @builtins.property
    def mysql_legacy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlLegacy"]]]:
        '''mysql_legacy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_legacy DatabaseSecretsMount#mysql_legacy}
        '''
        result = self._values.get("mysql_legacy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlLegacy"]]], result)

    @builtins.property
    def mysql_rds(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlRds"]]]:
        '''mysql_rds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#mysql_rds DatabaseSecretsMount#mysql_rds}
        '''
        result = self._values.get("mysql_rds")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountMysqlRds"]]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#namespace DatabaseSecretsMount#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies mount type specific options that are passed to the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#options DatabaseSecretsMount#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def oracle(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountOracle"]]]:
        '''oracle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#oracle DatabaseSecretsMount#oracle}
        '''
        result = self._values.get("oracle")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountOracle"]]], result)

    @builtins.property
    def postgresql(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountPostgresql"]]]:
        '''postgresql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#postgresql DatabaseSecretsMount#postgresql}
        '''
        result = self._values.get("postgresql")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountPostgresql"]]], result)

    @builtins.property
    def redis_elasticache(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedisElasticache"]]]:
        '''redis_elasticache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redis_elasticache DatabaseSecretsMount#redis_elasticache}
        '''
        result = self._values.get("redis_elasticache")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedisElasticache"]]], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedshift"]]]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#redshift DatabaseSecretsMount#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountRedshift"]]], result)

    @builtins.property
    def seal_wrap(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#seal_wrap DatabaseSecretsMount#seal_wrap}
        '''
        result = self._values.get("seal_wrap")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountSnowflake"]]]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#snowflake DatabaseSecretsMount#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseSecretsMountSnowflake"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCouchbase",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "name": "name",
        "password": "password",
        "username": "username",
        "allowed_roles": "allowedRoles",
        "base64_pem": "base64Pem",
        "bucket_name": "bucketName",
        "data": "data",
        "insecure_tls": "insecureTls",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "tls": "tls",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountCouchbase:
    def __init__(
        self,
        *,
        hosts: typing.Sequence[builtins.str],
        name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        base64_pem: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param hosts: A set of Couchbase URIs to connect to. Must use ``couchbases://`` scheme if ``tls`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hosts DatabaseSecretsMount#hosts}
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param username: Specifies the username for Vault to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param base64_pem: Required if ``tls`` is ``true``. Specifies the certificate authority of the Couchbase server, as a PEM certificate that has been base64 encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#base64_pem DatabaseSecretsMount#base64_pem}
        :param bucket_name: Required for Couchbase versions prior to 6.5.0. This is only used to verify vault's connection to the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#bucket_name DatabaseSecretsMount#bucket_name}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param insecure_tls: Specifies whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param tls: Specifies whether to use TLS when connecting to Couchbase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountCouchbase.__init__)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument base64_pem", value=base64_pem, expected_type=type_hints["base64_pem"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "hosts": hosts,
            "name": name,
            "password": password,
            "username": username,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if base64_pem is not None:
            self._values["base64_pem"] = base64_pem
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if data is not None:
            self._values["data"] = data
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if tls is not None:
            self._values["tls"] = tls
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def hosts(self) -> typing.List[builtins.str]:
        '''A set of Couchbase URIs to connect to. Must use ``couchbases://`` scheme if ``tls`` is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#hosts DatabaseSecretsMount#hosts}
        '''
        result = self._values.get("hosts")
        assert result is not None, "Required property 'hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Specifies the password corresponding to the given username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Specifies the username for Vault to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def base64_pem(self) -> typing.Optional[builtins.str]:
        '''Required if ``tls`` is ``true``.

        Specifies the certificate authority of the Couchbase server, as a PEM certificate that has been base64 encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#base64_pem DatabaseSecretsMount#base64_pem}
        '''
        result = self._values.get("base64_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Required for Couchbase versions prior to 6.5.0. This is only used to verify vault's connection to the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#bucket_name DatabaseSecretsMount#bucket_name}
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to use TLS when connecting to Couchbase.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountCouchbase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountCouchbaseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCouchbaseList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountCouchbaseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountCouchbaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountCouchbaseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountCouchbaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCouchbase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCouchbase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountCouchbase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountCouchbaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountCouchbaseOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountCouchbaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetBase64Pem")
    def reset_base64_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase64Pem", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="base64PemInput")
    def base64_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "base64PemInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureTlsInput")
    def insecure_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="base64Pem")
    def base64_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "base64Pem"))

    @base64_pem.setter
    def base64_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "base64_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base64Pem", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="insecureTls")
    def insecure_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureTls"))

    @insecure_tls.setter
    def insecure_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountCouchbase, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountCouchbase, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountCouchbase, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountCouchbaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountElasticsearch",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "url": "url",
        "username": "username",
        "allowed_roles": "allowedRoles",
        "ca_cert": "caCert",
        "ca_path": "caPath",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "data": "data",
        "insecure": "insecure",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "tls_server_name": "tlsServerName",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountElasticsearch:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        url: builtins.str,
        username: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        ca_cert: typing.Optional[builtins.str] = None,
        ca_path: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param password: The password to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param url: The URL for Elasticsearch's API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#url DatabaseSecretsMount#url}
        :param username: The username to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param ca_cert: The path to a PEM-encoded CA cert file to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#ca_cert DatabaseSecretsMount#ca_cert}
        :param ca_path: The path to a directory of PEM-encoded CA cert files to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#ca_path DatabaseSecretsMount#ca_path}
        :param client_cert: The path to the certificate for the Elasticsearch client to present for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#client_cert DatabaseSecretsMount#client_cert}
        :param client_key: The path to the key for the Elasticsearch client to use for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#client_key DatabaseSecretsMount#client_key}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param insecure: Whether to disable certificate verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure DatabaseSecretsMount#insecure}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param tls_server_name: This, if set, is used to set the SNI host when connecting via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_server_name DatabaseSecretsMount#tls_server_name}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountElasticsearch.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument ca_path", value=ca_path, expected_type=type_hints["ca_path"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "password": password,
            "url": url,
            "username": username,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if ca_path is not None:
            self._values["ca_path"] = ca_path
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if data is not None:
            self._values["data"] = data
        if insecure is not None:
            self._values["insecure"] = insecure
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password to be used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL for Elasticsearch's API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#url DatabaseSecretsMount#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username to be used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''The path to a PEM-encoded CA cert file to use to verify the Elasticsearch server's identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#ca_cert DatabaseSecretsMount#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_path(self) -> typing.Optional[builtins.str]:
        '''The path to a directory of PEM-encoded CA cert files to use to verify the Elasticsearch server's identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#ca_path DatabaseSecretsMount#ca_path}
        '''
        result = self._values.get("ca_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''The path to the certificate for the Elasticsearch client to present for communication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#client_cert DatabaseSecretsMount#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''The path to the key for the Elasticsearch client to use for communication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#client_key DatabaseSecretsMount#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to disable certificate verification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure DatabaseSecretsMount#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''This, if set, is used to set the SNI host when connecting via TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_server_name DatabaseSecretsMount#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountElasticsearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountElasticsearchList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountElasticsearchList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountElasticsearchList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountElasticsearchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountElasticsearchList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountElasticsearchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountElasticsearch]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountElasticsearch]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountElasticsearch]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountElasticsearchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountElasticsearchOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountElasticsearchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetCaPath")
    def reset_ca_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaPath", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetTlsServerName")
    def reset_tls_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsServerName", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="caPathInput")
    def ca_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsServerNameInput")
    def tls_server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "ca_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="caPath")
    def ca_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caPath"))

    @ca_path.setter
    def ca_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "ca_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPath", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "client_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "client_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="tlsServerName")
    def tls_server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsServerName"))

    @tls_server_name.setter
    def tls_server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "tls_server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsServerName", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountElasticsearch, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountElasticsearch, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountElasticsearch, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountElasticsearchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountHana",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountHana:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountHana.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if disable_escaping is not None:
            self._values["disable_escaping"] = disable_escaping
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountHana(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountHanaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountHanaList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountHanaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountHanaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountHanaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountHanaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountHana]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountHana]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountHana]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountHanaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountHanaOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountHanaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetDisableEscaping")
    def reset_disable_escaping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableEscaping", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="disableEscapingInput")
    def disable_escaping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableEscapingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="disableEscaping")
    def disable_escaping(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableEscaping"))

    @disable_escaping.setter
    def disable_escaping(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountHana, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountHana, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountHana, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountHanaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountInfluxdb",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "name": "name",
        "password": "password",
        "username": "username",
        "allowed_roles": "allowedRoles",
        "connect_timeout": "connectTimeout",
        "data": "data",
        "insecure_tls": "insecureTls",
        "pem_bundle": "pemBundle",
        "pem_json": "pemJson",
        "plugin_name": "pluginName",
        "port": "port",
        "root_rotation_statements": "rootRotationStatements",
        "tls": "tls",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountInfluxdb:
    def __init__(
        self,
        *,
        host: builtins.str,
        name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host: Influxdb host to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#host DatabaseSecretsMount#host}
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param username: Specifies the username to use for superuser access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connect_timeout DatabaseSecretsMount#connect_timeout}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_bundle DatabaseSecretsMount#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_json DatabaseSecretsMount#pem_json}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param port: The transport port to use to connect to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#port DatabaseSecretsMount#port}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param tls: Whether to use TLS when connecting to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountInfluxdb.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument pem_bundle", value=pem_bundle, expected_type=type_hints["pem_bundle"])
            check_type(argname="argument pem_json", value=pem_json, expected_type=type_hints["pem_json"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "name": name,
            "password": password,
            "username": username,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if data is not None:
            self._values["data"] = data
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if pem_bundle is not None:
            self._values["pem_bundle"] = pem_bundle
        if pem_json is not None:
            self._values["pem_json"] = pem_json
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if port is not None:
            self._values["port"] = port
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if tls is not None:
            self._values["tls"] = tls
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def host(self) -> builtins.str:
        '''Influxdb host to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#host DatabaseSecretsMount#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Specifies the password corresponding to the given username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Specifies the username to use for superuser access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to use as a connection timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connect_timeout DatabaseSecretsMount#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#insecure_tls DatabaseSecretsMount#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pem_bundle(self) -> typing.Optional[builtins.str]:
        '''Concatenated PEM blocks containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_bundle DatabaseSecretsMount#pem_bundle}
        '''
        result = self._values.get("pem_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_json(self) -> typing.Optional[builtins.str]:
        '''Specifies JSON containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#pem_json DatabaseSecretsMount#pem_json}
        '''
        result = self._values.get("pem_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The transport port to use to connect to Influxdb.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#port DatabaseSecretsMount#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to use TLS when connecting to Influxdb.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls DatabaseSecretsMount#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountInfluxdb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountInfluxdbList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountInfluxdbList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountInfluxdbList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountInfluxdbOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountInfluxdbList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountInfluxdbOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountInfluxdb]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountInfluxdb]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountInfluxdb]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountInfluxdbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountInfluxdbOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountInfluxdbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetPemBundle")
    def reset_pem_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemBundle", []))

    @jsii.member(jsii_name="resetPemJson")
    def reset_pem_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemJson", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureTlsInput")
    def insecure_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pemBundleInput")
    def pem_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="pemJsonInput")
    def pem_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="insecureTls")
    def insecure_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureTls"))

    @insecure_tls.setter
    def insecure_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pemBundle")
    def pem_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemBundle"))

    @pem_bundle.setter
    def pem_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "pem_bundle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemBundle", value)

    @builtins.property
    @jsii.member(jsii_name="pemJson")
    def pem_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemJson"))

    @pem_json.setter
    def pem_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "pem_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemJson", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountInfluxdb, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountInfluxdb, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountInfluxdb, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountInfluxdbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodb",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMongodb:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodb.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMongodb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMongodbList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodbList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountMongodbOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMongodbOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodb]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodb]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodb]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMongodbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodbOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMongodb, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMongodb, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMongodb, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodbatlas",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "private_key": "privateKey",
        "project_id": "projectId",
        "public_key": "publicKey",
        "allowed_roles": "allowedRoles",
        "data": "data",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMongodbatlas:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_key: builtins.str,
        project_id: builtins.str,
        public_key: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param private_key: The Private Programmatic API Key used to connect with MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#private_key DatabaseSecretsMount#private_key}
        :param project_id: The Project ID the Database User should be created within. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#project_id DatabaseSecretsMount#project_id}
        :param public_key: The Public Programmatic API Key used to authenticate with the MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#public_key DatabaseSecretsMount#public_key}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbatlas.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "private_key": private_key,
            "project_id": project_id,
            "public_key": public_key,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if data is not None:
            self._values["data"] = data
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''The Private Programmatic API Key used to connect with MongoDB Atlas API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#private_key DatabaseSecretsMount#private_key}
        '''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Project ID the Database User should be created within.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#project_id DatabaseSecretsMount#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_key(self) -> builtins.str:
        '''The Public Programmatic API Key used to authenticate with the MongoDB Atlas API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#public_key DatabaseSecretsMount#public_key}
        '''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMongodbatlas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMongodbatlasList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodbatlasList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbatlasList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountMongodbatlasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbatlasList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMongodbatlasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodbatlas]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodbatlas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMongodbatlas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMongodbatlasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMongodbatlasOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMongodbatlasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMongodbatlas, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMongodbatlas, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMongodbatlas, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMongodbatlasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMssql",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "contained_db": "containedDb",
        "data": "data",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMssql:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        contained_db: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param contained_db: Set to true when the target is a Contained Database, e.g. AzureSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#contained_db DatabaseSecretsMount#contained_db}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMssql.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument contained_db", value=contained_db, expected_type=type_hints["contained_db"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if contained_db is not None:
            self._values["contained_db"] = contained_db
        if data is not None:
            self._values["data"] = data
        if disable_escaping is not None:
            self._values["disable_escaping"] = disable_escaping
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contained_db(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to true when the target is a Contained Database, e.g. AzureSQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#contained_db DatabaseSecretsMount#contained_db}
        '''
        result = self._values.get("contained_db")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMssql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMssqlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMssqlList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMssqlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountMssqlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMssqlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMssqlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMssql]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMssql]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMssql]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMssqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMssqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMssqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetContainedDb")
    def reset_contained_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainedDb", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetDisableEscaping")
    def reset_disable_escaping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableEscaping", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="containedDbInput")
    def contained_db_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "containedDbInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="disableEscapingInput")
    def disable_escaping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableEscapingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="containedDb")
    def contained_db(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "containedDb"))

    @contained_db.setter
    def contained_db(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "contained_db").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containedDb", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="disableEscaping")
    def disable_escaping(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableEscaping"))

    @disable_escaping.setter
    def disable_escaping(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMssql, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMssql, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMssql, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMssqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysql",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "tls_ca": "tlsCa",
        "tls_certificate_key": "tlsCertificateKey",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMysql:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls_ca: typing.Optional[builtins.str] = None,
        tls_certificate_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param tls_ca: x509 CA file for validating the certificate presented by the MySQL server. Must be PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_ca DatabaseSecretsMount#tls_ca}
        :param tls_certificate_key: x509 certificate for connecting to the database. This must be a PEM encoded version of the private key and the certificate combined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_certificate_key DatabaseSecretsMount#tls_certificate_key}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysql.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument tls_ca", value=tls_ca, expected_type=type_hints["tls_ca"])
            check_type(argname="argument tls_certificate_key", value=tls_certificate_key, expected_type=type_hints["tls_certificate_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if tls_ca is not None:
            self._values["tls_ca"] = tls_ca
        if tls_certificate_key is not None:
            self._values["tls_certificate_key"] = tls_certificate_key
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls_ca(self) -> typing.Optional[builtins.str]:
        '''x509 CA file for validating the certificate presented by the MySQL server. Must be PEM encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_ca DatabaseSecretsMount#tls_ca}
        '''
        result = self._values.get("tls_ca")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_certificate_key(self) -> typing.Optional[builtins.str]:
        '''x509 certificate for connecting to the database.

        This must be a PEM encoded version of the private key and the certificate combined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#tls_certificate_key DatabaseSecretsMount#tls_certificate_key}
        '''
        result = self._values.get("tls_certificate_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMysql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlAurora",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMysqlAurora:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlAurora.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMysqlAurora(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMysqlAuroraList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlAuroraList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlAuroraList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountMysqlAuroraOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlAuroraList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMysqlAuroraOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlAurora]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlAurora]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlAurora]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMysqlAuroraOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlAuroraOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlAuroraOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMysqlAurora, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMysqlAurora, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMysqlAurora, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlAuroraOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlLegacy",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMysqlLegacy:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlLegacy.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMysqlLegacy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMysqlLegacyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlLegacyList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlLegacyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountMysqlLegacyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlLegacyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMysqlLegacyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlLegacy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlLegacy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlLegacy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMysqlLegacyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlLegacyOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlLegacyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMysqlLegacy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMysqlLegacy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMysqlLegacy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlLegacyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMysqlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountMysqlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMysqlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysql]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysql]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysql]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMysqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetTlsCa")
    def reset_tls_ca(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCa", []))

    @jsii.member(jsii_name="resetTlsCertificateKey")
    def reset_tls_certificate_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCertificateKey", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCaInput")
    def tls_ca_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCaInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCertificateKeyInput")
    def tls_certificate_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCertificateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCa")
    def tls_ca(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCa"))

    @tls_ca.setter
    def tls_ca(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "tls_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCa", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCertificateKey")
    def tls_certificate_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCertificateKey"))

    @tls_certificate_key.setter
    def tls_certificate_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "tls_certificate_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCertificateKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMysql, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMysql, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMysql, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlRds",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountMysqlRds:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlRds.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountMysqlRds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountMysqlRdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlRdsList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlRdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountMysqlRdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlRdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountMysqlRdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlRds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlRds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountMysqlRds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountMysqlRdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountMysqlRdsOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountMysqlRdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountMysqlRds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountMysqlRds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountMysqlRds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountMysqlRdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountOracle",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountOracle:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountOracle.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountOracle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountOracleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountOracleList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountOracleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountOracleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountOracleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountOracleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountOracle]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountOracle]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountOracle]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountOracleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountOracleOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountOracleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountOracle, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountOracle, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountOracle, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountOracleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountPostgresql",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountPostgresql:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountPostgresql.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if disable_escaping is not None:
            self._values["disable_escaping"] = disable_escaping
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountPostgresql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountPostgresqlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountPostgresqlList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountPostgresqlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountPostgresqlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountPostgresqlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountPostgresqlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountPostgresql]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountPostgresql]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountPostgresql]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountPostgresqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountPostgresqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountPostgresqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetDisableEscaping")
    def reset_disable_escaping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableEscaping", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="disableEscapingInput")
    def disable_escaping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableEscapingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="disableEscaping")
    def disable_escaping(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableEscaping"))

    @disable_escaping.setter
    def disable_escaping(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountPostgresql, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountPostgresql, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountPostgresql, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountPostgresqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedisElasticache",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "url": "url",
        "allowed_roles": "allowedRoles",
        "data": "data",
        "password": "password",
        "plugin_name": "pluginName",
        "region": "region",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountRedisElasticache:
    def __init__(
        self,
        *,
        name: builtins.str,
        url: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param url: The configuration endpoint for the ElastiCache cluster to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#url DatabaseSecretsMount#url}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param password: The AWS secret key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param region: The AWS region where the ElastiCache cluster is hosted. If omitted the plugin tries to infer the region from the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#region DatabaseSecretsMount#region}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The AWS access key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedisElasticache.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "url": url,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if data is not None:
            self._values["data"] = data
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if region is not None:
            self._values["region"] = region
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The configuration endpoint for the ElastiCache cluster to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#url DatabaseSecretsMount#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The AWS secret key id to use to talk to ElastiCache.

        If omitted the credentials chain provider is used instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region where the ElastiCache cluster is hosted.

        If omitted the plugin tries to infer the region from the environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#region DatabaseSecretsMount#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The AWS access key id to use to talk to ElastiCache.

        If omitted the credentials chain provider is used instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountRedisElasticache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountRedisElasticacheList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedisElasticacheList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedisElasticacheList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabaseSecretsMountRedisElasticacheOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedisElasticacheList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountRedisElasticacheOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedisElasticache]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedisElasticache]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedisElasticache]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountRedisElasticacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedisElasticacheOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedisElasticacheOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountRedisElasticache, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountRedisElasticache, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountRedisElasticache, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedisElasticacheOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountRedshift:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedshift.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if disable_escaping is not None:
            self._values["disable_escaping"] = disable_escaping
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#disable_escaping DatabaseSecretsMount#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountRedshiftList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedshiftList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedshiftList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountRedshiftOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedshiftList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountRedshiftOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedshift]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedshift]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountRedshift]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountRedshiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountRedshiftOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetDisableEscaping")
    def reset_disable_escaping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableEscaping", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="disableEscapingInput")
    def disable_escaping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableEscapingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="disableEscaping")
    def disable_escaping(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableEscaping"))

    @disable_escaping.setter
    def disable_escaping(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountRedshift, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountRedshift, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountRedshift, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountRedshiftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_roles": "allowedRoles",
        "connection_url": "connectionUrl",
        "data": "data",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "plugin_name": "pluginName",
        "root_rotation_statements": "rootRotationStatements",
        "username": "username",
        "username_template": "usernameTemplate",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretsMountSnowflake:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_url: typing.Optional[builtins.str] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountSnowflake.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if data is not None:
            self._values["data"] = data
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#name DatabaseSecretsMount#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#allowed_roles DatabaseSecretsMount#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#connection_url DatabaseSecretsMount#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#data DatabaseSecretsMount#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_connection_lifetime DatabaseSecretsMount#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_idle_connections DatabaseSecretsMount#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#max_open_connections DatabaseSecretsMount#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#password DatabaseSecretsMount#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#plugin_name DatabaseSecretsMount#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#root_rotation_statements DatabaseSecretsMount#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username DatabaseSecretsMount#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#username_template DatabaseSecretsMount#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secrets_mount#verify_connection DatabaseSecretsMount#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretsMountSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretsMountSnowflakeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountSnowflakeList",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountSnowflakeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseSecretsMountSnowflakeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretsMountSnowflakeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseSecretsMountSnowflakeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountSnowflake]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountSnowflake]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseSecretsMountSnowflake]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretsMountSnowflakeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretsMount.DatabaseSecretsMountSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretsMountSnowflakeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetMaxConnectionLifetime")
    def reset_max_connection_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionLifetime", []))

    @jsii.member(jsii_name="resetMaxIdleConnections")
    def reset_max_idle_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnections", []))

    @jsii.member(jsii_name="resetMaxOpenConnections")
    def reset_max_open_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetimeInput")
    def max_connection_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsInput")
    def max_idle_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnectionsInput")
    def max_open_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyConnectionInput")
    def verify_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRoles")
    def allowed_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRoles"))

    @allowed_roles.setter
    def allowed_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "root_rotation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootRotationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="verifyConnection")
    def verify_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyConnection"))

    @verify_connection.setter
    def verify_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseSecretsMountSnowflake, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseSecretsMountSnowflake, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseSecretsMountSnowflake, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretsMountSnowflakeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatabaseSecretsMount",
    "DatabaseSecretsMountCassandra",
    "DatabaseSecretsMountCassandraList",
    "DatabaseSecretsMountCassandraOutputReference",
    "DatabaseSecretsMountConfig",
    "DatabaseSecretsMountCouchbase",
    "DatabaseSecretsMountCouchbaseList",
    "DatabaseSecretsMountCouchbaseOutputReference",
    "DatabaseSecretsMountElasticsearch",
    "DatabaseSecretsMountElasticsearchList",
    "DatabaseSecretsMountElasticsearchOutputReference",
    "DatabaseSecretsMountHana",
    "DatabaseSecretsMountHanaList",
    "DatabaseSecretsMountHanaOutputReference",
    "DatabaseSecretsMountInfluxdb",
    "DatabaseSecretsMountInfluxdbList",
    "DatabaseSecretsMountInfluxdbOutputReference",
    "DatabaseSecretsMountMongodb",
    "DatabaseSecretsMountMongodbList",
    "DatabaseSecretsMountMongodbOutputReference",
    "DatabaseSecretsMountMongodbatlas",
    "DatabaseSecretsMountMongodbatlasList",
    "DatabaseSecretsMountMongodbatlasOutputReference",
    "DatabaseSecretsMountMssql",
    "DatabaseSecretsMountMssqlList",
    "DatabaseSecretsMountMssqlOutputReference",
    "DatabaseSecretsMountMysql",
    "DatabaseSecretsMountMysqlAurora",
    "DatabaseSecretsMountMysqlAuroraList",
    "DatabaseSecretsMountMysqlAuroraOutputReference",
    "DatabaseSecretsMountMysqlLegacy",
    "DatabaseSecretsMountMysqlLegacyList",
    "DatabaseSecretsMountMysqlLegacyOutputReference",
    "DatabaseSecretsMountMysqlList",
    "DatabaseSecretsMountMysqlOutputReference",
    "DatabaseSecretsMountMysqlRds",
    "DatabaseSecretsMountMysqlRdsList",
    "DatabaseSecretsMountMysqlRdsOutputReference",
    "DatabaseSecretsMountOracle",
    "DatabaseSecretsMountOracleList",
    "DatabaseSecretsMountOracleOutputReference",
    "DatabaseSecretsMountPostgresql",
    "DatabaseSecretsMountPostgresqlList",
    "DatabaseSecretsMountPostgresqlOutputReference",
    "DatabaseSecretsMountRedisElasticache",
    "DatabaseSecretsMountRedisElasticacheList",
    "DatabaseSecretsMountRedisElasticacheOutputReference",
    "DatabaseSecretsMountRedshift",
    "DatabaseSecretsMountRedshiftList",
    "DatabaseSecretsMountRedshiftOutputReference",
    "DatabaseSecretsMountSnowflake",
    "DatabaseSecretsMountSnowflakeList",
    "DatabaseSecretsMountSnowflakeOutputReference",
]

publication.publish()
