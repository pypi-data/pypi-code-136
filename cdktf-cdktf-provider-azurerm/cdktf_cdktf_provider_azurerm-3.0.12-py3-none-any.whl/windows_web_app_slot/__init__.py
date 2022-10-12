'''
# `azurerm_windows_web_app_slot`

Refer to the Terraform Registory for docs: [`azurerm_windows_web_app_slot`](https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot).
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


class WindowsWebAppSlot(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot azurerm_windows_web_app_slot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        app_service_id: builtins.str,
        name: builtins.str,
        site_config: typing.Union["WindowsWebAppSlotSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettings", typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union["WindowsWebAppSlotBackup", typing.Dict[str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsWebAppSlotIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["WindowsWebAppSlotLogs", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot azurerm_windows_web_app_slot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#id WindowsWebAppSlot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#tags WindowsWebAppSlot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WindowsWebAppSlotConfig(
            app_service_id=app_service_id,
            name=name,
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
        active_directory: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#github WindowsWebAppSlot#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#google WindowsWebAppSlot#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        value = WindowsWebAppSlotAuthSettings(
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
        schedule: typing.Union["WindowsWebAppSlotBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        value = WindowsWebAppSlotBackup(
            name=name,
            schedule=schedule,
            storage_account_url=storage_account_url,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putConnectionString")
    def put_connection_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlot.put_connection_string)
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
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.
        '''
        value = WindowsWebAppSlotIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putLogs")
    def put_logs(
        self,
        *,
        application_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogs", typing.Dict[str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        value = WindowsWebAppSlotLogs(
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
        application_stack: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSetting", typing.Dict[str, typing.Any]]] = None,
        auto_swap_slot_name: typing.Optional[builtins.str] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        virtual_application: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[str, typing.Any]]]]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        :param auto_swap_slot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}.
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}.
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.
        :param virtual_application: virtual_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.
        '''
        value = WindowsWebAppSlotSiteConfig(
            always_on=always_on,
            api_definition_url=api_definition_url,
            api_management_api_id=api_management_api_id,
            app_command_line=app_command_line,
            application_stack=application_stack,
            auto_heal_enabled=auto_heal_enabled,
            auto_heal_setting=auto_heal_setting,
            auto_swap_slot_name=auto_swap_slot_name,
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
            virtual_application=virtual_application,
            vnet_route_all_enabled=vnet_route_all_enabled,
            websockets_enabled=websockets_enabled,
            worker_count=worker_count,
        )

        return typing.cast(None, jsii.invoke(self, "putSiteConfig", [value]))

    @jsii.member(jsii_name="putStorageAccount")
    def put_storage_account(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlot.put_storage_account)
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#create WindowsWebAppSlot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#delete WindowsWebAppSlot#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#read WindowsWebAppSlot#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#update WindowsWebAppSlot#update}.
        '''
        value = WindowsWebAppSlotTimeouts(
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
    def auth_settings(self) -> "WindowsWebAppSlotAuthSettingsOutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsOutputReference", jsii.get(self, "authSettings"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "WindowsWebAppSlotBackupOutputReference":
        return typing.cast("WindowsWebAppSlotBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> "WindowsWebAppSlotConnectionStringList":
        return typing.cast("WindowsWebAppSlotConnectionStringList", jsii.get(self, "connectionString"))

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
    def identity(self) -> "WindowsWebAppSlotIdentityOutputReference":
        return typing.cast("WindowsWebAppSlotIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> "WindowsWebAppSlotLogsOutputReference":
        return typing.cast("WindowsWebAppSlotLogsOutputReference", jsii.get(self, "logs"))

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
    def site_config(self) -> "WindowsWebAppSlotSiteConfigOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigOutputReference", jsii.get(self, "siteConfig"))

    @builtins.property
    @jsii.member(jsii_name="siteCredential")
    def site_credential(self) -> "WindowsWebAppSlotSiteCredentialList":
        return typing.cast("WindowsWebAppSlotSiteCredentialList", jsii.get(self, "siteCredential"))

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> "WindowsWebAppSlotStorageAccountList":
        return typing.cast("WindowsWebAppSlotStorageAccountList", jsii.get(self, "storageAccount"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WindowsWebAppSlotTimeoutsOutputReference":
        return typing.cast("WindowsWebAppSlotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appServiceIdInput")
    def app_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSettingsInput")
    def app_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "appSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsInput")
    def auth_settings_input(self) -> typing.Optional["WindowsWebAppSlotAuthSettings"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettings"], jsii.get(self, "authSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["WindowsWebAppSlotBackup"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotBackup"], jsii.get(self, "backupInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]], jsii.get(self, "connectionStringInput"))

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
    def identity_input(self) -> typing.Optional["WindowsWebAppSlotIdentity"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityIdInput")
    def key_vault_reference_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultReferenceIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInput")
    def logs_input(self) -> typing.Optional["WindowsWebAppSlotLogs"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotLogs"], jsii.get(self, "logsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="siteConfigInput")
    def site_config_input(self) -> typing.Optional["WindowsWebAppSlotSiteConfig"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfig"], jsii.get(self, "siteConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="zipDeployFileInput")
    def zip_deploy_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipDeployFileInput"))

    @builtins.property
    @jsii.member(jsii_name="appServiceId")
    def app_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appServiceId"))

    @app_service_id.setter
    def app_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "app_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="appSettings")
    def app_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "appSettings"))

    @app_settings.setter
    def app_settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "app_settings").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "client_affinity_enabled").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "client_certificate_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateMode")
    def client_certificate_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateMode"))

    @client_certificate_mode.setter
    def client_certificate_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "client_certificate_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityId")
    def key_vault_reference_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultReferenceIdentityId"))

    @key_vault_reference_identity_id.setter
    def key_vault_reference_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "key_vault_reference_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultReferenceIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="zipDeployFile")
    def zip_deploy_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipDeployFile"))

    @zip_deploy_file.setter
    def zip_deploy_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlot, "zip_deploy_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipDeployFile", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettings",
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
class WindowsWebAppSlotAuthSettings:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        active_directory: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsFacebook", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGithub", typing.Dict[str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGoogle", typing.Dict[str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsMicrosoft", typing.Dict[str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsTwitter", typing.Dict[str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#github WindowsWebAppSlot#github}
        :param google: google block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#google WindowsWebAppSlot#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        if isinstance(active_directory, dict):
            active_directory = WindowsWebAppSlotAuthSettingsActiveDirectory(**active_directory)
        if isinstance(facebook, dict):
            facebook = WindowsWebAppSlotAuthSettingsFacebook(**facebook)
        if isinstance(github, dict):
            github = WindowsWebAppSlotAuthSettingsGithub(**github)
        if isinstance(google, dict):
            google = WindowsWebAppSlotAuthSettingsGoogle(**google)
        if isinstance(microsoft, dict):
            microsoft = WindowsWebAppSlotAuthSettingsMicrosoft(**microsoft)
        if isinstance(twitter, dict):
            twitter = WindowsWebAppSlotAuthSettingsTwitter(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettings.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsActiveDirectory"], result)

    @builtins.property
    def additional_login_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        '''
        result = self._values.get("additional_login_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def allowed_external_redirect_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        '''
        result = self._values.get("allowed_external_redirect_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_provider(self) -> typing.Optional[builtins.str]:
        '''The default authentication provider to use when multiple providers are configured.

        Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        '''
        result = self._values.get("default_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facebook(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsFacebook"]:
        '''facebook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        '''
        result = self._values.get("facebook")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsFacebook"], result)

    @builtins.property
    def github(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#github WindowsWebAppSlot#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsGithub"], result)

    @builtins.property
    def google(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsGoogle"]:
        '''google block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#google WindowsWebAppSlot#google}
        '''
        result = self._values.get("google")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsGoogle"], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''The OpenID Connect Issuer URI that represents the entity which issues access tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsMicrosoft"]:
        '''microsoft block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        '''
        result = self._values.get("microsoft")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsMicrosoft"], result)

    @builtins.property
    def runtime_version(self) -> typing.Optional[builtins.str]:
        '''The RuntimeVersion of the Authentication / Authorization feature in use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        '''
        result = self._values.get("runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_refresh_extension_hours(self) -> typing.Optional[jsii.Number]:
        '''The number of hours after session token expiration that a session token can be used to call the token refresh API.

        Defaults to ``72`` hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        '''
        result = self._values.get("token_refresh_extension_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_store_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        '''
        result = self._values.get("token_store_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def twitter(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"]:
        '''twitter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"], result)

    @builtins.property
    def unauthenticated_client_action(self) -> typing.Optional[builtins.str]:
        '''The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        result = self._values.get("unauthenticated_client_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "allowed_audiences": "allowedAudiences",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsActiveDirectory:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsActiveDirectory.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, "allowed_audiences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsFacebook",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "app_secret": "appSecret",
        "app_secret_setting_name": "appSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsFacebook:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsFacebook.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_secret(self) -> typing.Optional[builtins.str]:
        '''The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        '''
        result = self._values.get("app_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        '''
        result = self._values.get("app_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsFacebook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsFacebookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsFacebookOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsFacebookOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsFacebookOutputReference, "app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="appSecret")
    def app_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecret"))

    @app_secret.setter
    def app_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsFacebookOutputReference, "app_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecret", value)

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingName")
    def app_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecretSettingName"))

    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsFacebookOutputReference, "app_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsFacebookOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsFacebook]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsFacebook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsFacebook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsFacebookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGithub",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsGithub:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsGithub.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGithubOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsGithubOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGithubOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGithubOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGithubOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGithubOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGithub]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsGithub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGoogle",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsGoogle:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsGoogle.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The client secret associated with the Google web application.  Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsGoogle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsGoogleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGoogleOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsGoogleOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGoogleOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGoogleOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGoogleOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGoogleOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGoogle]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGoogle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsGoogle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsGoogleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsMicrosoft",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsMicrosoft:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsMicrosoft.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsMicrosoft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsMicrosoftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsMicrosoftOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, "client_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, "oauth_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotAuthSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsOutputReference.__init__)
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
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsActiveDirectory(
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
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsFacebook(
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
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsGithub(
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
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsGoogle(
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
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsMicrosoft(
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
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsTwitter(
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
    ) -> WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="facebook")
    def facebook(self) -> WindowsWebAppSlotAuthSettingsFacebookOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsFacebookOutputReference, jsii.get(self, "facebook"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> WindowsWebAppSlotAuthSettingsGithubOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="google")
    def google(self) -> WindowsWebAppSlotAuthSettingsGoogleOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsGoogleOutputReference, jsii.get(self, "google"))

    @builtins.property
    @jsii.member(jsii_name="microsoft")
    def microsoft(self) -> WindowsWebAppSlotAuthSettingsMicrosoftOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, jsii.get(self, "microsoft"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> "WindowsWebAppSlotAuthSettingsTwitterOutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsTwitterOutputReference", jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory], jsii.get(self, "activeDirectoryInput"))

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
    def facebook_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsFacebook]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsFacebook], jsii.get(self, "facebookInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGithub]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="googleInput")
    def google_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGoogle]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGoogle], jsii.get(self, "googleInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftInput")
    def microsoft_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft], jsii.get(self, "microsoftInput"))

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
    def twitter_input(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"], jsii.get(self, "twitterInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "additional_login_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalLoginParameters", value)

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedExternalRedirectUrls"))

    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "allowed_external_redirect_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExternalRedirectUrls", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProvider")
    def default_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProvider"))

    @default_provider.setter
    def default_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "default_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProvider", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "runtime_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenRefreshExtensionHours"))

    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "token_refresh_extension_hours").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "token_store_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthenticatedClientAction"))

    @unauthenticated_client_action.setter
    def unauthenticated_client_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "unauthenticated_client_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticatedClientAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettings]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsTwitter",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_key": "consumerKey",
        "consumer_secret": "consumerSecret",
        "consumer_secret_setting_name": "consumerSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsTwitter:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsTwitter.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        '''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        '''
        result = self._values.get("consumer_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consumer_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        result = self._values.get("consumer_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsTwitter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsTwitterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsTwitterOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotAuthSettingsTwitterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsTwitterOutputReference, "consumer_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerKey", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecret")
    def consumer_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecret"))

    @consumer_secret.setter
    def consumer_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsTwitterOutputReference, "consumer_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecretSettingName"))

    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsTwitterOutputReference, "consumer_secret_setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsTwitter]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsTwitter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsTwitter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotAuthSettingsTwitterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackup",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schedule": "schedule",
        "storage_account_url": "storageAccountUrl",
        "enabled": "enabled",
    },
)
class WindowsWebAppSlotBackup:
    def __init__(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["WindowsWebAppSlotBackupSchedule", typing.Dict[str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        if isinstance(schedule, dict):
            schedule = WindowsWebAppSlotBackupSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotBackup.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "WindowsWebAppSlotBackupSchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("WindowsWebAppSlotBackupSchedule", result)

    @builtins.property
    def storage_account_url(self) -> builtins.str:
        '''The SAS URL to the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        '''
        result = self._values.get("storage_account_url")
        assert result is not None, "Required property 'storage_account_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should this backup job be enabled?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotBackupOutputReference.__init__)
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
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        value = WindowsWebAppSlotBackupSchedule(
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
    def schedule(self) -> "WindowsWebAppSlotBackupScheduleOutputReference":
        return typing.cast("WindowsWebAppSlotBackupScheduleOutputReference", jsii.get(self, "schedule"))

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
    def schedule_input(self) -> typing.Optional["WindowsWebAppSlotBackupSchedule"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotBackupSchedule"], jsii.get(self, "scheduleInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrl")
    def storage_account_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUrl"))

    @storage_account_url.setter
    def storage_account_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupOutputReference, "storage_account_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotBackup]:
        return typing.cast(typing.Optional[WindowsWebAppSlotBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "frequency_interval": "frequencyInterval",
        "frequency_unit": "frequencyUnit",
        "keep_at_least_one_backup": "keepAtLeastOneBackup",
        "retention_period_days": "retentionPeriodDays",
        "start_time": "startTime",
    },
)
class WindowsWebAppSlotBackupSchedule:
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
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotBackupSchedule.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        '''
        result = self._values.get("frequency_interval")
        assert result is not None, "Required property 'frequency_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frequency_unit(self) -> builtins.str:
        '''The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        '''
        result = self._values.get("frequency_unit")
        assert result is not None, "Required property 'frequency_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keep_at_least_one_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        '''
        result = self._values.get("keep_at_least_one_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_period_days(self) -> typing.Optional[jsii.Number]:
        '''After how many days backups should be deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        '''
        result = self._values.get("retention_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''When the schedule should start working in RFC-3339 format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotBackupSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotBackupScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupScheduleOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotBackupScheduleOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "frequency_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="frequencyUnit")
    def frequency_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequencyUnit"))

    @frequency_unit.setter
    def frequency_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "frequency_unit").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "keep_at_least_one_backup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAtLeastOneBackup", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDays")
    def retention_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodDays"))

    @retention_period_days.setter
    def retention_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "retention_period_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotBackupSchedule]:
        return typing.cast(typing.Optional[WindowsWebAppSlotBackupSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotBackupSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotBackupScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_service_id": "appServiceId",
        "name": "name",
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
        "storage_account": "storageAccount",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
        "zip_deploy_file": "zipDeployFile",
    },
)
class WindowsWebAppSlotConfig(cdktf.TerraformMetaArguments):
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
        app_service_id: builtins.str,
        name: builtins.str,
        site_config: typing.Union["WindowsWebAppSlotSiteConfig", typing.Dict[str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettings, typing.Dict[str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union[WindowsWebAppSlotBackup, typing.Dict[str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsWebAppSlotIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["WindowsWebAppSlotLogs", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param app_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#id WindowsWebAppSlot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#tags WindowsWebAppSlot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(site_config, dict):
            site_config = WindowsWebAppSlotSiteConfig(**site_config)
        if isinstance(auth_settings, dict):
            auth_settings = WindowsWebAppSlotAuthSettings(**auth_settings)
        if isinstance(backup, dict):
            backup = WindowsWebAppSlotBackup(**backup)
        if isinstance(identity, dict):
            identity = WindowsWebAppSlotIdentity(**identity)
        if isinstance(logs, dict):
            logs = WindowsWebAppSlotLogs(**logs)
        if isinstance(timeouts, dict):
            timeouts = WindowsWebAppSlotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_service_id", value=app_service_id, expected_type=type_hints["app_service_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
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
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
            check_type(argname="argument zip_deploy_file", value=zip_deploy_file, expected_type=type_hints["zip_deploy_file"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_service_id": app_service_id,
            "name": name,
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
    def app_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.'''
        result = self._values.get("app_service_id")
        assert result is not None, "Required property 'app_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_config(self) -> "WindowsWebAppSlotSiteConfig":
        '''site_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        '''
        result = self._values.get("site_config")
        assert result is not None, "Required property 'site_config' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfig", result)

    @builtins.property
    def app_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.'''
        result = self._values.get("app_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auth_settings(self) -> typing.Optional[WindowsWebAppSlotAuthSettings]:
        '''auth_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        '''
        result = self._values.get("auth_settings")
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettings], result)

    @builtins.property
    def backup(self) -> typing.Optional[WindowsWebAppSlotBackup]:
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[WindowsWebAppSlotBackup], result)

    @builtins.property
    def client_affinity_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.'''
        result = self._values.get("client_affinity_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.'''
        result = self._values.get("client_certificate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.'''
        result = self._values.get("client_certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]]:
        '''connection_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        '''
        result = self._values.get("connection_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#id WindowsWebAppSlot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["WindowsWebAppSlotIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["WindowsWebAppSlotIdentity"], result)

    @builtins.property
    def key_vault_reference_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.'''
        result = self._values.get("key_vault_reference_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs(self) -> typing.Optional["WindowsWebAppSlotLogs"]:
        '''logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogs"], result)

    @builtins.property
    def storage_account(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]]:
        '''storage_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        '''
        result = self._values.get("storage_account")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#tags WindowsWebAppSlot#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WindowsWebAppSlotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WindowsWebAppSlotTimeouts"], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_deploy_file(self) -> typing.Optional[builtins.str]:
        '''The local path and filename of the Zip packaged application to deploy to this Windows Web App.

        **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        '''
        result = self._values.get("zip_deploy_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionString",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "value": "value"},
)
class WindowsWebAppSlotConnectionString:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: The name which should be used for this Connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param type: Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}
        :param value: The connection string value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#value WindowsWebAppSlot#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotConnectionString.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The connection string value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#value WindowsWebAppSlot#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotConnectionString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotConnectionStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionStringList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotConnectionStringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotConnectionStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotConnectionStringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotConnectionStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotConnectionStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionStringOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotConnectionStringOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotConnectionStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class WindowsWebAppSlotIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotIdentityOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotIdentity]:
        return typing.cast(typing.Optional[WindowsWebAppSlotIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogs",
    jsii_struct_bases=[],
    name_mapping={
        "application_logs": "applicationLogs",
        "detailed_error_messages": "detailedErrorMessages",
        "failed_request_tracing": "failedRequestTracing",
        "http_logs": "httpLogs",
    },
)
class WindowsWebAppSlotLogs:
    def __init__(
        self,
        *,
        application_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogs", typing.Dict[str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        if isinstance(application_logs, dict):
            application_logs = WindowsWebAppSlotLogsApplicationLogs(**application_logs)
        if isinstance(http_logs, dict):
            http_logs = WindowsWebAppSlotLogsHttpLogs(**http_logs)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogs.__init__)
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
    def application_logs(
        self,
    ) -> typing.Optional["WindowsWebAppSlotLogsApplicationLogs"]:
        '''application_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        '''
        result = self._values.get("application_logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsApplicationLogs"], result)

    @builtins.property
    def detailed_error_messages(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.'''
        result = self._values.get("detailed_error_messages")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def failed_request_tracing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.'''
        result = self._values.get("failed_request_tracing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_logs(self) -> typing.Optional["WindowsWebAppSlotLogsHttpLogs"]:
        '''http_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        result = self._values.get("http_logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogs",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_level": "fileSystemLevel",
        "azure_blob_storage": "azureBlobStorage",
    },
)
class WindowsWebAppSlotLogsApplicationLogs:
    def __init__(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(**azure_blob_storage)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsApplicationLogs.__init__)
            check_type(argname="argument file_system_level", value=file_system_level, expected_type=type_hints["file_system_level"])
            check_type(argname="argument azure_blob_storage", value=azure_blob_storage, expected_type=type_hints["azure_blob_storage"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_system_level": file_system_level,
        }
        if azure_blob_storage is not None:
            self._values["azure_blob_storage"] = azure_blob_storage

    @builtins.property
    def file_system_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.'''
        result = self._values.get("file_system_level")
        assert result is not None, "Required property 'file_system_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_blob_storage(
        self,
    ) -> typing.Optional["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsApplicationLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={
        "level": "level",
        "retention_in_days": "retentionInDays",
        "sas_url": "sasUrl",
    },
)
class WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        level: builtins.str,
        retention_in_days: jsii.Number,
        sas_url: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#level WindowsWebAppSlot#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#level WindowsWebAppSlot#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, "level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, "sas_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsApplicationLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsApplicationLogsOutputReference.__init__)
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
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#level WindowsWebAppSlot#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        '''
        value = WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(
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
    ) -> WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference:
        return typing.cast(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsOutputReference, "file_system_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsApplicationLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsApplicationLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogs",
    jsii_struct_bases=[],
    name_mapping={
        "azure_blob_storage": "azureBlobStorage",
        "file_system": "fileSystem",
    },
)
class WindowsWebAppSlotLogsHttpLogs:
    def __init__(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage", typing.Dict[str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogsFileSystem", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(**azure_blob_storage)
        if isinstance(file_system, dict):
            file_system = WindowsWebAppSlotLogsHttpLogsFileSystem(**file_system)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogs.__init__)
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
    ) -> typing.Optional["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage"], result)

    @builtins.property
    def file_system(self) -> typing.Optional["WindowsWebAppSlotLogsHttpLogsFileSystem"]:
        '''file_system block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        result = self._values.get("file_system")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogsFileSystem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={"sas_url": "sasUrl", "retention_in_days": "retentionInDays"},
)
class WindowsWebAppSlotLogsHttpLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        sas_url: builtins.str,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogsAzureBlobStorage.__init__)
            check_type(argname="argument sas_url", value=sas_url, expected_type=type_hints["sas_url"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "sas_url": sas_url,
        }
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference, "sas_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsFileSystem",
    jsii_struct_bases=[],
    name_mapping={
        "retention_in_days": "retentionInDays",
        "retention_in_mb": "retentionInMb",
    },
)
class WindowsWebAppSlotLogsHttpLogsFileSystem:
    def __init__(
        self,
        *,
        retention_in_days: jsii.Number,
        retention_in_mb: jsii.Number,
    ) -> None:
        '''
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogsFileSystem.__init__)
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument retention_in_mb", value=retention_in_mb, expected_type=type_hints["retention_in_mb"])
        self._values: typing.Dict[str, typing.Any] = {
            "retention_in_days": retention_in_days,
            "retention_in_mb": retention_in_mb,
        }

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retention_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.'''
        result = self._values.get("retention_in_mb")
        assert result is not None, "Required property 'retention_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInMb")
    def retention_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInMb"))

    @retention_in_mb.setter
    def retention_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference, "retention_in_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsHttpLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsHttpLogsOutputReference.__init__)
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
        :param sas_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        '''
        value = WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(
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
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.
        '''
        value = WindowsWebAppSlotLogsHttpLogsFileSystem(
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
    ) -> WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference, jsii.get(self, "fileSystem"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemInput")
    def file_system_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem], jsii.get(self, "fileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogsHttpLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsHttpLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationLogs")
    def put_application_logs(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        value = WindowsWebAppSlotLogsApplicationLogs(
            file_system_level=file_system_level, azure_blob_storage=azure_blob_storage
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationLogs", [value]))

    @jsii.member(jsii_name="putHttpLogs")
    def put_http_logs(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage, typing.Dict[str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsFileSystem, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        value = WindowsWebAppSlotLogsHttpLogs(
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
    def application_logs(self) -> WindowsWebAppSlotLogsApplicationLogsOutputReference:
        return typing.cast(WindowsWebAppSlotLogsApplicationLogsOutputReference, jsii.get(self, "applicationLogs"))

    @builtins.property
    @jsii.member(jsii_name="httpLogs")
    def http_logs(self) -> WindowsWebAppSlotLogsHttpLogsOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsOutputReference, jsii.get(self, "httpLogs"))

    @builtins.property
    @jsii.member(jsii_name="applicationLogsInput")
    def application_logs_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogs], jsii.get(self, "applicationLogsInput"))

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
    def http_logs_input(self) -> typing.Optional[WindowsWebAppSlotLogsHttpLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogs], jsii.get(self, "httpLogsInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsOutputReference, "detailed_error_messages").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsOutputReference, "failed_request_tracing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failedRequestTracing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotLogs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfig",
    jsii_struct_bases=[],
    name_mapping={
        "always_on": "alwaysOn",
        "api_definition_url": "apiDefinitionUrl",
        "api_management_api_id": "apiManagementApiId",
        "app_command_line": "appCommandLine",
        "application_stack": "applicationStack",
        "auto_heal_enabled": "autoHealEnabled",
        "auto_heal_setting": "autoHealSetting",
        "auto_swap_slot_name": "autoSwapSlotName",
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
        "virtual_application": "virtualApplication",
        "vnet_route_all_enabled": "vnetRouteAllEnabled",
        "websockets_enabled": "websocketsEnabled",
        "worker_count": "workerCount",
    },
)
class WindowsWebAppSlotSiteConfig:
    def __init__(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigApplicationStack", typing.Dict[str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSetting", typing.Dict[str, typing.Any]]] = None,
        auto_swap_slot_name: typing.Optional[builtins.str] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigCors", typing.Dict[str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        virtual_application: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[str, typing.Any]]]]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        :param auto_swap_slot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.
        :param ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}.
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.
        :param scm_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}.
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.
        :param virtual_application: virtual_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.
        '''
        if isinstance(application_stack, dict):
            application_stack = WindowsWebAppSlotSiteConfigApplicationStack(**application_stack)
        if isinstance(auto_heal_setting, dict):
            auto_heal_setting = WindowsWebAppSlotSiteConfigAutoHealSetting(**auto_heal_setting)
        if isinstance(cors, dict):
            cors = WindowsWebAppSlotSiteConfigCors(**cors)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfig.__init__)
            check_type(argname="argument always_on", value=always_on, expected_type=type_hints["always_on"])
            check_type(argname="argument api_definition_url", value=api_definition_url, expected_type=type_hints["api_definition_url"])
            check_type(argname="argument api_management_api_id", value=api_management_api_id, expected_type=type_hints["api_management_api_id"])
            check_type(argname="argument app_command_line", value=app_command_line, expected_type=type_hints["app_command_line"])
            check_type(argname="argument application_stack", value=application_stack, expected_type=type_hints["application_stack"])
            check_type(argname="argument auto_heal_enabled", value=auto_heal_enabled, expected_type=type_hints["auto_heal_enabled"])
            check_type(argname="argument auto_heal_setting", value=auto_heal_setting, expected_type=type_hints["auto_heal_setting"])
            check_type(argname="argument auto_swap_slot_name", value=auto_swap_slot_name, expected_type=type_hints["auto_swap_slot_name"])
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
            check_type(argname="argument virtual_application", value=virtual_application, expected_type=type_hints["virtual_application"])
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
        if auto_swap_slot_name is not None:
            self._values["auto_swap_slot_name"] = auto_swap_slot_name
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
        if virtual_application is not None:
            self._values["virtual_application"] = virtual_application
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.'''
        result = self._values.get("always_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def api_definition_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.'''
        result = self._values.get("api_definition_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_management_api_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.'''
        result = self._values.get("api_management_api_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_command_line(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.'''
        result = self._values.get("app_command_line")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_stack(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigApplicationStack"]:
        '''application_stack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        '''
        result = self._values.get("application_stack")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigApplicationStack"], result)

    @builtins.property
    def auto_heal_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.'''
        result = self._values.get("auto_heal_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_heal_setting(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSetting"]:
        '''auto_heal_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        '''
        result = self._values.get("auto_heal_setting")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSetting"], result)

    @builtins.property
    def auto_swap_slot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.'''
        result = self._values.get("auto_swap_slot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_managed_identity_client_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.'''
        result = self._values.get("container_registry_managed_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.'''
        result = self._values.get("container_registry_use_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cors(self) -> typing.Optional["WindowsWebAppSlotSiteConfigCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigCors"], result)

    @builtins.property
    def default_documents(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.'''
        result = self._values.get("default_documents")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ftps_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.'''
        result = self._values.get("ftps_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_eviction_time_in_min(self) -> typing.Optional[jsii.Number]:
        '''The amount of time in minutes that a node is unhealthy before being removed from the load balancer.

        Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        '''
        result = self._values.get("health_check_eviction_time_in_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.'''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.'''
        result = self._values.get("http2_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}.'''
        result = self._values.get("ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestriction"]]], result)

    @builtins.property
    def load_balancing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.'''
        result = self._values.get("load_balancing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_mysql_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.'''
        result = self._values.get("local_mysql_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def managed_pipeline_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.'''
        result = self._values.get("managed_pipeline_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_debugging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.'''
        result = self._values.get("remote_debugging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def remote_debugging_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.'''
        result = self._values.get("remote_debugging_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}.'''
        result = self._values.get("scm_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]], result)

    @builtins.property
    def scm_minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.'''
        result = self._values.get("scm_minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.'''
        result = self._values.get("scm_use_main_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use32_bit_worker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.'''
        result = self._values.get("use32_bit_worker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def virtual_application(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]]:
        '''virtual_application block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        '''
        result = self._values.get("virtual_application")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]], result)

    @builtins.property
    def vnet_route_all_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        '''
        result = self._values.get("vnet_route_all_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def websockets_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.'''
        result = self._values.get("websockets_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def worker_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.'''
        result = self._values.get("worker_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigApplicationStack",
    jsii_struct_bases=[],
    name_mapping={
        "current_stack": "currentStack",
        "docker_container_name": "dockerContainerName",
        "docker_container_registry": "dockerContainerRegistry",
        "docker_container_tag": "dockerContainerTag",
        "dotnet_version": "dotnetVersion",
        "java_container": "javaContainer",
        "java_container_version": "javaContainerVersion",
        "java_version": "javaVersion",
        "node_version": "nodeVersion",
        "php_version": "phpVersion",
        "python_version": "pythonVersion",
    },
)
class WindowsWebAppSlotSiteConfigApplicationStack:
    def __init__(
        self,
        *,
        current_stack: typing.Optional[builtins.str] = None,
        docker_container_name: typing.Optional[builtins.str] = None,
        docker_container_registry: typing.Optional[builtins.str] = None,
        docker_container_tag: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_container: typing.Optional[builtins.str] = None,
        java_container_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param current_stack: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.
        :param docker_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.
        :param docker_container_registry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.
        :param docker_container_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.
        :param dotnet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.
        :param java_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.
        :param java_container_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.
        :param java_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.
        :param python_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigApplicationStack.__init__)
            check_type(argname="argument current_stack", value=current_stack, expected_type=type_hints["current_stack"])
            check_type(argname="argument docker_container_name", value=docker_container_name, expected_type=type_hints["docker_container_name"])
            check_type(argname="argument docker_container_registry", value=docker_container_registry, expected_type=type_hints["docker_container_registry"])
            check_type(argname="argument docker_container_tag", value=docker_container_tag, expected_type=type_hints["docker_container_tag"])
            check_type(argname="argument dotnet_version", value=dotnet_version, expected_type=type_hints["dotnet_version"])
            check_type(argname="argument java_container", value=java_container, expected_type=type_hints["java_container"])
            check_type(argname="argument java_container_version", value=java_container_version, expected_type=type_hints["java_container_version"])
            check_type(argname="argument java_version", value=java_version, expected_type=type_hints["java_version"])
            check_type(argname="argument node_version", value=node_version, expected_type=type_hints["node_version"])
            check_type(argname="argument php_version", value=php_version, expected_type=type_hints["php_version"])
            check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if current_stack is not None:
            self._values["current_stack"] = current_stack
        if docker_container_name is not None:
            self._values["docker_container_name"] = docker_container_name
        if docker_container_registry is not None:
            self._values["docker_container_registry"] = docker_container_registry
        if docker_container_tag is not None:
            self._values["docker_container_tag"] = docker_container_tag
        if dotnet_version is not None:
            self._values["dotnet_version"] = dotnet_version
        if java_container is not None:
            self._values["java_container"] = java_container
        if java_container_version is not None:
            self._values["java_container_version"] = java_container_version
        if java_version is not None:
            self._values["java_version"] = java_version
        if node_version is not None:
            self._values["node_version"] = node_version
        if php_version is not None:
            self._values["php_version"] = php_version
        if python_version is not None:
            self._values["python_version"] = python_version

    @builtins.property
    def current_stack(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.'''
        result = self._values.get("current_stack")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.'''
        result = self._values.get("docker_container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_registry(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.'''
        result = self._values.get("docker_container_registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.'''
        result = self._values.get("docker_container_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dotnet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.'''
        result = self._values.get("dotnet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_container(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.'''
        result = self._values.get("java_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_container_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.'''
        result = self._values.get("java_container_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.'''
        result = self._values.get("java_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.'''
        result = self._values.get("node_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def php_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.'''
        result = self._values.get("php_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def python_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.'''
        result = self._values.get("python_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigApplicationStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigApplicationStackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigApplicationStackOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigApplicationStackOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCurrentStack")
    def reset_current_stack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurrentStack", []))

    @jsii.member(jsii_name="resetDockerContainerName")
    def reset_docker_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerName", []))

    @jsii.member(jsii_name="resetDockerContainerRegistry")
    def reset_docker_container_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerRegistry", []))

    @jsii.member(jsii_name="resetDockerContainerTag")
    def reset_docker_container_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerTag", []))

    @jsii.member(jsii_name="resetDotnetVersion")
    def reset_dotnet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDotnetVersion", []))

    @jsii.member(jsii_name="resetJavaContainer")
    def reset_java_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaContainer", []))

    @jsii.member(jsii_name="resetJavaContainerVersion")
    def reset_java_container_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaContainerVersion", []))

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

    @builtins.property
    @jsii.member(jsii_name="currentStackInput")
    def current_stack_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentStackInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerNameInput")
    def docker_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerRegistryInput")
    def docker_container_registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerRegistryInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerTagInput")
    def docker_container_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerTagInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetVersionInput")
    def dotnet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dotnetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaContainerInput")
    def java_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="javaContainerVersionInput")
    def java_container_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaContainerVersionInput"))

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
    @jsii.member(jsii_name="currentStack")
    def current_stack(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentStack"))

    @current_stack.setter
    def current_stack(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "current_stack").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentStack", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerName")
    def docker_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerName"))

    @docker_container_name.setter
    def docker_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "docker_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerRegistry")
    def docker_container_registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerRegistry"))

    @docker_container_registry.setter
    def docker_container_registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "docker_container_registry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerRegistry", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerTag")
    def docker_container_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerTag"))

    @docker_container_tag.setter
    def docker_container_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "docker_container_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerTag", value)

    @builtins.property
    @jsii.member(jsii_name="dotnetVersion")
    def dotnet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dotnetVersion"))

    @dotnet_version.setter
    def dotnet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "dotnet_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dotnetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaContainer")
    def java_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaContainer"))

    @java_container.setter
    def java_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "java_container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaContainer", value)

    @builtins.property
    @jsii.member(jsii_name="javaContainerVersion")
    def java_container_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaContainerVersion"))

    @java_container_version.setter
    def java_container_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "java_container_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaContainerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaVersion")
    def java_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaVersion"))

    @java_version.setter
    def java_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "java_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="nodeVersion")
    def node_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeVersion"))

    @node_version.setter
    def node_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "node_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="phpVersion")
    def php_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phpVersion"))

    @php_version.setter
    def php_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "php_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pythonVersion")
    def python_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pythonVersion"))

    @python_version.setter
    def python_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "python_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSetting",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "trigger": "trigger"},
)
class WindowsWebAppSlotSiteConfigAutoHealSetting:
    def __init__(
        self,
        *,
        action: typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingAction", typing.Dict[str, typing.Any]],
        trigger: typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        if isinstance(action, dict):
            action = WindowsWebAppSlotSiteConfigAutoHealSettingAction(**action)
        if isinstance(trigger, dict):
            trigger = WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSetting.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "trigger": trigger,
        }

    @builtins.property
    def action(self) -> "WindowsWebAppSlotSiteConfigAutoHealSettingAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingAction", result)

    @builtins.property
    def trigger(self) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger":
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        result = self._values.get("trigger")
        assert result is not None, "Required property 'trigger' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTrigger", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingAction",
    jsii_struct_bases=[],
    name_mapping={
        "action_type": "actionType",
        "custom_action": "customAction",
        "minimum_process_execution_time": "minimumProcessExecutionTime",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingAction:
    def __init__(
        self,
        *,
        action_type: builtins.str,
        custom_action: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction", typing.Dict[str, typing.Any]]] = None,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.
        :param custom_action: custom_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.
        '''
        if isinstance(custom_action, dict):
            custom_action = WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(**custom_action)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingAction.__init__)
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument custom_action", value=custom_action, expected_type=type_hints["custom_action"])
            check_type(argname="argument minimum_process_execution_time", value=minimum_process_execution_time, expected_type=type_hints["minimum_process_execution_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_type": action_type,
        }
        if custom_action is not None:
            self._values["custom_action"] = custom_action
        if minimum_process_execution_time is not None:
            self._values["minimum_process_execution_time"] = minimum_process_execution_time

    @builtins.property
    def action_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.'''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_action(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction"]:
        '''custom_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        '''
        result = self._values.get("custom_action")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction"], result)

    @builtins.property
    def minimum_process_execution_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.'''
        result = self._values.get("minimum_process_execution_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction",
    jsii_struct_bases=[],
    name_mapping={"executable": "executable", "parameters": "parameters"},
)
class WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction:
    def __init__(
        self,
        *,
        executable: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param executable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#executable WindowsWebAppSlot#executable}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction.__init__)
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "executable": executable,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def executable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#executable WindowsWebAppSlot#executable}.'''
        result = self._values.get("executable")
        assert result is not None, "Required property 'executable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="executableInput")
    def executable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executableInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="executable")
    def executable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executable"))

    @executable.setter
    def executable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference, "executable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executable", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomAction")
    def put_custom_action(
        self,
        *,
        executable: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param executable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#executable WindowsWebAppSlot#executable}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(
            executable=executable, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putCustomAction", [value]))

    @jsii.member(jsii_name="resetCustomAction")
    def reset_custom_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAction", []))

    @jsii.member(jsii_name="resetMinimumProcessExecutionTime")
    def reset_minimum_process_execution_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumProcessExecutionTime", []))

    @builtins.property
    @jsii.member(jsii_name="customAction")
    def custom_action(
        self,
    ) -> WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference, jsii.get(self, "customAction"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customActionInput")
    def custom_action_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction], jsii.get(self, "customActionInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="minimumProcessExecutionTime")
    def minimum_process_execution_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumProcessExecutionTime"))

    @minimum_process_execution_time.setter
    def minimum_process_execution_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference, "minimum_process_execution_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumProcessExecutionTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        action_type: builtins.str,
        custom_action: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction, typing.Dict[str, typing.Any]]] = None,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.
        :param custom_action: custom_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingAction(
            action_type=action_type,
            custom_action=custom_action,
            minimum_process_execution_time=minimum_process_execution_time,
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        private_memory_kb: typing.Optional[jsii.Number] = None,
        requests: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests", typing.Dict[str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param private_memory_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.
        :param requests: requests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(
            private_memory_kb=private_memory_kb,
            requests=requests,
            slow_request=slow_request,
            status_code=status_code,
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "private_memory_kb": "privateMemoryKb",
        "requests": "requests",
        "slow_request": "slowRequest",
        "status_code": "statusCode",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTrigger:
    def __init__(
        self,
        *,
        private_memory_kb: typing.Optional[jsii.Number] = None,
        requests: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests", typing.Dict[str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param private_memory_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.
        :param requests: requests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        if isinstance(requests, dict):
            requests = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(**requests)
        if isinstance(slow_request, dict):
            slow_request = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(**slow_request)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTrigger.__init__)
            check_type(argname="argument private_memory_kb", value=private_memory_kb, expected_type=type_hints["private_memory_kb"])
            check_type(argname="argument requests", value=requests, expected_type=type_hints["requests"])
            check_type(argname="argument slow_request", value=slow_request, expected_type=type_hints["slow_request"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {}
        if private_memory_kb is not None:
            self._values["private_memory_kb"] = private_memory_kb
        if requests is not None:
            self._values["requests"] = requests
        if slow_request is not None:
            self._values["slow_request"] = slow_request
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def private_memory_kb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.'''
        result = self._values.get("private_memory_kb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"]:
        '''requests block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        '''
        result = self._values.get("requests")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"], result)

    @builtins.property
    def slow_request(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"]:
        '''slow_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        '''
        result = self._values.get("slow_request")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"], result)

    @builtins.property
    def status_code(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        '''status_code block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequests")
    def put_requests(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(
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
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#path WindowsWebAppSlot#path}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(
            count=count, interval=interval, time_taken=time_taken, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putSlowRequest", [value]))

    @jsii.member(jsii_name="putStatusCode")
    def put_status_code(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference.put_status_code)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCode", [value]))

    @jsii.member(jsii_name="resetPrivateMemoryKb")
    def reset_private_memory_kb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateMemoryKb", []))

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
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference", jsii.get(self, "requests"))

    @builtins.property
    @jsii.member(jsii_name="slowRequest")
    def slow_request(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference", jsii.get(self, "slowRequest"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList", jsii.get(self, "statusCode"))

    @builtins.property
    @jsii.member(jsii_name="privateMemoryKbInput")
    def private_memory_kb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privateMemoryKbInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsInput")
    def requests_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"], jsii.get(self, "requestsInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRequestInput")
    def slow_request_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"], jsii.get(self, "slowRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="privateMemoryKb")
    def private_memory_kb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privateMemoryKb"))

    @private_memory_kb.setter
    def private_memory_kb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference, "private_memory_kb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateMemoryKb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval": "interval"},
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests:
    def __init__(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "interval": interval,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "time_taken": "timeTaken",
        "path": "path",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest:
    def __init__(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        time_taken: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#path WindowsWebAppSlot#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_taken(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.'''
        result = self._values.get("time_taken")
        assert result is not None, "Required property 'time_taken' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#path WindowsWebAppSlot#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="timeTaken")
    def time_taken(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeTaken"))

    @time_taken.setter
    def time_taken(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "time_taken").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeTaken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode",
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
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode:
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
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param status_code_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#status_code_range WindowsWebAppSlot#status_code_range}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#path WindowsWebAppSlot#path}.
        :param sub_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sub_status WindowsWebAppSlot#sub_status}.
        :param win32_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#win32_status WindowsWebAppSlot#win32_status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#status_code_range WindowsWebAppSlot#status_code_range}.'''
        result = self._values.get("status_code_range")
        assert result is not None, "Required property 'status_code_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#path WindowsWebAppSlot#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_status(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#sub_status WindowsWebAppSlot#sub_status}.'''
        result = self._values.get("sub_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def win32_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#win32_status WindowsWebAppSlot#win32_status}.'''
        result = self._values.get("win32_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="statusCodeRange")
    def status_code_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCodeRange"))

    @status_code_range.setter
    def status_code_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "status_code_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCodeRange", value)

    @builtins.property
    @jsii.member(jsii_name="subStatus")
    def sub_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subStatus"))

    @sub_status.setter
    def sub_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "sub_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subStatus", value)

    @builtins.property
    @jsii.member(jsii_name="win32Status")
    def win32_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "win32Status"))

    @win32_status.setter
    def win32_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "win32_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "win32Status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigCors",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_origins": "allowedOrigins",
        "support_credentials": "supportCredentials",
    },
)
class WindowsWebAppSlotSiteConfigCors:
    def __init__(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigCors.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        '''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def support_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Are credentials allowed in CORS requests? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        result = self._values.get("support_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigCorsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigCorsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigCorsOutputReference, "allowed_origins").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigCorsOutputReference, "support_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteConfigCors]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigCors],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestriction",
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
class WindowsWebAppSlotSiteConfigIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#headers WindowsWebAppSlot#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#priority WindowsWebAppSlot#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestriction.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#headers WindowsWebAppSlot#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#priority WindowsWebAppSlot#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class WindowsWebAppSlotSiteConfigIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionHeaders.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference.put_headers)
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
    def headers(self) -> WindowsWebAppSlotSiteConfigIpRestrictionHeadersList:
        return typing.cast(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationStack")
    def put_application_stack(
        self,
        *,
        current_stack: typing.Optional[builtins.str] = None,
        docker_container_name: typing.Optional[builtins.str] = None,
        docker_container_registry: typing.Optional[builtins.str] = None,
        docker_container_tag: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_container: typing.Optional[builtins.str] = None,
        java_container_version: typing.Optional[builtins.str] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param current_stack: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.
        :param docker_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.
        :param docker_container_registry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.
        :param docker_container_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.
        :param dotnet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.
        :param java_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.
        :param java_container_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.
        :param java_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.
        :param python_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.
        '''
        value = WindowsWebAppSlotSiteConfigApplicationStack(
            current_stack=current_stack,
            docker_container_name=docker_container_name,
            docker_container_registry=docker_container_registry,
            docker_container_tag=docker_container_tag,
            dotnet_version=dotnet_version,
            java_container=java_container,
            java_container_version=java_container_version,
            java_version=java_version,
            node_version=node_version,
            php_version=php_version,
            python_version=python_version,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationStack", [value]))

    @jsii.member(jsii_name="putAutoHealSetting")
    def put_auto_heal_setting(
        self,
        *,
        action: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingAction, typing.Dict[str, typing.Any]],
        trigger: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSetting(
            action=action, trigger=trigger
        )

        return typing.cast(None, jsii.invoke(self, "putAutoHealSetting", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allowed_origins: typing.Sequence[builtins.str],
        support_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        value = WindowsWebAppSlotSiteConfigCors(
            allowed_origins=allowed_origins, support_credentials=support_credentials
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putIpRestriction")
    def put_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigOutputReference.put_ip_restriction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpRestriction", [value]))

    @jsii.member(jsii_name="putScmIpRestriction")
    def put_scm_ip_restriction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigOutputReference.put_scm_ip_restriction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScmIpRestriction", [value]))

    @jsii.member(jsii_name="putVirtualApplication")
    def put_virtual_application(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigOutputReference.put_virtual_application)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualApplication", [value]))

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

    @jsii.member(jsii_name="resetAutoSwapSlotName")
    def reset_auto_swap_slot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSwapSlotName", []))

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

    @jsii.member(jsii_name="resetVirtualApplication")
    def reset_virtual_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualApplication", []))

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
    ) -> WindowsWebAppSlotSiteConfigApplicationStackOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, jsii.get(self, "applicationStack"))

    @builtins.property
    @jsii.member(jsii_name="autoHealSetting")
    def auto_heal_setting(
        self,
    ) -> WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference, jsii.get(self, "autoHealSetting"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> WindowsWebAppSlotSiteConfigCorsOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorLoggingEnabled")
    def detailed_error_logging_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "detailedErrorLoggingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="ipRestriction")
    def ip_restriction(self) -> WindowsWebAppSlotSiteConfigIpRestrictionList:
        return typing.cast(WindowsWebAppSlotSiteConfigIpRestrictionList, jsii.get(self, "ipRestriction"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestriction")
    def scm_ip_restriction(self) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionList":
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionList", jsii.get(self, "scmIpRestriction"))

    @builtins.property
    @jsii.member(jsii_name="scmType")
    def scm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmType"))

    @builtins.property
    @jsii.member(jsii_name="virtualApplication")
    def virtual_application(
        self,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationList":
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationList", jsii.get(self, "virtualApplication"))

    @builtins.property
    @jsii.member(jsii_name="windowsFxVersion")
    def windows_fx_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowsFxVersion"))

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
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack], jsii.get(self, "applicationStackInput"))

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
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting], jsii.get(self, "autoHealSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSwapSlotNameInput")
    def auto_swap_slot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoSwapSlotNameInput"))

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
    def cors_input(self) -> typing.Optional[WindowsWebAppSlotSiteConfigCors]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigCors], jsii.get(self, "corsInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]], jsii.get(self, "ipRestrictionInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]], jsii.get(self, "scmIpRestrictionInput"))

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
    @jsii.member(jsii_name="virtualApplicationInput")
    def virtual_application_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]], jsii.get(self, "virtualApplicationInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "always_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysOn", value)

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrl")
    def api_definition_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiDefinitionUrl"))

    @api_definition_url.setter
    def api_definition_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "api_definition_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiDefinitionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiId")
    def api_management_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementApiId"))

    @api_management_api_id.setter
    def api_management_api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "api_management_api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementApiId", value)

    @builtins.property
    @jsii.member(jsii_name="appCommandLine")
    def app_command_line(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appCommandLine"))

    @app_command_line.setter
    def app_command_line(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "app_command_line").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "auto_heal_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoSwapSlotName")
    def auto_swap_slot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoSwapSlotName"))

    @auto_swap_slot_name.setter
    def auto_swap_slot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "auto_swap_slot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSwapSlotName", value)

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "container_registry_managed_identity_client_id").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "container_registry_use_managed_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryUseManagedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDocuments")
    def default_documents(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultDocuments"))

    @default_documents.setter
    def default_documents(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "default_documents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="ftpsState")
    def ftps_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ftpsState"))

    @ftps_state.setter
    def ftps_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "ftps_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ftpsState", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMin")
    def health_check_eviction_time_in_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckEvictionTimeInMin"))

    @health_check_eviction_time_in_min.setter
    def health_check_eviction_time_in_min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "health_check_eviction_time_in_min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEvictionTimeInMin", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "health_check_path").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "http2_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMode")
    def load_balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingMode"))

    @load_balancing_mode.setter
    def load_balancing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "load_balancing_mode").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "local_mysql_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMysqlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="managedPipelineMode")
    def managed_pipeline_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPipelineMode"))

    @managed_pipeline_mode.setter
    def managed_pipeline_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "managed_pipeline_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPipelineMode", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "minimum_tls_version").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "remote_debugging_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersion")
    def remote_debugging_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteDebuggingVersion"))

    @remote_debugging_version.setter
    def remote_debugging_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "remote_debugging_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersion")
    def scm_minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmMinimumTlsVersion"))

    @scm_minimum_tls_version.setter
    def scm_minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "scm_minimum_tls_version").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "scm_use_main_ip_restriction").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "use32_bit_worker").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "vnet_route_all_enabled").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "websockets_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websocketsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "worker_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteConfig]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestriction",
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
class WindowsWebAppSlotSiteConfigScmIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders", typing.Dict[str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#headers WindowsWebAppSlot#headers}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#priority WindowsWebAppSlot#priority}.
        :param service_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}.
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestriction.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#action WindowsWebAppSlot#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#headers WindowsWebAppSlot#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#priority WindowsWebAppSlot#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}.'''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigScmIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference, "x_azure_fdid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference, "x_fd_health_probe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference, "x_forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference.put_headers)
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
    def headers(self) -> WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList:
        return typing.cast(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "service_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "virtual_network_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplication",
    jsii_struct_bases=[],
    name_mapping={
        "physical_path": "physicalPath",
        "preload": "preload",
        "virtual_path": "virtualPath",
        "virtual_directory": "virtualDirectory",
    },
)
class WindowsWebAppSlotSiteConfigVirtualApplication:
    def __init__(
        self,
        *,
        physical_path: builtins.str,
        preload: typing.Union[builtins.bool, cdktf.IResolvable],
        virtual_path: builtins.str,
        virtual_directory: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param physical_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.
        :param preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#preload WindowsWebAppSlot#preload}.
        :param virtual_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.
        :param virtual_directory: virtual_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_directory WindowsWebAppSlot#virtual_directory}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplication.__init__)
            check_type(argname="argument physical_path", value=physical_path, expected_type=type_hints["physical_path"])
            check_type(argname="argument preload", value=preload, expected_type=type_hints["preload"])
            check_type(argname="argument virtual_path", value=virtual_path, expected_type=type_hints["virtual_path"])
            check_type(argname="argument virtual_directory", value=virtual_directory, expected_type=type_hints["virtual_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "physical_path": physical_path,
            "preload": preload,
            "virtual_path": virtual_path,
        }
        if virtual_directory is not None:
            self._values["virtual_directory"] = virtual_directory

    @builtins.property
    def physical_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.'''
        result = self._values.get("physical_path")
        assert result is not None, "Required property 'physical_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preload(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#preload WindowsWebAppSlot#preload}.'''
        result = self._values.get("preload")
        assert result is not None, "Required property 'preload' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def virtual_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.'''
        result = self._values.get("virtual_path")
        assert result is not None, "Required property 'virtual_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_directory(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]]:
        '''virtual_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_directory WindowsWebAppSlot#virtual_directory}
        '''
        result = self._values.get("virtual_directory")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigVirtualApplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigVirtualApplicationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVirtualDirectory")
    def put_virtual_directory(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference.put_virtual_directory)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualDirectory", [value]))

    @jsii.member(jsii_name="resetVirtualDirectory")
    def reset_virtual_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="virtualDirectory")
    def virtual_directory(
        self,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList":
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList", jsii.get(self, "virtualDirectory"))

    @builtins.property
    @jsii.member(jsii_name="physicalPathInput")
    def physical_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "physicalPathInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadInput")
    def preload_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preloadInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualDirectoryInput")
    def virtual_directory_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]], jsii.get(self, "virtualDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualPathInput")
    def virtual_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualPathInput"))

    @builtins.property
    @jsii.member(jsii_name="physicalPath")
    def physical_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "physicalPath"))

    @physical_path.setter
    def physical_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference, "physical_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "physicalPath", value)

    @builtins.property
    @jsii.member(jsii_name="preload")
    def preload(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preload"))

    @preload.setter
    def preload(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference, "preload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preload", value)

    @builtins.property
    @jsii.member(jsii_name="virtualPath")
    def virtual_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualPath"))

    @virtual_path.setter
    def virtual_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference, "virtual_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory",
    jsii_struct_bases=[],
    name_mapping={"physical_path": "physicalPath", "virtual_path": "virtualPath"},
)
class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory:
    def __init__(
        self,
        *,
        physical_path: typing.Optional[builtins.str] = None,
        virtual_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param physical_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.
        :param virtual_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory.__init__)
            check_type(argname="argument physical_path", value=physical_path, expected_type=type_hints["physical_path"])
            check_type(argname="argument virtual_path", value=virtual_path, expected_type=type_hints["virtual_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if physical_path is not None:
            self._values["physical_path"] = physical_path
        if virtual_path is not None:
            self._values["virtual_path"] = virtual_path

    @builtins.property
    def physical_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.'''
        result = self._values.get("physical_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.'''
        result = self._values.get("virtual_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPhysicalPath")
    def reset_physical_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhysicalPath", []))

    @jsii.member(jsii_name="resetVirtualPath")
    def reset_virtual_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualPath", []))

    @builtins.property
    @jsii.member(jsii_name="physicalPathInput")
    def physical_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "physicalPathInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualPathInput")
    def virtual_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualPathInput"))

    @builtins.property
    @jsii.member(jsii_name="physicalPath")
    def physical_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "physicalPath"))

    @physical_path.setter
    def physical_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference, "physical_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "physicalPath", value)

    @builtins.property
    @jsii.member(jsii_name="virtualPath")
    def virtual_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualPath"))

    @virtual_path.setter
    def virtual_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference, "virtual_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredential",
    jsii_struct_bases=[],
    name_mapping={},
)
class WindowsWebAppSlotSiteCredential:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteCredentialList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredentialList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteCredentialList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteCredentialOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteCredentialList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteCredentialOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteCredentialList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteCredentialList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteCredentialList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class WindowsWebAppSlotSiteCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredentialOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotSiteCredentialOutputReference.__init__)
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
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteCredential]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotSiteCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccount",
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
class WindowsWebAppSlotStorageAccount:
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
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#access_key WindowsWebAppSlot#access_key}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#account_name WindowsWebAppSlot#account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#share_name WindowsWebAppSlot#share_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#mount_path WindowsWebAppSlot#mount_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotStorageAccount.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#access_key WindowsWebAppSlot#access_key}.'''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#account_name WindowsWebAppSlot#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#share_name WindowsWebAppSlot#share_name}.'''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#type WindowsWebAppSlot#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#mount_path WindowsWebAppSlot#mount_path}.'''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotStorageAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotStorageAccountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccountList",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotStorageAccountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotStorageAccountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotStorageAccountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotStorageAccountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotStorageAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccountOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotStorageAccountOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotStorageAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WindowsWebAppSlotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#create WindowsWebAppSlot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#delete WindowsWebAppSlot#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#read WindowsWebAppSlot#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#update WindowsWebAppSlot#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsWebAppSlotTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#create WindowsWebAppSlot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#delete WindowsWebAppSlot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#read WindowsWebAppSlot#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_web_app_slot#update WindowsWebAppSlot#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsWebAppSlotTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsWebAppSlotTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WindowsWebAppSlot",
    "WindowsWebAppSlotAuthSettings",
    "WindowsWebAppSlotAuthSettingsActiveDirectory",
    "WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference",
    "WindowsWebAppSlotAuthSettingsFacebook",
    "WindowsWebAppSlotAuthSettingsFacebookOutputReference",
    "WindowsWebAppSlotAuthSettingsGithub",
    "WindowsWebAppSlotAuthSettingsGithubOutputReference",
    "WindowsWebAppSlotAuthSettingsGoogle",
    "WindowsWebAppSlotAuthSettingsGoogleOutputReference",
    "WindowsWebAppSlotAuthSettingsMicrosoft",
    "WindowsWebAppSlotAuthSettingsMicrosoftOutputReference",
    "WindowsWebAppSlotAuthSettingsOutputReference",
    "WindowsWebAppSlotAuthSettingsTwitter",
    "WindowsWebAppSlotAuthSettingsTwitterOutputReference",
    "WindowsWebAppSlotBackup",
    "WindowsWebAppSlotBackupOutputReference",
    "WindowsWebAppSlotBackupSchedule",
    "WindowsWebAppSlotBackupScheduleOutputReference",
    "WindowsWebAppSlotConfig",
    "WindowsWebAppSlotConnectionString",
    "WindowsWebAppSlotConnectionStringList",
    "WindowsWebAppSlotConnectionStringOutputReference",
    "WindowsWebAppSlotIdentity",
    "WindowsWebAppSlotIdentityOutputReference",
    "WindowsWebAppSlotLogs",
    "WindowsWebAppSlotLogsApplicationLogs",
    "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage",
    "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference",
    "WindowsWebAppSlotLogsApplicationLogsOutputReference",
    "WindowsWebAppSlotLogsHttpLogs",
    "WindowsWebAppSlotLogsHttpLogsAzureBlobStorage",
    "WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference",
    "WindowsWebAppSlotLogsHttpLogsFileSystem",
    "WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference",
    "WindowsWebAppSlotLogsHttpLogsOutputReference",
    "WindowsWebAppSlotLogsOutputReference",
    "WindowsWebAppSlotSiteConfig",
    "WindowsWebAppSlotSiteConfigApplicationStack",
    "WindowsWebAppSlotSiteConfigApplicationStackOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSetting",
    "WindowsWebAppSlotSiteConfigAutoHealSettingAction",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
    "WindowsWebAppSlotSiteConfigCors",
    "WindowsWebAppSlotSiteConfigCorsOutputReference",
    "WindowsWebAppSlotSiteConfigIpRestriction",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeaders",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeadersList",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference",
    "WindowsWebAppSlotSiteConfigIpRestrictionList",
    "WindowsWebAppSlotSiteConfigIpRestrictionOutputReference",
    "WindowsWebAppSlotSiteConfigOutputReference",
    "WindowsWebAppSlotSiteConfigScmIpRestriction",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionList",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference",
    "WindowsWebAppSlotSiteConfigVirtualApplication",
    "WindowsWebAppSlotSiteConfigVirtualApplicationList",
    "WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference",
    "WindowsWebAppSlotSiteCredential",
    "WindowsWebAppSlotSiteCredentialList",
    "WindowsWebAppSlotSiteCredentialOutputReference",
    "WindowsWebAppSlotStorageAccount",
    "WindowsWebAppSlotStorageAccountList",
    "WindowsWebAppSlotStorageAccountOutputReference",
    "WindowsWebAppSlotTimeouts",
    "WindowsWebAppSlotTimeoutsOutputReference",
]

publication.publish()
