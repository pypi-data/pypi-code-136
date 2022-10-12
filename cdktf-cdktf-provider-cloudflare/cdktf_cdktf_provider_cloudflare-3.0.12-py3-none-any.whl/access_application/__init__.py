'''
# `cloudflare_access_application`

Refer to the Terraform Registory for docs: [`cloudflare_access_application`](https://www.terraform.io/docs/providers/cloudflare/r/access_application).
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


class AccessApplication(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application cloudflare_access_application}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allowed_idps: typing.Optional[typing.Sequence[builtins.str]] = None,
        app_launcher_visible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_redirect_to_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessApplicationCorsHeaders", typing.Dict[str, typing.Any]]]]] = None,
        custom_deny_message: typing.Optional[builtins.str] = None,
        custom_deny_url: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        enable_binding_cookie: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_only_cookie_attribute: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        logo_url: typing.Optional[builtins.str] = None,
        saas_app: typing.Optional[typing.Union["AccessApplicationSaasApp", typing.Dict[str, typing.Any]]] = None,
        same_site_cookie_attribute: typing.Optional[builtins.str] = None,
        service_auth401_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        session_duration: typing.Optional[builtins.str] = None,
        skip_interstitial: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application cloudflare_access_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Friendly name of the Access Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name AccessApplication#name}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#account_id AccessApplication#account_id}
        :param allowed_idps: The identity providers selected for the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_idps AccessApplication#allowed_idps}
        :param app_launcher_visible: Option to show/hide applications in App Launcher. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#app_launcher_visible AccessApplication#app_launcher_visible}
        :param auto_redirect_to_identity: Option to skip identity provider selection if only one is configured in ``allowed_idps``. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#auto_redirect_to_identity AccessApplication#auto_redirect_to_identity}
        :param cors_headers: cors_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#cors_headers AccessApplication#cors_headers}
        :param custom_deny_message: Option that returns a custom error message when a user is denied access to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_message AccessApplication#custom_deny_message}
        :param custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_url AccessApplication#custom_deny_url}
        :param domain: The complete URL of the asset you wish to put Cloudflare Access in front of. Can include subdomains or paths. Or both. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#domain AccessApplication#domain}
        :param enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#enable_binding_cookie AccessApplication#enable_binding_cookie}
        :param http_only_cookie_attribute: Option to add the ``HttpOnly`` cookie flag to access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#http_only_cookie_attribute AccessApplication#http_only_cookie_attribute}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#id AccessApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logo_url: Image URL for the logo shown in the app launcher dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#logo_url AccessApplication#logo_url}
        :param saas_app: saas_app block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#saas_app AccessApplication#saas_app}
        :param same_site_cookie_attribute: Defines the same-site cookie setting for access tokens. Available values: ``none``, ``lax``, ``strict``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#same_site_cookie_attribute AccessApplication#same_site_cookie_attribute}
        :param service_auth401_redirect: Option to return a 401 status code in service authentication rules on failed requests. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#service_auth_401_redirect AccessApplication#service_auth_401_redirect}
        :param session_duration: How often a user will be forced to re-authorise. Must be in the format ``48h`` or ``2h45m``. Defaults to ``24h``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#session_duration AccessApplication#session_duration}
        :param skip_interstitial: Option to skip the authorization interstitial when using the CLI. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#skip_interstitial AccessApplication#skip_interstitial}
        :param type: The application type. Available values: ``self_hosted``, ``saas``, ``ssh``, ``vnc``, ``bookmark``. Defaults to ``self_hosted``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#type AccessApplication#type}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#zone_id AccessApplication#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AccessApplicationConfig(
            name=name,
            account_id=account_id,
            allowed_idps=allowed_idps,
            app_launcher_visible=app_launcher_visible,
            auto_redirect_to_identity=auto_redirect_to_identity,
            cors_headers=cors_headers,
            custom_deny_message=custom_deny_message,
            custom_deny_url=custom_deny_url,
            domain=domain,
            enable_binding_cookie=enable_binding_cookie,
            http_only_cookie_attribute=http_only_cookie_attribute,
            id=id,
            logo_url=logo_url,
            saas_app=saas_app,
            same_site_cookie_attribute=same_site_cookie_attribute,
            service_auth401_redirect=service_auth401_redirect,
            session_duration=session_duration,
            skip_interstitial=skip_interstitial,
            type=type,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCorsHeaders")
    def put_cors_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessApplicationCorsHeaders", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplication.put_cors_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCorsHeaders", [value]))

    @jsii.member(jsii_name="putSaasApp")
    def put_saas_app(
        self,
        *,
        consumer_service_url: builtins.str,
        sp_entity_id: builtins.str,
        name_id_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_service_url: The service provider's endpoint that is responsible for receiving and parsing a SAML assertion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#consumer_service_url AccessApplication#consumer_service_url}
        :param sp_entity_id: A globally unique name for an identity or service provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#sp_entity_id AccessApplication#sp_entity_id}
        :param name_id_format: The format of the name identifier sent to the SaaS application. Defaults to ``email``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name_id_format AccessApplication#name_id_format}
        '''
        value = AccessApplicationSaasApp(
            consumer_service_url=consumer_service_url,
            sp_entity_id=sp_entity_id,
            name_id_format=name_id_format,
        )

        return typing.cast(None, jsii.invoke(self, "putSaasApp", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAllowedIdps")
    def reset_allowed_idps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedIdps", []))

    @jsii.member(jsii_name="resetAppLauncherVisible")
    def reset_app_launcher_visible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppLauncherVisible", []))

    @jsii.member(jsii_name="resetAutoRedirectToIdentity")
    def reset_auto_redirect_to_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRedirectToIdentity", []))

    @jsii.member(jsii_name="resetCorsHeaders")
    def reset_cors_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsHeaders", []))

    @jsii.member(jsii_name="resetCustomDenyMessage")
    def reset_custom_deny_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDenyMessage", []))

    @jsii.member(jsii_name="resetCustomDenyUrl")
    def reset_custom_deny_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDenyUrl", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetEnableBindingCookie")
    def reset_enable_binding_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBindingCookie", []))

    @jsii.member(jsii_name="resetHttpOnlyCookieAttribute")
    def reset_http_only_cookie_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpOnlyCookieAttribute", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogoUrl")
    def reset_logo_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoUrl", []))

    @jsii.member(jsii_name="resetSaasApp")
    def reset_saas_app(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaasApp", []))

    @jsii.member(jsii_name="resetSameSiteCookieAttribute")
    def reset_same_site_cookie_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSameSiteCookieAttribute", []))

    @jsii.member(jsii_name="resetServiceAuth401Redirect")
    def reset_service_auth401_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAuth401Redirect", []))

    @jsii.member(jsii_name="resetSessionDuration")
    def reset_session_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionDuration", []))

    @jsii.member(jsii_name="resetSkipInterstitial")
    def reset_skip_interstitial(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipInterstitial", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aud")
    def aud(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aud"))

    @builtins.property
    @jsii.member(jsii_name="corsHeaders")
    def cors_headers(self) -> "AccessApplicationCorsHeadersList":
        return typing.cast("AccessApplicationCorsHeadersList", jsii.get(self, "corsHeaders"))

    @builtins.property
    @jsii.member(jsii_name="saasApp")
    def saas_app(self) -> "AccessApplicationSaasAppOutputReference":
        return typing.cast("AccessApplicationSaasAppOutputReference", jsii.get(self, "saasApp"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedIdpsInput")
    def allowed_idps_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedIdpsInput"))

    @builtins.property
    @jsii.member(jsii_name="appLauncherVisibleInput")
    def app_launcher_visible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "appLauncherVisibleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRedirectToIdentityInput")
    def auto_redirect_to_identity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoRedirectToIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="corsHeadersInput")
    def cors_headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessApplicationCorsHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessApplicationCorsHeaders"]]], jsii.get(self, "corsHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="customDenyMessageInput")
    def custom_deny_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDenyMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="customDenyUrlInput")
    def custom_deny_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDenyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBindingCookieInput")
    def enable_binding_cookie_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBindingCookieInput"))

    @builtins.property
    @jsii.member(jsii_name="httpOnlyCookieAttributeInput")
    def http_only_cookie_attribute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpOnlyCookieAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logoUrlInput")
    def logo_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="saasAppInput")
    def saas_app_input(self) -> typing.Optional["AccessApplicationSaasApp"]:
        return typing.cast(typing.Optional["AccessApplicationSaasApp"], jsii.get(self, "saasAppInput"))

    @builtins.property
    @jsii.member(jsii_name="sameSiteCookieAttributeInput")
    def same_site_cookie_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sameSiteCookieAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAuth401RedirectInput")
    def service_auth401_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serviceAuth401RedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionDurationInput")
    def session_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="skipInterstitialInput")
    def skip_interstitial_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipInterstitialInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="allowedIdps")
    def allowed_idps(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedIdps"))

    @allowed_idps.setter
    def allowed_idps(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "allowed_idps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedIdps", value)

    @builtins.property
    @jsii.member(jsii_name="appLauncherVisible")
    def app_launcher_visible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "appLauncherVisible"))

    @app_launcher_visible.setter
    def app_launcher_visible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "app_launcher_visible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appLauncherVisible", value)

    @builtins.property
    @jsii.member(jsii_name="autoRedirectToIdentity")
    def auto_redirect_to_identity(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoRedirectToIdentity"))

    @auto_redirect_to_identity.setter
    def auto_redirect_to_identity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "auto_redirect_to_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRedirectToIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="customDenyMessage")
    def custom_deny_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDenyMessage"))

    @custom_deny_message.setter
    def custom_deny_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "custom_deny_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDenyMessage", value)

    @builtins.property
    @jsii.member(jsii_name="customDenyUrl")
    def custom_deny_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDenyUrl"))

    @custom_deny_url.setter
    def custom_deny_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "custom_deny_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDenyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="enableBindingCookie")
    def enable_binding_cookie(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBindingCookie"))

    @enable_binding_cookie.setter
    def enable_binding_cookie(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "enable_binding_cookie").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBindingCookie", value)

    @builtins.property
    @jsii.member(jsii_name="httpOnlyCookieAttribute")
    def http_only_cookie_attribute(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpOnlyCookieAttribute"))

    @http_only_cookie_attribute.setter
    def http_only_cookie_attribute(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "http_only_cookie_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpOnlyCookieAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logoUrl")
    def logo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoUrl"))

    @logo_url.setter
    def logo_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "logo_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sameSiteCookieAttribute")
    def same_site_cookie_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sameSiteCookieAttribute"))

    @same_site_cookie_attribute.setter
    def same_site_cookie_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "same_site_cookie_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sameSiteCookieAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAuth401Redirect")
    def service_auth401_redirect(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serviceAuth401Redirect"))

    @service_auth401_redirect.setter
    def service_auth401_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "service_auth401_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAuth401Redirect", value)

    @builtins.property
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "session_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="skipInterstitial")
    def skip_interstitial(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipInterstitial"))

    @skip_interstitial.setter
    def skip_interstitial(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "skip_interstitial").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipInterstitial", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplication, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "account_id": "accountId",
        "allowed_idps": "allowedIdps",
        "app_launcher_visible": "appLauncherVisible",
        "auto_redirect_to_identity": "autoRedirectToIdentity",
        "cors_headers": "corsHeaders",
        "custom_deny_message": "customDenyMessage",
        "custom_deny_url": "customDenyUrl",
        "domain": "domain",
        "enable_binding_cookie": "enableBindingCookie",
        "http_only_cookie_attribute": "httpOnlyCookieAttribute",
        "id": "id",
        "logo_url": "logoUrl",
        "saas_app": "saasApp",
        "same_site_cookie_attribute": "sameSiteCookieAttribute",
        "service_auth401_redirect": "serviceAuth401Redirect",
        "session_duration": "sessionDuration",
        "skip_interstitial": "skipInterstitial",
        "type": "type",
        "zone_id": "zoneId",
    },
)
class AccessApplicationConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allowed_idps: typing.Optional[typing.Sequence[builtins.str]] = None,
        app_launcher_visible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_redirect_to_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessApplicationCorsHeaders", typing.Dict[str, typing.Any]]]]] = None,
        custom_deny_message: typing.Optional[builtins.str] = None,
        custom_deny_url: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        enable_binding_cookie: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_only_cookie_attribute: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        logo_url: typing.Optional[builtins.str] = None,
        saas_app: typing.Optional[typing.Union["AccessApplicationSaasApp", typing.Dict[str, typing.Any]]] = None,
        same_site_cookie_attribute: typing.Optional[builtins.str] = None,
        service_auth401_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        session_duration: typing.Optional[builtins.str] = None,
        skip_interstitial: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Friendly name of the Access Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name AccessApplication#name}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#account_id AccessApplication#account_id}
        :param allowed_idps: The identity providers selected for the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_idps AccessApplication#allowed_idps}
        :param app_launcher_visible: Option to show/hide applications in App Launcher. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#app_launcher_visible AccessApplication#app_launcher_visible}
        :param auto_redirect_to_identity: Option to skip identity provider selection if only one is configured in ``allowed_idps``. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#auto_redirect_to_identity AccessApplication#auto_redirect_to_identity}
        :param cors_headers: cors_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#cors_headers AccessApplication#cors_headers}
        :param custom_deny_message: Option that returns a custom error message when a user is denied access to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_message AccessApplication#custom_deny_message}
        :param custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_url AccessApplication#custom_deny_url}
        :param domain: The complete URL of the asset you wish to put Cloudflare Access in front of. Can include subdomains or paths. Or both. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#domain AccessApplication#domain}
        :param enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#enable_binding_cookie AccessApplication#enable_binding_cookie}
        :param http_only_cookie_attribute: Option to add the ``HttpOnly`` cookie flag to access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#http_only_cookie_attribute AccessApplication#http_only_cookie_attribute}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#id AccessApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logo_url: Image URL for the logo shown in the app launcher dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#logo_url AccessApplication#logo_url}
        :param saas_app: saas_app block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#saas_app AccessApplication#saas_app}
        :param same_site_cookie_attribute: Defines the same-site cookie setting for access tokens. Available values: ``none``, ``lax``, ``strict``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#same_site_cookie_attribute AccessApplication#same_site_cookie_attribute}
        :param service_auth401_redirect: Option to return a 401 status code in service authentication rules on failed requests. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#service_auth_401_redirect AccessApplication#service_auth_401_redirect}
        :param session_duration: How often a user will be forced to re-authorise. Must be in the format ``48h`` or ``2h45m``. Defaults to ``24h``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#session_duration AccessApplication#session_duration}
        :param skip_interstitial: Option to skip the authorization interstitial when using the CLI. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#skip_interstitial AccessApplication#skip_interstitial}
        :param type: The application type. Available values: ``self_hosted``, ``saas``, ``ssh``, ``vnc``, ``bookmark``. Defaults to ``self_hosted``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#type AccessApplication#type}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#zone_id AccessApplication#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(saas_app, dict):
            saas_app = AccessApplicationSaasApp(**saas_app)
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplicationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument allowed_idps", value=allowed_idps, expected_type=type_hints["allowed_idps"])
            check_type(argname="argument app_launcher_visible", value=app_launcher_visible, expected_type=type_hints["app_launcher_visible"])
            check_type(argname="argument auto_redirect_to_identity", value=auto_redirect_to_identity, expected_type=type_hints["auto_redirect_to_identity"])
            check_type(argname="argument cors_headers", value=cors_headers, expected_type=type_hints["cors_headers"])
            check_type(argname="argument custom_deny_message", value=custom_deny_message, expected_type=type_hints["custom_deny_message"])
            check_type(argname="argument custom_deny_url", value=custom_deny_url, expected_type=type_hints["custom_deny_url"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument enable_binding_cookie", value=enable_binding_cookie, expected_type=type_hints["enable_binding_cookie"])
            check_type(argname="argument http_only_cookie_attribute", value=http_only_cookie_attribute, expected_type=type_hints["http_only_cookie_attribute"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logo_url", value=logo_url, expected_type=type_hints["logo_url"])
            check_type(argname="argument saas_app", value=saas_app, expected_type=type_hints["saas_app"])
            check_type(argname="argument same_site_cookie_attribute", value=same_site_cookie_attribute, expected_type=type_hints["same_site_cookie_attribute"])
            check_type(argname="argument service_auth401_redirect", value=service_auth401_redirect, expected_type=type_hints["service_auth401_redirect"])
            check_type(argname="argument session_duration", value=session_duration, expected_type=type_hints["session_duration"])
            check_type(argname="argument skip_interstitial", value=skip_interstitial, expected_type=type_hints["skip_interstitial"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if allowed_idps is not None:
            self._values["allowed_idps"] = allowed_idps
        if app_launcher_visible is not None:
            self._values["app_launcher_visible"] = app_launcher_visible
        if auto_redirect_to_identity is not None:
            self._values["auto_redirect_to_identity"] = auto_redirect_to_identity
        if cors_headers is not None:
            self._values["cors_headers"] = cors_headers
        if custom_deny_message is not None:
            self._values["custom_deny_message"] = custom_deny_message
        if custom_deny_url is not None:
            self._values["custom_deny_url"] = custom_deny_url
        if domain is not None:
            self._values["domain"] = domain
        if enable_binding_cookie is not None:
            self._values["enable_binding_cookie"] = enable_binding_cookie
        if http_only_cookie_attribute is not None:
            self._values["http_only_cookie_attribute"] = http_only_cookie_attribute
        if id is not None:
            self._values["id"] = id
        if logo_url is not None:
            self._values["logo_url"] = logo_url
        if saas_app is not None:
            self._values["saas_app"] = saas_app
        if same_site_cookie_attribute is not None:
            self._values["same_site_cookie_attribute"] = same_site_cookie_attribute
        if service_auth401_redirect is not None:
            self._values["service_auth401_redirect"] = service_auth401_redirect
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if skip_interstitial is not None:
            self._values["skip_interstitial"] = skip_interstitial
        if type is not None:
            self._values["type"] = type
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def name(self) -> builtins.str:
        '''Friendly name of the Access Application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name AccessApplication#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Conflicts with ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#account_id AccessApplication#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_idps(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identity providers selected for the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_idps AccessApplication#allowed_idps}
        '''
        result = self._values.get("allowed_idps")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def app_launcher_visible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to show/hide applications in App Launcher. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#app_launcher_visible AccessApplication#app_launcher_visible}
        '''
        result = self._values.get("app_launcher_visible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_redirect_to_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to skip identity provider selection if only one is configured in ``allowed_idps``. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#auto_redirect_to_identity AccessApplication#auto_redirect_to_identity}
        '''
        result = self._values.get("auto_redirect_to_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cors_headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessApplicationCorsHeaders"]]]:
        '''cors_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#cors_headers AccessApplication#cors_headers}
        '''
        result = self._values.get("cors_headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessApplicationCorsHeaders"]]], result)

    @builtins.property
    def custom_deny_message(self) -> typing.Optional[builtins.str]:
        '''Option that returns a custom error message when a user is denied access to the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_message AccessApplication#custom_deny_message}
        '''
        result = self._values.get("custom_deny_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_deny_url(self) -> typing.Optional[builtins.str]:
        '''Option that redirects to a custom URL when a user is denied access to the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#custom_deny_url AccessApplication#custom_deny_url}
        '''
        result = self._values.get("custom_deny_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The complete URL of the asset you wish to put Cloudflare Access in front of.

        Can include subdomains or paths. Or both.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#domain AccessApplication#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_binding_cookie(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests.

        Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#enable_binding_cookie AccessApplication#enable_binding_cookie}
        '''
        result = self._values.get("enable_binding_cookie")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_only_cookie_attribute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to add the ``HttpOnly`` cookie flag to access tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#http_only_cookie_attribute AccessApplication#http_only_cookie_attribute}
        '''
        result = self._values.get("http_only_cookie_attribute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#id AccessApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logo_url(self) -> typing.Optional[builtins.str]:
        '''Image URL for the logo shown in the app launcher dashboard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#logo_url AccessApplication#logo_url}
        '''
        result = self._values.get("logo_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saas_app(self) -> typing.Optional["AccessApplicationSaasApp"]:
        '''saas_app block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#saas_app AccessApplication#saas_app}
        '''
        result = self._values.get("saas_app")
        return typing.cast(typing.Optional["AccessApplicationSaasApp"], result)

    @builtins.property
    def same_site_cookie_attribute(self) -> typing.Optional[builtins.str]:
        '''Defines the same-site cookie setting for access tokens. Available values: ``none``, ``lax``, ``strict``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#same_site_cookie_attribute AccessApplication#same_site_cookie_attribute}
        '''
        result = self._values.get("same_site_cookie_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_auth401_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to return a 401 status code in service authentication rules on failed requests. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#service_auth_401_redirect AccessApplication#service_auth_401_redirect}
        '''
        result = self._values.get("service_auth401_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''How often a user will be forced to re-authorise.

        Must be in the format ``48h`` or ``2h45m``. Defaults to ``24h``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#session_duration AccessApplication#session_duration}
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_interstitial(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to skip the authorization interstitial when using the CLI. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#skip_interstitial AccessApplication#skip_interstitial}
        '''
        result = self._values.get("skip_interstitial")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The application type. Available values: ``self_hosted``, ``saas``, ``ssh``, ``vnc``, ``bookmark``. Defaults to ``self_hosted``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#type AccessApplication#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Conflicts with ``account_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#zone_id AccessApplication#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationCorsHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "allow_all_headers": "allowAllHeaders",
        "allow_all_methods": "allowAllMethods",
        "allow_all_origins": "allowAllOrigins",
        "allow_credentials": "allowCredentials",
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "max_age": "maxAge",
    },
)
class AccessApplicationCorsHeaders:
    def __init__(
        self,
        *,
        allow_all_headers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_all_methods: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_all_origins: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_all_headers: Value to determine whether all HTTP headers are exposed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_headers AccessApplication#allow_all_headers}
        :param allow_all_methods: Value to determine whether all methods are exposed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_methods AccessApplication#allow_all_methods}
        :param allow_all_origins: Value to determine whether all origins are permitted to make CORS requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_origins AccessApplication#allow_all_origins}
        :param allow_credentials: Value to determine if credentials (cookies, authorization headers, or TLS client certificates) are included with requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_credentials AccessApplication#allow_credentials}
        :param allowed_headers: List of HTTP headers to expose via CORS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_headers AccessApplication#allowed_headers}
        :param allowed_methods: List of methods to expose via CORS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_methods AccessApplication#allowed_methods}
        :param allowed_origins: List of origins permitted to make CORS requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_origins AccessApplication#allowed_origins}
        :param max_age: The maximum time a preflight request will be cached. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#max_age AccessApplication#max_age}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplicationCorsHeaders.__init__)
            check_type(argname="argument allow_all_headers", value=allow_all_headers, expected_type=type_hints["allow_all_headers"])
            check_type(argname="argument allow_all_methods", value=allow_all_methods, expected_type=type_hints["allow_all_methods"])
            check_type(argname="argument allow_all_origins", value=allow_all_origins, expected_type=type_hints["allow_all_origins"])
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_all_headers is not None:
            self._values["allow_all_headers"] = allow_all_headers
        if allow_all_methods is not None:
            self._values["allow_all_methods"] = allow_all_methods
        if allow_all_origins is not None:
            self._values["allow_all_origins"] = allow_all_origins
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allowed_headers is not None:
            self._values["allowed_headers"] = allowed_headers
        if allowed_methods is not None:
            self._values["allowed_methods"] = allowed_methods
        if allowed_origins is not None:
            self._values["allowed_origins"] = allowed_origins
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_all_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Value to determine whether all HTTP headers are exposed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_headers AccessApplication#allow_all_headers}
        '''
        result = self._values.get("allow_all_headers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_all_methods(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Value to determine whether all methods are exposed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_methods AccessApplication#allow_all_methods}
        '''
        result = self._values.get("allow_all_methods")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_all_origins(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Value to determine whether all origins are permitted to make CORS requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_all_origins AccessApplication#allow_all_origins}
        '''
        result = self._values.get("allow_all_origins")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Value to determine if credentials (cookies, authorization headers, or TLS client certificates) are included with requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allow_credentials AccessApplication#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allowed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of HTTP headers to expose via CORS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_headers AccessApplication#allowed_headers}
        '''
        result = self._values.get("allowed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of methods to expose via CORS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_methods AccessApplication#allowed_methods}
        '''
        result = self._values.get("allowed_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of origins permitted to make CORS requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#allowed_origins AccessApplication#allowed_origins}
        '''
        result = self._values.get("allowed_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''The maximum time a preflight request will be cached.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#max_age AccessApplication#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessApplicationCorsHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessApplicationCorsHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationCorsHeadersList",
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
            type_hints = typing.get_type_hints(AccessApplicationCorsHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessApplicationCorsHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplicationCorsHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessApplicationCorsHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessApplicationCorsHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessApplicationCorsHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessApplicationCorsHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessApplicationCorsHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationCorsHeadersOutputReference",
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
            type_hints = typing.get_type_hints(AccessApplicationCorsHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowAllHeaders")
    def reset_allow_all_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowAllHeaders", []))

    @jsii.member(jsii_name="resetAllowAllMethods")
    def reset_allow_all_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowAllMethods", []))

    @jsii.member(jsii_name="resetAllowAllOrigins")
    def reset_allow_all_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowAllOrigins", []))

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowedHeaders")
    def reset_allowed_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHeaders", []))

    @jsii.member(jsii_name="resetAllowedMethods")
    def reset_allowed_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedMethods", []))

    @jsii.member(jsii_name="resetAllowedOrigins")
    def reset_allowed_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOrigins", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowAllHeadersInput")
    def allow_all_headers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowAllHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowAllMethodsInput")
    def allow_all_methods_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowAllMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowAllOriginsInput")
    def allow_all_origins_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowAllOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowAllHeaders")
    def allow_all_headers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowAllHeaders"))

    @allow_all_headers.setter
    def allow_all_headers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allow_all_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAllHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowAllMethods")
    def allow_all_methods(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowAllMethods"))

    @allow_all_methods.setter
    def allow_all_methods(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allow_all_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAllMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowAllOrigins")
    def allow_all_origins(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowAllOrigins"))

    @allow_all_origins.setter
    def allow_all_origins(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allow_all_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAllOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessApplicationCorsHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessApplicationCorsHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessApplicationCorsHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationCorsHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationSaasApp",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_service_url": "consumerServiceUrl",
        "sp_entity_id": "spEntityId",
        "name_id_format": "nameIdFormat",
    },
)
class AccessApplicationSaasApp:
    def __init__(
        self,
        *,
        consumer_service_url: builtins.str,
        sp_entity_id: builtins.str,
        name_id_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_service_url: The service provider's endpoint that is responsible for receiving and parsing a SAML assertion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#consumer_service_url AccessApplication#consumer_service_url}
        :param sp_entity_id: A globally unique name for an identity or service provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#sp_entity_id AccessApplication#sp_entity_id}
        :param name_id_format: The format of the name identifier sent to the SaaS application. Defaults to ``email``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name_id_format AccessApplication#name_id_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessApplicationSaasApp.__init__)
            check_type(argname="argument consumer_service_url", value=consumer_service_url, expected_type=type_hints["consumer_service_url"])
            check_type(argname="argument sp_entity_id", value=sp_entity_id, expected_type=type_hints["sp_entity_id"])
            check_type(argname="argument name_id_format", value=name_id_format, expected_type=type_hints["name_id_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "consumer_service_url": consumer_service_url,
            "sp_entity_id": sp_entity_id,
        }
        if name_id_format is not None:
            self._values["name_id_format"] = name_id_format

    @builtins.property
    def consumer_service_url(self) -> builtins.str:
        '''The service provider's endpoint that is responsible for receiving and parsing a SAML assertion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#consumer_service_url AccessApplication#consumer_service_url}
        '''
        result = self._values.get("consumer_service_url")
        assert result is not None, "Required property 'consumer_service_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sp_entity_id(self) -> builtins.str:
        '''A globally unique name for an identity or service provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#sp_entity_id AccessApplication#sp_entity_id}
        '''
        result = self._values.get("sp_entity_id")
        assert result is not None, "Required property 'sp_entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name_id_format(self) -> typing.Optional[builtins.str]:
        '''The format of the name identifier sent to the SaaS application. Defaults to ``email``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_application#name_id_format AccessApplication#name_id_format}
        '''
        result = self._values.get("name_id_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessApplicationSaasApp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessApplicationSaasAppOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessApplication.AccessApplicationSaasAppOutputReference",
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
            type_hints = typing.get_type_hints(AccessApplicationSaasAppOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNameIdFormat")
    def reset_name_id_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameIdFormat", []))

    @builtins.property
    @jsii.member(jsii_name="consumerServiceUrlInput")
    def consumer_service_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerServiceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameIdFormatInput")
    def name_id_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameIdFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="spEntityIdInput")
    def sp_entity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spEntityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerServiceUrl")
    def consumer_service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerServiceUrl"))

    @consumer_service_url.setter
    def consumer_service_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationSaasAppOutputReference, "consumer_service_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerServiceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="nameIdFormat")
    def name_id_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameIdFormat"))

    @name_id_format.setter
    def name_id_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationSaasAppOutputReference, "name_id_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameIdFormat", value)

    @builtins.property
    @jsii.member(jsii_name="spEntityId")
    def sp_entity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spEntityId"))

    @sp_entity_id.setter
    def sp_entity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationSaasAppOutputReference, "sp_entity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spEntityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessApplicationSaasApp]:
        return typing.cast(typing.Optional[AccessApplicationSaasApp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AccessApplicationSaasApp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessApplicationSaasAppOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AccessApplication",
    "AccessApplicationConfig",
    "AccessApplicationCorsHeaders",
    "AccessApplicationCorsHeadersList",
    "AccessApplicationCorsHeadersOutputReference",
    "AccessApplicationSaasApp",
    "AccessApplicationSaasAppOutputReference",
]

publication.publish()
