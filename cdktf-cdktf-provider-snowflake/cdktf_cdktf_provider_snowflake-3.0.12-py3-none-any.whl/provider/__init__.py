'''
# `provider`

Refer to the Terraform Registory for docs: [`snowflake`](https://www.terraform.io/docs/providers/snowflake).
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


class SnowflakeProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.provider.SnowflakeProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake snowflake}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: builtins.str,
        username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        browser_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[builtins.str] = None,
        oauth_access_token: typing.Optional[builtins.str] = None,
        oauth_client_id: typing.Optional[builtins.str] = None,
        oauth_client_secret: typing.Optional[builtins.str] = None,
        oauth_endpoint: typing.Optional[builtins.str] = None,
        oauth_redirect_url: typing.Optional[builtins.str] = None,
        oauth_refresh_token: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        private_key: typing.Optional[builtins.str] = None,
        private_key_passphrase: typing.Optional[builtins.str] = None,
        private_key_path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        warehouse: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake snowflake} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account: The name of the Snowflake account. Can also come from the ``SNOWFLAKE_ACCOUNT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#account SnowflakeProvider#account}
        :param username: Username for username+password authentication. Can come from the ``SNOWFLAKE_USER`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#username SnowflakeProvider#username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#alias SnowflakeProvider#alias}
        :param browser_auth: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#browser_auth SnowflakeProvider#browser_auth}
        :param host: Supports passing in a custom host value to the snowflake go driver for use with privatelink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#host SnowflakeProvider#host}
        :param oauth_access_token: Token for use with OAuth. Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_access_token SnowflakeProvider#oauth_access_token}
        :param oauth_client_id: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_id SnowflakeProvider#oauth_client_id}
        :param oauth_client_secret: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        :param oauth_endpoint: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        :param oauth_redirect_url: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        :param oauth_refresh_token: Token for use with OAuth. Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        :param password: Password for username+password auth. Cannot be used with ``browser_auth`` or ``private_key_path``. Can be source from ``SNOWFLAKE_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#password SnowflakeProvider#password}
        :param port: Support custom port values to snowflake go driver for use with privatelink. Can be sourced from ``SNOWFLAKE_PORT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#port SnowflakeProvider#port}
        :param private_key: Private Key for username+private-key auth. Cannot be used with ``browser_auth`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key SnowflakeProvider#private_key}
        :param private_key_passphrase: Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        :param private_key_path: Path to a private key for using keypair authentication. Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_path SnowflakeProvider#private_key_path}
        :param protocol: Support custom protocols to snowflake go driver. Can be sourced from ``SNOWFLAKE_PROTOCOL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#protocol SnowflakeProvider#protocol}
        :param region: `Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use. Can be source from the ``SNOWFLAKE_REGION`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#region SnowflakeProvider#region}
        :param role: Snowflake role to use for operations. If left unset, default role for user will be used. Can come from the ``SNOWFLAKE_ROLE`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#role SnowflakeProvider#role}
        :param warehouse: Sets the default warehouse. Optional. Can be sourced from SNOWFLAKE_WAREHOUSE environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#warehouse SnowflakeProvider#warehouse}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SnowflakeProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SnowflakeProviderConfig(
            account=account,
            username=username,
            alias=alias,
            browser_auth=browser_auth,
            host=host,
            oauth_access_token=oauth_access_token,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
            oauth_endpoint=oauth_endpoint,
            oauth_redirect_url=oauth_redirect_url,
            oauth_refresh_token=oauth_refresh_token,
            password=password,
            port=port,
            private_key=private_key,
            private_key_passphrase=private_key_passphrase,
            private_key_path=private_key_path,
            protocol=protocol,
            region=region,
            role=role,
            warehouse=warehouse,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetBrowserAuth")
    def reset_browser_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserAuth", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetOauthAccessToken")
    def reset_oauth_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthAccessToken", []))

    @jsii.member(jsii_name="resetOauthClientId")
    def reset_oauth_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthClientId", []))

    @jsii.member(jsii_name="resetOauthClientSecret")
    def reset_oauth_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthClientSecret", []))

    @jsii.member(jsii_name="resetOauthEndpoint")
    def reset_oauth_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthEndpoint", []))

    @jsii.member(jsii_name="resetOauthRedirectUrl")
    def reset_oauth_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRedirectUrl", []))

    @jsii.member(jsii_name="resetOauthRefreshToken")
    def reset_oauth_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRefreshToken", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPrivateKey")
    def reset_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKey", []))

    @jsii.member(jsii_name="resetPrivateKeyPassphrase")
    def reset_private_key_passphrase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyPassphrase", []))

    @jsii.member(jsii_name="resetPrivateKeyPath")
    def reset_private_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyPath", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetWarehouse")
    def reset_warehouse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouse", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="browserAuthInput")
    def browser_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "browserAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthAccessTokenInput")
    def oauth_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthClientIdInput")
    def oauth_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthClientSecretInput")
    def oauth_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthEndpointInput")
    def oauth_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRedirectUrlInput")
    def oauth_redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRedirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshTokenInput")
    def oauth_refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRefreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPassphraseInput")
    def private_key_passphrase_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPassphraseInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPathInput")
    def private_key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @account.setter
    def account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="browserAuth")
    def browser_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "browserAuth"))

    @browser_auth.setter
    def browser_auth(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "browser_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserAuth", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="oauthAccessToken")
    def oauth_access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthAccessToken"))

    @oauth_access_token.setter
    def oauth_access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="oauthClientId")
    def oauth_client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientId"))

    @oauth_client_id.setter
    def oauth_client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthClientId", value)

    @builtins.property
    @jsii.member(jsii_name="oauthClientSecret")
    def oauth_client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientSecret"))

    @oauth_client_secret.setter
    def oauth_client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="oauthEndpoint")
    def oauth_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthEndpoint"))

    @oauth_endpoint.setter
    def oauth_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="oauthRedirectUrl")
    def oauth_redirect_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRedirectUrl"))

    @oauth_redirect_url.setter
    def oauth_redirect_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_redirect_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthRedirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshToken")
    def oauth_refresh_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthRefreshToken"))

    @oauth_refresh_token.setter
    def oauth_refresh_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "oauth_refresh_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthRefreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPassphrase")
    def private_key_passphrase(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPassphrase"))

    @private_key_passphrase.setter
    def private_key_passphrase(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "private_key_passphrase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPassphrase", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPath")
    def private_key_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPath"))

    @private_key_path.setter
    def private_key_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "private_key_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "role"))

    @role.setter
    def role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SnowflakeProvider, "warehouse").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.provider.SnowflakeProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "username": "username",
        "alias": "alias",
        "browser_auth": "browserAuth",
        "host": "host",
        "oauth_access_token": "oauthAccessToken",
        "oauth_client_id": "oauthClientId",
        "oauth_client_secret": "oauthClientSecret",
        "oauth_endpoint": "oauthEndpoint",
        "oauth_redirect_url": "oauthRedirectUrl",
        "oauth_refresh_token": "oauthRefreshToken",
        "password": "password",
        "port": "port",
        "private_key": "privateKey",
        "private_key_passphrase": "privateKeyPassphrase",
        "private_key_path": "privateKeyPath",
        "protocol": "protocol",
        "region": "region",
        "role": "role",
        "warehouse": "warehouse",
    },
)
class SnowflakeProviderConfig:
    def __init__(
        self,
        *,
        account: builtins.str,
        username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        browser_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[builtins.str] = None,
        oauth_access_token: typing.Optional[builtins.str] = None,
        oauth_client_id: typing.Optional[builtins.str] = None,
        oauth_client_secret: typing.Optional[builtins.str] = None,
        oauth_endpoint: typing.Optional[builtins.str] = None,
        oauth_redirect_url: typing.Optional[builtins.str] = None,
        oauth_refresh_token: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        private_key: typing.Optional[builtins.str] = None,
        private_key_passphrase: typing.Optional[builtins.str] = None,
        private_key_path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        warehouse: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: The name of the Snowflake account. Can also come from the ``SNOWFLAKE_ACCOUNT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#account SnowflakeProvider#account}
        :param username: Username for username+password authentication. Can come from the ``SNOWFLAKE_USER`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#username SnowflakeProvider#username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#alias SnowflakeProvider#alias}
        :param browser_auth: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#browser_auth SnowflakeProvider#browser_auth}
        :param host: Supports passing in a custom host value to the snowflake go driver for use with privatelink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#host SnowflakeProvider#host}
        :param oauth_access_token: Token for use with OAuth. Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_access_token SnowflakeProvider#oauth_access_token}
        :param oauth_client_id: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_id SnowflakeProvider#oauth_client_id}
        :param oauth_client_secret: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        :param oauth_endpoint: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        :param oauth_redirect_url: Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        :param oauth_refresh_token: Token for use with OAuth. Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        :param password: Password for username+password auth. Cannot be used with ``browser_auth`` or ``private_key_path``. Can be source from ``SNOWFLAKE_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#password SnowflakeProvider#password}
        :param port: Support custom port values to snowflake go driver for use with privatelink. Can be sourced from ``SNOWFLAKE_PORT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#port SnowflakeProvider#port}
        :param private_key: Private Key for username+private-key auth. Cannot be used with ``browser_auth`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key SnowflakeProvider#private_key}
        :param private_key_passphrase: Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        :param private_key_path: Path to a private key for using keypair authentication. Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_path SnowflakeProvider#private_key_path}
        :param protocol: Support custom protocols to snowflake go driver. Can be sourced from ``SNOWFLAKE_PROTOCOL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#protocol SnowflakeProvider#protocol}
        :param region: `Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use. Can be source from the ``SNOWFLAKE_REGION`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#region SnowflakeProvider#region}
        :param role: Snowflake role to use for operations. If left unset, default role for user will be used. Can come from the ``SNOWFLAKE_ROLE`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#role SnowflakeProvider#role}
        :param warehouse: Sets the default warehouse. Optional. Can be sourced from SNOWFLAKE_WAREHOUSE environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#warehouse SnowflakeProvider#warehouse}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SnowflakeProviderConfig.__init__)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument browser_auth", value=browser_auth, expected_type=type_hints["browser_auth"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument oauth_access_token", value=oauth_access_token, expected_type=type_hints["oauth_access_token"])
            check_type(argname="argument oauth_client_id", value=oauth_client_id, expected_type=type_hints["oauth_client_id"])
            check_type(argname="argument oauth_client_secret", value=oauth_client_secret, expected_type=type_hints["oauth_client_secret"])
            check_type(argname="argument oauth_endpoint", value=oauth_endpoint, expected_type=type_hints["oauth_endpoint"])
            check_type(argname="argument oauth_redirect_url", value=oauth_redirect_url, expected_type=type_hints["oauth_redirect_url"])
            check_type(argname="argument oauth_refresh_token", value=oauth_refresh_token, expected_type=type_hints["oauth_refresh_token"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument private_key_passphrase", value=private_key_passphrase, expected_type=type_hints["private_key_passphrase"])
            check_type(argname="argument private_key_path", value=private_key_path, expected_type=type_hints["private_key_path"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "username": username,
        }
        if alias is not None:
            self._values["alias"] = alias
        if browser_auth is not None:
            self._values["browser_auth"] = browser_auth
        if host is not None:
            self._values["host"] = host
        if oauth_access_token is not None:
            self._values["oauth_access_token"] = oauth_access_token
        if oauth_client_id is not None:
            self._values["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not None:
            self._values["oauth_client_secret"] = oauth_client_secret
        if oauth_endpoint is not None:
            self._values["oauth_endpoint"] = oauth_endpoint
        if oauth_redirect_url is not None:
            self._values["oauth_redirect_url"] = oauth_redirect_url
        if oauth_refresh_token is not None:
            self._values["oauth_refresh_token"] = oauth_refresh_token
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if private_key is not None:
            self._values["private_key"] = private_key
        if private_key_passphrase is not None:
            self._values["private_key_passphrase"] = private_key_passphrase
        if private_key_path is not None:
            self._values["private_key_path"] = private_key_path
        if protocol is not None:
            self._values["protocol"] = protocol
        if region is not None:
            self._values["region"] = region
        if role is not None:
            self._values["role"] = role
        if warehouse is not None:
            self._values["warehouse"] = warehouse

    @builtins.property
    def account(self) -> builtins.str:
        '''The name of the Snowflake account. Can also come from the ``SNOWFLAKE_ACCOUNT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#account SnowflakeProvider#account}
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Username for username+password authentication. Can come from the ``SNOWFLAKE_USER`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#username SnowflakeProvider#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#alias SnowflakeProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_USE_BROWSER_AUTH`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#browser_auth SnowflakeProvider#browser_auth}
        '''
        result = self._values.get("browser_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Supports passing in a custom host value to the snowflake go driver for use with privatelink.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#host SnowflakeProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_access_token(self) -> typing.Optional[builtins.str]:
        '''Token for use with OAuth.

        Generating the token is left to other tools. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_refresh_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_ACCESS_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_access_token SnowflakeProvider#oauth_access_token}
        '''
        result = self._values.get("oauth_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_client_id(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_ID`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_id SnowflakeProvider#oauth_client_id}
        '''
        result = self._values.get("oauth_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_client_secret(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_CLIENT_SECRET`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_client_secret SnowflakeProvider#oauth_client_secret}
        '''
        result = self._values.get("oauth_client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_endpoint(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_ENDPOINT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_endpoint SnowflakeProvider#oauth_endpoint}
        '''
        result = self._values.get("oauth_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_redirect_url(self) -> typing.Optional[builtins.str]:
        '''Required when ``oauth_refresh_token`` is used. Can be sourced from ``SNOWFLAKE_OAUTH_REDIRECT_URL`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_redirect_url SnowflakeProvider#oauth_redirect_url}
        '''
        result = self._values.get("oauth_redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_refresh_token(self) -> typing.Optional[builtins.str]:
        '''Token for use with OAuth.

        Setup and generation of the token is left to other tools. Should be used in conjunction with ``oauth_client_id``, ``oauth_client_secret``, ``oauth_endpoint``, ``oauth_redirect_url``. Cannot be used with ``browser_auth``, ``private_key_path``, ``oauth_access_token`` or ``password``. Can be sourced from ``SNOWFLAKE_OAUTH_REFRESH_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#oauth_refresh_token SnowflakeProvider#oauth_refresh_token}
        '''
        result = self._values.get("oauth_refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for username+password auth. Cannot be used with ``browser_auth`` or ``private_key_path``. Can be source from ``SNOWFLAKE_PASSWORD`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#password SnowflakeProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Support custom port values to snowflake go driver for use with privatelink. Can be sourced from ``SNOWFLAKE_PORT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#port SnowflakeProvider#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''Private Key for username+private-key auth. Cannot be used with ``browser_auth`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key SnowflakeProvider#private_key}
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_passphrase(self) -> typing.Optional[builtins.str]:
        '''Supports the encryption ciphers aes-128-cbc, aes-128-gcm, aes-192-cbc, aes-192-gcm, aes-256-cbc, aes-256-gcm, and des-ede3-cbc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_passphrase SnowflakeProvider#private_key_passphrase}
        '''
        result = self._values.get("private_key_passphrase")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_path(self) -> typing.Optional[builtins.str]:
        '''Path to a private key for using keypair authentication.

        Cannot be used with ``browser_auth``, ``oauth_access_token`` or ``password``. Can be source from ``SNOWFLAKE_PRIVATE_KEY_PATH`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#private_key_path SnowflakeProvider#private_key_path}
        '''
        result = self._values.get("private_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Support custom protocols to snowflake go driver. Can be sourced from ``SNOWFLAKE_PROTOCOL`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#protocol SnowflakeProvider#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''`Snowflake region <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_ to use. Can be source from the ``SNOWFLAKE_REGION`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#region SnowflakeProvider#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Snowflake role to use for operations.

        If left unset, default role for user will be used. Can come from the ``SNOWFLAKE_ROLE`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#role SnowflakeProvider#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warehouse(self) -> typing.Optional[builtins.str]:
        '''Sets the default warehouse. Optional. Can be sourced from SNOWFLAKE_WAREHOUSE environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake#warehouse SnowflakeProvider#warehouse}
        '''
        result = self._values.get("warehouse")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnowflakeProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnowflakeProvider",
    "SnowflakeProviderConfig",
]

publication.publish()
