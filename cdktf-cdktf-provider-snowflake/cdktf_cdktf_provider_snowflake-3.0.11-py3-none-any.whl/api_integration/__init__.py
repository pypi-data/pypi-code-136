'''
# `snowflake_api_integration`

Refer to the Terraform Registory for docs: [`snowflake_api_integration`](https://www.terraform.io/docs/providers/snowflake/r/api_integration).
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


class ApiIntegration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.apiIntegration.ApiIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration snowflake_api_integration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_allowed_prefixes: typing.Sequence[builtins.str],
        api_provider: builtins.str,
        name: builtins.str,
        api_aws_role_arn: typing.Optional[builtins.str] = None,
        api_blocked_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_ad_application_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration snowflake_api_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_allowed_prefixes: Explicitly limits external functions that use the integration to reference one or more HTTPS proxy service endpoints and resources within those proxies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_allowed_prefixes ApiIntegration#api_allowed_prefixes}
        :param api_provider: Specifies the HTTPS proxy service type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_provider ApiIntegration#api_provider}
        :param name: Specifies the name of the API integration. This name follows the rules for Object Identifiers. The name should be unique among api integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#name ApiIntegration#name}
        :param api_aws_role_arn: ARN of a cloud platform role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_aws_role_arn ApiIntegration#api_aws_role_arn}
        :param api_blocked_prefixes: Lists the endpoints and resources in the HTTPS proxy service that are not allowed to be called from Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_blocked_prefixes ApiIntegration#api_blocked_prefixes}
        :param azure_ad_application_id: The 'Application (client) id' of the Azure AD app for your remote service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_ad_application_id ApiIntegration#azure_ad_application_id}
        :param azure_tenant_id: Specifies the ID for your Office 365 tenant that all Azure API Management instances belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_tenant_id ApiIntegration#azure_tenant_id}
        :param enabled: Specifies whether this API integration is enabled or disabled. If the API integration is disabled, any external function that relies on it will not work. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#enabled ApiIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#id ApiIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiIntegration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiIntegrationConfig(
            api_allowed_prefixes=api_allowed_prefixes,
            api_provider=api_provider,
            name=name,
            api_aws_role_arn=api_aws_role_arn,
            api_blocked_prefixes=api_blocked_prefixes,
            azure_ad_application_id=azure_ad_application_id,
            azure_tenant_id=azure_tenant_id,
            enabled=enabled,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetApiAwsRoleArn")
    def reset_api_aws_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiAwsRoleArn", []))

    @jsii.member(jsii_name="resetApiBlockedPrefixes")
    def reset_api_blocked_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiBlockedPrefixes", []))

    @jsii.member(jsii_name="resetAzureAdApplicationId")
    def reset_azure_ad_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAdApplicationId", []))

    @jsii.member(jsii_name="resetAzureTenantId")
    def reset_azure_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureTenantId", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiAwsExternalId")
    def api_aws_external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiAwsExternalId"))

    @builtins.property
    @jsii.member(jsii_name="apiAwsIamUserArn")
    def api_aws_iam_user_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiAwsIamUserArn"))

    @builtins.property
    @jsii.member(jsii_name="azureConsentUrl")
    def azure_consent_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureConsentUrl"))

    @builtins.property
    @jsii.member(jsii_name="azureMultiTenantAppName")
    def azure_multi_tenant_app_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureMultiTenantAppName"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="apiAllowedPrefixesInput")
    def api_allowed_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiAllowedPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiAwsRoleArnInput")
    def api_aws_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiAwsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="apiBlockedPrefixesInput")
    def api_blocked_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiBlockedPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiProviderInput")
    def api_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAdApplicationIdInput")
    def azure_ad_application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureAdApplicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureTenantIdInput")
    def azure_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantIdInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiAllowedPrefixes")
    def api_allowed_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiAllowedPrefixes"))

    @api_allowed_prefixes.setter
    def api_allowed_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "api_allowed_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiAllowedPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="apiAwsRoleArn")
    def api_aws_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiAwsRoleArn"))

    @api_aws_role_arn.setter
    def api_aws_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "api_aws_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiAwsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="apiBlockedPrefixes")
    def api_blocked_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiBlockedPrefixes"))

    @api_blocked_prefixes.setter
    def api_blocked_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "api_blocked_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiBlockedPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="apiProvider")
    def api_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiProvider"))

    @api_provider.setter
    def api_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "api_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiProvider", value)

    @builtins.property
    @jsii.member(jsii_name="azureAdApplicationId")
    def azure_ad_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureAdApplicationId"))

    @azure_ad_application_id.setter
    def azure_ad_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "azure_ad_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureAdApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="azureTenantId")
    def azure_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureTenantId"))

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "azure_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiIntegration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.apiIntegration.ApiIntegrationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_allowed_prefixes": "apiAllowedPrefixes",
        "api_provider": "apiProvider",
        "name": "name",
        "api_aws_role_arn": "apiAwsRoleArn",
        "api_blocked_prefixes": "apiBlockedPrefixes",
        "azure_ad_application_id": "azureAdApplicationId",
        "azure_tenant_id": "azureTenantId",
        "enabled": "enabled",
        "id": "id",
    },
)
class ApiIntegrationConfig(cdktf.TerraformMetaArguments):
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
        api_allowed_prefixes: typing.Sequence[builtins.str],
        api_provider: builtins.str,
        name: builtins.str,
        api_aws_role_arn: typing.Optional[builtins.str] = None,
        api_blocked_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_ad_application_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_allowed_prefixes: Explicitly limits external functions that use the integration to reference one or more HTTPS proxy service endpoints and resources within those proxies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_allowed_prefixes ApiIntegration#api_allowed_prefixes}
        :param api_provider: Specifies the HTTPS proxy service type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_provider ApiIntegration#api_provider}
        :param name: Specifies the name of the API integration. This name follows the rules for Object Identifiers. The name should be unique among api integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#name ApiIntegration#name}
        :param api_aws_role_arn: ARN of a cloud platform role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_aws_role_arn ApiIntegration#api_aws_role_arn}
        :param api_blocked_prefixes: Lists the endpoints and resources in the HTTPS proxy service that are not allowed to be called from Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_blocked_prefixes ApiIntegration#api_blocked_prefixes}
        :param azure_ad_application_id: The 'Application (client) id' of the Azure AD app for your remote service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_ad_application_id ApiIntegration#azure_ad_application_id}
        :param azure_tenant_id: Specifies the ID for your Office 365 tenant that all Azure API Management instances belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_tenant_id ApiIntegration#azure_tenant_id}
        :param enabled: Specifies whether this API integration is enabled or disabled. If the API integration is disabled, any external function that relies on it will not work. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#enabled ApiIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#id ApiIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ApiIntegrationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_allowed_prefixes", value=api_allowed_prefixes, expected_type=type_hints["api_allowed_prefixes"])
            check_type(argname="argument api_provider", value=api_provider, expected_type=type_hints["api_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_aws_role_arn", value=api_aws_role_arn, expected_type=type_hints["api_aws_role_arn"])
            check_type(argname="argument api_blocked_prefixes", value=api_blocked_prefixes, expected_type=type_hints["api_blocked_prefixes"])
            check_type(argname="argument azure_ad_application_id", value=azure_ad_application_id, expected_type=type_hints["azure_ad_application_id"])
            check_type(argname="argument azure_tenant_id", value=azure_tenant_id, expected_type=type_hints["azure_tenant_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_allowed_prefixes": api_allowed_prefixes,
            "api_provider": api_provider,
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
        if api_aws_role_arn is not None:
            self._values["api_aws_role_arn"] = api_aws_role_arn
        if api_blocked_prefixes is not None:
            self._values["api_blocked_prefixes"] = api_blocked_prefixes
        if azure_ad_application_id is not None:
            self._values["azure_ad_application_id"] = azure_ad_application_id
        if azure_tenant_id is not None:
            self._values["azure_tenant_id"] = azure_tenant_id
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id

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
    def api_allowed_prefixes(self) -> typing.List[builtins.str]:
        '''Explicitly limits external functions that use the integration to reference one or more HTTPS proxy service endpoints and resources within those proxies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_allowed_prefixes ApiIntegration#api_allowed_prefixes}
        '''
        result = self._values.get("api_allowed_prefixes")
        assert result is not None, "Required property 'api_allowed_prefixes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def api_provider(self) -> builtins.str:
        '''Specifies the HTTPS proxy service type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_provider ApiIntegration#api_provider}
        '''
        result = self._values.get("api_provider")
        assert result is not None, "Required property 'api_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the API integration.

        This name follows the rules for Object Identifiers. The name should be unique among api integrations in your account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#name ApiIntegration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_aws_role_arn(self) -> typing.Optional[builtins.str]:
        '''ARN of a cloud platform role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_aws_role_arn ApiIntegration#api_aws_role_arn}
        '''
        result = self._values.get("api_aws_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_blocked_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Lists the endpoints and resources in the HTTPS proxy service that are not allowed to be called from Snowflake.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#api_blocked_prefixes ApiIntegration#api_blocked_prefixes}
        '''
        result = self._values.get("api_blocked_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def azure_ad_application_id(self) -> typing.Optional[builtins.str]:
        '''The 'Application (client) id' of the Azure AD app for your remote service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_ad_application_id ApiIntegration#azure_ad_application_id}
        '''
        result = self._values.get("azure_ad_application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID for your Office 365 tenant that all Azure API Management instances belong to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#azure_tenant_id ApiIntegration#azure_tenant_id}
        '''
        result = self._values.get("azure_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether this API integration is enabled or disabled.

        If the API integration is disabled, any external function that relies on it will not work.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#enabled ApiIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/api_integration#id ApiIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiIntegration",
    "ApiIntegrationConfig",
]

publication.publish()
