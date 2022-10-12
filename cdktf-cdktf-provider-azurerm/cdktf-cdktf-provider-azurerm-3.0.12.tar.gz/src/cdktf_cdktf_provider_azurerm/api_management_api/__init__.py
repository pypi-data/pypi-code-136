'''
# `azurerm_api_management_api`

Refer to the Terraform Registory for docs: [`azurerm_api_management_api`](https://www.terraform.io/docs/providers/azurerm/r/api_management_api).
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


class ApiManagementApi(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApi",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api azurerm_api_management_api}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        revision: builtins.str,
        api_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        import_: typing.Optional[typing.Union["ApiManagementApiImport", typing.Dict[str, typing.Any]]] = None,
        oauth2_authorization: typing.Optional[typing.Union["ApiManagementApiOauth2Authorization", typing.Dict[str, typing.Any]]] = None,
        openid_authentication: typing.Optional[typing.Union["ApiManagementApiOpenidAuthentication", typing.Dict[str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        revision_description: typing.Optional[builtins.str] = None,
        service_url: typing.Optional[builtins.str] = None,
        soap_pass_through: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_api_id: typing.Optional[builtins.str] = None,
        subscription_key_parameter_names: typing.Optional[typing.Union["ApiManagementApiSubscriptionKeyParameterNames", typing.Dict[str, typing.Any]]] = None,
        subscription_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
        version_set_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api azurerm_api_management_api} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_management_name ApiManagementApi#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#name ApiManagementApi#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#resource_group_name ApiManagementApi#resource_group_name}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision ApiManagementApi#revision}.
        :param api_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_type ApiManagementApi#api_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#description ApiManagementApi#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#display_name ApiManagementApi#display_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#id ApiManagementApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_: import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#import ApiManagementApi#import}
        :param oauth2_authorization: oauth2_authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#oauth2_authorization ApiManagementApi#oauth2_authorization}
        :param openid_authentication: openid_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_authentication ApiManagementApi#openid_authentication}
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#path ApiManagementApi#path}.
        :param protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#protocols ApiManagementApi#protocols}.
        :param revision_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision_description ApiManagementApi#revision_description}.
        :param service_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_url ApiManagementApi#service_url}.
        :param soap_pass_through: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#soap_pass_through ApiManagementApi#soap_pass_through}.
        :param source_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#source_api_id ApiManagementApi#source_api_id}.
        :param subscription_key_parameter_names: subscription_key_parameter_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_key_parameter_names ApiManagementApi#subscription_key_parameter_names}
        :param subscription_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_required ApiManagementApi#subscription_required}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#timeouts ApiManagementApi#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version ApiManagementApi#version}.
        :param version_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_description ApiManagementApi#version_description}.
        :param version_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_set_id ApiManagementApi#version_set_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApi.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementApiConfig(
            api_management_name=api_management_name,
            name=name,
            resource_group_name=resource_group_name,
            revision=revision,
            api_type=api_type,
            description=description,
            display_name=display_name,
            id=id,
            import_=import_,
            oauth2_authorization=oauth2_authorization,
            openid_authentication=openid_authentication,
            path=path,
            protocols=protocols,
            revision_description=revision_description,
            service_url=service_url,
            soap_pass_through=soap_pass_through,
            source_api_id=source_api_id,
            subscription_key_parameter_names=subscription_key_parameter_names,
            subscription_required=subscription_required,
            timeouts=timeouts,
            version=version,
            version_description=version_description,
            version_set_id=version_set_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putImport")
    def put_import(
        self,
        *,
        content_format: builtins.str,
        content_value: builtins.str,
        wsdl_selector: typing.Optional[typing.Union["ApiManagementApiImportWsdlSelector", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_format ApiManagementApi#content_format}.
        :param content_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_value ApiManagementApi#content_value}.
        :param wsdl_selector: wsdl_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#wsdl_selector ApiManagementApi#wsdl_selector}
        '''
        value = ApiManagementApiImport(
            content_format=content_format,
            content_value=content_value,
            wsdl_selector=wsdl_selector,
        )

        return typing.cast(None, jsii.invoke(self, "putImport", [value]))

    @jsii.member(jsii_name="putOauth2Authorization")
    def put_oauth2_authorization(
        self,
        *,
        authorization_server_name: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorization_server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#authorization_server_name ApiManagementApi#authorization_server_name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#scope ApiManagementApi#scope}.
        '''
        value = ApiManagementApiOauth2Authorization(
            authorization_server_name=authorization_server_name, scope=scope
        )

        return typing.cast(None, jsii.invoke(self, "putOauth2Authorization", [value]))

    @jsii.member(jsii_name="putOpenidAuthentication")
    def put_openid_authentication(
        self,
        *,
        openid_provider_name: builtins.str,
        bearer_token_sending_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param openid_provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_provider_name ApiManagementApi#openid_provider_name}.
        :param bearer_token_sending_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#bearer_token_sending_methods ApiManagementApi#bearer_token_sending_methods}.
        '''
        value = ApiManagementApiOpenidAuthentication(
            openid_provider_name=openid_provider_name,
            bearer_token_sending_methods=bearer_token_sending_methods,
        )

        return typing.cast(None, jsii.invoke(self, "putOpenidAuthentication", [value]))

    @jsii.member(jsii_name="putSubscriptionKeyParameterNames")
    def put_subscription_key_parameter_names(
        self,
        *,
        header: builtins.str,
        query: builtins.str,
    ) -> None:
        '''
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#header ApiManagementApi#header}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#query ApiManagementApi#query}.
        '''
        value = ApiManagementApiSubscriptionKeyParameterNames(
            header=header, query=query
        )

        return typing.cast(None, jsii.invoke(self, "putSubscriptionKeyParameterNames", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#create ApiManagementApi#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#delete ApiManagementApi#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#read ApiManagementApi#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#update ApiManagementApi#update}.
        '''
        value = ApiManagementApiTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApiType")
    def reset_api_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiType", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImport")
    def reset_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImport", []))

    @jsii.member(jsii_name="resetOauth2Authorization")
    def reset_oauth2_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2Authorization", []))

    @jsii.member(jsii_name="resetOpenidAuthentication")
    def reset_openid_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidAuthentication", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetProtocols")
    def reset_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocols", []))

    @jsii.member(jsii_name="resetRevisionDescription")
    def reset_revision_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevisionDescription", []))

    @jsii.member(jsii_name="resetServiceUrl")
    def reset_service_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceUrl", []))

    @jsii.member(jsii_name="resetSoapPassThrough")
    def reset_soap_pass_through(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoapPassThrough", []))

    @jsii.member(jsii_name="resetSourceApiId")
    def reset_source_api_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceApiId", []))

    @jsii.member(jsii_name="resetSubscriptionKeyParameterNames")
    def reset_subscription_key_parameter_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionKeyParameterNames", []))

    @jsii.member(jsii_name="resetSubscriptionRequired")
    def reset_subscription_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionRequired", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetVersionDescription")
    def reset_version_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionDescription", []))

    @jsii.member(jsii_name="resetVersionSetId")
    def reset_version_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionSetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="import")
    def import_(self) -> "ApiManagementApiImportOutputReference":
        return typing.cast("ApiManagementApiImportOutputReference", jsii.get(self, "import"))

    @builtins.property
    @jsii.member(jsii_name="isCurrent")
    def is_current(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isCurrent"))

    @builtins.property
    @jsii.member(jsii_name="isOnline")
    def is_online(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isOnline"))

    @builtins.property
    @jsii.member(jsii_name="oauth2Authorization")
    def oauth2_authorization(
        self,
    ) -> "ApiManagementApiOauth2AuthorizationOutputReference":
        return typing.cast("ApiManagementApiOauth2AuthorizationOutputReference", jsii.get(self, "oauth2Authorization"))

    @builtins.property
    @jsii.member(jsii_name="openidAuthentication")
    def openid_authentication(
        self,
    ) -> "ApiManagementApiOpenidAuthenticationOutputReference":
        return typing.cast("ApiManagementApiOpenidAuthenticationOutputReference", jsii.get(self, "openidAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionKeyParameterNames")
    def subscription_key_parameter_names(
        self,
    ) -> "ApiManagementApiSubscriptionKeyParameterNamesOutputReference":
        return typing.cast("ApiManagementApiSubscriptionKeyParameterNamesOutputReference", jsii.get(self, "subscriptionKeyParameterNames"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementApiTimeoutsOutputReference":
        return typing.cast("ApiManagementApiTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementNameInput")
    def api_management_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiTypeInput")
    def api_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importInput")
    def import_input(self) -> typing.Optional["ApiManagementApiImport"]:
        return typing.cast(typing.Optional["ApiManagementApiImport"], jsii.get(self, "importInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2AuthorizationInput")
    def oauth2_authorization_input(
        self,
    ) -> typing.Optional["ApiManagementApiOauth2Authorization"]:
        return typing.cast(typing.Optional["ApiManagementApiOauth2Authorization"], jsii.get(self, "oauth2AuthorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="openidAuthenticationInput")
    def openid_authentication_input(
        self,
    ) -> typing.Optional["ApiManagementApiOpenidAuthentication"]:
        return typing.cast(typing.Optional["ApiManagementApiOpenidAuthentication"], jsii.get(self, "openidAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolsInput")
    def protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionDescriptionInput")
    def revision_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceUrlInput")
    def service_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="soapPassThroughInput")
    def soap_pass_through_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "soapPassThroughInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceApiIdInput")
    def source_api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceApiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionKeyParameterNamesInput")
    def subscription_key_parameter_names_input(
        self,
    ) -> typing.Optional["ApiManagementApiSubscriptionKeyParameterNames"]:
        return typing.cast(typing.Optional["ApiManagementApiSubscriptionKeyParameterNames"], jsii.get(self, "subscriptionKeyParameterNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionRequiredInput")
    def subscription_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "subscriptionRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementApiTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementApiTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionDescriptionInput")
    def version_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="versionSetIdInput")
    def version_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "api_management_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

    @builtins.property
    @jsii.member(jsii_name="apiType")
    def api_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiType"))

    @api_type.setter
    def api_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "api_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocols", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "revision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="revisionDescription")
    def revision_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revisionDescription"))

    @revision_description.setter
    def revision_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "revision_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="serviceUrl")
    def service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUrl"))

    @service_url.setter
    def service_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "service_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="soapPassThrough")
    def soap_pass_through(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "soapPassThrough"))

    @soap_pass_through.setter
    def soap_pass_through(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "soap_pass_through").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "soapPassThrough", value)

    @builtins.property
    @jsii.member(jsii_name="sourceApiId")
    def source_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceApiId"))

    @source_api_id.setter
    def source_api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "source_api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceApiId", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionRequired")
    def subscription_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "subscriptionRequired"))

    @subscription_required.setter
    def subscription_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "subscription_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionRequired", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "version_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="versionSetId")
    def version_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionSetId"))

    @version_set_id.setter
    def version_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApi, "version_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionSetId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_name": "apiManagementName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "revision": "revision",
        "api_type": "apiType",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "import_": "import",
        "oauth2_authorization": "oauth2Authorization",
        "openid_authentication": "openidAuthentication",
        "path": "path",
        "protocols": "protocols",
        "revision_description": "revisionDescription",
        "service_url": "serviceUrl",
        "soap_pass_through": "soapPassThrough",
        "source_api_id": "sourceApiId",
        "subscription_key_parameter_names": "subscriptionKeyParameterNames",
        "subscription_required": "subscriptionRequired",
        "timeouts": "timeouts",
        "version": "version",
        "version_description": "versionDescription",
        "version_set_id": "versionSetId",
    },
)
class ApiManagementApiConfig(cdktf.TerraformMetaArguments):
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
        api_management_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        revision: builtins.str,
        api_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        import_: typing.Optional[typing.Union["ApiManagementApiImport", typing.Dict[str, typing.Any]]] = None,
        oauth2_authorization: typing.Optional[typing.Union["ApiManagementApiOauth2Authorization", typing.Dict[str, typing.Any]]] = None,
        openid_authentication: typing.Optional[typing.Union["ApiManagementApiOpenidAuthentication", typing.Dict[str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        revision_description: typing.Optional[builtins.str] = None,
        service_url: typing.Optional[builtins.str] = None,
        soap_pass_through: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_api_id: typing.Optional[builtins.str] = None,
        subscription_key_parameter_names: typing.Optional[typing.Union["ApiManagementApiSubscriptionKeyParameterNames", typing.Dict[str, typing.Any]]] = None,
        subscription_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
        version_set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_management_name ApiManagementApi#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#name ApiManagementApi#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#resource_group_name ApiManagementApi#resource_group_name}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision ApiManagementApi#revision}.
        :param api_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_type ApiManagementApi#api_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#description ApiManagementApi#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#display_name ApiManagementApi#display_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#id ApiManagementApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_: import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#import ApiManagementApi#import}
        :param oauth2_authorization: oauth2_authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#oauth2_authorization ApiManagementApi#oauth2_authorization}
        :param openid_authentication: openid_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_authentication ApiManagementApi#openid_authentication}
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#path ApiManagementApi#path}.
        :param protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#protocols ApiManagementApi#protocols}.
        :param revision_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision_description ApiManagementApi#revision_description}.
        :param service_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_url ApiManagementApi#service_url}.
        :param soap_pass_through: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#soap_pass_through ApiManagementApi#soap_pass_through}.
        :param source_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#source_api_id ApiManagementApi#source_api_id}.
        :param subscription_key_parameter_names: subscription_key_parameter_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_key_parameter_names ApiManagementApi#subscription_key_parameter_names}
        :param subscription_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_required ApiManagementApi#subscription_required}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#timeouts ApiManagementApi#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version ApiManagementApi#version}.
        :param version_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_description ApiManagementApi#version_description}.
        :param version_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_set_id ApiManagementApi#version_set_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(import_, dict):
            import_ = ApiManagementApiImport(**import_)
        if isinstance(oauth2_authorization, dict):
            oauth2_authorization = ApiManagementApiOauth2Authorization(**oauth2_authorization)
        if isinstance(openid_authentication, dict):
            openid_authentication = ApiManagementApiOpenidAuthentication(**openid_authentication)
        if isinstance(subscription_key_parameter_names, dict):
            subscription_key_parameter_names = ApiManagementApiSubscriptionKeyParameterNames(**subscription_key_parameter_names)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementApiTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            check_type(argname="argument api_type", value=api_type, expected_type=type_hints["api_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument import_", value=import_, expected_type=type_hints["import_"])
            check_type(argname="argument oauth2_authorization", value=oauth2_authorization, expected_type=type_hints["oauth2_authorization"])
            check_type(argname="argument openid_authentication", value=openid_authentication, expected_type=type_hints["openid_authentication"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument revision_description", value=revision_description, expected_type=type_hints["revision_description"])
            check_type(argname="argument service_url", value=service_url, expected_type=type_hints["service_url"])
            check_type(argname="argument soap_pass_through", value=soap_pass_through, expected_type=type_hints["soap_pass_through"])
            check_type(argname="argument source_api_id", value=source_api_id, expected_type=type_hints["source_api_id"])
            check_type(argname="argument subscription_key_parameter_names", value=subscription_key_parameter_names, expected_type=type_hints["subscription_key_parameter_names"])
            check_type(argname="argument subscription_required", value=subscription_required, expected_type=type_hints["subscription_required"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument version_description", value=version_description, expected_type=type_hints["version_description"])
            check_type(argname="argument version_set_id", value=version_set_id, expected_type=type_hints["version_set_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_name": api_management_name,
            "name": name,
            "resource_group_name": resource_group_name,
            "revision": revision,
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
        if api_type is not None:
            self._values["api_type"] = api_type
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if import_ is not None:
            self._values["import_"] = import_
        if oauth2_authorization is not None:
            self._values["oauth2_authorization"] = oauth2_authorization
        if openid_authentication is not None:
            self._values["openid_authentication"] = openid_authentication
        if path is not None:
            self._values["path"] = path
        if protocols is not None:
            self._values["protocols"] = protocols
        if revision_description is not None:
            self._values["revision_description"] = revision_description
        if service_url is not None:
            self._values["service_url"] = service_url
        if soap_pass_through is not None:
            self._values["soap_pass_through"] = soap_pass_through
        if source_api_id is not None:
            self._values["source_api_id"] = source_api_id
        if subscription_key_parameter_names is not None:
            self._values["subscription_key_parameter_names"] = subscription_key_parameter_names
        if subscription_required is not None:
            self._values["subscription_required"] = subscription_required
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version
        if version_description is not None:
            self._values["version_description"] = version_description
        if version_set_id is not None:
            self._values["version_set_id"] = version_set_id

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
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_management_name ApiManagementApi#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#name ApiManagementApi#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#resource_group_name ApiManagementApi#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision ApiManagementApi#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#api_type ApiManagementApi#api_type}.'''
        result = self._values.get("api_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#description ApiManagementApi#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#display_name ApiManagementApi#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#id ApiManagementApi#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_(self) -> typing.Optional["ApiManagementApiImport"]:
        '''import block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#import ApiManagementApi#import}
        '''
        result = self._values.get("import_")
        return typing.cast(typing.Optional["ApiManagementApiImport"], result)

    @builtins.property
    def oauth2_authorization(
        self,
    ) -> typing.Optional["ApiManagementApiOauth2Authorization"]:
        '''oauth2_authorization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#oauth2_authorization ApiManagementApi#oauth2_authorization}
        '''
        result = self._values.get("oauth2_authorization")
        return typing.cast(typing.Optional["ApiManagementApiOauth2Authorization"], result)

    @builtins.property
    def openid_authentication(
        self,
    ) -> typing.Optional["ApiManagementApiOpenidAuthentication"]:
        '''openid_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_authentication ApiManagementApi#openid_authentication}
        '''
        result = self._values.get("openid_authentication")
        return typing.cast(typing.Optional["ApiManagementApiOpenidAuthentication"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#path ApiManagementApi#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#protocols ApiManagementApi#protocols}.'''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def revision_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#revision_description ApiManagementApi#revision_description}.'''
        result = self._values.get("revision_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_url ApiManagementApi#service_url}.'''
        result = self._values.get("service_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def soap_pass_through(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#soap_pass_through ApiManagementApi#soap_pass_through}.'''
        result = self._values.get("soap_pass_through")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_api_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#source_api_id ApiManagementApi#source_api_id}.'''
        result = self._values.get("source_api_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_key_parameter_names(
        self,
    ) -> typing.Optional["ApiManagementApiSubscriptionKeyParameterNames"]:
        '''subscription_key_parameter_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_key_parameter_names ApiManagementApi#subscription_key_parameter_names}
        '''
        result = self._values.get("subscription_key_parameter_names")
        return typing.cast(typing.Optional["ApiManagementApiSubscriptionKeyParameterNames"], result)

    @builtins.property
    def subscription_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#subscription_required ApiManagementApi#subscription_required}.'''
        result = self._values.get("subscription_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementApiTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#timeouts ApiManagementApi#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementApiTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version ApiManagementApi#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_description ApiManagementApi#version_description}.'''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#version_set_id ApiManagementApi#version_set_id}.'''
        result = self._values.get("version_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiImport",
    jsii_struct_bases=[],
    name_mapping={
        "content_format": "contentFormat",
        "content_value": "contentValue",
        "wsdl_selector": "wsdlSelector",
    },
)
class ApiManagementApiImport:
    def __init__(
        self,
        *,
        content_format: builtins.str,
        content_value: builtins.str,
        wsdl_selector: typing.Optional[typing.Union["ApiManagementApiImportWsdlSelector", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_format ApiManagementApi#content_format}.
        :param content_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_value ApiManagementApi#content_value}.
        :param wsdl_selector: wsdl_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#wsdl_selector ApiManagementApi#wsdl_selector}
        '''
        if isinstance(wsdl_selector, dict):
            wsdl_selector = ApiManagementApiImportWsdlSelector(**wsdl_selector)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiImport.__init__)
            check_type(argname="argument content_format", value=content_format, expected_type=type_hints["content_format"])
            check_type(argname="argument content_value", value=content_value, expected_type=type_hints["content_value"])
            check_type(argname="argument wsdl_selector", value=wsdl_selector, expected_type=type_hints["wsdl_selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_format": content_format,
            "content_value": content_value,
        }
        if wsdl_selector is not None:
            self._values["wsdl_selector"] = wsdl_selector

    @builtins.property
    def content_format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_format ApiManagementApi#content_format}.'''
        result = self._values.get("content_format")
        assert result is not None, "Required property 'content_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#content_value ApiManagementApi#content_value}.'''
        result = self._values.get("content_value")
        assert result is not None, "Required property 'content_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wsdl_selector(self) -> typing.Optional["ApiManagementApiImportWsdlSelector"]:
        '''wsdl_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#wsdl_selector ApiManagementApi#wsdl_selector}
        '''
        result = self._values.get("wsdl_selector")
        return typing.cast(typing.Optional["ApiManagementApiImportWsdlSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiImport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiImportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiImportOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiImportOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWsdlSelector")
    def put_wsdl_selector(
        self,
        *,
        endpoint_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#endpoint_name ApiManagementApi#endpoint_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_name ApiManagementApi#service_name}.
        '''
        value = ApiManagementApiImportWsdlSelector(
            endpoint_name=endpoint_name, service_name=service_name
        )

        return typing.cast(None, jsii.invoke(self, "putWsdlSelector", [value]))

    @jsii.member(jsii_name="resetWsdlSelector")
    def reset_wsdl_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWsdlSelector", []))

    @builtins.property
    @jsii.member(jsii_name="wsdlSelector")
    def wsdl_selector(self) -> "ApiManagementApiImportWsdlSelectorOutputReference":
        return typing.cast("ApiManagementApiImportWsdlSelectorOutputReference", jsii.get(self, "wsdlSelector"))

    @builtins.property
    @jsii.member(jsii_name="contentFormatInput")
    def content_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="contentValueInput")
    def content_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentValueInput"))

    @builtins.property
    @jsii.member(jsii_name="wsdlSelectorInput")
    def wsdl_selector_input(
        self,
    ) -> typing.Optional["ApiManagementApiImportWsdlSelector"]:
        return typing.cast(typing.Optional["ApiManagementApiImportWsdlSelector"], jsii.get(self, "wsdlSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="contentFormat")
    def content_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentFormat"))

    @content_format.setter
    def content_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportOutputReference, "content_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentFormat", value)

    @builtins.property
    @jsii.member(jsii_name="contentValue")
    def content_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentValue"))

    @content_value.setter
    def content_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportOutputReference, "content_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementApiImport]:
        return typing.cast(typing.Optional[ApiManagementApiImport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementApiImport]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiImportWsdlSelector",
    jsii_struct_bases=[],
    name_mapping={"endpoint_name": "endpointName", "service_name": "serviceName"},
)
class ApiManagementApiImportWsdlSelector:
    def __init__(
        self,
        *,
        endpoint_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#endpoint_name ApiManagementApi#endpoint_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_name ApiManagementApi#service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiImportWsdlSelector.__init__)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_name": endpoint_name,
            "service_name": service_name,
        }

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#endpoint_name ApiManagementApi#endpoint_name}.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#service_name ApiManagementApi#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiImportWsdlSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiImportWsdlSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiImportWsdlSelectorOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiImportWsdlSelectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointNameInput")
    def endpoint_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportWsdlSelectorOutputReference, "endpoint_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportWsdlSelectorOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementApiImportWsdlSelector]:
        return typing.cast(typing.Optional[ApiManagementApiImportWsdlSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiImportWsdlSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiImportWsdlSelectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiOauth2Authorization",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_server_name": "authorizationServerName",
        "scope": "scope",
    },
)
class ApiManagementApiOauth2Authorization:
    def __init__(
        self,
        *,
        authorization_server_name: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorization_server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#authorization_server_name ApiManagementApi#authorization_server_name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#scope ApiManagementApi#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOauth2Authorization.__init__)
            check_type(argname="argument authorization_server_name", value=authorization_server_name, expected_type=type_hints["authorization_server_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_server_name": authorization_server_name,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def authorization_server_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#authorization_server_name ApiManagementApi#authorization_server_name}.'''
        result = self._values.get("authorization_server_name")
        assert result is not None, "Required property 'authorization_server_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#scope ApiManagementApi#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOauth2Authorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOauth2AuthorizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiOauth2AuthorizationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOauth2AuthorizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationServerNameInput")
    def authorization_server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationServerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationServerName")
    def authorization_server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationServerName"))

    @authorization_server_name.setter
    def authorization_server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOauth2AuthorizationOutputReference, "authorization_server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationServerName", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOauth2AuthorizationOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementApiOauth2Authorization]:
        return typing.cast(typing.Optional[ApiManagementApiOauth2Authorization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiOauth2Authorization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOauth2AuthorizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiOpenidAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "openid_provider_name": "openidProviderName",
        "bearer_token_sending_methods": "bearerTokenSendingMethods",
    },
)
class ApiManagementApiOpenidAuthentication:
    def __init__(
        self,
        *,
        openid_provider_name: builtins.str,
        bearer_token_sending_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param openid_provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_provider_name ApiManagementApi#openid_provider_name}.
        :param bearer_token_sending_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#bearer_token_sending_methods ApiManagementApi#bearer_token_sending_methods}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOpenidAuthentication.__init__)
            check_type(argname="argument openid_provider_name", value=openid_provider_name, expected_type=type_hints["openid_provider_name"])
            check_type(argname="argument bearer_token_sending_methods", value=bearer_token_sending_methods, expected_type=type_hints["bearer_token_sending_methods"])
        self._values: typing.Dict[str, typing.Any] = {
            "openid_provider_name": openid_provider_name,
        }
        if bearer_token_sending_methods is not None:
            self._values["bearer_token_sending_methods"] = bearer_token_sending_methods

    @builtins.property
    def openid_provider_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#openid_provider_name ApiManagementApi#openid_provider_name}.'''
        result = self._values.get("openid_provider_name")
        assert result is not None, "Required property 'openid_provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bearer_token_sending_methods(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#bearer_token_sending_methods ApiManagementApi#bearer_token_sending_methods}.'''
        result = self._values.get("bearer_token_sending_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOpenidAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOpenidAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiOpenidAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOpenidAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBearerTokenSendingMethods")
    def reset_bearer_token_sending_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBearerTokenSendingMethods", []))

    @builtins.property
    @jsii.member(jsii_name="bearerTokenSendingMethodsInput")
    def bearer_token_sending_methods_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bearerTokenSendingMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="openidProviderNameInput")
    def openid_provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "openidProviderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bearerTokenSendingMethods")
    def bearer_token_sending_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bearerTokenSendingMethods"))

    @bearer_token_sending_methods.setter
    def bearer_token_sending_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOpenidAuthenticationOutputReference, "bearer_token_sending_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bearerTokenSendingMethods", value)

    @builtins.property
    @jsii.member(jsii_name="openidProviderName")
    def openid_provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "openidProviderName"))

    @openid_provider_name.setter
    def openid_provider_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOpenidAuthenticationOutputReference, "openid_provider_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openidProviderName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementApiOpenidAuthentication]:
        return typing.cast(typing.Optional[ApiManagementApiOpenidAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiOpenidAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOpenidAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiSubscriptionKeyParameterNames",
    jsii_struct_bases=[],
    name_mapping={"header": "header", "query": "query"},
)
class ApiManagementApiSubscriptionKeyParameterNames:
    def __init__(self, *, header: builtins.str, query: builtins.str) -> None:
        '''
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#header ApiManagementApi#header}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#query ApiManagementApi#query}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiSubscriptionKeyParameterNames.__init__)
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "header": header,
            "query": query,
        }

    @builtins.property
    def header(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#header ApiManagementApi#header}.'''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#query ApiManagementApi#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiSubscriptionKeyParameterNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiSubscriptionKeyParameterNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiSubscriptionKeyParameterNamesOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiSubscriptionKeyParameterNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "header"))

    @header.setter
    def header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiSubscriptionKeyParameterNamesOutputReference, "header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiSubscriptionKeyParameterNamesOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiSubscriptionKeyParameterNames]:
        return typing.cast(typing.Optional[ApiManagementApiSubscriptionKeyParameterNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiSubscriptionKeyParameterNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiSubscriptionKeyParameterNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementApiTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#create ApiManagementApi#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#delete ApiManagementApi#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#read ApiManagementApi#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#update ApiManagementApi#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#create ApiManagementApi#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#delete ApiManagementApi#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#read ApiManagementApi#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api#update ApiManagementApi#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApi.ApiManagementApiTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementApi",
    "ApiManagementApiConfig",
    "ApiManagementApiImport",
    "ApiManagementApiImportOutputReference",
    "ApiManagementApiImportWsdlSelector",
    "ApiManagementApiImportWsdlSelectorOutputReference",
    "ApiManagementApiOauth2Authorization",
    "ApiManagementApiOauth2AuthorizationOutputReference",
    "ApiManagementApiOpenidAuthentication",
    "ApiManagementApiOpenidAuthenticationOutputReference",
    "ApiManagementApiSubscriptionKeyParameterNames",
    "ApiManagementApiSubscriptionKeyParameterNamesOutputReference",
    "ApiManagementApiTimeouts",
    "ApiManagementApiTimeoutsOutputReference",
]

publication.publish()
