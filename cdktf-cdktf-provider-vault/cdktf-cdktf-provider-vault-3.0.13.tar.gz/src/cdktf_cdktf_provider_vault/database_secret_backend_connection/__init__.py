'''
# `vault_database_secret_backend_connection`

Refer to the Terraform Registory for docs: [`vault_database_secret_backend_connection`](https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection).
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


class DatabaseSecretBackendConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection vault_database_secret_backend_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        cassandra: typing.Optional[typing.Union["DatabaseSecretBackendConnectionCassandra", typing.Dict[str, typing.Any]]] = None,
        couchbase: typing.Optional[typing.Union["DatabaseSecretBackendConnectionCouchbase", typing.Dict[str, typing.Any]]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticsearch: typing.Optional[typing.Union["DatabaseSecretBackendConnectionElasticsearch", typing.Dict[str, typing.Any]]] = None,
        hana: typing.Optional[typing.Union["DatabaseSecretBackendConnectionHana", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        influxdb: typing.Optional[typing.Union["DatabaseSecretBackendConnectionInfluxdb", typing.Dict[str, typing.Any]]] = None,
        mongodb: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMongodb", typing.Dict[str, typing.Any]]] = None,
        mongodbatlas: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMongodbatlas", typing.Dict[str, typing.Any]]] = None,
        mssql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMssql", typing.Dict[str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysql", typing.Dict[str, typing.Any]]] = None,
        mysql_aurora: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlAurora", typing.Dict[str, typing.Any]]] = None,
        mysql_legacy: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlLegacy", typing.Dict[str, typing.Any]]] = None,
        mysql_rds: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlRds", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        oracle: typing.Optional[typing.Union["DatabaseSecretBackendConnectionOracle", typing.Dict[str, typing.Any]]] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        postgresql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionPostgresql", typing.Dict[str, typing.Any]]] = None,
        redis_elasticache: typing.Optional[typing.Union["DatabaseSecretBackendConnectionRedisElasticache", typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["DatabaseSecretBackendConnectionRedshift", typing.Dict[str, typing.Any]]] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        snowflake: typing.Optional[typing.Union["DatabaseSecretBackendConnectionSnowflake", typing.Dict[str, typing.Any]]] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection vault_database_secret_backend_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: Unique name of the Vault mount to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#backend DatabaseSecretBackendConnection#backend}
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#name DatabaseSecretBackendConnection#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#allowed_roles DatabaseSecretBackendConnection#allowed_roles}
        :param cassandra: cassandra block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#cassandra DatabaseSecretBackendConnection#cassandra}
        :param couchbase: couchbase block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#couchbase DatabaseSecretBackendConnection#couchbase}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#data DatabaseSecretBackendConnection#data}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#elasticsearch DatabaseSecretBackendConnection#elasticsearch}
        :param hana: hana block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hana DatabaseSecretBackendConnection#hana}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#id DatabaseSecretBackendConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param influxdb: influxdb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#influxdb DatabaseSecretBackendConnection#influxdb}
        :param mongodb: mongodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodb DatabaseSecretBackendConnection#mongodb}
        :param mongodbatlas: mongodbatlas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodbatlas DatabaseSecretBackendConnection#mongodbatlas}
        :param mssql: mssql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mssql DatabaseSecretBackendConnection#mssql}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql DatabaseSecretBackendConnection#mysql}
        :param mysql_aurora: mysql_aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_aurora DatabaseSecretBackendConnection#mysql_aurora}
        :param mysql_legacy: mysql_legacy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_legacy DatabaseSecretBackendConnection#mysql_legacy}
        :param mysql_rds: mysql_rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_rds DatabaseSecretBackendConnection#mysql_rds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#namespace DatabaseSecretBackendConnection#namespace}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#oracle DatabaseSecretBackendConnection#oracle}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#plugin_name DatabaseSecretBackendConnection#plugin_name}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#postgresql DatabaseSecretBackendConnection#postgresql}
        :param redis_elasticache: redis_elasticache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redis_elasticache DatabaseSecretBackendConnection#redis_elasticache}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redshift DatabaseSecretBackendConnection#redshift}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#root_rotation_statements DatabaseSecretBackendConnection#root_rotation_statements}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#snowflake DatabaseSecretBackendConnection#snowflake}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#verify_connection DatabaseSecretBackendConnection#verify_connection}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseSecretBackendConnectionConfig(
            backend=backend,
            name=name,
            allowed_roles=allowed_roles,
            cassandra=cassandra,
            couchbase=couchbase,
            data=data,
            elasticsearch=elasticsearch,
            hana=hana,
            id=id,
            influxdb=influxdb,
            mongodb=mongodb,
            mongodbatlas=mongodbatlas,
            mssql=mssql,
            mysql=mysql,
            mysql_aurora=mysql_aurora,
            mysql_legacy=mysql_legacy,
            mysql_rds=mysql_rds,
            namespace=namespace,
            oracle=oracle,
            plugin_name=plugin_name,
            postgresql=postgresql,
            redis_elasticache=redis_elasticache,
            redshift=redshift,
            root_rotation_statements=root_rotation_statements,
            snowflake=snowflake,
            verify_connection=verify_connection,
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
        *,
        connect_timeout: typing.Optional[jsii.Number] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol_version: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        :param hosts: Cassandra hosts to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param password: The password to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        :param port: The transport port to use to connect to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        :param protocol_version: The CQL protocol version to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#protocol_version DatabaseSecretBackendConnection#protocol_version}
        :param tls: Whether to use TLS when connecting to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username: The username to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        value = DatabaseSecretBackendConnectionCassandra(
            connect_timeout=connect_timeout,
            hosts=hosts,
            insecure_tls=insecure_tls,
            password=password,
            pem_bundle=pem_bundle,
            pem_json=pem_json,
            port=port,
            protocol_version=protocol_version,
            tls=tls,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putCassandra", [value]))

    @jsii.member(jsii_name="putCouchbase")
    def put_couchbase(
        self,
        *,
        hosts: typing.Sequence[builtins.str],
        password: builtins.str,
        username: builtins.str,
        base64_pem: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: A set of Couchbase URIs to connect to. Must use ``couchbases://`` scheme if ``tls`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: Specifies the username for Vault to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param base64_pem: Required if ``tls`` is ``true``. Specifies the certificate authority of the Couchbase server, as a PEM certificate that has been base64 encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#base64_pem DatabaseSecretBackendConnection#base64_pem}
        :param bucket_name: Required for Couchbase versions prior to 6.5.0. This is only used to verify vault's connection to the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#bucket_name DatabaseSecretBackendConnection#bucket_name}
        :param insecure_tls: Specifies whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param tls: Specifies whether to use TLS when connecting to Couchbase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionCouchbase(
            hosts=hosts,
            password=password,
            username=username,
            base64_pem=base64_pem,
            bucket_name=bucket_name,
            insecure_tls=insecure_tls,
            tls=tls,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putCouchbase", [value]))

    @jsii.member(jsii_name="putElasticsearch")
    def put_elasticsearch(
        self,
        *,
        password: builtins.str,
        url: builtins.str,
        username: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        ca_path: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: The password to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param url: The URL for Elasticsearch's API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        :param username: The username to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param ca_cert: The path to a PEM-encoded CA cert file to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_cert DatabaseSecretBackendConnection#ca_cert}
        :param ca_path: The path to a directory of PEM-encoded CA cert files to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_path DatabaseSecretBackendConnection#ca_path}
        :param client_cert: The path to the certificate for the Elasticsearch client to present for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_cert DatabaseSecretBackendConnection#client_cert}
        :param client_key: The path to the key for the Elasticsearch client to use for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_key DatabaseSecretBackendConnection#client_key}
        :param insecure: Whether to disable certificate verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure DatabaseSecretBackendConnection#insecure}
        :param tls_server_name: This, if set, is used to set the SNI host when connecting via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_server_name DatabaseSecretBackendConnection#tls_server_name}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionElasticsearch(
            password=password,
            url=url,
            username=username,
            ca_cert=ca_cert,
            ca_path=ca_path,
            client_cert=client_cert,
            client_key=client_key,
            insecure=insecure,
            tls_server_name=tls_server_name,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearch", [value]))

    @jsii.member(jsii_name="putHana")
    def put_hana(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        value = DatabaseSecretBackendConnectionHana(
            connection_url=connection_url,
            disable_escaping=disable_escaping,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putHana", [value]))

    @jsii.member(jsii_name="putInfluxdb")
    def put_influxdb(
        self,
        *,
        host: builtins.str,
        password: builtins.str,
        username: builtins.str,
        connect_timeout: typing.Optional[jsii.Number] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Influxdb host to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#host DatabaseSecretBackendConnection#host}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: Specifies the username to use for superuser access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        :param port: The transport port to use to connect to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        :param tls: Whether to use TLS when connecting to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionInfluxdb(
            host=host,
            password=password,
            username=username,
            connect_timeout=connect_timeout,
            insecure_tls=insecure_tls,
            pem_bundle=pem_bundle,
            pem_json=pem_json,
            port=port,
            tls=tls,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putInfluxdb", [value]))

    @jsii.member(jsii_name="putMongodb")
    def put_mongodb(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMongodb(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMongodb", [value]))

    @jsii.member(jsii_name="putMongodbatlas")
    def put_mongodbatlas(
        self,
        *,
        private_key: builtins.str,
        project_id: builtins.str,
        public_key: builtins.str,
    ) -> None:
        '''
        :param private_key: The Private Programmatic API Key used to connect with MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#private_key DatabaseSecretBackendConnection#private_key}
        :param project_id: The Project ID the Database User should be created within. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#project_id DatabaseSecretBackendConnection#project_id}
        :param public_key: The Public Programmatic API Key used to authenticate with the MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#public_key DatabaseSecretBackendConnection#public_key}
        '''
        value = DatabaseSecretBackendConnectionMongodbatlas(
            private_key=private_key, project_id=project_id, public_key=public_key
        )

        return typing.cast(None, jsii.invoke(self, "putMongodbatlas", [value]))

    @jsii.member(jsii_name="putMssql")
    def put_mssql(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        contained_db: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param contained_db: Set to true when the target is a Contained Database, e.g. AzureSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#contained_db DatabaseSecretBackendConnection#contained_db}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMssql(
            connection_url=connection_url,
            contained_db=contained_db,
            disable_escaping=disable_escaping,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMssql", [value]))

    @jsii.member(jsii_name="putMysql")
    def put_mysql(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        tls_ca: typing.Optional[builtins.str] = None,
        tls_certificate_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param tls_ca: x509 CA file for validating the certificate presented by the MySQL server. Must be PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_ca DatabaseSecretBackendConnection#tls_ca}
        :param tls_certificate_key: x509 certificate for connecting to the database. This must be a PEM encoded version of the private key and the certificate combined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_certificate_key DatabaseSecretBackendConnection#tls_certificate_key}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMysql(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            tls_ca=tls_ca,
            tls_certificate_key=tls_certificate_key,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMysql", [value]))

    @jsii.member(jsii_name="putMysqlAurora")
    def put_mysql_aurora(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMysqlAurora(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlAurora", [value]))

    @jsii.member(jsii_name="putMysqlLegacy")
    def put_mysql_legacy(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMysqlLegacy(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlLegacy", [value]))

    @jsii.member(jsii_name="putMysqlRds")
    def put_mysql_rds(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionMysqlRds(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlRds", [value]))

    @jsii.member(jsii_name="putOracle")
    def put_oracle(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionOracle(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putOracle", [value]))

    @jsii.member(jsii_name="putPostgresql")
    def put_postgresql(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionPostgresql(
            connection_url=connection_url,
            disable_escaping=disable_escaping,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putPostgresql", [value]))

    @jsii.member(jsii_name="putRedisElasticache")
    def put_redis_elasticache(
        self,
        *,
        url: builtins.str,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: The configuration endpoint for the ElastiCache cluster to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        :param password: The AWS secret key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param region: The AWS region where the ElastiCache cluster is hosted. If omitted the plugin tries to infer the region from the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#region DatabaseSecretBackendConnection#region}
        :param username: The AWS access key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        value = DatabaseSecretBackendConnectionRedisElasticache(
            url=url, password=password, region=region, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putRedisElasticache", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionRedshift(
            connection_url=connection_url,
            disable_escaping=disable_escaping,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        value = DatabaseSecretBackendConnectionSnowflake(
            connection_url=connection_url,
            max_connection_lifetime=max_connection_lifetime,
            max_idle_connections=max_idle_connections,
            max_open_connections=max_open_connections,
            password=password,
            username=username,
            username_template=username_template,
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="resetAllowedRoles")
    def reset_allowed_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRoles", []))

    @jsii.member(jsii_name="resetCassandra")
    def reset_cassandra(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCassandra", []))

    @jsii.member(jsii_name="resetCouchbase")
    def reset_couchbase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCouchbase", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetElasticsearch")
    def reset_elasticsearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearch", []))

    @jsii.member(jsii_name="resetHana")
    def reset_hana(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHana", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInfluxdb")
    def reset_influxdb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfluxdb", []))

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

    @jsii.member(jsii_name="resetOracle")
    def reset_oracle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracle", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetPostgresql")
    def reset_postgresql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresql", []))

    @jsii.member(jsii_name="resetRedisElasticache")
    def reset_redis_elasticache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisElasticache", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetRootRotationStatements")
    def reset_root_rotation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootRotationStatements", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetVerifyConnection")
    def reset_verify_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyConnection", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cassandra")
    def cassandra(self) -> "DatabaseSecretBackendConnectionCassandraOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionCassandraOutputReference", jsii.get(self, "cassandra"))

    @builtins.property
    @jsii.member(jsii_name="couchbase")
    def couchbase(self) -> "DatabaseSecretBackendConnectionCouchbaseOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionCouchbaseOutputReference", jsii.get(self, "couchbase"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearch")
    def elasticsearch(
        self,
    ) -> "DatabaseSecretBackendConnectionElasticsearchOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionElasticsearchOutputReference", jsii.get(self, "elasticsearch"))

    @builtins.property
    @jsii.member(jsii_name="hana")
    def hana(self) -> "DatabaseSecretBackendConnectionHanaOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionHanaOutputReference", jsii.get(self, "hana"))

    @builtins.property
    @jsii.member(jsii_name="influxdb")
    def influxdb(self) -> "DatabaseSecretBackendConnectionInfluxdbOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionInfluxdbOutputReference", jsii.get(self, "influxdb"))

    @builtins.property
    @jsii.member(jsii_name="mongodb")
    def mongodb(self) -> "DatabaseSecretBackendConnectionMongodbOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMongodbOutputReference", jsii.get(self, "mongodb"))

    @builtins.property
    @jsii.member(jsii_name="mongodbatlas")
    def mongodbatlas(
        self,
    ) -> "DatabaseSecretBackendConnectionMongodbatlasOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMongodbatlasOutputReference", jsii.get(self, "mongodbatlas"))

    @builtins.property
    @jsii.member(jsii_name="mssql")
    def mssql(self) -> "DatabaseSecretBackendConnectionMssqlOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMssqlOutputReference", jsii.get(self, "mssql"))

    @builtins.property
    @jsii.member(jsii_name="mysql")
    def mysql(self) -> "DatabaseSecretBackendConnectionMysqlOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMysqlOutputReference", jsii.get(self, "mysql"))

    @builtins.property
    @jsii.member(jsii_name="mysqlAurora")
    def mysql_aurora(
        self,
    ) -> "DatabaseSecretBackendConnectionMysqlAuroraOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMysqlAuroraOutputReference", jsii.get(self, "mysqlAurora"))

    @builtins.property
    @jsii.member(jsii_name="mysqlLegacy")
    def mysql_legacy(
        self,
    ) -> "DatabaseSecretBackendConnectionMysqlLegacyOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMysqlLegacyOutputReference", jsii.get(self, "mysqlLegacy"))

    @builtins.property
    @jsii.member(jsii_name="mysqlRds")
    def mysql_rds(self) -> "DatabaseSecretBackendConnectionMysqlRdsOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionMysqlRdsOutputReference", jsii.get(self, "mysqlRds"))

    @builtins.property
    @jsii.member(jsii_name="oracle")
    def oracle(self) -> "DatabaseSecretBackendConnectionOracleOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionOracleOutputReference", jsii.get(self, "oracle"))

    @builtins.property
    @jsii.member(jsii_name="postgresql")
    def postgresql(self) -> "DatabaseSecretBackendConnectionPostgresqlOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionPostgresqlOutputReference", jsii.get(self, "postgresql"))

    @builtins.property
    @jsii.member(jsii_name="redisElasticache")
    def redis_elasticache(
        self,
    ) -> "DatabaseSecretBackendConnectionRedisElasticacheOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionRedisElasticacheOutputReference", jsii.get(self, "redisElasticache"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(self) -> "DatabaseSecretBackendConnectionRedshiftOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(self) -> "DatabaseSecretBackendConnectionSnowflakeOutputReference":
        return typing.cast("DatabaseSecretBackendConnectionSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="allowedRolesInput")
    def allowed_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="cassandraInput")
    def cassandra_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionCassandra"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionCassandra"], jsii.get(self, "cassandraInput"))

    @builtins.property
    @jsii.member(jsii_name="couchbaseInput")
    def couchbase_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionCouchbase"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionCouchbase"], jsii.get(self, "couchbaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchInput")
    def elasticsearch_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionElasticsearch"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionElasticsearch"], jsii.get(self, "elasticsearchInput"))

    @builtins.property
    @jsii.member(jsii_name="hanaInput")
    def hana_input(self) -> typing.Optional["DatabaseSecretBackendConnectionHana"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionHana"], jsii.get(self, "hanaInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="influxdbInput")
    def influxdb_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionInfluxdb"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionInfluxdb"], jsii.get(self, "influxdbInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbatlasInput")
    def mongodbatlas_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMongodbatlas"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMongodbatlas"], jsii.get(self, "mongodbatlasInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbInput")
    def mongodb_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMongodb"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMongodb"], jsii.get(self, "mongodbInput"))

    @builtins.property
    @jsii.member(jsii_name="mssqlInput")
    def mssql_input(self) -> typing.Optional["DatabaseSecretBackendConnectionMssql"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMssql"], jsii.get(self, "mssqlInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlAuroraInput")
    def mysql_aurora_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMysqlAurora"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlAurora"], jsii.get(self, "mysqlAuroraInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlInput")
    def mysql_input(self) -> typing.Optional["DatabaseSecretBackendConnectionMysql"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysql"], jsii.get(self, "mysqlInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlLegacyInput")
    def mysql_legacy_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMysqlLegacy"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlLegacy"], jsii.get(self, "mysqlLegacyInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlRdsInput")
    def mysql_rds_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMysqlRds"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlRds"], jsii.get(self, "mysqlRdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleInput")
    def oracle_input(self) -> typing.Optional["DatabaseSecretBackendConnectionOracle"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionOracle"], jsii.get(self, "oracleInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlInput")
    def postgresql_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionPostgresql"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionPostgresql"], jsii.get(self, "postgresqlInput"))

    @builtins.property
    @jsii.member(jsii_name="redisElasticacheInput")
    def redis_elasticache_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionRedisElasticache"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionRedisElasticache"], jsii.get(self, "redisElasticacheInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionRedshift"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatementsInput")
    def root_rotation_statements_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rootRotationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionSnowflake"]:
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionSnowflake"], jsii.get(self, "snowflakeInput"))

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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "allowed_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="rootRotationStatements")
    def root_rotation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rootRotationStatements"))

    @root_rotation_statements.setter
    def root_rotation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "root_rotation_statements").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnection, "verify_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyConnection", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionCassandra",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "hosts": "hosts",
        "insecure_tls": "insecureTls",
        "password": "password",
        "pem_bundle": "pemBundle",
        "pem_json": "pemJson",
        "port": "port",
        "protocol_version": "protocolVersion",
        "tls": "tls",
        "username": "username",
    },
)
class DatabaseSecretBackendConnectionCassandra:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[jsii.Number] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol_version: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        :param hosts: Cassandra hosts to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param password: The password to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        :param port: The transport port to use to connect to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        :param protocol_version: The CQL protocol version to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#protocol_version DatabaseSecretBackendConnection#protocol_version}
        :param tls: Whether to use TLS when connecting to Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username: The username to use when authenticating with Cassandra. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionCassandra.__init__)
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument pem_bundle", value=pem_bundle, expected_type=type_hints["pem_bundle"])
            check_type(argname="argument pem_json", value=pem_json, expected_type=type_hints["pem_json"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
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
        if port is not None:
            self._values["port"] = port
        if protocol_version is not None:
            self._values["protocol_version"] = protocol_version
        if tls is not None:
            self._values["tls"] = tls
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to use as a connection timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Cassandra hosts to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use when authenticating with Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_bundle(self) -> typing.Optional[builtins.str]:
        '''Concatenated PEM blocks containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        '''
        result = self._values.get("pem_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_json(self) -> typing.Optional[builtins.str]:
        '''Specifies JSON containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        '''
        result = self._values.get("pem_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The transport port to use to connect to Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol_version(self) -> typing.Optional[jsii.Number]:
        '''The CQL protocol version to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#protocol_version DatabaseSecretBackendConnection#protocol_version}
        '''
        result = self._values.get("protocol_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to use TLS when connecting to Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use when authenticating with Cassandra.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionCassandra(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionCassandraOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionCassandraOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionCassandraOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

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

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocolVersion")
    def reset_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocolVersion", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

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
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolVersionInput")
    def protocol_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "protocolVersionInput"))

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
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "hosts").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pemBundle")
    def pem_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemBundle"))

    @pem_bundle.setter
    def pem_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "pem_bundle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemBundle", value)

    @builtins.property
    @jsii.member(jsii_name="pemJson")
    def pem_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemJson"))

    @pem_json.setter
    def pem_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "pem_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemJson", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocolVersion")
    def protocol_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocolVersion"))

    @protocol_version.setter
    def protocol_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "protocol_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionCassandra]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionCassandra], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionCassandra],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCassandraOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "name": "name",
        "allowed_roles": "allowedRoles",
        "cassandra": "cassandra",
        "couchbase": "couchbase",
        "data": "data",
        "elasticsearch": "elasticsearch",
        "hana": "hana",
        "id": "id",
        "influxdb": "influxdb",
        "mongodb": "mongodb",
        "mongodbatlas": "mongodbatlas",
        "mssql": "mssql",
        "mysql": "mysql",
        "mysql_aurora": "mysqlAurora",
        "mysql_legacy": "mysqlLegacy",
        "mysql_rds": "mysqlRds",
        "namespace": "namespace",
        "oracle": "oracle",
        "plugin_name": "pluginName",
        "postgresql": "postgresql",
        "redis_elasticache": "redisElasticache",
        "redshift": "redshift",
        "root_rotation_statements": "rootRotationStatements",
        "snowflake": "snowflake",
        "verify_connection": "verifyConnection",
    },
)
class DatabaseSecretBackendConnectionConfig(cdktf.TerraformMetaArguments):
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
        backend: builtins.str,
        name: builtins.str,
        allowed_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        cassandra: typing.Optional[typing.Union[DatabaseSecretBackendConnectionCassandra, typing.Dict[str, typing.Any]]] = None,
        couchbase: typing.Optional[typing.Union["DatabaseSecretBackendConnectionCouchbase", typing.Dict[str, typing.Any]]] = None,
        data: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticsearch: typing.Optional[typing.Union["DatabaseSecretBackendConnectionElasticsearch", typing.Dict[str, typing.Any]]] = None,
        hana: typing.Optional[typing.Union["DatabaseSecretBackendConnectionHana", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        influxdb: typing.Optional[typing.Union["DatabaseSecretBackendConnectionInfluxdb", typing.Dict[str, typing.Any]]] = None,
        mongodb: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMongodb", typing.Dict[str, typing.Any]]] = None,
        mongodbatlas: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMongodbatlas", typing.Dict[str, typing.Any]]] = None,
        mssql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMssql", typing.Dict[str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysql", typing.Dict[str, typing.Any]]] = None,
        mysql_aurora: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlAurora", typing.Dict[str, typing.Any]]] = None,
        mysql_legacy: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlLegacy", typing.Dict[str, typing.Any]]] = None,
        mysql_rds: typing.Optional[typing.Union["DatabaseSecretBackendConnectionMysqlRds", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        oracle: typing.Optional[typing.Union["DatabaseSecretBackendConnectionOracle", typing.Dict[str, typing.Any]]] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        postgresql: typing.Optional[typing.Union["DatabaseSecretBackendConnectionPostgresql", typing.Dict[str, typing.Any]]] = None,
        redis_elasticache: typing.Optional[typing.Union["DatabaseSecretBackendConnectionRedisElasticache", typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["DatabaseSecretBackendConnectionRedshift", typing.Dict[str, typing.Any]]] = None,
        root_rotation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        snowflake: typing.Optional[typing.Union["DatabaseSecretBackendConnectionSnowflake", typing.Dict[str, typing.Any]]] = None,
        verify_connection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: Unique name of the Vault mount to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#backend DatabaseSecretBackendConnection#backend}
        :param name: Name of the database connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#name DatabaseSecretBackendConnection#name}
        :param allowed_roles: A list of roles that are allowed to use this connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#allowed_roles DatabaseSecretBackendConnection#allowed_roles}
        :param cassandra: cassandra block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#cassandra DatabaseSecretBackendConnection#cassandra}
        :param couchbase: couchbase block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#couchbase DatabaseSecretBackendConnection#couchbase}
        :param data: A map of sensitive data to pass to the endpoint. Useful for templated connection strings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#data DatabaseSecretBackendConnection#data}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#elasticsearch DatabaseSecretBackendConnection#elasticsearch}
        :param hana: hana block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hana DatabaseSecretBackendConnection#hana}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#id DatabaseSecretBackendConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param influxdb: influxdb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#influxdb DatabaseSecretBackendConnection#influxdb}
        :param mongodb: mongodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodb DatabaseSecretBackendConnection#mongodb}
        :param mongodbatlas: mongodbatlas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodbatlas DatabaseSecretBackendConnection#mongodbatlas}
        :param mssql: mssql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mssql DatabaseSecretBackendConnection#mssql}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql DatabaseSecretBackendConnection#mysql}
        :param mysql_aurora: mysql_aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_aurora DatabaseSecretBackendConnection#mysql_aurora}
        :param mysql_legacy: mysql_legacy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_legacy DatabaseSecretBackendConnection#mysql_legacy}
        :param mysql_rds: mysql_rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_rds DatabaseSecretBackendConnection#mysql_rds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#namespace DatabaseSecretBackendConnection#namespace}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#oracle DatabaseSecretBackendConnection#oracle}
        :param plugin_name: Specifies the name of the plugin to use for this connection. Must be prefixed with the name of one of the supported database engine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#plugin_name DatabaseSecretBackendConnection#plugin_name}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#postgresql DatabaseSecretBackendConnection#postgresql}
        :param redis_elasticache: redis_elasticache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redis_elasticache DatabaseSecretBackendConnection#redis_elasticache}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redshift DatabaseSecretBackendConnection#redshift}
        :param root_rotation_statements: A list of database statements to be executed to rotate the root user's credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#root_rotation_statements DatabaseSecretBackendConnection#root_rotation_statements}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#snowflake DatabaseSecretBackendConnection#snowflake}
        :param verify_connection: Specifies if the connection is verified during initial configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#verify_connection DatabaseSecretBackendConnection#verify_connection}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cassandra, dict):
            cassandra = DatabaseSecretBackendConnectionCassandra(**cassandra)
        if isinstance(couchbase, dict):
            couchbase = DatabaseSecretBackendConnectionCouchbase(**couchbase)
        if isinstance(elasticsearch, dict):
            elasticsearch = DatabaseSecretBackendConnectionElasticsearch(**elasticsearch)
        if isinstance(hana, dict):
            hana = DatabaseSecretBackendConnectionHana(**hana)
        if isinstance(influxdb, dict):
            influxdb = DatabaseSecretBackendConnectionInfluxdb(**influxdb)
        if isinstance(mongodb, dict):
            mongodb = DatabaseSecretBackendConnectionMongodb(**mongodb)
        if isinstance(mongodbatlas, dict):
            mongodbatlas = DatabaseSecretBackendConnectionMongodbatlas(**mongodbatlas)
        if isinstance(mssql, dict):
            mssql = DatabaseSecretBackendConnectionMssql(**mssql)
        if isinstance(mysql, dict):
            mysql = DatabaseSecretBackendConnectionMysql(**mysql)
        if isinstance(mysql_aurora, dict):
            mysql_aurora = DatabaseSecretBackendConnectionMysqlAurora(**mysql_aurora)
        if isinstance(mysql_legacy, dict):
            mysql_legacy = DatabaseSecretBackendConnectionMysqlLegacy(**mysql_legacy)
        if isinstance(mysql_rds, dict):
            mysql_rds = DatabaseSecretBackendConnectionMysqlRds(**mysql_rds)
        if isinstance(oracle, dict):
            oracle = DatabaseSecretBackendConnectionOracle(**oracle)
        if isinstance(postgresql, dict):
            postgresql = DatabaseSecretBackendConnectionPostgresql(**postgresql)
        if isinstance(redis_elasticache, dict):
            redis_elasticache = DatabaseSecretBackendConnectionRedisElasticache(**redis_elasticache)
        if isinstance(redshift, dict):
            redshift = DatabaseSecretBackendConnectionRedshift(**redshift)
        if isinstance(snowflake, dict):
            snowflake = DatabaseSecretBackendConnectionSnowflake(**snowflake)
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_roles", value=allowed_roles, expected_type=type_hints["allowed_roles"])
            check_type(argname="argument cassandra", value=cassandra, expected_type=type_hints["cassandra"])
            check_type(argname="argument couchbase", value=couchbase, expected_type=type_hints["couchbase"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
            check_type(argname="argument hana", value=hana, expected_type=type_hints["hana"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument influxdb", value=influxdb, expected_type=type_hints["influxdb"])
            check_type(argname="argument mongodb", value=mongodb, expected_type=type_hints["mongodb"])
            check_type(argname="argument mongodbatlas", value=mongodbatlas, expected_type=type_hints["mongodbatlas"])
            check_type(argname="argument mssql", value=mssql, expected_type=type_hints["mssql"])
            check_type(argname="argument mysql", value=mysql, expected_type=type_hints["mysql"])
            check_type(argname="argument mysql_aurora", value=mysql_aurora, expected_type=type_hints["mysql_aurora"])
            check_type(argname="argument mysql_legacy", value=mysql_legacy, expected_type=type_hints["mysql_legacy"])
            check_type(argname="argument mysql_rds", value=mysql_rds, expected_type=type_hints["mysql_rds"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument oracle", value=oracle, expected_type=type_hints["oracle"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument postgresql", value=postgresql, expected_type=type_hints["postgresql"])
            check_type(argname="argument redis_elasticache", value=redis_elasticache, expected_type=type_hints["redis_elasticache"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument root_rotation_statements", value=root_rotation_statements, expected_type=type_hints["root_rotation_statements"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument verify_connection", value=verify_connection, expected_type=type_hints["verify_connection"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
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
        if allowed_roles is not None:
            self._values["allowed_roles"] = allowed_roles
        if cassandra is not None:
            self._values["cassandra"] = cassandra
        if couchbase is not None:
            self._values["couchbase"] = couchbase
        if data is not None:
            self._values["data"] = data
        if elasticsearch is not None:
            self._values["elasticsearch"] = elasticsearch
        if hana is not None:
            self._values["hana"] = hana
        if id is not None:
            self._values["id"] = id
        if influxdb is not None:
            self._values["influxdb"] = influxdb
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
        if oracle is not None:
            self._values["oracle"] = oracle
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if postgresql is not None:
            self._values["postgresql"] = postgresql
        if redis_elasticache is not None:
            self._values["redis_elasticache"] = redis_elasticache
        if redshift is not None:
            self._values["redshift"] = redshift
        if root_rotation_statements is not None:
            self._values["root_rotation_statements"] = root_rotation_statements
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if verify_connection is not None:
            self._values["verify_connection"] = verify_connection

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
    def backend(self) -> builtins.str:
        '''Unique name of the Vault mount to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#backend DatabaseSecretBackendConnection#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the database connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#name DatabaseSecretBackendConnection#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of roles that are allowed to use this connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#allowed_roles DatabaseSecretBackendConnection#allowed_roles}
        '''
        result = self._values.get("allowed_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cassandra(self) -> typing.Optional[DatabaseSecretBackendConnectionCassandra]:
        '''cassandra block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#cassandra DatabaseSecretBackendConnection#cassandra}
        '''
        result = self._values.get("cassandra")
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionCassandra], result)

    @builtins.property
    def couchbase(self) -> typing.Optional["DatabaseSecretBackendConnectionCouchbase"]:
        '''couchbase block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#couchbase DatabaseSecretBackendConnection#couchbase}
        '''
        result = self._values.get("couchbase")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionCouchbase"], result)

    @builtins.property
    def data(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of sensitive data to pass to the endpoint. Useful for templated connection strings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#data DatabaseSecretBackendConnection#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elasticsearch(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionElasticsearch"]:
        '''elasticsearch block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#elasticsearch DatabaseSecretBackendConnection#elasticsearch}
        '''
        result = self._values.get("elasticsearch")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionElasticsearch"], result)

    @builtins.property
    def hana(self) -> typing.Optional["DatabaseSecretBackendConnectionHana"]:
        '''hana block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hana DatabaseSecretBackendConnection#hana}
        '''
        result = self._values.get("hana")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionHana"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#id DatabaseSecretBackendConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def influxdb(self) -> typing.Optional["DatabaseSecretBackendConnectionInfluxdb"]:
        '''influxdb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#influxdb DatabaseSecretBackendConnection#influxdb}
        '''
        result = self._values.get("influxdb")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionInfluxdb"], result)

    @builtins.property
    def mongodb(self) -> typing.Optional["DatabaseSecretBackendConnectionMongodb"]:
        '''mongodb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodb DatabaseSecretBackendConnection#mongodb}
        '''
        result = self._values.get("mongodb")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMongodb"], result)

    @builtins.property
    def mongodbatlas(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMongodbatlas"]:
        '''mongodbatlas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mongodbatlas DatabaseSecretBackendConnection#mongodbatlas}
        '''
        result = self._values.get("mongodbatlas")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMongodbatlas"], result)

    @builtins.property
    def mssql(self) -> typing.Optional["DatabaseSecretBackendConnectionMssql"]:
        '''mssql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mssql DatabaseSecretBackendConnection#mssql}
        '''
        result = self._values.get("mssql")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMssql"], result)

    @builtins.property
    def mysql(self) -> typing.Optional["DatabaseSecretBackendConnectionMysql"]:
        '''mysql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql DatabaseSecretBackendConnection#mysql}
        '''
        result = self._values.get("mysql")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysql"], result)

    @builtins.property
    def mysql_aurora(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMysqlAurora"]:
        '''mysql_aurora block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_aurora DatabaseSecretBackendConnection#mysql_aurora}
        '''
        result = self._values.get("mysql_aurora")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlAurora"], result)

    @builtins.property
    def mysql_legacy(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionMysqlLegacy"]:
        '''mysql_legacy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_legacy DatabaseSecretBackendConnection#mysql_legacy}
        '''
        result = self._values.get("mysql_legacy")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlLegacy"], result)

    @builtins.property
    def mysql_rds(self) -> typing.Optional["DatabaseSecretBackendConnectionMysqlRds"]:
        '''mysql_rds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#mysql_rds DatabaseSecretBackendConnection#mysql_rds}
        '''
        result = self._values.get("mysql_rds")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionMysqlRds"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#namespace DatabaseSecretBackendConnection#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oracle(self) -> typing.Optional["DatabaseSecretBackendConnectionOracle"]:
        '''oracle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#oracle DatabaseSecretBackendConnection#oracle}
        '''
        result = self._values.get("oracle")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionOracle"], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the plugin to use for this connection.

        Must be prefixed with the name of one of the supported database engine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#plugin_name DatabaseSecretBackendConnection#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postgresql(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionPostgresql"]:
        '''postgresql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#postgresql DatabaseSecretBackendConnection#postgresql}
        '''
        result = self._values.get("postgresql")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionPostgresql"], result)

    @builtins.property
    def redis_elasticache(
        self,
    ) -> typing.Optional["DatabaseSecretBackendConnectionRedisElasticache"]:
        '''redis_elasticache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redis_elasticache DatabaseSecretBackendConnection#redis_elasticache}
        '''
        result = self._values.get("redis_elasticache")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionRedisElasticache"], result)

    @builtins.property
    def redshift(self) -> typing.Optional["DatabaseSecretBackendConnectionRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#redshift DatabaseSecretBackendConnection#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionRedshift"], result)

    @builtins.property
    def root_rotation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database statements to be executed to rotate the root user's credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#root_rotation_statements DatabaseSecretBackendConnection#root_rotation_statements}
        '''
        result = self._values.get("root_rotation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snowflake(self) -> typing.Optional["DatabaseSecretBackendConnectionSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#snowflake DatabaseSecretBackendConnection#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["DatabaseSecretBackendConnectionSnowflake"], result)

    @builtins.property
    def verify_connection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the connection is verified during initial configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#verify_connection DatabaseSecretBackendConnection#verify_connection}
        '''
        result = self._values.get("verify_connection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionCouchbase",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "password": "password",
        "username": "username",
        "base64_pem": "base64Pem",
        "bucket_name": "bucketName",
        "insecure_tls": "insecureTls",
        "tls": "tls",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionCouchbase:
    def __init__(
        self,
        *,
        hosts: typing.Sequence[builtins.str],
        password: builtins.str,
        username: builtins.str,
        base64_pem: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: A set of Couchbase URIs to connect to. Must use ``couchbases://`` scheme if ``tls`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: Specifies the username for Vault to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param base64_pem: Required if ``tls`` is ``true``. Specifies the certificate authority of the Couchbase server, as a PEM certificate that has been base64 encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#base64_pem DatabaseSecretBackendConnection#base64_pem}
        :param bucket_name: Required for Couchbase versions prior to 6.5.0. This is only used to verify vault's connection to the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#bucket_name DatabaseSecretBackendConnection#bucket_name}
        :param insecure_tls: Specifies whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param tls: Specifies whether to use TLS when connecting to Couchbase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionCouchbase.__init__)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument base64_pem", value=base64_pem, expected_type=type_hints["base64_pem"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "hosts": hosts,
            "password": password,
            "username": username,
        }
        if base64_pem is not None:
            self._values["base64_pem"] = base64_pem
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if tls is not None:
            self._values["tls"] = tls
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def hosts(self) -> typing.List[builtins.str]:
        '''A set of Couchbase URIs to connect to. Must use ``couchbases://`` scheme if ``tls`` is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#hosts DatabaseSecretBackendConnection#hosts}
        '''
        result = self._values.get("hosts")
        assert result is not None, "Required property 'hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Specifies the password corresponding to the given username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Specifies the username for Vault to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base64_pem(self) -> typing.Optional[builtins.str]:
        '''Required if ``tls`` is ``true``.

        Specifies the certificate authority of the Couchbase server, as a PEM certificate that has been base64 encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#base64_pem DatabaseSecretBackendConnection#base64_pem}
        '''
        result = self._values.get("base64_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Required for Couchbase versions prior to 6.5.0. This is only used to verify vault's connection to the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#bucket_name DatabaseSecretBackendConnection#bucket_name}
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to use TLS when connecting to Couchbase.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionCouchbase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionCouchbaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionCouchbaseOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionCouchbaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBase64Pem")
    def reset_base64_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase64Pem", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="base64PemInput")
    def base64_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "base64PemInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

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
    @jsii.member(jsii_name="base64Pem")
    def base64_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "base64Pem"))

    @base64_pem.setter
    def base64_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "base64_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base64Pem", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "hosts").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionCouchbase]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionCouchbase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionCouchbase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionCouchbaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionElasticsearch",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "url": "url",
        "username": "username",
        "ca_cert": "caCert",
        "ca_path": "caPath",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "insecure": "insecure",
        "tls_server_name": "tlsServerName",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionElasticsearch:
    def __init__(
        self,
        *,
        password: builtins.str,
        url: builtins.str,
        username: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        ca_path: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: The password to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param url: The URL for Elasticsearch's API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        :param username: The username to be used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param ca_cert: The path to a PEM-encoded CA cert file to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_cert DatabaseSecretBackendConnection#ca_cert}
        :param ca_path: The path to a directory of PEM-encoded CA cert files to use to verify the Elasticsearch server's identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_path DatabaseSecretBackendConnection#ca_path}
        :param client_cert: The path to the certificate for the Elasticsearch client to present for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_cert DatabaseSecretBackendConnection#client_cert}
        :param client_key: The path to the key for the Elasticsearch client to use for communication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_key DatabaseSecretBackendConnection#client_key}
        :param insecure: Whether to disable certificate verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure DatabaseSecretBackendConnection#insecure}
        :param tls_server_name: This, if set, is used to set the SNI host when connecting via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_server_name DatabaseSecretBackendConnection#tls_server_name}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionElasticsearch.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument ca_path", value=ca_path, expected_type=type_hints["ca_path"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "url": url,
            "username": username,
        }
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if ca_path is not None:
            self._values["ca_path"] = ca_path
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if insecure is not None:
            self._values["insecure"] = insecure
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def password(self) -> builtins.str:
        '''The password to be used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL for Elasticsearch's API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username to be used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''The path to a PEM-encoded CA cert file to use to verify the Elasticsearch server's identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_cert DatabaseSecretBackendConnection#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_path(self) -> typing.Optional[builtins.str]:
        '''The path to a directory of PEM-encoded CA cert files to use to verify the Elasticsearch server's identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#ca_path DatabaseSecretBackendConnection#ca_path}
        '''
        result = self._values.get("ca_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''The path to the certificate for the Elasticsearch client to present for communication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_cert DatabaseSecretBackendConnection#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''The path to the key for the Elasticsearch client to use for communication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#client_key DatabaseSecretBackendConnection#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to disable certificate verification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure DatabaseSecretBackendConnection#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''This, if set, is used to set the SNI host when connecting via TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_server_name DatabaseSecretBackendConnection#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionElasticsearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionElasticsearchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionElasticsearchOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionElasticsearchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetTlsServerName")
    def reset_tls_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsServerName", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

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
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

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
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "ca_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="caPath")
    def ca_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caPath"))

    @ca_path.setter
    def ca_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "ca_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPath", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "client_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "client_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tlsServerName")
    def tls_server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsServerName"))

    @tls_server_name.setter
    def tls_server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "tls_server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsServerName", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionElasticsearch]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionElasticsearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionElasticsearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionElasticsearchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionHana",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
    },
)
class DatabaseSecretBackendConnectionHana:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionHana.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
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
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionHana(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionHanaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionHanaOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionHanaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseSecretBackendConnectionHana]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionHana], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionHana],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionHanaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionInfluxdb",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "password": "password",
        "username": "username",
        "connect_timeout": "connectTimeout",
        "insecure_tls": "insecureTls",
        "pem_bundle": "pemBundle",
        "pem_json": "pemJson",
        "port": "port",
        "tls": "tls",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionInfluxdb:
    def __init__(
        self,
        *,
        host: builtins.str,
        password: builtins.str,
        username: builtins.str,
        connect_timeout: typing.Optional[jsii.Number] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pem_bundle: typing.Optional[builtins.str] = None,
        pem_json: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Influxdb host to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#host DatabaseSecretBackendConnection#host}
        :param password: Specifies the password corresponding to the given username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: Specifies the username to use for superuser access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param connect_timeout: The number of seconds to use as a connection timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        :param insecure_tls: Whether to skip verification of the server certificate when using TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        :param pem_bundle: Concatenated PEM blocks containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        :param pem_json: Specifies JSON containing a certificate and private key; a certificate, private key, and issuing CA certificate; or just a CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        :param port: The transport port to use to connect to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        :param tls: Whether to use TLS when connecting to Influxdb. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        :param username_template: Template describing how dynamic usernames are generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionInfluxdb.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument pem_bundle", value=pem_bundle, expected_type=type_hints["pem_bundle"])
            check_type(argname="argument pem_json", value=pem_json, expected_type=type_hints["pem_json"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "password": password,
            "username": username,
        }
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if pem_bundle is not None:
            self._values["pem_bundle"] = pem_bundle
        if pem_json is not None:
            self._values["pem_json"] = pem_json
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def host(self) -> builtins.str:
        '''Influxdb host to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#host DatabaseSecretBackendConnection#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Specifies the password corresponding to the given username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Specifies the username to use for superuser access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to use as a connection timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connect_timeout DatabaseSecretBackendConnection#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to skip verification of the server certificate when using TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#insecure_tls DatabaseSecretBackendConnection#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pem_bundle(self) -> typing.Optional[builtins.str]:
        '''Concatenated PEM blocks containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_bundle DatabaseSecretBackendConnection#pem_bundle}
        '''
        result = self._values.get("pem_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_json(self) -> typing.Optional[builtins.str]:
        '''Specifies JSON containing a certificate and private key;

        a certificate, private key, and issuing CA certificate; or just a CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#pem_json DatabaseSecretBackendConnection#pem_json}
        '''
        result = self._values.get("pem_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The transport port to use to connect to Influxdb.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#port DatabaseSecretBackendConnection#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to use TLS when connecting to Influxdb.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls DatabaseSecretBackendConnection#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Template describing how dynamic usernames are generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionInfluxdb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionInfluxdbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionInfluxdbOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionInfluxdbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetPemBundle")
    def reset_pem_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemBundle", []))

    @jsii.member(jsii_name="resetPemJson")
    def reset_pem_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemJson", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

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
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

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
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "host").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pemBundle")
    def pem_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemBundle"))

    @pem_bundle.setter
    def pem_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "pem_bundle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemBundle", value)

    @builtins.property
    @jsii.member(jsii_name="pemJson")
    def pem_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemJson"))

    @pem_json.setter
    def pem_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "pem_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemJson", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionInfluxdb]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionInfluxdb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionInfluxdb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionInfluxdbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMongodb",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMongodb:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMongodb.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMongodb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMongodbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMongodbOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMongodbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseSecretBackendConnectionMongodb]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMongodb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMongodb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMongodbatlas",
    jsii_struct_bases=[],
    name_mapping={
        "private_key": "privateKey",
        "project_id": "projectId",
        "public_key": "publicKey",
    },
)
class DatabaseSecretBackendConnectionMongodbatlas:
    def __init__(
        self,
        *,
        private_key: builtins.str,
        project_id: builtins.str,
        public_key: builtins.str,
    ) -> None:
        '''
        :param private_key: The Private Programmatic API Key used to connect with MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#private_key DatabaseSecretBackendConnection#private_key}
        :param project_id: The Project ID the Database User should be created within. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#project_id DatabaseSecretBackendConnection#project_id}
        :param public_key: The Public Programmatic API Key used to authenticate with the MongoDB Atlas API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#public_key DatabaseSecretBackendConnection#public_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMongodbatlas.__init__)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "private_key": private_key,
            "project_id": project_id,
            "public_key": public_key,
        }

    @builtins.property
    def private_key(self) -> builtins.str:
        '''The Private Programmatic API Key used to connect with MongoDB Atlas API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#private_key DatabaseSecretBackendConnection#private_key}
        '''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Project ID the Database User should be created within.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#project_id DatabaseSecretBackendConnection#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_key(self) -> builtins.str:
        '''The Public Programmatic API Key used to authenticate with the MongoDB Atlas API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#public_key DatabaseSecretBackendConnection#public_key}
        '''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMongodbatlas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMongodbatlasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMongodbatlasOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMongodbatlasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbatlasOutputReference, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbatlasOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbatlasOutputReference, "public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionMongodbatlas]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMongodbatlas], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMongodbatlas],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMongodbatlasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMssql",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "contained_db": "containedDb",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMssql:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        contained_db: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param contained_db: Set to true when the target is a Contained Database, e.g. AzureSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#contained_db DatabaseSecretBackendConnection#contained_db}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMssql.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument contained_db", value=contained_db, expected_type=type_hints["contained_db"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if contained_db is not None:
            self._values["contained_db"] = contained_db
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
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contained_db(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to true when the target is a Contained Database, e.g. AzureSQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#contained_db DatabaseSecretBackendConnection#contained_db}
        '''
        result = self._values.get("contained_db")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMssql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMssqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMssqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMssqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

    @jsii.member(jsii_name="resetContainedDb")
    def reset_contained_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainedDb", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "connection_url").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "contained_db").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containedDb", value)

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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseSecretBackendConnectionMssql]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMssql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMssql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMssqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysql",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "tls_ca": "tlsCa",
        "tls_certificate_key": "tlsCertificateKey",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMysql:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        tls_ca: typing.Optional[builtins.str] = None,
        tls_certificate_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param tls_ca: x509 CA file for validating the certificate presented by the MySQL server. Must be PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_ca DatabaseSecretBackendConnection#tls_ca}
        :param tls_certificate_key: x509 certificate for connecting to the database. This must be a PEM encoded version of the private key and the certificate combined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_certificate_key DatabaseSecretBackendConnection#tls_certificate_key}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysql.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tls_ca", value=tls_ca, expected_type=type_hints["tls_ca"])
            check_type(argname="argument tls_certificate_key", value=tls_certificate_key, expected_type=type_hints["tls_certificate_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if tls_ca is not None:
            self._values["tls_ca"] = tls_ca
        if tls_certificate_key is not None:
            self._values["tls_certificate_key"] = tls_certificate_key
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_ca(self) -> typing.Optional[builtins.str]:
        '''x509 CA file for validating the certificate presented by the MySQL server. Must be PEM encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_ca DatabaseSecretBackendConnection#tls_ca}
        '''
        result = self._values.get("tls_ca")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_certificate_key(self) -> typing.Optional[builtins.str]:
        '''x509 certificate for connecting to the database.

        This must be a PEM encoded version of the private key and the certificate combined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#tls_certificate_key DatabaseSecretBackendConnection#tls_certificate_key}
        '''
        result = self._values.get("tls_certificate_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMysql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlAurora",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMysqlAurora:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlAurora.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMysqlAurora(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMysqlAuroraOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlAuroraOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlAuroraOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionMysqlAurora]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMysqlAurora], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMysqlAurora],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlAuroraOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlLegacy",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMysqlLegacy:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlLegacy.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMysqlLegacy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMysqlLegacyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlLegacyOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlLegacyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionMysqlLegacy]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMysqlLegacy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMysqlLegacy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlLegacyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseSecretBackendConnectionMysqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

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
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCa")
    def tls_ca(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCa"))

    @tls_ca.setter
    def tls_ca(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "tls_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCa", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCertificateKey")
    def tls_certificate_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCertificateKey"))

    @tls_certificate_key.setter
    def tls_certificate_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "tls_certificate_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCertificateKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseSecretBackendConnectionMysql]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMysql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMysql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlRds",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionMysqlRds:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlRds.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionMysqlRds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionMysqlRdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionMysqlRdsOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionMysqlRdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionMysqlRds]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionMysqlRds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionMysqlRds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionMysqlRdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionOracle",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionOracle:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionOracle.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionOracle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionOracleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionOracleOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionOracleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseSecretBackendConnectionOracle]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionOracle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionOracle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionOracleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionPostgresql",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionPostgresql:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionPostgresql.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
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
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionPostgresql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionPostgresqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionPostgresqlOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionPostgresqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionPostgresql]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionPostgresql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionPostgresql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionPostgresqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionRedisElasticache",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "password": "password",
        "region": "region",
        "username": "username",
    },
)
class DatabaseSecretBackendConnectionRedisElasticache:
    def __init__(
        self,
        *,
        url: builtins.str,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: The configuration endpoint for the ElastiCache cluster to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        :param password: The AWS secret key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param region: The AWS region where the ElastiCache cluster is hosted. If omitted the plugin tries to infer the region from the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#region DatabaseSecretBackendConnection#region}
        :param username: The AWS access key id to use to talk to ElastiCache. If omitted the credentials chain provider is used instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionRedisElasticache.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if password is not None:
            self._values["password"] = password
        if region is not None:
            self._values["region"] = region
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def url(self) -> builtins.str:
        '''The configuration endpoint for the ElastiCache cluster to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#url DatabaseSecretBackendConnection#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The AWS secret key id to use to talk to ElastiCache.

        If omitted the credentials chain provider is used instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region where the ElastiCache cluster is hosted.

        If omitted the plugin tries to infer the region from the environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#region DatabaseSecretBackendConnection#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The AWS access key id to use to talk to ElastiCache.

        If omitted the credentials chain provider is used instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionRedisElasticache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionRedisElasticacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionRedisElasticacheOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionRedisElasticacheOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedisElasticacheOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedisElasticacheOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedisElasticacheOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedisElasticacheOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionRedisElasticache]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionRedisElasticache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionRedisElasticache],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedisElasticacheOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "disable_escaping": "disableEscaping",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionRedshift:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        disable_escaping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param disable_escaping: Disable special character escaping in username and password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionRedshift.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument disable_escaping", value=disable_escaping, expected_type=type_hints["disable_escaping"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
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
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_escaping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable special character escaping in username and password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#disable_escaping DatabaseSecretBackendConnection#disable_escaping}
        '''
        result = self._values.get("disable_escaping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionRedshiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionRedshiftOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

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
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "disable_escaping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEscaping", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionRedshift]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionRedshift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionRedshiftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "connection_url": "connectionUrl",
        "max_connection_lifetime": "maxConnectionLifetime",
        "max_idle_connections": "maxIdleConnections",
        "max_open_connections": "maxOpenConnections",
        "password": "password",
        "username": "username",
        "username_template": "usernameTemplate",
    },
)
class DatabaseSecretBackendConnectionSnowflake:
    def __init__(
        self,
        *,
        connection_url: typing.Optional[builtins.str] = None,
        max_connection_lifetime: typing.Optional[jsii.Number] = None,
        max_idle_connections: typing.Optional[jsii.Number] = None,
        max_open_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        username_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_url: Connection string to use to connect to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        :param max_connection_lifetime: Maximum number of seconds a connection may be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        :param max_idle_connections: Maximum number of idle connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        :param max_open_connections: Maximum number of open connections to the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        :param password: The root credential password used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        :param username: The root credential username used in the connection URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        :param username_template: Username generation template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionSnowflake.__init__)
            check_type(argname="argument connection_url", value=connection_url, expected_type=type_hints["connection_url"])
            check_type(argname="argument max_connection_lifetime", value=max_connection_lifetime, expected_type=type_hints["max_connection_lifetime"])
            check_type(argname="argument max_idle_connections", value=max_idle_connections, expected_type=type_hints["max_idle_connections"])
            check_type(argname="argument max_open_connections", value=max_open_connections, expected_type=type_hints["max_open_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument username_template", value=username_template, expected_type=type_hints["username_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_url is not None:
            self._values["connection_url"] = connection_url
        if max_connection_lifetime is not None:
            self._values["max_connection_lifetime"] = max_connection_lifetime
        if max_idle_connections is not None:
            self._values["max_idle_connections"] = max_idle_connections
        if max_open_connections is not None:
            self._values["max_open_connections"] = max_open_connections
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username
        if username_template is not None:
            self._values["username_template"] = username_template

    @builtins.property
    def connection_url(self) -> typing.Optional[builtins.str]:
        '''Connection string to use to connect to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#connection_url DatabaseSecretBackendConnection#connection_url}
        '''
        result = self._values.get("connection_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connection_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds a connection may be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_connection_lifetime DatabaseSecretBackendConnection#max_connection_lifetime}
        '''
        result = self._values.get("max_connection_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_idle_connections DatabaseSecretBackendConnection#max_idle_connections}
        '''
        result = self._values.get("max_idle_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of open connections to the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#max_open_connections DatabaseSecretBackendConnection#max_open_connections}
        '''
        result = self._values.get("max_open_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The root credential password used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#password DatabaseSecretBackendConnection#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The root credential username used in the connection URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username DatabaseSecretBackendConnection#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_template(self) -> typing.Optional[builtins.str]:
        '''Username generation template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_connection#username_template DatabaseSecretBackendConnection#username_template}
        '''
        result = self._values.get("username_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendConnectionSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecretBackendConnectionSnowflakeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendConnection.DatabaseSecretBackendConnectionSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseSecretBackendConnectionSnowflakeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionUrl")
    def reset_connection_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionUrl", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetUsernameTemplate")
    def reset_username_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameTemplateInput")
    def username_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "connection_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionLifetime")
    def max_connection_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionLifetime"))

    @max_connection_lifetime.setter
    def max_connection_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "max_connection_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnections")
    def max_idle_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnections"))

    @max_idle_connections.setter
    def max_idle_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "max_idle_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnections")
    def max_open_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConnections"))

    @max_open_connections.setter
    def max_open_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "max_open_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="usernameTemplate")
    def username_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameTemplate"))

    @username_template.setter
    def username_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "username_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseSecretBackendConnectionSnowflake]:
        return typing.cast(typing.Optional[DatabaseSecretBackendConnectionSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseSecretBackendConnectionSnowflake],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendConnectionSnowflakeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatabaseSecretBackendConnection",
    "DatabaseSecretBackendConnectionCassandra",
    "DatabaseSecretBackendConnectionCassandraOutputReference",
    "DatabaseSecretBackendConnectionConfig",
    "DatabaseSecretBackendConnectionCouchbase",
    "DatabaseSecretBackendConnectionCouchbaseOutputReference",
    "DatabaseSecretBackendConnectionElasticsearch",
    "DatabaseSecretBackendConnectionElasticsearchOutputReference",
    "DatabaseSecretBackendConnectionHana",
    "DatabaseSecretBackendConnectionHanaOutputReference",
    "DatabaseSecretBackendConnectionInfluxdb",
    "DatabaseSecretBackendConnectionInfluxdbOutputReference",
    "DatabaseSecretBackendConnectionMongodb",
    "DatabaseSecretBackendConnectionMongodbOutputReference",
    "DatabaseSecretBackendConnectionMongodbatlas",
    "DatabaseSecretBackendConnectionMongodbatlasOutputReference",
    "DatabaseSecretBackendConnectionMssql",
    "DatabaseSecretBackendConnectionMssqlOutputReference",
    "DatabaseSecretBackendConnectionMysql",
    "DatabaseSecretBackendConnectionMysqlAurora",
    "DatabaseSecretBackendConnectionMysqlAuroraOutputReference",
    "DatabaseSecretBackendConnectionMysqlLegacy",
    "DatabaseSecretBackendConnectionMysqlLegacyOutputReference",
    "DatabaseSecretBackendConnectionMysqlOutputReference",
    "DatabaseSecretBackendConnectionMysqlRds",
    "DatabaseSecretBackendConnectionMysqlRdsOutputReference",
    "DatabaseSecretBackendConnectionOracle",
    "DatabaseSecretBackendConnectionOracleOutputReference",
    "DatabaseSecretBackendConnectionPostgresql",
    "DatabaseSecretBackendConnectionPostgresqlOutputReference",
    "DatabaseSecretBackendConnectionRedisElasticache",
    "DatabaseSecretBackendConnectionRedisElasticacheOutputReference",
    "DatabaseSecretBackendConnectionRedshift",
    "DatabaseSecretBackendConnectionRedshiftOutputReference",
    "DatabaseSecretBackendConnectionSnowflake",
    "DatabaseSecretBackendConnectionSnowflakeOutputReference",
]

publication.publish()
