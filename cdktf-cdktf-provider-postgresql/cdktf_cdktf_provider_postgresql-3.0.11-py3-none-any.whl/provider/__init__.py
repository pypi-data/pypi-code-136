'''
# `provider`

Refer to the Terraform Registory for docs: [`postgresql`](https://www.terraform.io/docs/providers/postgresql).
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


class PostgresqlProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-postgresql.provider.PostgresqlProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/postgresql postgresql}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_rds_iam_profile: typing.Optional[builtins.str] = None,
        clientcert: typing.Optional[typing.Union["PostgresqlProviderClientcert", typing.Dict[str, typing.Any]]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        database: typing.Optional[builtins.str] = None,
        database_username: typing.Optional[builtins.str] = None,
        expected_version: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
        sslmode: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sslrootcert: typing.Optional[builtins.str] = None,
        superuser: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/postgresql postgresql} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#alias PostgresqlProvider#alias}
        :param aws_rds_iam_auth: Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        :param aws_rds_iam_profile: AWS profile to use for IAM auth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        :param clientcert: clientcert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#clientcert PostgresqlProvider#clientcert}
        :param connect_timeout: Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#connect_timeout PostgresqlProvider#connect_timeout}
        :param database: The name of the database to connect to in order to conenct to (defaults to ``postgres``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database PostgresqlProvider#database}
        :param database_username: Database username associated to the connected user (for user name maps). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database_username PostgresqlProvider#database_username}
        :param expected_version: Specify the expected version of PostgreSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#expected_version PostgresqlProvider#expected_version}
        :param host: Name of PostgreSQL server address to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#host PostgresqlProvider#host}
        :param max_connections: Maximum number of connections to establish to the database. Zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#max_connections PostgresqlProvider#max_connections}
        :param password: Password to be used if the PostgreSQL server demands password authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#password PostgresqlProvider#password}
        :param port: The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#port PostgresqlProvider#port}
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#scheme PostgresqlProvider#scheme}.
        :param sslmode: This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslmode PostgresqlProvider#sslmode}
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#ssl_mode PostgresqlProvider#ssl_mode}.
        :param sslrootcert: The SSL server root certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslrootcert PostgresqlProvider#sslrootcert}
        :param superuser: Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#superuser PostgresqlProvider#superuser}
        :param username: PostgreSQL user name to connect as. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#username PostgresqlProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PostgresqlProviderConfig(
            alias=alias,
            aws_rds_iam_auth=aws_rds_iam_auth,
            aws_rds_iam_profile=aws_rds_iam_profile,
            clientcert=clientcert,
            connect_timeout=connect_timeout,
            database=database,
            database_username=database_username,
            expected_version=expected_version,
            host=host,
            max_connections=max_connections,
            password=password,
            port=port,
            scheme=scheme,
            sslmode=sslmode,
            ssl_mode=ssl_mode,
            sslrootcert=sslrootcert,
            superuser=superuser,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAwsRdsIamAuth")
    def reset_aws_rds_iam_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRdsIamAuth", []))

    @jsii.member(jsii_name="resetAwsRdsIamProfile")
    def reset_aws_rds_iam_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRdsIamProfile", []))

    @jsii.member(jsii_name="resetClientcert")
    def reset_clientcert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientcert", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDatabaseUsername")
    def reset_database_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseUsername", []))

    @jsii.member(jsii_name="resetExpectedVersion")
    def reset_expected_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedVersion", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetMaxConnections")
    def reset_max_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @jsii.member(jsii_name="resetSslmode")
    def reset_sslmode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslmode", []))

    @jsii.member(jsii_name="resetSslMode")
    def reset_ssl_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslMode", []))

    @jsii.member(jsii_name="resetSslrootcert")
    def reset_sslrootcert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslrootcert", []))

    @jsii.member(jsii_name="resetSuperuser")
    def reset_superuser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuperuser", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamAuthInput")
    def aws_rds_iam_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsRdsIamAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamProfileInput")
    def aws_rds_iam_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="clientcertInput")
    def clientcert_input(self) -> typing.Optional["PostgresqlProviderClientcert"]:
        return typing.cast(typing.Optional["PostgresqlProviderClientcert"], jsii.get(self, "clientcertInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseUsernameInput")
    def database_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedVersionInput")
    def expected_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslmodeInput")
    def sslmode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslmodeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslModeInput")
    def ssl_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslrootcertInput")
    def sslrootcert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslrootcertInput"))

    @builtins.property
    @jsii.member(jsii_name="superuserInput")
    def superuser_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "superuserInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamAuth")
    def aws_rds_iam_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "awsRdsIamAuth"))

    @aws_rds_iam_auth.setter
    def aws_rds_iam_auth(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "aws_rds_iam_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRdsIamAuth", value)

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamProfile")
    def aws_rds_iam_profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamProfile"))

    @aws_rds_iam_profile.setter
    def aws_rds_iam_profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "aws_rds_iam_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRdsIamProfile", value)

    @builtins.property
    @jsii.member(jsii_name="clientcert")
    def clientcert(self) -> typing.Optional["PostgresqlProviderClientcert"]:
        return typing.cast(typing.Optional["PostgresqlProviderClientcert"], jsii.get(self, "clientcert"))

    @clientcert.setter
    def clientcert(
        self,
        value: typing.Optional["PostgresqlProviderClientcert"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "clientcert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientcert", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "database"))

    @database.setter
    def database(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="databaseUsername")
    def database_username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUsername"))

    @database_username.setter
    def database_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "database_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseUsername", value)

    @builtins.property
    @jsii.member(jsii_name="expectedVersion")
    def expected_version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedVersion"))

    @expected_version.setter
    def expected_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "expected_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedVersion", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "max_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="sslmode")
    def sslmode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslmode"))

    @sslmode.setter
    def sslmode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "sslmode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslmode", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "ssl_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="sslrootcert")
    def sslrootcert(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslrootcert"))

    @sslrootcert.setter
    def sslrootcert(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "sslrootcert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslrootcert", value)

    @builtins.property
    @jsii.member(jsii_name="superuser")
    def superuser(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "superuser"))

    @superuser.setter
    def superuser(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "superuser").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "superuser", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlProvider, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-postgresql.provider.PostgresqlProviderClientcert",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "key": "key"},
)
class PostgresqlProviderClientcert:
    def __init__(self, *, cert: builtins.str, key: builtins.str) -> None:
        '''
        :param cert: The SSL client certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#cert PostgresqlProvider#cert}
        :param key: The SSL client certificate private key file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#key PostgresqlProvider#key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlProviderClientcert.__init__)
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "cert": cert,
            "key": key,
        }

    @builtins.property
    def cert(self) -> builtins.str:
        '''The SSL client certificate file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#cert PostgresqlProvider#cert}
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''The SSL client certificate private key file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#key PostgresqlProvider#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlProviderClientcert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-postgresql.provider.PostgresqlProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "aws_rds_iam_auth": "awsRdsIamAuth",
        "aws_rds_iam_profile": "awsRdsIamProfile",
        "clientcert": "clientcert",
        "connect_timeout": "connectTimeout",
        "database": "database",
        "database_username": "databaseUsername",
        "expected_version": "expectedVersion",
        "host": "host",
        "max_connections": "maxConnections",
        "password": "password",
        "port": "port",
        "scheme": "scheme",
        "sslmode": "sslmode",
        "ssl_mode": "sslMode",
        "sslrootcert": "sslrootcert",
        "superuser": "superuser",
        "username": "username",
    },
)
class PostgresqlProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_rds_iam_profile: typing.Optional[builtins.str] = None,
        clientcert: typing.Optional[typing.Union[PostgresqlProviderClientcert, typing.Dict[str, typing.Any]]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        database: typing.Optional[builtins.str] = None,
        database_username: typing.Optional[builtins.str] = None,
        expected_version: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
        sslmode: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sslrootcert: typing.Optional[builtins.str] = None,
        superuser: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#alias PostgresqlProvider#alias}
        :param aws_rds_iam_auth: Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        :param aws_rds_iam_profile: AWS profile to use for IAM auth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        :param clientcert: clientcert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#clientcert PostgresqlProvider#clientcert}
        :param connect_timeout: Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#connect_timeout PostgresqlProvider#connect_timeout}
        :param database: The name of the database to connect to in order to conenct to (defaults to ``postgres``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database PostgresqlProvider#database}
        :param database_username: Database username associated to the connected user (for user name maps). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database_username PostgresqlProvider#database_username}
        :param expected_version: Specify the expected version of PostgreSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#expected_version PostgresqlProvider#expected_version}
        :param host: Name of PostgreSQL server address to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#host PostgresqlProvider#host}
        :param max_connections: Maximum number of connections to establish to the database. Zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#max_connections PostgresqlProvider#max_connections}
        :param password: Password to be used if the PostgreSQL server demands password authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#password PostgresqlProvider#password}
        :param port: The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#port PostgresqlProvider#port}
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#scheme PostgresqlProvider#scheme}.
        :param sslmode: This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslmode PostgresqlProvider#sslmode}
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#ssl_mode PostgresqlProvider#ssl_mode}.
        :param sslrootcert: The SSL server root certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslrootcert PostgresqlProvider#sslrootcert}
        :param superuser: Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#superuser PostgresqlProvider#superuser}
        :param username: PostgreSQL user name to connect as. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#username PostgresqlProvider#username}
        '''
        if isinstance(clientcert, dict):
            clientcert = PostgresqlProviderClientcert(**clientcert)
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlProviderConfig.__init__)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument aws_rds_iam_auth", value=aws_rds_iam_auth, expected_type=type_hints["aws_rds_iam_auth"])
            check_type(argname="argument aws_rds_iam_profile", value=aws_rds_iam_profile, expected_type=type_hints["aws_rds_iam_profile"])
            check_type(argname="argument clientcert", value=clientcert, expected_type=type_hints["clientcert"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument database_username", value=database_username, expected_type=type_hints["database_username"])
            check_type(argname="argument expected_version", value=expected_version, expected_type=type_hints["expected_version"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument sslmode", value=sslmode, expected_type=type_hints["sslmode"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument sslrootcert", value=sslrootcert, expected_type=type_hints["sslrootcert"])
            check_type(argname="argument superuser", value=superuser, expected_type=type_hints["superuser"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if aws_rds_iam_auth is not None:
            self._values["aws_rds_iam_auth"] = aws_rds_iam_auth
        if aws_rds_iam_profile is not None:
            self._values["aws_rds_iam_profile"] = aws_rds_iam_profile
        if clientcert is not None:
            self._values["clientcert"] = clientcert
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if database is not None:
            self._values["database"] = database
        if database_username is not None:
            self._values["database_username"] = database_username
        if expected_version is not None:
            self._values["expected_version"] = expected_version
        if host is not None:
            self._values["host"] = host
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme
        if sslmode is not None:
            self._values["sslmode"] = sslmode
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if sslrootcert is not None:
            self._values["sslrootcert"] = sslrootcert
        if superuser is not None:
            self._values["superuser"] = superuser
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#alias PostgresqlProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_rds_iam_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        '''
        result = self._values.get("aws_rds_iam_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_rds_iam_profile(self) -> typing.Optional[builtins.str]:
        '''AWS profile to use for IAM auth.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        '''
        result = self._values.get("aws_rds_iam_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def clientcert(self) -> typing.Optional[PostgresqlProviderClientcert]:
        '''clientcert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#clientcert PostgresqlProvider#clientcert}
        '''
        result = self._values.get("clientcert")
        return typing.cast(typing.Optional[PostgresqlProviderClientcert], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#connect_timeout PostgresqlProvider#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''The name of the database to connect to in order to conenct to (defaults to ``postgres``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database PostgresqlProvider#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_username(self) -> typing.Optional[builtins.str]:
        '''Database username associated to the connected user (for user name maps).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#database_username PostgresqlProvider#database_username}
        '''
        result = self._values.get("database_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expected_version(self) -> typing.Optional[builtins.str]:
        '''Specify the expected version of PostgreSQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#expected_version PostgresqlProvider#expected_version}
        '''
        result = self._values.get("expected_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Name of PostgreSQL server address to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#host PostgresqlProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of connections to establish to the database. Zero means unlimited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#max_connections PostgresqlProvider#max_connections}
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password to be used if the PostgreSQL server demands password authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#password PostgresqlProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#port PostgresqlProvider#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#scheme PostgresqlProvider#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sslmode(self) -> typing.Optional[builtins.str]:
        '''This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslmode PostgresqlProvider#sslmode}
        '''
        result = self._values.get("sslmode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#ssl_mode PostgresqlProvider#ssl_mode}.'''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sslrootcert(self) -> typing.Optional[builtins.str]:
        '''The SSL server root certificate file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#sslrootcert PostgresqlProvider#sslrootcert}
        '''
        result = self._values.get("sslrootcert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def superuser(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#superuser PostgresqlProvider#superuser}
        '''
        result = self._values.get("superuser")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''PostgreSQL user name to connect as.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql#username PostgresqlProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PostgresqlProvider",
    "PostgresqlProviderClientcert",
    "PostgresqlProviderConfig",
]

publication.publish()
