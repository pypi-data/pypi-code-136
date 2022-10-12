'''
# `provider`

Refer to the Terraform Registory for docs: [`databricks`](https://www.terraform.io/docs/providers/databricks).
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


class DatabricksProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.provider.DatabricksProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks databricks}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_id: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_login_app_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_workspace_resource_id: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        config_file: typing.Optional[builtins.str] = None,
        debug_headers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        debug_truncate_bytes: typing.Optional[jsii.Number] = None,
        google_credentials: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        http_timeout_seconds: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        token_endpoint: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks databricks} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.
        :param azure_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.
        :param azure_client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.
        :param azure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.
        :param azure_login_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.
        :param azure_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.
        :param azure_use_msi: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.
        :param azure_workspace_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.
        :param config_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.
        :param debug_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.
        :param debug_truncate_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.
        :param google_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.
        :param http_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.
        :param rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.
        :param skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token_endpoint DatabricksProvider#token_endpoint}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DatabricksProviderConfig(
            account_id=account_id,
            alias=alias,
            auth_type=auth_type,
            azure_client_id=azure_client_id,
            azure_client_secret=azure_client_secret,
            azure_environment=azure_environment,
            azure_login_app_id=azure_login_app_id,
            azure_tenant_id=azure_tenant_id,
            azure_use_msi=azure_use_msi,
            azure_workspace_resource_id=azure_workspace_resource_id,
            client_id=client_id,
            client_secret=client_secret,
            config_file=config_file,
            debug_headers=debug_headers,
            debug_truncate_bytes=debug_truncate_bytes,
            google_credentials=google_credentials,
            google_service_account=google_service_account,
            host=host,
            http_timeout_seconds=http_timeout_seconds,
            password=password,
            profile=profile,
            rate_limit=rate_limit,
            skip_verify=skip_verify,
            token=token,
            token_endpoint=token_endpoint,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetAzureClientId")
    def reset_azure_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientId", []))

    @jsii.member(jsii_name="resetAzureClientSecret")
    def reset_azure_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientSecret", []))

    @jsii.member(jsii_name="resetAzureEnvironment")
    def reset_azure_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureEnvironment", []))

    @jsii.member(jsii_name="resetAzureLoginAppId")
    def reset_azure_login_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureLoginAppId", []))

    @jsii.member(jsii_name="resetAzureTenantId")
    def reset_azure_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureTenantId", []))

    @jsii.member(jsii_name="resetAzureUseMsi")
    def reset_azure_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureUseMsi", []))

    @jsii.member(jsii_name="resetAzureWorkspaceResourceId")
    def reset_azure_workspace_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureWorkspaceResourceId", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetConfigFile")
    def reset_config_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigFile", []))

    @jsii.member(jsii_name="resetDebugHeaders")
    def reset_debug_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDebugHeaders", []))

    @jsii.member(jsii_name="resetDebugTruncateBytes")
    def reset_debug_truncate_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDebugTruncateBytes", []))

    @jsii.member(jsii_name="resetGoogleCredentials")
    def reset_google_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleCredentials", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHttpTimeoutSeconds")
    def reset_http_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTimeoutSeconds", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetRateLimit")
    def reset_rate_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimit", []))

    @jsii.member(jsii_name="resetSkipVerify")
    def reset_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipVerify", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetTokenEndpoint")
    def reset_token_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenEndpoint", []))

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
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientIdInput")
    def azure_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientSecretInput")
    def azure_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="azureEnvironmentInput")
    def azure_environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="azureLoginAppIdInput")
    def azure_login_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureLoginAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureTenantIdInput")
    def azure_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureUseMsiInput")
    def azure_use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azureUseMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="azureWorkspaceResourceIdInput")
    def azure_workspace_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureWorkspaceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="configFileInput")
    def config_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configFileInput"))

    @builtins.property
    @jsii.member(jsii_name="debugHeadersInput")
    def debug_headers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "debugHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="debugTruncateBytesInput")
    def debug_truncate_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "debugTruncateBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="googleCredentialsInput")
    def google_credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTimeoutSecondsInput")
    def http_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitInput")
    def rate_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="skipVerifyInput")
    def skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenEndpointInput")
    def token_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "auth_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientId")
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientId"))

    @azure_client_id.setter
    def azure_client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientId", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientSecret")
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecret"))

    @azure_client_secret.setter
    def azure_client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="azureEnvironment")
    def azure_environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironment"))

    @azure_environment.setter
    def azure_environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="azureLoginAppId")
    def azure_login_app_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureLoginAppId"))

    @azure_login_app_id.setter
    def azure_login_app_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_login_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureLoginAppId", value)

    @builtins.property
    @jsii.member(jsii_name="azureTenantId")
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantId"))

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="azureUseMsi")
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azureUseMsi"))

    @azure_use_msi.setter
    def azure_use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_use_msi").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureUseMsi", value)

    @builtins.property
    @jsii.member(jsii_name="azureWorkspaceResourceId")
    def azure_workspace_resource_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureWorkspaceResourceId"))

    @azure_workspace_resource_id.setter
    def azure_workspace_resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "azure_workspace_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureWorkspaceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="configFile")
    def config_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configFile"))

    @config_file.setter
    def config_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "config_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configFile", value)

    @builtins.property
    @jsii.member(jsii_name="debugHeaders")
    def debug_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "debugHeaders"))

    @debug_headers.setter
    def debug_headers(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "debug_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "debugHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="debugTruncateBytes")
    def debug_truncate_bytes(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "debugTruncateBytes"))

    @debug_truncate_bytes.setter
    def debug_truncate_bytes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "debug_truncate_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "debugTruncateBytes", value)

    @builtins.property
    @jsii.member(jsii_name="googleCredentials")
    def google_credentials(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleCredentials"))

    @google_credentials.setter
    def google_credentials(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "google_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "google_service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="httpTimeoutSeconds")
    def http_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpTimeoutSeconds"))

    @http_timeout_seconds.setter
    def http_timeout_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "http_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimit")
    def rate_limit(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimit"))

    @rate_limit.setter
    def rate_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "rate_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimit", value)

    @builtins.property
    @jsii.member(jsii_name="skipVerify")
    def skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipVerify"))

    @skip_verify.setter
    def skip_verify(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "skip_verify").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="tokenEndpoint")
    def token_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenEndpoint"))

    @token_endpoint.setter
    def token_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "token_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksProvider, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.provider.DatabricksProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "alias": "alias",
        "auth_type": "authType",
        "azure_client_id": "azureClientId",
        "azure_client_secret": "azureClientSecret",
        "azure_environment": "azureEnvironment",
        "azure_login_app_id": "azureLoginAppId",
        "azure_tenant_id": "azureTenantId",
        "azure_use_msi": "azureUseMsi",
        "azure_workspace_resource_id": "azureWorkspaceResourceId",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "config_file": "configFile",
        "debug_headers": "debugHeaders",
        "debug_truncate_bytes": "debugTruncateBytes",
        "google_credentials": "googleCredentials",
        "google_service_account": "googleServiceAccount",
        "host": "host",
        "http_timeout_seconds": "httpTimeoutSeconds",
        "password": "password",
        "profile": "profile",
        "rate_limit": "rateLimit",
        "skip_verify": "skipVerify",
        "token": "token",
        "token_endpoint": "tokenEndpoint",
        "username": "username",
    },
)
class DatabricksProviderConfig:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_login_app_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_workspace_resource_id: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        config_file: typing.Optional[builtins.str] = None,
        debug_headers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        debug_truncate_bytes: typing.Optional[jsii.Number] = None,
        google_credentials: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        http_timeout_seconds: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        token_endpoint: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.
        :param azure_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.
        :param azure_client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.
        :param azure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.
        :param azure_login_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.
        :param azure_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.
        :param azure_use_msi: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.
        :param azure_workspace_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.
        :param config_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.
        :param debug_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.
        :param debug_truncate_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.
        :param google_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.
        :param http_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.
        :param rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.
        :param skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token_endpoint DatabricksProvider#token_endpoint}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksProviderConfig.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument azure_client_id", value=azure_client_id, expected_type=type_hints["azure_client_id"])
            check_type(argname="argument azure_client_secret", value=azure_client_secret, expected_type=type_hints["azure_client_secret"])
            check_type(argname="argument azure_environment", value=azure_environment, expected_type=type_hints["azure_environment"])
            check_type(argname="argument azure_login_app_id", value=azure_login_app_id, expected_type=type_hints["azure_login_app_id"])
            check_type(argname="argument azure_tenant_id", value=azure_tenant_id, expected_type=type_hints["azure_tenant_id"])
            check_type(argname="argument azure_use_msi", value=azure_use_msi, expected_type=type_hints["azure_use_msi"])
            check_type(argname="argument azure_workspace_resource_id", value=azure_workspace_resource_id, expected_type=type_hints["azure_workspace_resource_id"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument config_file", value=config_file, expected_type=type_hints["config_file"])
            check_type(argname="argument debug_headers", value=debug_headers, expected_type=type_hints["debug_headers"])
            check_type(argname="argument debug_truncate_bytes", value=debug_truncate_bytes, expected_type=type_hints["debug_truncate_bytes"])
            check_type(argname="argument google_credentials", value=google_credentials, expected_type=type_hints["google_credentials"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument http_timeout_seconds", value=http_timeout_seconds, expected_type=type_hints["http_timeout_seconds"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument rate_limit", value=rate_limit, expected_type=type_hints["rate_limit"])
            check_type(argname="argument skip_verify", value=skip_verify, expected_type=type_hints["skip_verify"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument token_endpoint", value=token_endpoint, expected_type=type_hints["token_endpoint"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if alias is not None:
            self._values["alias"] = alias
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if azure_client_id is not None:
            self._values["azure_client_id"] = azure_client_id
        if azure_client_secret is not None:
            self._values["azure_client_secret"] = azure_client_secret
        if azure_environment is not None:
            self._values["azure_environment"] = azure_environment
        if azure_login_app_id is not None:
            self._values["azure_login_app_id"] = azure_login_app_id
        if azure_tenant_id is not None:
            self._values["azure_tenant_id"] = azure_tenant_id
        if azure_use_msi is not None:
            self._values["azure_use_msi"] = azure_use_msi
        if azure_workspace_resource_id is not None:
            self._values["azure_workspace_resource_id"] = azure_workspace_resource_id
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if config_file is not None:
            self._values["config_file"] = config_file
        if debug_headers is not None:
            self._values["debug_headers"] = debug_headers
        if debug_truncate_bytes is not None:
            self._values["debug_truncate_bytes"] = debug_truncate_bytes
        if google_credentials is not None:
            self._values["google_credentials"] = google_credentials
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if host is not None:
            self._values["host"] = host
        if http_timeout_seconds is not None:
            self._values["http_timeout_seconds"] = http_timeout_seconds
        if password is not None:
            self._values["password"] = password
        if profile is not None:
            self._values["profile"] = profile
        if rate_limit is not None:
            self._values["rate_limit"] = rate_limit
        if skip_verify is not None:
            self._values["skip_verify"] = skip_verify
        if token is not None:
            self._values["token"] = token
        if token_endpoint is not None:
            self._values["token_endpoint"] = token_endpoint
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.'''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.'''
        result = self._values.get("azure_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.'''
        result = self._values.get("azure_client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_environment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.'''
        result = self._values.get("azure_environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_login_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.'''
        result = self._values.get("azure_login_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.'''
        result = self._values.get("azure_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.'''
        result = self._values.get("azure_use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def azure_workspace_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.'''
        result = self._values.get("azure_workspace_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.'''
        result = self._values.get("config_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def debug_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.'''
        result = self._values.get("debug_headers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def debug_truncate_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.'''
        result = self._values.get("debug_truncate_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.'''
        result = self._values.get("google_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.'''
        result = self._values.get("http_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rate_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.'''
        result = self._values.get("rate_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.'''
        result = self._values.get("skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token_endpoint DatabricksProvider#token_endpoint}.'''
        result = self._values.get("token_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabricksProvider",
    "DatabricksProviderConfig",
]

publication.publish()
