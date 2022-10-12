'''
# `azurerm_bot_service_azure_bot`

Refer to the Terraform Registory for docs: [`azurerm_bot_service_azure_bot`](https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot).
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


class BotServiceAzureBot(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.botServiceAzureBot.BotServiceAzureBot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot azurerm_bot_service_azure_bot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        microsoft_app_id: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        developer_app_insights_api_key: typing.Optional[builtins.str] = None,
        developer_app_insights_application_id: typing.Optional[builtins.str] = None,
        developer_app_insights_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        luis_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        luis_key: typing.Optional[builtins.str] = None,
        microsoft_app_msi_id: typing.Optional[builtins.str] = None,
        microsoft_app_tenant_id: typing.Optional[builtins.str] = None,
        microsoft_app_type: typing.Optional[builtins.str] = None,
        streaming_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["BotServiceAzureBotTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot azurerm_bot_service_azure_bot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#location BotServiceAzureBot#location}.
        :param microsoft_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_id BotServiceAzureBot#microsoft_app_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#name BotServiceAzureBot#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#resource_group_name BotServiceAzureBot#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#sku BotServiceAzureBot#sku}.
        :param developer_app_insights_api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_api_key BotServiceAzureBot#developer_app_insights_api_key}.
        :param developer_app_insights_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_application_id BotServiceAzureBot#developer_app_insights_application_id}.
        :param developer_app_insights_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_key BotServiceAzureBot#developer_app_insights_key}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#display_name BotServiceAzureBot#display_name}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#endpoint BotServiceAzureBot#endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#id BotServiceAzureBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param luis_app_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_app_ids BotServiceAzureBot#luis_app_ids}.
        :param luis_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_key BotServiceAzureBot#luis_key}.
        :param microsoft_app_msi_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_msi_id BotServiceAzureBot#microsoft_app_msi_id}.
        :param microsoft_app_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_tenant_id BotServiceAzureBot#microsoft_app_tenant_id}.
        :param microsoft_app_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_type BotServiceAzureBot#microsoft_app_type}.
        :param streaming_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#streaming_endpoint_enabled BotServiceAzureBot#streaming_endpoint_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#tags BotServiceAzureBot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#timeouts BotServiceAzureBot#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BotServiceAzureBot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BotServiceAzureBotConfig(
            location=location,
            microsoft_app_id=microsoft_app_id,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            developer_app_insights_api_key=developer_app_insights_api_key,
            developer_app_insights_application_id=developer_app_insights_application_id,
            developer_app_insights_key=developer_app_insights_key,
            display_name=display_name,
            endpoint=endpoint,
            id=id,
            luis_app_ids=luis_app_ids,
            luis_key=luis_key,
            microsoft_app_msi_id=microsoft_app_msi_id,
            microsoft_app_tenant_id=microsoft_app_tenant_id,
            microsoft_app_type=microsoft_app_type,
            streaming_endpoint_enabled=streaming_endpoint_enabled,
            tags=tags,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#create BotServiceAzureBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#delete BotServiceAzureBot#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#read BotServiceAzureBot#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#update BotServiceAzureBot#update}.
        '''
        value = BotServiceAzureBotTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDeveloperAppInsightsApiKey")
    def reset_developer_app_insights_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperAppInsightsApiKey", []))

    @jsii.member(jsii_name="resetDeveloperAppInsightsApplicationId")
    def reset_developer_app_insights_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperAppInsightsApplicationId", []))

    @jsii.member(jsii_name="resetDeveloperAppInsightsKey")
    def reset_developer_app_insights_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperAppInsightsKey", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLuisAppIds")
    def reset_luis_app_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLuisAppIds", []))

    @jsii.member(jsii_name="resetLuisKey")
    def reset_luis_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLuisKey", []))

    @jsii.member(jsii_name="resetMicrosoftAppMsiId")
    def reset_microsoft_app_msi_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoftAppMsiId", []))

    @jsii.member(jsii_name="resetMicrosoftAppTenantId")
    def reset_microsoft_app_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoftAppTenantId", []))

    @jsii.member(jsii_name="resetMicrosoftAppType")
    def reset_microsoft_app_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoftAppType", []))

    @jsii.member(jsii_name="resetStreamingEndpointEnabled")
    def reset_streaming_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamingEndpointEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BotServiceAzureBotTimeoutsOutputReference":
        return typing.cast("BotServiceAzureBotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsApiKeyInput")
    def developer_app_insights_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "developerAppInsightsApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsApplicationIdInput")
    def developer_app_insights_application_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "developerAppInsightsApplicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsKeyInput")
    def developer_app_insights_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "developerAppInsightsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="luisAppIdsInput")
    def luis_app_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "luisAppIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="luisKeyInput")
    def luis_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "luisKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftAppIdInput")
    def microsoft_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "microsoftAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftAppMsiIdInput")
    def microsoft_app_msi_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "microsoftAppMsiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftAppTenantIdInput")
    def microsoft_app_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "microsoftAppTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftAppTypeInput")
    def microsoft_app_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "microsoftAppTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingEndpointEnabledInput")
    def streaming_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "streamingEndpointEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BotServiceAzureBotTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BotServiceAzureBotTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsApiKey")
    def developer_app_insights_api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developerAppInsightsApiKey"))

    @developer_app_insights_api_key.setter
    def developer_app_insights_api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "developer_app_insights_api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developerAppInsightsApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsApplicationId")
    def developer_app_insights_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developerAppInsightsApplicationId"))

    @developer_app_insights_application_id.setter
    def developer_app_insights_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "developer_app_insights_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developerAppInsightsApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="developerAppInsightsKey")
    def developer_app_insights_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developerAppInsightsKey"))

    @developer_app_insights_key.setter
    def developer_app_insights_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "developer_app_insights_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developerAppInsightsKey", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="luisAppIds")
    def luis_app_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "luisAppIds"))

    @luis_app_ids.setter
    def luis_app_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "luis_app_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "luisAppIds", value)

    @builtins.property
    @jsii.member(jsii_name="luisKey")
    def luis_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "luisKey"))

    @luis_key.setter
    def luis_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "luis_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "luisKey", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftAppId")
    def microsoft_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "microsoftAppId"))

    @microsoft_app_id.setter
    def microsoft_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "microsoft_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftAppId", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftAppMsiId")
    def microsoft_app_msi_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "microsoftAppMsiId"))

    @microsoft_app_msi_id.setter
    def microsoft_app_msi_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "microsoft_app_msi_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftAppMsiId", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftAppTenantId")
    def microsoft_app_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "microsoftAppTenantId"))

    @microsoft_app_tenant_id.setter
    def microsoft_app_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "microsoft_app_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftAppTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftAppType")
    def microsoft_app_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "microsoftAppType"))

    @microsoft_app_type.setter
    def microsoft_app_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "microsoft_app_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftAppType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="streamingEndpointEnabled")
    def streaming_endpoint_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "streamingEndpointEnabled"))

    @streaming_endpoint_enabled.setter
    def streaming_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "streaming_endpoint_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingEndpointEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBot, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.botServiceAzureBot.BotServiceAzureBotConfig",
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
        "microsoft_app_id": "microsoftAppId",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "developer_app_insights_api_key": "developerAppInsightsApiKey",
        "developer_app_insights_application_id": "developerAppInsightsApplicationId",
        "developer_app_insights_key": "developerAppInsightsKey",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "id": "id",
        "luis_app_ids": "luisAppIds",
        "luis_key": "luisKey",
        "microsoft_app_msi_id": "microsoftAppMsiId",
        "microsoft_app_tenant_id": "microsoftAppTenantId",
        "microsoft_app_type": "microsoftAppType",
        "streaming_endpoint_enabled": "streamingEndpointEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class BotServiceAzureBotConfig(cdktf.TerraformMetaArguments):
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
        microsoft_app_id: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        developer_app_insights_api_key: typing.Optional[builtins.str] = None,
        developer_app_insights_application_id: typing.Optional[builtins.str] = None,
        developer_app_insights_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        luis_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        luis_key: typing.Optional[builtins.str] = None,
        microsoft_app_msi_id: typing.Optional[builtins.str] = None,
        microsoft_app_tenant_id: typing.Optional[builtins.str] = None,
        microsoft_app_type: typing.Optional[builtins.str] = None,
        streaming_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["BotServiceAzureBotTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#location BotServiceAzureBot#location}.
        :param microsoft_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_id BotServiceAzureBot#microsoft_app_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#name BotServiceAzureBot#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#resource_group_name BotServiceAzureBot#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#sku BotServiceAzureBot#sku}.
        :param developer_app_insights_api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_api_key BotServiceAzureBot#developer_app_insights_api_key}.
        :param developer_app_insights_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_application_id BotServiceAzureBot#developer_app_insights_application_id}.
        :param developer_app_insights_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_key BotServiceAzureBot#developer_app_insights_key}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#display_name BotServiceAzureBot#display_name}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#endpoint BotServiceAzureBot#endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#id BotServiceAzureBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param luis_app_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_app_ids BotServiceAzureBot#luis_app_ids}.
        :param luis_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_key BotServiceAzureBot#luis_key}.
        :param microsoft_app_msi_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_msi_id BotServiceAzureBot#microsoft_app_msi_id}.
        :param microsoft_app_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_tenant_id BotServiceAzureBot#microsoft_app_tenant_id}.
        :param microsoft_app_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_type BotServiceAzureBot#microsoft_app_type}.
        :param streaming_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#streaming_endpoint_enabled BotServiceAzureBot#streaming_endpoint_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#tags BotServiceAzureBot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#timeouts BotServiceAzureBot#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = BotServiceAzureBotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BotServiceAzureBotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument microsoft_app_id", value=microsoft_app_id, expected_type=type_hints["microsoft_app_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument developer_app_insights_api_key", value=developer_app_insights_api_key, expected_type=type_hints["developer_app_insights_api_key"])
            check_type(argname="argument developer_app_insights_application_id", value=developer_app_insights_application_id, expected_type=type_hints["developer_app_insights_application_id"])
            check_type(argname="argument developer_app_insights_key", value=developer_app_insights_key, expected_type=type_hints["developer_app_insights_key"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument luis_app_ids", value=luis_app_ids, expected_type=type_hints["luis_app_ids"])
            check_type(argname="argument luis_key", value=luis_key, expected_type=type_hints["luis_key"])
            check_type(argname="argument microsoft_app_msi_id", value=microsoft_app_msi_id, expected_type=type_hints["microsoft_app_msi_id"])
            check_type(argname="argument microsoft_app_tenant_id", value=microsoft_app_tenant_id, expected_type=type_hints["microsoft_app_tenant_id"])
            check_type(argname="argument microsoft_app_type", value=microsoft_app_type, expected_type=type_hints["microsoft_app_type"])
            check_type(argname="argument streaming_endpoint_enabled", value=streaming_endpoint_enabled, expected_type=type_hints["streaming_endpoint_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "microsoft_app_id": microsoft_app_id,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if developer_app_insights_api_key is not None:
            self._values["developer_app_insights_api_key"] = developer_app_insights_api_key
        if developer_app_insights_application_id is not None:
            self._values["developer_app_insights_application_id"] = developer_app_insights_application_id
        if developer_app_insights_key is not None:
            self._values["developer_app_insights_key"] = developer_app_insights_key
        if display_name is not None:
            self._values["display_name"] = display_name
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if id is not None:
            self._values["id"] = id
        if luis_app_ids is not None:
            self._values["luis_app_ids"] = luis_app_ids
        if luis_key is not None:
            self._values["luis_key"] = luis_key
        if microsoft_app_msi_id is not None:
            self._values["microsoft_app_msi_id"] = microsoft_app_msi_id
        if microsoft_app_tenant_id is not None:
            self._values["microsoft_app_tenant_id"] = microsoft_app_tenant_id
        if microsoft_app_type is not None:
            self._values["microsoft_app_type"] = microsoft_app_type
        if streaming_endpoint_enabled is not None:
            self._values["streaming_endpoint_enabled"] = streaming_endpoint_enabled
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#location BotServiceAzureBot#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def microsoft_app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_id BotServiceAzureBot#microsoft_app_id}.'''
        result = self._values.get("microsoft_app_id")
        assert result is not None, "Required property 'microsoft_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#name BotServiceAzureBot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#resource_group_name BotServiceAzureBot#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#sku BotServiceAzureBot#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def developer_app_insights_api_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_api_key BotServiceAzureBot#developer_app_insights_api_key}.'''
        result = self._values.get("developer_app_insights_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def developer_app_insights_application_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_application_id BotServiceAzureBot#developer_app_insights_application_id}.'''
        result = self._values.get("developer_app_insights_application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def developer_app_insights_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#developer_app_insights_key BotServiceAzureBot#developer_app_insights_key}.'''
        result = self._values.get("developer_app_insights_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#display_name BotServiceAzureBot#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#endpoint BotServiceAzureBot#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#id BotServiceAzureBot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def luis_app_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_app_ids BotServiceAzureBot#luis_app_ids}.'''
        result = self._values.get("luis_app_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def luis_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#luis_key BotServiceAzureBot#luis_key}.'''
        result = self._values.get("luis_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_app_msi_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_msi_id BotServiceAzureBot#microsoft_app_msi_id}.'''
        result = self._values.get("microsoft_app_msi_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_app_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_tenant_id BotServiceAzureBot#microsoft_app_tenant_id}.'''
        result = self._values.get("microsoft_app_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_app_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#microsoft_app_type BotServiceAzureBot#microsoft_app_type}.'''
        result = self._values.get("microsoft_app_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def streaming_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#streaming_endpoint_enabled BotServiceAzureBot#streaming_endpoint_enabled}.'''
        result = self._values.get("streaming_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#tags BotServiceAzureBot#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BotServiceAzureBotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#timeouts BotServiceAzureBot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BotServiceAzureBotTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BotServiceAzureBotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.botServiceAzureBot.BotServiceAzureBotTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class BotServiceAzureBotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#create BotServiceAzureBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#delete BotServiceAzureBot#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#read BotServiceAzureBot#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#update BotServiceAzureBot#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BotServiceAzureBotTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#create BotServiceAzureBot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#delete BotServiceAzureBot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#read BotServiceAzureBot#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/bot_service_azure_bot#update BotServiceAzureBot#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BotServiceAzureBotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BotServiceAzureBotTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.botServiceAzureBot.BotServiceAzureBotTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(BotServiceAzureBotTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBotTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBotTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBotTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBotTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BotServiceAzureBotTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BotServiceAzureBotTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BotServiceAzureBotTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BotServiceAzureBotTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BotServiceAzureBot",
    "BotServiceAzureBotConfig",
    "BotServiceAzureBotTimeouts",
    "BotServiceAzureBotTimeoutsOutputReference",
]

publication.publish()
