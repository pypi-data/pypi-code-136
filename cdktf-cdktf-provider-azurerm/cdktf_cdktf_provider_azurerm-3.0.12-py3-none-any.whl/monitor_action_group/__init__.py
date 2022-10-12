'''
# `azurerm_monitor_action_group`

Refer to the Terraform Registory for docs: [`azurerm_monitor_action_group`](https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group).
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


class MonitorActionGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group azurerm_monitor_action_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
        short_name: builtins.str,
        arm_role_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupArmRoleReceiver", typing.Dict[str, typing.Any]]]]] = None,
        automation_runbook_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAutomationRunbookReceiver", typing.Dict[str, typing.Any]]]]] = None,
        azure_app_push_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAzureAppPushReceiver", typing.Dict[str, typing.Any]]]]] = None,
        azure_function_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAzureFunctionReceiver", typing.Dict[str, typing.Any]]]]] = None,
        email_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEmailReceiver", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event_hub_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEventHubReceiver", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        itsm_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupItsmReceiver", typing.Dict[str, typing.Any]]]]] = None,
        logic_app_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupLogicAppReceiver", typing.Dict[str, typing.Any]]]]] = None,
        sms_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupSmsReceiver", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorActionGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        voice_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupVoiceReceiver", typing.Dict[str, typing.Any]]]]] = None,
        webhook_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupWebhookReceiver", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group azurerm_monitor_action_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#resource_group_name MonitorActionGroup#resource_group_name}.
        :param short_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#short_name MonitorActionGroup#short_name}.
        :param arm_role_receiver: arm_role_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#arm_role_receiver MonitorActionGroup#arm_role_receiver}
        :param automation_runbook_receiver: automation_runbook_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#automation_runbook_receiver MonitorActionGroup#automation_runbook_receiver}
        :param azure_app_push_receiver: azure_app_push_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_app_push_receiver MonitorActionGroup#azure_app_push_receiver}
        :param azure_function_receiver: azure_function_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_function_receiver MonitorActionGroup#azure_function_receiver}
        :param email_receiver: email_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_receiver MonitorActionGroup#email_receiver}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#enabled MonitorActionGroup#enabled}.
        :param event_hub_receiver: event_hub_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_receiver MonitorActionGroup#event_hub_receiver}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#id MonitorActionGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param itsm_receiver: itsm_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#itsm_receiver MonitorActionGroup#itsm_receiver}
        :param logic_app_receiver: logic_app_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#logic_app_receiver MonitorActionGroup#logic_app_receiver}
        :param sms_receiver: sms_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#sms_receiver MonitorActionGroup#sms_receiver}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tags MonitorActionGroup#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#timeouts MonitorActionGroup#timeouts}
        :param voice_receiver: voice_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#voice_receiver MonitorActionGroup#voice_receiver}
        :param webhook_receiver: webhook_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#webhook_receiver MonitorActionGroup#webhook_receiver}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorActionGroupConfig(
            name=name,
            resource_group_name=resource_group_name,
            short_name=short_name,
            arm_role_receiver=arm_role_receiver,
            automation_runbook_receiver=automation_runbook_receiver,
            azure_app_push_receiver=azure_app_push_receiver,
            azure_function_receiver=azure_function_receiver,
            email_receiver=email_receiver,
            enabled=enabled,
            event_hub_receiver=event_hub_receiver,
            id=id,
            itsm_receiver=itsm_receiver,
            logic_app_receiver=logic_app_receiver,
            sms_receiver=sms_receiver,
            tags=tags,
            timeouts=timeouts,
            voice_receiver=voice_receiver,
            webhook_receiver=webhook_receiver,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArmRoleReceiver")
    def put_arm_role_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupArmRoleReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_arm_role_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArmRoleReceiver", [value]))

    @jsii.member(jsii_name="putAutomationRunbookReceiver")
    def put_automation_runbook_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAutomationRunbookReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_automation_runbook_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutomationRunbookReceiver", [value]))

    @jsii.member(jsii_name="putAzureAppPushReceiver")
    def put_azure_app_push_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAzureAppPushReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_azure_app_push_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzureAppPushReceiver", [value]))

    @jsii.member(jsii_name="putAzureFunctionReceiver")
    def put_azure_function_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupAzureFunctionReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_azure_function_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzureFunctionReceiver", [value]))

    @jsii.member(jsii_name="putEmailReceiver")
    def put_email_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEmailReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_email_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmailReceiver", [value]))

    @jsii.member(jsii_name="putEventHubReceiver")
    def put_event_hub_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEventHubReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_event_hub_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventHubReceiver", [value]))

    @jsii.member(jsii_name="putItsmReceiver")
    def put_itsm_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupItsmReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_itsm_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItsmReceiver", [value]))

    @jsii.member(jsii_name="putLogicAppReceiver")
    def put_logic_app_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupLogicAppReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_logic_app_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogicAppReceiver", [value]))

    @jsii.member(jsii_name="putSmsReceiver")
    def put_sms_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupSmsReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_sms_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSmsReceiver", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#create MonitorActionGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#delete MonitorActionGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#read MonitorActionGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#update MonitorActionGroup#update}.
        '''
        value = MonitorActionGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVoiceReceiver")
    def put_voice_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupVoiceReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_voice_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVoiceReceiver", [value]))

    @jsii.member(jsii_name="putWebhookReceiver")
    def put_webhook_receiver(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupWebhookReceiver", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroup.put_webhook_receiver)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhookReceiver", [value]))

    @jsii.member(jsii_name="resetArmRoleReceiver")
    def reset_arm_role_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArmRoleReceiver", []))

    @jsii.member(jsii_name="resetAutomationRunbookReceiver")
    def reset_automation_runbook_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationRunbookReceiver", []))

    @jsii.member(jsii_name="resetAzureAppPushReceiver")
    def reset_azure_app_push_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAppPushReceiver", []))

    @jsii.member(jsii_name="resetAzureFunctionReceiver")
    def reset_azure_function_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFunctionReceiver", []))

    @jsii.member(jsii_name="resetEmailReceiver")
    def reset_email_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailReceiver", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEventHubReceiver")
    def reset_event_hub_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHubReceiver", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetItsmReceiver")
    def reset_itsm_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItsmReceiver", []))

    @jsii.member(jsii_name="resetLogicAppReceiver")
    def reset_logic_app_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogicAppReceiver", []))

    @jsii.member(jsii_name="resetSmsReceiver")
    def reset_sms_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsReceiver", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVoiceReceiver")
    def reset_voice_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVoiceReceiver", []))

    @jsii.member(jsii_name="resetWebhookReceiver")
    def reset_webhook_receiver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhookReceiver", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="armRoleReceiver")
    def arm_role_receiver(self) -> "MonitorActionGroupArmRoleReceiverList":
        return typing.cast("MonitorActionGroupArmRoleReceiverList", jsii.get(self, "armRoleReceiver"))

    @builtins.property
    @jsii.member(jsii_name="automationRunbookReceiver")
    def automation_runbook_receiver(
        self,
    ) -> "MonitorActionGroupAutomationRunbookReceiverList":
        return typing.cast("MonitorActionGroupAutomationRunbookReceiverList", jsii.get(self, "automationRunbookReceiver"))

    @builtins.property
    @jsii.member(jsii_name="azureAppPushReceiver")
    def azure_app_push_receiver(self) -> "MonitorActionGroupAzureAppPushReceiverList":
        return typing.cast("MonitorActionGroupAzureAppPushReceiverList", jsii.get(self, "azureAppPushReceiver"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionReceiver")
    def azure_function_receiver(self) -> "MonitorActionGroupAzureFunctionReceiverList":
        return typing.cast("MonitorActionGroupAzureFunctionReceiverList", jsii.get(self, "azureFunctionReceiver"))

    @builtins.property
    @jsii.member(jsii_name="emailReceiver")
    def email_receiver(self) -> "MonitorActionGroupEmailReceiverList":
        return typing.cast("MonitorActionGroupEmailReceiverList", jsii.get(self, "emailReceiver"))

    @builtins.property
    @jsii.member(jsii_name="eventHubReceiver")
    def event_hub_receiver(self) -> "MonitorActionGroupEventHubReceiverList":
        return typing.cast("MonitorActionGroupEventHubReceiverList", jsii.get(self, "eventHubReceiver"))

    @builtins.property
    @jsii.member(jsii_name="itsmReceiver")
    def itsm_receiver(self) -> "MonitorActionGroupItsmReceiverList":
        return typing.cast("MonitorActionGroupItsmReceiverList", jsii.get(self, "itsmReceiver"))

    @builtins.property
    @jsii.member(jsii_name="logicAppReceiver")
    def logic_app_receiver(self) -> "MonitorActionGroupLogicAppReceiverList":
        return typing.cast("MonitorActionGroupLogicAppReceiverList", jsii.get(self, "logicAppReceiver"))

    @builtins.property
    @jsii.member(jsii_name="smsReceiver")
    def sms_receiver(self) -> "MonitorActionGroupSmsReceiverList":
        return typing.cast("MonitorActionGroupSmsReceiverList", jsii.get(self, "smsReceiver"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorActionGroupTimeoutsOutputReference":
        return typing.cast("MonitorActionGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="voiceReceiver")
    def voice_receiver(self) -> "MonitorActionGroupVoiceReceiverList":
        return typing.cast("MonitorActionGroupVoiceReceiverList", jsii.get(self, "voiceReceiver"))

    @builtins.property
    @jsii.member(jsii_name="webhookReceiver")
    def webhook_receiver(self) -> "MonitorActionGroupWebhookReceiverList":
        return typing.cast("MonitorActionGroupWebhookReceiverList", jsii.get(self, "webhookReceiver"))

    @builtins.property
    @jsii.member(jsii_name="armRoleReceiverInput")
    def arm_role_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupArmRoleReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupArmRoleReceiver"]]], jsii.get(self, "armRoleReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="automationRunbookReceiverInput")
    def automation_runbook_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAutomationRunbookReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAutomationRunbookReceiver"]]], jsii.get(self, "automationRunbookReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAppPushReceiverInput")
    def azure_app_push_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAzureAppPushReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAzureAppPushReceiver"]]], jsii.get(self, "azureAppPushReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionReceiverInput")
    def azure_function_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAzureFunctionReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupAzureFunctionReceiver"]]], jsii.get(self, "azureFunctionReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="emailReceiverInput")
    def email_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEmailReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEmailReceiver"]]], jsii.get(self, "emailReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHubReceiverInput")
    def event_hub_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEventHubReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEventHubReceiver"]]], jsii.get(self, "eventHubReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="itsmReceiverInput")
    def itsm_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupItsmReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupItsmReceiver"]]], jsii.get(self, "itsmReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="logicAppReceiverInput")
    def logic_app_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupLogicAppReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupLogicAppReceiver"]]], jsii.get(self, "logicAppReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="shortNameInput")
    def short_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortNameInput"))

    @builtins.property
    @jsii.member(jsii_name="smsReceiverInput")
    def sms_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupSmsReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupSmsReceiver"]]], jsii.get(self, "smsReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorActionGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorActionGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="voiceReceiverInput")
    def voice_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupVoiceReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupVoiceReceiver"]]], jsii.get(self, "voiceReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookReceiverInput")
    def webhook_receiver_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupWebhookReceiver"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupWebhookReceiver"]]], jsii.get(self, "webhookReceiverInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "short_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupArmRoleReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_id": "roleId",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupArmRoleReceiver:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_id: builtins.str,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param role_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#role_id MonitorActionGroup#role_id}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupArmRoleReceiver.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "role_id": role_id,
        }
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#role_id MonitorActionGroup#role_id}.'''
        result = self._values.get("role_id")
        assert result is not None, "Required property 'role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupArmRoleReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupArmRoleReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupArmRoleReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupArmRoleReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupArmRoleReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupArmRoleReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupArmRoleReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupArmRoleReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupArmRoleReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupArmRoleReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupArmRoleReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupArmRoleReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupArmRoleReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleIdInput")
    def role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @role_id.setter
    def role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverOutputReference, "role_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleId", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupArmRoleReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupArmRoleReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupArmRoleReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupArmRoleReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAutomationRunbookReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "automation_account_id": "automationAccountId",
        "is_global_runbook": "isGlobalRunbook",
        "name": "name",
        "runbook_name": "runbookName",
        "service_uri": "serviceUri",
        "webhook_resource_id": "webhookResourceId",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupAutomationRunbookReceiver:
    def __init__(
        self,
        *,
        automation_account_id: builtins.str,
        is_global_runbook: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        runbook_name: builtins.str,
        service_uri: builtins.str,
        webhook_resource_id: builtins.str,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param automation_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#automation_account_id MonitorActionGroup#automation_account_id}.
        :param is_global_runbook: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#is_global_runbook MonitorActionGroup#is_global_runbook}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param runbook_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#runbook_name MonitorActionGroup#runbook_name}.
        :param service_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#service_uri MonitorActionGroup#service_uri}.
        :param webhook_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#webhook_resource_id MonitorActionGroup#webhook_resource_id}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAutomationRunbookReceiver.__init__)
            check_type(argname="argument automation_account_id", value=automation_account_id, expected_type=type_hints["automation_account_id"])
            check_type(argname="argument is_global_runbook", value=is_global_runbook, expected_type=type_hints["is_global_runbook"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runbook_name", value=runbook_name, expected_type=type_hints["runbook_name"])
            check_type(argname="argument service_uri", value=service_uri, expected_type=type_hints["service_uri"])
            check_type(argname="argument webhook_resource_id", value=webhook_resource_id, expected_type=type_hints["webhook_resource_id"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "automation_account_id": automation_account_id,
            "is_global_runbook": is_global_runbook,
            "name": name,
            "runbook_name": runbook_name,
            "service_uri": service_uri,
            "webhook_resource_id": webhook_resource_id,
        }
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def automation_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#automation_account_id MonitorActionGroup#automation_account_id}.'''
        result = self._values.get("automation_account_id")
        assert result is not None, "Required property 'automation_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_global_runbook(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#is_global_runbook MonitorActionGroup#is_global_runbook}.'''
        result = self._values.get("is_global_runbook")
        assert result is not None, "Required property 'is_global_runbook' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runbook_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#runbook_name MonitorActionGroup#runbook_name}.'''
        result = self._values.get("runbook_name")
        assert result is not None, "Required property 'runbook_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#service_uri MonitorActionGroup#service_uri}.'''
        result = self._values.get("service_uri")
        assert result is not None, "Required property 'service_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def webhook_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#webhook_resource_id MonitorActionGroup#webhook_resource_id}.'''
        result = self._values.get("webhook_resource_id")
        assert result is not None, "Required property 'webhook_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupAutomationRunbookReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupAutomationRunbookReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAutomationRunbookReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAutomationRunbookReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupAutomationRunbookReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAutomationRunbookReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupAutomationRunbookReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAutomationRunbookReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAutomationRunbookReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAutomationRunbookReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupAutomationRunbookReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAutomationRunbookReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAutomationRunbookReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="automationAccountIdInput")
    def automation_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isGlobalRunbookInput")
    def is_global_runbook_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isGlobalRunbookInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookNameInput")
    def runbook_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceUriInput")
    def service_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookResourceIdInput")
    def webhook_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="automationAccountId")
    def automation_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automationAccountId"))

    @automation_account_id.setter
    def automation_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "automation_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automationAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="isGlobalRunbook")
    def is_global_runbook(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isGlobalRunbook"))

    @is_global_runbook.setter
    def is_global_runbook(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "is_global_runbook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isGlobalRunbook", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runbookName")
    def runbook_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookName"))

    @runbook_name.setter
    def runbook_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "runbook_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceUri")
    def service_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUri"))

    @service_uri.setter
    def service_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "service_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceUri", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="webhookResourceId")
    def webhook_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhookResourceId"))

    @webhook_resource_id.setter
    def webhook_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "webhook_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhookResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupAutomationRunbookReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupAutomationRunbookReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupAutomationRunbookReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAutomationRunbookReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureAppPushReceiver",
    jsii_struct_bases=[],
    name_mapping={"email_address": "emailAddress", "name": "name"},
)
class MonitorActionGroupAzureAppPushReceiver:
    def __init__(self, *, email_address: builtins.str, name: builtins.str) -> None:
        '''
        :param email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_address MonitorActionGroup#email_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAzureAppPushReceiver.__init__)
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "email_address": email_address,
            "name": name,
        }

    @builtins.property
    def email_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_address MonitorActionGroup#email_address}.'''
        result = self._values.get("email_address")
        assert result is not None, "Required property 'email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupAzureAppPushReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupAzureAppPushReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureAppPushReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAzureAppPushReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupAzureAppPushReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAzureAppPushReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupAzureAppPushReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureAppPushReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureAppPushReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureAppPushReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupAzureAppPushReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureAppPushReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAzureAppPushReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverOutputReference, "email_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupAzureAppPushReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupAzureAppPushReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupAzureAppPushReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureAppPushReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureFunctionReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "function_app_resource_id": "functionAppResourceId",
        "function_name": "functionName",
        "http_trigger_url": "httpTriggerUrl",
        "name": "name",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupAzureFunctionReceiver:
    def __init__(
        self,
        *,
        function_app_resource_id: builtins.str,
        function_name: builtins.str,
        http_trigger_url: builtins.str,
        name: builtins.str,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param function_app_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#function_app_resource_id MonitorActionGroup#function_app_resource_id}.
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#function_name MonitorActionGroup#function_name}.
        :param http_trigger_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#http_trigger_url MonitorActionGroup#http_trigger_url}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAzureFunctionReceiver.__init__)
            check_type(argname="argument function_app_resource_id", value=function_app_resource_id, expected_type=type_hints["function_app_resource_id"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument http_trigger_url", value=http_trigger_url, expected_type=type_hints["http_trigger_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_app_resource_id": function_app_resource_id,
            "function_name": function_name,
            "http_trigger_url": http_trigger_url,
            "name": name,
        }
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def function_app_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#function_app_resource_id MonitorActionGroup#function_app_resource_id}.'''
        result = self._values.get("function_app_resource_id")
        assert result is not None, "Required property 'function_app_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#function_name MonitorActionGroup#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_trigger_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#http_trigger_url MonitorActionGroup#http_trigger_url}.'''
        result = self._values.get("http_trigger_url")
        assert result is not None, "Required property 'http_trigger_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupAzureFunctionReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupAzureFunctionReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureFunctionReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAzureFunctionReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupAzureFunctionReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupAzureFunctionReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupAzureFunctionReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureFunctionReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureFunctionReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureFunctionReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupAzureFunctionReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupAzureFunctionReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupAzureFunctionReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="functionAppResourceIdInput")
    def function_app_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionAppResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTriggerUrlInput")
    def http_trigger_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpTriggerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="functionAppResourceId")
    def function_app_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionAppResourceId"))

    @function_app_resource_id.setter
    def function_app_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "function_app_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionAppResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "function_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="httpTriggerUrl")
    def http_trigger_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTriggerUrl"))

    @http_trigger_url.setter
    def http_trigger_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "http_trigger_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTriggerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupAzureFunctionReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupAzureFunctionReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupAzureFunctionReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupAzureFunctionReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupConfig",
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
        "resource_group_name": "resourceGroupName",
        "short_name": "shortName",
        "arm_role_receiver": "armRoleReceiver",
        "automation_runbook_receiver": "automationRunbookReceiver",
        "azure_app_push_receiver": "azureAppPushReceiver",
        "azure_function_receiver": "azureFunctionReceiver",
        "email_receiver": "emailReceiver",
        "enabled": "enabled",
        "event_hub_receiver": "eventHubReceiver",
        "id": "id",
        "itsm_receiver": "itsmReceiver",
        "logic_app_receiver": "logicAppReceiver",
        "sms_receiver": "smsReceiver",
        "tags": "tags",
        "timeouts": "timeouts",
        "voice_receiver": "voiceReceiver",
        "webhook_receiver": "webhookReceiver",
    },
)
class MonitorActionGroupConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        short_name: builtins.str,
        arm_role_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorActionGroupArmRoleReceiver, typing.Dict[str, typing.Any]]]]] = None,
        automation_runbook_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorActionGroupAutomationRunbookReceiver, typing.Dict[str, typing.Any]]]]] = None,
        azure_app_push_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorActionGroupAzureAppPushReceiver, typing.Dict[str, typing.Any]]]]] = None,
        azure_function_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorActionGroupAzureFunctionReceiver, typing.Dict[str, typing.Any]]]]] = None,
        email_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEmailReceiver", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event_hub_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupEventHubReceiver", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        itsm_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupItsmReceiver", typing.Dict[str, typing.Any]]]]] = None,
        logic_app_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupLogicAppReceiver", typing.Dict[str, typing.Any]]]]] = None,
        sms_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupSmsReceiver", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorActionGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        voice_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupVoiceReceiver", typing.Dict[str, typing.Any]]]]] = None,
        webhook_receiver: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorActionGroupWebhookReceiver", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#resource_group_name MonitorActionGroup#resource_group_name}.
        :param short_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#short_name MonitorActionGroup#short_name}.
        :param arm_role_receiver: arm_role_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#arm_role_receiver MonitorActionGroup#arm_role_receiver}
        :param automation_runbook_receiver: automation_runbook_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#automation_runbook_receiver MonitorActionGroup#automation_runbook_receiver}
        :param azure_app_push_receiver: azure_app_push_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_app_push_receiver MonitorActionGroup#azure_app_push_receiver}
        :param azure_function_receiver: azure_function_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_function_receiver MonitorActionGroup#azure_function_receiver}
        :param email_receiver: email_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_receiver MonitorActionGroup#email_receiver}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#enabled MonitorActionGroup#enabled}.
        :param event_hub_receiver: event_hub_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_receiver MonitorActionGroup#event_hub_receiver}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#id MonitorActionGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param itsm_receiver: itsm_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#itsm_receiver MonitorActionGroup#itsm_receiver}
        :param logic_app_receiver: logic_app_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#logic_app_receiver MonitorActionGroup#logic_app_receiver}
        :param sms_receiver: sms_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#sms_receiver MonitorActionGroup#sms_receiver}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tags MonitorActionGroup#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#timeouts MonitorActionGroup#timeouts}
        :param voice_receiver: voice_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#voice_receiver MonitorActionGroup#voice_receiver}
        :param webhook_receiver: webhook_receiver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#webhook_receiver MonitorActionGroup#webhook_receiver}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MonitorActionGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
            check_type(argname="argument arm_role_receiver", value=arm_role_receiver, expected_type=type_hints["arm_role_receiver"])
            check_type(argname="argument automation_runbook_receiver", value=automation_runbook_receiver, expected_type=type_hints["automation_runbook_receiver"])
            check_type(argname="argument azure_app_push_receiver", value=azure_app_push_receiver, expected_type=type_hints["azure_app_push_receiver"])
            check_type(argname="argument azure_function_receiver", value=azure_function_receiver, expected_type=type_hints["azure_function_receiver"])
            check_type(argname="argument email_receiver", value=email_receiver, expected_type=type_hints["email_receiver"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_hub_receiver", value=event_hub_receiver, expected_type=type_hints["event_hub_receiver"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument itsm_receiver", value=itsm_receiver, expected_type=type_hints["itsm_receiver"])
            check_type(argname="argument logic_app_receiver", value=logic_app_receiver, expected_type=type_hints["logic_app_receiver"])
            check_type(argname="argument sms_receiver", value=sms_receiver, expected_type=type_hints["sms_receiver"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument voice_receiver", value=voice_receiver, expected_type=type_hints["voice_receiver"])
            check_type(argname="argument webhook_receiver", value=webhook_receiver, expected_type=type_hints["webhook_receiver"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
            "short_name": short_name,
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
        if arm_role_receiver is not None:
            self._values["arm_role_receiver"] = arm_role_receiver
        if automation_runbook_receiver is not None:
            self._values["automation_runbook_receiver"] = automation_runbook_receiver
        if azure_app_push_receiver is not None:
            self._values["azure_app_push_receiver"] = azure_app_push_receiver
        if azure_function_receiver is not None:
            self._values["azure_function_receiver"] = azure_function_receiver
        if email_receiver is not None:
            self._values["email_receiver"] = email_receiver
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_hub_receiver is not None:
            self._values["event_hub_receiver"] = event_hub_receiver
        if id is not None:
            self._values["id"] = id
        if itsm_receiver is not None:
            self._values["itsm_receiver"] = itsm_receiver
        if logic_app_receiver is not None:
            self._values["logic_app_receiver"] = logic_app_receiver
        if sms_receiver is not None:
            self._values["sms_receiver"] = sms_receiver
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if voice_receiver is not None:
            self._values["voice_receiver"] = voice_receiver
        if webhook_receiver is not None:
            self._values["webhook_receiver"] = webhook_receiver

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#resource_group_name MonitorActionGroup#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def short_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#short_name MonitorActionGroup#short_name}.'''
        result = self._values.get("short_name")
        assert result is not None, "Required property 'short_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arm_role_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupArmRoleReceiver]]]:
        '''arm_role_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#arm_role_receiver MonitorActionGroup#arm_role_receiver}
        '''
        result = self._values.get("arm_role_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupArmRoleReceiver]]], result)

    @builtins.property
    def automation_runbook_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAutomationRunbookReceiver]]]:
        '''automation_runbook_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#automation_runbook_receiver MonitorActionGroup#automation_runbook_receiver}
        '''
        result = self._values.get("automation_runbook_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAutomationRunbookReceiver]]], result)

    @builtins.property
    def azure_app_push_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureAppPushReceiver]]]:
        '''azure_app_push_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_app_push_receiver MonitorActionGroup#azure_app_push_receiver}
        '''
        result = self._values.get("azure_app_push_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureAppPushReceiver]]], result)

    @builtins.property
    def azure_function_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureFunctionReceiver]]]:
        '''azure_function_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#azure_function_receiver MonitorActionGroup#azure_function_receiver}
        '''
        result = self._values.get("azure_function_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupAzureFunctionReceiver]]], result)

    @builtins.property
    def email_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEmailReceiver"]]]:
        '''email_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_receiver MonitorActionGroup#email_receiver}
        '''
        result = self._values.get("email_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEmailReceiver"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#enabled MonitorActionGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def event_hub_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEventHubReceiver"]]]:
        '''event_hub_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_receiver MonitorActionGroup#event_hub_receiver}
        '''
        result = self._values.get("event_hub_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupEventHubReceiver"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#id MonitorActionGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def itsm_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupItsmReceiver"]]]:
        '''itsm_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#itsm_receiver MonitorActionGroup#itsm_receiver}
        '''
        result = self._values.get("itsm_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupItsmReceiver"]]], result)

    @builtins.property
    def logic_app_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupLogicAppReceiver"]]]:
        '''logic_app_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#logic_app_receiver MonitorActionGroup#logic_app_receiver}
        '''
        result = self._values.get("logic_app_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupLogicAppReceiver"]]], result)

    @builtins.property
    def sms_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupSmsReceiver"]]]:
        '''sms_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#sms_receiver MonitorActionGroup#sms_receiver}
        '''
        result = self._values.get("sms_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupSmsReceiver"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tags MonitorActionGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorActionGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#timeouts MonitorActionGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorActionGroupTimeouts"], result)

    @builtins.property
    def voice_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupVoiceReceiver"]]]:
        '''voice_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#voice_receiver MonitorActionGroup#voice_receiver}
        '''
        result = self._values.get("voice_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupVoiceReceiver"]]], result)

    @builtins.property
    def webhook_receiver(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupWebhookReceiver"]]]:
        '''webhook_receiver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#webhook_receiver MonitorActionGroup#webhook_receiver}
        '''
        result = self._values.get("webhook_receiver")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorActionGroupWebhookReceiver"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEmailReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "email_address": "emailAddress",
        "name": "name",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupEmailReceiver:
    def __init__(
        self,
        *,
        email_address: builtins.str,
        name: builtins.str,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_address MonitorActionGroup#email_address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupEmailReceiver.__init__)
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "email_address": email_address,
            "name": name,
        }
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def email_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#email_address MonitorActionGroup#email_address}.'''
        result = self._values.get("email_address")
        assert result is not None, "Required property 'email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupEmailReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupEmailReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEmailReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupEmailReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupEmailReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupEmailReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupEmailReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEmailReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEmailReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEmailReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupEmailReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEmailReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupEmailReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverOutputReference, "email_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupEmailReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupEmailReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupEmailReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEmailReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEventHubReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "event_hub_id": "eventHubId",
        "event_hub_name": "eventHubName",
        "event_hub_namespace": "eventHubNamespace",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupEventHubReceiver:
    def __init__(
        self,
        *,
        name: builtins.str,
        event_hub_id: typing.Optional[builtins.str] = None,
        event_hub_name: typing.Optional[builtins.str] = None,
        event_hub_namespace: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param event_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_id MonitorActionGroup#event_hub_id}.
        :param event_hub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_name MonitorActionGroup#event_hub_name}.
        :param event_hub_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_namespace MonitorActionGroup#event_hub_namespace}.
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#subscription_id MonitorActionGroup#subscription_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tenant_id MonitorActionGroup#tenant_id}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupEventHubReceiver.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument event_hub_id", value=event_hub_id, expected_type=type_hints["event_hub_id"])
            check_type(argname="argument event_hub_name", value=event_hub_name, expected_type=type_hints["event_hub_name"])
            check_type(argname="argument event_hub_namespace", value=event_hub_namespace, expected_type=type_hints["event_hub_namespace"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if event_hub_id is not None:
            self._values["event_hub_id"] = event_hub_id
        if event_hub_name is not None:
            self._values["event_hub_name"] = event_hub_name
        if event_hub_namespace is not None:
            self._values["event_hub_namespace"] = event_hub_namespace
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_hub_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_id MonitorActionGroup#event_hub_id}.'''
        result = self._values.get("event_hub_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_hub_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_name MonitorActionGroup#event_hub_name}.'''
        result = self._values.get("event_hub_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_hub_namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#event_hub_namespace MonitorActionGroup#event_hub_namespace}.'''
        result = self._values.get("event_hub_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#subscription_id MonitorActionGroup#subscription_id}.'''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tenant_id MonitorActionGroup#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupEventHubReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupEventHubReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEventHubReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupEventHubReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupEventHubReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupEventHubReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupEventHubReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEventHubReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEventHubReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupEventHubReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupEventHubReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupEventHubReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupEventHubReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEventHubId")
    def reset_event_hub_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHubId", []))

    @jsii.member(jsii_name="resetEventHubName")
    def reset_event_hub_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHubName", []))

    @jsii.member(jsii_name="resetEventHubNamespace")
    def reset_event_hub_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHubNamespace", []))

    @jsii.member(jsii_name="resetSubscriptionId")
    def reset_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="eventHubIdInput")
    def event_hub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventHubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHubNameInput")
    def event_hub_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventHubNameInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHubNamespaceInput")
    def event_hub_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventHubNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHubId")
    def event_hub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventHubId"))

    @event_hub_id.setter
    def event_hub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "event_hub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventHubId", value)

    @builtins.property
    @jsii.member(jsii_name="eventHubName")
    def event_hub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventHubName"))

    @event_hub_name.setter
    def event_hub_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "event_hub_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventHubName", value)

    @builtins.property
    @jsii.member(jsii_name="eventHubNamespace")
    def event_hub_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventHubNamespace"))

    @event_hub_namespace.setter
    def event_hub_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "event_hub_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventHubNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "subscription_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupEventHubReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupEventHubReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupEventHubReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupEventHubReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupItsmReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "connection_id": "connectionId",
        "name": "name",
        "region": "region",
        "ticket_configuration": "ticketConfiguration",
        "workspace_id": "workspaceId",
    },
)
class MonitorActionGroupItsmReceiver:
    def __init__(
        self,
        *,
        connection_id: builtins.str,
        name: builtins.str,
        region: builtins.str,
        ticket_configuration: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#connection_id MonitorActionGroup#connection_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#region MonitorActionGroup#region}.
        :param ticket_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#ticket_configuration MonitorActionGroup#ticket_configuration}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#workspace_id MonitorActionGroup#workspace_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupItsmReceiver.__init__)
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument ticket_configuration", value=ticket_configuration, expected_type=type_hints["ticket_configuration"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_id": connection_id,
            "name": name,
            "region": region,
            "ticket_configuration": ticket_configuration,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def connection_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#connection_id MonitorActionGroup#connection_id}.'''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#region MonitorActionGroup#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ticket_configuration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#ticket_configuration MonitorActionGroup#ticket_configuration}.'''
        result = self._values.get("ticket_configuration")
        assert result is not None, "Required property 'ticket_configuration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#workspace_id MonitorActionGroup#workspace_id}.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupItsmReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupItsmReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupItsmReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupItsmReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupItsmReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupItsmReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupItsmReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupItsmReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupItsmReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupItsmReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupItsmReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupItsmReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupItsmReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketConfigurationInput")
    def ticket_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "connection_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="ticketConfiguration")
    def ticket_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketConfiguration"))

    @ticket_configuration.setter
    def ticket_configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "ticket_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupItsmReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupItsmReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupItsmReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupItsmReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupLogicAppReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "callback_url": "callbackUrl",
        "name": "name",
        "resource_id": "resourceId",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupLogicAppReceiver:
    def __init__(
        self,
        *,
        callback_url: builtins.str,
        name: builtins.str,
        resource_id: builtins.str,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param callback_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#callback_url MonitorActionGroup#callback_url}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#resource_id MonitorActionGroup#resource_id}.
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupLogicAppReceiver.__init__)
            check_type(argname="argument callback_url", value=callback_url, expected_type=type_hints["callback_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "callback_url": callback_url,
            "name": name,
            "resource_id": resource_id,
        }
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def callback_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#callback_url MonitorActionGroup#callback_url}.'''
        result = self._values.get("callback_url")
        assert result is not None, "Required property 'callback_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#resource_id MonitorActionGroup#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupLogicAppReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupLogicAppReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupLogicAppReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupLogicAppReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupLogicAppReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupLogicAppReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupLogicAppReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupLogicAppReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupLogicAppReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupLogicAppReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupLogicAppReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupLogicAppReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupLogicAppReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="callbackUrlInput")
    def callback_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callbackUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="callbackUrl")
    def callback_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callbackUrl"))

    @callback_url.setter
    def callback_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverOutputReference, "callback_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbackUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverOutputReference, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupLogicAppReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupLogicAppReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupLogicAppReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupLogicAppReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupSmsReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "country_code": "countryCode",
        "name": "name",
        "phone_number": "phoneNumber",
    },
)
class MonitorActionGroupSmsReceiver:
    def __init__(
        self,
        *,
        country_code: builtins.str,
        name: builtins.str,
        phone_number: builtins.str,
    ) -> None:
        '''
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#country_code MonitorActionGroup#country_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#phone_number MonitorActionGroup#phone_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupSmsReceiver.__init__)
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "country_code": country_code,
            "name": name,
            "phone_number": phone_number,
        }

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#country_code MonitorActionGroup#country_code}.'''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#phone_number MonitorActionGroup#phone_number}.'''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupSmsReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupSmsReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupSmsReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupSmsReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorActionGroupSmsReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupSmsReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupSmsReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupSmsReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupSmsReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupSmsReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupSmsReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupSmsReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupSmsReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverOutputReference, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverOutputReference, "phone_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupSmsReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupSmsReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupSmsReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupSmsReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorActionGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#create MonitorActionGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#delete MonitorActionGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#read MonitorActionGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#update MonitorActionGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#create MonitorActionGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#delete MonitorActionGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#read MonitorActionGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#update MonitorActionGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupVoiceReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "country_code": "countryCode",
        "name": "name",
        "phone_number": "phoneNumber",
    },
)
class MonitorActionGroupVoiceReceiver:
    def __init__(
        self,
        *,
        country_code: builtins.str,
        name: builtins.str,
        phone_number: builtins.str,
    ) -> None:
        '''
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#country_code MonitorActionGroup#country_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#phone_number MonitorActionGroup#phone_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupVoiceReceiver.__init__)
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "country_code": country_code,
            "name": name,
            "phone_number": phone_number,
        }

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#country_code MonitorActionGroup#country_code}.'''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#phone_number MonitorActionGroup#phone_number}.'''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupVoiceReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupVoiceReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupVoiceReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupVoiceReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupVoiceReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupVoiceReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupVoiceReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupVoiceReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupVoiceReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupVoiceReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupVoiceReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupVoiceReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupVoiceReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverOutputReference, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverOutputReference, "phone_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupVoiceReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupVoiceReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupVoiceReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupVoiceReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupWebhookReceiver",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "service_uri": "serviceUri",
        "aad_auth": "aadAuth",
        "use_common_alert_schema": "useCommonAlertSchema",
    },
)
class MonitorActionGroupWebhookReceiver:
    def __init__(
        self,
        *,
        name: builtins.str,
        service_uri: builtins.str,
        aad_auth: typing.Optional[typing.Union["MonitorActionGroupWebhookReceiverAadAuth", typing.Dict[str, typing.Any]]] = None,
        use_common_alert_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.
        :param service_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#service_uri MonitorActionGroup#service_uri}.
        :param aad_auth: aad_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#aad_auth MonitorActionGroup#aad_auth}
        :param use_common_alert_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.
        '''
        if isinstance(aad_auth, dict):
            aad_auth = MonitorActionGroupWebhookReceiverAadAuth(**aad_auth)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiver.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_uri", value=service_uri, expected_type=type_hints["service_uri"])
            check_type(argname="argument aad_auth", value=aad_auth, expected_type=type_hints["aad_auth"])
            check_type(argname="argument use_common_alert_schema", value=use_common_alert_schema, expected_type=type_hints["use_common_alert_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "service_uri": service_uri,
        }
        if aad_auth is not None:
            self._values["aad_auth"] = aad_auth
        if use_common_alert_schema is not None:
            self._values["use_common_alert_schema"] = use_common_alert_schema

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#name MonitorActionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#service_uri MonitorActionGroup#service_uri}.'''
        result = self._values.get("service_uri")
        assert result is not None, "Required property 'service_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aad_auth(self) -> typing.Optional["MonitorActionGroupWebhookReceiverAadAuth"]:
        '''aad_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#aad_auth MonitorActionGroup#aad_auth}
        '''
        result = self._values.get("aad_auth")
        return typing.cast(typing.Optional["MonitorActionGroupWebhookReceiverAadAuth"], result)

    @builtins.property
    def use_common_alert_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#use_common_alert_schema MonitorActionGroup#use_common_alert_schema}.'''
        result = self._values.get("use_common_alert_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupWebhookReceiver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupWebhookReceiverAadAuth",
    jsii_struct_bases=[],
    name_mapping={
        "object_id": "objectId",
        "identifier_uri": "identifierUri",
        "tenant_id": "tenantId",
    },
)
class MonitorActionGroupWebhookReceiverAadAuth:
    def __init__(
        self,
        *,
        object_id: builtins.str,
        identifier_uri: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#object_id MonitorActionGroup#object_id}.
        :param identifier_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#identifier_uri MonitorActionGroup#identifier_uri}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tenant_id MonitorActionGroup#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiverAadAuth.__init__)
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument identifier_uri", value=identifier_uri, expected_type=type_hints["identifier_uri"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id": object_id,
        }
        if identifier_uri is not None:
            self._values["identifier_uri"] = identifier_uri
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def object_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#object_id MonitorActionGroup#object_id}.'''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#identifier_uri MonitorActionGroup#identifier_uri}.'''
        result = self._values.get("identifier_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tenant_id MonitorActionGroup#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorActionGroupWebhookReceiverAadAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorActionGroupWebhookReceiverAadAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupWebhookReceiverAadAuthOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiverAadAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentifierUri")
    def reset_identifier_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifierUri", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="identifierUriInput")
    def identifier_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierUriInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierUri")
    def identifier_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifierUri"))

    @identifier_uri.setter
    def identifier_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverAadAuthOutputReference, "identifier_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifierUri", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverAadAuthOutputReference, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverAadAuthOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorActionGroupWebhookReceiverAadAuth]:
        return typing.cast(typing.Optional[MonitorActionGroupWebhookReceiverAadAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorActionGroupWebhookReceiverAadAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverAadAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupWebhookReceiverList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupWebhookReceiverList",
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
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiverList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorActionGroupWebhookReceiverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiverList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorActionGroupWebhookReceiverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupWebhookReceiver]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupWebhookReceiver]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorActionGroupWebhookReceiver]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorActionGroupWebhookReceiverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorActionGroup.MonitorActionGroupWebhookReceiverOutputReference",
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
            type_hints = typing.get_type_hints(MonitorActionGroupWebhookReceiverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAadAuth")
    def put_aad_auth(
        self,
        *,
        object_id: builtins.str,
        identifier_uri: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#object_id MonitorActionGroup#object_id}.
        :param identifier_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#identifier_uri MonitorActionGroup#identifier_uri}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group#tenant_id MonitorActionGroup#tenant_id}.
        '''
        value = MonitorActionGroupWebhookReceiverAadAuth(
            object_id=object_id, identifier_uri=identifier_uri, tenant_id=tenant_id
        )

        return typing.cast(None, jsii.invoke(self, "putAadAuth", [value]))

    @jsii.member(jsii_name="resetAadAuth")
    def reset_aad_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAadAuth", []))

    @jsii.member(jsii_name="resetUseCommonAlertSchema")
    def reset_use_common_alert_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCommonAlertSchema", []))

    @builtins.property
    @jsii.member(jsii_name="aadAuth")
    def aad_auth(self) -> MonitorActionGroupWebhookReceiverAadAuthOutputReference:
        return typing.cast(MonitorActionGroupWebhookReceiverAadAuthOutputReference, jsii.get(self, "aadAuth"))

    @builtins.property
    @jsii.member(jsii_name="aadAuthInput")
    def aad_auth_input(
        self,
    ) -> typing.Optional[MonitorActionGroupWebhookReceiverAadAuth]:
        return typing.cast(typing.Optional[MonitorActionGroupWebhookReceiverAadAuth], jsii.get(self, "aadAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceUriInput")
    def service_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchemaInput")
    def use_common_alert_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCommonAlertSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceUri")
    def service_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceUri"))

    @service_uri.setter
    def service_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverOutputReference, "service_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceUri", value)

    @builtins.property
    @jsii.member(jsii_name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCommonAlertSchema"))

    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverOutputReference, "use_common_alert_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCommonAlertSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorActionGroupWebhookReceiver, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorActionGroupWebhookReceiver, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorActionGroupWebhookReceiver, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorActionGroupWebhookReceiverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorActionGroup",
    "MonitorActionGroupArmRoleReceiver",
    "MonitorActionGroupArmRoleReceiverList",
    "MonitorActionGroupArmRoleReceiverOutputReference",
    "MonitorActionGroupAutomationRunbookReceiver",
    "MonitorActionGroupAutomationRunbookReceiverList",
    "MonitorActionGroupAutomationRunbookReceiverOutputReference",
    "MonitorActionGroupAzureAppPushReceiver",
    "MonitorActionGroupAzureAppPushReceiverList",
    "MonitorActionGroupAzureAppPushReceiverOutputReference",
    "MonitorActionGroupAzureFunctionReceiver",
    "MonitorActionGroupAzureFunctionReceiverList",
    "MonitorActionGroupAzureFunctionReceiverOutputReference",
    "MonitorActionGroupConfig",
    "MonitorActionGroupEmailReceiver",
    "MonitorActionGroupEmailReceiverList",
    "MonitorActionGroupEmailReceiverOutputReference",
    "MonitorActionGroupEventHubReceiver",
    "MonitorActionGroupEventHubReceiverList",
    "MonitorActionGroupEventHubReceiverOutputReference",
    "MonitorActionGroupItsmReceiver",
    "MonitorActionGroupItsmReceiverList",
    "MonitorActionGroupItsmReceiverOutputReference",
    "MonitorActionGroupLogicAppReceiver",
    "MonitorActionGroupLogicAppReceiverList",
    "MonitorActionGroupLogicAppReceiverOutputReference",
    "MonitorActionGroupSmsReceiver",
    "MonitorActionGroupSmsReceiverList",
    "MonitorActionGroupSmsReceiverOutputReference",
    "MonitorActionGroupTimeouts",
    "MonitorActionGroupTimeoutsOutputReference",
    "MonitorActionGroupVoiceReceiver",
    "MonitorActionGroupVoiceReceiverList",
    "MonitorActionGroupVoiceReceiverOutputReference",
    "MonitorActionGroupWebhookReceiver",
    "MonitorActionGroupWebhookReceiverAadAuth",
    "MonitorActionGroupWebhookReceiverAadAuthOutputReference",
    "MonitorActionGroupWebhookReceiverList",
    "MonitorActionGroupWebhookReceiverOutputReference",
]

publication.publish()
