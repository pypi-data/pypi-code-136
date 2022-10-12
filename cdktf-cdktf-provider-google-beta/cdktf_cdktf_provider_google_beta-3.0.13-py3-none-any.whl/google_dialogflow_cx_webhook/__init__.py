'''
# `google_dialogflow_cx_webhook`

Refer to the Terraform Registory for docs: [`google_dialogflow_cx_webhook`](https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook).
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


class GoogleDialogflowCxWebhook(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook google_dialogflow_cx_webhook}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_spell_correction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_stackdriver_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        generic_web_service: typing.Optional[typing.Union["GoogleDialogflowCxWebhookGenericWebService", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        security_settings: typing.Optional[builtins.str] = None,
        service_directory: typing.Optional[typing.Union["GoogleDialogflowCxWebhookServiceDirectory", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxWebhookTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook google_dialogflow_cx_webhook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The human-readable name of the webhook, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#display_name GoogleDialogflowCxWebhook#display_name}
        :param disabled: Indicates whether the webhook is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#disabled GoogleDialogflowCxWebhook#disabled}
        :param enable_spell_correction: Indicates if automatic spell correction is enabled in detect intent requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_spell_correction GoogleDialogflowCxWebhook#enable_spell_correction}
        :param enable_stackdriver_logging: Determines whether this agent should log conversation queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_stackdriver_logging GoogleDialogflowCxWebhook#enable_stackdriver_logging}
        :param generic_web_service: generic_web_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#id GoogleDialogflowCxWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent: The agent to create a webhook for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#parent GoogleDialogflowCxWebhook#parent}
        :param security_settings: Name of the SecuritySettings reference for the agent. Format: projects//locations//securitySettings/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#security_settings GoogleDialogflowCxWebhook#security_settings}
        :param service_directory: service_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service_directory GoogleDialogflowCxWebhook#service_directory}
        :param timeout: Webhook execution timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeout GoogleDialogflowCxWebhook#timeout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeouts GoogleDialogflowCxWebhook#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhook.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDialogflowCxWebhookConfig(
            display_name=display_name,
            disabled=disabled,
            enable_spell_correction=enable_spell_correction,
            enable_stackdriver_logging=enable_stackdriver_logging,
            generic_web_service=generic_web_service,
            id=id,
            parent=parent,
            security_settings=security_settings,
            service_directory=service_directory,
            timeout=timeout,
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

    @jsii.member(jsii_name="putGenericWebService")
    def put_generic_web_service(
        self,
        *,
        uri: builtins.str,
        allowed_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param uri: Whether to use speech adaptation for speech recognition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        :param allowed_ca_certs: Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        :param request_headers: The HTTP request headers to send together with webhook requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        value = GoogleDialogflowCxWebhookGenericWebService(
            uri=uri, allowed_ca_certs=allowed_ca_certs, request_headers=request_headers
        )

        return typing.cast(None, jsii.invoke(self, "putGenericWebService", [value]))

    @jsii.member(jsii_name="putServiceDirectory")
    def put_service_directory(
        self,
        *,
        generic_web_service: typing.Union["GoogleDialogflowCxWebhookServiceDirectoryGenericWebService", typing.Dict[str, typing.Any]],
        service: builtins.str,
    ) -> None:
        '''
        :param generic_web_service: generic_web_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        :param service: The name of Service Directory service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service GoogleDialogflowCxWebhook#service}
        '''
        value = GoogleDialogflowCxWebhookServiceDirectory(
            generic_web_service=generic_web_service, service=service
        )

        return typing.cast(None, jsii.invoke(self, "putServiceDirectory", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#create GoogleDialogflowCxWebhook#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#delete GoogleDialogflowCxWebhook#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#update GoogleDialogflowCxWebhook#update}.
        '''
        value = GoogleDialogflowCxWebhookTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnableSpellCorrection")
    def reset_enable_spell_correction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSpellCorrection", []))

    @jsii.member(jsii_name="resetEnableStackdriverLogging")
    def reset_enable_stackdriver_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableStackdriverLogging", []))

    @jsii.member(jsii_name="resetGenericWebService")
    def reset_generic_web_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenericWebService", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetSecuritySettings")
    def reset_security_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecuritySettings", []))

    @jsii.member(jsii_name="resetServiceDirectory")
    def reset_service_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDirectory", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

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
    @jsii.member(jsii_name="genericWebService")
    def generic_web_service(
        self,
    ) -> "GoogleDialogflowCxWebhookGenericWebServiceOutputReference":
        return typing.cast("GoogleDialogflowCxWebhookGenericWebServiceOutputReference", jsii.get(self, "genericWebService"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="serviceDirectory")
    def service_directory(
        self,
    ) -> "GoogleDialogflowCxWebhookServiceDirectoryOutputReference":
        return typing.cast("GoogleDialogflowCxWebhookServiceDirectoryOutputReference", jsii.get(self, "serviceDirectory"))

    @builtins.property
    @jsii.member(jsii_name="startFlow")
    def start_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startFlow"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDialogflowCxWebhookTimeoutsOutputReference":
        return typing.cast("GoogleDialogflowCxWebhookTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSpellCorrectionInput")
    def enable_spell_correction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSpellCorrectionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverLoggingInput")
    def enable_stackdriver_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableStackdriverLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="genericWebServiceInput")
    def generic_web_service_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxWebhookGenericWebService"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxWebhookGenericWebService"], jsii.get(self, "genericWebServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="securitySettingsInput")
    def security_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securitySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDirectoryInput")
    def service_directory_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxWebhookServiceDirectory"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxWebhookServiceDirectory"], jsii.get(self, "serviceDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDialogflowCxWebhookTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDialogflowCxWebhookTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enableSpellCorrection")
    def enable_spell_correction(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSpellCorrection"))

    @enable_spell_correction.setter
    def enable_spell_correction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "enable_spell_correction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSpellCorrection", value)

    @builtins.property
    @jsii.member(jsii_name="enableStackdriverLogging")
    def enable_stackdriver_logging(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableStackdriverLogging"))

    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "enable_stackdriver_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStackdriverLogging", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="securitySettings")
    def security_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securitySettings"))

    @security_settings.setter
    def security_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "security_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securitySettings", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhook, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookConfig",
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
        "disabled": "disabled",
        "enable_spell_correction": "enableSpellCorrection",
        "enable_stackdriver_logging": "enableStackdriverLogging",
        "generic_web_service": "genericWebService",
        "id": "id",
        "parent": "parent",
        "security_settings": "securitySettings",
        "service_directory": "serviceDirectory",
        "timeout": "timeout",
        "timeouts": "timeouts",
    },
)
class GoogleDialogflowCxWebhookConfig(cdktf.TerraformMetaArguments):
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
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_spell_correction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_stackdriver_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        generic_web_service: typing.Optional[typing.Union["GoogleDialogflowCxWebhookGenericWebService", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        security_settings: typing.Optional[builtins.str] = None,
        service_directory: typing.Optional[typing.Union["GoogleDialogflowCxWebhookServiceDirectory", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxWebhookTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The human-readable name of the webhook, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#display_name GoogleDialogflowCxWebhook#display_name}
        :param disabled: Indicates whether the webhook is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#disabled GoogleDialogflowCxWebhook#disabled}
        :param enable_spell_correction: Indicates if automatic spell correction is enabled in detect intent requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_spell_correction GoogleDialogflowCxWebhook#enable_spell_correction}
        :param enable_stackdriver_logging: Determines whether this agent should log conversation queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_stackdriver_logging GoogleDialogflowCxWebhook#enable_stackdriver_logging}
        :param generic_web_service: generic_web_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#id GoogleDialogflowCxWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent: The agent to create a webhook for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#parent GoogleDialogflowCxWebhook#parent}
        :param security_settings: Name of the SecuritySettings reference for the agent. Format: projects//locations//securitySettings/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#security_settings GoogleDialogflowCxWebhook#security_settings}
        :param service_directory: service_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service_directory GoogleDialogflowCxWebhook#service_directory}
        :param timeout: Webhook execution timeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeout GoogleDialogflowCxWebhook#timeout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeouts GoogleDialogflowCxWebhook#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(generic_web_service, dict):
            generic_web_service = GoogleDialogflowCxWebhookGenericWebService(**generic_web_service)
        if isinstance(service_directory, dict):
            service_directory = GoogleDialogflowCxWebhookServiceDirectory(**service_directory)
        if isinstance(timeouts, dict):
            timeouts = GoogleDialogflowCxWebhookTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument enable_spell_correction", value=enable_spell_correction, expected_type=type_hints["enable_spell_correction"])
            check_type(argname="argument enable_stackdriver_logging", value=enable_stackdriver_logging, expected_type=type_hints["enable_stackdriver_logging"])
            check_type(argname="argument generic_web_service", value=generic_web_service, expected_type=type_hints["generic_web_service"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument security_settings", value=security_settings, expected_type=type_hints["security_settings"])
            check_type(argname="argument service_directory", value=service_directory, expected_type=type_hints["service_directory"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if disabled is not None:
            self._values["disabled"] = disabled
        if enable_spell_correction is not None:
            self._values["enable_spell_correction"] = enable_spell_correction
        if enable_stackdriver_logging is not None:
            self._values["enable_stackdriver_logging"] = enable_stackdriver_logging
        if generic_web_service is not None:
            self._values["generic_web_service"] = generic_web_service
        if id is not None:
            self._values["id"] = id
        if parent is not None:
            self._values["parent"] = parent
        if security_settings is not None:
            self._values["security_settings"] = security_settings
        if service_directory is not None:
            self._values["service_directory"] = service_directory
        if timeout is not None:
            self._values["timeout"] = timeout
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
    def display_name(self) -> builtins.str:
        '''The human-readable name of the webhook, unique within the agent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#display_name GoogleDialogflowCxWebhook#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the webhook is disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#disabled GoogleDialogflowCxWebhook#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_spell_correction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if automatic spell correction is enabled in detect intent requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_spell_correction GoogleDialogflowCxWebhook#enable_spell_correction}
        '''
        result = self._values.get("enable_spell_correction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_stackdriver_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether this agent should log conversation queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#enable_stackdriver_logging GoogleDialogflowCxWebhook#enable_stackdriver_logging}
        '''
        result = self._values.get("enable_stackdriver_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def generic_web_service(
        self,
    ) -> typing.Optional["GoogleDialogflowCxWebhookGenericWebService"]:
        '''generic_web_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        '''
        result = self._values.get("generic_web_service")
        return typing.cast(typing.Optional["GoogleDialogflowCxWebhookGenericWebService"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#id GoogleDialogflowCxWebhook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''The agent to create a webhook for. Format: projects//locations//agents/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#parent GoogleDialogflowCxWebhook#parent}
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_settings(self) -> typing.Optional[builtins.str]:
        '''Name of the SecuritySettings reference for the agent. Format: projects//locations//securitySettings/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#security_settings GoogleDialogflowCxWebhook#security_settings}
        '''
        result = self._values.get("security_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_directory(
        self,
    ) -> typing.Optional["GoogleDialogflowCxWebhookServiceDirectory"]:
        '''service_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service_directory GoogleDialogflowCxWebhook#service_directory}
        '''
        result = self._values.get("service_directory")
        return typing.cast(typing.Optional["GoogleDialogflowCxWebhookServiceDirectory"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Webhook execution timeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeout GoogleDialogflowCxWebhook#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDialogflowCxWebhookTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#timeouts GoogleDialogflowCxWebhook#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDialogflowCxWebhookTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxWebhookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookGenericWebService",
    jsii_struct_bases=[],
    name_mapping={
        "uri": "uri",
        "allowed_ca_certs": "allowedCaCerts",
        "request_headers": "requestHeaders",
    },
)
class GoogleDialogflowCxWebhookGenericWebService:
    def __init__(
        self,
        *,
        uri: builtins.str,
        allowed_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param uri: Whether to use speech adaptation for speech recognition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        :param allowed_ca_certs: Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        :param request_headers: The HTTP request headers to send together with webhook requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookGenericWebService.__init__)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument allowed_ca_certs", value=allowed_ca_certs, expected_type=type_hints["allowed_ca_certs"])
            check_type(argname="argument request_headers", value=request_headers, expected_type=type_hints["request_headers"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }
        if allowed_ca_certs is not None:
            self._values["allowed_ca_certs"] = allowed_ca_certs
        if request_headers is not None:
            self._values["request_headers"] = request_headers

    @builtins.property
    def uri(self) -> builtins.str:
        '''Whether to use speech adaptation for speech recognition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_ca_certs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        '''
        result = self._values.get("allowed_ca_certs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def request_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The HTTP request headers to send together with webhook requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        result = self._values.get("request_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxWebhookGenericWebService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxWebhookGenericWebServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookGenericWebServiceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookGenericWebServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedCaCerts")
    def reset_allowed_ca_certs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCaCerts", []))

    @jsii.member(jsii_name="resetRequestHeaders")
    def reset_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="allowedCaCertsInput")
    def allowed_ca_certs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCaCertsInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersInput")
    def request_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCaCerts")
    def allowed_ca_certs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCaCerts"))

    @allowed_ca_certs.setter
    def allowed_ca_certs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookGenericWebServiceOutputReference, "allowed_ca_certs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCaCerts", value)

    @builtins.property
    @jsii.member(jsii_name="requestHeaders")
    def request_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestHeaders"))

    @request_headers.setter
    def request_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookGenericWebServiceOutputReference, "request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookGenericWebServiceOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxWebhookGenericWebService]:
        return typing.cast(typing.Optional[GoogleDialogflowCxWebhookGenericWebService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxWebhookGenericWebService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookGenericWebServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookServiceDirectory",
    jsii_struct_bases=[],
    name_mapping={"generic_web_service": "genericWebService", "service": "service"},
)
class GoogleDialogflowCxWebhookServiceDirectory:
    def __init__(
        self,
        *,
        generic_web_service: typing.Union["GoogleDialogflowCxWebhookServiceDirectoryGenericWebService", typing.Dict[str, typing.Any]],
        service: builtins.str,
    ) -> None:
        '''
        :param generic_web_service: generic_web_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        :param service: The name of Service Directory service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service GoogleDialogflowCxWebhook#service}
        '''
        if isinstance(generic_web_service, dict):
            generic_web_service = GoogleDialogflowCxWebhookServiceDirectoryGenericWebService(**generic_web_service)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookServiceDirectory.__init__)
            check_type(argname="argument generic_web_service", value=generic_web_service, expected_type=type_hints["generic_web_service"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[str, typing.Any] = {
            "generic_web_service": generic_web_service,
            "service": service,
        }

    @builtins.property
    def generic_web_service(
        self,
    ) -> "GoogleDialogflowCxWebhookServiceDirectoryGenericWebService":
        '''generic_web_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#generic_web_service GoogleDialogflowCxWebhook#generic_web_service}
        '''
        result = self._values.get("generic_web_service")
        assert result is not None, "Required property 'generic_web_service' is missing"
        return typing.cast("GoogleDialogflowCxWebhookServiceDirectoryGenericWebService", result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The name of Service Directory service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#service GoogleDialogflowCxWebhook#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxWebhookServiceDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookServiceDirectoryGenericWebService",
    jsii_struct_bases=[],
    name_mapping={
        "uri": "uri",
        "allowed_ca_certs": "allowedCaCerts",
        "request_headers": "requestHeaders",
    },
)
class GoogleDialogflowCxWebhookServiceDirectoryGenericWebService:
    def __init__(
        self,
        *,
        uri: builtins.str,
        allowed_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param uri: Whether to use speech adaptation for speech recognition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        :param allowed_ca_certs: Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        :param request_headers: The HTTP request headers to send together with webhook requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookServiceDirectoryGenericWebService.__init__)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument allowed_ca_certs", value=allowed_ca_certs, expected_type=type_hints["allowed_ca_certs"])
            check_type(argname="argument request_headers", value=request_headers, expected_type=type_hints["request_headers"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }
        if allowed_ca_certs is not None:
            self._values["allowed_ca_certs"] = allowed_ca_certs
        if request_headers is not None:
            self._values["request_headers"] = request_headers

    @builtins.property
    def uri(self) -> builtins.str:
        '''Whether to use speech adaptation for speech recognition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_ca_certs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        '''
        result = self._values.get("allowed_ca_certs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def request_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The HTTP request headers to send together with webhook requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        result = self._values.get("request_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxWebhookServiceDirectoryGenericWebService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedCaCerts")
    def reset_allowed_ca_certs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCaCerts", []))

    @jsii.member(jsii_name="resetRequestHeaders")
    def reset_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="allowedCaCertsInput")
    def allowed_ca_certs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCaCertsInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersInput")
    def request_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCaCerts")
    def allowed_ca_certs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCaCerts"))

    @allowed_ca_certs.setter
    def allowed_ca_certs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference, "allowed_ca_certs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCaCerts", value)

    @builtins.property
    @jsii.member(jsii_name="requestHeaders")
    def request_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestHeaders"))

    @request_headers.setter
    def request_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference, "request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxWebhookServiceDirectoryGenericWebService]:
        return typing.cast(typing.Optional[GoogleDialogflowCxWebhookServiceDirectoryGenericWebService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxWebhookServiceDirectoryGenericWebService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxWebhookServiceDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookServiceDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookServiceDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGenericWebService")
    def put_generic_web_service(
        self,
        *,
        uri: builtins.str,
        allowed_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param uri: Whether to use speech adaptation for speech recognition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#uri GoogleDialogflowCxWebhook#uri}
        :param allowed_ca_certs: Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#allowed_ca_certs GoogleDialogflowCxWebhook#allowed_ca_certs}
        :param request_headers: The HTTP request headers to send together with webhook requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#request_headers GoogleDialogflowCxWebhook#request_headers}
        '''
        value = GoogleDialogflowCxWebhookServiceDirectoryGenericWebService(
            uri=uri, allowed_ca_certs=allowed_ca_certs, request_headers=request_headers
        )

        return typing.cast(None, jsii.invoke(self, "putGenericWebService", [value]))

    @builtins.property
    @jsii.member(jsii_name="genericWebService")
    def generic_web_service(
        self,
    ) -> GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference:
        return typing.cast(GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference, jsii.get(self, "genericWebService"))

    @builtins.property
    @jsii.member(jsii_name="genericWebServiceInput")
    def generic_web_service_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxWebhookServiceDirectoryGenericWebService]:
        return typing.cast(typing.Optional[GoogleDialogflowCxWebhookServiceDirectoryGenericWebService], jsii.get(self, "genericWebServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxWebhookServiceDirectory]:
        return typing.cast(typing.Optional[GoogleDialogflowCxWebhookServiceDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxWebhookServiceDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookServiceDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDialogflowCxWebhookTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#create GoogleDialogflowCxWebhook#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#delete GoogleDialogflowCxWebhook#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#update GoogleDialogflowCxWebhook#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#create GoogleDialogflowCxWebhook#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#delete GoogleDialogflowCxWebhook#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_webhook#update GoogleDialogflowCxWebhook#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxWebhookTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxWebhookTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxWebhook.GoogleDialogflowCxWebhookTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxWebhookTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxWebhookTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxWebhookTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxWebhookTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxWebhookTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDialogflowCxWebhook",
    "GoogleDialogflowCxWebhookConfig",
    "GoogleDialogflowCxWebhookGenericWebService",
    "GoogleDialogflowCxWebhookGenericWebServiceOutputReference",
    "GoogleDialogflowCxWebhookServiceDirectory",
    "GoogleDialogflowCxWebhookServiceDirectoryGenericWebService",
    "GoogleDialogflowCxWebhookServiceDirectoryGenericWebServiceOutputReference",
    "GoogleDialogflowCxWebhookServiceDirectoryOutputReference",
    "GoogleDialogflowCxWebhookTimeouts",
    "GoogleDialogflowCxWebhookTimeoutsOutputReference",
]

publication.publish()
