'''
# `azuread_service_principal`

Refer to the Terraform Registory for docs: [`azuread_service_principal`](https://www.terraform.io/docs/providers/azuread/r/service_principal).
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


class ServicePrincipal(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipal",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/service_principal azuread_service_principal}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        application_id: builtins.str,
        account_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        app_role_assignment_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        features: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatures", typing.Dict[str, typing.Any]]]]] = None,
        feature_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatureTags", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        login_url: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        notification_email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_single_sign_on_mode: typing.Optional[builtins.str] = None,
        saml_single_sign_on: typing.Optional[typing.Union["ServicePrincipalSamlSingleSignOn", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServicePrincipalTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_existing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/service_principal azuread_service_principal} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_id: The application ID (client ID) of the application for which to create a service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#application_id ServicePrincipal#application_id}
        :param account_enabled: Whether or not the service principal account is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#account_enabled ServicePrincipal#account_enabled}
        :param alternative_names: A list of alternative names, used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#alternative_names ServicePrincipal#alternative_names}
        :param app_role_assignment_required: Whether this service principal requires an app role assignment to a user or group before Azure AD will issue a user or access token to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#app_role_assignment_required ServicePrincipal#app_role_assignment_required}
        :param description: Description of the service principal provided for internal end-users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#description ServicePrincipal#description}
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#features ServicePrincipal#features}
        :param feature_tags: feature_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#feature_tags ServicePrincipal#feature_tags}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#id ServicePrincipal#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param login_url: The URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#login_url ServicePrincipal#login_url}
        :param notes: Free text field to capture information about the service principal, typically used for operational purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notes ServicePrincipal#notes}
        :param notification_email_addresses: List of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notification_email_addresses ServicePrincipal#notification_email_addresses}
        :param owners: A list of object IDs of principals that will be granted ownership of the service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#owners ServicePrincipal#owners}
        :param preferred_single_sign_on_mode: The single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#preferred_single_sign_on_mode ServicePrincipal#preferred_single_sign_on_mode}
        :param saml_single_sign_on: saml_single_sign_on block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#saml_single_sign_on ServicePrincipal#saml_single_sign_on}
        :param tags: A set of tags to apply to the service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#tags ServicePrincipal#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#timeouts ServicePrincipal#timeouts}
        :param use_existing: When true, the resource will return an existing service principal instead of failing with an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#use_existing ServicePrincipal#use_existing}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipal.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServicePrincipalConfig(
            application_id=application_id,
            account_enabled=account_enabled,
            alternative_names=alternative_names,
            app_role_assignment_required=app_role_assignment_required,
            description=description,
            features=features,
            feature_tags=feature_tags,
            id=id,
            login_url=login_url,
            notes=notes,
            notification_email_addresses=notification_email_addresses,
            owners=owners,
            preferred_single_sign_on_mode=preferred_single_sign_on_mode,
            saml_single_sign_on=saml_single_sign_on,
            tags=tags,
            timeouts=timeouts,
            use_existing=use_existing,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFeatures")
    def put_features(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatures", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipal.put_features)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFeatures", [value]))

    @jsii.member(jsii_name="putFeatureTags")
    def put_feature_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatureTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipal.put_feature_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFeatureTags", [value]))

    @jsii.member(jsii_name="putSamlSingleSignOn")
    def put_saml_single_sign_on(
        self,
        *,
        relay_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param relay_state: The relative URI the service provider would redirect to after completion of the single sign-on flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#relay_state ServicePrincipal#relay_state}
        '''
        value = ServicePrincipalSamlSingleSignOn(relay_state=relay_state)

        return typing.cast(None, jsii.invoke(self, "putSamlSingleSignOn", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#create ServicePrincipal#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#delete ServicePrincipal#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#read ServicePrincipal#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#update ServicePrincipal#update}.
        '''
        value = ServicePrincipalTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccountEnabled")
    def reset_account_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountEnabled", []))

    @jsii.member(jsii_name="resetAlternativeNames")
    def reset_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternativeNames", []))

    @jsii.member(jsii_name="resetAppRoleAssignmentRequired")
    def reset_app_role_assignment_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppRoleAssignmentRequired", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFeatures")
    def reset_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatures", []))

    @jsii.member(jsii_name="resetFeatureTags")
    def reset_feature_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureTags", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoginUrl")
    def reset_login_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginUrl", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetNotificationEmailAddresses")
    def reset_notification_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmailAddresses", []))

    @jsii.member(jsii_name="resetOwners")
    def reset_owners(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwners", []))

    @jsii.member(jsii_name="resetPreferredSingleSignOnMode")
    def reset_preferred_single_sign_on_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredSingleSignOnMode", []))

    @jsii.member(jsii_name="resetSamlSingleSignOn")
    def reset_saml_single_sign_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamlSingleSignOn", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseExisting")
    def reset_use_existing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseExisting", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="applicationTenantId")
    def application_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationTenantId"))

    @builtins.property
    @jsii.member(jsii_name="appRoleIds")
    def app_role_ids(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "appRoleIds"))

    @builtins.property
    @jsii.member(jsii_name="appRoles")
    def app_roles(self) -> "ServicePrincipalAppRolesList":
        return typing.cast("ServicePrincipalAppRolesList", jsii.get(self, "appRoles"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(self) -> "ServicePrincipalFeaturesList":
        return typing.cast("ServicePrincipalFeaturesList", jsii.get(self, "features"))

    @builtins.property
    @jsii.member(jsii_name="featureTags")
    def feature_tags(self) -> "ServicePrincipalFeatureTagsList":
        return typing.cast("ServicePrincipalFeatureTagsList", jsii.get(self, "featureTags"))

    @builtins.property
    @jsii.member(jsii_name="homepageUrl")
    def homepage_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homepageUrl"))

    @builtins.property
    @jsii.member(jsii_name="logoutUrl")
    def logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoutUrl"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PermissionScopeIds")
    def oauth2_permission_scope_ids(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "oauth2PermissionScopeIds"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PermissionScopes")
    def oauth2_permission_scopes(self) -> "ServicePrincipalOauth2PermissionScopesList":
        return typing.cast("ServicePrincipalOauth2PermissionScopesList", jsii.get(self, "oauth2PermissionScopes"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="redirectUris")
    def redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "redirectUris"))

    @builtins.property
    @jsii.member(jsii_name="samlMetadataUrl")
    def saml_metadata_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "samlMetadataUrl"))

    @builtins.property
    @jsii.member(jsii_name="samlSingleSignOn")
    def saml_single_sign_on(self) -> "ServicePrincipalSamlSingleSignOnOutputReference":
        return typing.cast("ServicePrincipalSamlSingleSignOnOutputReference", jsii.get(self, "samlSingleSignOn"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalNames")
    def service_principal_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servicePrincipalNames"))

    @builtins.property
    @jsii.member(jsii_name="signInAudience")
    def sign_in_audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signInAudience"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServicePrincipalTimeoutsOutputReference":
        return typing.cast("ServicePrincipalTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="accountEnabledInput")
    def account_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "accountEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="alternativeNamesInput")
    def alternative_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appRoleAssignmentRequiredInput")
    def app_role_assignment_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "appRoleAssignmentRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="featuresInput")
    def features_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatures"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatures"]]], jsii.get(self, "featuresInput"))

    @builtins.property
    @jsii.member(jsii_name="featureTagsInput")
    def feature_tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatureTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatureTags"]]], jsii.get(self, "featureTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loginUrlInput")
    def login_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailAddressesInput")
    def notification_email_addresses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEmailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ownersInput")
    def owners_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ownersInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredSingleSignOnModeInput")
    def preferred_single_sign_on_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredSingleSignOnModeInput"))

    @builtins.property
    @jsii.member(jsii_name="samlSingleSignOnInput")
    def saml_single_sign_on_input(
        self,
    ) -> typing.Optional["ServicePrincipalSamlSingleSignOn"]:
        return typing.cast(typing.Optional["ServicePrincipalSamlSingleSignOn"], jsii.get(self, "samlSingleSignOnInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServicePrincipalTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServicePrincipalTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useExistingInput")
    def use_existing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useExistingInput"))

    @builtins.property
    @jsii.member(jsii_name="accountEnabled")
    def account_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "accountEnabled"))

    @account_enabled.setter
    def account_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "account_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="alternativeNames")
    def alternative_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alternativeNames"))

    @alternative_names.setter
    def alternative_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "alternative_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alternativeNames", value)

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="appRoleAssignmentRequired")
    def app_role_assignment_required(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "appRoleAssignmentRequired"))

    @app_role_assignment_required.setter
    def app_role_assignment_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "app_role_assignment_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appRoleAssignmentRequired", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loginUrl")
    def login_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginUrl"))

    @login_url.setter
    def login_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "login_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginUrl", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "notes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmailAddresses")
    def notification_email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEmailAddresses"))

    @notification_email_addresses.setter
    def notification_email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "notification_email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="owners")
    def owners(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "owners"))

    @owners.setter
    def owners(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "owners").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owners", value)

    @builtins.property
    @jsii.member(jsii_name="preferredSingleSignOnMode")
    def preferred_single_sign_on_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredSingleSignOnMode"))

    @preferred_single_sign_on_mode.setter
    def preferred_single_sign_on_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "preferred_single_sign_on_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredSingleSignOnMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="useExisting")
    def use_existing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useExisting"))

    @use_existing.setter
    def use_existing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipal, "use_existing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useExisting", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalAppRoles",
    jsii_struct_bases=[],
    name_mapping={},
)
class ServicePrincipalAppRoles:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalAppRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalAppRolesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalAppRolesList",
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
            type_hints = typing.get_type_hints(ServicePrincipalAppRolesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServicePrincipalAppRolesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalAppRolesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServicePrincipalAppRolesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalAppRolesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalAppRolesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalAppRolesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ServicePrincipalAppRolesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalAppRolesOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalAppRolesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allowedMemberTypes")
    def allowed_member_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMemberTypes"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServicePrincipalAppRoles]:
        return typing.cast(typing.Optional[ServicePrincipalAppRoles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServicePrincipalAppRoles]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalAppRolesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_id": "applicationId",
        "account_enabled": "accountEnabled",
        "alternative_names": "alternativeNames",
        "app_role_assignment_required": "appRoleAssignmentRequired",
        "description": "description",
        "features": "features",
        "feature_tags": "featureTags",
        "id": "id",
        "login_url": "loginUrl",
        "notes": "notes",
        "notification_email_addresses": "notificationEmailAddresses",
        "owners": "owners",
        "preferred_single_sign_on_mode": "preferredSingleSignOnMode",
        "saml_single_sign_on": "samlSingleSignOn",
        "tags": "tags",
        "timeouts": "timeouts",
        "use_existing": "useExisting",
    },
)
class ServicePrincipalConfig(cdktf.TerraformMetaArguments):
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
        application_id: builtins.str,
        account_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        app_role_assignment_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        features: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatures", typing.Dict[str, typing.Any]]]]] = None,
        feature_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServicePrincipalFeatureTags", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        login_url: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        notification_email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_single_sign_on_mode: typing.Optional[builtins.str] = None,
        saml_single_sign_on: typing.Optional[typing.Union["ServicePrincipalSamlSingleSignOn", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServicePrincipalTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_existing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param application_id: The application ID (client ID) of the application for which to create a service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#application_id ServicePrincipal#application_id}
        :param account_enabled: Whether or not the service principal account is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#account_enabled ServicePrincipal#account_enabled}
        :param alternative_names: A list of alternative names, used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#alternative_names ServicePrincipal#alternative_names}
        :param app_role_assignment_required: Whether this service principal requires an app role assignment to a user or group before Azure AD will issue a user or access token to the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#app_role_assignment_required ServicePrincipal#app_role_assignment_required}
        :param description: Description of the service principal provided for internal end-users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#description ServicePrincipal#description}
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#features ServicePrincipal#features}
        :param feature_tags: feature_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#feature_tags ServicePrincipal#feature_tags}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#id ServicePrincipal#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param login_url: The URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#login_url ServicePrincipal#login_url}
        :param notes: Free text field to capture information about the service principal, typically used for operational purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notes ServicePrincipal#notes}
        :param notification_email_addresses: List of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notification_email_addresses ServicePrincipal#notification_email_addresses}
        :param owners: A list of object IDs of principals that will be granted ownership of the service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#owners ServicePrincipal#owners}
        :param preferred_single_sign_on_mode: The single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#preferred_single_sign_on_mode ServicePrincipal#preferred_single_sign_on_mode}
        :param saml_single_sign_on: saml_single_sign_on block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#saml_single_sign_on ServicePrincipal#saml_single_sign_on}
        :param tags: A set of tags to apply to the service principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#tags ServicePrincipal#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#timeouts ServicePrincipal#timeouts}
        :param use_existing: When true, the resource will return an existing service principal instead of failing with an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#use_existing ServicePrincipal#use_existing}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(saml_single_sign_on, dict):
            saml_single_sign_on = ServicePrincipalSamlSingleSignOn(**saml_single_sign_on)
        if isinstance(timeouts, dict):
            timeouts = ServicePrincipalTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument account_enabled", value=account_enabled, expected_type=type_hints["account_enabled"])
            check_type(argname="argument alternative_names", value=alternative_names, expected_type=type_hints["alternative_names"])
            check_type(argname="argument app_role_assignment_required", value=app_role_assignment_required, expected_type=type_hints["app_role_assignment_required"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument feature_tags", value=feature_tags, expected_type=type_hints["feature_tags"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument login_url", value=login_url, expected_type=type_hints["login_url"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument notification_email_addresses", value=notification_email_addresses, expected_type=type_hints["notification_email_addresses"])
            check_type(argname="argument owners", value=owners, expected_type=type_hints["owners"])
            check_type(argname="argument preferred_single_sign_on_mode", value=preferred_single_sign_on_mode, expected_type=type_hints["preferred_single_sign_on_mode"])
            check_type(argname="argument saml_single_sign_on", value=saml_single_sign_on, expected_type=type_hints["saml_single_sign_on"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_existing", value=use_existing, expected_type=type_hints["use_existing"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
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
        if account_enabled is not None:
            self._values["account_enabled"] = account_enabled
        if alternative_names is not None:
            self._values["alternative_names"] = alternative_names
        if app_role_assignment_required is not None:
            self._values["app_role_assignment_required"] = app_role_assignment_required
        if description is not None:
            self._values["description"] = description
        if features is not None:
            self._values["features"] = features
        if feature_tags is not None:
            self._values["feature_tags"] = feature_tags
        if id is not None:
            self._values["id"] = id
        if login_url is not None:
            self._values["login_url"] = login_url
        if notes is not None:
            self._values["notes"] = notes
        if notification_email_addresses is not None:
            self._values["notification_email_addresses"] = notification_email_addresses
        if owners is not None:
            self._values["owners"] = owners
        if preferred_single_sign_on_mode is not None:
            self._values["preferred_single_sign_on_mode"] = preferred_single_sign_on_mode
        if saml_single_sign_on is not None:
            self._values["saml_single_sign_on"] = saml_single_sign_on
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_existing is not None:
            self._values["use_existing"] = use_existing

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
    def application_id(self) -> builtins.str:
        '''The application ID (client ID) of the application for which to create a service principal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#application_id ServicePrincipal#application_id}
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not the service principal account is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#account_enabled ServicePrincipal#account_enabled}
        '''
        result = self._values.get("account_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of alternative names, used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#alternative_names ServicePrincipal#alternative_names}
        '''
        result = self._values.get("alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def app_role_assignment_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal requires an app role assignment to a user or group before Azure AD will issue a user or access token to the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#app_role_assignment_required ServicePrincipal#app_role_assignment_required}
        '''
        result = self._values.get("app_role_assignment_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the service principal provided for internal end-users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#description ServicePrincipal#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def features(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatures"]]]:
        '''features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#features ServicePrincipal#features}
        '''
        result = self._values.get("features")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatures"]]], result)

    @builtins.property
    def feature_tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatureTags"]]]:
        '''feature_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#feature_tags ServicePrincipal#feature_tags}
        '''
        result = self._values.get("feature_tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServicePrincipalFeatureTags"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#id ServicePrincipal#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_url(self) -> typing.Optional[builtins.str]:
        '''The URL where the service provider redirects the user to Azure AD to authenticate.

        Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#login_url ServicePrincipal#login_url}
        '''
        result = self._values.get("login_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Free text field to capture information about the service principal, typically used for operational purposes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notes ServicePrincipal#notes}
        '''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email_addresses(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''List of email addresses where Azure AD sends a notification when the active certificate is near the expiration date.

        This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#notification_email_addresses ServicePrincipal#notification_email_addresses}
        '''
        result = self._values.get("notification_email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of object IDs of principals that will be granted ownership of the service principal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#owners ServicePrincipal#owners}
        '''
        result = self._values.get("owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_single_sign_on_mode(self) -> typing.Optional[builtins.str]:
        '''The single sign-on mode configured for this application.

        Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#preferred_single_sign_on_mode ServicePrincipal#preferred_single_sign_on_mode}
        '''
        result = self._values.get("preferred_single_sign_on_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml_single_sign_on(
        self,
    ) -> typing.Optional["ServicePrincipalSamlSingleSignOn"]:
        '''saml_single_sign_on block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#saml_single_sign_on ServicePrincipal#saml_single_sign_on}
        '''
        result = self._values.get("saml_single_sign_on")
        return typing.cast(typing.Optional["ServicePrincipalSamlSingleSignOn"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of tags to apply to the service principal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#tags ServicePrincipal#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServicePrincipalTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#timeouts ServicePrincipal#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServicePrincipalTimeouts"], result)

    @builtins.property
    def use_existing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the resource will return an existing service principal instead of failing with an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#use_existing ServicePrincipal#use_existing}
        '''
        result = self._values.get("use_existing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeatureTags",
    jsii_struct_bases=[],
    name_mapping={
        "custom_single_sign_on": "customSingleSignOn",
        "enterprise": "enterprise",
        "gallery": "gallery",
        "hide": "hide",
    },
)
class ServicePrincipalFeatureTags:
    def __init__(
        self,
        *,
        custom_single_sign_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enterprise: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gallery: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param custom_single_sign_on: Whether this service principal represents a custom SAML application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#custom_single_sign_on ServicePrincipal#custom_single_sign_on}
        :param enterprise: Whether this service principal represents an Enterprise Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#enterprise ServicePrincipal#enterprise}
        :param gallery: Whether this service principal represents a gallery application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#gallery ServicePrincipal#gallery}
        :param hide: Whether this app is invisible to users in My Apps and Office 365 Launcher. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#hide ServicePrincipal#hide}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalFeatureTags.__init__)
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
        '''Whether this service principal represents a custom SAML application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#custom_single_sign_on ServicePrincipal#custom_single_sign_on}
        '''
        result = self._values.get("custom_single_sign_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enterprise(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal represents an Enterprise Application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#enterprise ServicePrincipal#enterprise}
        '''
        result = self._values.get("enterprise")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gallery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal represents a gallery application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#gallery ServicePrincipal#gallery}
        '''
        result = self._values.get("gallery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hide(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this app is invisible to users in My Apps and Office 365 Launcher.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#hide ServicePrincipal#hide}
        '''
        result = self._values.get("hide")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalFeatureTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalFeatureTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeatureTagsList",
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
            type_hints = typing.get_type_hints(ServicePrincipalFeatureTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServicePrincipalFeatureTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalFeatureTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServicePrincipalFeatureTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatureTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatureTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatureTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServicePrincipalFeatureTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeatureTagsOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalFeatureTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsOutputReference, "custom_single_sign_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSingleSignOn", value)

    @builtins.property
    @jsii.member(jsii_name="enterprise")
    def enterprise(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enterprise"))

    @enterprise.setter
    def enterprise(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsOutputReference, "enterprise").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enterprise", value)

    @builtins.property
    @jsii.member(jsii_name="gallery")
    def gallery(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "gallery"))

    @gallery.setter
    def gallery(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsOutputReference, "gallery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gallery", value)

    @builtins.property
    @jsii.member(jsii_name="hide")
    def hide(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hide"))

    @hide.setter
    def hide(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsOutputReference, "hide").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hide", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServicePrincipalFeatureTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServicePrincipalFeatureTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServicePrincipalFeatureTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeatureTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "custom_single_sign_on_app": "customSingleSignOnApp",
        "enterprise_application": "enterpriseApplication",
        "gallery_application": "galleryApplication",
        "visible_to_users": "visibleToUsers",
    },
)
class ServicePrincipalFeatures:
    def __init__(
        self,
        *,
        custom_single_sign_on_app: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enterprise_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gallery_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visible_to_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param custom_single_sign_on_app: Whether this service principal represents a custom SAML application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#custom_single_sign_on_app ServicePrincipal#custom_single_sign_on_app}
        :param enterprise_application: Whether this service principal represents an Enterprise Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#enterprise_application ServicePrincipal#enterprise_application}
        :param gallery_application: Whether this service principal represents a gallery application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#gallery_application ServicePrincipal#gallery_application}
        :param visible_to_users: Whether this app is visible to users in My Apps and Office 365 Launcher. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#visible_to_users ServicePrincipal#visible_to_users}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalFeatures.__init__)
            check_type(argname="argument custom_single_sign_on_app", value=custom_single_sign_on_app, expected_type=type_hints["custom_single_sign_on_app"])
            check_type(argname="argument enterprise_application", value=enterprise_application, expected_type=type_hints["enterprise_application"])
            check_type(argname="argument gallery_application", value=gallery_application, expected_type=type_hints["gallery_application"])
            check_type(argname="argument visible_to_users", value=visible_to_users, expected_type=type_hints["visible_to_users"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_single_sign_on_app is not None:
            self._values["custom_single_sign_on_app"] = custom_single_sign_on_app
        if enterprise_application is not None:
            self._values["enterprise_application"] = enterprise_application
        if gallery_application is not None:
            self._values["gallery_application"] = gallery_application
        if visible_to_users is not None:
            self._values["visible_to_users"] = visible_to_users

    @builtins.property
    def custom_single_sign_on_app(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal represents a custom SAML application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#custom_single_sign_on_app ServicePrincipal#custom_single_sign_on_app}
        '''
        result = self._values.get("custom_single_sign_on_app")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enterprise_application(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal represents an Enterprise Application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#enterprise_application ServicePrincipal#enterprise_application}
        '''
        result = self._values.get("enterprise_application")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gallery_application(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this service principal represents a gallery application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#gallery_application ServicePrincipal#gallery_application}
        '''
        result = self._values.get("gallery_application")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def visible_to_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this app is visible to users in My Apps and Office 365 Launcher.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#visible_to_users ServicePrincipal#visible_to_users}
        '''
        result = self._values.get("visible_to_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalFeaturesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeaturesList",
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
            type_hints = typing.get_type_hints(ServicePrincipalFeaturesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServicePrincipalFeaturesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalFeaturesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServicePrincipalFeaturesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatures]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatures]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServicePrincipalFeatures]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServicePrincipalFeaturesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalFeaturesOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalFeaturesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomSingleSignOnApp")
    def reset_custom_single_sign_on_app(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSingleSignOnApp", []))

    @jsii.member(jsii_name="resetEnterpriseApplication")
    def reset_enterprise_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnterpriseApplication", []))

    @jsii.member(jsii_name="resetGalleryApplication")
    def reset_gallery_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGalleryApplication", []))

    @jsii.member(jsii_name="resetVisibleToUsers")
    def reset_visible_to_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibleToUsers", []))

    @builtins.property
    @jsii.member(jsii_name="customSingleSignOnAppInput")
    def custom_single_sign_on_app_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customSingleSignOnAppInput"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseApplicationInput")
    def enterprise_application_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enterpriseApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryApplicationInput")
    def gallery_application_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "galleryApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="visibleToUsersInput")
    def visible_to_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "visibleToUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="customSingleSignOnApp")
    def custom_single_sign_on_app(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customSingleSignOnApp"))

    @custom_single_sign_on_app.setter
    def custom_single_sign_on_app(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesOutputReference, "custom_single_sign_on_app").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSingleSignOnApp", value)

    @builtins.property
    @jsii.member(jsii_name="enterpriseApplication")
    def enterprise_application(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enterpriseApplication"))

    @enterprise_application.setter
    def enterprise_application(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesOutputReference, "enterprise_application").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enterpriseApplication", value)

    @builtins.property
    @jsii.member(jsii_name="galleryApplication")
    def gallery_application(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "galleryApplication"))

    @gallery_application.setter
    def gallery_application(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesOutputReference, "gallery_application").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "galleryApplication", value)

    @builtins.property
    @jsii.member(jsii_name="visibleToUsers")
    def visible_to_users(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "visibleToUsers"))

    @visible_to_users.setter
    def visible_to_users(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesOutputReference, "visible_to_users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleToUsers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServicePrincipalFeatures, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServicePrincipalFeatures, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServicePrincipalFeatures, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalFeaturesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalOauth2PermissionScopes",
    jsii_struct_bases=[],
    name_mapping={},
)
class ServicePrincipalOauth2PermissionScopes:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalOauth2PermissionScopes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalOauth2PermissionScopesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalOauth2PermissionScopesList",
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
            type_hints = typing.get_type_hints(ServicePrincipalOauth2PermissionScopesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServicePrincipalOauth2PermissionScopesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalOauth2PermissionScopesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServicePrincipalOauth2PermissionScopesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalOauth2PermissionScopesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalOauth2PermissionScopesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalOauth2PermissionScopesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ServicePrincipalOauth2PermissionScopesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalOauth2PermissionScopesOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalOauth2PermissionScopesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="adminConsentDescription")
    def admin_consent_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminConsentDescription"))

    @builtins.property
    @jsii.member(jsii_name="adminConsentDisplayName")
    def admin_consent_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminConsentDisplayName"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="userConsentDescription")
    def user_consent_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userConsentDescription"))

    @builtins.property
    @jsii.member(jsii_name="userConsentDisplayName")
    def user_consent_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userConsentDisplayName"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServicePrincipalOauth2PermissionScopes]:
        return typing.cast(typing.Optional[ServicePrincipalOauth2PermissionScopes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServicePrincipalOauth2PermissionScopes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalOauth2PermissionScopesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalSamlSingleSignOn",
    jsii_struct_bases=[],
    name_mapping={"relay_state": "relayState"},
)
class ServicePrincipalSamlSingleSignOn:
    def __init__(self, *, relay_state: typing.Optional[builtins.str] = None) -> None:
        '''
        :param relay_state: The relative URI the service provider would redirect to after completion of the single sign-on flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#relay_state ServicePrincipal#relay_state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalSamlSingleSignOn.__init__)
            check_type(argname="argument relay_state", value=relay_state, expected_type=type_hints["relay_state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if relay_state is not None:
            self._values["relay_state"] = relay_state

    @builtins.property
    def relay_state(self) -> typing.Optional[builtins.str]:
        '''The relative URI the service provider would redirect to after completion of the single sign-on flow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#relay_state ServicePrincipal#relay_state}
        '''
        result = self._values.get("relay_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalSamlSingleSignOn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalSamlSingleSignOnOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalSamlSingleSignOnOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalSamlSingleSignOnOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRelayState")
    def reset_relay_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelayState", []))

    @builtins.property
    @jsii.member(jsii_name="relayStateInput")
    def relay_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relayStateInput"))

    @builtins.property
    @jsii.member(jsii_name="relayState")
    def relay_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relayState"))

    @relay_state.setter
    def relay_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalSamlSingleSignOnOutputReference, "relay_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relayState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServicePrincipalSamlSingleSignOn]:
        return typing.cast(typing.Optional[ServicePrincipalSamlSingleSignOn], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServicePrincipalSamlSingleSignOn],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalSamlSingleSignOnOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ServicePrincipalTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#create ServicePrincipal#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#delete ServicePrincipal#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#read ServicePrincipal#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#update ServicePrincipal#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicePrincipalTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#create ServicePrincipal#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#delete ServicePrincipal#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#read ServicePrincipal#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/service_principal#update ServicePrincipal#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipalTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.servicePrincipal.ServicePrincipalTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ServicePrincipalTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServicePrincipalTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServicePrincipalTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServicePrincipalTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServicePrincipalTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicePrincipalTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServicePrincipal",
    "ServicePrincipalAppRoles",
    "ServicePrincipalAppRolesList",
    "ServicePrincipalAppRolesOutputReference",
    "ServicePrincipalConfig",
    "ServicePrincipalFeatureTags",
    "ServicePrincipalFeatureTagsList",
    "ServicePrincipalFeatureTagsOutputReference",
    "ServicePrincipalFeatures",
    "ServicePrincipalFeaturesList",
    "ServicePrincipalFeaturesOutputReference",
    "ServicePrincipalOauth2PermissionScopes",
    "ServicePrincipalOauth2PermissionScopesList",
    "ServicePrincipalOauth2PermissionScopesOutputReference",
    "ServicePrincipalSamlSingleSignOn",
    "ServicePrincipalSamlSingleSignOnOutputReference",
    "ServicePrincipalTimeouts",
    "ServicePrincipalTimeoutsOutputReference",
]

publication.publish()
