'''
# `azurerm_monitor_diagnostic_setting`

Refer to the Terraform Registory for docs: [`azurerm_monitor_diagnostic_setting`](https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting).
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


class MonitorDiagnosticSetting(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSetting",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting azurerm_monitor_diagnostic_setting}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        target_resource_id: builtins.str,
        eventhub_authorization_rule_id: typing.Optional[builtins.str] = None,
        eventhub_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingLog", typing.Dict[str, typing.Any]]]]] = None,
        log_analytics_destination_type: typing.Optional[builtins.str] = None,
        log_analytics_workspace_id: typing.Optional[builtins.str] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingMetric", typing.Dict[str, typing.Any]]]]] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MonitorDiagnosticSettingTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting azurerm_monitor_diagnostic_setting} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#name MonitorDiagnosticSetting#name}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#target_resource_id MonitorDiagnosticSetting#target_resource_id}.
        :param eventhub_authorization_rule_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_authorization_rule_id MonitorDiagnosticSetting#eventhub_authorization_rule_id}.
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_name MonitorDiagnosticSetting#eventhub_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#id MonitorDiagnosticSetting#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log: log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log MonitorDiagnosticSetting#log}
        :param log_analytics_destination_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_destination_type MonitorDiagnosticSetting#log_analytics_destination_type}.
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_workspace_id MonitorDiagnosticSetting#log_analytics_workspace_id}.
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#metric MonitorDiagnosticSetting#metric}
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#storage_account_id MonitorDiagnosticSetting#storage_account_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#timeouts MonitorDiagnosticSetting#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSetting.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorDiagnosticSettingConfig(
            name=name,
            target_resource_id=target_resource_id,
            eventhub_authorization_rule_id=eventhub_authorization_rule_id,
            eventhub_name=eventhub_name,
            id=id,
            log=log,
            log_analytics_destination_type=log_analytics_destination_type,
            log_analytics_workspace_id=log_analytics_workspace_id,
            metric=metric,
            storage_account_id=storage_account_id,
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

    @jsii.member(jsii_name="putLog")
    def put_log(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingLog", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSetting.put_log)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLog", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingMetric", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSetting.put_metric)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#create MonitorDiagnosticSetting#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#delete MonitorDiagnosticSetting#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#read MonitorDiagnosticSetting#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#update MonitorDiagnosticSetting#update}.
        '''
        value = MonitorDiagnosticSettingTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEventhubAuthorizationRuleId")
    def reset_eventhub_authorization_rule_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventhubAuthorizationRuleId", []))

    @jsii.member(jsii_name="resetEventhubName")
    def reset_eventhub_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventhubName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLog")
    def reset_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLog", []))

    @jsii.member(jsii_name="resetLogAnalyticsDestinationType")
    def reset_log_analytics_destination_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogAnalyticsDestinationType", []))

    @jsii.member(jsii_name="resetLogAnalyticsWorkspaceId")
    def reset_log_analytics_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogAnalyticsWorkspaceId", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetStorageAccountId")
    def reset_storage_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountId", []))

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
    @jsii.member(jsii_name="log")
    def log(self) -> "MonitorDiagnosticSettingLogList":
        return typing.cast("MonitorDiagnosticSettingLogList", jsii.get(self, "log"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> "MonitorDiagnosticSettingMetricList":
        return typing.cast("MonitorDiagnosticSettingMetricList", jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorDiagnosticSettingTimeoutsOutputReference":
        return typing.cast("MonitorDiagnosticSettingTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="eventhubAuthorizationRuleIdInput")
    def eventhub_authorization_rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubAuthorizationRuleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubNameInput")
    def eventhub_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsDestinationTypeInput")
    def log_analytics_destination_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsDestinationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logInput")
    def log_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingLog"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingLog"]]], jsii.get(self, "logInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingMetric"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingMetric"]]], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceIdInput")
    def target_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorDiagnosticSettingTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorDiagnosticSettingTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubAuthorizationRuleId")
    def eventhub_authorization_rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubAuthorizationRuleId"))

    @eventhub_authorization_rule_id.setter
    def eventhub_authorization_rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "eventhub_authorization_rule_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubAuthorizationRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubName")
    def eventhub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubName"))

    @eventhub_name.setter
    def eventhub_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "eventhub_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsDestinationType")
    def log_analytics_destination_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsDestinationType"))

    @log_analytics_destination_type.setter
    def log_analytics_destination_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "log_analytics_destination_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsDestinationType", value)

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceId")
    def target_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceId"))

    @target_resource_id.setter
    def target_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSetting, "target_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingConfig",
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
        "target_resource_id": "targetResourceId",
        "eventhub_authorization_rule_id": "eventhubAuthorizationRuleId",
        "eventhub_name": "eventhubName",
        "id": "id",
        "log": "log",
        "log_analytics_destination_type": "logAnalyticsDestinationType",
        "log_analytics_workspace_id": "logAnalyticsWorkspaceId",
        "metric": "metric",
        "storage_account_id": "storageAccountId",
        "timeouts": "timeouts",
    },
)
class MonitorDiagnosticSettingConfig(cdktf.TerraformMetaArguments):
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
        target_resource_id: builtins.str,
        eventhub_authorization_rule_id: typing.Optional[builtins.str] = None,
        eventhub_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingLog", typing.Dict[str, typing.Any]]]]] = None,
        log_analytics_destination_type: typing.Optional[builtins.str] = None,
        log_analytics_workspace_id: typing.Optional[builtins.str] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDiagnosticSettingMetric", typing.Dict[str, typing.Any]]]]] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MonitorDiagnosticSettingTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#name MonitorDiagnosticSetting#name}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#target_resource_id MonitorDiagnosticSetting#target_resource_id}.
        :param eventhub_authorization_rule_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_authorization_rule_id MonitorDiagnosticSetting#eventhub_authorization_rule_id}.
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_name MonitorDiagnosticSetting#eventhub_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#id MonitorDiagnosticSetting#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log: log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log MonitorDiagnosticSetting#log}
        :param log_analytics_destination_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_destination_type MonitorDiagnosticSetting#log_analytics_destination_type}.
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_workspace_id MonitorDiagnosticSetting#log_analytics_workspace_id}.
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#metric MonitorDiagnosticSetting#metric}
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#storage_account_id MonitorDiagnosticSetting#storage_account_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#timeouts MonitorDiagnosticSetting#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MonitorDiagnosticSettingTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_resource_id", value=target_resource_id, expected_type=type_hints["target_resource_id"])
            check_type(argname="argument eventhub_authorization_rule_id", value=eventhub_authorization_rule_id, expected_type=type_hints["eventhub_authorization_rule_id"])
            check_type(argname="argument eventhub_name", value=eventhub_name, expected_type=type_hints["eventhub_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument log_analytics_destination_type", value=log_analytics_destination_type, expected_type=type_hints["log_analytics_destination_type"])
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "target_resource_id": target_resource_id,
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
        if eventhub_authorization_rule_id is not None:
            self._values["eventhub_authorization_rule_id"] = eventhub_authorization_rule_id
        if eventhub_name is not None:
            self._values["eventhub_name"] = eventhub_name
        if id is not None:
            self._values["id"] = id
        if log is not None:
            self._values["log"] = log
        if log_analytics_destination_type is not None:
            self._values["log_analytics_destination_type"] = log_analytics_destination_type
        if log_analytics_workspace_id is not None:
            self._values["log_analytics_workspace_id"] = log_analytics_workspace_id
        if metric is not None:
            self._values["metric"] = metric
        if storage_account_id is not None:
            self._values["storage_account_id"] = storage_account_id
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#name MonitorDiagnosticSetting#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#target_resource_id MonitorDiagnosticSetting#target_resource_id}.'''
        result = self._values.get("target_resource_id")
        assert result is not None, "Required property 'target_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def eventhub_authorization_rule_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_authorization_rule_id MonitorDiagnosticSetting#eventhub_authorization_rule_id}.'''
        result = self._values.get("eventhub_authorization_rule_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventhub_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#eventhub_name MonitorDiagnosticSetting#eventhub_name}.'''
        result = self._values.get("eventhub_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#id MonitorDiagnosticSetting#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingLog"]]]:
        '''log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log MonitorDiagnosticSetting#log}
        '''
        result = self._values.get("log")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingLog"]]], result)

    @builtins.property
    def log_analytics_destination_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_destination_type MonitorDiagnosticSetting#log_analytics_destination_type}.'''
        result = self._values.get("log_analytics_destination_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_analytics_workspace_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#log_analytics_workspace_id MonitorDiagnosticSetting#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingMetric"]]]:
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#metric MonitorDiagnosticSetting#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDiagnosticSettingMetric"]]], result)

    @builtins.property
    def storage_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#storage_account_id MonitorDiagnosticSetting#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorDiagnosticSettingTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#timeouts MonitorDiagnosticSetting#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorDiagnosticSettingTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingLog",
    jsii_struct_bases=[],
    name_mapping={
        "category": "category",
        "category_group": "categoryGroup",
        "enabled": "enabled",
        "retention_policy": "retentionPolicy",
    },
)
class MonitorDiagnosticSettingLog:
    def __init__(
        self,
        *,
        category: typing.Optional[builtins.str] = None,
        category_group: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy: typing.Optional[typing.Union["MonitorDiagnosticSettingLogRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category MonitorDiagnosticSetting#category}.
        :param category_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category_group MonitorDiagnosticSetting#category_group}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#retention_policy MonitorDiagnosticSetting#retention_policy}
        '''
        if isinstance(retention_policy, dict):
            retention_policy = MonitorDiagnosticSettingLogRetentionPolicy(**retention_policy)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLog.__init__)
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument category_group", value=category_group, expected_type=type_hints["category_group"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if category is not None:
            self._values["category"] = category
        if category_group is not None:
            self._values["category_group"] = category_group
        if enabled is not None:
            self._values["enabled"] = enabled
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category MonitorDiagnosticSetting#category}.'''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def category_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category_group MonitorDiagnosticSetting#category_group}.'''
        result = self._values.get("category_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_policy(
        self,
    ) -> typing.Optional["MonitorDiagnosticSettingLogRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#retention_policy MonitorDiagnosticSetting#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["MonitorDiagnosticSettingLogRetentionPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDiagnosticSettingLogList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingLogList",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLogList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorDiagnosticSettingLogOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLogList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDiagnosticSettingLogOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingLog]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingLog]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingLog]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDiagnosticSettingLogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingLogOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.
        '''
        value = MonitorDiagnosticSettingLogRetentionPolicy(enabled=enabled, days=days)

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="resetCategory")
    def reset_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategory", []))

    @jsii.member(jsii_name="resetCategoryGroup")
    def reset_category_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryGroup", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(
        self,
    ) -> "MonitorDiagnosticSettingLogRetentionPolicyOutputReference":
        return typing.cast("MonitorDiagnosticSettingLogRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="categoryGroupInput")
    def category_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["MonitorDiagnosticSettingLogRetentionPolicy"]:
        return typing.cast(typing.Optional["MonitorDiagnosticSettingLogRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogOutputReference, "category").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="categoryGroup")
    def category_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "categoryGroup"))

    @category_group.setter
    def category_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogOutputReference, "category_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryGroup", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDiagnosticSettingLog, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDiagnosticSettingLog, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDiagnosticSettingLog, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingLogRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "days": "days"},
)
class MonitorDiagnosticSettingLogRetentionPolicy:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLogRetentionPolicy.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingLogRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDiagnosticSettingLogRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingLogRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingLogRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogRetentionPolicyOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogRetentionPolicyOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorDiagnosticSettingLogRetentionPolicy]:
        return typing.cast(typing.Optional[MonitorDiagnosticSettingLogRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorDiagnosticSettingLogRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingLogRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingMetric",
    jsii_struct_bases=[],
    name_mapping={
        "category": "category",
        "enabled": "enabled",
        "retention_policy": "retentionPolicy",
    },
)
class MonitorDiagnosticSettingMetric:
    def __init__(
        self,
        *,
        category: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy: typing.Optional[typing.Union["MonitorDiagnosticSettingMetricRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category MonitorDiagnosticSetting#category}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#retention_policy MonitorDiagnosticSetting#retention_policy}
        '''
        if isinstance(retention_policy, dict):
            retention_policy = MonitorDiagnosticSettingMetricRetentionPolicy(**retention_policy)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetric.__init__)
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "category": category,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy

    @builtins.property
    def category(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#category MonitorDiagnosticSetting#category}.'''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_policy(
        self,
    ) -> typing.Optional["MonitorDiagnosticSettingMetricRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#retention_policy MonitorDiagnosticSetting#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["MonitorDiagnosticSettingMetricRetentionPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDiagnosticSettingMetricList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingMetricList",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetricList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDiagnosticSettingMetricOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetricList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDiagnosticSettingMetricOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingMetric]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingMetric]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDiagnosticSettingMetric]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDiagnosticSettingMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingMetricOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.
        '''
        value = MonitorDiagnosticSettingMetricRetentionPolicy(
            enabled=enabled, days=days
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(
        self,
    ) -> "MonitorDiagnosticSettingMetricRetentionPolicyOutputReference":
        return typing.cast("MonitorDiagnosticSettingMetricRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["MonitorDiagnosticSettingMetricRetentionPolicy"]:
        return typing.cast(typing.Optional["MonitorDiagnosticSettingMetricRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricOutputReference, "category").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDiagnosticSettingMetric, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDiagnosticSettingMetric, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDiagnosticSettingMetric, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingMetricRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "days": "days"},
)
class MonitorDiagnosticSettingMetricRetentionPolicy:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetricRetentionPolicy.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#enabled MonitorDiagnosticSetting#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#days MonitorDiagnosticSetting#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingMetricRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDiagnosticSettingMetricRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingMetricRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingMetricRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricRetentionPolicyOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricRetentionPolicyOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorDiagnosticSettingMetricRetentionPolicy]:
        return typing.cast(typing.Optional[MonitorDiagnosticSettingMetricRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorDiagnosticSettingMetricRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingMetricRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorDiagnosticSettingTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#create MonitorDiagnosticSetting#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#delete MonitorDiagnosticSetting#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#read MonitorDiagnosticSetting#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#update MonitorDiagnosticSetting#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#create MonitorDiagnosticSetting#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#delete MonitorDiagnosticSetting#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#read MonitorDiagnosticSetting#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting#update MonitorDiagnosticSetting#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDiagnosticSettingTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDiagnosticSettingTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDiagnosticSetting.MonitorDiagnosticSettingTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDiagnosticSettingTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDiagnosticSettingTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDiagnosticSettingTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDiagnosticSettingTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDiagnosticSettingTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorDiagnosticSetting",
    "MonitorDiagnosticSettingConfig",
    "MonitorDiagnosticSettingLog",
    "MonitorDiagnosticSettingLogList",
    "MonitorDiagnosticSettingLogOutputReference",
    "MonitorDiagnosticSettingLogRetentionPolicy",
    "MonitorDiagnosticSettingLogRetentionPolicyOutputReference",
    "MonitorDiagnosticSettingMetric",
    "MonitorDiagnosticSettingMetricList",
    "MonitorDiagnosticSettingMetricOutputReference",
    "MonitorDiagnosticSettingMetricRetentionPolicy",
    "MonitorDiagnosticSettingMetricRetentionPolicyOutputReference",
    "MonitorDiagnosticSettingTimeouts",
    "MonitorDiagnosticSettingTimeoutsOutputReference",
]

publication.publish()
