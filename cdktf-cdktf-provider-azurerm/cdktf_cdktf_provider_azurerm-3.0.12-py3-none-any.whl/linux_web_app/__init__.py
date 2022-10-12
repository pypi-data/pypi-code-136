'''
# `azurerm_linux_web_app`

Refer to the Terraform Registory for docs: [`azurerm_linux_web_app`](https://www.terraform.io/docs/providers/azurerm/r/linux_web_app).
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


class LinuxWebApp(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebApp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app azurerm_linux_web_app}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        service_plan_id: builtins.str,
        site_config: typing.Union["LinuxWebAppSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union["LinuxWebAppAuthSettings", typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union["LinuxWebAppBackup", typing.Dict[str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LinuxWebAppIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["LinuxWebAppLogs", typing.Dict[str, typing.Any]]] = None,
        sticky_settings: typing.Optional[typing.Union["LinuxWebAppStickySettings", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxWebAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
        zip_deploy_file: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app azurerm_linux_web_app} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#location LinuxWebApp#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#resource_group_name LinuxWebApp#resource_group_name}.
        :param service_plan_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_plan_id LinuxWebApp#service_plan_id}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#site_config LinuxWebApp#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_settings LinuxWebApp#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auth_settings LinuxWebApp#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#backup LinuxWebApp#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_affinity_enabled LinuxWebApp#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_enabled LinuxWebApp#client_certificate_enabled}.
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_mode LinuxWebApp#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string LinuxWebApp#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#https_only LinuxWebApp#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#id LinuxWebApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity LinuxWebApp#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#key_vault_reference_identity_id LinuxWebApp#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#logs LinuxWebApp#logs}
        :param sticky_settings: sticky_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sticky_settings LinuxWebApp#sticky_settings}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account LinuxWebApp#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#tags LinuxWebApp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#timeouts LinuxWebApp#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#zip_deploy_file LinuxWebApp#zip_deploy_file}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebApp.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LinuxWebAppConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            service_plan_id=service_plan_id,
            site_config=site_config,
            app_settings=app_settings,
            auth_settings=auth_settings,
            backup=backup,
            client_affinity_enabled=client_affinity_enabled,
            client_certificate_enabled=client_certificate_enabled,
            client_certificate_mode=client_certificate_mode,
            connection_string=connection_string,
            enabled=enabled,
            https_only=https_only,
            id=id,
            identity=identity,
            key_vault_reference_identity_id=key_vault_reference_identity_id,
            logs=logs,
            sticky_settings=sticky_settings,
            storage_account=storage_account,
            tags=tags,
            timeouts=timeouts,
            virtual_network_subnet_id=virtual_network_subnet_id,
            zip_deploy_file=zip_deploy_file,
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
        active_directory: typing.Optional[typing.Union["LinuxWebAppAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["LinuxWebAppAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["LinuxWebAppAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["LinuxWebAppAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["LinuxWebAppAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["LinuxWebAppAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#active_directory LinuxWebApp#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#additional_login_parameters LinuxWebApp#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_external_redirect_urls LinuxWebApp#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_provider LinuxWebApp#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#facebook LinuxWebApp#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#github LinuxWebApp#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#google LinuxWebApp#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#issuer LinuxWebApp#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#microsoft LinuxWebApp#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#runtime_version LinuxWebApp#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_refresh_extension_hours LinuxWebApp#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_store_enabled LinuxWebApp#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#twitter LinuxWebApp#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#unauthenticated_client_action LinuxWebApp#unauthenticated_client_action}
        '''
        value = LinuxWebAppAuthSettings(
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
        schedule: typing.Union["LinuxWebAppBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#schedule LinuxWebApp#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account_url LinuxWebApp#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        '''
        value = LinuxWebAppBackup(
            name=name,
            schedule=schedule,
            storage_account_url=storage_account_url,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putConnectionString")
    def put_connection_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppConnectionString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebApp.put_connection_string)
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
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity_ids LinuxWebApp#identity_ids}.
        '''
        value = LinuxWebAppIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putLogs")
    def put_logs(
        self,
        *,
        application_logs: typing.Optional[typing.Union["LinuxWebAppLogsApplicationLogs", typing.Dict[str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["LinuxWebAppLogsHttpLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_logs LinuxWebApp#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#detailed_error_messages LinuxWebApp#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#failed_request_tracing LinuxWebApp#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http_logs LinuxWebApp#http_logs}
        '''
        value = LinuxWebAppLogs(
            application_logs=application_logs,
            detailed_error_messages=detailed_error_messages,
            failed_request_tracing=failed_request_tracing,
            http_logs=http_logs,
        )

        return typing.cast(None, jsii.invoke(self, "putLogs", [value]))

    @jsii.member(jsii_name="putSiteConfig")
    def put_site_config(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["LinuxWebAppSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSetting", typing.Dict[str, typing.Any]]] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["LinuxWebAppSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#always_on LinuxWebApp#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_definition_url LinuxWebApp#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_management_api_id LinuxWebApp#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_command_line LinuxWebApp#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_stack LinuxWebApp#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_enabled LinuxWebApp#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_setting LinuxWebApp#auto_heal_setting}
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_managed_identity_client_id LinuxWebApp#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_use_managed_identity LinuxWebApp#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#cors LinuxWebApp#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_documents LinuxWebApp#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ftps_state LinuxWebApp#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_eviction_time_in_min LinuxWebApp#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_path LinuxWebApp#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http2_enabled LinuxWebApp#http2_enabled}.
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_restriction LinuxWebApp#ip_restriction}.
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#load_balancing_mode LinuxWebApp#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#local_mysql_enabled LinuxWebApp#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#managed_pipeline_mode LinuxWebApp#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_tls_version LinuxWebApp#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_enabled LinuxWebApp#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_version LinuxWebApp#remote_debugging_version}.
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_ip_restriction LinuxWebApp#scm_ip_restriction}.
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_minimum_tls_version LinuxWebApp#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_use_main_ip_restriction LinuxWebApp#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#use_32_bit_worker LinuxWebApp#use_32_bit_worker}.
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#vnet_route_all_enabled LinuxWebApp#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#websockets_enabled LinuxWebApp#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#worker_count LinuxWebApp#worker_count}.
        '''
        value = LinuxWebAppSiteConfig(
            always_on=always_on,
            api_definition_url=api_definition_url,
            api_management_api_id=api_management_api_id,
            app_command_line=app_command_line,
            application_stack=application_stack,
            auto_heal_enabled=auto_heal_enabled,
            auto_heal_setting=auto_heal_setting,
            container_registry_managed_identity_client_id=container_registry_managed_identity_client_id,
            container_registry_use_managed_identity=container_registry_use_managed_identity,
            cors=cors,
            default_documents=default_documents,
            ftps_state=ftps_state,
            health_check_eviction_time_in_min=health_check_eviction_time_in_min,
            health_check_path=health_check_path,
            http2_enabled=http2_enabled,
            ip_restriction=ip_restriction,
            load_balancing_mode=load_balancing_mode,
            local_mysql_enabled=local_mysql_enabled,
            managed_pipeline_mode=managed_pipeline_mode,
            minimum_tls_version=minimum_tls_version,
            remote_debugging_enabled=remote_debugging_enabled,
            remote_debugging_version=remote_debugging_version,
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
        :param app_setting_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_setting_names LinuxWebApp#app_setting_names}.
        :param connection_string_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string_names LinuxWebApp#connection_string_names}.
        '''
        value = LinuxWebAppStickySettings(
            app_setting_names=app_setting_names,
            connection_string_names=connection_string_names,
        )

        return typing.cast(None, jsii.invoke(self, "putStickySettings", [value]))

    @jsii.member(jsii_name="putStorageAccount")
    def put_storage_account(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppStorageAccount", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebApp.put_storage_account)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageAccount", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#create LinuxWebApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#delete LinuxWebApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#read LinuxWebApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#update LinuxWebApp#update}.
        '''
        value = LinuxWebAppTimeouts(
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

    @jsii.member(jsii_name="resetClientAffinityEnabled")
    def reset_client_affinity_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAffinityEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateEnabled")
    def reset_client_certificate_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateMode")
    def reset_client_certificate_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateMode", []))

    @jsii.member(jsii_name="resetConnectionString")
    def reset_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionString", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

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

    @jsii.member(jsii_name="resetLogs")
    def reset_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogs", []))

    @jsii.member(jsii_name="resetStickySettings")
    def reset_sticky_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickySettings", []))

    @jsii.member(jsii_name="resetStorageAccount")
    def reset_storage_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccount", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @jsii.member(jsii_name="resetZipDeployFile")
    def reset_zip_deploy_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipDeployFile", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authSettings")
    def auth_settings(self) -> "LinuxWebAppAuthSettingsOutputReference":
        return typing.cast("LinuxWebAppAuthSettingsOutputReference", jsii.get(self, "authSettings"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "LinuxWebAppBackupOutputReference":
        return typing.cast("LinuxWebAppBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> "LinuxWebAppConnectionStringList":
        return typing.cast("LinuxWebAppConnectionStringList", jsii.get(self, "connectionString"))

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
    def identity(self) -> "LinuxWebAppIdentityOutputReference":
        return typing.cast("LinuxWebAppIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> "LinuxWebAppLogsOutputReference":
        return typing.cast("LinuxWebAppLogsOutputReference", jsii.get(self, "logs"))

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
    def site_config(self) -> "LinuxWebAppSiteConfigOutputReference":
        return typing.cast("LinuxWebAppSiteConfigOutputReference", jsii.get(self, "siteConfig"))

    @builtins.property
    @jsii.member(jsii_name="siteCredential")
    def site_credential(self) -> "LinuxWebAppSiteCredentialList":
        return typing.cast("LinuxWebAppSiteCredentialList", jsii.get(self, "siteCredential"))

    @builtins.property
    @jsii.member(jsii_name="stickySettings")
    def sticky_settings(self) -> "LinuxWebAppStickySettingsOutputReference":
        return typing.cast("LinuxWebAppStickySettingsOutputReference", jsii.get(self, "stickySettings"))

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> "LinuxWebAppStorageAccountList":
        return typing.cast("LinuxWebAppStorageAccountList", jsii.get(self, "storageAccount"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LinuxWebAppTimeoutsOutputReference":
        return typing.cast("LinuxWebAppTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appSettingsInput")
    def app_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "appSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsInput")
    def auth_settings_input(self) -> typing.Optional["LinuxWebAppAuthSettings"]:
        return typing.cast(typing.Optional["LinuxWebAppAuthSettings"], jsii.get(self, "authSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["LinuxWebAppBackup"]:
        return typing.cast(typing.Optional["LinuxWebAppBackup"], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAffinityEnabledInput")
    def client_affinity_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "clientAffinityEnabledInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppConnectionString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppConnectionString"]]], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["LinuxWebAppIdentity"]:
        return typing.cast(typing.Optional["LinuxWebAppIdentity"], jsii.get(self, "identityInput"))

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
    @jsii.member(jsii_name="logsInput")
    def logs_input(self) -> typing.Optional["LinuxWebAppLogs"]:
        return typing.cast(typing.Optional["LinuxWebAppLogs"], jsii.get(self, "logsInput"))

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
    def site_config_input(self) -> typing.Optional["LinuxWebAppSiteConfig"]:
        return typing.cast(typing.Optional["LinuxWebAppSiteConfig"], jsii.get(self, "siteConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="stickySettingsInput")
    def sticky_settings_input(self) -> typing.Optional["LinuxWebAppStickySettings"]:
        return typing.cast(typing.Optional["LinuxWebAppStickySettings"], jsii.get(self, "stickySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppStorageAccount"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppStorageAccount"]]], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LinuxWebAppTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LinuxWebAppTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="zipDeployFileInput")
    def zip_deploy_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipDeployFileInput"))

    @builtins.property
    @jsii.member(jsii_name="appSettings")
    def app_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "appSettings"))

    @app_settings.setter
    def app_settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "app_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSettings", value)

    @builtins.property
    @jsii.member(jsii_name="clientAffinityEnabled")
    def client_affinity_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "clientAffinityEnabled"))

    @client_affinity_enabled.setter
    def client_affinity_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "client_affinity_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAffinityEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "client_certificate_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateMode")
    def client_certificate_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateMode"))

    @client_certificate_mode.setter
    def client_certificate_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "client_certificate_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityId")
    def key_vault_reference_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultReferenceIdentityId"))

    @key_vault_reference_identity_id.setter
    def key_vault_reference_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "key_vault_reference_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultReferenceIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePlanId")
    def service_plan_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePlanId"))

    @service_plan_id.setter
    def service_plan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "service_plan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePlanId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="zipDeployFile")
    def zip_deploy_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipDeployFile"))

    @zip_deploy_file.setter
    def zip_deploy_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebApp, "zip_deploy_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipDeployFile", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettings",
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
class LinuxWebAppAuthSettings:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        active_directory: typing.Optional[typing.Union["LinuxWebAppAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["LinuxWebAppAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["LinuxWebAppAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["LinuxWebAppAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["LinuxWebAppAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["LinuxWebAppAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#active_directory LinuxWebApp#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#additional_login_parameters LinuxWebApp#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_external_redirect_urls LinuxWebApp#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_provider LinuxWebApp#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#facebook LinuxWebApp#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#github LinuxWebApp#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#google LinuxWebApp#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#issuer LinuxWebApp#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#microsoft LinuxWebApp#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#runtime_version LinuxWebApp#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_refresh_extension_hours LinuxWebApp#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_store_enabled LinuxWebApp#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#twitter LinuxWebApp#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#unauthenticated_client_action LinuxWebApp#unauthenticated_client_action}
        '''
        if isinstance(active_directory, dict):
            active_directory = LinuxWebAppAuthSettingsActiveDirectory(**active_directory)
        if isinstance(facebook, dict):
            facebook = LinuxWebAppAuthSettingsFacebook(**facebook)
        if isinstance(github, dict):
            github = LinuxWebAppAuthSettingsGithub(**github)
        if isinstance(google, dict):
            google = LinuxWebAppAuthSettingsGoogle(**google)
        if isinstance(microsoft, dict):
            microsoft = LinuxWebAppAuthSettingsMicrosoft(**microsoft)
        if isinstance(twitter, dict):
            twitter = LinuxWebAppAuthSettingsTwitter(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettings.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["LinuxWebAppAuthSettingsActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#active_directory LinuxWebApp#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsActiveDirectory"], result)

    @builtins.property
    def additional_login_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#additional_login_parameters LinuxWebApp#additional_login_parameters}
        '''
        result = self._values.get("additional_login_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def allowed_external_redirect_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_external_redirect_urls LinuxWebApp#allowed_external_redirect_urls}
        '''
        result = self._values.get("allowed_external_redirect_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_provider(self) -> typing.Optional[builtins.str]:
        '''The default authentication provider to use when multiple providers are configured.

        Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_provider LinuxWebApp#default_provider}
        '''
        result = self._values.get("default_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facebook(self) -> typing.Optional["LinuxWebAppAuthSettingsFacebook"]:
        '''facebook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#facebook LinuxWebApp#facebook}
        '''
        result = self._values.get("facebook")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsFacebook"], result)

    @builtins.property
    def github(self) -> typing.Optional["LinuxWebAppAuthSettingsGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#github LinuxWebApp#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsGithub"], result)

    @builtins.property
    def google(self) -> typing.Optional["LinuxWebAppAuthSettingsGoogle"]:
        '''google block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#google LinuxWebApp#google}
        '''
        result = self._values.get("google")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsGoogle"], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''The OpenID Connect Issuer URI that represents the entity which issues access tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#issuer LinuxWebApp#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft(self) -> typing.Optional["LinuxWebAppAuthSettingsMicrosoft"]:
        '''microsoft block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#microsoft LinuxWebApp#microsoft}
        '''
        result = self._values.get("microsoft")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsMicrosoft"], result)

    @builtins.property
    def runtime_version(self) -> typing.Optional[builtins.str]:
        '''The RuntimeVersion of the Authentication / Authorization feature in use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#runtime_version LinuxWebApp#runtime_version}
        '''
        result = self._values.get("runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_refresh_extension_hours(self) -> typing.Optional[jsii.Number]:
        '''The number of hours after session token expiration that a session token can be used to call the token refresh API.

        Defaults to ``72`` hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_refresh_extension_hours LinuxWebApp#token_refresh_extension_hours}
        '''
        result = self._values.get("token_refresh_extension_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_store_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#token_store_enabled LinuxWebApp#token_store_enabled}
        '''
        result = self._values.get("token_store_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def twitter(self) -> typing.Optional["LinuxWebAppAuthSettingsTwitter"]:
        '''twitter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#twitter LinuxWebApp#twitter}
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsTwitter"], result)

    @builtins.property
    def unauthenticated_client_action(self) -> typing.Optional[builtins.str]:
        '''The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#unauthenticated_client_action LinuxWebApp#unauthenticated_client_action}
        '''
        result = self._values.get("unauthenticated_client_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "allowed_audiences": "allowedAudiences",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
    },
)
class LinuxWebAppAuthSettingsActiveDirectory:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_audiences LinuxWebApp#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsActiveDirectory.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_audiences LinuxWebApp#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsActiveDirectoryOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, "allowed_audiences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsFacebook",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "app_secret": "appSecret",
        "app_secret_setting_name": "appSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxWebAppAuthSettingsFacebook:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_id LinuxWebApp#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret LinuxWebApp#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret_setting_name LinuxWebApp#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsFacebook.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_id LinuxWebApp#app_id}
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_secret(self) -> typing.Optional[builtins.str]:
        '''The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret LinuxWebApp#app_secret}
        '''
        result = self._values.get("app_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret_setting_name LinuxWebApp#app_secret_setting_name}
        '''
        result = self._values.get("app_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsFacebook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsFacebookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsFacebookOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsFacebookOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsFacebookOutputReference, "app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="appSecret")
    def app_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecret"))

    @app_secret.setter
    def app_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsFacebookOutputReference, "app_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecret", value)

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingName")
    def app_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecretSettingName"))

    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsFacebookOutputReference, "app_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsFacebookOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsFacebook]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsFacebook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsFacebook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsFacebookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsGithub",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxWebAppAuthSettingsGithub:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsGithub.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsGithubOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsGithubOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGithubOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGithubOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGithubOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGithubOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsGithub]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsGithub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsGoogle",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxWebAppAuthSettingsGoogle:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsGoogle.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The client secret associated with the Google web application.  Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsGoogle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsGoogleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsGoogleOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsGoogleOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGoogleOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGoogleOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGoogleOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGoogleOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsGoogle]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsGoogle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsGoogle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsGoogleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsMicrosoft",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class LinuxWebAppAuthSettingsMicrosoft:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsMicrosoft.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsMicrosoft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsMicrosoftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsMicrosoftOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsMicrosoftOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsMicrosoftOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsMicrosoftOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsMicrosoftOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsMicrosoftOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsMicrosoft], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsMicrosoft],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsMicrosoftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppAuthSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsOutputReference.__init__)
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
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_audiences LinuxWebApp#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        '''
        value = LinuxWebAppAuthSettingsActiveDirectory(
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
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_id LinuxWebApp#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret LinuxWebApp#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_secret_setting_name LinuxWebApp#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        value = LinuxWebAppAuthSettingsFacebook(
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
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        value = LinuxWebAppAuthSettingsGithub(
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
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        value = LinuxWebAppAuthSettingsGoogle(
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
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_id LinuxWebApp#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret LinuxWebApp#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_secret_setting_name LinuxWebApp#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#oauth_scopes LinuxWebApp#oauth_scopes}
        '''
        value = LinuxWebAppAuthSettingsMicrosoft(
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
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_key LinuxWebApp#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret LinuxWebApp#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret_setting_name LinuxWebApp#consumer_secret_setting_name}
        '''
        value = LinuxWebAppAuthSettingsTwitter(
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
    def active_directory(self) -> LinuxWebAppAuthSettingsActiveDirectoryOutputReference:
        return typing.cast(LinuxWebAppAuthSettingsActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="facebook")
    def facebook(self) -> LinuxWebAppAuthSettingsFacebookOutputReference:
        return typing.cast(LinuxWebAppAuthSettingsFacebookOutputReference, jsii.get(self, "facebook"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> LinuxWebAppAuthSettingsGithubOutputReference:
        return typing.cast(LinuxWebAppAuthSettingsGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="google")
    def google(self) -> LinuxWebAppAuthSettingsGoogleOutputReference:
        return typing.cast(LinuxWebAppAuthSettingsGoogleOutputReference, jsii.get(self, "google"))

    @builtins.property
    @jsii.member(jsii_name="microsoft")
    def microsoft(self) -> LinuxWebAppAuthSettingsMicrosoftOutputReference:
        return typing.cast(LinuxWebAppAuthSettingsMicrosoftOutputReference, jsii.get(self, "microsoft"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> "LinuxWebAppAuthSettingsTwitterOutputReference":
        return typing.cast("LinuxWebAppAuthSettingsTwitterOutputReference", jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[LinuxWebAppAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsActiveDirectory], jsii.get(self, "activeDirectoryInput"))

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
    def facebook_input(self) -> typing.Optional[LinuxWebAppAuthSettingsFacebook]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsFacebook], jsii.get(self, "facebookInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[LinuxWebAppAuthSettingsGithub]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="googleInput")
    def google_input(self) -> typing.Optional[LinuxWebAppAuthSettingsGoogle]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsGoogle], jsii.get(self, "googleInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftInput")
    def microsoft_input(self) -> typing.Optional[LinuxWebAppAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsMicrosoft], jsii.get(self, "microsoftInput"))

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
    def twitter_input(self) -> typing.Optional["LinuxWebAppAuthSettingsTwitter"]:
        return typing.cast(typing.Optional["LinuxWebAppAuthSettingsTwitter"], jsii.get(self, "twitterInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "additional_login_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalLoginParameters", value)

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedExternalRedirectUrls"))

    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "allowed_external_redirect_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExternalRedirectUrls", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProvider")
    def default_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProvider"))

    @default_provider.setter
    def default_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "default_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProvider", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "runtime_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenRefreshExtensionHours"))

    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "token_refresh_extension_hours").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "token_store_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthenticatedClientAction"))

    @unauthenticated_client_action.setter
    def unauthenticated_client_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "unauthenticated_client_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticatedClientAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettings]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppAuthSettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsTwitter",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_key": "consumerKey",
        "consumer_secret": "consumerSecret",
        "consumer_secret_setting_name": "consumerSecretSettingName",
    },
)
class LinuxWebAppAuthSettingsTwitter:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_key LinuxWebApp#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret LinuxWebApp#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret_setting_name LinuxWebApp#consumer_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsTwitter.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_key LinuxWebApp#consumer_key}
        '''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret LinuxWebApp#consumer_secret}
        '''
        result = self._values.get("consumer_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consumer_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#consumer_secret_setting_name LinuxWebApp#consumer_secret_setting_name}
        '''
        result = self._values.get("consumer_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppAuthSettingsTwitter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppAuthSettingsTwitterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppAuthSettingsTwitterOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppAuthSettingsTwitterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsTwitterOutputReference, "consumer_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerKey", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecret")
    def consumer_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecret"))

    @consumer_secret.setter
    def consumer_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsTwitterOutputReference, "consumer_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecretSettingName"))

    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsTwitterOutputReference, "consumer_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppAuthSettingsTwitter]:
        return typing.cast(typing.Optional[LinuxWebAppAuthSettingsTwitter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppAuthSettingsTwitter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppAuthSettingsTwitterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppBackup",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schedule": "schedule",
        "storage_account_url": "storageAccountUrl",
        "enabled": "enabled",
    },
)
class LinuxWebAppBackup:
    def __init__(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["LinuxWebAppBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#schedule LinuxWebApp#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account_url LinuxWebApp#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        '''
        if isinstance(schedule, dict):
            schedule = LinuxWebAppBackupSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppBackup.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "LinuxWebAppBackupSchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#schedule LinuxWebApp#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("LinuxWebAppBackupSchedule", result)

    @builtins.property
    def storage_account_url(self) -> builtins.str:
        '''The SAS URL to the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account_url LinuxWebApp#storage_account_url}
        '''
        result = self._values.get("storage_account_url")
        assert result is not None, "Required property 'storage_account_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should this backup job be enabled?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppBackupOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppBackupOutputReference.__init__)
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
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_interval LinuxWebApp#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_unit LinuxWebApp#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#keep_at_least_one_backup LinuxWebApp#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_period_days LinuxWebApp#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#start_time LinuxWebApp#start_time}
        '''
        value = LinuxWebAppBackupSchedule(
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
    def schedule(self) -> "LinuxWebAppBackupScheduleOutputReference":
        return typing.cast("LinuxWebAppBackupScheduleOutputReference", jsii.get(self, "schedule"))

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
    def schedule_input(self) -> typing.Optional["LinuxWebAppBackupSchedule"]:
        return typing.cast(typing.Optional["LinuxWebAppBackupSchedule"], jsii.get(self, "scheduleInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrl")
    def storage_account_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUrl"))

    @storage_account_url.setter
    def storage_account_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupOutputReference, "storage_account_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppBackup]:
        return typing.cast(typing.Optional[LinuxWebAppBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppBackupSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "frequency_interval": "frequencyInterval",
        "frequency_unit": "frequencyUnit",
        "keep_at_least_one_backup": "keepAtLeastOneBackup",
        "retention_period_days": "retentionPeriodDays",
        "start_time": "startTime",
    },
)
class LinuxWebAppBackupSchedule:
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
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_interval LinuxWebApp#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_unit LinuxWebApp#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#keep_at_least_one_backup LinuxWebApp#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_period_days LinuxWebApp#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#start_time LinuxWebApp#start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppBackupSchedule.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_interval LinuxWebApp#frequency_interval}
        '''
        result = self._values.get("frequency_interval")
        assert result is not None, "Required property 'frequency_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frequency_unit(self) -> builtins.str:
        '''The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#frequency_unit LinuxWebApp#frequency_unit}
        '''
        result = self._values.get("frequency_unit")
        assert result is not None, "Required property 'frequency_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keep_at_least_one_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#keep_at_least_one_backup LinuxWebApp#keep_at_least_one_backup}
        '''
        result = self._values.get("keep_at_least_one_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_period_days(self) -> typing.Optional[jsii.Number]:
        '''After how many days backups should be deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_period_days LinuxWebApp#retention_period_days}
        '''
        result = self._values.get("retention_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''When the schedule should start working in RFC-3339 format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#start_time LinuxWebApp#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppBackupSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppBackupScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppBackupScheduleOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppBackupScheduleOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "frequency_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="frequencyUnit")
    def frequency_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequencyUnit"))

    @frequency_unit.setter
    def frequency_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "frequency_unit").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "keep_at_least_one_backup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAtLeastOneBackup", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDays")
    def retention_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodDays"))

    @retention_period_days.setter
    def retention_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "retention_period_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppBackupSchedule]:
        return typing.cast(typing.Optional[LinuxWebAppBackupSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppBackupSchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppBackupScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppConfig",
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
        "client_affinity_enabled": "clientAffinityEnabled",
        "client_certificate_enabled": "clientCertificateEnabled",
        "client_certificate_mode": "clientCertificateMode",
        "connection_string": "connectionString",
        "enabled": "enabled",
        "https_only": "httpsOnly",
        "id": "id",
        "identity": "identity",
        "key_vault_reference_identity_id": "keyVaultReferenceIdentityId",
        "logs": "logs",
        "sticky_settings": "stickySettings",
        "storage_account": "storageAccount",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
        "zip_deploy_file": "zipDeployFile",
    },
)
class LinuxWebAppConfig(cdktf.TerraformMetaArguments):
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
        site_config: typing.Union["LinuxWebAppSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union[LinuxWebAppAuthSettings, typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union[LinuxWebAppBackup, typing.Dict[str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LinuxWebAppIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["LinuxWebAppLogs", typing.Dict[str, typing.Any]]] = None,
        sticky_settings: typing.Optional[typing.Union["LinuxWebAppStickySettings", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxWebAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
        zip_deploy_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#location LinuxWebApp#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#resource_group_name LinuxWebApp#resource_group_name}.
        :param service_plan_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_plan_id LinuxWebApp#service_plan_id}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#site_config LinuxWebApp#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_settings LinuxWebApp#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auth_settings LinuxWebApp#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#backup LinuxWebApp#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_affinity_enabled LinuxWebApp#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_enabled LinuxWebApp#client_certificate_enabled}.
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_mode LinuxWebApp#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string LinuxWebApp#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#https_only LinuxWebApp#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#id LinuxWebApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity LinuxWebApp#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#key_vault_reference_identity_id LinuxWebApp#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#logs LinuxWebApp#logs}
        :param sticky_settings: sticky_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sticky_settings LinuxWebApp#sticky_settings}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account LinuxWebApp#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#tags LinuxWebApp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#timeouts LinuxWebApp#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#zip_deploy_file LinuxWebApp#zip_deploy_file}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(site_config, dict):
            site_config = LinuxWebAppSiteConfig(**site_config)
        if isinstance(auth_settings, dict):
            auth_settings = LinuxWebAppAuthSettings(**auth_settings)
        if isinstance(backup, dict):
            backup = LinuxWebAppBackup(**backup)
        if isinstance(identity, dict):
            identity = LinuxWebAppIdentity(**identity)
        if isinstance(logs, dict):
            logs = LinuxWebAppLogs(**logs)
        if isinstance(sticky_settings, dict):
            sticky_settings = LinuxWebAppStickySettings(**sticky_settings)
        if isinstance(timeouts, dict):
            timeouts = LinuxWebAppTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppConfig.__init__)
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
            check_type(argname="argument client_affinity_enabled", value=client_affinity_enabled, expected_type=type_hints["client_affinity_enabled"])
            check_type(argname="argument client_certificate_enabled", value=client_certificate_enabled, expected_type=type_hints["client_certificate_enabled"])
            check_type(argname="argument client_certificate_mode", value=client_certificate_mode, expected_type=type_hints["client_certificate_mode"])
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument key_vault_reference_identity_id", value=key_vault_reference_identity_id, expected_type=type_hints["key_vault_reference_identity_id"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument sticky_settings", value=sticky_settings, expected_type=type_hints["sticky_settings"])
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
            check_type(argname="argument zip_deploy_file", value=zip_deploy_file, expected_type=type_hints["zip_deploy_file"])
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
        if client_affinity_enabled is not None:
            self._values["client_affinity_enabled"] = client_affinity_enabled
        if client_certificate_enabled is not None:
            self._values["client_certificate_enabled"] = client_certificate_enabled
        if client_certificate_mode is not None:
            self._values["client_certificate_mode"] = client_certificate_mode
        if connection_string is not None:
            self._values["connection_string"] = connection_string
        if enabled is not None:
            self._values["enabled"] = enabled
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if key_vault_reference_identity_id is not None:
            self._values["key_vault_reference_identity_id"] = key_vault_reference_identity_id
        if logs is not None:
            self._values["logs"] = logs
        if sticky_settings is not None:
            self._values["sticky_settings"] = sticky_settings
        if storage_account is not None:
            self._values["storage_account"] = storage_account
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id
        if zip_deploy_file is not None:
            self._values["zip_deploy_file"] = zip_deploy_file

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#location LinuxWebApp#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#resource_group_name LinuxWebApp#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_plan_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_plan_id LinuxWebApp#service_plan_id}.'''
        result = self._values.get("service_plan_id")
        assert result is not None, "Required property 'service_plan_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_config(self) -> "LinuxWebAppSiteConfig":
        '''site_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#site_config LinuxWebApp#site_config}
        '''
        result = self._values.get("site_config")
        assert result is not None, "Required property 'site_config' is missing"
        return typing.cast("LinuxWebAppSiteConfig", result)

    @builtins.property
    def app_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_settings LinuxWebApp#app_settings}.'''
        result = self._values.get("app_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auth_settings(self) -> typing.Optional[LinuxWebAppAuthSettings]:
        '''auth_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auth_settings LinuxWebApp#auth_settings}
        '''
        result = self._values.get("auth_settings")
        return typing.cast(typing.Optional[LinuxWebAppAuthSettings], result)

    @builtins.property
    def backup(self) -> typing.Optional[LinuxWebAppBackup]:
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#backup LinuxWebApp#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[LinuxWebAppBackup], result)

    @builtins.property
    def client_affinity_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_affinity_enabled LinuxWebApp#client_affinity_enabled}.'''
        result = self._values.get("client_affinity_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_enabled LinuxWebApp#client_certificate_enabled}.'''
        result = self._values.get("client_certificate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#client_certificate_mode LinuxWebApp#client_certificate_mode}.'''
        result = self._values.get("client_certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppConnectionString"]]]:
        '''connection_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string LinuxWebApp#connection_string}
        '''
        result = self._values.get("connection_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppConnectionString"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#enabled LinuxWebApp#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#https_only LinuxWebApp#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#id LinuxWebApp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["LinuxWebAppIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity LinuxWebApp#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["LinuxWebAppIdentity"], result)

    @builtins.property
    def key_vault_reference_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#key_vault_reference_identity_id LinuxWebApp#key_vault_reference_identity_id}.'''
        result = self._values.get("key_vault_reference_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs(self) -> typing.Optional["LinuxWebAppLogs"]:
        '''logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#logs LinuxWebApp#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional["LinuxWebAppLogs"], result)

    @builtins.property
    def sticky_settings(self) -> typing.Optional["LinuxWebAppStickySettings"]:
        '''sticky_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sticky_settings LinuxWebApp#sticky_settings}
        '''
        result = self._values.get("sticky_settings")
        return typing.cast(typing.Optional["LinuxWebAppStickySettings"], result)

    @builtins.property
    def storage_account(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppStorageAccount"]]]:
        '''storage_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#storage_account LinuxWebApp#storage_account}
        '''
        result = self._values.get("storage_account")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppStorageAccount"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#tags LinuxWebApp#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LinuxWebAppTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#timeouts LinuxWebApp#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LinuxWebAppTimeouts"], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_deploy_file(self) -> typing.Optional[builtins.str]:
        '''The local path and filename of the Zip packaged application to deploy to this Windows Web App.

        **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#zip_deploy_file LinuxWebApp#zip_deploy_file}
        '''
        result = self._values.get("zip_deploy_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppConnectionString",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "value": "value"},
)
class LinuxWebAppConnectionString:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: The name which should be used for this Connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}
        :param type: Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}
        :param value: The connection string value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#value LinuxWebApp#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppConnectionString.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The connection string value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#value LinuxWebApp#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppConnectionString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppConnectionStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppConnectionStringList",
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
            type_hints = typing.get_type_hints(LinuxWebAppConnectionStringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LinuxWebAppConnectionStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppConnectionStringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppConnectionStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppConnectionString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppConnectionString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppConnectionString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppConnectionStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppConnectionStringOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppConnectionStringOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppConnectionString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppConnectionString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppConnectionString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppConnectionStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class LinuxWebAppIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity_ids LinuxWebApp#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#identity_ids LinuxWebApp#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppIdentityOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppIdentity]:
        return typing.cast(typing.Optional[LinuxWebAppIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogs",
    jsii_struct_bases=[],
    name_mapping={
        "application_logs": "applicationLogs",
        "detailed_error_messages": "detailedErrorMessages",
        "failed_request_tracing": "failedRequestTracing",
        "http_logs": "httpLogs",
    },
)
class LinuxWebAppLogs:
    def __init__(
        self,
        *,
        application_logs: typing.Optional[typing.Union["LinuxWebAppLogsApplicationLogs", typing.Dict[str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["LinuxWebAppLogsHttpLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_logs LinuxWebApp#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#detailed_error_messages LinuxWebApp#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#failed_request_tracing LinuxWebApp#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http_logs LinuxWebApp#http_logs}
        '''
        if isinstance(application_logs, dict):
            application_logs = LinuxWebAppLogsApplicationLogs(**application_logs)
        if isinstance(http_logs, dict):
            http_logs = LinuxWebAppLogsHttpLogs(**http_logs)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogs.__init__)
            check_type(argname="argument application_logs", value=application_logs, expected_type=type_hints["application_logs"])
            check_type(argname="argument detailed_error_messages", value=detailed_error_messages, expected_type=type_hints["detailed_error_messages"])
            check_type(argname="argument failed_request_tracing", value=failed_request_tracing, expected_type=type_hints["failed_request_tracing"])
            check_type(argname="argument http_logs", value=http_logs, expected_type=type_hints["http_logs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if application_logs is not None:
            self._values["application_logs"] = application_logs
        if detailed_error_messages is not None:
            self._values["detailed_error_messages"] = detailed_error_messages
        if failed_request_tracing is not None:
            self._values["failed_request_tracing"] = failed_request_tracing
        if http_logs is not None:
            self._values["http_logs"] = http_logs

    @builtins.property
    def application_logs(self) -> typing.Optional["LinuxWebAppLogsApplicationLogs"]:
        '''application_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_logs LinuxWebApp#application_logs}
        '''
        result = self._values.get("application_logs")
        return typing.cast(typing.Optional["LinuxWebAppLogsApplicationLogs"], result)

    @builtins.property
    def detailed_error_messages(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#detailed_error_messages LinuxWebApp#detailed_error_messages}.'''
        result = self._values.get("detailed_error_messages")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def failed_request_tracing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#failed_request_tracing LinuxWebApp#failed_request_tracing}.'''
        result = self._values.get("failed_request_tracing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_logs(self) -> typing.Optional["LinuxWebAppLogsHttpLogs"]:
        '''http_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http_logs LinuxWebApp#http_logs}
        '''
        result = self._values.get("http_logs")
        return typing.cast(typing.Optional["LinuxWebAppLogsHttpLogs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsApplicationLogs",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_level": "fileSystemLevel",
        "azure_blob_storage": "azureBlobStorage",
    },
)
class LinuxWebAppLogsApplicationLogs:
    def __init__(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union["LinuxWebAppLogsApplicationLogsAzureBlobStorage", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system_level LinuxWebApp#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = LinuxWebAppLogsApplicationLogsAzureBlobStorage(**azure_blob_storage)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogsApplicationLogs.__init__)
            check_type(argname="argument file_system_level", value=file_system_level, expected_type=type_hints["file_system_level"])
            check_type(argname="argument azure_blob_storage", value=azure_blob_storage, expected_type=type_hints["azure_blob_storage"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_system_level": file_system_level,
        }
        if azure_blob_storage is not None:
            self._values["azure_blob_storage"] = azure_blob_storage

    @builtins.property
    def file_system_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system_level LinuxWebApp#file_system_level}.'''
        result = self._values.get("file_system_level")
        assert result is not None, "Required property 'file_system_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_blob_storage(
        self,
    ) -> typing.Optional["LinuxWebAppLogsApplicationLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["LinuxWebAppLogsApplicationLogsAzureBlobStorage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogsApplicationLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsApplicationLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={
        "level": "level",
        "retention_in_days": "retentionInDays",
        "sas_url": "sasUrl",
    },
)
class LinuxWebAppLogsApplicationLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        level: builtins.str,
        retention_in_days: jsii.Number,
        sas_url: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#level LinuxWebApp#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogsApplicationLogsAzureBlobStorage.__init__)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument sas_url", value=sas_url, expected_type=type_hints["sas_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "level": level,
            "retention_in_days": retention_in_days,
            "sas_url": sas_url,
        }

    @builtins.property
    def level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#level LinuxWebApp#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogsApplicationLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="sasUrlInput")
    def sas_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference, "level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference, "sas_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[LinuxWebAppLogsApplicationLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppLogsApplicationLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppLogsApplicationLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsApplicationLogsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsApplicationLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureBlobStorage")
    def put_azure_blob_storage(
        self,
        *,
        level: builtins.str,
        retention_in_days: jsii.Number,
        sas_url: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#level LinuxWebApp#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.
        '''
        value = LinuxWebAppLogsApplicationLogsAzureBlobStorage(
            level=level, retention_in_days=retention_in_days, sas_url=sas_url
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorage", [value]))

    @jsii.member(jsii_name="resetAzureBlobStorage")
    def reset_azure_blob_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorage", []))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference:
        return typing.cast(LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[LinuxWebAppLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[LinuxWebAppLogsApplicationLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLevelInput")
    def file_system_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLevel")
    def file_system_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemLevel"))

    @file_system_level.setter
    def file_system_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsOutputReference, "file_system_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppLogsApplicationLogs]:
        return typing.cast(typing.Optional[LinuxWebAppLogsApplicationLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppLogsApplicationLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsApplicationLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogs",
    jsii_struct_bases=[],
    name_mapping={
        "azure_blob_storage": "azureBlobStorage",
        "file_system": "fileSystem",
    },
)
class LinuxWebAppLogsHttpLogs:
    def __init__(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union["LinuxWebAppLogsHttpLogsAzureBlobStorage", typing.Dict[str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union["LinuxWebAppLogsHttpLogsFileSystem", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system LinuxWebApp#file_system}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = LinuxWebAppLogsHttpLogsAzureBlobStorage(**azure_blob_storage)
        if isinstance(file_system, dict):
            file_system = LinuxWebAppLogsHttpLogsFileSystem(**file_system)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogs.__init__)
            check_type(argname="argument azure_blob_storage", value=azure_blob_storage, expected_type=type_hints["azure_blob_storage"])
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        self._values: typing.Dict[str, typing.Any] = {}
        if azure_blob_storage is not None:
            self._values["azure_blob_storage"] = azure_blob_storage
        if file_system is not None:
            self._values["file_system"] = file_system

    @builtins.property
    def azure_blob_storage(
        self,
    ) -> typing.Optional["LinuxWebAppLogsHttpLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["LinuxWebAppLogsHttpLogsAzureBlobStorage"], result)

    @builtins.property
    def file_system(self) -> typing.Optional["LinuxWebAppLogsHttpLogsFileSystem"]:
        '''file_system block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system LinuxWebApp#file_system}
        '''
        result = self._values.get("file_system")
        return typing.cast(typing.Optional["LinuxWebAppLogsHttpLogsFileSystem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogsHttpLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={"sas_url": "sasUrl", "retention_in_days": "retentionInDays"},
)
class LinuxWebAppLogsHttpLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        sas_url: builtins.str,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogsAzureBlobStorage.__init__)
            check_type(argname="argument sas_url", value=sas_url, expected_type=type_hints["sas_url"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "sas_url": sas_url,
        }
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogsHttpLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRetentionInDays")
    def reset_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInDays", []))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="sasUrlInput")
    def sas_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference, "sas_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppLogsHttpLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogsFileSystem",
    jsii_struct_bases=[],
    name_mapping={
        "retention_in_days": "retentionInDays",
        "retention_in_mb": "retentionInMb",
    },
)
class LinuxWebAppLogsHttpLogsFileSystem:
    def __init__(
        self,
        *,
        retention_in_days: jsii.Number,
        retention_in_mb: jsii.Number,
    ) -> None:
        '''
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_mb LinuxWebApp#retention_in_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogsFileSystem.__init__)
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument retention_in_mb", value=retention_in_mb, expected_type=type_hints["retention_in_mb"])
        self._values: typing.Dict[str, typing.Any] = {
            "retention_in_days": retention_in_days,
            "retention_in_mb": retention_in_mb,
        }

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retention_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_mb LinuxWebApp#retention_in_mb}.'''
        result = self._values.get("retention_in_mb")
        assert result is not None, "Required property 'retention_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppLogsHttpLogsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppLogsHttpLogsFileSystemOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogsFileSystemOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogsFileSystemOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInMbInput")
    def retention_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsFileSystemOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInMb")
    def retention_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInMb"))

    @retention_in_mb.setter
    def retention_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsFileSystemOutputReference, "retention_in_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogsFileSystem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppLogsHttpLogsFileSystem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsFileSystemOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppLogsHttpLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsHttpLogsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsHttpLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureBlobStorage")
    def put_azure_blob_storage(
        self,
        *,
        sas_url: builtins.str,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sas_url LinuxWebApp#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        '''
        value = LinuxWebAppLogsHttpLogsAzureBlobStorage(
            sas_url=sas_url, retention_in_days=retention_in_days
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorage", [value]))

    @jsii.member(jsii_name="putFileSystem")
    def put_file_system(
        self,
        *,
        retention_in_days: jsii.Number,
        retention_in_mb: jsii.Number,
    ) -> None:
        '''
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_days LinuxWebApp#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#retention_in_mb LinuxWebApp#retention_in_mb}.
        '''
        value = LinuxWebAppLogsHttpLogsFileSystem(
            retention_in_days=retention_in_days, retention_in_mb=retention_in_mb
        )

        return typing.cast(None, jsii.invoke(self, "putFileSystem", [value]))

    @jsii.member(jsii_name="resetAzureBlobStorage")
    def reset_azure_blob_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorage", []))

    @jsii.member(jsii_name="resetFileSystem")
    def reset_file_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystem", []))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference:
        return typing.cast(LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> LinuxWebAppLogsHttpLogsFileSystemOutputReference:
        return typing.cast(LinuxWebAppLogsHttpLogsFileSystemOutputReference, jsii.get(self, "fileSystem"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[LinuxWebAppLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemInput")
    def file_system_input(self) -> typing.Optional[LinuxWebAppLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogsFileSystem], jsii.get(self, "fileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppLogsHttpLogs]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppLogsHttpLogs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsHttpLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppLogsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationLogs")
    def put_application_logs(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union[LinuxWebAppLogsApplicationLogsAzureBlobStorage, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system_level LinuxWebApp#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        '''
        value = LinuxWebAppLogsApplicationLogs(
            file_system_level=file_system_level, azure_blob_storage=azure_blob_storage
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationLogs", [value]))

    @jsii.member(jsii_name="putHttpLogs")
    def put_http_logs(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union[LinuxWebAppLogsHttpLogsAzureBlobStorage, typing.Dict[str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union[LinuxWebAppLogsHttpLogsFileSystem, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#azure_blob_storage LinuxWebApp#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#file_system LinuxWebApp#file_system}
        '''
        value = LinuxWebAppLogsHttpLogs(
            azure_blob_storage=azure_blob_storage, file_system=file_system
        )

        return typing.cast(None, jsii.invoke(self, "putHttpLogs", [value]))

    @jsii.member(jsii_name="resetApplicationLogs")
    def reset_application_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationLogs", []))

    @jsii.member(jsii_name="resetDetailedErrorMessages")
    def reset_detailed_error_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetailedErrorMessages", []))

    @jsii.member(jsii_name="resetFailedRequestTracing")
    def reset_failed_request_tracing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailedRequestTracing", []))

    @jsii.member(jsii_name="resetHttpLogs")
    def reset_http_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpLogs", []))

    @builtins.property
    @jsii.member(jsii_name="applicationLogs")
    def application_logs(self) -> LinuxWebAppLogsApplicationLogsOutputReference:
        return typing.cast(LinuxWebAppLogsApplicationLogsOutputReference, jsii.get(self, "applicationLogs"))

    @builtins.property
    @jsii.member(jsii_name="httpLogs")
    def http_logs(self) -> LinuxWebAppLogsHttpLogsOutputReference:
        return typing.cast(LinuxWebAppLogsHttpLogsOutputReference, jsii.get(self, "httpLogs"))

    @builtins.property
    @jsii.member(jsii_name="applicationLogsInput")
    def application_logs_input(self) -> typing.Optional[LinuxWebAppLogsApplicationLogs]:
        return typing.cast(typing.Optional[LinuxWebAppLogsApplicationLogs], jsii.get(self, "applicationLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorMessagesInput")
    def detailed_error_messages_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "detailedErrorMessagesInput"))

    @builtins.property
    @jsii.member(jsii_name="failedRequestTracingInput")
    def failed_request_tracing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failedRequestTracingInput"))

    @builtins.property
    @jsii.member(jsii_name="httpLogsInput")
    def http_logs_input(self) -> typing.Optional[LinuxWebAppLogsHttpLogs]:
        return typing.cast(typing.Optional[LinuxWebAppLogsHttpLogs], jsii.get(self, "httpLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorMessages")
    def detailed_error_messages(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "detailedErrorMessages"))

    @detailed_error_messages.setter
    def detailed_error_messages(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsOutputReference, "detailed_error_messages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detailedErrorMessages", value)

    @builtins.property
    @jsii.member(jsii_name="failedRequestTracing")
    def failed_request_tracing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failedRequestTracing"))

    @failed_request_tracing.setter
    def failed_request_tracing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsOutputReference, "failed_request_tracing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failedRequestTracing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppLogs]:
        return typing.cast(typing.Optional[LinuxWebAppLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppLogs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfig",
    jsii_struct_bases=[],
    name_mapping={
        "always_on": "alwaysOn",
        "api_definition_url": "apiDefinitionUrl",
        "api_management_api_id": "apiManagementApiId",
        "app_command_line": "appCommandLine",
        "application_stack": "applicationStack",
        "auto_heal_enabled": "autoHealEnabled",
        "auto_heal_setting": "autoHealSetting",
        "container_registry_managed_identity_client_id": "containerRegistryManagedIdentityClientId",
        "container_registry_use_managed_identity": "containerRegistryUseManagedIdentity",
        "cors": "cors",
        "default_documents": "defaultDocuments",
        "ftps_state": "ftpsState",
        "health_check_eviction_time_in_min": "healthCheckEvictionTimeInMin",
        "health_check_path": "healthCheckPath",
        "http2_enabled": "http2Enabled",
        "ip_restriction": "ipRestriction",
        "load_balancing_mode": "loadBalancingMode",
        "local_mysql_enabled": "localMysqlEnabled",
        "managed_pipeline_mode": "managedPipelineMode",
        "minimum_tls_version": "minimumTlsVersion",
        "remote_debugging_enabled": "remoteDebuggingEnabled",
        "remote_debugging_version": "remoteDebuggingVersion",
        "scm_ip_restriction": "scmIpRestriction",
        "scm_minimum_tls_version": "scmMinimumTlsVersion",
        "scm_use_main_ip_restriction": "scmUseMainIpRestriction",
        "use32_bit_worker": "use32BitWorker",
        "vnet_route_all_enabled": "vnetRouteAllEnabled",
        "websockets_enabled": "websocketsEnabled",
        "worker_count": "workerCount",
    },
)
class LinuxWebAppSiteConfig:
    def __init__(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["LinuxWebAppSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSetting", typing.Dict[str, typing.Any]]] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["LinuxWebAppSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#always_on LinuxWebApp#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_definition_url LinuxWebApp#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_management_api_id LinuxWebApp#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_command_line LinuxWebApp#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_stack LinuxWebApp#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_enabled LinuxWebApp#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_setting LinuxWebApp#auto_heal_setting}
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_managed_identity_client_id LinuxWebApp#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_use_managed_identity LinuxWebApp#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#cors LinuxWebApp#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_documents LinuxWebApp#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ftps_state LinuxWebApp#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_eviction_time_in_min LinuxWebApp#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_path LinuxWebApp#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http2_enabled LinuxWebApp#http2_enabled}.
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_restriction LinuxWebApp#ip_restriction}.
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#load_balancing_mode LinuxWebApp#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#local_mysql_enabled LinuxWebApp#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#managed_pipeline_mode LinuxWebApp#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_tls_version LinuxWebApp#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_enabled LinuxWebApp#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_version LinuxWebApp#remote_debugging_version}.
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_ip_restriction LinuxWebApp#scm_ip_restriction}.
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_minimum_tls_version LinuxWebApp#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_use_main_ip_restriction LinuxWebApp#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#use_32_bit_worker LinuxWebApp#use_32_bit_worker}.
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#vnet_route_all_enabled LinuxWebApp#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#websockets_enabled LinuxWebApp#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#worker_count LinuxWebApp#worker_count}.
        '''
        if isinstance(application_stack, dict):
            application_stack = LinuxWebAppSiteConfigApplicationStack(**application_stack)
        if isinstance(auto_heal_setting, dict):
            auto_heal_setting = LinuxWebAppSiteConfigAutoHealSetting(**auto_heal_setting)
        if isinstance(cors, dict):
            cors = LinuxWebAppSiteConfigCors(**cors)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfig.__init__)
            check_type(argname="argument always_on", value=always_on, expected_type=type_hints["always_on"])
            check_type(argname="argument api_definition_url", value=api_definition_url, expected_type=type_hints["api_definition_url"])
            check_type(argname="argument api_management_api_id", value=api_management_api_id, expected_type=type_hints["api_management_api_id"])
            check_type(argname="argument app_command_line", value=app_command_line, expected_type=type_hints["app_command_line"])
            check_type(argname="argument application_stack", value=application_stack, expected_type=type_hints["application_stack"])
            check_type(argname="argument auto_heal_enabled", value=auto_heal_enabled, expected_type=type_hints["auto_heal_enabled"])
            check_type(argname="argument auto_heal_setting", value=auto_heal_setting, expected_type=type_hints["auto_heal_setting"])
            check_type(argname="argument container_registry_managed_identity_client_id", value=container_registry_managed_identity_client_id, expected_type=type_hints["container_registry_managed_identity_client_id"])
            check_type(argname="argument container_registry_use_managed_identity", value=container_registry_use_managed_identity, expected_type=type_hints["container_registry_use_managed_identity"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument default_documents", value=default_documents, expected_type=type_hints["default_documents"])
            check_type(argname="argument ftps_state", value=ftps_state, expected_type=type_hints["ftps_state"])
            check_type(argname="argument health_check_eviction_time_in_min", value=health_check_eviction_time_in_min, expected_type=type_hints["health_check_eviction_time_in_min"])
            check_type(argname="argument health_check_path", value=health_check_path, expected_type=type_hints["health_check_path"])
            check_type(argname="argument http2_enabled", value=http2_enabled, expected_type=type_hints["http2_enabled"])
            check_type(argname="argument ip_restriction", value=ip_restriction, expected_type=type_hints["ip_restriction"])
            check_type(argname="argument load_balancing_mode", value=load_balancing_mode, expected_type=type_hints["load_balancing_mode"])
            check_type(argname="argument local_mysql_enabled", value=local_mysql_enabled, expected_type=type_hints["local_mysql_enabled"])
            check_type(argname="argument managed_pipeline_mode", value=managed_pipeline_mode, expected_type=type_hints["managed_pipeline_mode"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument remote_debugging_enabled", value=remote_debugging_enabled, expected_type=type_hints["remote_debugging_enabled"])
            check_type(argname="argument remote_debugging_version", value=remote_debugging_version, expected_type=type_hints["remote_debugging_version"])
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
        if application_stack is not None:
            self._values["application_stack"] = application_stack
        if auto_heal_enabled is not None:
            self._values["auto_heal_enabled"] = auto_heal_enabled
        if auto_heal_setting is not None:
            self._values["auto_heal_setting"] = auto_heal_setting
        if container_registry_managed_identity_client_id is not None:
            self._values["container_registry_managed_identity_client_id"] = container_registry_managed_identity_client_id
        if container_registry_use_managed_identity is not None:
            self._values["container_registry_use_managed_identity"] = container_registry_use_managed_identity
        if cors is not None:
            self._values["cors"] = cors
        if default_documents is not None:
            self._values["default_documents"] = default_documents
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
        if local_mysql_enabled is not None:
            self._values["local_mysql_enabled"] = local_mysql_enabled
        if managed_pipeline_mode is not None:
            self._values["managed_pipeline_mode"] = managed_pipeline_mode
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if remote_debugging_enabled is not None:
            self._values["remote_debugging_enabled"] = remote_debugging_enabled
        if remote_debugging_version is not None:
            self._values["remote_debugging_version"] = remote_debugging_version
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#always_on LinuxWebApp#always_on}.'''
        result = self._values.get("always_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def api_definition_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_definition_url LinuxWebApp#api_definition_url}.'''
        result = self._values.get("api_definition_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_management_api_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#api_management_api_id LinuxWebApp#api_management_api_id}.'''
        result = self._values.get("api_management_api_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_command_line(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_command_line LinuxWebApp#app_command_line}.'''
        result = self._values.get("app_command_line")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_stack(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigApplicationStack"]:
        '''application_stack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#application_stack LinuxWebApp#application_stack}
        '''
        result = self._values.get("application_stack")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigApplicationStack"], result)

    @builtins.property
    def auto_heal_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_enabled LinuxWebApp#auto_heal_enabled}.'''
        result = self._values.get("auto_heal_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_heal_setting(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSetting"]:
        '''auto_heal_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#auto_heal_setting LinuxWebApp#auto_heal_setting}
        '''
        result = self._values.get("auto_heal_setting")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSetting"], result)

    @builtins.property
    def container_registry_managed_identity_client_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_managed_identity_client_id LinuxWebApp#container_registry_managed_identity_client_id}.'''
        result = self._values.get("container_registry_managed_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#container_registry_use_managed_identity LinuxWebApp#container_registry_use_managed_identity}.'''
        result = self._values.get("container_registry_use_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cors(self) -> typing.Optional["LinuxWebAppSiteConfigCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#cors LinuxWebApp#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigCors"], result)

    @builtins.property
    def default_documents(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#default_documents LinuxWebApp#default_documents}.'''
        result = self._values.get("default_documents")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ftps_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ftps_state LinuxWebApp#ftps_state}.'''
        result = self._values.get("ftps_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_eviction_time_in_min(self) -> typing.Optional[jsii.Number]:
        '''The amount of time in minutes that a node is unhealthy before being removed from the load balancer.

        Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_eviction_time_in_min LinuxWebApp#health_check_eviction_time_in_min}
        '''
        result = self._values.get("health_check_eviction_time_in_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#health_check_path LinuxWebApp#health_check_path}.'''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#http2_enabled LinuxWebApp#http2_enabled}.'''
        result = self._values.get("http2_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_restriction LinuxWebApp#ip_restriction}.'''
        result = self._values.get("ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigIpRestriction"]]], result)

    @builtins.property
    def load_balancing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#load_balancing_mode LinuxWebApp#load_balancing_mode}.'''
        result = self._values.get("load_balancing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_mysql_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#local_mysql_enabled LinuxWebApp#local_mysql_enabled}.'''
        result = self._values.get("local_mysql_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def managed_pipeline_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#managed_pipeline_mode LinuxWebApp#managed_pipeline_mode}.'''
        result = self._values.get("managed_pipeline_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_tls_version LinuxWebApp#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_debugging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_enabled LinuxWebApp#remote_debugging_enabled}.'''
        result = self._values.get("remote_debugging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def remote_debugging_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#remote_debugging_version LinuxWebApp#remote_debugging_version}.'''
        result = self._values.get("remote_debugging_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_ip_restriction LinuxWebApp#scm_ip_restriction}.'''
        result = self._values.get("scm_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestriction"]]], result)

    @builtins.property
    def scm_minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_minimum_tls_version LinuxWebApp#scm_minimum_tls_version}.'''
        result = self._values.get("scm_minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#scm_use_main_ip_restriction LinuxWebApp#scm_use_main_ip_restriction}.'''
        result = self._values.get("scm_use_main_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use32_bit_worker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#use_32_bit_worker LinuxWebApp#use_32_bit_worker}.'''
        result = self._values.get("use32_bit_worker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vnet_route_all_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#vnet_route_all_enabled LinuxWebApp#vnet_route_all_enabled}
        '''
        result = self._values.get("vnet_route_all_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def websockets_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#websockets_enabled LinuxWebApp#websockets_enabled}.'''
        result = self._values.get("websockets_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def worker_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#worker_count LinuxWebApp#worker_count}.'''
        result = self._values.get("worker_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigApplicationStack",
    jsii_struct_bases=[],
    name_mapping={
        "docker_image": "dockerImage",
        "docker_image_tag": "dockerImageTag",
        "dotnet_version": "dotnetVersion",
        "java_server": "javaServer",
        "java_server_version": "javaServerVersion",
        "java_version": "javaVersion",
        "node_version": "nodeVersion",
        "php_version": "phpVersion",
        "python_version": "pythonVersion",
        "ruby_version": "rubyVersion",
    },
)
class LinuxWebAppSiteConfigApplicationStack:
    def __init__(
        self,
        *,
        docker_image: typing.Optional[builtins.str] = None,
        docker_image_tag: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_server: typing.Optional[builtins.str] = None,
        java_server_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
        ruby_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param docker_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image LinuxWebApp#docker_image}.
        :param docker_image_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image_tag LinuxWebApp#docker_image_tag}.
        :param dotnet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#dotnet_version LinuxWebApp#dotnet_version}.
        :param java_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server LinuxWebApp#java_server}.
        :param java_server_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server_version LinuxWebApp#java_server_version}.
        :param java_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_version LinuxWebApp#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#node_version LinuxWebApp#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#php_version LinuxWebApp#php_version}.
        :param python_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#python_version LinuxWebApp#python_version}.
        :param ruby_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ruby_version LinuxWebApp#ruby_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigApplicationStack.__init__)
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument docker_image_tag", value=docker_image_tag, expected_type=type_hints["docker_image_tag"])
            check_type(argname="argument dotnet_version", value=dotnet_version, expected_type=type_hints["dotnet_version"])
            check_type(argname="argument java_server", value=java_server, expected_type=type_hints["java_server"])
            check_type(argname="argument java_server_version", value=java_server_version, expected_type=type_hints["java_server_version"])
            check_type(argname="argument java_version", value=java_version, expected_type=type_hints["java_version"])
            check_type(argname="argument node_version", value=node_version, expected_type=type_hints["node_version"])
            check_type(argname="argument php_version", value=php_version, expected_type=type_hints["php_version"])
            check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
            check_type(argname="argument ruby_version", value=ruby_version, expected_type=type_hints["ruby_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if docker_image_tag is not None:
            self._values["docker_image_tag"] = docker_image_tag
        if dotnet_version is not None:
            self._values["dotnet_version"] = dotnet_version
        if java_server is not None:
            self._values["java_server"] = java_server
        if java_server_version is not None:
            self._values["java_server_version"] = java_server_version
        if java_version is not None:
            self._values["java_version"] = java_version
        if node_version is not None:
            self._values["node_version"] = node_version
        if php_version is not None:
            self._values["php_version"] = php_version
        if python_version is not None:
            self._values["python_version"] = python_version
        if ruby_version is not None:
            self._values["ruby_version"] = ruby_version

    @builtins.property
    def docker_image(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image LinuxWebApp#docker_image}.'''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_image_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image_tag LinuxWebApp#docker_image_tag}.'''
        result = self._values.get("docker_image_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dotnet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#dotnet_version LinuxWebApp#dotnet_version}.'''
        result = self._values.get("dotnet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_server(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server LinuxWebApp#java_server}.'''
        result = self._values.get("java_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_server_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server_version LinuxWebApp#java_server_version}.'''
        result = self._values.get("java_server_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_version LinuxWebApp#java_version}.'''
        result = self._values.get("java_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#node_version LinuxWebApp#node_version}.'''
        result = self._values.get("node_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def php_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#php_version LinuxWebApp#php_version}.'''
        result = self._values.get("php_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def python_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#python_version LinuxWebApp#python_version}.'''
        result = self._values.get("python_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ruby_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ruby_version LinuxWebApp#ruby_version}.'''
        result = self._values.get("ruby_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigApplicationStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigApplicationStackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigApplicationStackOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigApplicationStackOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDockerImage")
    def reset_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImage", []))

    @jsii.member(jsii_name="resetDockerImageTag")
    def reset_docker_image_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImageTag", []))

    @jsii.member(jsii_name="resetDotnetVersion")
    def reset_dotnet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDotnetVersion", []))

    @jsii.member(jsii_name="resetJavaServer")
    def reset_java_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaServer", []))

    @jsii.member(jsii_name="resetJavaServerVersion")
    def reset_java_server_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaServerVersion", []))

    @jsii.member(jsii_name="resetJavaVersion")
    def reset_java_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaVersion", []))

    @jsii.member(jsii_name="resetNodeVersion")
    def reset_node_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeVersion", []))

    @jsii.member(jsii_name="resetPhpVersion")
    def reset_php_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhpVersion", []))

    @jsii.member(jsii_name="resetPythonVersion")
    def reset_python_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonVersion", []))

    @jsii.member(jsii_name="resetRubyVersion")
    def reset_ruby_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRubyVersion", []))

    @builtins.property
    @jsii.member(jsii_name="dockerImageInput")
    def docker_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerImageTagInput")
    def docker_image_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerImageTagInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetVersionInput")
    def dotnet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dotnetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaServerInput")
    def java_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaServerInput"))

    @builtins.property
    @jsii.member(jsii_name="javaServerVersionInput")
    def java_server_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaServerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaVersionInput")
    def java_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeVersionInput")
    def node_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="phpVersionInput")
    def php_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonVersionInput")
    def python_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pythonVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="rubyVersionInput")
    def ruby_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rubyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerImage")
    def docker_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerImage"))

    @docker_image.setter
    def docker_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "docker_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerImage", value)

    @builtins.property
    @jsii.member(jsii_name="dockerImageTag")
    def docker_image_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerImageTag"))

    @docker_image_tag.setter
    def docker_image_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "docker_image_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerImageTag", value)

    @builtins.property
    @jsii.member(jsii_name="dotnetVersion")
    def dotnet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dotnetVersion"))

    @dotnet_version.setter
    def dotnet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "dotnet_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dotnetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaServer")
    def java_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaServer"))

    @java_server.setter
    def java_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "java_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaServer", value)

    @builtins.property
    @jsii.member(jsii_name="javaServerVersion")
    def java_server_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaServerVersion"))

    @java_server_version.setter
    def java_server_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "java_server_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaServerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaVersion")
    def java_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaVersion"))

    @java_version.setter
    def java_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "java_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="nodeVersion")
    def node_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeVersion"))

    @node_version.setter
    def node_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "node_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="phpVersion")
    def php_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phpVersion"))

    @php_version.setter
    def php_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "php_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pythonVersion")
    def python_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pythonVersion"))

    @python_version.setter
    def python_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "python_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonVersion", value)

    @builtins.property
    @jsii.member(jsii_name="rubyVersion")
    def ruby_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rubyVersion"))

    @ruby_version.setter
    def ruby_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "ruby_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rubyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigApplicationStack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigApplicationStack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigApplicationStackOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSetting",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "trigger": "trigger"},
)
class LinuxWebAppSiteConfigAutoHealSetting:
    def __init__(
        self,
        *,
        action: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingAction", typing.Dict[str, typing.Any]]] = None,
        trigger: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#trigger LinuxWebApp#trigger}
        '''
        if isinstance(action, dict):
            action = LinuxWebAppSiteConfigAutoHealSettingAction(**action)
        if isinstance(trigger, dict):
            trigger = LinuxWebAppSiteConfigAutoHealSettingTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSetting.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action(self) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingAction"]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingAction"], result)

    @builtins.property
    def trigger(self) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#trigger LinuxWebApp#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingAction",
    jsii_struct_bases=[],
    name_mapping={
        "action_type": "actionType",
        "minimum_process_execution_time": "minimumProcessExecutionTime",
    },
)
class LinuxWebAppSiteConfigAutoHealSettingAction:
    def __init__(
        self,
        *,
        action_type: builtins.str,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action_type LinuxWebApp#action_type}.
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_process_execution_time LinuxWebApp#minimum_process_execution_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingAction.__init__)
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument minimum_process_execution_time", value=minimum_process_execution_time, expected_type=type_hints["minimum_process_execution_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_type": action_type,
        }
        if minimum_process_execution_time is not None:
            self._values["minimum_process_execution_time"] = minimum_process_execution_time

    @builtins.property
    def action_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action_type LinuxWebApp#action_type}.'''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def minimum_process_execution_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_process_execution_time LinuxWebApp#minimum_process_execution_time}.'''
        result = self._values.get("minimum_process_execution_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSettingAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigAutoHealSettingActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingActionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinimumProcessExecutionTime")
    def reset_minimum_process_execution_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumProcessExecutionTime", []))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumProcessExecutionTimeInput")
    def minimum_process_execution_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumProcessExecutionTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingActionOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="minimumProcessExecutionTime")
    def minimum_process_execution_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumProcessExecutionTime"))

    @minimum_process_execution_time.setter
    def minimum_process_execution_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingActionOutputReference, "minimum_process_execution_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumProcessExecutionTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSettingAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigAutoHealSettingAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigAutoHealSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        action_type: builtins.str,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action_type LinuxWebApp#action_type}.
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#minimum_process_execution_time LinuxWebApp#minimum_process_execution_time}.
        '''
        value = LinuxWebAppSiteConfigAutoHealSettingAction(
            action_type=action_type,
            minimum_process_execution_time=minimum_process_execution_time,
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        requests: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests", typing.Dict[str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param requests: requests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#requests LinuxWebApp#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#slow_request LinuxWebApp#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#status_code LinuxWebApp#status_code}
        '''
        value = LinuxWebAppSiteConfigAutoHealSettingTrigger(
            requests=requests, slow_request=slow_request, status_code=status_code
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> LinuxWebAppSiteConfigAutoHealSettingActionOutputReference:
        return typing.cast(LinuxWebAppSiteConfigAutoHealSettingActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(self) -> "LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference":
        return typing.cast("LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSettingAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTrigger"]:
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigAutoHealSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "requests": "requests",
        "slow_request": "slowRequest",
        "status_code": "statusCode",
    },
)
class LinuxWebAppSiteConfigAutoHealSettingTrigger:
    def __init__(
        self,
        *,
        requests: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests", typing.Dict[str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param requests: requests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#requests LinuxWebApp#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#slow_request LinuxWebApp#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#status_code LinuxWebApp#status_code}
        '''
        if isinstance(requests, dict):
            requests = LinuxWebAppSiteConfigAutoHealSettingTriggerRequests(**requests)
        if isinstance(slow_request, dict):
            slow_request = LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest(**slow_request)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTrigger.__init__)
            check_type(argname="argument requests", value=requests, expected_type=type_hints["requests"])
            check_type(argname="argument slow_request", value=slow_request, expected_type=type_hints["slow_request"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {}
        if requests is not None:
            self._values["requests"] = requests
        if slow_request is not None:
            self._values["slow_request"] = slow_request
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def requests(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests"]:
        '''requests block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#requests LinuxWebApp#requests}
        '''
        result = self._values.get("requests")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests"], result)

    @builtins.property
    def slow_request(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest"]:
        '''slow_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#slow_request LinuxWebApp#slow_request}
        '''
        result = self._values.get("slow_request")
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest"], result)

    @builtins.property
    def status_code(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        '''status_code block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#status_code LinuxWebApp#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSettingTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequests")
    def put_requests(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.
        '''
        value = LinuxWebAppSiteConfigAutoHealSettingTriggerRequests(
            count=count, interval=interval
        )

        return typing.cast(None, jsii.invoke(self, "putRequests", [value]))

    @jsii.member(jsii_name="putSlowRequest")
    def put_slow_request(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        time_taken: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#time_taken LinuxWebApp#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#path LinuxWebApp#path}.
        '''
        value = LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest(
            count=count, interval=interval, time_taken=time_taken, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putSlowRequest", [value]))

    @jsii.member(jsii_name="putStatusCode")
    def put_status_code(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference.put_status_code)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCode", [value]))

    @jsii.member(jsii_name="resetRequests")
    def reset_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequests", []))

    @jsii.member(jsii_name="resetSlowRequest")
    def reset_slow_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowRequest", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="requests")
    def requests(
        self,
    ) -> "LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference":
        return typing.cast("LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference", jsii.get(self, "requests"))

    @builtins.property
    @jsii.member(jsii_name="slowRequest")
    def slow_request(
        self,
    ) -> "LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference":
        return typing.cast("LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference", jsii.get(self, "slowRequest"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(
        self,
    ) -> "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList":
        return typing.cast("LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList", jsii.get(self, "statusCode"))

    @builtins.property
    @jsii.member(jsii_name="requestsInput")
    def requests_input(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests"]:
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerRequests"], jsii.get(self, "requestsInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRequestInput")
    def slow_request_input(
        self,
    ) -> typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest"]:
        return typing.cast(typing.Optional["LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest"], jsii.get(self, "slowRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode"]]], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTrigger]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerRequests",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval": "interval"},
)
class LinuxWebAppSiteConfigAutoHealSettingTriggerRequests:
    def __init__(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerRequests.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval": interval,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSettingTriggerRequests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerRequests]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerRequests], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerRequests],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "time_taken": "timeTaken",
        "path": "path",
    },
)
class LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest:
    def __init__(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        time_taken: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#time_taken LinuxWebApp#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#path LinuxWebApp#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument time_taken", value=time_taken, expected_type=type_hints["time_taken"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval": interval,
            "time_taken": time_taken,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_taken(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#time_taken LinuxWebApp#time_taken}.'''
        result = self._values.get("time_taken")
        assert result is not None, "Required property 'time_taken' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#path LinuxWebApp#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="timeTakenInput")
    def time_taken_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeTakenInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="timeTaken")
    def time_taken(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeTaken"))

    @time_taken.setter
    def time_taken(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "time_taken").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeTaken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "status_code_range": "statusCodeRange",
        "path": "path",
        "sub_status": "subStatus",
        "win32_status": "win32Status",
    },
)
class LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode:
    def __init__(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        status_code_range: builtins.str,
        path: typing.Optional[builtins.str] = None,
        sub_status: typing.Optional[jsii.Number] = None,
        win32_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.
        :param status_code_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#status_code_range LinuxWebApp#status_code_range}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#path LinuxWebApp#path}.
        :param sub_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sub_status LinuxWebApp#sub_status}.
        :param win32_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#win32_status LinuxWebApp#win32_status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument status_code_range", value=status_code_range, expected_type=type_hints["status_code_range"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument sub_status", value=sub_status, expected_type=type_hints["sub_status"])
            check_type(argname="argument win32_status", value=win32_status, expected_type=type_hints["win32_status"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval": interval,
            "status_code_range": status_code_range,
        }
        if path is not None:
            self._values["path"] = path
        if sub_status is not None:
            self._values["sub_status"] = sub_status
        if win32_status is not None:
            self._values["win32_status"] = win32_status

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#count LinuxWebApp#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#interval LinuxWebApp#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#status_code_range LinuxWebApp#status_code_range}.'''
        result = self._values.get("status_code_range")
        assert result is not None, "Required property 'status_code_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#path LinuxWebApp#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_status(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#sub_status LinuxWebApp#sub_status}.'''
        result = self._values.get("sub_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def win32_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#win32_status LinuxWebApp#win32_status}.'''
        result = self._values.get("win32_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSubStatus")
    def reset_sub_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubStatus", []))

    @jsii.member(jsii_name="resetWin32Status")
    def reset_win32_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWin32Status", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRangeInput")
    def status_code_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subStatusInput")
    def sub_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="win32StatusInput")
    def win32_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "win32StatusInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="statusCodeRange")
    def status_code_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCodeRange"))

    @status_code_range.setter
    def status_code_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "status_code_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCodeRange", value)

    @builtins.property
    @jsii.member(jsii_name="subStatus")
    def sub_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subStatus"))

    @sub_status.setter
    def sub_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "sub_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subStatus", value)

    @builtins.property
    @jsii.member(jsii_name="win32Status")
    def win32_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "win32Status"))

    @win32_status.setter
    def win32_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "win32_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "win32Status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigCors",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_origins": "allowedOrigins",
        "support_credentials": "supportCredentials",
    },
)
class LinuxWebAppSiteConfigCors:
    def __init__(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_origins LinuxWebApp#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#support_credentials LinuxWebApp#support_credentials}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigCors.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_origins LinuxWebApp#allowed_origins}
        '''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def support_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Are credentials allowed in CORS requests? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#support_credentials LinuxWebApp#support_credentials}
        '''
        result = self._values.get("support_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigCorsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigCorsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigCorsOutputReference, "allowed_origins").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigCorsOutputReference, "support_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppSiteConfigCors]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppSiteConfigCors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestriction",
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
class LinuxWebAppSiteConfigIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#headers LinuxWebApp#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_address LinuxWebApp#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#priority LinuxWebApp#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_tag LinuxWebApp#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestriction.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#headers LinuxWebApp#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_address LinuxWebApp#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#priority LinuxWebApp#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_tag LinuxWebApp#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class LinuxWebAppSiteConfigIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_azure_fdid LinuxWebApp#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_fd_health_probe LinuxWebApp#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_for LinuxWebApp#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_host LinuxWebApp#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionHeaders.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_azure_fdid LinuxWebApp#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_fd_health_probe LinuxWebApp#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_for LinuxWebApp#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_host LinuxWebApp#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestrictionList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxWebAppSiteConfigIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteConfigIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxWebAppSiteConfigIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigIpRestrictionOutputReference.put_headers)
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
    def headers(self) -> LinuxWebAppSiteConfigIpRestrictionHeadersList:
        return typing.cast(LinuxWebAppSiteConfigIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppSiteConfigIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationStack")
    def put_application_stack(
        self,
        *,
        docker_image: typing.Optional[builtins.str] = None,
        docker_image_tag: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_server: typing.Optional[builtins.str] = None,
        java_server_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
        ruby_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param docker_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image LinuxWebApp#docker_image}.
        :param docker_image_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#docker_image_tag LinuxWebApp#docker_image_tag}.
        :param dotnet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#dotnet_version LinuxWebApp#dotnet_version}.
        :param java_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server LinuxWebApp#java_server}.
        :param java_server_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_server_version LinuxWebApp#java_server_version}.
        :param java_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#java_version LinuxWebApp#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#node_version LinuxWebApp#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#php_version LinuxWebApp#php_version}.
        :param python_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#python_version LinuxWebApp#python_version}.
        :param ruby_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ruby_version LinuxWebApp#ruby_version}.
        '''
        value = LinuxWebAppSiteConfigApplicationStack(
            docker_image=docker_image,
            docker_image_tag=docker_image_tag,
            dotnet_version=dotnet_version,
            java_server=java_server,
            java_server_version=java_server_version,
            java_version=java_version,
            node_version=node_version,
            php_version=php_version,
            python_version=python_version,
            ruby_version=ruby_version,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationStack", [value]))

    @jsii.member(jsii_name="putAutoHealSetting")
    def put_auto_heal_setting(
        self,
        *,
        action: typing.Optional[typing.Union[LinuxWebAppSiteConfigAutoHealSettingAction, typing.Dict[str, typing.Any]]] = None,
        trigger: typing.Optional[typing.Union[LinuxWebAppSiteConfigAutoHealSettingTrigger, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#trigger LinuxWebApp#trigger}
        '''
        value = LinuxWebAppSiteConfigAutoHealSetting(action=action, trigger=trigger)

        return typing.cast(None, jsii.invoke(self, "putAutoHealSetting", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#allowed_origins LinuxWebApp#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#support_credentials LinuxWebApp#support_credentials}
        '''
        value = LinuxWebAppSiteConfigCors(
            allowed_origins=allowed_origins, support_credentials=support_credentials
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putIpRestriction")
    def put_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxWebAppSiteConfigIpRestriction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigOutputReference.put_ip_restriction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpRestriction", [value]))

    @jsii.member(jsii_name="putScmIpRestriction")
    def put_scm_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigOutputReference.put_scm_ip_restriction)
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

    @jsii.member(jsii_name="resetApplicationStack")
    def reset_application_stack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationStack", []))

    @jsii.member(jsii_name="resetAutoHealEnabled")
    def reset_auto_heal_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealEnabled", []))

    @jsii.member(jsii_name="resetAutoHealSetting")
    def reset_auto_heal_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealSetting", []))

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

    @jsii.member(jsii_name="resetLocalMysqlEnabled")
    def reset_local_mysql_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalMysqlEnabled", []))

    @jsii.member(jsii_name="resetManagedPipelineMode")
    def reset_managed_pipeline_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedPipelineMode", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetRemoteDebuggingEnabled")
    def reset_remote_debugging_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingEnabled", []))

    @jsii.member(jsii_name="resetRemoteDebuggingVersion")
    def reset_remote_debugging_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingVersion", []))

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
    def application_stack(self) -> LinuxWebAppSiteConfigApplicationStackOutputReference:
        return typing.cast(LinuxWebAppSiteConfigApplicationStackOutputReference, jsii.get(self, "applicationStack"))

    @builtins.property
    @jsii.member(jsii_name="autoHealSetting")
    def auto_heal_setting(self) -> LinuxWebAppSiteConfigAutoHealSettingOutputReference:
        return typing.cast(LinuxWebAppSiteConfigAutoHealSettingOutputReference, jsii.get(self, "autoHealSetting"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> LinuxWebAppSiteConfigCorsOutputReference:
        return typing.cast(LinuxWebAppSiteConfigCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorLoggingEnabled")
    def detailed_error_logging_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "detailedErrorLoggingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="ipRestriction")
    def ip_restriction(self) -> LinuxWebAppSiteConfigIpRestrictionList:
        return typing.cast(LinuxWebAppSiteConfigIpRestrictionList, jsii.get(self, "ipRestriction"))

    @builtins.property
    @jsii.member(jsii_name="linuxFxVersion")
    def linux_fx_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linuxFxVersion"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestriction")
    def scm_ip_restriction(self) -> "LinuxWebAppSiteConfigScmIpRestrictionList":
        return typing.cast("LinuxWebAppSiteConfigScmIpRestrictionList", jsii.get(self, "scmIpRestriction"))

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
    @jsii.member(jsii_name="applicationStackInput")
    def application_stack_input(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigApplicationStack], jsii.get(self, "applicationStackInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealEnabledInput")
    def auto_heal_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHealEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealSettingInput")
    def auto_heal_setting_input(
        self,
    ) -> typing.Optional[LinuxWebAppSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigAutoHealSetting], jsii.get(self, "autoHealSettingInput"))

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
    def cors_input(self) -> typing.Optional[LinuxWebAppSiteConfigCors]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfigCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDocumentsInput")
    def default_documents_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultDocumentsInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigIpRestriction]]], jsii.get(self, "ipRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingModeInput")
    def load_balancing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="localMysqlEnabledInput")
    def local_mysql_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localMysqlEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPipelineModeInput")
    def managed_pipeline_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPipelineModeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

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
    @jsii.member(jsii_name="scmIpRestrictionInput")
    def scm_ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestriction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestriction"]]], jsii.get(self, "scmIpRestrictionInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "always_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysOn", value)

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrl")
    def api_definition_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiDefinitionUrl"))

    @api_definition_url.setter
    def api_definition_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "api_definition_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiDefinitionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiId")
    def api_management_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementApiId"))

    @api_management_api_id.setter
    def api_management_api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "api_management_api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementApiId", value)

    @builtins.property
    @jsii.member(jsii_name="appCommandLine")
    def app_command_line(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appCommandLine"))

    @app_command_line.setter
    def app_command_line(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "app_command_line").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appCommandLine", value)

    @builtins.property
    @jsii.member(jsii_name="autoHealEnabled")
    def auto_heal_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoHealEnabled"))

    @auto_heal_enabled.setter
    def auto_heal_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "auto_heal_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "container_registry_managed_identity_client_id").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "container_registry_use_managed_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryUseManagedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDocuments")
    def default_documents(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultDocuments"))

    @default_documents.setter
    def default_documents(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "default_documents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="ftpsState")
    def ftps_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ftpsState"))

    @ftps_state.setter
    def ftps_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "ftps_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ftpsState", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMin")
    def health_check_eviction_time_in_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckEvictionTimeInMin"))

    @health_check_eviction_time_in_min.setter
    def health_check_eviction_time_in_min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "health_check_eviction_time_in_min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEvictionTimeInMin", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "health_check_path").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "http2_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMode")
    def load_balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingMode"))

    @load_balancing_mode.setter
    def load_balancing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "load_balancing_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingMode", value)

    @builtins.property
    @jsii.member(jsii_name="localMysqlEnabled")
    def local_mysql_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localMysqlEnabled"))

    @local_mysql_enabled.setter
    def local_mysql_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "local_mysql_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMysqlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="managedPipelineMode")
    def managed_pipeline_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPipelineMode"))

    @managed_pipeline_mode.setter
    def managed_pipeline_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "managed_pipeline_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPipelineMode", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "remote_debugging_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersion")
    def remote_debugging_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteDebuggingVersion"))

    @remote_debugging_version.setter
    def remote_debugging_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "remote_debugging_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersion")
    def scm_minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmMinimumTlsVersion"))

    @scm_minimum_tls_version.setter
    def scm_minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "scm_minimum_tls_version").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "scm_use_main_ip_restriction").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "use32_bit_worker").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "vnet_route_all_enabled").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "websockets_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websocketsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "worker_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppSiteConfig]:
        return typing.cast(typing.Optional[LinuxWebAppSiteConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppSiteConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestriction",
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
class LinuxWebAppSiteConfigScmIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxWebAppSiteConfigScmIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#headers LinuxWebApp#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_address LinuxWebApp#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#priority LinuxWebApp#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_tag LinuxWebApp#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestriction.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#action LinuxWebApp#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#headers LinuxWebApp#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxWebAppSiteConfigScmIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#ip_address LinuxWebApp#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#priority LinuxWebApp#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#service_tag LinuxWebApp#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#virtual_network_subnet_id LinuxWebApp#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigScmIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class LinuxWebAppSiteConfigScmIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_azure_fdid LinuxWebApp#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_fd_health_probe LinuxWebApp#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_for LinuxWebApp#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_host LinuxWebApp#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionHeaders.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_azure_fdid LinuxWebApp#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_fd_health_probe LinuxWebApp#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_for LinuxWebApp#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#x_forwarded_host LinuxWebApp#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteConfigScmIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteConfigScmIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigScmIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestrictionList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxWebAppSiteConfigScmIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteConfigScmIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppSiteConfigScmIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteConfigScmIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxWebAppSiteConfigScmIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteConfigScmIpRestrictionOutputReference.put_headers)
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
    def headers(self) -> LinuxWebAppSiteConfigScmIpRestrictionHeadersList:
        return typing.cast(LinuxWebAppSiteConfigScmIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppSiteConfigScmIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteConfigScmIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteCredential",
    jsii_struct_bases=[],
    name_mapping={},
)
class LinuxWebAppSiteCredential:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppSiteCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppSiteCredentialList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteCredentialList",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteCredentialList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LinuxWebAppSiteCredentialOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppSiteCredentialList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppSiteCredentialOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteCredentialList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteCredentialList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteCredentialList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class LinuxWebAppSiteCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppSiteCredentialOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppSiteCredentialOutputReference.__init__)
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
    def internal_value(self) -> typing.Optional[LinuxWebAppSiteCredential]:
        return typing.cast(typing.Optional[LinuxWebAppSiteCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppSiteCredential]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppSiteCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppStickySettings",
    jsii_struct_bases=[],
    name_mapping={
        "app_setting_names": "appSettingNames",
        "connection_string_names": "connectionStringNames",
    },
)
class LinuxWebAppStickySettings:
    def __init__(
        self,
        *,
        app_setting_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_string_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_setting_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_setting_names LinuxWebApp#app_setting_names}.
        :param connection_string_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string_names LinuxWebApp#connection_string_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppStickySettings.__init__)
            check_type(argname="argument app_setting_names", value=app_setting_names, expected_type=type_hints["app_setting_names"])
            check_type(argname="argument connection_string_names", value=connection_string_names, expected_type=type_hints["connection_string_names"])
        self._values: typing.Dict[str, typing.Any] = {}
        if app_setting_names is not None:
            self._values["app_setting_names"] = app_setting_names
        if connection_string_names is not None:
            self._values["connection_string_names"] = connection_string_names

    @builtins.property
    def app_setting_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#app_setting_names LinuxWebApp#app_setting_names}.'''
        result = self._values.get("app_setting_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_string_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#connection_string_names LinuxWebApp#connection_string_names}.'''
        result = self._values.get("connection_string_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppStickySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppStickySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppStickySettingsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppStickySettingsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStickySettingsOutputReference, "app_setting_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSettingNames", value)

    @builtins.property
    @jsii.member(jsii_name="connectionStringNames")
    def connection_string_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectionStringNames"))

    @connection_string_names.setter
    def connection_string_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStickySettingsOutputReference, "connection_string_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionStringNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxWebAppStickySettings]:
        return typing.cast(typing.Optional[LinuxWebAppStickySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxWebAppStickySettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStickySettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppStorageAccount",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "account_name": "accountName",
        "name": "name",
        "share_name": "shareName",
        "type": "type",
        "mount_path": "mountPath",
    },
)
class LinuxWebAppStorageAccount:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        account_name: builtins.str,
        name: builtins.str,
        share_name: builtins.str,
        type: builtins.str,
        mount_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#access_key LinuxWebApp#access_key}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#account_name LinuxWebApp#account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.
        :param share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#share_name LinuxWebApp#share_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}.
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#mount_path LinuxWebApp#mount_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppStorageAccount.__init__)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_key": access_key,
            "account_name": account_name,
            "name": name,
            "share_name": share_name,
            "type": type,
        }
        if mount_path is not None:
            self._values["mount_path"] = mount_path

    @builtins.property
    def access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#access_key LinuxWebApp#access_key}.'''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#account_name LinuxWebApp#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#name LinuxWebApp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#share_name LinuxWebApp#share_name}.'''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#type LinuxWebApp#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#mount_path LinuxWebApp#mount_path}.'''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppStorageAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppStorageAccountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppStorageAccountList",
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
            type_hints = typing.get_type_hints(LinuxWebAppStorageAccountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LinuxWebAppStorageAccountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppStorageAccountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxWebAppStorageAccountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppStorageAccount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppStorageAccount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxWebAppStorageAccount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxWebAppStorageAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppStorageAccountOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppStorageAccountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountPath")
    def reset_mount_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountPath", []))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppStorageAccount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppStorageAccount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppStorageAccount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppStorageAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LinuxWebAppTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#create LinuxWebApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#delete LinuxWebApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#read LinuxWebApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#update LinuxWebApp#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxWebAppTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#create LinuxWebApp#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#delete LinuxWebApp#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#read LinuxWebApp#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/linux_web_app#update LinuxWebApp#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxWebAppTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxWebAppTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.linuxWebApp.LinuxWebAppTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxWebAppTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxWebAppTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxWebAppTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxWebAppTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxWebAppTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxWebAppTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LinuxWebApp",
    "LinuxWebAppAuthSettings",
    "LinuxWebAppAuthSettingsActiveDirectory",
    "LinuxWebAppAuthSettingsActiveDirectoryOutputReference",
    "LinuxWebAppAuthSettingsFacebook",
    "LinuxWebAppAuthSettingsFacebookOutputReference",
    "LinuxWebAppAuthSettingsGithub",
    "LinuxWebAppAuthSettingsGithubOutputReference",
    "LinuxWebAppAuthSettingsGoogle",
    "LinuxWebAppAuthSettingsGoogleOutputReference",
    "LinuxWebAppAuthSettingsMicrosoft",
    "LinuxWebAppAuthSettingsMicrosoftOutputReference",
    "LinuxWebAppAuthSettingsOutputReference",
    "LinuxWebAppAuthSettingsTwitter",
    "LinuxWebAppAuthSettingsTwitterOutputReference",
    "LinuxWebAppBackup",
    "LinuxWebAppBackupOutputReference",
    "LinuxWebAppBackupSchedule",
    "LinuxWebAppBackupScheduleOutputReference",
    "LinuxWebAppConfig",
    "LinuxWebAppConnectionString",
    "LinuxWebAppConnectionStringList",
    "LinuxWebAppConnectionStringOutputReference",
    "LinuxWebAppIdentity",
    "LinuxWebAppIdentityOutputReference",
    "LinuxWebAppLogs",
    "LinuxWebAppLogsApplicationLogs",
    "LinuxWebAppLogsApplicationLogsAzureBlobStorage",
    "LinuxWebAppLogsApplicationLogsAzureBlobStorageOutputReference",
    "LinuxWebAppLogsApplicationLogsOutputReference",
    "LinuxWebAppLogsHttpLogs",
    "LinuxWebAppLogsHttpLogsAzureBlobStorage",
    "LinuxWebAppLogsHttpLogsAzureBlobStorageOutputReference",
    "LinuxWebAppLogsHttpLogsFileSystem",
    "LinuxWebAppLogsHttpLogsFileSystemOutputReference",
    "LinuxWebAppLogsHttpLogsOutputReference",
    "LinuxWebAppLogsOutputReference",
    "LinuxWebAppSiteConfig",
    "LinuxWebAppSiteConfigApplicationStack",
    "LinuxWebAppSiteConfigApplicationStackOutputReference",
    "LinuxWebAppSiteConfigAutoHealSetting",
    "LinuxWebAppSiteConfigAutoHealSettingAction",
    "LinuxWebAppSiteConfigAutoHealSettingActionOutputReference",
    "LinuxWebAppSiteConfigAutoHealSettingOutputReference",
    "LinuxWebAppSiteConfigAutoHealSettingTrigger",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerOutputReference",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerRequests",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerRequestsOutputReference",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequest",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCode",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeList",
    "LinuxWebAppSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
    "LinuxWebAppSiteConfigCors",
    "LinuxWebAppSiteConfigCorsOutputReference",
    "LinuxWebAppSiteConfigIpRestriction",
    "LinuxWebAppSiteConfigIpRestrictionHeaders",
    "LinuxWebAppSiteConfigIpRestrictionHeadersList",
    "LinuxWebAppSiteConfigIpRestrictionHeadersOutputReference",
    "LinuxWebAppSiteConfigIpRestrictionList",
    "LinuxWebAppSiteConfigIpRestrictionOutputReference",
    "LinuxWebAppSiteConfigOutputReference",
    "LinuxWebAppSiteConfigScmIpRestriction",
    "LinuxWebAppSiteConfigScmIpRestrictionHeaders",
    "LinuxWebAppSiteConfigScmIpRestrictionHeadersList",
    "LinuxWebAppSiteConfigScmIpRestrictionHeadersOutputReference",
    "LinuxWebAppSiteConfigScmIpRestrictionList",
    "LinuxWebAppSiteConfigScmIpRestrictionOutputReference",
    "LinuxWebAppSiteCredential",
    "LinuxWebAppSiteCredentialList",
    "LinuxWebAppSiteCredentialOutputReference",
    "LinuxWebAppStickySettings",
    "LinuxWebAppStickySettingsOutputReference",
    "LinuxWebAppStorageAccount",
    "LinuxWebAppStorageAccountList",
    "LinuxWebAppStorageAccountOutputReference",
    "LinuxWebAppTimeouts",
    "LinuxWebAppTimeoutsOutputReference",
]

publication.publish()
