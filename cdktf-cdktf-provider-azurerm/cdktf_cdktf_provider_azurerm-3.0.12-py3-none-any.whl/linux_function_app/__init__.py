'''
# `azurerm_linux_function_app`

Refer to the Terraform Registory for docs: [`azurerm_linux_function_app`](https://www.terraform.io/docs/providers/azurerm/r/linux_function_app).
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


class LinuxFunctionApp(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionApp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app azurerm_linux_function_app}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        service_plan_id: builtins.str,
        site_config: typing.Union["LinuxFunctionAppSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union["LinuxFunctionAppAuthSettings", typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union["LinuxFunctionAppBackup", typing.Dict[str, typing.Any]]] = None,
        builtin_logging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        content_share_force_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_memory_time_quota: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        functions_extension_version: typing.Optional[builtins.str] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LinuxFunctionAppIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        sticky_settings: typing.Optional[typing.Union["LinuxFunctionAppStickySettings", typing.Dict[str, typing.Any]]] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        storage_key_vault_secret_id: typing.Optional[builtins.str] = None,
        storage_uses_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxFunctionAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app azurerm_linux_function_app} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#location LinuxFunctionApp#location}.
        :param name: Specifies the name of the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#resource_group_name LinuxFunctionApp#resource_group_name}.
        :param service_plan_id: The ID of the App Service Plan within which to create this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_plan_id LinuxFunctionApp#service_plan_id}
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#site_config LinuxFunctionApp#site_config}
        :param app_settings: A map of key-value pairs for `App Settings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings>`_ and custom values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_settings LinuxFunctionApp#app_settings}
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#auth_settings LinuxFunctionApp#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#backup LinuxFunctionApp#backup}
        :param builtin_logging_enabled: Should built in logging be enabled. Configures ``AzureWebJobsDashboard`` app setting based on the configured storage setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#builtin_logging_enabled LinuxFunctionApp#builtin_logging_enabled}
        :param client_certificate_enabled: Should the function app use Client Certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_enabled LinuxFunctionApp#client_certificate_enabled}
        :param client_certificate_mode: The mode of the Function App's client certificates requirement for incoming requests. Possible values are ``Required``, ``Optional``, and ``OptionalInteractiveUser`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_mode LinuxFunctionApp#client_certificate_mode}
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string LinuxFunctionApp#connection_string}
        :param content_share_force_disabled: Force disable the content share settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#content_share_force_disabled LinuxFunctionApp#content_share_force_disabled}
        :param daily_memory_time_quota: The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps in Consumption Plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#daily_memory_time_quota LinuxFunctionApp#daily_memory_time_quota}
        :param enabled: Is the Linux Function App enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        :param functions_extension_version: The runtime version associated with the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#functions_extension_version LinuxFunctionApp#functions_extension_version}
        :param https_only: Can the Function App only be accessed via HTTPS? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#https_only LinuxFunctionApp#https_only}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#id LinuxFunctionApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity LinuxFunctionApp#identity}
        :param key_vault_reference_identity_id: The User Assigned Identity to use for Key Vault access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#key_vault_reference_identity_id LinuxFunctionApp#key_vault_reference_identity_id}
        :param sticky_settings: sticky_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#sticky_settings LinuxFunctionApp#sticky_settings}
        :param storage_account_access_key: The access key which will be used to access the storage account for the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_access_key LinuxFunctionApp#storage_account_access_key}
        :param storage_account_name: The backend storage account name which will be used by this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_name LinuxFunctionApp#storage_account_name}
        :param storage_key_vault_secret_id: The Key Vault Secret ID, including version, that contains the Connection String to connect to the storage account for this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_key_vault_secret_id LinuxFunctionApp#storage_key_vault_secret_id}
        :param storage_uses_managed_identity: Should the Function App use its Managed Identity to access storage? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_uses_managed_identity LinuxFunctionApp#storage_uses_managed_identity}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#tags LinuxFunctionApp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#timeouts LinuxFunctionApp#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionApp.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LinuxFunctionAppConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            service_plan_id=service_plan_id,
            site_config=site_config,
            app_settings=app_settings,
            auth_settings=auth_settings,
            backup=backup,
            builtin_logging_enabled=builtin_logging_enabled,
            client_certificate_enabled=client_certificate_enabled,
            client_certificate_mode=client_certificate_mode,
            connection_string=connection_string,
            content_share_force_disabled=content_share_force_disabled,
            daily_memory_time_quota=daily_memory_time_quota,
            enabled=enabled,
            functions_extension_version=functions_extension_version,
            https_only=https_only,
            id=id,
            identity=identity,
            key_vault_reference_identity_id=key_vault_reference_identity_id,
            sticky_settings=sticky_settings,
            storage_account_access_key=storage_account_access_key,
            storage_account_name=storage_account_name,
            storage_key_vault_secret_id=storage_key_vault_secret_id,
            storage_uses_managed_identity=storage_uses_managed_identity,
            tags=tags,
            timeouts=timeouts,
            virtual_network_subnet_id=virtual_network_subnet_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthSettings")
    def put_auth_settings(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        active_directory: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#active_directory LinuxFunctionApp#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#additional_login_parameters LinuxFunctionApp#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_external_redirect_urls LinuxFunctionApp#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_provider LinuxFunctionApp#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#facebook LinuxFunctionApp#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#github LinuxFunctionApp#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#google LinuxFunctionApp#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#issuer LinuxFunctionApp#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#microsoft LinuxFunctionApp#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_version LinuxFunctionApp#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_refresh_extension_hours LinuxFunctionApp#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_store_enabled LinuxFunctionApp#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#twitter LinuxFunctionApp#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#unauthenticated_client_action LinuxFunctionApp#unauthenticated_client_action}
        '''
        value = LinuxFunctionAppAuthSettings(
            enabled=enabled,
            active_directory=active_directory,
            additional_login_parameters=additional_login_parameters,
            allowed_external_redirect_urls=allowed_external_redirect_urls,
            default_provider=default_provider,
            facebook=facebook,
            github=github,
            google=google,
            issuer=issuer,
            microsoft=microsoft,
            runtime_version=runtime_version,
            token_refresh_extension_hours=token_refresh_extension_hours,
            token_store_enabled=token_store_enabled,
            twitter=twitter,
            unauthenticated_client_action=unauthenticated_client_action,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthSettings", [value]))

    @jsii.member(jsii_name="putBackup")
    def put_backup(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["LinuxFunctionAppBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#schedule LinuxFunctionApp#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_url LinuxFunctionApp#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        '''
        value = LinuxFunctionAppBackup(
            name=name,
            schedule=schedule,
            storage_account_url=storage_account_url,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putConnectionString")
    def put_connection_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppConnectionString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionApp.put_connection_string)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConnectionString", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#type LinuxFunctionApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity_ids LinuxFunctionApp#identity_ids}.
        '''
        value = LinuxFunctionAppIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putSiteConfig")
    def put_site_config(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_insights_connection_string: typing.Optional[builtins.str] = None,
        application_insights_key: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        app_scale_limit: typing.Optional[jsii.Number] = None,
        app_service_logs: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigAppServiceLogs", typing.Dict[str, typing.Any]]] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        elastic_instance_minimum: typing.Optional[jsii.Number] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        pre_warmed_instance_count: typing.Optional[jsii.Number] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        runtime_scale_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: If this Linux Web App is Always On enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#always_on LinuxFunctionApp#always_on}
        :param api_definition_url: The URL of the API definition that describes this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_definition_url LinuxFunctionApp#api_definition_url}
        :param api_management_api_id: The ID of the API Management API for this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_management_api_id LinuxFunctionApp#api_management_api_id}
        :param app_command_line: The program and any arguments used to launch this app via the command line. (Example ``node myapp.js``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_command_line LinuxFunctionApp#app_command_line}
        :param application_insights_connection_string: The Connection String for linking the Linux Function App to Application Insights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_connection_string LinuxFunctionApp#application_insights_connection_string}
        :param application_insights_key: The Instrumentation Key for connecting the Linux Function App to Application Insights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_key LinuxFunctionApp#application_insights_key}
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_stack LinuxFunctionApp#application_stack}
        :param app_scale_limit: The number of workers this function app can scale out to. Only applicable to apps on the Consumption and Premium plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_scale_limit LinuxFunctionApp#app_scale_limit}
        :param app_service_logs: app_service_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_service_logs LinuxFunctionApp#app_service_logs}
        :param container_registry_managed_identity_client_id: The Client ID of the Managed Service Identity to use for connections to the Azure Container Registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_managed_identity_client_id LinuxFunctionApp#container_registry_managed_identity_client_id}
        :param container_registry_use_managed_identity: Should connections for Azure Container Registry use Managed Identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_use_managed_identity LinuxFunctionApp#container_registry_use_managed_identity}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#cors LinuxFunctionApp#cors}
        :param default_documents: Specifies a list of Default Documents for the Linux Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_documents LinuxFunctionApp#default_documents}
        :param elastic_instance_minimum: The number of minimum instances for this Linux Function App. Only affects apps on Elastic Premium plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#elastic_instance_minimum LinuxFunctionApp#elastic_instance_minimum}
        :param ftps_state: State of FTP / FTPS service for this function app. Possible values include: ``AllAllowed``, ``FtpsOnly`` and ``Disabled``. Defaults to ``Disabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ftps_state LinuxFunctionApp#ftps_state}
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_eviction_time_in_min LinuxFunctionApp#health_check_eviction_time_in_min}
        :param health_check_path: The path to be checked for this function app health. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_path LinuxFunctionApp#health_check_path}
        :param http2_enabled: Specifies if the http2 protocol should be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#http2_enabled LinuxFunctionApp#http2_enabled}
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_restriction LinuxFunctionApp#ip_restriction}.
        :param load_balancing_mode: The Site load balancing mode. Possible values include: ``WeightedRoundRobin``, ``LeastRequests``, ``LeastResponseTime``, ``WeightedTotalTraffic``, ``RequestHash``, ``PerSiteRoundRobin``. Defaults to ``LeastRequests`` if omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#load_balancing_mode LinuxFunctionApp#load_balancing_mode}
        :param managed_pipeline_mode: The Managed Pipeline mode. Possible values include: ``Integrated``, ``Classic``. Defaults to ``Integrated``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#managed_pipeline_mode LinuxFunctionApp#managed_pipeline_mode}
        :param minimum_tls_version: The configures the minimum version of TLS required for SSL requests. Possible values include: ``1.0``, ``1.1``, and ``1.2``. Defaults to ``1.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#minimum_tls_version LinuxFunctionApp#minimum_tls_version}
        :param pre_warmed_instance_count: The number of pre-warmed instances for this function app. Only affects apps on an Elastic Premium plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#pre_warmed_instance_count LinuxFunctionApp#pre_warmed_instance_count}
        :param remote_debugging_enabled: Should Remote Debugging be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_enabled LinuxFunctionApp#remote_debugging_enabled}
        :param remote_debugging_version: The Remote Debugging Version. Possible values include ``VS2017`` and ``VS2019``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_version LinuxFunctionApp#remote_debugging_version}
        :param runtime_scale_monitoring_enabled: Should Functions Runtime Scale Monitoring be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_scale_monitoring_enabled LinuxFunctionApp#runtime_scale_monitoring_enabled}
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_ip_restriction LinuxFunctionApp#scm_ip_restriction}.
        :param scm_minimum_tls_version: Configures the minimum version of TLS required for SSL requests to the SCM site Possible values include: ``1.0``, ``1.1``, and ``1.2``. Defaults to ``1.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_minimum_tls_version LinuxFunctionApp#scm_minimum_tls_version}
        :param scm_use_main_ip_restriction: Should the Linux Function App ``ip_restriction`` configuration be used for the SCM also. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_use_main_ip_restriction LinuxFunctionApp#scm_use_main_ip_restriction}
        :param use32_bit_worker: Should the Linux Web App use a 32-bit worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_32_bit_worker LinuxFunctionApp#use_32_bit_worker}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#vnet_route_all_enabled LinuxFunctionApp#vnet_route_all_enabled}
        :param websockets_enabled: Should Web Sockets be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#websockets_enabled LinuxFunctionApp#websockets_enabled}
        :param worker_count: The number of Workers for this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#worker_count LinuxFunctionApp#worker_count}
        '''
        value = LinuxFunctionAppSiteConfig(
            always_on=always_on,
            api_definition_url=api_definition_url,
            api_management_api_id=api_management_api_id,
            app_command_line=app_command_line,
            application_insights_connection_string=application_insights_connection_string,
            application_insights_key=application_insights_key,
            application_stack=application_stack,
            app_scale_limit=app_scale_limit,
            app_service_logs=app_service_logs,
            container_registry_managed_identity_client_id=container_registry_managed_identity_client_id,
            container_registry_use_managed_identity=container_registry_use_managed_identity,
            cors=cors,
            default_documents=default_documents,
            elastic_instance_minimum=elastic_instance_minimum,
            ftps_state=ftps_state,
            health_check_eviction_time_in_min=health_check_eviction_time_in_min,
            health_check_path=health_check_path,
            http2_enabled=http2_enabled,
            ip_restriction=ip_restriction,
            load_balancing_mode=load_balancing_mode,
            managed_pipeline_mode=managed_pipeline_mode,
            minimum_tls_version=minimum_tls_version,
            pre_warmed_instance_count=pre_warmed_instance_count,
            remote_debugging_enabled=remote_debugging_enabled,
            remote_debugging_version=remote_debugging_version,
            runtime_scale_monitoring_enabled=runtime_scale_monitoring_enabled,
            scm_ip_restriction=scm_ip_restriction,
            scm_minimum_tls_version=scm_minimum_tls_version,
            scm_use_main_ip_restriction=scm_use_main_ip_restriction,
            use32_bit_worker=use32_bit_worker,
            vnet_route_all_enabled=vnet_route_all_enabled,
            websockets_enabled=websockets_enabled,
            worker_count=worker_count,
        )

        return typing.cast(None, jsii.invoke(self, "putSiteConfig", [value]))

    @jsii.member(jsii_name="putStickySettings")
    def put_sticky_settings(
        self,
        *,
        app_setting_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_string_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_setting_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_setting_names LinuxFunctionApp#app_setting_names}.
        :param connection_string_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string_names LinuxFunctionApp#connection_string_names}.
        '''
        value = LinuxFunctionAppStickySettings(
            app_setting_names=app_setting_names,
            connection_string_names=connection_string_names,
        )

        return typing.cast(None, jsii.invoke(self, "putStickySettings", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#create LinuxFunctionApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#delete LinuxFunctionApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#read LinuxFunctionApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#update LinuxFunctionApp#update}.
        '''
        value = LinuxFunctionAppTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAppSettings")
    def reset_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSettings", []))

    @jsii.member(jsii_name="resetAuthSettings")
    def reset_auth_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSettings", []))

    @jsii.member(jsii_name="resetBackup")
    def reset_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackup", []))

    @jsii.member(jsii_name="resetBuiltinLoggingEnabled")
    def reset_builtin_logging_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuiltinLoggingEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateEnabled")
    def reset_client_certificate_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateMode")
    def reset_client_certificate_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateMode", []))

    @jsii.member(jsii_name="resetConnectionString")
    def reset_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionString", []))

    @jsii.member(jsii_name="resetContentShareForceDisabled")
    def reset_content_share_force_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentShareForceDisabled", []))

    @jsii.member(jsii_name="resetDailyMemoryTimeQuota")
    def reset_daily_memory_time_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyMemoryTimeQuota", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFunctionsExtensionVersion")
    def reset_functions_extension_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionsExtensionVersion", []))

    @jsii.member(jsii_name="resetHttpsOnly")
    def reset_https_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetKeyVaultReferenceIdentityId")
    def reset_key_vault_reference_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultReferenceIdentityId", []))

    @jsii.member(jsii_name="resetStickySettings")
    def reset_sticky_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickySettings", []))

    @jsii.member(jsii_name="resetStorageAccountAccessKey")
    def reset_storage_account_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountAccessKey", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @jsii.member(jsii_name="resetStorageKeyVaultSecretId")
    def reset_storage_key_vault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageKeyVaultSecretId", []))

    @jsii.member(jsii_name="resetStorageUsesManagedIdentity")
    def reset_storage_uses_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageUsesManagedIdentity", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authSettings")
    def auth_settings(self) -> "LinuxFunctionAppAuthSettingsOutputReference":
        return typing.cast("LinuxFunctionAppAuthSettingsOutputReference", jsii.get(self, "authSettings"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "LinuxFunctionAppBackupOutputReference":
        return typing.cast("LinuxFunctionAppBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> "LinuxFunctionAppConnectionStringList":
        return typing.cast("LinuxFunctionAppConnectionStringList", jsii.get(self, "connectionString"))

    @builtins.property
    @jsii.member(jsii_name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomainVerificationId"))

    @builtins.property
    @jsii.member(jsii_name="defaultHostname")
    def default_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultHostname"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "LinuxFunctionAppIdentityOutputReference":
        return typing.cast("LinuxFunctionAppIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddressList")
    def outbound_ip_address_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outboundIpAddressList"))

    @builtins.property
    @jsii.member(jsii_name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "possibleOutboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="possibleOutboundIpAddressList")
    def possible_outbound_ip_address_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "possibleOutboundIpAddressList"))

    @builtins.property
    @jsii.member(jsii_name="siteConfig")
    def site_config(self) -> "LinuxFunctionAppSiteConfigOutputReference":
        return typing.cast("LinuxFunctionAppSiteConfigOutputReference", jsii.get(self, "siteConfig"))

    @builtins.property
    @jsii.member(jsii_name="siteCredential")
    def site_credential(self) -> "LinuxFunctionAppSiteCredentialList":
        return typing.cast("LinuxFunctionAppSiteCredentialList", jsii.get(self, "siteCredential"))

    @builtins.property
    @jsii.member(jsii_name="stickySettings")
    def sticky_settings(self) -> "LinuxFunctionAppStickySettingsOutputReference":
        return typing.cast("LinuxFunctionAppStickySettingsOutputReference", jsii.get(self, "stickySettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LinuxFunctionAppTimeoutsOutputReference":
        return typing.cast("LinuxFunctionAppTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appSettingsInput")
    def app_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "appSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsInput")
    def auth_settings_input(self) -> typing.Optional["LinuxFunctionAppAuthSettings"]:
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettings"], jsii.get(self, "authSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["LinuxFunctionAppBackup"]:
        return typing.cast(typing.Optional["LinuxFunctionAppBackup"], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="builtinLoggingEnabledInput")
    def builtin_logging_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "builtinLoggingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabledInput")
    def client_certificate_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "clientCertificateEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateModeInput")
    def client_certificate_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateModeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppConnectionString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppConnectionString"]]], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="contentShareForceDisabledInput")
    def content_share_force_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "contentShareForceDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyMemoryTimeQuotaInput")
    def daily_memory_time_quota_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dailyMemoryTimeQuotaInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="functionsExtensionVersionInput")
    def functions_extension_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionsExtensionVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["LinuxFunctionAppIdentity"]:
        return typing.cast(typing.Optional["LinuxFunctionAppIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityIdInput")
    def key_vault_reference_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultReferenceIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePlanIdInput")
    def service_plan_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="siteConfigInput")
    def site_config_input(self) -> typing.Optional["LinuxFunctionAppSiteConfig"]:
        return typing.cast(typing.Optional["LinuxFunctionAppSiteConfig"], jsii.get(self, "siteConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stickySettingsInput")
    def sticky_settings_input(
        self,
    ) -> typing.Optional["LinuxFunctionAppStickySettings"]:
        return typing.cast(typing.Optional["LinuxFunctionAppStickySettings"], jsii.get(self, "stickySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageKeyVaultSecretIdInput")
    def storage_key_vault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageKeyVaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageUsesManagedIdentityInput")
    def storage_uses_managed_identity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "storageUsesManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LinuxFunctionAppTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LinuxFunctionAppTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSettings")
    def app_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "appSettings"))

    @app_settings.setter
    def app_settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "app_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSettings", value)

    @builtins.property
    @jsii.member(jsii_name="builtinLoggingEnabled")
    def builtin_logging_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "builtinLoggingEnabled"))

    @builtin_logging_enabled.setter
    def builtin_logging_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "builtin_logging_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "builtinLoggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabled")
    def client_certificate_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "clientCertificateEnabled"))

    @client_certificate_enabled.setter
    def client_certificate_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "client_certificate_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateMode")
    def client_certificate_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateMode"))

    @client_certificate_mode.setter
    def client_certificate_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "client_certificate_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="contentShareForceDisabled")
    def content_share_force_disabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "contentShareForceDisabled"))

    @content_share_force_disabled.setter
    def content_share_force_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "content_share_force_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentShareForceDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="dailyMemoryTimeQuota")
    def daily_memory_time_quota(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dailyMemoryTimeQuota"))

    @daily_memory_time_quota.setter
    def daily_memory_time_quota(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "daily_memory_time_quota").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailyMemoryTimeQuota", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="functionsExtensionVersion")
    def functions_extension_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionsExtensionVersion"))

    @functions_extension_version.setter
    def functions_extension_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "functions_extension_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionsExtensionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityId")
    def key_vault_reference_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultReferenceIdentityId"))

    @key_vault_reference_identity_id.setter
    def key_vault_reference_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "key_vault_reference_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultReferenceIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePlanId")
    def service_plan_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePlanId"))

    @service_plan_id.setter
    def service_plan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "service_plan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePlanId", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "storage_account_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="storageKeyVaultSecretId")
    def storage_key_vault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageKeyVaultSecretId"))

    @storage_key_vault_secret_id.setter
    def storage_key_vault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "storage_key_vault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageKeyVaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="storageUsesManagedIdentity")
    def storage_uses_managed_identity(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "storageUsesManagedIdentity"))

    @storage_uses_managed_identity.setter
    def storage_uses_managed_identity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "storage_uses_managed_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageUsesManagedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionApp, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "active_directory": "activeDirectory",
        "additional_login_parameters": "additionalLoginParameters",
        "allowed_external_redirect_urls": "allowedExternalRedirectUrls",
        "default_provider": "defaultProvider",
        "facebook": "facebook",
        "github": "github",
        "google": "google",
        "issuer": "issuer",
        "microsoft": "microsoft",
        "runtime_version": "runtimeVersion",
        "token_refresh_extension_hours": "tokenRefreshExtensionHours",
        "token_store_enabled": "tokenStoreEnabled",
        "twitter": "twitter",
        "unauthenticated_client_action": "unauthenticatedClientAction",
    },
)
class LinuxFunctionAppAuthSettings:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        active_directory: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["LinuxFunctionAppAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#active_directory LinuxFunctionApp#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#additional_login_parameters LinuxFunctionApp#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_external_redirect_urls LinuxFunctionApp#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_provider LinuxFunctionApp#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#facebook LinuxFunctionApp#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#github LinuxFunctionApp#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#google LinuxFunctionApp#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#issuer LinuxFunctionApp#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#microsoft LinuxFunctionApp#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_version LinuxFunctionApp#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_refresh_extension_hours LinuxFunctionApp#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_store_enabled LinuxFunctionApp#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#twitter LinuxFunctionApp#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#unauthenticated_client_action LinuxFunctionApp#unauthenticated_client_action}
        '''
        if isinstance(active_directory, dict):
            active_directory = LinuxFunctionAppAuthSettingsActiveDirectory(**active_directory)
        if isinstance(facebook, dict):
            facebook = LinuxFunctionAppAuthSettingsFacebook(**facebook)
        if isinstance(github, dict):
            github = LinuxFunctionAppAuthSettingsGithub(**github)
        if isinstance(google, dict):
            google = LinuxFunctionAppAuthSettingsGoogle(**google)
        if isinstance(microsoft, dict):
            microsoft = LinuxFunctionAppAuthSettingsMicrosoft(**microsoft)
        if isinstance(twitter, dict):
            twitter = LinuxFunctionAppAuthSettingsTwitter(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettings.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument active_directory", value=active_directory, expected_type=type_hints["active_directory"])
            check_type(argname="argument additional_login_parameters", value=additional_login_parameters, expected_type=type_hints["additional_login_parameters"])
            check_type(argname="argument allowed_external_redirect_urls", value=allowed_external_redirect_urls, expected_type=type_hints["allowed_external_redirect_urls"])
            check_type(argname="argument default_provider", value=default_provider, expected_type=type_hints["default_provider"])
            check_type(argname="argument facebook", value=facebook, expected_type=type_hints["facebook"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument google", value=google, expected_type=type_hints["google"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument microsoft", value=microsoft, expected_type=type_hints["microsoft"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument token_refresh_extension_hours", value=token_refresh_extension_hours, expected_type=type_hints["token_refresh_extension_hours"])
            check_type(argname="argument token_store_enabled", value=token_store_enabled, expected_type=type_hints["token_store_enabled"])
            check_type(argname="argument twitter", value=twitter, expected_type=type_hints["twitter"])
            check_type(argname="argument unauthenticated_client_action", value=unauthenticated_client_action, expected_type=type_hints["unauthenticated_client_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if active_directory is not None:
            self._values["active_directory"] = active_directory
        if additional_login_parameters is not None:
            self._values["additional_login_parameters"] = additional_login_parameters
        if allowed_external_redirect_urls is not None:
            self._values["allowed_external_redirect_urls"] = allowed_external_redirect_urls
        if default_provider is not None:
            self._values["default_provider"] = default_provider
        if facebook is not None:
            self._values["facebook"] = facebook
        if github is not None:
            self._values["github"] = github
        if google is not None:
            self._values["google"] = google
        if issuer is not None:
            self._values["issuer"] = issuer
        if microsoft is not None:
            self._values["microsoft"] = microsoft
        if runtime_version is not None:
            self._values["runtime_version"] = runtime_version
        if token_refresh_extension_hours is not None:
            self._values["token_refresh_extension_hours"] = token_refresh_extension_hours
        if token_store_enabled is not None:
            self._values["token_store_enabled"] = token_store_enabled
        if twitter is not None:
            self._values["twitter"] = twitter
        if unauthenticated_client_action is not None:
            self._values["unauthenticated_client_action"] = unauthenticated_client_action

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Should the Authentication / Authorization feature be enabled?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["LinuxFunctionAppAuthSettingsActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#active_directory LinuxFunctionApp#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsActiveDirectory"], result)

    @builtins.property
    def additional_login_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#additional_login_parameters LinuxFunctionApp#additional_login_parameters}
        '''
        result = self._values.get("additional_login_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def allowed_external_redirect_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_external_redirect_urls LinuxFunctionApp#allowed_external_redirect_urls}
        '''
        result = self._values.get("allowed_external_redirect_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_provider(self) -> typing.Optional[builtins.str]:
        '''The default authentication provider to use when multiple providers are configured.

        Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_provider LinuxFunctionApp#default_provider}
        '''
        result = self._values.get("default_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facebook(self) -> typing.Optional["LinuxFunctionAppAuthSettingsFacebook"]:
        '''facebook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#facebook LinuxFunctionApp#facebook}
        '''
        result = self._values.get("facebook")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsFacebook"], result)

    @builtins.property
    def github(self) -> typing.Optional["LinuxFunctionAppAuthSettingsGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#github LinuxFunctionApp#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsGithub"], result)

    @builtins.property
    def google(self) -> typing.Optional["LinuxFunctionAppAuthSettingsGoogle"]:
        '''google block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#google LinuxFunctionApp#google}
        '''
        result = self._values.get("google")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsGoogle"], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''The OpenID Connect Issuer URI that represents the entity which issues access tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#issuer LinuxFunctionApp#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft(self) -> typing.Optional["LinuxFunctionAppAuthSettingsMicrosoft"]:
        '''microsoft block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#microsoft LinuxFunctionApp#microsoft}
        '''
        result = self._values.get("microsoft")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsMicrosoft"], result)

    @builtins.property
    def runtime_version(self) -> typing.Optional[builtins.str]:
        '''The RuntimeVersion of the Authentication / Authorization feature in use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_version LinuxFunctionApp#runtime_version}
        '''
        result = self._values.get("runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_refresh_extension_hours(self) -> typing.Optional[jsii.Number]:
        '''The number of hours after session token expiration that a session token can be used to call the token refresh API.

        Defaults to ``72`` hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_refresh_extension_hours LinuxFunctionApp#token_refresh_extension_hours}
        '''
        result = self._values.get("token_refresh_extension_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_store_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#token_store_enabled LinuxFunctionApp#token_store_enabled}
        '''
        result = self._values.get("token_store_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def twitter(self) -> typing.Optional["LinuxFunctionAppAuthSettingsTwitter"]:
        '''twitter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#twitter LinuxFunctionApp#twitter}
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsTwitter"], result)

    @builtins.property
    def unauthenticated_client_action(self) -> typing.Optional[builtins.str]:
        '''The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#unauthenticated_client_action LinuxFunctionApp#unauthenticated_client_action}
        '''
        result = self._values.get("unauthenticated_client_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "allowed_audiences": "allowedAudiences",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
    },
)
class LinuxFunctionAppAuthSettingsActiveDirectory:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_audiences LinuxFunctionApp#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsActiveDirectory.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
        }
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the Client to use to authenticate with Azure Active Directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_audiences LinuxFunctionApp#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, "allowed_audiences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxFunctionAppAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsFacebook",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "app_secret": "appSecret",
        "app_secret_setting_name": "appSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxFunctionAppAuthSettingsFacebook:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_id LinuxFunctionApp#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret LinuxFunctionApp#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret_setting_name LinuxFunctionApp#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsFacebook.__init__)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument app_secret", value=app_secret, expected_type=type_hints["app_secret"])
            check_type(argname="argument app_secret_setting_name", value=app_secret_setting_name, expected_type=type_hints["app_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_id": app_id,
        }
        if app_secret is not None:
            self._values["app_secret"] = app_secret
        if app_secret_setting_name is not None:
            self._values["app_secret_setting_name"] = app_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The App ID of the Facebook app used for login.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_id LinuxFunctionApp#app_id}
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_secret(self) -> typing.Optional[builtins.str]:
        '''The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret LinuxFunctionApp#app_secret}
        '''
        result = self._values.get("app_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret_setting_name LinuxFunctionApp#app_secret_setting_name}
        '''
        result = self._values.get("app_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsFacebook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsFacebookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsFacebookOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsFacebookOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppSecret")
    def reset_app_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSecret", []))

    @jsii.member(jsii_name="resetAppSecretSettingName")
    def reset_app_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="appIdInput")
    def app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecretInput")
    def app_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingNameInput")
    def app_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsFacebookOutputReference, "app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="appSecret")
    def app_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecret"))

    @app_secret.setter
    def app_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsFacebookOutputReference, "app_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecret", value)

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingName")
    def app_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecretSettingName"))

    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsFacebookOutputReference, "app_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsFacebookOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettingsFacebook]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsFacebook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsFacebook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsFacebookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsGithub",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxFunctionAppAuthSettingsGithub:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsGithub.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the GitHub app used for login.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsGithubOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGithubOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGithubOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGithubOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGithubOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettingsGithub]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsGithub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsGoogle",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxFunctionAppAuthSettingsGoogle:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsGoogle.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OpenID Connect Client ID for the Google web application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The client secret associated with the Google web application.  Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsGoogle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsGoogleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsGoogleOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsGoogleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGoogleOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGoogleOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGoogleOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGoogleOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettingsGoogle]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsGoogle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsGoogle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsGoogleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsMicrosoft",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxFunctionAppAuthSettingsMicrosoft:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsMicrosoft.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OAuth 2.0 client ID that was created for the app used for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsMicrosoft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsMicrosoftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsMicrosoftOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsMicrosoftOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsMicrosoft], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsMicrosoft],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppAuthSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectory")
    def put_active_directory(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_audiences LinuxFunctionApp#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        '''
        value = LinuxFunctionAppAuthSettingsActiveDirectory(
            client_id=client_id,
            allowed_audiences=allowed_audiences,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectory", [value]))

    @jsii.member(jsii_name="putFacebook")
    def put_facebook(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_id LinuxFunctionApp#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret LinuxFunctionApp#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_secret_setting_name LinuxFunctionApp#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        value = LinuxFunctionAppAuthSettingsFacebook(
            app_id=app_id,
            app_secret=app_secret,
            app_secret_setting_name=app_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putFacebook", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        value = LinuxFunctionAppAuthSettingsGithub(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGoogle")
    def put_google(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        value = LinuxFunctionAppAuthSettingsGoogle(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGoogle", [value]))

    @jsii.member(jsii_name="putMicrosoft")
    def put_microsoft(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_id LinuxFunctionApp#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret LinuxFunctionApp#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_secret_setting_name LinuxFunctionApp#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#oauth_scopes LinuxFunctionApp#oauth_scopes}
        '''
        value = LinuxFunctionAppAuthSettingsMicrosoft(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putMicrosoft", [value]))

    @jsii.member(jsii_name="putTwitter")
    def put_twitter(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_key LinuxFunctionApp#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret LinuxFunctionApp#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret_setting_name LinuxFunctionApp#consumer_secret_setting_name}
        '''
        value = LinuxFunctionAppAuthSettingsTwitter(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            consumer_secret_setting_name=consumer_secret_setting_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTwitter", [value]))

    @jsii.member(jsii_name="resetActiveDirectory")
    def reset_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectory", []))

    @jsii.member(jsii_name="resetAdditionalLoginParameters")
    def reset_additional_login_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalLoginParameters", []))

    @jsii.member(jsii_name="resetAllowedExternalRedirectUrls")
    def reset_allowed_external_redirect_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExternalRedirectUrls", []))

    @jsii.member(jsii_name="resetDefaultProvider")
    def reset_default_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultProvider", []))

    @jsii.member(jsii_name="resetFacebook")
    def reset_facebook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacebook", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGoogle")
    def reset_google(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogle", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetMicrosoft")
    def reset_microsoft(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoft", []))

    @jsii.member(jsii_name="resetRuntimeVersion")
    def reset_runtime_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeVersion", []))

    @jsii.member(jsii_name="resetTokenRefreshExtensionHours")
    def reset_token_refresh_extension_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenRefreshExtensionHours", []))

    @jsii.member(jsii_name="resetTokenStoreEnabled")
    def reset_token_store_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenStoreEnabled", []))

    @jsii.member(jsii_name="resetTwitter")
    def reset_twitter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTwitter", []))

    @jsii.member(jsii_name="resetUnauthenticatedClientAction")
    def reset_unauthenticated_client_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnauthenticatedClientAction", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectory")
    def active_directory(
        self,
    ) -> LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference:
        return typing.cast(LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="facebook")
    def facebook(self) -> LinuxFunctionAppAuthSettingsFacebookOutputReference:
        return typing.cast(LinuxFunctionAppAuthSettingsFacebookOutputReference, jsii.get(self, "facebook"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> LinuxFunctionAppAuthSettingsGithubOutputReference:
        return typing.cast(LinuxFunctionAppAuthSettingsGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="google")
    def google(self) -> LinuxFunctionAppAuthSettingsGoogleOutputReference:
        return typing.cast(LinuxFunctionAppAuthSettingsGoogleOutputReference, jsii.get(self, "google"))

    @builtins.property
    @jsii.member(jsii_name="microsoft")
    def microsoft(self) -> LinuxFunctionAppAuthSettingsMicrosoftOutputReference:
        return typing.cast(LinuxFunctionAppAuthSettingsMicrosoftOutputReference, jsii.get(self, "microsoft"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> "LinuxFunctionAppAuthSettingsTwitterOutputReference":
        return typing.cast("LinuxFunctionAppAuthSettingsTwitterOutputReference", jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[LinuxFunctionAppAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsActiveDirectory], jsii.get(self, "activeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalLoginParametersInput")
    def additional_login_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalLoginParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrlsInput")
    def allowed_external_redirect_urls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedExternalRedirectUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultProviderInput")
    def default_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="facebookInput")
    def facebook_input(self) -> typing.Optional[LinuxFunctionAppAuthSettingsFacebook]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsFacebook], jsii.get(self, "facebookInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[LinuxFunctionAppAuthSettingsGithub]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="googleInput")
    def google_input(self) -> typing.Optional[LinuxFunctionAppAuthSettingsGoogle]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsGoogle], jsii.get(self, "googleInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftInput")
    def microsoft_input(self) -> typing.Optional[LinuxFunctionAppAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsMicrosoft], jsii.get(self, "microsoftInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeVersionInput")
    def runtime_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHoursInput")
    def token_refresh_extension_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenRefreshExtensionHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabledInput")
    def token_store_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tokenStoreEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="twitterInput")
    def twitter_input(self) -> typing.Optional["LinuxFunctionAppAuthSettingsTwitter"]:
        return typing.cast(typing.Optional["LinuxFunctionAppAuthSettingsTwitter"], jsii.get(self, "twitterInput"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientActionInput")
    def unauthenticated_client_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unauthenticatedClientActionInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalLoginParameters")
    def additional_login_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalLoginParameters"))

    @additional_login_parameters.setter
    def additional_login_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "additional_login_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalLoginParameters", value)

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedExternalRedirectUrls"))

    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "allowed_external_redirect_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExternalRedirectUrls", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProvider")
    def default_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProvider"))

    @default_provider.setter
    def default_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "default_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProvider", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "runtime_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenRefreshExtensionHours"))

    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "token_refresh_extension_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenRefreshExtensionHours", value)

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabled")
    def token_store_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tokenStoreEnabled"))

    @token_store_enabled.setter
    def token_store_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "token_store_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthenticatedClientAction"))

    @unauthenticated_client_action.setter
    def unauthenticated_client_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "unauthenticated_client_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticatedClientAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettings]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsTwitter",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_key": "consumerKey",
        "consumer_secret": "consumerSecret",
        "consumer_secret_setting_name": "consumerSecretSettingName",
    },
)
class LinuxFunctionAppAuthSettingsTwitter:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_key LinuxFunctionApp#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret LinuxFunctionApp#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret_setting_name LinuxFunctionApp#consumer_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsTwitter.__init__)
            check_type(argname="argument consumer_key", value=consumer_key, expected_type=type_hints["consumer_key"])
            check_type(argname="argument consumer_secret", value=consumer_secret, expected_type=type_hints["consumer_secret"])
            check_type(argname="argument consumer_secret_setting_name", value=consumer_secret_setting_name, expected_type=type_hints["consumer_secret_setting_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "consumer_key": consumer_key,
        }
        if consumer_secret is not None:
            self._values["consumer_secret"] = consumer_secret
        if consumer_secret_setting_name is not None:
            self._values["consumer_secret_setting_name"] = consumer_secret_setting_name

    @builtins.property
    def consumer_key(self) -> builtins.str:
        '''The OAuth 1.0a consumer key of the Twitter application used for sign-in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_key LinuxFunctionApp#consumer_key}
        '''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret LinuxFunctionApp#consumer_secret}
        '''
        result = self._values.get("consumer_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consumer_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#consumer_secret_setting_name LinuxFunctionApp#consumer_secret_setting_name}
        '''
        result = self._values.get("consumer_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppAuthSettingsTwitter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppAuthSettingsTwitterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppAuthSettingsTwitterOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppAuthSettingsTwitterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConsumerSecret")
    def reset_consumer_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerSecret", []))

    @jsii.member(jsii_name="resetConsumerSecretSettingName")
    def reset_consumer_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerSecretSettingName", []))

    @builtins.property
    @jsii.member(jsii_name="consumerKeyInput")
    def consumer_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerSecretInput")
    def consumer_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingNameInput")
    def consumer_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerKey")
    def consumer_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerKey"))

    @consumer_key.setter
    def consumer_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsTwitterOutputReference, "consumer_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerKey", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecret")
    def consumer_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecret"))

    @consumer_secret.setter
    def consumer_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsTwitterOutputReference, "consumer_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecretSettingName"))

    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsTwitterOutputReference, "consumer_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppAuthSettingsTwitter]:
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettingsTwitter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppAuthSettingsTwitter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppAuthSettingsTwitterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppBackup",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schedule": "schedule",
        "storage_account_url": "storageAccountUrl",
        "enabled": "enabled",
    },
)
class LinuxFunctionAppBackup:
    def __init__(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["LinuxFunctionAppBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#schedule LinuxFunctionApp#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_url LinuxFunctionApp#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        '''
        if isinstance(schedule, dict):
            schedule = LinuxFunctionAppBackupSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppBackup.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument storage_account_url", value=storage_account_url, expected_type=type_hints["storage_account_url"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "schedule": schedule,
            "storage_account_url": storage_account_url,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def name(self) -> builtins.str:
        '''The name which should be used for this Backup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "LinuxFunctionAppBackupSchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#schedule LinuxFunctionApp#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("LinuxFunctionAppBackupSchedule", result)

    @builtins.property
    def storage_account_url(self) -> builtins.str:
        '''The SAS URL to the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_url LinuxFunctionApp#storage_account_url}
        '''
        result = self._values.get("storage_account_url")
        assert result is not None, "Required property 'storage_account_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should this backup job be enabled?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppBackupOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        frequency_interval: jsii.Number,
        frequency_unit: builtins.str,
        keep_at_least_one_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_interval LinuxFunctionApp#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_unit LinuxFunctionApp#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#keep_at_least_one_backup LinuxFunctionApp#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#start_time LinuxFunctionApp#start_time}
        '''
        value = LinuxFunctionAppBackupSchedule(
            frequency_interval=frequency_interval,
            frequency_unit=frequency_unit,
            keep_at_least_one_backup=keep_at_least_one_backup,
            retention_period_days=retention_period_days,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "LinuxFunctionAppBackupScheduleOutputReference":
        return typing.cast("LinuxFunctionAppBackupScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["LinuxFunctionAppBackupSchedule"]:
        return typing.cast(typing.Optional["LinuxFunctionAppBackupSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrlInput")
    def storage_account_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrl")
    def storage_account_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUrl"))

    @storage_account_url.setter
    def storage_account_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupOutputReference, "storage_account_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppBackup]:
        return typing.cast(typing.Optional[LinuxFunctionAppBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxFunctionAppBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppBackupSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "frequency_interval": "frequencyInterval",
        "frequency_unit": "frequencyUnit",
        "keep_at_least_one_backup": "keepAtLeastOneBackup",
        "retention_period_days": "retentionPeriodDays",
        "start_time": "startTime",
    },
)
class LinuxFunctionAppBackupSchedule:
    def __init__(
        self,
        *,
        frequency_interval: jsii.Number,
        frequency_unit: builtins.str,
        keep_at_least_one_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_interval LinuxFunctionApp#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_unit LinuxFunctionApp#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#keep_at_least_one_backup LinuxFunctionApp#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#start_time LinuxFunctionApp#start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppBackupSchedule.__init__)
            check_type(argname="argument frequency_interval", value=frequency_interval, expected_type=type_hints["frequency_interval"])
            check_type(argname="argument frequency_unit", value=frequency_unit, expected_type=type_hints["frequency_unit"])
            check_type(argname="argument keep_at_least_one_backup", value=keep_at_least_one_backup, expected_type=type_hints["keep_at_least_one_backup"])
            check_type(argname="argument retention_period_days", value=retention_period_days, expected_type=type_hints["retention_period_days"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency_interval": frequency_interval,
            "frequency_unit": frequency_unit,
        }
        if keep_at_least_one_backup is not None:
            self._values["keep_at_least_one_backup"] = keep_at_least_one_backup
        if retention_period_days is not None:
            self._values["retention_period_days"] = retention_period_days
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def frequency_interval(self) -> jsii.Number:
        '''How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_interval LinuxFunctionApp#frequency_interval}
        '''
        result = self._values.get("frequency_interval")
        assert result is not None, "Required property 'frequency_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frequency_unit(self) -> builtins.str:
        '''The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#frequency_unit LinuxFunctionApp#frequency_unit}
        '''
        result = self._values.get("frequency_unit")
        assert result is not None, "Required property 'frequency_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keep_at_least_one_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#keep_at_least_one_backup LinuxFunctionApp#keep_at_least_one_backup}
        '''
        result = self._values.get("keep_at_least_one_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_period_days(self) -> typing.Optional[jsii.Number]:
        '''After how many days backups should be deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        '''
        result = self._values.get("retention_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''When the schedule should start working in RFC-3339 format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#start_time LinuxFunctionApp#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppBackupSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppBackupScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppBackupScheduleOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppBackupScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeepAtLeastOneBackup")
    def reset_keep_at_least_one_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepAtLeastOneBackup", []))

    @jsii.member(jsii_name="resetRetentionPeriodDays")
    def reset_retention_period_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPeriodDays", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="lastExecutionTime")
    def last_execution_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastExecutionTime"))

    @builtins.property
    @jsii.member(jsii_name="frequencyIntervalInput")
    def frequency_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyUnitInput")
    def frequency_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="keepAtLeastOneBackupInput")
    def keep_at_least_one_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keepAtLeastOneBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDaysInput")
    def retention_period_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInterval")
    def frequency_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequencyInterval"))

    @frequency_interval.setter
    def frequency_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "frequency_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="frequencyUnit")
    def frequency_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequencyUnit"))

    @frequency_unit.setter
    def frequency_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "frequency_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyUnit", value)

    @builtins.property
    @jsii.member(jsii_name="keepAtLeastOneBackup")
    def keep_at_least_one_backup(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "keepAtLeastOneBackup"))

    @keep_at_least_one_backup.setter
    def keep_at_least_one_backup(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "keep_at_least_one_backup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAtLeastOneBackup", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDays")
    def retention_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodDays"))

    @retention_period_days.setter
    def retention_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "retention_period_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppBackupSchedule]:
        return typing.cast(typing.Optional[LinuxFunctionAppBackupSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppBackupSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppBackupScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "service_plan_id": "servicePlanId",
        "site_config": "siteConfig",
        "app_settings": "appSettings",
        "auth_settings": "authSettings",
        "backup": "backup",
        "builtin_logging_enabled": "builtinLoggingEnabled",
        "client_certificate_enabled": "clientCertificateEnabled",
        "client_certificate_mode": "clientCertificateMode",
        "connection_string": "connectionString",
        "content_share_force_disabled": "contentShareForceDisabled",
        "daily_memory_time_quota": "dailyMemoryTimeQuota",
        "enabled": "enabled",
        "functions_extension_version": "functionsExtensionVersion",
        "https_only": "httpsOnly",
        "id": "id",
        "identity": "identity",
        "key_vault_reference_identity_id": "keyVaultReferenceIdentityId",
        "sticky_settings": "stickySettings",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_account_name": "storageAccountName",
        "storage_key_vault_secret_id": "storageKeyVaultSecretId",
        "storage_uses_managed_identity": "storageUsesManagedIdentity",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
    },
)
class LinuxFunctionAppConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        service_plan_id: builtins.str,
        site_config: typing.Union["LinuxFunctionAppSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union[LinuxFunctionAppAuthSettings, typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union[LinuxFunctionAppBackup, typing.Dict[str, typing.Any]]] = None,
        builtin_logging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        content_share_force_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_memory_time_quota: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        functions_extension_version: typing.Optional[builtins.str] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LinuxFunctionAppIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        sticky_settings: typing.Optional[typing.Union["LinuxFunctionAppStickySettings", typing.Dict[str, typing.Any]]] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        storage_key_vault_secret_id: typing.Optional[builtins.str] = None,
        storage_uses_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxFunctionAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#location LinuxFunctionApp#location}.
        :param name: Specifies the name of the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#resource_group_name LinuxFunctionApp#resource_group_name}.
        :param service_plan_id: The ID of the App Service Plan within which to create this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_plan_id LinuxFunctionApp#service_plan_id}
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#site_config LinuxFunctionApp#site_config}
        :param app_settings: A map of key-value pairs for `App Settings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings>`_ and custom values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_settings LinuxFunctionApp#app_settings}
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#auth_settings LinuxFunctionApp#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#backup LinuxFunctionApp#backup}
        :param builtin_logging_enabled: Should built in logging be enabled. Configures ``AzureWebJobsDashboard`` app setting based on the configured storage setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#builtin_logging_enabled LinuxFunctionApp#builtin_logging_enabled}
        :param client_certificate_enabled: Should the function app use Client Certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_enabled LinuxFunctionApp#client_certificate_enabled}
        :param client_certificate_mode: The mode of the Function App's client certificates requirement for incoming requests. Possible values are ``Required``, ``Optional``, and ``OptionalInteractiveUser`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_mode LinuxFunctionApp#client_certificate_mode}
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string LinuxFunctionApp#connection_string}
        :param content_share_force_disabled: Force disable the content share settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#content_share_force_disabled LinuxFunctionApp#content_share_force_disabled}
        :param daily_memory_time_quota: The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps in Consumption Plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#daily_memory_time_quota LinuxFunctionApp#daily_memory_time_quota}
        :param enabled: Is the Linux Function App enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        :param functions_extension_version: The runtime version associated with the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#functions_extension_version LinuxFunctionApp#functions_extension_version}
        :param https_only: Can the Function App only be accessed via HTTPS? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#https_only LinuxFunctionApp#https_only}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#id LinuxFunctionApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity LinuxFunctionApp#identity}
        :param key_vault_reference_identity_id: The User Assigned Identity to use for Key Vault access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#key_vault_reference_identity_id LinuxFunctionApp#key_vault_reference_identity_id}
        :param sticky_settings: sticky_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#sticky_settings LinuxFunctionApp#sticky_settings}
        :param storage_account_access_key: The access key which will be used to access the storage account for the Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_access_key LinuxFunctionApp#storage_account_access_key}
        :param storage_account_name: The backend storage account name which will be used by this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_name LinuxFunctionApp#storage_account_name}
        :param storage_key_vault_secret_id: The Key Vault Secret ID, including version, that contains the Connection String to connect to the storage account for this Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_key_vault_secret_id LinuxFunctionApp#storage_key_vault_secret_id}
        :param storage_uses_managed_identity: Should the Function App use its Managed Identity to access storage? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_uses_managed_identity LinuxFunctionApp#storage_uses_managed_identity}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#tags LinuxFunctionApp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#timeouts LinuxFunctionApp#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(site_config, dict):
            site_config = LinuxFunctionAppSiteConfig(**site_config)
        if isinstance(auth_settings, dict):
            auth_settings = LinuxFunctionAppAuthSettings(**auth_settings)
        if isinstance(backup, dict):
            backup = LinuxFunctionAppBackup(**backup)
        if isinstance(identity, dict):
            identity = LinuxFunctionAppIdentity(**identity)
        if isinstance(sticky_settings, dict):
            sticky_settings = LinuxFunctionAppStickySettings(**sticky_settings)
        if isinstance(timeouts, dict):
            timeouts = LinuxFunctionAppTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument service_plan_id", value=service_plan_id, expected_type=type_hints["service_plan_id"])
            check_type(argname="argument site_config", value=site_config, expected_type=type_hints["site_config"])
            check_type(argname="argument app_settings", value=app_settings, expected_type=type_hints["app_settings"])
            check_type(argname="argument auth_settings", value=auth_settings, expected_type=type_hints["auth_settings"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument builtin_logging_enabled", value=builtin_logging_enabled, expected_type=type_hints["builtin_logging_enabled"])
            check_type(argname="argument client_certificate_enabled", value=client_certificate_enabled, expected_type=type_hints["client_certificate_enabled"])
            check_type(argname="argument client_certificate_mode", value=client_certificate_mode, expected_type=type_hints["client_certificate_mode"])
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument content_share_force_disabled", value=content_share_force_disabled, expected_type=type_hints["content_share_force_disabled"])
            check_type(argname="argument daily_memory_time_quota", value=daily_memory_time_quota, expected_type=type_hints["daily_memory_time_quota"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument functions_extension_version", value=functions_extension_version, expected_type=type_hints["functions_extension_version"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument key_vault_reference_identity_id", value=key_vault_reference_identity_id, expected_type=type_hints["key_vault_reference_identity_id"])
            check_type(argname="argument sticky_settings", value=sticky_settings, expected_type=type_hints["sticky_settings"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument storage_key_vault_secret_id", value=storage_key_vault_secret_id, expected_type=type_hints["storage_key_vault_secret_id"])
            check_type(argname="argument storage_uses_managed_identity", value=storage_uses_managed_identity, expected_type=type_hints["storage_uses_managed_identity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "service_plan_id": service_plan_id,
            "site_config": site_config,
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
        if app_settings is not None:
            self._values["app_settings"] = app_settings
        if auth_settings is not None:
            self._values["auth_settings"] = auth_settings
        if backup is not None:
            self._values["backup"] = backup
        if builtin_logging_enabled is not None:
            self._values["builtin_logging_enabled"] = builtin_logging_enabled
        if client_certificate_enabled is not None:
            self._values["client_certificate_enabled"] = client_certificate_enabled
        if client_certificate_mode is not None:
            self._values["client_certificate_mode"] = client_certificate_mode
        if connection_string is not None:
            self._values["connection_string"] = connection_string
        if content_share_force_disabled is not None:
            self._values["content_share_force_disabled"] = content_share_force_disabled
        if daily_memory_time_quota is not None:
            self._values["daily_memory_time_quota"] = daily_memory_time_quota
        if enabled is not None:
            self._values["enabled"] = enabled
        if functions_extension_version is not None:
            self._values["functions_extension_version"] = functions_extension_version
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if key_vault_reference_identity_id is not None:
            self._values["key_vault_reference_identity_id"] = key_vault_reference_identity_id
        if sticky_settings is not None:
            self._values["sticky_settings"] = sticky_settings
        if storage_account_access_key is not None:
            self._values["storage_account_access_key"] = storage_account_access_key
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name
        if storage_key_vault_secret_id is not None:
            self._values["storage_key_vault_secret_id"] = storage_key_vault_secret_id
        if storage_uses_managed_identity is not None:
            self._values["storage_uses_managed_identity"] = storage_uses_managed_identity
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#location LinuxFunctionApp#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#resource_group_name LinuxFunctionApp#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_plan_id(self) -> builtins.str:
        '''The ID of the App Service Plan within which to create this Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_plan_id LinuxFunctionApp#service_plan_id}
        '''
        result = self._values.get("service_plan_id")
        assert result is not None, "Required property 'service_plan_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_config(self) -> "LinuxFunctionAppSiteConfig":
        '''site_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#site_config LinuxFunctionApp#site_config}
        '''
        result = self._values.get("site_config")
        assert result is not None, "Required property 'site_config' is missing"
        return typing.cast("LinuxFunctionAppSiteConfig", result)

    @builtins.property
    def app_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key-value pairs for `App Settings <https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings>`_ and custom values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_settings LinuxFunctionApp#app_settings}
        '''
        result = self._values.get("app_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auth_settings(self) -> typing.Optional[LinuxFunctionAppAuthSettings]:
        '''auth_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#auth_settings LinuxFunctionApp#auth_settings}
        '''
        result = self._values.get("auth_settings")
        return typing.cast(typing.Optional[LinuxFunctionAppAuthSettings], result)

    @builtins.property
    def backup(self) -> typing.Optional[LinuxFunctionAppBackup]:
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#backup LinuxFunctionApp#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[LinuxFunctionAppBackup], result)

    @builtins.property
    def builtin_logging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should built in logging be enabled. Configures ``AzureWebJobsDashboard`` app setting based on the configured storage setting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#builtin_logging_enabled LinuxFunctionApp#builtin_logging_enabled}
        '''
        result = self._values.get("builtin_logging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the function app use Client Certificates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_enabled LinuxFunctionApp#client_certificate_enabled}
        '''
        result = self._values.get("client_certificate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_mode(self) -> typing.Optional[builtins.str]:
        '''The mode of the Function App's client certificates requirement for incoming requests.

        Possible values are ``Required``, ``Optional``, and ``OptionalInteractiveUser``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#client_certificate_mode LinuxFunctionApp#client_certificate_mode}
        '''
        result = self._values.get("client_certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppConnectionString"]]]:
        '''connection_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string LinuxFunctionApp#connection_string}
        '''
        result = self._values.get("connection_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppConnectionString"]]], result)

    @builtins.property
    def content_share_force_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Force disable the content share settings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#content_share_force_disabled LinuxFunctionApp#content_share_force_disabled}
        '''
        result = self._values.get("content_share_force_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def daily_memory_time_quota(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory in gigabyte-seconds that your application is allowed to consume per day.

        Setting this value only affects function apps in Consumption Plans.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#daily_memory_time_quota LinuxFunctionApp#daily_memory_time_quota}
        '''
        result = self._values.get("daily_memory_time_quota")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Is the Linux Function App enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#enabled LinuxFunctionApp#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def functions_extension_version(self) -> typing.Optional[builtins.str]:
        '''The runtime version associated with the Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#functions_extension_version LinuxFunctionApp#functions_extension_version}
        '''
        result = self._values.get("functions_extension_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Can the Function App only be accessed via HTTPS?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#https_only LinuxFunctionApp#https_only}
        '''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#id LinuxFunctionApp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["LinuxFunctionAppIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity LinuxFunctionApp#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["LinuxFunctionAppIdentity"], result)

    @builtins.property
    def key_vault_reference_identity_id(self) -> typing.Optional[builtins.str]:
        '''The User Assigned Identity to use for Key Vault access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#key_vault_reference_identity_id LinuxFunctionApp#key_vault_reference_identity_id}
        '''
        result = self._values.get("key_vault_reference_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sticky_settings(self) -> typing.Optional["LinuxFunctionAppStickySettings"]:
        '''sticky_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#sticky_settings LinuxFunctionApp#sticky_settings}
        '''
        result = self._values.get("sticky_settings")
        return typing.cast(typing.Optional["LinuxFunctionAppStickySettings"], result)

    @builtins.property
    def storage_account_access_key(self) -> typing.Optional[builtins.str]:
        '''The access key which will be used to access the storage account for the Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_access_key LinuxFunctionApp#storage_account_access_key}
        '''
        result = self._values.get("storage_account_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''The backend storage account name which will be used by this Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_account_name LinuxFunctionApp#storage_account_name}
        '''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_key_vault_secret_id(self) -> typing.Optional[builtins.str]:
        '''The Key Vault Secret ID, including version, that contains the Connection String to connect to the storage account for this Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_key_vault_secret_id LinuxFunctionApp#storage_key_vault_secret_id}
        '''
        result = self._values.get("storage_key_vault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_uses_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Function App use its Managed Identity to access storage?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#storage_uses_managed_identity LinuxFunctionApp#storage_uses_managed_identity}
        '''
        result = self._values.get("storage_uses_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#tags LinuxFunctionApp#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LinuxFunctionAppTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#timeouts LinuxFunctionApp#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LinuxFunctionAppTimeouts"], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppConnectionString",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "value": "value"},
)
class LinuxFunctionAppConnectionString:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: The name which should be used for this Connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        :param type: Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#type LinuxFunctionApp#type}
        :param value: The connection string value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#value LinuxFunctionApp#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppConnectionString.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name which should be used for this Connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#type LinuxFunctionApp#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The connection string value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#value LinuxFunctionApp#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppConnectionString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppConnectionStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppConnectionStringList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppConnectionStringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppConnectionStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppConnectionStringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppConnectionStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppConnectionString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppConnectionString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppConnectionString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppConnectionStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppConnectionStringOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppConnectionStringOutputReference.__init__)
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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppConnectionString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppConnectionString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppConnectionString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppConnectionStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class LinuxFunctionAppIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#type LinuxFunctionApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity_ids LinuxFunctionApp#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#type LinuxFunctionApp#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#identity_ids LinuxFunctionApp#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppIdentityOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppIdentity]:
        return typing.cast(typing.Optional[LinuxFunctionAppIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxFunctionAppIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfig",
    jsii_struct_bases=[],
    name_mapping={
        "always_on": "alwaysOn",
        "api_definition_url": "apiDefinitionUrl",
        "api_management_api_id": "apiManagementApiId",
        "app_command_line": "appCommandLine",
        "application_insights_connection_string": "applicationInsightsConnectionString",
        "application_insights_key": "applicationInsightsKey",
        "application_stack": "applicationStack",
        "app_scale_limit": "appScaleLimit",
        "app_service_logs": "appServiceLogs",
        "container_registry_managed_identity_client_id": "containerRegistryManagedIdentityClientId",
        "container_registry_use_managed_identity": "containerRegistryUseManagedIdentity",
        "cors": "cors",
        "default_documents": "defaultDocuments",
        "elastic_instance_minimum": "elasticInstanceMinimum",
        "ftps_state": "ftpsState",
        "health_check_eviction_time_in_min": "healthCheckEvictionTimeInMin",
        "health_check_path": "healthCheckPath",
        "http2_enabled": "http2Enabled",
        "ip_restriction": "ipRestriction",
        "load_balancing_mode": "loadBalancingMode",
        "managed_pipeline_mode": "managedPipelineMode",
        "minimum_tls_version": "minimumTlsVersion",
        "pre_warmed_instance_count": "preWarmedInstanceCount",
        "remote_debugging_enabled": "remoteDebuggingEnabled",
        "remote_debugging_version": "remoteDebuggingVersion",
        "runtime_scale_monitoring_enabled": "runtimeScaleMonitoringEnabled",
        "scm_ip_restriction": "scmIpRestriction",
        "scm_minimum_tls_version": "scmMinimumTlsVersion",
        "scm_use_main_ip_restriction": "scmUseMainIpRestriction",
        "use32_bit_worker": "use32BitWorker",
        "vnet_route_all_enabled": "vnetRouteAllEnabled",
        "websockets_enabled": "websocketsEnabled",
        "worker_count": "workerCount",
    },
)
class LinuxFunctionAppSiteConfig:
    def __init__(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_insights_connection_string: typing.Optional[builtins.str] = None,
        application_insights_key: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        app_scale_limit: typing.Optional[jsii.Number] = None,
        app_service_logs: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigAppServiceLogs", typing.Dict[str, typing.Any]]] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["LinuxFunctionAppSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        elastic_instance_minimum: typing.Optional[jsii.Number] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        pre_warmed_instance_count: typing.Optional[jsii.Number] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        runtime_scale_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: If this Linux Web App is Always On enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#always_on LinuxFunctionApp#always_on}
        :param api_definition_url: The URL of the API definition that describes this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_definition_url LinuxFunctionApp#api_definition_url}
        :param api_management_api_id: The ID of the API Management API for this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_management_api_id LinuxFunctionApp#api_management_api_id}
        :param app_command_line: The program and any arguments used to launch this app via the command line. (Example ``node myapp.js``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_command_line LinuxFunctionApp#app_command_line}
        :param application_insights_connection_string: The Connection String for linking the Linux Function App to Application Insights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_connection_string LinuxFunctionApp#application_insights_connection_string}
        :param application_insights_key: The Instrumentation Key for connecting the Linux Function App to Application Insights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_key LinuxFunctionApp#application_insights_key}
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_stack LinuxFunctionApp#application_stack}
        :param app_scale_limit: The number of workers this function app can scale out to. Only applicable to apps on the Consumption and Premium plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_scale_limit LinuxFunctionApp#app_scale_limit}
        :param app_service_logs: app_service_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_service_logs LinuxFunctionApp#app_service_logs}
        :param container_registry_managed_identity_client_id: The Client ID of the Managed Service Identity to use for connections to the Azure Container Registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_managed_identity_client_id LinuxFunctionApp#container_registry_managed_identity_client_id}
        :param container_registry_use_managed_identity: Should connections for Azure Container Registry use Managed Identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_use_managed_identity LinuxFunctionApp#container_registry_use_managed_identity}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#cors LinuxFunctionApp#cors}
        :param default_documents: Specifies a list of Default Documents for the Linux Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_documents LinuxFunctionApp#default_documents}
        :param elastic_instance_minimum: The number of minimum instances for this Linux Function App. Only affects apps on Elastic Premium plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#elastic_instance_minimum LinuxFunctionApp#elastic_instance_minimum}
        :param ftps_state: State of FTP / FTPS service for this function app. Possible values include: ``AllAllowed``, ``FtpsOnly`` and ``Disabled``. Defaults to ``Disabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ftps_state LinuxFunctionApp#ftps_state}
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_eviction_time_in_min LinuxFunctionApp#health_check_eviction_time_in_min}
        :param health_check_path: The path to be checked for this function app health. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_path LinuxFunctionApp#health_check_path}
        :param http2_enabled: Specifies if the http2 protocol should be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#http2_enabled LinuxFunctionApp#http2_enabled}
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_restriction LinuxFunctionApp#ip_restriction}.
        :param load_balancing_mode: The Site load balancing mode. Possible values include: ``WeightedRoundRobin``, ``LeastRequests``, ``LeastResponseTime``, ``WeightedTotalTraffic``, ``RequestHash``, ``PerSiteRoundRobin``. Defaults to ``LeastRequests`` if omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#load_balancing_mode LinuxFunctionApp#load_balancing_mode}
        :param managed_pipeline_mode: The Managed Pipeline mode. Possible values include: ``Integrated``, ``Classic``. Defaults to ``Integrated``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#managed_pipeline_mode LinuxFunctionApp#managed_pipeline_mode}
        :param minimum_tls_version: The configures the minimum version of TLS required for SSL requests. Possible values include: ``1.0``, ``1.1``, and ``1.2``. Defaults to ``1.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#minimum_tls_version LinuxFunctionApp#minimum_tls_version}
        :param pre_warmed_instance_count: The number of pre-warmed instances for this function app. Only affects apps on an Elastic Premium plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#pre_warmed_instance_count LinuxFunctionApp#pre_warmed_instance_count}
        :param remote_debugging_enabled: Should Remote Debugging be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_enabled LinuxFunctionApp#remote_debugging_enabled}
        :param remote_debugging_version: The Remote Debugging Version. Possible values include ``VS2017`` and ``VS2019``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_version LinuxFunctionApp#remote_debugging_version}
        :param runtime_scale_monitoring_enabled: Should Functions Runtime Scale Monitoring be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_scale_monitoring_enabled LinuxFunctionApp#runtime_scale_monitoring_enabled}
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_ip_restriction LinuxFunctionApp#scm_ip_restriction}.
        :param scm_minimum_tls_version: Configures the minimum version of TLS required for SSL requests to the SCM site Possible values include: ``1.0``, ``1.1``, and ``1.2``. Defaults to ``1.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_minimum_tls_version LinuxFunctionApp#scm_minimum_tls_version}
        :param scm_use_main_ip_restriction: Should the Linux Function App ``ip_restriction`` configuration be used for the SCM also. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_use_main_ip_restriction LinuxFunctionApp#scm_use_main_ip_restriction}
        :param use32_bit_worker: Should the Linux Web App use a 32-bit worker. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_32_bit_worker LinuxFunctionApp#use_32_bit_worker}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#vnet_route_all_enabled LinuxFunctionApp#vnet_route_all_enabled}
        :param websockets_enabled: Should Web Sockets be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#websockets_enabled LinuxFunctionApp#websockets_enabled}
        :param worker_count: The number of Workers for this Linux Function App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#worker_count LinuxFunctionApp#worker_count}
        '''
        if isinstance(application_stack, dict):
            application_stack = LinuxFunctionAppSiteConfigApplicationStack(**application_stack)
        if isinstance(app_service_logs, dict):
            app_service_logs = LinuxFunctionAppSiteConfigAppServiceLogs(**app_service_logs)
        if isinstance(cors, dict):
            cors = LinuxFunctionAppSiteConfigCors(**cors)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfig.__init__)
            check_type(argname="argument always_on", value=always_on, expected_type=type_hints["always_on"])
            check_type(argname="argument api_definition_url", value=api_definition_url, expected_type=type_hints["api_definition_url"])
            check_type(argname="argument api_management_api_id", value=api_management_api_id, expected_type=type_hints["api_management_api_id"])
            check_type(argname="argument app_command_line", value=app_command_line, expected_type=type_hints["app_command_line"])
            check_type(argname="argument application_insights_connection_string", value=application_insights_connection_string, expected_type=type_hints["application_insights_connection_string"])
            check_type(argname="argument application_insights_key", value=application_insights_key, expected_type=type_hints["application_insights_key"])
            check_type(argname="argument application_stack", value=application_stack, expected_type=type_hints["application_stack"])
            check_type(argname="argument app_scale_limit", value=app_scale_limit, expected_type=type_hints["app_scale_limit"])
            check_type(argname="argument app_service_logs", value=app_service_logs, expected_type=type_hints["app_service_logs"])
            check_type(argname="argument container_registry_managed_identity_client_id", value=container_registry_managed_identity_client_id, expected_type=type_hints["container_registry_managed_identity_client_id"])
            check_type(argname="argument container_registry_use_managed_identity", value=container_registry_use_managed_identity, expected_type=type_hints["container_registry_use_managed_identity"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument default_documents", value=default_documents, expected_type=type_hints["default_documents"])
            check_type(argname="argument elastic_instance_minimum", value=elastic_instance_minimum, expected_type=type_hints["elastic_instance_minimum"])
            check_type(argname="argument ftps_state", value=ftps_state, expected_type=type_hints["ftps_state"])
            check_type(argname="argument health_check_eviction_time_in_min", value=health_check_eviction_time_in_min, expected_type=type_hints["health_check_eviction_time_in_min"])
            check_type(argname="argument health_check_path", value=health_check_path, expected_type=type_hints["health_check_path"])
            check_type(argname="argument http2_enabled", value=http2_enabled, expected_type=type_hints["http2_enabled"])
            check_type(argname="argument ip_restriction", value=ip_restriction, expected_type=type_hints["ip_restriction"])
            check_type(argname="argument load_balancing_mode", value=load_balancing_mode, expected_type=type_hints["load_balancing_mode"])
            check_type(argname="argument managed_pipeline_mode", value=managed_pipeline_mode, expected_type=type_hints["managed_pipeline_mode"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument pre_warmed_instance_count", value=pre_warmed_instance_count, expected_type=type_hints["pre_warmed_instance_count"])
            check_type(argname="argument remote_debugging_enabled", value=remote_debugging_enabled, expected_type=type_hints["remote_debugging_enabled"])
            check_type(argname="argument remote_debugging_version", value=remote_debugging_version, expected_type=type_hints["remote_debugging_version"])
            check_type(argname="argument runtime_scale_monitoring_enabled", value=runtime_scale_monitoring_enabled, expected_type=type_hints["runtime_scale_monitoring_enabled"])
            check_type(argname="argument scm_ip_restriction", value=scm_ip_restriction, expected_type=type_hints["scm_ip_restriction"])
            check_type(argname="argument scm_minimum_tls_version", value=scm_minimum_tls_version, expected_type=type_hints["scm_minimum_tls_version"])
            check_type(argname="argument scm_use_main_ip_restriction", value=scm_use_main_ip_restriction, expected_type=type_hints["scm_use_main_ip_restriction"])
            check_type(argname="argument use32_bit_worker", value=use32_bit_worker, expected_type=type_hints["use32_bit_worker"])
            check_type(argname="argument vnet_route_all_enabled", value=vnet_route_all_enabled, expected_type=type_hints["vnet_route_all_enabled"])
            check_type(argname="argument websockets_enabled", value=websockets_enabled, expected_type=type_hints["websockets_enabled"])
            check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if always_on is not None:
            self._values["always_on"] = always_on
        if api_definition_url is not None:
            self._values["api_definition_url"] = api_definition_url
        if api_management_api_id is not None:
            self._values["api_management_api_id"] = api_management_api_id
        if app_command_line is not None:
            self._values["app_command_line"] = app_command_line
        if application_insights_connection_string is not None:
            self._values["application_insights_connection_string"] = application_insights_connection_string
        if application_insights_key is not None:
            self._values["application_insights_key"] = application_insights_key
        if application_stack is not None:
            self._values["application_stack"] = application_stack
        if app_scale_limit is not None:
            self._values["app_scale_limit"] = app_scale_limit
        if app_service_logs is not None:
            self._values["app_service_logs"] = app_service_logs
        if container_registry_managed_identity_client_id is not None:
            self._values["container_registry_managed_identity_client_id"] = container_registry_managed_identity_client_id
        if container_registry_use_managed_identity is not None:
            self._values["container_registry_use_managed_identity"] = container_registry_use_managed_identity
        if cors is not None:
            self._values["cors"] = cors
        if default_documents is not None:
            self._values["default_documents"] = default_documents
        if elastic_instance_minimum is not None:
            self._values["elastic_instance_minimum"] = elastic_instance_minimum
        if ftps_state is not None:
            self._values["ftps_state"] = ftps_state
        if health_check_eviction_time_in_min is not None:
            self._values["health_check_eviction_time_in_min"] = health_check_eviction_time_in_min
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if http2_enabled is not None:
            self._values["http2_enabled"] = http2_enabled
        if ip_restriction is not None:
            self._values["ip_restriction"] = ip_restriction
        if load_balancing_mode is not None:
            self._values["load_balancing_mode"] = load_balancing_mode
        if managed_pipeline_mode is not None:
            self._values["managed_pipeline_mode"] = managed_pipeline_mode
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if pre_warmed_instance_count is not None:
            self._values["pre_warmed_instance_count"] = pre_warmed_instance_count
        if remote_debugging_enabled is not None:
            self._values["remote_debugging_enabled"] = remote_debugging_enabled
        if remote_debugging_version is not None:
            self._values["remote_debugging_version"] = remote_debugging_version
        if runtime_scale_monitoring_enabled is not None:
            self._values["runtime_scale_monitoring_enabled"] = runtime_scale_monitoring_enabled
        if scm_ip_restriction is not None:
            self._values["scm_ip_restriction"] = scm_ip_restriction
        if scm_minimum_tls_version is not None:
            self._values["scm_minimum_tls_version"] = scm_minimum_tls_version
        if scm_use_main_ip_restriction is not None:
            self._values["scm_use_main_ip_restriction"] = scm_use_main_ip_restriction
        if use32_bit_worker is not None:
            self._values["use32_bit_worker"] = use32_bit_worker
        if vnet_route_all_enabled is not None:
            self._values["vnet_route_all_enabled"] = vnet_route_all_enabled
        if websockets_enabled is not None:
            self._values["websockets_enabled"] = websockets_enabled
        if worker_count is not None:
            self._values["worker_count"] = worker_count

    @builtins.property
    def always_on(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this Linux Web App is Always On enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#always_on LinuxFunctionApp#always_on}
        '''
        result = self._values.get("always_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def api_definition_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the API definition that describes this Linux Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_definition_url LinuxFunctionApp#api_definition_url}
        '''
        result = self._values.get("api_definition_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_management_api_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the API Management API for this Linux Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#api_management_api_id LinuxFunctionApp#api_management_api_id}
        '''
        result = self._values.get("api_management_api_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_command_line(self) -> typing.Optional[builtins.str]:
        '''The program and any arguments used to launch this app via the command line. (Example ``node myapp.js``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_command_line LinuxFunctionApp#app_command_line}
        '''
        result = self._values.get("app_command_line")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_insights_connection_string(self) -> typing.Optional[builtins.str]:
        '''The Connection String for linking the Linux Function App to Application Insights.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_connection_string LinuxFunctionApp#application_insights_connection_string}
        '''
        result = self._values.get("application_insights_connection_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_insights_key(self) -> typing.Optional[builtins.str]:
        '''The Instrumentation Key for connecting the Linux Function App to Application Insights.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_insights_key LinuxFunctionApp#application_insights_key}
        '''
        result = self._values.get("application_insights_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_stack(
        self,
    ) -> typing.Optional["LinuxFunctionAppSiteConfigApplicationStack"]:
        '''application_stack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#application_stack LinuxFunctionApp#application_stack}
        '''
        result = self._values.get("application_stack")
        return typing.cast(typing.Optional["LinuxFunctionAppSiteConfigApplicationStack"], result)

    @builtins.property
    def app_scale_limit(self) -> typing.Optional[jsii.Number]:
        '''The number of workers this function app can scale out to.

        Only applicable to apps on the Consumption and Premium plan.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_scale_limit LinuxFunctionApp#app_scale_limit}
        '''
        result = self._values.get("app_scale_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def app_service_logs(
        self,
    ) -> typing.Optional["LinuxFunctionAppSiteConfigAppServiceLogs"]:
        '''app_service_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_service_logs LinuxFunctionApp#app_service_logs}
        '''
        result = self._values.get("app_service_logs")
        return typing.cast(typing.Optional["LinuxFunctionAppSiteConfigAppServiceLogs"], result)

    @builtins.property
    def container_registry_managed_identity_client_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Client ID of the Managed Service Identity to use for connections to the Azure Container Registry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_managed_identity_client_id LinuxFunctionApp#container_registry_managed_identity_client_id}
        '''
        result = self._values.get("container_registry_managed_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should connections for Azure Container Registry use Managed Identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#container_registry_use_managed_identity LinuxFunctionApp#container_registry_use_managed_identity}
        '''
        result = self._values.get("container_registry_use_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cors(self) -> typing.Optional["LinuxFunctionAppSiteConfigCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#cors LinuxFunctionApp#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["LinuxFunctionAppSiteConfigCors"], result)

    @builtins.property
    def default_documents(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Default Documents for the Linux Web App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#default_documents LinuxFunctionApp#default_documents}
        '''
        result = self._values.get("default_documents")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def elastic_instance_minimum(self) -> typing.Optional[jsii.Number]:
        '''The number of minimum instances for this Linux Function App. Only affects apps on Elastic Premium plans.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#elastic_instance_minimum LinuxFunctionApp#elastic_instance_minimum}
        '''
        result = self._values.get("elastic_instance_minimum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ftps_state(self) -> typing.Optional[builtins.str]:
        '''State of FTP / FTPS service for this function app.

        Possible values include: ``AllAllowed``, ``FtpsOnly`` and ``Disabled``. Defaults to ``Disabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ftps_state LinuxFunctionApp#ftps_state}
        '''
        result = self._values.get("ftps_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_eviction_time_in_min(self) -> typing.Optional[jsii.Number]:
        '''The amount of time in minutes that a node is unhealthy before being removed from the load balancer.

        Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_eviction_time_in_min LinuxFunctionApp#health_check_eviction_time_in_min}
        '''
        result = self._values.get("health_check_eviction_time_in_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''The path to be checked for this function app health.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#health_check_path LinuxFunctionApp#health_check_path}
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the http2 protocol should be enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#http2_enabled LinuxFunctionApp#http2_enabled}
        '''
        result = self._values.get("http2_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_restriction LinuxFunctionApp#ip_restriction}.'''
        result = self._values.get("ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigIpRestriction"]]], result)

    @builtins.property
    def load_balancing_mode(self) -> typing.Optional[builtins.str]:
        '''The Site load balancing mode. Possible values include: ``WeightedRoundRobin``, ``LeastRequests``, ``LeastResponseTime``, ``WeightedTotalTraffic``, ``RequestHash``, ``PerSiteRoundRobin``. Defaults to ``LeastRequests`` if omitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#load_balancing_mode LinuxFunctionApp#load_balancing_mode}
        '''
        result = self._values.get("load_balancing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_pipeline_mode(self) -> typing.Optional[builtins.str]:
        '''The Managed Pipeline mode. Possible values include: ``Integrated``, ``Classic``. Defaults to ``Integrated``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#managed_pipeline_mode LinuxFunctionApp#managed_pipeline_mode}
        '''
        result = self._values.get("managed_pipeline_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''The configures the minimum version of TLS required for SSL requests.

        Possible values include: ``1.0``, ``1.1``, and  ``1.2``. Defaults to ``1.2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#minimum_tls_version LinuxFunctionApp#minimum_tls_version}
        '''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_warmed_instance_count(self) -> typing.Optional[jsii.Number]:
        '''The number of pre-warmed instances for this function app. Only affects apps on an Elastic Premium plan.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#pre_warmed_instance_count LinuxFunctionApp#pre_warmed_instance_count}
        '''
        result = self._values.get("pre_warmed_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def remote_debugging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should Remote Debugging be enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_enabled LinuxFunctionApp#remote_debugging_enabled}
        '''
        result = self._values.get("remote_debugging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def remote_debugging_version(self) -> typing.Optional[builtins.str]:
        '''The Remote Debugging Version. Possible values include ``VS2017`` and ``VS2019``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#remote_debugging_version LinuxFunctionApp#remote_debugging_version}
        '''
        result = self._values.get("remote_debugging_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_scale_monitoring_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should Functions Runtime Scale Monitoring be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#runtime_scale_monitoring_enabled LinuxFunctionApp#runtime_scale_monitoring_enabled}
        '''
        result = self._values.get("runtime_scale_monitoring_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scm_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_ip_restriction LinuxFunctionApp#scm_ip_restriction}.'''
        result = self._values.get("scm_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestriction"]]], result)

    @builtins.property
    def scm_minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Configures the minimum version of TLS required for SSL requests to the SCM site Possible values include: ``1.0``, ``1.1``, and  ``1.2``. Defaults to ``1.2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_minimum_tls_version LinuxFunctionApp#scm_minimum_tls_version}
        '''
        result = self._values.get("scm_minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Linux Function App ``ip_restriction`` configuration be used for the SCM also.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#scm_use_main_ip_restriction LinuxFunctionApp#scm_use_main_ip_restriction}
        '''
        result = self._values.get("scm_use_main_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use32_bit_worker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Linux Web App use a 32-bit worker.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_32_bit_worker LinuxFunctionApp#use_32_bit_worker}
        '''
        result = self._values.get("use32_bit_worker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vnet_route_all_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#vnet_route_all_enabled LinuxFunctionApp#vnet_route_all_enabled}
        '''
        result = self._values.get("vnet_route_all_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def websockets_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should Web Sockets be enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#websockets_enabled LinuxFunctionApp#websockets_enabled}
        '''
        result = self._values.get("websockets_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def worker_count(self) -> typing.Optional[jsii.Number]:
        '''The number of Workers for this Linux Function App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#worker_count LinuxFunctionApp#worker_count}
        '''
        result = self._values.get("worker_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigAppServiceLogs",
    jsii_struct_bases=[],
    name_mapping={
        "disk_quota_mb": "diskQuotaMb",
        "retention_period_days": "retentionPeriodDays",
    },
)
class LinuxFunctionAppSiteConfigAppServiceLogs:
    def __init__(
        self,
        *,
        disk_quota_mb: typing.Optional[jsii.Number] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disk_quota_mb: The amount of disk space to use for logs. Valid values are between ``25`` and ``100``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#disk_quota_mb LinuxFunctionApp#disk_quota_mb}
        :param retention_period_days: The retention period for logs in days. Valid values are between ``0`` and ``99999``. Defaults to ``0`` (never delete). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigAppServiceLogs.__init__)
            check_type(argname="argument disk_quota_mb", value=disk_quota_mb, expected_type=type_hints["disk_quota_mb"])
            check_type(argname="argument retention_period_days", value=retention_period_days, expected_type=type_hints["retention_period_days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_quota_mb is not None:
            self._values["disk_quota_mb"] = disk_quota_mb
        if retention_period_days is not None:
            self._values["retention_period_days"] = retention_period_days

    @builtins.property
    def disk_quota_mb(self) -> typing.Optional[jsii.Number]:
        '''The amount of disk space to use for logs. Valid values are between ``25`` and ``100``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#disk_quota_mb LinuxFunctionApp#disk_quota_mb}
        '''
        result = self._values.get("disk_quota_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retention_period_days(self) -> typing.Optional[jsii.Number]:
        '''The retention period for logs in days. Valid values are between ``0`` and ``99999``. Defaults to ``0`` (never delete).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        '''
        result = self._values.get("retention_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigAppServiceLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteConfigAppServiceLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigAppServiceLogsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigAppServiceLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDiskQuotaMb")
    def reset_disk_quota_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskQuotaMb", []))

    @jsii.member(jsii_name="resetRetentionPeriodDays")
    def reset_retention_period_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPeriodDays", []))

    @builtins.property
    @jsii.member(jsii_name="diskQuotaMbInput")
    def disk_quota_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskQuotaMbInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDaysInput")
    def retention_period_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="diskQuotaMb")
    def disk_quota_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskQuotaMb"))

    @disk_quota_mb.setter
    def disk_quota_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigAppServiceLogsOutputReference, "disk_quota_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskQuotaMb", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDays")
    def retention_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodDays"))

    @retention_period_days.setter
    def retention_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigAppServiceLogsOutputReference, "retention_period_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxFunctionAppSiteConfigAppServiceLogs]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigAppServiceLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppSiteConfigAppServiceLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigAppServiceLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigApplicationStack",
    jsii_struct_bases=[],
    name_mapping={
        "docker": "docker",
        "dotnet_version": "dotnetVersion",
        "java_version": "javaVersion",
        "node_version": "nodeVersion",
        "powershell_core_version": "powershellCoreVersion",
        "python_version": "pythonVersion",
        "use_custom_runtime": "useCustomRuntime",
        "use_dotnet_isolated_runtime": "useDotnetIsolatedRuntime",
    },
)
class LinuxFunctionAppSiteConfigApplicationStack:
    def __init__(
        self,
        *,
        docker: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigApplicationStackDocker", typing.Dict[str, typing.Any]]]]] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        powershell_core_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
        use_custom_runtime: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_dotnet_isolated_runtime: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param docker: docker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#docker LinuxFunctionApp#docker}
        :param dotnet_version: The version of .Net. Possible values are ``3.1`` and ``6.0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#dotnet_version LinuxFunctionApp#dotnet_version}
        :param java_version: The version of Java to use. Possible values are ``8``, and ``11``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#java_version LinuxFunctionApp#java_version}
        :param node_version: The version of Node to use. Possible values include ``12``, and ``14``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#node_version LinuxFunctionApp#node_version}
        :param powershell_core_version: The version of PowerShell Core to use. Possibles values are ``7``, and ``7.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#powershell_core_version LinuxFunctionApp#powershell_core_version}
        :param python_version: The version of Python to use. Possible values include ``3.9``, ``3.8``, and ``3.7``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#python_version LinuxFunctionApp#python_version}
        :param use_custom_runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_custom_runtime LinuxFunctionApp#use_custom_runtime}.
        :param use_dotnet_isolated_runtime: Should the DotNet process use an isolated runtime. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_dotnet_isolated_runtime LinuxFunctionApp#use_dotnet_isolated_runtime}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStack.__init__)
            check_type(argname="argument docker", value=docker, expected_type=type_hints["docker"])
            check_type(argname="argument dotnet_version", value=dotnet_version, expected_type=type_hints["dotnet_version"])
            check_type(argname="argument java_version", value=java_version, expected_type=type_hints["java_version"])
            check_type(argname="argument node_version", value=node_version, expected_type=type_hints["node_version"])
            check_type(argname="argument powershell_core_version", value=powershell_core_version, expected_type=type_hints["powershell_core_version"])
            check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
            check_type(argname="argument use_custom_runtime", value=use_custom_runtime, expected_type=type_hints["use_custom_runtime"])
            check_type(argname="argument use_dotnet_isolated_runtime", value=use_dotnet_isolated_runtime, expected_type=type_hints["use_dotnet_isolated_runtime"])
        self._values: typing.Dict[str, typing.Any] = {}
        if docker is not None:
            self._values["docker"] = docker
        if dotnet_version is not None:
            self._values["dotnet_version"] = dotnet_version
        if java_version is not None:
            self._values["java_version"] = java_version
        if node_version is not None:
            self._values["node_version"] = node_version
        if powershell_core_version is not None:
            self._values["powershell_core_version"] = powershell_core_version
        if python_version is not None:
            self._values["python_version"] = python_version
        if use_custom_runtime is not None:
            self._values["use_custom_runtime"] = use_custom_runtime
        if use_dotnet_isolated_runtime is not None:
            self._values["use_dotnet_isolated_runtime"] = use_dotnet_isolated_runtime

    @builtins.property
    def docker(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigApplicationStackDocker"]]]:
        '''docker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#docker LinuxFunctionApp#docker}
        '''
        result = self._values.get("docker")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigApplicationStackDocker"]]], result)

    @builtins.property
    def dotnet_version(self) -> typing.Optional[builtins.str]:
        '''The version of .Net. Possible values are ``3.1`` and ``6.0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#dotnet_version LinuxFunctionApp#dotnet_version}
        '''
        result = self._values.get("dotnet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_version(self) -> typing.Optional[builtins.str]:
        '''The version of Java to use. Possible values are ``8``, and ``11``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#java_version LinuxFunctionApp#java_version}
        '''
        result = self._values.get("java_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_version(self) -> typing.Optional[builtins.str]:
        '''The version of Node to use. Possible values include ``12``, and ``14``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#node_version LinuxFunctionApp#node_version}
        '''
        result = self._values.get("node_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def powershell_core_version(self) -> typing.Optional[builtins.str]:
        '''The version of PowerShell Core to use. Possibles values are ``7``, and ``7.2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#powershell_core_version LinuxFunctionApp#powershell_core_version}
        '''
        result = self._values.get("powershell_core_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def python_version(self) -> typing.Optional[builtins.str]:
        '''The version of Python to use. Possible values include ``3.9``, ``3.8``, and ``3.7``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#python_version LinuxFunctionApp#python_version}
        '''
        result = self._values.get("python_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_custom_runtime(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_custom_runtime LinuxFunctionApp#use_custom_runtime}.'''
        result = self._values.get("use_custom_runtime")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_dotnet_isolated_runtime(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the DotNet process use an isolated runtime. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_dotnet_isolated_runtime LinuxFunctionApp#use_dotnet_isolated_runtime}
        '''
        result = self._values.get("use_dotnet_isolated_runtime")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigApplicationStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigApplicationStackDocker",
    jsii_struct_bases=[],
    name_mapping={
        "image_name": "imageName",
        "image_tag": "imageTag",
        "registry_url": "registryUrl",
        "registry_password": "registryPassword",
        "registry_username": "registryUsername",
    },
)
class LinuxFunctionAppSiteConfigApplicationStackDocker:
    def __init__(
        self,
        *,
        image_name: builtins.str,
        image_tag: builtins.str,
        registry_url: builtins.str,
        registry_password: typing.Optional[builtins.str] = None,
        registry_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_name: The name of the Docker image to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#image_name LinuxFunctionApp#image_name}
        :param image_tag: The image tag of the image to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#image_tag LinuxFunctionApp#image_tag}
        :param registry_url: The URL of the docker registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_url LinuxFunctionApp#registry_url}
        :param registry_password: The password for the account to use to connect to the registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_password LinuxFunctionApp#registry_password}
        :param registry_username: The username to use for connections to the registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_username LinuxFunctionApp#registry_username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackDocker.__init__)
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
            check_type(argname="argument registry_url", value=registry_url, expected_type=type_hints["registry_url"])
            check_type(argname="argument registry_password", value=registry_password, expected_type=type_hints["registry_password"])
            check_type(argname="argument registry_username", value=registry_username, expected_type=type_hints["registry_username"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
            "image_tag": image_tag,
            "registry_url": registry_url,
        }
        if registry_password is not None:
            self._values["registry_password"] = registry_password
        if registry_username is not None:
            self._values["registry_username"] = registry_username

    @builtins.property
    def image_name(self) -> builtins.str:
        '''The name of the Docker image to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#image_name LinuxFunctionApp#image_name}
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_tag(self) -> builtins.str:
        '''The image tag of the image to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#image_tag LinuxFunctionApp#image_tag}
        '''
        result = self._values.get("image_tag")
        assert result is not None, "Required property 'image_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry_url(self) -> builtins.str:
        '''The URL of the docker registry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_url LinuxFunctionApp#registry_url}
        '''
        result = self._values.get("registry_url")
        assert result is not None, "Required property 'registry_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry_password(self) -> typing.Optional[builtins.str]:
        '''The password for the account to use to connect to the registry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_password LinuxFunctionApp#registry_password}
        '''
        result = self._values.get("registry_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_username(self) -> typing.Optional[builtins.str]:
        '''The username to use for connections to the registry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#registry_username LinuxFunctionApp#registry_username}
        '''
        result = self._values.get("registry_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigApplicationStackDocker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteConfigApplicationStackDockerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigApplicationStackDockerList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackDockerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackDockerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigApplicationStackDocker]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigApplicationStackDocker]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigApplicationStackDocker]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRegistryPassword")
    def reset_registry_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryPassword", []))

    @jsii.member(jsii_name="resetRegistryUsername")
    def reset_registry_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryUsername", []))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTagInput")
    def image_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTagInput"))

    @builtins.property
    @jsii.member(jsii_name="registryPasswordInput")
    def registry_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="registryUrlInput")
    def registry_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="registryUsernameInput")
    def registry_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "image_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageTag"))

    @image_tag.setter
    def image_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "image_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTag", value)

    @builtins.property
    @jsii.member(jsii_name="registryPassword")
    def registry_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryPassword"))

    @registry_password.setter
    def registry_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "registry_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryPassword", value)

    @builtins.property
    @jsii.member(jsii_name="registryUrl")
    def registry_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryUrl"))

    @registry_url.setter
    def registry_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "registry_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryUrl", value)

    @builtins.property
    @jsii.member(jsii_name="registryUsername")
    def registry_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryUsername"))

    @registry_username.setter
    def registry_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "registry_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppSiteConfigApplicationStackDocker, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppSiteConfigApplicationStackDocker, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppSiteConfigApplicationStackDocker, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigApplicationStackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigApplicationStackOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDocker")
    def put_docker(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxFunctionAppSiteConfigApplicationStackDocker, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigApplicationStackOutputReference.put_docker)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDocker", [value]))

    @jsii.member(jsii_name="resetDocker")
    def reset_docker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocker", []))

    @jsii.member(jsii_name="resetDotnetVersion")
    def reset_dotnet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDotnetVersion", []))

    @jsii.member(jsii_name="resetJavaVersion")
    def reset_java_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaVersion", []))

    @jsii.member(jsii_name="resetNodeVersion")
    def reset_node_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeVersion", []))

    @jsii.member(jsii_name="resetPowershellCoreVersion")
    def reset_powershell_core_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPowershellCoreVersion", []))

    @jsii.member(jsii_name="resetPythonVersion")
    def reset_python_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonVersion", []))

    @jsii.member(jsii_name="resetUseCustomRuntime")
    def reset_use_custom_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCustomRuntime", []))

    @jsii.member(jsii_name="resetUseDotnetIsolatedRuntime")
    def reset_use_dotnet_isolated_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseDotnetIsolatedRuntime", []))

    @builtins.property
    @jsii.member(jsii_name="docker")
    def docker(self) -> LinuxFunctionAppSiteConfigApplicationStackDockerList:
        return typing.cast(LinuxFunctionAppSiteConfigApplicationStackDockerList, jsii.get(self, "docker"))

    @builtins.property
    @jsii.member(jsii_name="dockerInput")
    def docker_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigApplicationStackDocker]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigApplicationStackDocker]]], jsii.get(self, "dockerInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetVersionInput")
    def dotnet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dotnetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaVersionInput")
    def java_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeVersionInput")
    def node_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="powershellCoreVersionInput")
    def powershell_core_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "powershellCoreVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonVersionInput")
    def python_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pythonVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="useCustomRuntimeInput")
    def use_custom_runtime_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCustomRuntimeInput"))

    @builtins.property
    @jsii.member(jsii_name="useDotnetIsolatedRuntimeInput")
    def use_dotnet_isolated_runtime_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useDotnetIsolatedRuntimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetVersion")
    def dotnet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dotnetVersion"))

    @dotnet_version.setter
    def dotnet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "dotnet_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dotnetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaVersion")
    def java_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaVersion"))

    @java_version.setter
    def java_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "java_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="nodeVersion")
    def node_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeVersion"))

    @node_version.setter
    def node_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "node_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="powershellCoreVersion")
    def powershell_core_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "powershellCoreVersion"))

    @powershell_core_version.setter
    def powershell_core_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "powershell_core_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "powershellCoreVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pythonVersion")
    def python_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pythonVersion"))

    @python_version.setter
    def python_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "python_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonVersion", value)

    @builtins.property
    @jsii.member(jsii_name="useCustomRuntime")
    def use_custom_runtime(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCustomRuntime"))

    @use_custom_runtime.setter
    def use_custom_runtime(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "use_custom_runtime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCustomRuntime", value)

    @builtins.property
    @jsii.member(jsii_name="useDotnetIsolatedRuntime")
    def use_dotnet_isolated_runtime(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useDotnetIsolatedRuntime"))

    @use_dotnet_isolated_runtime.setter
    def use_dotnet_isolated_runtime(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "use_dotnet_isolated_runtime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useDotnetIsolatedRuntime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxFunctionAppSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigApplicationStack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppSiteConfigApplicationStack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigApplicationStackOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigCors",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_origins": "allowedOrigins",
        "support_credentials": "supportCredentials",
    },
)
class LinuxFunctionAppSiteConfigCors:
    def __init__(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_origins LinuxFunctionApp#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#support_credentials LinuxFunctionApp#support_credentials}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigCors.__init__)
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument support_credentials", value=support_credentials, expected_type=type_hints["support_credentials"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_origins": allowed_origins,
        }
        if support_credentials is not None:
            self._values["support_credentials"] = support_credentials

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Specifies a list of origins that should be allowed to make cross-origin calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_origins LinuxFunctionApp#allowed_origins}
        '''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def support_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Are credentials allowed in CORS requests? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#support_credentials LinuxFunctionApp#support_credentials}
        '''
        result = self._values.get("support_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteConfigCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigCorsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSupportCredentials")
    def reset_support_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="supportCredentialsInput")
    def support_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "supportCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigCorsOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="supportCredentials")
    def support_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "supportCredentials"))

    @support_credentials.setter
    def support_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigCorsOutputReference, "support_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppSiteConfigCors]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppSiteConfigCors],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "headers": "headers",
        "ip_address": "ipAddress",
        "name": "name",
        "priority": "priority",
        "service_tag": "serviceTag",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
    },
)
class LinuxFunctionAppSiteConfigIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#action LinuxFunctionApp#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#headers LinuxFunctionApp#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_address LinuxFunctionApp#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#priority LinuxFunctionApp#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_tag LinuxFunctionApp#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestriction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_tag", value=service_tag, expected_type=type_hints["service_tag"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if headers is not None:
            self._values["headers"] = headers
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_tag is not None:
            self._values["service_tag"] = service_tag
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#action LinuxFunctionApp#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#headers LinuxFunctionApp#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_address LinuxFunctionApp#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#priority LinuxFunctionApp#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_tag LinuxFunctionApp#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class LinuxFunctionAppSiteConfigIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_azure_fdid LinuxFunctionApp#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_fd_health_probe LinuxFunctionApp#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_for LinuxFunctionApp#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_host LinuxFunctionApp#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionHeaders.__init__)
            check_type(argname="argument x_azure_fdid", value=x_azure_fdid, expected_type=type_hints["x_azure_fdid"])
            check_type(argname="argument x_fd_health_probe", value=x_fd_health_probe, expected_type=type_hints["x_fd_health_probe"])
            check_type(argname="argument x_forwarded_for", value=x_forwarded_for, expected_type=type_hints["x_forwarded_for"])
            check_type(argname="argument x_forwarded_host", value=x_forwarded_host, expected_type=type_hints["x_forwarded_host"])
        self._values: typing.Dict[str, typing.Any] = {}
        if x_azure_fdid is not None:
            self._values["x_azure_fdid"] = x_azure_fdid
        if x_fd_health_probe is not None:
            self._values["x_fd_health_probe"] = x_fd_health_probe
        if x_forwarded_for is not None:
            self._values["x_forwarded_for"] = x_forwarded_for
        if x_forwarded_host is not None:
            self._values["x_forwarded_host"] = x_forwarded_host

    @builtins.property
    def x_azure_fdid(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_azure_fdid LinuxFunctionApp#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_fd_health_probe LinuxFunctionApp#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_for LinuxFunctionApp#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_host LinuxFunctionApp#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteConfigIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetXAzureFdid")
    def reset_x_azure_fdid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXAzureFdid", []))

    @jsii.member(jsii_name="resetXFdHealthProbe")
    def reset_x_fd_health_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXFdHealthProbe", []))

    @jsii.member(jsii_name="resetXForwardedFor")
    def reset_x_forwarded_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedFor", []))

    @jsii.member(jsii_name="resetXForwardedHost")
    def reset_x_forwarded_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedHost", []))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdidInput")
    def x_azure_fdid_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xAzureFdidInput"))

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbeInput")
    def x_fd_health_probe_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xFdHealthProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedForInput")
    def x_forwarded_for_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedForInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedHostInput")
    def x_forwarded_host_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedHostInput"))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdid")
    def x_azure_fdid(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xAzureFdid"))

    @x_azure_fdid.setter
    def x_azure_fdid(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestrictionList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteConfigIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteConfigIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxFunctionAppSiteConfigIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigIpRestrictionOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceTag")
    def reset_service_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceTag", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> LinuxFunctionAppSiteConfigIpRestrictionHeadersList:
        return typing.cast(LinuxFunctionAppSiteConfigIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTagInput")
    def service_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceTagInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppSiteConfigIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationStack")
    def put_application_stack(
        self,
        *,
        docker: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxFunctionAppSiteConfigApplicationStackDocker, typing.Dict[str, typing.Any]]]]] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        powershell_core_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
        use_custom_runtime: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_dotnet_isolated_runtime: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param docker: docker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#docker LinuxFunctionApp#docker}
        :param dotnet_version: The version of .Net. Possible values are ``3.1`` and ``6.0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#dotnet_version LinuxFunctionApp#dotnet_version}
        :param java_version: The version of Java to use. Possible values are ``8``, and ``11``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#java_version LinuxFunctionApp#java_version}
        :param node_version: The version of Node to use. Possible values include ``12``, and ``14``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#node_version LinuxFunctionApp#node_version}
        :param powershell_core_version: The version of PowerShell Core to use. Possibles values are ``7``, and ``7.2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#powershell_core_version LinuxFunctionApp#powershell_core_version}
        :param python_version: The version of Python to use. Possible values include ``3.9``, ``3.8``, and ``3.7``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#python_version LinuxFunctionApp#python_version}
        :param use_custom_runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_custom_runtime LinuxFunctionApp#use_custom_runtime}.
        :param use_dotnet_isolated_runtime: Should the DotNet process use an isolated runtime. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#use_dotnet_isolated_runtime LinuxFunctionApp#use_dotnet_isolated_runtime}
        '''
        value = LinuxFunctionAppSiteConfigApplicationStack(
            docker=docker,
            dotnet_version=dotnet_version,
            java_version=java_version,
            node_version=node_version,
            powershell_core_version=powershell_core_version,
            python_version=python_version,
            use_custom_runtime=use_custom_runtime,
            use_dotnet_isolated_runtime=use_dotnet_isolated_runtime,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationStack", [value]))

    @jsii.member(jsii_name="putAppServiceLogs")
    def put_app_service_logs(
        self,
        *,
        disk_quota_mb: typing.Optional[jsii.Number] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disk_quota_mb: The amount of disk space to use for logs. Valid values are between ``25`` and ``100``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#disk_quota_mb LinuxFunctionApp#disk_quota_mb}
        :param retention_period_days: The retention period for logs in days. Valid values are between ``0`` and ``99999``. Defaults to ``0`` (never delete). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#retention_period_days LinuxFunctionApp#retention_period_days}
        '''
        value = LinuxFunctionAppSiteConfigAppServiceLogs(
            disk_quota_mb=disk_quota_mb, retention_period_days=retention_period_days
        )

        return typing.cast(None, jsii.invoke(self, "putAppServiceLogs", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#allowed_origins LinuxFunctionApp#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#support_credentials LinuxFunctionApp#support_credentials}
        '''
        value = LinuxFunctionAppSiteConfigCors(
            allowed_origins=allowed_origins, support_credentials=support_credentials
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putIpRestriction")
    def put_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxFunctionAppSiteConfigIpRestriction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigOutputReference.put_ip_restriction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpRestriction", [value]))

    @jsii.member(jsii_name="putScmIpRestriction")
    def put_scm_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigOutputReference.put_scm_ip_restriction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScmIpRestriction", [value]))

    @jsii.member(jsii_name="resetAlwaysOn")
    def reset_always_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysOn", []))

    @jsii.member(jsii_name="resetApiDefinitionUrl")
    def reset_api_definition_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiDefinitionUrl", []))

    @jsii.member(jsii_name="resetApiManagementApiId")
    def reset_api_management_api_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiManagementApiId", []))

    @jsii.member(jsii_name="resetAppCommandLine")
    def reset_app_command_line(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppCommandLine", []))

    @jsii.member(jsii_name="resetApplicationInsightsConnectionString")
    def reset_application_insights_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationInsightsConnectionString", []))

    @jsii.member(jsii_name="resetApplicationInsightsKey")
    def reset_application_insights_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationInsightsKey", []))

    @jsii.member(jsii_name="resetApplicationStack")
    def reset_application_stack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationStack", []))

    @jsii.member(jsii_name="resetAppScaleLimit")
    def reset_app_scale_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppScaleLimit", []))

    @jsii.member(jsii_name="resetAppServiceLogs")
    def reset_app_service_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppServiceLogs", []))

    @jsii.member(jsii_name="resetContainerRegistryManagedIdentityClientId")
    def reset_container_registry_managed_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryManagedIdentityClientId", []))

    @jsii.member(jsii_name="resetContainerRegistryUseManagedIdentity")
    def reset_container_registry_use_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryUseManagedIdentity", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetDefaultDocuments")
    def reset_default_documents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultDocuments", []))

    @jsii.member(jsii_name="resetElasticInstanceMinimum")
    def reset_elastic_instance_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticInstanceMinimum", []))

    @jsii.member(jsii_name="resetFtpsState")
    def reset_ftps_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFtpsState", []))

    @jsii.member(jsii_name="resetHealthCheckEvictionTimeInMin")
    def reset_health_check_eviction_time_in_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckEvictionTimeInMin", []))

    @jsii.member(jsii_name="resetHealthCheckPath")
    def reset_health_check_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckPath", []))

    @jsii.member(jsii_name="resetHttp2Enabled")
    def reset_http2_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Enabled", []))

    @jsii.member(jsii_name="resetIpRestriction")
    def reset_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRestriction", []))

    @jsii.member(jsii_name="resetLoadBalancingMode")
    def reset_load_balancing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingMode", []))

    @jsii.member(jsii_name="resetManagedPipelineMode")
    def reset_managed_pipeline_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedPipelineMode", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetPreWarmedInstanceCount")
    def reset_pre_warmed_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreWarmedInstanceCount", []))

    @jsii.member(jsii_name="resetRemoteDebuggingEnabled")
    def reset_remote_debugging_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingEnabled", []))

    @jsii.member(jsii_name="resetRemoteDebuggingVersion")
    def reset_remote_debugging_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingVersion", []))

    @jsii.member(jsii_name="resetRuntimeScaleMonitoringEnabled")
    def reset_runtime_scale_monitoring_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeScaleMonitoringEnabled", []))

    @jsii.member(jsii_name="resetScmIpRestriction")
    def reset_scm_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmIpRestriction", []))

    @jsii.member(jsii_name="resetScmMinimumTlsVersion")
    def reset_scm_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetScmUseMainIpRestriction")
    def reset_scm_use_main_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmUseMainIpRestriction", []))

    @jsii.member(jsii_name="resetUse32BitWorker")
    def reset_use32_bit_worker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUse32BitWorker", []))

    @jsii.member(jsii_name="resetVnetRouteAllEnabled")
    def reset_vnet_route_all_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnetRouteAllEnabled", []))

    @jsii.member(jsii_name="resetWebsocketsEnabled")
    def reset_websockets_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsocketsEnabled", []))

    @jsii.member(jsii_name="resetWorkerCount")
    def reset_worker_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerCount", []))

    @builtins.property
    @jsii.member(jsii_name="applicationStack")
    def application_stack(
        self,
    ) -> LinuxFunctionAppSiteConfigApplicationStackOutputReference:
        return typing.cast(LinuxFunctionAppSiteConfigApplicationStackOutputReference, jsii.get(self, "applicationStack"))

    @builtins.property
    @jsii.member(jsii_name="appServiceLogs")
    def app_service_logs(
        self,
    ) -> LinuxFunctionAppSiteConfigAppServiceLogsOutputReference:
        return typing.cast(LinuxFunctionAppSiteConfigAppServiceLogsOutputReference, jsii.get(self, "appServiceLogs"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> LinuxFunctionAppSiteConfigCorsOutputReference:
        return typing.cast(LinuxFunctionAppSiteConfigCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorLoggingEnabled")
    def detailed_error_logging_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "detailedErrorLoggingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="ipRestriction")
    def ip_restriction(self) -> LinuxFunctionAppSiteConfigIpRestrictionList:
        return typing.cast(LinuxFunctionAppSiteConfigIpRestrictionList, jsii.get(self, "ipRestriction"))

    @builtins.property
    @jsii.member(jsii_name="linuxFxVersion")
    def linux_fx_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linuxFxVersion"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestriction")
    def scm_ip_restriction(self) -> "LinuxFunctionAppSiteConfigScmIpRestrictionList":
        return typing.cast("LinuxFunctionAppSiteConfigScmIpRestrictionList", jsii.get(self, "scmIpRestriction"))

    @builtins.property
    @jsii.member(jsii_name="scmType")
    def scm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmType"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOnInput")
    def always_on_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "alwaysOnInput"))

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrlInput")
    def api_definition_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiDefinitionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiIdInput")
    def api_management_api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementApiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appCommandLineInput")
    def app_command_line_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appCommandLineInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsConnectionStringInput")
    def application_insights_connection_string_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationInsightsConnectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsKeyInput")
    def application_insights_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationInsightsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationStackInput")
    def application_stack_input(
        self,
    ) -> typing.Optional[LinuxFunctionAppSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigApplicationStack], jsii.get(self, "applicationStackInput"))

    @builtins.property
    @jsii.member(jsii_name="appScaleLimitInput")
    def app_scale_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "appScaleLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="appServiceLogsInput")
    def app_service_logs_input(
        self,
    ) -> typing.Optional[LinuxFunctionAppSiteConfigAppServiceLogs]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigAppServiceLogs], jsii.get(self, "appServiceLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryManagedIdentityClientIdInput")
    def container_registry_managed_identity_client_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryManagedIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryUseManagedIdentityInput")
    def container_registry_use_managed_identity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "containerRegistryUseManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional[LinuxFunctionAppSiteConfigCors]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfigCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDocumentsInput")
    def default_documents_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultDocumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticInstanceMinimumInput")
    def elastic_instance_minimum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "elasticInstanceMinimumInput"))

    @builtins.property
    @jsii.member(jsii_name="ftpsStateInput")
    def ftps_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ftpsStateInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMinInput")
    def health_check_eviction_time_in_min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckEvictionTimeInMinInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckPathInput")
    def health_check_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckPathInput"))

    @builtins.property
    @jsii.member(jsii_name="http2EnabledInput")
    def http2_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "http2EnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRestrictionInput")
    def ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigIpRestriction]]], jsii.get(self, "ipRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingModeInput")
    def load_balancing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPipelineModeInput")
    def managed_pipeline_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPipelineModeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="preWarmedInstanceCountInput")
    def pre_warmed_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preWarmedInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingEnabledInput")
    def remote_debugging_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "remoteDebuggingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersionInput")
    def remote_debugging_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteDebuggingVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeScaleMonitoringEnabledInput")
    def runtime_scale_monitoring_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runtimeScaleMonitoringEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestrictionInput")
    def scm_ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestriction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestriction"]]], jsii.get(self, "scmIpRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersionInput")
    def scm_minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scmMinimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmUseMainIpRestrictionInput")
    def scm_use_main_ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "scmUseMainIpRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="use32BitWorkerInput")
    def use32_bit_worker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "use32BitWorkerInput"))

    @builtins.property
    @jsii.member(jsii_name="vnetRouteAllEnabledInput")
    def vnet_route_all_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vnetRouteAllEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="websocketsEnabledInput")
    def websockets_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "websocketsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCountInput")
    def worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOn")
    def always_on(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "alwaysOn"))

    @always_on.setter
    def always_on(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "always_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysOn", value)

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrl")
    def api_definition_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiDefinitionUrl"))

    @api_definition_url.setter
    def api_definition_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "api_definition_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiDefinitionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiId")
    def api_management_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementApiId"))

    @api_management_api_id.setter
    def api_management_api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "api_management_api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementApiId", value)

    @builtins.property
    @jsii.member(jsii_name="appCommandLine")
    def app_command_line(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appCommandLine"))

    @app_command_line.setter
    def app_command_line(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "app_command_line").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appCommandLine", value)

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsConnectionString")
    def application_insights_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationInsightsConnectionString"))

    @application_insights_connection_string.setter
    def application_insights_connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "application_insights_connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationInsightsConnectionString", value)

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsKey")
    def application_insights_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationInsightsKey"))

    @application_insights_key.setter
    def application_insights_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "application_insights_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationInsightsKey", value)

    @builtins.property
    @jsii.member(jsii_name="appScaleLimit")
    def app_scale_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "appScaleLimit"))

    @app_scale_limit.setter
    def app_scale_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "app_scale_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appScaleLimit", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryManagedIdentityClientId")
    def container_registry_managed_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryManagedIdentityClientId"))

    @container_registry_managed_identity_client_id.setter
    def container_registry_managed_identity_client_id(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "container_registry_managed_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryManagedIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryUseManagedIdentity")
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "containerRegistryUseManagedIdentity"))

    @container_registry_use_managed_identity.setter
    def container_registry_use_managed_identity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "container_registry_use_managed_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryUseManagedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDocuments")
    def default_documents(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultDocuments"))

    @default_documents.setter
    def default_documents(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "default_documents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="elasticInstanceMinimum")
    def elastic_instance_minimum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "elasticInstanceMinimum"))

    @elastic_instance_minimum.setter
    def elastic_instance_minimum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "elastic_instance_minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticInstanceMinimum", value)

    @builtins.property
    @jsii.member(jsii_name="ftpsState")
    def ftps_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ftpsState"))

    @ftps_state.setter
    def ftps_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "ftps_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ftpsState", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMin")
    def health_check_eviction_time_in_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckEvictionTimeInMin"))

    @health_check_eviction_time_in_min.setter
    def health_check_eviction_time_in_min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "health_check_eviction_time_in_min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEvictionTimeInMin", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "health_check_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckPath", value)

    @builtins.property
    @jsii.member(jsii_name="http2Enabled")
    def http2_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "http2Enabled"))

    @http2_enabled.setter
    def http2_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "http2_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMode")
    def load_balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingMode"))

    @load_balancing_mode.setter
    def load_balancing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "load_balancing_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingMode", value)

    @builtins.property
    @jsii.member(jsii_name="managedPipelineMode")
    def managed_pipeline_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPipelineMode"))

    @managed_pipeline_mode.setter
    def managed_pipeline_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "managed_pipeline_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPipelineMode", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="preWarmedInstanceCount")
    def pre_warmed_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preWarmedInstanceCount"))

    @pre_warmed_instance_count.setter
    def pre_warmed_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "pre_warmed_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preWarmedInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingEnabled")
    def remote_debugging_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "remoteDebuggingEnabled"))

    @remote_debugging_enabled.setter
    def remote_debugging_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "remote_debugging_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersion")
    def remote_debugging_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteDebuggingVersion"))

    @remote_debugging_version.setter
    def remote_debugging_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "remote_debugging_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingVersion", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeScaleMonitoringEnabled")
    def runtime_scale_monitoring_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runtimeScaleMonitoringEnabled"))

    @runtime_scale_monitoring_enabled.setter
    def runtime_scale_monitoring_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "runtime_scale_monitoring_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeScaleMonitoringEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersion")
    def scm_minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmMinimumTlsVersion"))

    @scm_minimum_tls_version.setter
    def scm_minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "scm_minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scmMinimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scmUseMainIpRestriction")
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "scmUseMainIpRestriction"))

    @scm_use_main_ip_restriction.setter
    def scm_use_main_ip_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "scm_use_main_ip_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scmUseMainIpRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="use32BitWorker")
    def use32_bit_worker(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "use32BitWorker"))

    @use32_bit_worker.setter
    def use32_bit_worker(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "use32_bit_worker").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "use32BitWorker", value)

    @builtins.property
    @jsii.member(jsii_name="vnetRouteAllEnabled")
    def vnet_route_all_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vnetRouteAllEnabled"))

    @vnet_route_all_enabled.setter
    def vnet_route_all_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "vnet_route_all_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnetRouteAllEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="websocketsEnabled")
    def websockets_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "websocketsEnabled"))

    @websockets_enabled.setter
    def websockets_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "websockets_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websocketsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "worker_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppSiteConfig]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppSiteConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "headers": "headers",
        "ip_address": "ipAddress",
        "name": "name",
        "priority": "priority",
        "service_tag": "serviceTag",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
    },
)
class LinuxFunctionAppSiteConfigScmIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxFunctionAppSiteConfigScmIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#action LinuxFunctionApp#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#headers LinuxFunctionApp#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_address LinuxFunctionApp#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#priority LinuxFunctionApp#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_tag LinuxFunctionApp#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestriction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_tag", value=service_tag, expected_type=type_hints["service_tag"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if headers is not None:
            self._values["headers"] = headers
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_tag is not None:
            self._values["service_tag"] = service_tag
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#action LinuxFunctionApp#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#headers LinuxFunctionApp#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxFunctionAppSiteConfigScmIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#ip_address LinuxFunctionApp#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#name LinuxFunctionApp#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#priority LinuxFunctionApp#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#service_tag LinuxFunctionApp#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#virtual_network_subnet_id LinuxFunctionApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigScmIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class LinuxFunctionAppSiteConfigScmIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_azure_fdid LinuxFunctionApp#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_fd_health_probe LinuxFunctionApp#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_for LinuxFunctionApp#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_host LinuxFunctionApp#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionHeaders.__init__)
            check_type(argname="argument x_azure_fdid", value=x_azure_fdid, expected_type=type_hints["x_azure_fdid"])
            check_type(argname="argument x_fd_health_probe", value=x_fd_health_probe, expected_type=type_hints["x_fd_health_probe"])
            check_type(argname="argument x_forwarded_for", value=x_forwarded_for, expected_type=type_hints["x_forwarded_for"])
            check_type(argname="argument x_forwarded_host", value=x_forwarded_host, expected_type=type_hints["x_forwarded_host"])
        self._values: typing.Dict[str, typing.Any] = {}
        if x_azure_fdid is not None:
            self._values["x_azure_fdid"] = x_azure_fdid
        if x_fd_health_probe is not None:
            self._values["x_fd_health_probe"] = x_fd_health_probe
        if x_forwarded_for is not None:
            self._values["x_forwarded_for"] = x_forwarded_for
        if x_forwarded_host is not None:
            self._values["x_forwarded_host"] = x_forwarded_host

    @builtins.property
    def x_azure_fdid(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_azure_fdid LinuxFunctionApp#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_fd_health_probe LinuxFunctionApp#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_for LinuxFunctionApp#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#x_forwarded_host LinuxFunctionApp#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteConfigScmIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetXAzureFdid")
    def reset_x_azure_fdid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXAzureFdid", []))

    @jsii.member(jsii_name="resetXFdHealthProbe")
    def reset_x_fd_health_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXFdHealthProbe", []))

    @jsii.member(jsii_name="resetXForwardedFor")
    def reset_x_forwarded_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedFor", []))

    @jsii.member(jsii_name="resetXForwardedHost")
    def reset_x_forwarded_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedHost", []))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdidInput")
    def x_azure_fdid_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xAzureFdidInput"))

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbeInput")
    def x_fd_health_probe_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xFdHealthProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedForInput")
    def x_forwarded_for_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedForInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedHostInput")
    def x_forwarded_host_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedHostInput"))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdid")
    def x_azure_fdid(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xAzureFdid"))

    @x_azure_fdid.setter
    def x_azure_fdid(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigScmIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestrictionList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceTag")
    def reset_service_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceTag", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList:
        return typing.cast(LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxFunctionAppSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTagInput")
    def service_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceTagInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppSiteConfigScmIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteCredential",
    jsii_struct_bases=[],
    name_mapping={},
)
class LinuxFunctionAppSiteCredential:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppSiteCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppSiteCredentialList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteCredentialList",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteCredentialList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxFunctionAppSiteCredentialOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteCredentialList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxFunctionAppSiteCredentialOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteCredentialList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteCredentialList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteCredentialList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class LinuxFunctionAppSiteCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppSiteCredentialOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppSiteCredentialOutputReference.__init__)
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
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppSiteCredential]:
        return typing.cast(typing.Optional[LinuxFunctionAppSiteCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppSiteCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppSiteCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppStickySettings",
    jsii_struct_bases=[],
    name_mapping={
        "app_setting_names": "appSettingNames",
        "connection_string_names": "connectionStringNames",
    },
)
class LinuxFunctionAppStickySettings:
    def __init__(
        self,
        *,
        app_setting_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_string_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_setting_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_setting_names LinuxFunctionApp#app_setting_names}.
        :param connection_string_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string_names LinuxFunctionApp#connection_string_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppStickySettings.__init__)
            check_type(argname="argument app_setting_names", value=app_setting_names, expected_type=type_hints["app_setting_names"])
            check_type(argname="argument connection_string_names", value=connection_string_names, expected_type=type_hints["connection_string_names"])
        self._values: typing.Dict[str, typing.Any] = {}
        if app_setting_names is not None:
            self._values["app_setting_names"] = app_setting_names
        if connection_string_names is not None:
            self._values["connection_string_names"] = connection_string_names

    @builtins.property
    def app_setting_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#app_setting_names LinuxFunctionApp#app_setting_names}.'''
        result = self._values.get("app_setting_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_string_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#connection_string_names LinuxFunctionApp#connection_string_names}.'''
        result = self._values.get("connection_string_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppStickySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppStickySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppStickySettingsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppStickySettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppSettingNames")
    def reset_app_setting_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSettingNames", []))

    @jsii.member(jsii_name="resetConnectionStringNames")
    def reset_connection_string_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionStringNames", []))

    @builtins.property
    @jsii.member(jsii_name="appSettingNamesInput")
    def app_setting_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "appSettingNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionStringNamesInput")
    def connection_string_names_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "connectionStringNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="appSettingNames")
    def app_setting_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "appSettingNames"))

    @app_setting_names.setter
    def app_setting_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppStickySettingsOutputReference, "app_setting_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSettingNames", value)

    @builtins.property
    @jsii.member(jsii_name="connectionStringNames")
    def connection_string_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectionStringNames"))

    @connection_string_names.setter
    def connection_string_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppStickySettingsOutputReference, "connection_string_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionStringNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxFunctionAppStickySettings]:
        return typing.cast(typing.Optional[LinuxFunctionAppStickySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxFunctionAppStickySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppStickySettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LinuxFunctionAppTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#create LinuxFunctionApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#delete LinuxFunctionApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#read LinuxFunctionApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#update LinuxFunctionApp#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxFunctionAppTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#create LinuxFunctionApp#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#delete LinuxFunctionApp#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#read LinuxFunctionApp#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_function_app#update LinuxFunctionApp#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxFunctionAppTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxFunctionAppTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxFunctionApp.LinuxFunctionAppTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxFunctionAppTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxFunctionAppTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxFunctionAppTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxFunctionAppTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxFunctionAppTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LinuxFunctionApp",
    "LinuxFunctionAppAuthSettings",
    "LinuxFunctionAppAuthSettingsActiveDirectory",
    "LinuxFunctionAppAuthSettingsActiveDirectoryOutputReference",
    "LinuxFunctionAppAuthSettingsFacebook",
    "LinuxFunctionAppAuthSettingsFacebookOutputReference",
    "LinuxFunctionAppAuthSettingsGithub",
    "LinuxFunctionAppAuthSettingsGithubOutputReference",
    "LinuxFunctionAppAuthSettingsGoogle",
    "LinuxFunctionAppAuthSettingsGoogleOutputReference",
    "LinuxFunctionAppAuthSettingsMicrosoft",
    "LinuxFunctionAppAuthSettingsMicrosoftOutputReference",
    "LinuxFunctionAppAuthSettingsOutputReference",
    "LinuxFunctionAppAuthSettingsTwitter",
    "LinuxFunctionAppAuthSettingsTwitterOutputReference",
    "LinuxFunctionAppBackup",
    "LinuxFunctionAppBackupOutputReference",
    "LinuxFunctionAppBackupSchedule",
    "LinuxFunctionAppBackupScheduleOutputReference",
    "LinuxFunctionAppConfig",
    "LinuxFunctionAppConnectionString",
    "LinuxFunctionAppConnectionStringList",
    "LinuxFunctionAppConnectionStringOutputReference",
    "LinuxFunctionAppIdentity",
    "LinuxFunctionAppIdentityOutputReference",
    "LinuxFunctionAppSiteConfig",
    "LinuxFunctionAppSiteConfigAppServiceLogs",
    "LinuxFunctionAppSiteConfigAppServiceLogsOutputReference",
    "LinuxFunctionAppSiteConfigApplicationStack",
    "LinuxFunctionAppSiteConfigApplicationStackDocker",
    "LinuxFunctionAppSiteConfigApplicationStackDockerList",
    "LinuxFunctionAppSiteConfigApplicationStackDockerOutputReference",
    "LinuxFunctionAppSiteConfigApplicationStackOutputReference",
    "LinuxFunctionAppSiteConfigCors",
    "LinuxFunctionAppSiteConfigCorsOutputReference",
    "LinuxFunctionAppSiteConfigIpRestriction",
    "LinuxFunctionAppSiteConfigIpRestrictionHeaders",
    "LinuxFunctionAppSiteConfigIpRestrictionHeadersList",
    "LinuxFunctionAppSiteConfigIpRestrictionHeadersOutputReference",
    "LinuxFunctionAppSiteConfigIpRestrictionList",
    "LinuxFunctionAppSiteConfigIpRestrictionOutputReference",
    "LinuxFunctionAppSiteConfigOutputReference",
    "LinuxFunctionAppSiteConfigScmIpRestriction",
    "LinuxFunctionAppSiteConfigScmIpRestrictionHeaders",
    "LinuxFunctionAppSiteConfigScmIpRestrictionHeadersList",
    "LinuxFunctionAppSiteConfigScmIpRestrictionHeadersOutputReference",
    "LinuxFunctionAppSiteConfigScmIpRestrictionList",
    "LinuxFunctionAppSiteConfigScmIpRestrictionOutputReference",
    "LinuxFunctionAppSiteCredential",
    "LinuxFunctionAppSiteCredentialList",
    "LinuxFunctionAppSiteCredentialOutputReference",
    "LinuxFunctionAppStickySettings",
    "LinuxFunctionAppStickySettingsOutputReference",
    "LinuxFunctionAppTimeouts",
    "LinuxFunctionAppTimeoutsOutputReference",
]

publication.publish()
