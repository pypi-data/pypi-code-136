'''
# `azuread_application`

Refer to the Terraform Registory for docs: [`azuread_application`](https://www.terraform.io/docs/providers/azuread/r/application).
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


class Application(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.Application",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/application azuread_application}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        api: typing.Optional[typing.Union["ApplicationApi", typing.Dict[str, typing.Any]]] = None,
        app_role: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationAppRole", typing.Dict[str, typing.Any]]]]] = None,
        device_only_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fallback_public_client_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        feature_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationFeatureTags", typing.Dict[str, typing.Any]]]]] = None,
        group_membership_claims: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logo_image: typing.Optional[builtins.str] = None,
        marketing_url: typing.Optional[builtins.str] = None,
        oauth2_post_response_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optional_claims: typing.Optional[typing.Union["ApplicationOptionalClaims", typing.Dict[str, typing.Any]]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        privacy_statement_url: typing.Optional[builtins.str] = None,
        public_client: typing.Optional[typing.Union["ApplicationPublicClient", typing.Dict[str, typing.Any]]] = None,
        required_resource_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationRequiredResourceAccess", typing.Dict[str, typing.Any]]]]] = None,
        sign_in_audience: typing.Optional[builtins.str] = None,
        single_page_application: typing.Optional[typing.Union["ApplicationSinglePageApplication", typing.Dict[str, typing.Any]]] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_id: typing.Optional[builtins.str] = None,
        terms_of_service_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationTimeouts", typing.Dict[str, typing.Any]]] = None,
        web: typing.Optional[typing.Union["ApplicationWeb", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/application azuread_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The display name for the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#display_name Application#display_name}
        :param api: api block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#api Application#api}
        :param app_role: app_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#app_role Application#app_role}
        :param device_only_auth_enabled: Specifies whether this application supports device authentication without a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#device_only_auth_enabled Application#device_only_auth_enabled}
        :param fallback_public_client_enabled: Specifies whether the application is a public client. Appropriate for apps using token grant flows that don't use a redirect URI Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#fallback_public_client_enabled Application#fallback_public_client_enabled}
        :param feature_tags: feature_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#feature_tags Application#feature_tags}
        :param group_membership_claims: Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#group_membership_claims Application#group_membership_claims}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier_uris: The user-defined URI(s) that uniquely identify an application within its Azure AD tenant, or within a verified custom domain if the application is multi-tenant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#identifier_uris Application#identifier_uris}
        :param logo_image: Base64 encoded logo image in gif, png or jpeg format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logo_image Application#logo_image}
        :param marketing_url: URL of the application's marketing page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#marketing_url Application#marketing_url}
        :param oauth2_post_response_required: Specifies whether, as part of OAuth 2.0 token requests, Azure AD allows POST requests, as opposed to GET requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_post_response_required Application#oauth2_post_response_required}
        :param optional_claims: optional_claims block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#optional_claims Application#optional_claims}
        :param owners: A list of object IDs of principals that will be granted ownership of the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#owners Application#owners}
        :param prevent_duplicate_names: If ``true``, will return an error if an existing application is found with the same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#prevent_duplicate_names Application#prevent_duplicate_names}
        :param privacy_statement_url: URL of the application's privacy statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#privacy_statement_url Application#privacy_statement_url}
        :param public_client: public_client block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#public_client Application#public_client}
        :param required_resource_access: required_resource_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#required_resource_access Application#required_resource_access}
        :param sign_in_audience: The Microsoft account types that are supported for the current application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#sign_in_audience Application#sign_in_audience}
        :param single_page_application: single_page_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#single_page_application Application#single_page_application}
        :param support_url: URL of the application's support page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#support_url Application#support_url}
        :param tags: A set of tags to apply to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#tags Application#tags}
        :param template_id: Unique ID of the application template from which this application is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#template_id Application#template_id}
        :param terms_of_service_url: URL of the application's terms of service statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#terms_of_service_url Application#terms_of_service_url}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#timeouts Application#timeouts}
        :param web: web block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#web Application#web}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Application.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationConfig(
            display_name=display_name,
            api=api,
            app_role=app_role,
            device_only_auth_enabled=device_only_auth_enabled,
            fallback_public_client_enabled=fallback_public_client_enabled,
            feature_tags=feature_tags,
            group_membership_claims=group_membership_claims,
            id=id,
            identifier_uris=identifier_uris,
            logo_image=logo_image,
            marketing_url=marketing_url,
            oauth2_post_response_required=oauth2_post_response_required,
            optional_claims=optional_claims,
            owners=owners,
            prevent_duplicate_names=prevent_duplicate_names,
            privacy_statement_url=privacy_statement_url,
            public_client=public_client,
            required_resource_access=required_resource_access,
            sign_in_audience=sign_in_audience,
            single_page_application=single_page_application,
            support_url=support_url,
            tags=tags,
            template_id=template_id,
            terms_of_service_url=terms_of_service_url,
            timeouts=timeouts,
            web=web,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApi")
    def put_api(
        self,
        *,
        known_client_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        mapped_claims_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oauth2_permission_scope: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationApiOauth2PermissionScope", typing.Dict[str, typing.Any]]]]] = None,
        requested_access_token_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param known_client_applications: Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#known_client_applications Application#known_client_applications}
        :param mapped_claims_enabled: Allows an application to use claims mapping without specifying a custom signing key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#mapped_claims_enabled Application#mapped_claims_enabled}
        :param oauth2_permission_scope: oauth2_permission_scope block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_permission_scope Application#oauth2_permission_scope}
        :param requested_access_token_version: The access token version expected by this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#requested_access_token_version Application#requested_access_token_version}
        '''
        value = ApplicationApi(
            known_client_applications=known_client_applications,
            mapped_claims_enabled=mapped_claims_enabled,
            oauth2_permission_scope=oauth2_permission_scope,
            requested_access_token_version=requested_access_token_version,
        )

        return typing.cast(None, jsii.invoke(self, "putApi", [value]))

    @jsii.member(jsii_name="putAppRole")
    def put_app_role(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationAppRole", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Application.put_app_role)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAppRole", [value]))

    @jsii.member(jsii_name="putFeatureTags")
    def put_feature_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationFeatureTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Application.put_feature_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFeatureTags", [value]))

    @jsii.member(jsii_name="putOptionalClaims")
    def put_optional_claims(
        self,
        *,
        access_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsAccessToken", typing.Dict[str, typing.Any]]]]] = None,
        id_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsIdToken", typing.Dict[str, typing.Any]]]]] = None,
        saml2_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsSaml2Token", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param access_token: access_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token Application#access_token}
        :param id_token: id_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token Application#id_token}
        :param saml2_token: saml2_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#saml2_token Application#saml2_token}
        '''
        value = ApplicationOptionalClaims(
            access_token=access_token, id_token=id_token, saml2_token=saml2_token
        )

        return typing.cast(None, jsii.invoke(self, "putOptionalClaims", [value]))

    @jsii.member(jsii_name="putPublicClient")
    def put_public_client(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        value = ApplicationPublicClient(redirect_uris=redirect_uris)

        return typing.cast(None, jsii.invoke(self, "putPublicClient", [value]))

    @jsii.member(jsii_name="putRequiredResourceAccess")
    def put_required_resource_access(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationRequiredResourceAccess", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Application.put_required_resource_access)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequiredResourceAccess", [value]))

    @jsii.member(jsii_name="putSinglePageApplication")
    def put_single_page_application(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        value = ApplicationSinglePageApplication(redirect_uris=redirect_uris)

        return typing.cast(None, jsii.invoke(self, "putSinglePageApplication", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#create Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#delete Application#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#read Application#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#update Application#update}.
        '''
        value = ApplicationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWeb")
    def put_web(
        self,
        *,
        homepage_url: typing.Optional[builtins.str] = None,
        implicit_grant: typing.Optional[typing.Union["ApplicationWebImplicitGrant", typing.Dict[str, typing.Any]]] = None,
        logout_url: typing.Optional[builtins.str] = None,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param homepage_url: Home page or landing page of the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#homepage_url Application#homepage_url}
        :param implicit_grant: implicit_grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#implicit_grant Application#implicit_grant}
        :param logout_url: The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logout_url Application#logout_url}
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        value = ApplicationWeb(
            homepage_url=homepage_url,
            implicit_grant=implicit_grant,
            logout_url=logout_url,
            redirect_uris=redirect_uris,
        )

        return typing.cast(None, jsii.invoke(self, "putWeb", [value]))

    @jsii.member(jsii_name="resetApi")
    def reset_api(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApi", []))

    @jsii.member(jsii_name="resetAppRole")
    def reset_app_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppRole", []))

    @jsii.member(jsii_name="resetDeviceOnlyAuthEnabled")
    def reset_device_only_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceOnlyAuthEnabled", []))

    @jsii.member(jsii_name="resetFallbackPublicClientEnabled")
    def reset_fallback_public_client_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackPublicClientEnabled", []))

    @jsii.member(jsii_name="resetFeatureTags")
    def reset_feature_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureTags", []))

    @jsii.member(jsii_name="resetGroupMembershipClaims")
    def reset_group_membership_claims(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupMembershipClaims", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentifierUris")
    def reset_identifier_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifierUris", []))

    @jsii.member(jsii_name="resetLogoImage")
    def reset_logo_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoImage", []))

    @jsii.member(jsii_name="resetMarketingUrl")
    def reset_marketing_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketingUrl", []))

    @jsii.member(jsii_name="resetOauth2PostResponseRequired")
    def reset_oauth2_post_response_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2PostResponseRequired", []))

    @jsii.member(jsii_name="resetOptionalClaims")
    def reset_optional_claims(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionalClaims", []))

    @jsii.member(jsii_name="resetOwners")
    def reset_owners(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwners", []))

    @jsii.member(jsii_name="resetPreventDuplicateNames")
    def reset_prevent_duplicate_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreventDuplicateNames", []))

    @jsii.member(jsii_name="resetPrivacyStatementUrl")
    def reset_privacy_statement_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivacyStatementUrl", []))

    @jsii.member(jsii_name="resetPublicClient")
    def reset_public_client(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicClient", []))

    @jsii.member(jsii_name="resetRequiredResourceAccess")
    def reset_required_resource_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredResourceAccess", []))

    @jsii.member(jsii_name="resetSignInAudience")
    def reset_sign_in_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignInAudience", []))

    @jsii.member(jsii_name="resetSinglePageApplication")
    def reset_single_page_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSinglePageApplication", []))

    @jsii.member(jsii_name="resetSupportUrl")
    def reset_support_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportUrl", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTemplateId")
    def reset_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateId", []))

    @jsii.member(jsii_name="resetTermsOfServiceUrl")
    def reset_terms_of_service_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTermsOfServiceUrl", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWeb")
    def reset_web(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeb", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def api(self) -> "ApplicationApiOutputReference":
        return typing.cast("ApplicationApiOutputReference", jsii.get(self, "api"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="appRole")
    def app_role(self) -> "ApplicationAppRoleList":
        return typing.cast("ApplicationAppRoleList", jsii.get(self, "appRole"))

    @builtins.property
    @jsii.member(jsii_name="appRoleIds")
    def app_role_ids(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "appRoleIds"))

    @builtins.property
    @jsii.member(jsii_name="disabledByMicrosoft")
    def disabled_by_microsoft(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disabledByMicrosoft"))

    @builtins.property
    @jsii.member(jsii_name="featureTags")
    def feature_tags(self) -> "ApplicationFeatureTagsList":
        return typing.cast("ApplicationFeatureTagsList", jsii.get(self, "featureTags"))

    @builtins.property
    @jsii.member(jsii_name="logoUrl")
    def logo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoUrl"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PermissionScopeIds")
    def oauth2_permission_scope_ids(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "oauth2PermissionScopeIds"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="optionalClaims")
    def optional_claims(self) -> "ApplicationOptionalClaimsOutputReference":
        return typing.cast("ApplicationOptionalClaimsOutputReference", jsii.get(self, "optionalClaims"))

    @builtins.property
    @jsii.member(jsii_name="publicClient")
    def public_client(self) -> "ApplicationPublicClientOutputReference":
        return typing.cast("ApplicationPublicClientOutputReference", jsii.get(self, "publicClient"))

    @builtins.property
    @jsii.member(jsii_name="publisherDomain")
    def publisher_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisherDomain"))

    @builtins.property
    @jsii.member(jsii_name="requiredResourceAccess")
    def required_resource_access(self) -> "ApplicationRequiredResourceAccessList":
        return typing.cast("ApplicationRequiredResourceAccessList", jsii.get(self, "requiredResourceAccess"))

    @builtins.property
    @jsii.member(jsii_name="singlePageApplication")
    def single_page_application(
        self,
    ) -> "ApplicationSinglePageApplicationOutputReference":
        return typing.cast("ApplicationSinglePageApplicationOutputReference", jsii.get(self, "singlePageApplication"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApplicationTimeoutsOutputReference":
        return typing.cast("ApplicationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="web")
    def web(self) -> "ApplicationWebOutputReference":
        return typing.cast("ApplicationWebOutputReference", jsii.get(self, "web"))

    @builtins.property
    @jsii.member(jsii_name="apiInput")
    def api_input(self) -> typing.Optional["ApplicationApi"]:
        return typing.cast(typing.Optional["ApplicationApi"], jsii.get(self, "apiInput"))

    @builtins.property
    @jsii.member(jsii_name="appRoleInput")
    def app_role_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationAppRole"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationAppRole"]]], jsii.get(self, "appRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceOnlyAuthEnabledInput")
    def device_only_auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deviceOnlyAuthEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackPublicClientEnabledInput")
    def fallback_public_client_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallbackPublicClientEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="featureTagsInput")
    def feature_tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationFeatureTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationFeatureTags"]]], jsii.get(self, "featureTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupMembershipClaimsInput")
    def group_membership_claims_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupMembershipClaimsInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierUrisInput")
    def identifier_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identifierUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logoImageInput")
    def logo_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoImageInput"))

    @builtins.property
    @jsii.member(jsii_name="marketingUrlInput")
    def marketing_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marketingUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PostResponseRequiredInput")
    def oauth2_post_response_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "oauth2PostResponseRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalClaimsInput")
    def optional_claims_input(self) -> typing.Optional["ApplicationOptionalClaims"]:
        return typing.cast(typing.Optional["ApplicationOptionalClaims"], jsii.get(self, "optionalClaimsInput"))

    @builtins.property
    @jsii.member(jsii_name="ownersInput")
    def owners_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ownersInput"))

    @builtins.property
    @jsii.member(jsii_name="preventDuplicateNamesInput")
    def prevent_duplicate_names_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preventDuplicateNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="privacyStatementUrlInput")
    def privacy_statement_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privacyStatementUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="publicClientInput")
    def public_client_input(self) -> typing.Optional["ApplicationPublicClient"]:
        return typing.cast(typing.Optional["ApplicationPublicClient"], jsii.get(self, "publicClientInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredResourceAccessInput")
    def required_resource_access_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccess"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccess"]]], jsii.get(self, "requiredResourceAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="signInAudienceInput")
    def sign_in_audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signInAudienceInput"))

    @builtins.property
    @jsii.member(jsii_name="singlePageApplicationInput")
    def single_page_application_input(
        self,
    ) -> typing.Optional["ApplicationSinglePageApplication"]:
        return typing.cast(typing.Optional["ApplicationSinglePageApplication"], jsii.get(self, "singlePageApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="supportUrlInput")
    def support_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="templateIdInput")
    def template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="termsOfServiceUrlInput")
    def terms_of_service_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "termsOfServiceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApplicationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApplicationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="webInput")
    def web_input(self) -> typing.Optional["ApplicationWeb"]:
        return typing.cast(typing.Optional["ApplicationWeb"], jsii.get(self, "webInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceOnlyAuthEnabled")
    def device_only_auth_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deviceOnlyAuthEnabled"))

    @device_only_auth_enabled.setter
    def device_only_auth_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "device_only_auth_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceOnlyAuthEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackPublicClientEnabled")
    def fallback_public_client_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fallbackPublicClientEnabled"))

    @fallback_public_client_enabled.setter
    def fallback_public_client_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "fallback_public_client_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackPublicClientEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="groupMembershipClaims")
    def group_membership_claims(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupMembershipClaims"))

    @group_membership_claims.setter
    def group_membership_claims(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "group_membership_claims").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupMembershipClaims", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identifierUris")
    def identifier_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identifierUris"))

    @identifier_uris.setter
    def identifier_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "identifier_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifierUris", value)

    @builtins.property
    @jsii.member(jsii_name="logoImage")
    def logo_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoImage"))

    @logo_image.setter
    def logo_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "logo_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoImage", value)

    @builtins.property
    @jsii.member(jsii_name="marketingUrl")
    def marketing_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "marketingUrl"))

    @marketing_url.setter
    def marketing_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "marketing_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "marketingUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2PostResponseRequired")
    def oauth2_post_response_required(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "oauth2PostResponseRequired"))

    @oauth2_post_response_required.setter
    def oauth2_post_response_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "oauth2_post_response_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2PostResponseRequired", value)

    @builtins.property
    @jsii.member(jsii_name="owners")
    def owners(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "owners"))

    @owners.setter
    def owners(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "owners").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owners", value)

    @builtins.property
    @jsii.member(jsii_name="preventDuplicateNames")
    def prevent_duplicate_names(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preventDuplicateNames"))

    @prevent_duplicate_names.setter
    def prevent_duplicate_names(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "prevent_duplicate_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preventDuplicateNames", value)

    @builtins.property
    @jsii.member(jsii_name="privacyStatementUrl")
    def privacy_statement_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privacyStatementUrl"))

    @privacy_statement_url.setter
    def privacy_statement_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "privacy_statement_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privacyStatementUrl", value)

    @builtins.property
    @jsii.member(jsii_name="signInAudience")
    def sign_in_audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signInAudience"))

    @sign_in_audience.setter
    def sign_in_audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "sign_in_audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signInAudience", value)

    @builtins.property
    @jsii.member(jsii_name="supportUrl")
    def support_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportUrl"))

    @support_url.setter
    def support_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "support_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "template_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateId", value)

    @builtins.property
    @jsii.member(jsii_name="termsOfServiceUrl")
    def terms_of_service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "termsOfServiceUrl"))

    @terms_of_service_url.setter
    def terms_of_service_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Application, "terms_of_service_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "termsOfServiceUrl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationApi",
    jsii_struct_bases=[],
    name_mapping={
        "known_client_applications": "knownClientApplications",
        "mapped_claims_enabled": "mappedClaimsEnabled",
        "oauth2_permission_scope": "oauth2PermissionScope",
        "requested_access_token_version": "requestedAccessTokenVersion",
    },
)
class ApplicationApi:
    def __init__(
        self,
        *,
        known_client_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        mapped_claims_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oauth2_permission_scope: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationApiOauth2PermissionScope", typing.Dict[str, typing.Any]]]]] = None,
        requested_access_token_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param known_client_applications: Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#known_client_applications Application#known_client_applications}
        :param mapped_claims_enabled: Allows an application to use claims mapping without specifying a custom signing key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#mapped_claims_enabled Application#mapped_claims_enabled}
        :param oauth2_permission_scope: oauth2_permission_scope block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_permission_scope Application#oauth2_permission_scope}
        :param requested_access_token_version: The access token version expected by this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#requested_access_token_version Application#requested_access_token_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationApi.__init__)
            check_type(argname="argument known_client_applications", value=known_client_applications, expected_type=type_hints["known_client_applications"])
            check_type(argname="argument mapped_claims_enabled", value=mapped_claims_enabled, expected_type=type_hints["mapped_claims_enabled"])
            check_type(argname="argument oauth2_permission_scope", value=oauth2_permission_scope, expected_type=type_hints["oauth2_permission_scope"])
            check_type(argname="argument requested_access_token_version", value=requested_access_token_version, expected_type=type_hints["requested_access_token_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if known_client_applications is not None:
            self._values["known_client_applications"] = known_client_applications
        if mapped_claims_enabled is not None:
            self._values["mapped_claims_enabled"] = mapped_claims_enabled
        if oauth2_permission_scope is not None:
            self._values["oauth2_permission_scope"] = oauth2_permission_scope
        if requested_access_token_version is not None:
            self._values["requested_access_token_version"] = requested_access_token_version

    @builtins.property
    def known_client_applications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#known_client_applications Application#known_client_applications}
        '''
        result = self._values.get("known_client_applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mapped_claims_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows an application to use claims mapping without specifying a custom signing key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#mapped_claims_enabled Application#mapped_claims_enabled}
        '''
        result = self._values.get("mapped_claims_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def oauth2_permission_scope(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationApiOauth2PermissionScope"]]]:
        '''oauth2_permission_scope block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_permission_scope Application#oauth2_permission_scope}
        '''
        result = self._values.get("oauth2_permission_scope")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationApiOauth2PermissionScope"]]], result)

    @builtins.property
    def requested_access_token_version(self) -> typing.Optional[jsii.Number]:
        '''The access token version expected by this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#requested_access_token_version Application#requested_access_token_version}
        '''
        result = self._values.get("requested_access_token_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationApi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationApiOauth2PermissionScope",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "admin_consent_description": "adminConsentDescription",
        "admin_consent_display_name": "adminConsentDisplayName",
        "enabled": "enabled",
        "type": "type",
        "user_consent_description": "userConsentDescription",
        "user_consent_display_name": "userConsentDisplayName",
        "value": "value",
    },
)
class ApplicationApiOauth2PermissionScope:
    def __init__(
        self,
        *,
        id: builtins.str,
        admin_consent_description: typing.Optional[builtins.str] = None,
        admin_consent_display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
        user_consent_description: typing.Optional[builtins.str] = None,
        user_consent_display_name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: The unique identifier of the delegated permission. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param admin_consent_description: Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#admin_consent_description Application#admin_consent_description}
        :param admin_consent_display_name: Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#admin_consent_display_name Application#admin_consent_display_name}
        :param enabled: Determines if the permission scope is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enabled Application#enabled}
        :param type: Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#type Application#type}
        :param user_consent_description: Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#user_consent_description Application#user_consent_description}
        :param user_consent_display_name: Display name for the delegated permission that appears in the end user consent experience. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#user_consent_display_name Application#user_consent_display_name}
        :param value: The value that is used for the ``scp`` claim in OAuth 2.0 access tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationApiOauth2PermissionScope.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument admin_consent_description", value=admin_consent_description, expected_type=type_hints["admin_consent_description"])
            check_type(argname="argument admin_consent_display_name", value=admin_consent_display_name, expected_type=type_hints["admin_consent_display_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_consent_description", value=user_consent_description, expected_type=type_hints["user_consent_description"])
            check_type(argname="argument user_consent_display_name", value=user_consent_display_name, expected_type=type_hints["user_consent_display_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if admin_consent_description is not None:
            self._values["admin_consent_description"] = admin_consent_description
        if admin_consent_display_name is not None:
            self._values["admin_consent_display_name"] = admin_consent_display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if type is not None:
            self._values["type"] = type
        if user_consent_description is not None:
            self._values["user_consent_description"] = user_consent_description
        if user_consent_display_name is not None:
            self._values["user_consent_display_name"] = user_consent_display_name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier of the delegated permission.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_consent_description(self) -> typing.Optional[builtins.str]:
        '''Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#admin_consent_description Application#admin_consent_description}
        '''
        result = self._values.get("admin_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#admin_consent_display_name Application#admin_consent_display_name}
        '''
        result = self._values.get("admin_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if the permission scope is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enabled Application#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#type Application#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_description(self) -> typing.Optional[builtins.str]:
        '''Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#user_consent_description Application#user_consent_description}
        '''
        result = self._values.get("user_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the delegated permission that appears in the end user consent experience.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#user_consent_display_name Application#user_consent_display_name}
        '''
        result = self._values.get("user_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value that is used for the ``scp`` claim in OAuth 2.0 access tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationApiOauth2PermissionScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationApiOauth2PermissionScopeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationApiOauth2PermissionScopeList",
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
            type_hints = typing.get_type_hints(ApplicationApiOauth2PermissionScopeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationApiOauth2PermissionScopeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationApiOauth2PermissionScopeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationApiOauth2PermissionScopeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationApiOauth2PermissionScope]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationApiOauth2PermissionScope]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationApiOauth2PermissionScope]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationApiOauth2PermissionScopeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationApiOauth2PermissionScopeOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationApiOauth2PermissionScopeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdminConsentDescription")
    def reset_admin_consent_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminConsentDescription", []))

    @jsii.member(jsii_name="resetAdminConsentDisplayName")
    def reset_admin_consent_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminConsentDisplayName", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUserConsentDescription")
    def reset_user_consent_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserConsentDescription", []))

    @jsii.member(jsii_name="resetUserConsentDisplayName")
    def reset_user_consent_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserConsentDisplayName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="adminConsentDescriptionInput")
    def admin_consent_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminConsentDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="adminConsentDisplayNameInput")
    def admin_consent_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminConsentDisplayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userConsentDescriptionInput")
    def user_consent_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userConsentDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="userConsentDisplayNameInput")
    def user_consent_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userConsentDisplayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="adminConsentDescription")
    def admin_consent_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminConsentDescription"))

    @admin_consent_description.setter
    def admin_consent_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "admin_consent_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminConsentDescription", value)

    @builtins.property
    @jsii.member(jsii_name="adminConsentDisplayName")
    def admin_consent_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminConsentDisplayName"))

    @admin_consent_display_name.setter
    def admin_consent_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "admin_consent_display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminConsentDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userConsentDescription")
    def user_consent_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userConsentDescription"))

    @user_consent_description.setter
    def user_consent_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "user_consent_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userConsentDescription", value)

    @builtins.property
    @jsii.member(jsii_name="userConsentDisplayName")
    def user_consent_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userConsentDisplayName"))

    @user_consent_display_name.setter
    def user_consent_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "user_consent_display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userConsentDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationApiOauth2PermissionScope, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationApiOauth2PermissionScope, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationApiOauth2PermissionScope, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOauth2PermissionScopeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationApiOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationApiOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationApiOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauth2PermissionScope")
    def put_oauth2_permission_scope(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationApiOauth2PermissionScope, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationApiOutputReference.put_oauth2_permission_scope)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOauth2PermissionScope", [value]))

    @jsii.member(jsii_name="resetKnownClientApplications")
    def reset_known_client_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKnownClientApplications", []))

    @jsii.member(jsii_name="resetMappedClaimsEnabled")
    def reset_mapped_claims_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappedClaimsEnabled", []))

    @jsii.member(jsii_name="resetOauth2PermissionScope")
    def reset_oauth2_permission_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2PermissionScope", []))

    @jsii.member(jsii_name="resetRequestedAccessTokenVersion")
    def reset_requested_access_token_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestedAccessTokenVersion", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2PermissionScope")
    def oauth2_permission_scope(self) -> ApplicationApiOauth2PermissionScopeList:
        return typing.cast(ApplicationApiOauth2PermissionScopeList, jsii.get(self, "oauth2PermissionScope"))

    @builtins.property
    @jsii.member(jsii_name="knownClientApplicationsInput")
    def known_client_applications_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "knownClientApplicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="mappedClaimsEnabledInput")
    def mapped_claims_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mappedClaimsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PermissionScopeInput")
    def oauth2_permission_scope_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationApiOauth2PermissionScope]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationApiOauth2PermissionScope]]], jsii.get(self, "oauth2PermissionScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="requestedAccessTokenVersionInput")
    def requested_access_token_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestedAccessTokenVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="knownClientApplications")
    def known_client_applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "knownClientApplications"))

    @known_client_applications.setter
    def known_client_applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOutputReference, "known_client_applications").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knownClientApplications", value)

    @builtins.property
    @jsii.member(jsii_name="mappedClaimsEnabled")
    def mapped_claims_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mappedClaimsEnabled"))

    @mapped_claims_enabled.setter
    def mapped_claims_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOutputReference, "mapped_claims_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappedClaimsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="requestedAccessTokenVersion")
    def requested_access_token_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestedAccessTokenVersion"))

    @requested_access_token_version.setter
    def requested_access_token_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOutputReference, "requested_access_token_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestedAccessTokenVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationApi]:
        return typing.cast(typing.Optional[ApplicationApi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationApi]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationApiOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationAppRole",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_member_types": "allowedMemberTypes",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "enabled": "enabled",
        "value": "value",
    },
)
class ApplicationAppRole:
    def __init__(
        self,
        *,
        allowed_member_types: typing.Sequence[builtins.str],
        description: builtins.str,
        display_name: builtins.str,
        id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_member_types: Specifies whether this app role definition can be assigned to users and groups by setting to ``User``, or to other applications (that are accessing this application in a standalone scenario) by setting to ``Application``, or to both. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#allowed_member_types Application#allowed_member_types}
        :param description: Description of the app role that appears when the role is being assigned and, if the role functions as an application permissions, during the consent experiences. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#description Application#description}
        :param display_name: Display name for the app role that appears during app role assignment and in consent experiences. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#display_name Application#display_name}
        :param id: The unique identifier of the app role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param enabled: Determines if the app role is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enabled Application#enabled}
        :param value: The value that is used for the ``roles`` claim in ID tokens and OAuth 2.0 access tokens that are authenticating an assigned service or user principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationAppRole.__init__)
            check_type(argname="argument allowed_member_types", value=allowed_member_types, expected_type=type_hints["allowed_member_types"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_member_types": allowed_member_types,
            "description": description,
            "display_name": display_name,
            "id": id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def allowed_member_types(self) -> typing.List[builtins.str]:
        '''Specifies whether this app role definition can be assigned to users and groups by setting to ``User``, or to other applications (that are accessing this application in a standalone scenario) by setting to ``Application``, or to both.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#allowed_member_types Application#allowed_member_types}
        '''
        result = self._values.get("allowed_member_types")
        assert result is not None, "Required property 'allowed_member_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''Description of the app role that appears when the role is being assigned and, if the role functions as an application permissions, during the consent experiences.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#description Application#description}
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Display name for the app role that appears during app role assignment and in consent experiences.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#display_name Application#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier of the app role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if the app role is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enabled Application#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value that is used for the ``roles`` claim in ID tokens and OAuth 2.0 access tokens that are authenticating an assigned service or user principal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationAppRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationAppRoleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationAppRoleList",
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
            type_hints = typing.get_type_hints(ApplicationAppRoleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationAppRoleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationAppRoleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationAppRoleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationAppRole]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationAppRole]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationAppRole]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationAppRoleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationAppRoleOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationAppRoleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="allowedMemberTypesInput")
    def allowed_member_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMemberTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMemberTypes")
    def allowed_member_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMemberTypes"))

    @allowed_member_types.setter
    def allowed_member_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "allowed_member_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMemberTypes", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationAppRole, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationAppRole, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationAppRole, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationAppRoleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "api": "api",
        "app_role": "appRole",
        "device_only_auth_enabled": "deviceOnlyAuthEnabled",
        "fallback_public_client_enabled": "fallbackPublicClientEnabled",
        "feature_tags": "featureTags",
        "group_membership_claims": "groupMembershipClaims",
        "id": "id",
        "identifier_uris": "identifierUris",
        "logo_image": "logoImage",
        "marketing_url": "marketingUrl",
        "oauth2_post_response_required": "oauth2PostResponseRequired",
        "optional_claims": "optionalClaims",
        "owners": "owners",
        "prevent_duplicate_names": "preventDuplicateNames",
        "privacy_statement_url": "privacyStatementUrl",
        "public_client": "publicClient",
        "required_resource_access": "requiredResourceAccess",
        "sign_in_audience": "signInAudience",
        "single_page_application": "singlePageApplication",
        "support_url": "supportUrl",
        "tags": "tags",
        "template_id": "templateId",
        "terms_of_service_url": "termsOfServiceUrl",
        "timeouts": "timeouts",
        "web": "web",
    },
)
class ApplicationConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        api: typing.Optional[typing.Union[ApplicationApi, typing.Dict[str, typing.Any]]] = None,
        app_role: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationAppRole, typing.Dict[str, typing.Any]]]]] = None,
        device_only_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fallback_public_client_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        feature_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationFeatureTags", typing.Dict[str, typing.Any]]]]] = None,
        group_membership_claims: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logo_image: typing.Optional[builtins.str] = None,
        marketing_url: typing.Optional[builtins.str] = None,
        oauth2_post_response_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optional_claims: typing.Optional[typing.Union["ApplicationOptionalClaims", typing.Dict[str, typing.Any]]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        privacy_statement_url: typing.Optional[builtins.str] = None,
        public_client: typing.Optional[typing.Union["ApplicationPublicClient", typing.Dict[str, typing.Any]]] = None,
        required_resource_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationRequiredResourceAccess", typing.Dict[str, typing.Any]]]]] = None,
        sign_in_audience: typing.Optional[builtins.str] = None,
        single_page_application: typing.Optional[typing.Union["ApplicationSinglePageApplication", typing.Dict[str, typing.Any]]] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_id: typing.Optional[builtins.str] = None,
        terms_of_service_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationTimeouts", typing.Dict[str, typing.Any]]] = None,
        web: typing.Optional[typing.Union["ApplicationWeb", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The display name for the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#display_name Application#display_name}
        :param api: api block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#api Application#api}
        :param app_role: app_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#app_role Application#app_role}
        :param device_only_auth_enabled: Specifies whether this application supports device authentication without a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#device_only_auth_enabled Application#device_only_auth_enabled}
        :param fallback_public_client_enabled: Specifies whether the application is a public client. Appropriate for apps using token grant flows that don't use a redirect URI Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#fallback_public_client_enabled Application#fallback_public_client_enabled}
        :param feature_tags: feature_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#feature_tags Application#feature_tags}
        :param group_membership_claims: Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#group_membership_claims Application#group_membership_claims}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier_uris: The user-defined URI(s) that uniquely identify an application within its Azure AD tenant, or within a verified custom domain if the application is multi-tenant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#identifier_uris Application#identifier_uris}
        :param logo_image: Base64 encoded logo image in gif, png or jpeg format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logo_image Application#logo_image}
        :param marketing_url: URL of the application's marketing page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#marketing_url Application#marketing_url}
        :param oauth2_post_response_required: Specifies whether, as part of OAuth 2.0 token requests, Azure AD allows POST requests, as opposed to GET requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_post_response_required Application#oauth2_post_response_required}
        :param optional_claims: optional_claims block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#optional_claims Application#optional_claims}
        :param owners: A list of object IDs of principals that will be granted ownership of the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#owners Application#owners}
        :param prevent_duplicate_names: If ``true``, will return an error if an existing application is found with the same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#prevent_duplicate_names Application#prevent_duplicate_names}
        :param privacy_statement_url: URL of the application's privacy statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#privacy_statement_url Application#privacy_statement_url}
        :param public_client: public_client block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#public_client Application#public_client}
        :param required_resource_access: required_resource_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#required_resource_access Application#required_resource_access}
        :param sign_in_audience: The Microsoft account types that are supported for the current application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#sign_in_audience Application#sign_in_audience}
        :param single_page_application: single_page_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#single_page_application Application#single_page_application}
        :param support_url: URL of the application's support page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#support_url Application#support_url}
        :param tags: A set of tags to apply to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#tags Application#tags}
        :param template_id: Unique ID of the application template from which this application is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#template_id Application#template_id}
        :param terms_of_service_url: URL of the application's terms of service statement. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#terms_of_service_url Application#terms_of_service_url}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#timeouts Application#timeouts}
        :param web: web block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#web Application#web}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(api, dict):
            api = ApplicationApi(**api)
        if isinstance(optional_claims, dict):
            optional_claims = ApplicationOptionalClaims(**optional_claims)
        if isinstance(public_client, dict):
            public_client = ApplicationPublicClient(**public_client)
        if isinstance(single_page_application, dict):
            single_page_application = ApplicationSinglePageApplication(**single_page_application)
        if isinstance(timeouts, dict):
            timeouts = ApplicationTimeouts(**timeouts)
        if isinstance(web, dict):
            web = ApplicationWeb(**web)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument app_role", value=app_role, expected_type=type_hints["app_role"])
            check_type(argname="argument device_only_auth_enabled", value=device_only_auth_enabled, expected_type=type_hints["device_only_auth_enabled"])
            check_type(argname="argument fallback_public_client_enabled", value=fallback_public_client_enabled, expected_type=type_hints["fallback_public_client_enabled"])
            check_type(argname="argument feature_tags", value=feature_tags, expected_type=type_hints["feature_tags"])
            check_type(argname="argument group_membership_claims", value=group_membership_claims, expected_type=type_hints["group_membership_claims"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identifier_uris", value=identifier_uris, expected_type=type_hints["identifier_uris"])
            check_type(argname="argument logo_image", value=logo_image, expected_type=type_hints["logo_image"])
            check_type(argname="argument marketing_url", value=marketing_url, expected_type=type_hints["marketing_url"])
            check_type(argname="argument oauth2_post_response_required", value=oauth2_post_response_required, expected_type=type_hints["oauth2_post_response_required"])
            check_type(argname="argument optional_claims", value=optional_claims, expected_type=type_hints["optional_claims"])
            check_type(argname="argument owners", value=owners, expected_type=type_hints["owners"])
            check_type(argname="argument prevent_duplicate_names", value=prevent_duplicate_names, expected_type=type_hints["prevent_duplicate_names"])
            check_type(argname="argument privacy_statement_url", value=privacy_statement_url, expected_type=type_hints["privacy_statement_url"])
            check_type(argname="argument public_client", value=public_client, expected_type=type_hints["public_client"])
            check_type(argname="argument required_resource_access", value=required_resource_access, expected_type=type_hints["required_resource_access"])
            check_type(argname="argument sign_in_audience", value=sign_in_audience, expected_type=type_hints["sign_in_audience"])
            check_type(argname="argument single_page_application", value=single_page_application, expected_type=type_hints["single_page_application"])
            check_type(argname="argument support_url", value=support_url, expected_type=type_hints["support_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
            check_type(argname="argument terms_of_service_url", value=terms_of_service_url, expected_type=type_hints["terms_of_service_url"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument web", value=web, expected_type=type_hints["web"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
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
        if api is not None:
            self._values["api"] = api
        if app_role is not None:
            self._values["app_role"] = app_role
        if device_only_auth_enabled is not None:
            self._values["device_only_auth_enabled"] = device_only_auth_enabled
        if fallback_public_client_enabled is not None:
            self._values["fallback_public_client_enabled"] = fallback_public_client_enabled
        if feature_tags is not None:
            self._values["feature_tags"] = feature_tags
        if group_membership_claims is not None:
            self._values["group_membership_claims"] = group_membership_claims
        if id is not None:
            self._values["id"] = id
        if identifier_uris is not None:
            self._values["identifier_uris"] = identifier_uris
        if logo_image is not None:
            self._values["logo_image"] = logo_image
        if marketing_url is not None:
            self._values["marketing_url"] = marketing_url
        if oauth2_post_response_required is not None:
            self._values["oauth2_post_response_required"] = oauth2_post_response_required
        if optional_claims is not None:
            self._values["optional_claims"] = optional_claims
        if owners is not None:
            self._values["owners"] = owners
        if prevent_duplicate_names is not None:
            self._values["prevent_duplicate_names"] = prevent_duplicate_names
        if privacy_statement_url is not None:
            self._values["privacy_statement_url"] = privacy_statement_url
        if public_client is not None:
            self._values["public_client"] = public_client
        if required_resource_access is not None:
            self._values["required_resource_access"] = required_resource_access
        if sign_in_audience is not None:
            self._values["sign_in_audience"] = sign_in_audience
        if single_page_application is not None:
            self._values["single_page_application"] = single_page_application
        if support_url is not None:
            self._values["support_url"] = support_url
        if tags is not None:
            self._values["tags"] = tags
        if template_id is not None:
            self._values["template_id"] = template_id
        if terms_of_service_url is not None:
            self._values["terms_of_service_url"] = terms_of_service_url
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if web is not None:
            self._values["web"] = web

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
    def display_name(self) -> builtins.str:
        '''The display name for the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#display_name Application#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api(self) -> typing.Optional[ApplicationApi]:
        '''api block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#api Application#api}
        '''
        result = self._values.get("api")
        return typing.cast(typing.Optional[ApplicationApi], result)

    @builtins.property
    def app_role(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationAppRole]]]:
        '''app_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#app_role Application#app_role}
        '''
        result = self._values.get("app_role")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationAppRole]]], result)

    @builtins.property
    def device_only_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether this application supports device authentication without a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#device_only_auth_enabled Application#device_only_auth_enabled}
        '''
        result = self._values.get("device_only_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fallback_public_client_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether the application is a public client.

        Appropriate for apps using token grant flows that don't use a redirect URI

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#fallback_public_client_enabled Application#fallback_public_client_enabled}
        '''
        result = self._values.get("fallback_public_client_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def feature_tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationFeatureTags"]]]:
        '''feature_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#feature_tags Application#feature_tags}
        '''
        result = self._values.get("feature_tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationFeatureTags"]]], result)

    @builtins.property
    def group_membership_claims(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#group_membership_claims Application#group_membership_claims}
        '''
        result = self._values.get("group_membership_claims")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The user-defined URI(s) that uniquely identify an application within its Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#identifier_uris Application#identifier_uris}
        '''
        result = self._values.get("identifier_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logo_image(self) -> typing.Optional[builtins.str]:
        '''Base64 encoded logo image in gif, png or jpeg format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logo_image Application#logo_image}
        '''
        result = self._values.get("logo_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketing_url(self) -> typing.Optional[builtins.str]:
        '''URL of the application's marketing page.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#marketing_url Application#marketing_url}
        '''
        result = self._values.get("marketing_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_post_response_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether, as part of OAuth 2.0 token requests, Azure AD allows POST requests, as opposed to GET requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#oauth2_post_response_required Application#oauth2_post_response_required}
        '''
        result = self._values.get("oauth2_post_response_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def optional_claims(self) -> typing.Optional["ApplicationOptionalClaims"]:
        '''optional_claims block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#optional_claims Application#optional_claims}
        '''
        result = self._values.get("optional_claims")
        return typing.cast(typing.Optional["ApplicationOptionalClaims"], result)

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of object IDs of principals that will be granted ownership of the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#owners Application#owners}
        '''
        result = self._values.get("owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prevent_duplicate_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, will return an error if an existing application is found with the same name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#prevent_duplicate_names Application#prevent_duplicate_names}
        '''
        result = self._values.get("prevent_duplicate_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def privacy_statement_url(self) -> typing.Optional[builtins.str]:
        '''URL of the application's privacy statement.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#privacy_statement_url Application#privacy_statement_url}
        '''
        result = self._values.get("privacy_statement_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_client(self) -> typing.Optional["ApplicationPublicClient"]:
        '''public_client block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#public_client Application#public_client}
        '''
        result = self._values.get("public_client")
        return typing.cast(typing.Optional["ApplicationPublicClient"], result)

    @builtins.property
    def required_resource_access(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccess"]]]:
        '''required_resource_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#required_resource_access Application#required_resource_access}
        '''
        result = self._values.get("required_resource_access")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccess"]]], result)

    @builtins.property
    def sign_in_audience(self) -> typing.Optional[builtins.str]:
        '''The Microsoft account types that are supported for the current application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#sign_in_audience Application#sign_in_audience}
        '''
        result = self._values.get("sign_in_audience")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_page_application(
        self,
    ) -> typing.Optional["ApplicationSinglePageApplication"]:
        '''single_page_application block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#single_page_application Application#single_page_application}
        '''
        result = self._values.get("single_page_application")
        return typing.cast(typing.Optional["ApplicationSinglePageApplication"], result)

    @builtins.property
    def support_url(self) -> typing.Optional[builtins.str]:
        '''URL of the application's support page.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#support_url Application#support_url}
        '''
        result = self._values.get("support_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of tags to apply to the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#tags Application#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''Unique ID of the application template from which this application is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#template_id Application#template_id}
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def terms_of_service_url(self) -> typing.Optional[builtins.str]:
        '''URL of the application's terms of service statement.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#terms_of_service_url Application#terms_of_service_url}
        '''
        result = self._values.get("terms_of_service_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApplicationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#timeouts Application#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationTimeouts"], result)

    @builtins.property
    def web(self) -> typing.Optional["ApplicationWeb"]:
        '''web block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#web Application#web}
        '''
        result = self._values.get("web")
        return typing.cast(typing.Optional["ApplicationWeb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationFeatureTags",
    jsii_struct_bases=[],
    name_mapping={
        "custom_single_sign_on": "customSingleSignOn",
        "enterprise": "enterprise",
        "gallery": "gallery",
        "hide": "hide",
    },
)
class ApplicationFeatureTags:
    def __init__(
        self,
        *,
        custom_single_sign_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enterprise: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gallery: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param custom_single_sign_on: Whether this application represents a custom SAML application for linked service principals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#custom_single_sign_on Application#custom_single_sign_on}
        :param enterprise: Whether this application represents an Enterprise Application for linked service principals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enterprise Application#enterprise}
        :param gallery: Whether this application represents a gallery application for linked service principals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#gallery Application#gallery}
        :param hide: Whether this application is invisible to users in My Apps and Office 365 Launcher. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#hide Application#hide}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationFeatureTags.__init__)
            check_type(argname="argument custom_single_sign_on", value=custom_single_sign_on, expected_type=type_hints["custom_single_sign_on"])
            check_type(argname="argument enterprise", value=enterprise, expected_type=type_hints["enterprise"])
            check_type(argname="argument gallery", value=gallery, expected_type=type_hints["gallery"])
            check_type(argname="argument hide", value=hide, expected_type=type_hints["hide"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_single_sign_on is not None:
            self._values["custom_single_sign_on"] = custom_single_sign_on
        if enterprise is not None:
            self._values["enterprise"] = enterprise
        if gallery is not None:
            self._values["gallery"] = gallery
        if hide is not None:
            self._values["hide"] = hide

    @builtins.property
    def custom_single_sign_on(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this application represents a custom SAML application for linked service principals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#custom_single_sign_on Application#custom_single_sign_on}
        '''
        result = self._values.get("custom_single_sign_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enterprise(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this application represents an Enterprise Application for linked service principals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#enterprise Application#enterprise}
        '''
        result = self._values.get("enterprise")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gallery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this application represents a gallery application for linked service principals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#gallery Application#gallery}
        '''
        result = self._values.get("gallery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hide(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this application is invisible to users in My Apps and Office 365 Launcher.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#hide Application#hide}
        '''
        result = self._values.get("hide")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationFeatureTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationFeatureTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationFeatureTagsList",
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
            type_hints = typing.get_type_hints(ApplicationFeatureTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationFeatureTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationFeatureTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationFeatureTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationFeatureTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationFeatureTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationFeatureTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationFeatureTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationFeatureTagsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationFeatureTagsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomSingleSignOn")
    def reset_custom_single_sign_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSingleSignOn", []))

    @jsii.member(jsii_name="resetEnterprise")
    def reset_enterprise(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnterprise", []))

    @jsii.member(jsii_name="resetGallery")
    def reset_gallery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGallery", []))

    @jsii.member(jsii_name="resetHide")
    def reset_hide(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHide", []))

    @builtins.property
    @jsii.member(jsii_name="customSingleSignOnInput")
    def custom_single_sign_on_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customSingleSignOnInput"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseInput")
    def enterprise_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enterpriseInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryInput")
    def gallery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "galleryInput"))

    @builtins.property
    @jsii.member(jsii_name="hideInput")
    def hide_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hideInput"))

    @builtins.property
    @jsii.member(jsii_name="customSingleSignOn")
    def custom_single_sign_on(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customSingleSignOn"))

    @custom_single_sign_on.setter
    def custom_single_sign_on(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsOutputReference, "custom_single_sign_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSingleSignOn", value)

    @builtins.property
    @jsii.member(jsii_name="enterprise")
    def enterprise(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enterprise"))

    @enterprise.setter
    def enterprise(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsOutputReference, "enterprise").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enterprise", value)

    @builtins.property
    @jsii.member(jsii_name="gallery")
    def gallery(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "gallery"))

    @gallery.setter
    def gallery(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsOutputReference, "gallery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gallery", value)

    @builtins.property
    @jsii.member(jsii_name="hide")
    def hide(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hide"))

    @hide.setter
    def hide(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsOutputReference, "hide").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hide", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationFeatureTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationFeatureTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationFeatureTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationFeatureTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaims",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "id_token": "idToken",
        "saml2_token": "saml2Token",
    },
)
class ApplicationOptionalClaims:
    def __init__(
        self,
        *,
        access_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsAccessToken", typing.Dict[str, typing.Any]]]]] = None,
        id_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsIdToken", typing.Dict[str, typing.Any]]]]] = None,
        saml2_token: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsSaml2Token", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param access_token: access_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token Application#access_token}
        :param id_token: id_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token Application#id_token}
        :param saml2_token: saml2_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#saml2_token Application#saml2_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaims.__init__)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument id_token", value=id_token, expected_type=type_hints["id_token"])
            check_type(argname="argument saml2_token", value=saml2_token, expected_type=type_hints["saml2_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if id_token is not None:
            self._values["id_token"] = id_token
        if saml2_token is not None:
            self._values["saml2_token"] = saml2_token

    @builtins.property
    def access_token(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsAccessToken"]]]:
        '''access_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token Application#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsAccessToken"]]], result)

    @builtins.property
    def id_token(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsIdToken"]]]:
        '''id_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token Application#id_token}
        '''
        result = self._values.get("id_token")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsIdToken"]]], result)

    @builtins.property
    def saml2_token(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsSaml2Token"]]]:
        '''saml2_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#saml2_token Application#saml2_token}
        '''
        result = self._values.get("saml2_token")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsSaml2Token"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationOptionalClaims(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsAccessToken",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_properties": "additionalProperties",
        "essential": "essential",
        "source": "source",
    },
)
class ApplicationOptionalClaimsAccessToken:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
        essential: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the optional claim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        :param additional_properties: List of additional properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        :param essential: Whether the claim specified by the client is necessary to ensure a smooth authorization experience. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        :param source: The source of the claim. If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsAccessToken.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if essential is not None:
            self._values["essential"] = essential
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the optional claim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of additional properties of the claim.

        If a property exists in this list, it modifies the behaviour of the optional claim

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        '''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def essential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the claim specified by the client is necessary to ensure a smooth authorization experience.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        '''
        result = self._values.get("essential")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The source of the claim.

        If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationOptionalClaimsAccessToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationOptionalClaimsAccessTokenList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsAccessTokenList",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsAccessTokenList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationOptionalClaimsAccessTokenOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsAccessTokenList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationOptionalClaimsAccessTokenOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsAccessToken]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsAccessToken]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsAccessToken]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationOptionalClaimsAccessTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsAccessTokenOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsAccessTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetEssential")
    def reset_essential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEssential", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="essentialInput")
    def essential_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "essentialInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenOutputReference, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="essential")
    def essential(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "essential"))

    @essential.setter
    def essential(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenOutputReference, "essential").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "essential", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationOptionalClaimsAccessToken, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationOptionalClaimsAccessToken, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationOptionalClaimsAccessToken, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsAccessTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsIdToken",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_properties": "additionalProperties",
        "essential": "essential",
        "source": "source",
    },
)
class ApplicationOptionalClaimsIdToken:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
        essential: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the optional claim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        :param additional_properties: List of additional properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        :param essential: Whether the claim specified by the client is necessary to ensure a smooth authorization experience. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        :param source: The source of the claim. If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsIdToken.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if essential is not None:
            self._values["essential"] = essential
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the optional claim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of additional properties of the claim.

        If a property exists in this list, it modifies the behaviour of the optional claim

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        '''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def essential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the claim specified by the client is necessary to ensure a smooth authorization experience.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        '''
        result = self._values.get("essential")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The source of the claim.

        If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationOptionalClaimsIdToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationOptionalClaimsIdTokenList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsIdTokenList",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsIdTokenList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationOptionalClaimsIdTokenOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsIdTokenList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationOptionalClaimsIdTokenOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsIdToken]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsIdToken]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsIdToken]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationOptionalClaimsIdTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsIdTokenOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsIdTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetEssential")
    def reset_essential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEssential", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="essentialInput")
    def essential_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "essentialInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenOutputReference, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="essential")
    def essential(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "essential"))

    @essential.setter
    def essential(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenOutputReference, "essential").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "essential", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationOptionalClaimsIdToken, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationOptionalClaimsIdToken, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationOptionalClaimsIdToken, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsIdTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationOptionalClaimsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessToken")
    def put_access_token(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationOptionalClaimsAccessToken, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsOutputReference.put_access_token)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessToken", [value]))

    @jsii.member(jsii_name="putIdToken")
    def put_id_token(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationOptionalClaimsIdToken, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsOutputReference.put_id_token)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIdToken", [value]))

    @jsii.member(jsii_name="putSaml2Token")
    def put_saml2_token(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationOptionalClaimsSaml2Token", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsOutputReference.put_saml2_token)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml2Token", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetIdToken")
    def reset_id_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdToken", []))

    @jsii.member(jsii_name="resetSaml2Token")
    def reset_saml2_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2Token", []))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> ApplicationOptionalClaimsAccessTokenList:
        return typing.cast(ApplicationOptionalClaimsAccessTokenList, jsii.get(self, "accessToken"))

    @builtins.property
    @jsii.member(jsii_name="idToken")
    def id_token(self) -> ApplicationOptionalClaimsIdTokenList:
        return typing.cast(ApplicationOptionalClaimsIdTokenList, jsii.get(self, "idToken"))

    @builtins.property
    @jsii.member(jsii_name="saml2Token")
    def saml2_token(self) -> "ApplicationOptionalClaimsSaml2TokenList":
        return typing.cast("ApplicationOptionalClaimsSaml2TokenList", jsii.get(self, "saml2Token"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsAccessToken]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsAccessToken]]], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="idTokenInput")
    def id_token_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsIdToken]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsIdToken]]], jsii.get(self, "idTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2TokenInput")
    def saml2_token_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsSaml2Token"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationOptionalClaimsSaml2Token"]]], jsii.get(self, "saml2TokenInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationOptionalClaims]:
        return typing.cast(typing.Optional[ApplicationOptionalClaims], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationOptionalClaims]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsSaml2Token",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_properties": "additionalProperties",
        "essential": "essential",
        "source": "source",
    },
)
class ApplicationOptionalClaimsSaml2Token:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
        essential: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the optional claim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        :param additional_properties: List of additional properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        :param essential: Whether the claim specified by the client is necessary to ensure a smooth authorization experience. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        :param source: The source of the claim. If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsSaml2Token.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if essential is not None:
            self._values["essential"] = essential
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the optional claim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#name Application#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of additional properties of the claim.

        If a property exists in this list, it modifies the behaviour of the optional claim

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#additional_properties Application#additional_properties}
        '''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def essential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the claim specified by the client is necessary to ensure a smooth authorization experience.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#essential Application#essential}
        '''
        result = self._values.get("essential")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The source of the claim.

        If ``source`` is absent, the claim is a predefined optional claim. If ``source`` is ``user``, the value of ``name`` is the extension property from the user object

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#source Application#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationOptionalClaimsSaml2Token(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationOptionalClaimsSaml2TokenList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsSaml2TokenList",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsSaml2TokenList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationOptionalClaimsSaml2TokenOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsSaml2TokenList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationOptionalClaimsSaml2TokenOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsSaml2Token]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsSaml2Token]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationOptionalClaimsSaml2Token]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationOptionalClaimsSaml2TokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationOptionalClaimsSaml2TokenOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationOptionalClaimsSaml2TokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetEssential")
    def reset_essential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEssential", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="essentialInput")
    def essential_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "essentialInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenOutputReference, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="essential")
    def essential(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "essential"))

    @essential.setter
    def essential(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenOutputReference, "essential").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "essential", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationOptionalClaimsSaml2Token, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationOptionalClaimsSaml2Token, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationOptionalClaimsSaml2Token, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationOptionalClaimsSaml2TokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationPublicClient",
    jsii_struct_bases=[],
    name_mapping={"redirect_uris": "redirectUris"},
)
class ApplicationPublicClient:
    def __init__(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationPublicClient.__init__)
            check_type(argname="argument redirect_uris", value=redirect_uris, expected_type=type_hints["redirect_uris"])
        self._values: typing.Dict[str, typing.Any] = {}
        if redirect_uris is not None:
            self._values["redirect_uris"] = redirect_uris

    @builtins.property
    def redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        result = self._values.get("redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationPublicClient(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationPublicClientOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationPublicClientOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationPublicClientOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRedirectUris")
    def reset_redirect_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUris", []))

    @builtins.property
    @jsii.member(jsii_name="redirectUrisInput")
    def redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redirectUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUris")
    def redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "redirectUris"))

    @redirect_uris.setter
    def redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationPublicClientOutputReference, "redirect_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationPublicClient]:
        return typing.cast(typing.Optional[ApplicationPublicClient], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationPublicClient]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationPublicClientOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccess",
    jsii_struct_bases=[],
    name_mapping={
        "resource_access": "resourceAccess",
        "resource_app_id": "resourceAppId",
    },
)
class ApplicationRequiredResourceAccess:
    def __init__(
        self,
        *,
        resource_access: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationRequiredResourceAccessResourceAccess", typing.Dict[str, typing.Any]]]],
        resource_app_id: builtins.str,
    ) -> None:
        '''
        :param resource_access: resource_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#resource_access Application#resource_access}
        :param resource_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#resource_app_id Application#resource_app_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccess.__init__)
            check_type(argname="argument resource_access", value=resource_access, expected_type=type_hints["resource_access"])
            check_type(argname="argument resource_app_id", value=resource_app_id, expected_type=type_hints["resource_app_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_access": resource_access,
            "resource_app_id": resource_app_id,
        }

    @builtins.property
    def resource_access(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccessResourceAccess"]]:
        '''resource_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#resource_access Application#resource_access}
        '''
        result = self._values.get("resource_access")
        assert result is not None, "Required property 'resource_access' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccessResourceAccess"]], result)

    @builtins.property
    def resource_app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#resource_app_id Application#resource_app_id}.'''
        result = self._values.get("resource_app_id")
        assert result is not None, "Required property 'resource_app_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationRequiredResourceAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationRequiredResourceAccessList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccessList",
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
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationRequiredResourceAccessOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationRequiredResourceAccessOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccess]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccess]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccess]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationRequiredResourceAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccessOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putResourceAccess")
    def put_resource_access(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationRequiredResourceAccessResourceAccess", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessOutputReference.put_resource_access)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceAccess", [value]))

    @builtins.property
    @jsii.member(jsii_name="resourceAccess")
    def resource_access(self) -> "ApplicationRequiredResourceAccessResourceAccessList":
        return typing.cast("ApplicationRequiredResourceAccessResourceAccessList", jsii.get(self, "resourceAccess"))

    @builtins.property
    @jsii.member(jsii_name="resourceAccessInput")
    def resource_access_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccessResourceAccess"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationRequiredResourceAccessResourceAccess"]]], jsii.get(self, "resourceAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceAppIdInput")
    def resource_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceAppId")
    def resource_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceAppId"))

    @resource_app_id.setter
    def resource_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessOutputReference, "resource_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAppId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationRequiredResourceAccess, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationRequiredResourceAccess, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationRequiredResourceAccess, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccessResourceAccess",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class ApplicationRequiredResourceAccessResourceAccess:
    def __init__(self, *, id: builtins.str, type: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#type Application#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessResourceAccess.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id Application#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#type Application#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationRequiredResourceAccessResourceAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationRequiredResourceAccessResourceAccessList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccessResourceAccessList",
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
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessResourceAccessList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationRequiredResourceAccessResourceAccessOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessResourceAccessList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationRequiredResourceAccessResourceAccessOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccessResourceAccess]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccessResourceAccess]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationRequiredResourceAccessResourceAccess]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationRequiredResourceAccessResourceAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationRequiredResourceAccessResourceAccessOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationRequiredResourceAccessResourceAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationRequiredResourceAccessResourceAccess, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationRequiredResourceAccessResourceAccess, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationRequiredResourceAccessResourceAccess, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationRequiredResourceAccessResourceAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationSinglePageApplication",
    jsii_struct_bases=[],
    name_mapping={"redirect_uris": "redirectUris"},
)
class ApplicationSinglePageApplication:
    def __init__(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationSinglePageApplication.__init__)
            check_type(argname="argument redirect_uris", value=redirect_uris, expected_type=type_hints["redirect_uris"])
        self._values: typing.Dict[str, typing.Any] = {}
        if redirect_uris is not None:
            self._values["redirect_uris"] = redirect_uris

    @builtins.property
    def redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        result = self._values.get("redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSinglePageApplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSinglePageApplicationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationSinglePageApplicationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationSinglePageApplicationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRedirectUris")
    def reset_redirect_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUris", []))

    @builtins.property
    @jsii.member(jsii_name="redirectUrisInput")
    def redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redirectUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUris")
    def redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "redirectUris"))

    @redirect_uris.setter
    def redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationSinglePageApplicationOutputReference, "redirect_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSinglePageApplication]:
        return typing.cast(typing.Optional[ApplicationSinglePageApplication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSinglePageApplication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationSinglePageApplicationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApplicationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#create Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#delete Application#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#read Application#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#update Application#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#create Application#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#delete Application#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#read Application#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#update Application#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApplicationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationWeb",
    jsii_struct_bases=[],
    name_mapping={
        "homepage_url": "homepageUrl",
        "implicit_grant": "implicitGrant",
        "logout_url": "logoutUrl",
        "redirect_uris": "redirectUris",
    },
)
class ApplicationWeb:
    def __init__(
        self,
        *,
        homepage_url: typing.Optional[builtins.str] = None,
        implicit_grant: typing.Optional[typing.Union["ApplicationWebImplicitGrant", typing.Dict[str, typing.Any]]] = None,
        logout_url: typing.Optional[builtins.str] = None,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param homepage_url: Home page or landing page of the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#homepage_url Application#homepage_url}
        :param implicit_grant: implicit_grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#implicit_grant Application#implicit_grant}
        :param logout_url: The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logout_url Application#logout_url}
        :param redirect_uris: The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        if isinstance(implicit_grant, dict):
            implicit_grant = ApplicationWebImplicitGrant(**implicit_grant)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationWeb.__init__)
            check_type(argname="argument homepage_url", value=homepage_url, expected_type=type_hints["homepage_url"])
            check_type(argname="argument implicit_grant", value=implicit_grant, expected_type=type_hints["implicit_grant"])
            check_type(argname="argument logout_url", value=logout_url, expected_type=type_hints["logout_url"])
            check_type(argname="argument redirect_uris", value=redirect_uris, expected_type=type_hints["redirect_uris"])
        self._values: typing.Dict[str, typing.Any] = {}
        if homepage_url is not None:
            self._values["homepage_url"] = homepage_url
        if implicit_grant is not None:
            self._values["implicit_grant"] = implicit_grant
        if logout_url is not None:
            self._values["logout_url"] = logout_url
        if redirect_uris is not None:
            self._values["redirect_uris"] = redirect_uris

    @builtins.property
    def homepage_url(self) -> typing.Optional[builtins.str]:
        '''Home page or landing page of the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#homepage_url Application#homepage_url}
        '''
        result = self._values.get("homepage_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def implicit_grant(self) -> typing.Optional["ApplicationWebImplicitGrant"]:
        '''implicit_grant block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#implicit_grant Application#implicit_grant}
        '''
        result = self._values.get("implicit_grant")
        return typing.cast(typing.Optional["ApplicationWebImplicitGrant"], result)

    @builtins.property
    def logout_url(self) -> typing.Optional[builtins.str]:
        '''The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#logout_url Application#logout_url}
        '''
        result = self._values.get("logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#redirect_uris Application#redirect_uris}
        '''
        result = self._values.get("redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationWeb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.application.ApplicationWebImplicitGrant",
    jsii_struct_bases=[],
    name_mapping={
        "access_token_issuance_enabled": "accessTokenIssuanceEnabled",
        "id_token_issuance_enabled": "idTokenIssuanceEnabled",
    },
)
class ApplicationWebImplicitGrant:
    def __init__(
        self,
        *,
        access_token_issuance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id_token_issuance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param access_token_issuance_enabled: Whether this web application can request an access token using OAuth 2.0 implicit flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token_issuance_enabled Application#access_token_issuance_enabled}
        :param id_token_issuance_enabled: Whether this web application can request an ID token using OAuth 2.0 implicit flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token_issuance_enabled Application#id_token_issuance_enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationWebImplicitGrant.__init__)
            check_type(argname="argument access_token_issuance_enabled", value=access_token_issuance_enabled, expected_type=type_hints["access_token_issuance_enabled"])
            check_type(argname="argument id_token_issuance_enabled", value=id_token_issuance_enabled, expected_type=type_hints["id_token_issuance_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token_issuance_enabled is not None:
            self._values["access_token_issuance_enabled"] = access_token_issuance_enabled
        if id_token_issuance_enabled is not None:
            self._values["id_token_issuance_enabled"] = id_token_issuance_enabled

    @builtins.property
    def access_token_issuance_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this web application can request an access token using OAuth 2.0 implicit flow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token_issuance_enabled Application#access_token_issuance_enabled}
        '''
        result = self._values.get("access_token_issuance_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id_token_issuance_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this web application can request an ID token using OAuth 2.0 implicit flow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token_issuance_enabled Application#id_token_issuance_enabled}
        '''
        result = self._values.get("id_token_issuance_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationWebImplicitGrant(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationWebImplicitGrantOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationWebImplicitGrantOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationWebImplicitGrantOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessTokenIssuanceEnabled")
    def reset_access_token_issuance_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessTokenIssuanceEnabled", []))

    @jsii.member(jsii_name="resetIdTokenIssuanceEnabled")
    def reset_id_token_issuance_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdTokenIssuanceEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="accessTokenIssuanceEnabledInput")
    def access_token_issuance_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "accessTokenIssuanceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idTokenIssuanceEnabledInput")
    def id_token_issuance_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "idTokenIssuanceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenIssuanceEnabled")
    def access_token_issuance_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "accessTokenIssuanceEnabled"))

    @access_token_issuance_enabled.setter
    def access_token_issuance_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebImplicitGrantOutputReference, "access_token_issuance_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessTokenIssuanceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="idTokenIssuanceEnabled")
    def id_token_issuance_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "idTokenIssuanceEnabled"))

    @id_token_issuance_enabled.setter
    def id_token_issuance_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebImplicitGrantOutputReference, "id_token_issuance_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idTokenIssuanceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationWebImplicitGrant]:
        return typing.cast(typing.Optional[ApplicationWebImplicitGrant], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationWebImplicitGrant],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebImplicitGrantOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationWebOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.application.ApplicationWebOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationWebOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putImplicitGrant")
    def put_implicit_grant(
        self,
        *,
        access_token_issuance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id_token_issuance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param access_token_issuance_enabled: Whether this web application can request an access token using OAuth 2.0 implicit flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#access_token_issuance_enabled Application#access_token_issuance_enabled}
        :param id_token_issuance_enabled: Whether this web application can request an ID token using OAuth 2.0 implicit flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/application#id_token_issuance_enabled Application#id_token_issuance_enabled}
        '''
        value = ApplicationWebImplicitGrant(
            access_token_issuance_enabled=access_token_issuance_enabled,
            id_token_issuance_enabled=id_token_issuance_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putImplicitGrant", [value]))

    @jsii.member(jsii_name="resetHomepageUrl")
    def reset_homepage_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomepageUrl", []))

    @jsii.member(jsii_name="resetImplicitGrant")
    def reset_implicit_grant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImplicitGrant", []))

    @jsii.member(jsii_name="resetLogoutUrl")
    def reset_logout_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoutUrl", []))

    @jsii.member(jsii_name="resetRedirectUris")
    def reset_redirect_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUris", []))

    @builtins.property
    @jsii.member(jsii_name="implicitGrant")
    def implicit_grant(self) -> ApplicationWebImplicitGrantOutputReference:
        return typing.cast(ApplicationWebImplicitGrantOutputReference, jsii.get(self, "implicitGrant"))

    @builtins.property
    @jsii.member(jsii_name="homepageUrlInput")
    def homepage_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homepageUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="implicitGrantInput")
    def implicit_grant_input(self) -> typing.Optional[ApplicationWebImplicitGrant]:
        return typing.cast(typing.Optional[ApplicationWebImplicitGrant], jsii.get(self, "implicitGrantInput"))

    @builtins.property
    @jsii.member(jsii_name="logoutUrlInput")
    def logout_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoutUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUrisInput")
    def redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redirectUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="homepageUrl")
    def homepage_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homepageUrl"))

    @homepage_url.setter
    def homepage_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebOutputReference, "homepage_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homepageUrl", value)

    @builtins.property
    @jsii.member(jsii_name="logoutUrl")
    def logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoutUrl"))

    @logout_url.setter
    def logout_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebOutputReference, "logout_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoutUrl", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUris")
    def redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "redirectUris"))

    @redirect_uris.setter
    def redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebOutputReference, "redirect_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationWeb]:
        return typing.cast(typing.Optional[ApplicationWeb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationWeb]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationWebOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Application",
    "ApplicationApi",
    "ApplicationApiOauth2PermissionScope",
    "ApplicationApiOauth2PermissionScopeList",
    "ApplicationApiOauth2PermissionScopeOutputReference",
    "ApplicationApiOutputReference",
    "ApplicationAppRole",
    "ApplicationAppRoleList",
    "ApplicationAppRoleOutputReference",
    "ApplicationConfig",
    "ApplicationFeatureTags",
    "ApplicationFeatureTagsList",
    "ApplicationFeatureTagsOutputReference",
    "ApplicationOptionalClaims",
    "ApplicationOptionalClaimsAccessToken",
    "ApplicationOptionalClaimsAccessTokenList",
    "ApplicationOptionalClaimsAccessTokenOutputReference",
    "ApplicationOptionalClaimsIdToken",
    "ApplicationOptionalClaimsIdTokenList",
    "ApplicationOptionalClaimsIdTokenOutputReference",
    "ApplicationOptionalClaimsOutputReference",
    "ApplicationOptionalClaimsSaml2Token",
    "ApplicationOptionalClaimsSaml2TokenList",
    "ApplicationOptionalClaimsSaml2TokenOutputReference",
    "ApplicationPublicClient",
    "ApplicationPublicClientOutputReference",
    "ApplicationRequiredResourceAccess",
    "ApplicationRequiredResourceAccessList",
    "ApplicationRequiredResourceAccessOutputReference",
    "ApplicationRequiredResourceAccessResourceAccess",
    "ApplicationRequiredResourceAccessResourceAccessList",
    "ApplicationRequiredResourceAccessResourceAccessOutputReference",
    "ApplicationSinglePageApplication",
    "ApplicationSinglePageApplicationOutputReference",
    "ApplicationTimeouts",
    "ApplicationTimeoutsOutputReference",
    "ApplicationWeb",
    "ApplicationWebImplicitGrant",
    "ApplicationWebImplicitGrantOutputReference",
    "ApplicationWebOutputReference",
]

publication.publish()
