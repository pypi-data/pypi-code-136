'''
# `azurerm_consumption_budget_management_group`

Refer to the Terraform Registory for docs: [`azurerm_consumption_budget_management_group`](https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group).
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


class ConsumptionBudgetManagementGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group azurerm_consumption_budget_management_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        amount: jsii.Number,
        management_group_id: builtins.str,
        name: builtins.str,
        notification: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupNotification", typing.Dict[str, typing.Any]]]],
        time_period: typing.Union["ConsumptionBudgetManagementGroupTimePeriod", typing.Dict[str, typing.Any]],
        etag: typing.Optional[builtins.str] = None,
        filter: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        time_grain: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group azurerm_consumption_budget_management_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#amount ConsumptionBudgetManagementGroup#amount}.
        :param management_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#management_group_id ConsumptionBudgetManagementGroup#management_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#notification ConsumptionBudgetManagementGroup#notification}
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_period ConsumptionBudgetManagementGroup#time_period}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#etag ConsumptionBudgetManagementGroup#etag}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#filter ConsumptionBudgetManagementGroup#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#id ConsumptionBudgetManagementGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param time_grain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_grain ConsumptionBudgetManagementGroup#time_grain}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#timeouts ConsumptionBudgetManagementGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConsumptionBudgetManagementGroupConfig(
            amount=amount,
            management_group_id=management_group_id,
            name=name,
            notification=notification,
            time_period=time_period,
            etag=etag,
            filter=filter,
            id=id,
            time_grain=time_grain,
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

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupFilterDimension", typing.Dict[str, typing.Any]]]]] = None,
        not_: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilterNot", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupFilterTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#not ConsumptionBudgetManagementGroup#not}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        value = ConsumptionBudgetManagementGroupFilter(
            dimension=dimension, not_=not_, tag=tag
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putNotification")
    def put_notification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupNotification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroup.put_notification)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNotification", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#create ConsumptionBudgetManagementGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#delete ConsumptionBudgetManagementGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#read ConsumptionBudgetManagementGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#update ConsumptionBudgetManagementGroup#update}.
        '''
        value = ConsumptionBudgetManagementGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTimePeriod")
    def put_time_period(
        self,
        *,
        start_date: builtins.str,
        end_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#start_date ConsumptionBudgetManagementGroup#start_date}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#end_date ConsumptionBudgetManagementGroup#end_date}.
        '''
        value = ConsumptionBudgetManagementGroupTimePeriod(
            start_date=start_date, end_date=end_date
        )

        return typing.cast(None, jsii.invoke(self, "putTimePeriod", [value]))

    @jsii.member(jsii_name="resetEtag")
    def reset_etag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtag", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeGrain")
    def reset_time_grain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeGrain", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "ConsumptionBudgetManagementGroupFilterOutputReference":
        return typing.cast("ConsumptionBudgetManagementGroupFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="notification")
    def notification(self) -> "ConsumptionBudgetManagementGroupNotificationList":
        return typing.cast("ConsumptionBudgetManagementGroupNotificationList", jsii.get(self, "notification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConsumptionBudgetManagementGroupTimeoutsOutputReference":
        return typing.cast("ConsumptionBudgetManagementGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="timePeriod")
    def time_period(
        self,
    ) -> "ConsumptionBudgetManagementGroupTimePeriodOutputReference":
        return typing.cast("ConsumptionBudgetManagementGroupTimePeriodOutputReference", jsii.get(self, "timePeriod"))

    @builtins.property
    @jsii.member(jsii_name="amountInput")
    def amount_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "amountInput"))

    @builtins.property
    @jsii.member(jsii_name="etagInput")
    def etag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "etagInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["ConsumptionBudgetManagementGroupFilter"]:
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managementGroupIdInput")
    def management_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managementGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationInput")
    def notification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupNotification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupNotification"]]], jsii.get(self, "notificationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeGrainInput")
    def time_grain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeGrainInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ConsumptionBudgetManagementGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ConsumptionBudgetManagementGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodInput")
    def time_period_input(
        self,
    ) -> typing.Optional["ConsumptionBudgetManagementGroupTimePeriod"]:
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupTimePeriod"], jsii.get(self, "timePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="amount")
    def amount(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "amount"))

    @amount.setter
    def amount(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "amount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amount", value)

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @etag.setter
    def etag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "etag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "etag", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="managementGroupId")
    def management_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementGroupId"))

    @management_group_id.setter
    def management_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "management_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="timeGrain")
    def time_grain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeGrain"))

    @time_grain.setter
    def time_grain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroup, "time_grain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeGrain", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "amount": "amount",
        "management_group_id": "managementGroupId",
        "name": "name",
        "notification": "notification",
        "time_period": "timePeriod",
        "etag": "etag",
        "filter": "filter",
        "id": "id",
        "time_grain": "timeGrain",
        "timeouts": "timeouts",
    },
)
class ConsumptionBudgetManagementGroupConfig(cdktf.TerraformMetaArguments):
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
        amount: jsii.Number,
        management_group_id: builtins.str,
        name: builtins.str,
        notification: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupNotification", typing.Dict[str, typing.Any]]]],
        time_period: typing.Union["ConsumptionBudgetManagementGroupTimePeriod", typing.Dict[str, typing.Any]],
        etag: typing.Optional[builtins.str] = None,
        filter: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        time_grain: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#amount ConsumptionBudgetManagementGroup#amount}.
        :param management_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#management_group_id ConsumptionBudgetManagementGroup#management_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#notification ConsumptionBudgetManagementGroup#notification}
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_period ConsumptionBudgetManagementGroup#time_period}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#etag ConsumptionBudgetManagementGroup#etag}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#filter ConsumptionBudgetManagementGroup#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#id ConsumptionBudgetManagementGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param time_grain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_grain ConsumptionBudgetManagementGroup#time_grain}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#timeouts ConsumptionBudgetManagementGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(time_period, dict):
            time_period = ConsumptionBudgetManagementGroupTimePeriod(**time_period)
        if isinstance(filter, dict):
            filter = ConsumptionBudgetManagementGroupFilter(**filter)
        if isinstance(timeouts, dict):
            timeouts = ConsumptionBudgetManagementGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
            check_type(argname="argument management_group_id", value=management_group_id, expected_type=type_hints["management_group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notification", value=notification, expected_type=type_hints["notification"])
            check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument time_grain", value=time_grain, expected_type=type_hints["time_grain"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "amount": amount,
            "management_group_id": management_group_id,
            "name": name,
            "notification": notification,
            "time_period": time_period,
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
        if etag is not None:
            self._values["etag"] = etag
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if time_grain is not None:
            self._values["time_grain"] = time_grain
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
    def amount(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#amount ConsumptionBudgetManagementGroup#amount}.'''
        result = self._values.get("amount")
        assert result is not None, "Required property 'amount' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def management_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#management_group_id ConsumptionBudgetManagementGroup#management_group_id}.'''
        result = self._values.get("management_group_id")
        assert result is not None, "Required property 'management_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupNotification"]]:
        '''notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#notification ConsumptionBudgetManagementGroup#notification}
        '''
        result = self._values.get("notification")
        assert result is not None, "Required property 'notification' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupNotification"]], result)

    @builtins.property
    def time_period(self) -> "ConsumptionBudgetManagementGroupTimePeriod":
        '''time_period block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_period ConsumptionBudgetManagementGroup#time_period}
        '''
        result = self._values.get("time_period")
        assert result is not None, "Required property 'time_period' is missing"
        return typing.cast("ConsumptionBudgetManagementGroupTimePeriod", result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#etag ConsumptionBudgetManagementGroup#etag}.'''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional["ConsumptionBudgetManagementGroupFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#filter ConsumptionBudgetManagementGroup#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#id ConsumptionBudgetManagementGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_grain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#time_grain ConsumptionBudgetManagementGroup#time_grain}.'''
        result = self._values.get("time_grain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConsumptionBudgetManagementGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#timeouts ConsumptionBudgetManagementGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilter",
    jsii_struct_bases=[],
    name_mapping={"dimension": "dimension", "not_": "not", "tag": "tag"},
)
class ConsumptionBudgetManagementGroupFilter:
    def __init__(
        self,
        *,
        dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupFilterDimension", typing.Dict[str, typing.Any]]]]] = None,
        not_: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilterNot", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupFilterTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#not ConsumptionBudgetManagementGroup#not}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        if isinstance(not_, dict):
            not_ = ConsumptionBudgetManagementGroupFilterNot(**not_)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilter.__init__)
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument not_", value=not_, expected_type=type_hints["not_"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dimension is not None:
            self._values["dimension"] = dimension
        if not_ is not None:
            self._values["not_"] = not_
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def dimension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterDimension"]]]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterDimension"]]], result)

    @builtins.property
    def not_(self) -> typing.Optional["ConsumptionBudgetManagementGroupFilterNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#not ConsumptionBudgetManagementGroup#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilterNot"], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetManagementGroupFilterDimension:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterDimension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilterDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupFilterDimensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterDimensionList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterDimensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetManagementGroupFilterDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterDimensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetManagementGroupFilterDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetManagementGroupFilterDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterDimensionOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterDimensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterDimension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterDimension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterDimension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNot",
    jsii_struct_bases=[],
    name_mapping={"dimension": "dimension", "tag": "tag"},
)
class ConsumptionBudgetManagementGroupFilterNot:
    def __init__(
        self,
        *,
        dimension: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilterNotDimension", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union["ConsumptionBudgetManagementGroupFilterNotTag", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        if isinstance(dimension, dict):
            dimension = ConsumptionBudgetManagementGroupFilterNotDimension(**dimension)
        if isinstance(tag, dict):
            tag = ConsumptionBudgetManagementGroupFilterNotTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNot.__init__)
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dimension is not None:
            self._values["dimension"] = dimension
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def dimension(
        self,
    ) -> typing.Optional["ConsumptionBudgetManagementGroupFilterNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilterNotDimension"], result)

    @builtins.property
    def tag(self) -> typing.Optional["ConsumptionBudgetManagementGroupFilterNotTag"]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilterNotTag"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilterNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNotDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetManagementGroupFilterNotDimension:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNotDimension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilterNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetManagementGroupFilterNotDimension]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilterNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetManagementGroupFilterNotDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetManagementGroupFilterNotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNotOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNotOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        value = ConsumptionBudgetManagementGroupFilterNotDimension(
            name=name, values=values, operator=operator
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        value = ConsumptionBudgetManagementGroupFilterNotTag(
            name=name, values=values, operator=operator
        )

        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(
        self,
    ) -> ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference:
        return typing.cast(ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "ConsumptionBudgetManagementGroupFilterNotTagOutputReference":
        return typing.cast("ConsumptionBudgetManagementGroupFilterNotTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[ConsumptionBudgetManagementGroupFilterNotDimension]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilterNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional["ConsumptionBudgetManagementGroupFilterNotTag"]:
        return typing.cast(typing.Optional["ConsumptionBudgetManagementGroupFilterNotTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetManagementGroupFilterNot]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilterNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetManagementGroupFilterNot],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNotTag",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetManagementGroupFilterNotTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNotTag.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilterNotTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupFilterNotTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterNotTagOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterNotTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotTagOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotTagOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetManagementGroupFilterNotTag]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilterNotTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetManagementGroupFilterNotTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterNotTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetManagementGroupFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ConsumptionBudgetManagementGroupFilterDimension, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterOutputReference.put_dimension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        dimension: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterNotDimension, typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterNotTag, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#dimension ConsumptionBudgetManagementGroup#dimension}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#tag ConsumptionBudgetManagementGroup#tag}
        '''
        value = ConsumptionBudgetManagementGroupFilterNot(dimension=dimension, tag=tag)

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetManagementGroupFilterTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterOutputReference.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetNot")
    def reset_not(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNot", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> ConsumptionBudgetManagementGroupFilterDimensionList:
        return typing.cast(ConsumptionBudgetManagementGroupFilterDimensionList, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> ConsumptionBudgetManagementGroupFilterNotOutputReference:
        return typing.cast(ConsumptionBudgetManagementGroupFilterNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "ConsumptionBudgetManagementGroupFilterTagList":
        return typing.cast("ConsumptionBudgetManagementGroupFilterTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterDimension]]], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[ConsumptionBudgetManagementGroupFilterNot]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilterNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetManagementGroupFilterTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConsumptionBudgetManagementGroupFilter]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetManagementGroupFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterTag",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetManagementGroupFilterTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterTag.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#name ConsumptionBudgetManagementGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#values ConsumptionBudgetManagementGroup#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupFilterTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupFilterTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterTagList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetManagementGroupFilterTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetManagementGroupFilterTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupFilterTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetManagementGroupFilterTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupFilterTagOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupFilterTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupFilterTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupFilterTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupNotification",
    jsii_struct_bases=[],
    name_mapping={
        "contact_emails": "contactEmails",
        "operator": "operator",
        "threshold": "threshold",
        "enabled": "enabled",
        "threshold_type": "thresholdType",
    },
)
class ConsumptionBudgetManagementGroupNotification:
    def __init__(
        self,
        *,
        contact_emails: typing.Sequence[builtins.str],
        operator: builtins.str,
        threshold: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threshold_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param contact_emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#contact_emails ConsumptionBudgetManagementGroup#contact_emails}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#threshold ConsumptionBudgetManagementGroup#threshold}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#enabled ConsumptionBudgetManagementGroup#enabled}.
        :param threshold_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#threshold_type ConsumptionBudgetManagementGroup#threshold_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupNotification.__init__)
            check_type(argname="argument contact_emails", value=contact_emails, expected_type=type_hints["contact_emails"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "contact_emails": contact_emails,
            "operator": operator,
            "threshold": threshold,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if threshold_type is not None:
            self._values["threshold_type"] = threshold_type

    @builtins.property
    def contact_emails(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#contact_emails ConsumptionBudgetManagementGroup#contact_emails}.'''
        result = self._values.get("contact_emails")
        assert result is not None, "Required property 'contact_emails' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#operator ConsumptionBudgetManagementGroup#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#threshold ConsumptionBudgetManagementGroup#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#enabled ConsumptionBudgetManagementGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def threshold_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#threshold_type ConsumptionBudgetManagementGroup#threshold_type}.'''
        result = self._values.get("threshold_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupNotificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupNotificationList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupNotificationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetManagementGroupNotificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupNotificationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetManagementGroupNotificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupNotification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupNotification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetManagementGroupNotification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetManagementGroupNotificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupNotificationOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupNotificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetThresholdType")
    def reset_threshold_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdType", []))

    @builtins.property
    @jsii.member(jsii_name="contactEmailsInput")
    def contact_emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contactEmailsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTypeInput")
    def threshold_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contactEmails")
    def contact_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contactEmails"))

    @contact_emails.setter
    def contact_emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "contact_emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactEmails", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdType")
    def threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdType"))

    @threshold_type.setter
    def threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "threshold_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetManagementGroupNotification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetManagementGroupNotification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupNotification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupNotificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupTimePeriod",
    jsii_struct_bases=[],
    name_mapping={"start_date": "startDate", "end_date": "endDate"},
)
class ConsumptionBudgetManagementGroupTimePeriod:
    def __init__(
        self,
        *,
        start_date: builtins.str,
        end_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#start_date ConsumptionBudgetManagementGroup#start_date}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#end_date ConsumptionBudgetManagementGroup#end_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupTimePeriod.__init__)
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "start_date": start_date,
        }
        if end_date is not None:
            self._values["end_date"] = end_date

    @builtins.property
    def start_date(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#start_date ConsumptionBudgetManagementGroup#start_date}.'''
        result = self._values.get("start_date")
        assert result is not None, "Required property 'start_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#end_date ConsumptionBudgetManagementGroup#end_date}.'''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupTimePeriod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupTimePeriodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupTimePeriodOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupTimePeriodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndDate")
    def reset_end_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndDate", []))

    @builtins.property
    @jsii.member(jsii_name="endDateInput")
    def end_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDateInput"))

    @builtins.property
    @jsii.member(jsii_name="startDateInput")
    def start_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDateInput"))

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimePeriodOutputReference, "end_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value)

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimePeriodOutputReference, "start_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetManagementGroupTimePeriod]:
        return typing.cast(typing.Optional[ConsumptionBudgetManagementGroupTimePeriod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetManagementGroupTimePeriod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimePeriodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ConsumptionBudgetManagementGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#create ConsumptionBudgetManagementGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#delete ConsumptionBudgetManagementGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#read ConsumptionBudgetManagementGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#update ConsumptionBudgetManagementGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#create ConsumptionBudgetManagementGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#delete ConsumptionBudgetManagementGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#read ConsumptionBudgetManagementGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_management_group#update ConsumptionBudgetManagementGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetManagementGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetManagementGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetManagementGroup.ConsumptionBudgetManagementGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetManagementGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetManagementGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetManagementGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetManagementGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetManagementGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConsumptionBudgetManagementGroup",
    "ConsumptionBudgetManagementGroupConfig",
    "ConsumptionBudgetManagementGroupFilter",
    "ConsumptionBudgetManagementGroupFilterDimension",
    "ConsumptionBudgetManagementGroupFilterDimensionList",
    "ConsumptionBudgetManagementGroupFilterDimensionOutputReference",
    "ConsumptionBudgetManagementGroupFilterNot",
    "ConsumptionBudgetManagementGroupFilterNotDimension",
    "ConsumptionBudgetManagementGroupFilterNotDimensionOutputReference",
    "ConsumptionBudgetManagementGroupFilterNotOutputReference",
    "ConsumptionBudgetManagementGroupFilterNotTag",
    "ConsumptionBudgetManagementGroupFilterNotTagOutputReference",
    "ConsumptionBudgetManagementGroupFilterOutputReference",
    "ConsumptionBudgetManagementGroupFilterTag",
    "ConsumptionBudgetManagementGroupFilterTagList",
    "ConsumptionBudgetManagementGroupFilterTagOutputReference",
    "ConsumptionBudgetManagementGroupNotification",
    "ConsumptionBudgetManagementGroupNotificationList",
    "ConsumptionBudgetManagementGroupNotificationOutputReference",
    "ConsumptionBudgetManagementGroupTimePeriod",
    "ConsumptionBudgetManagementGroupTimePeriodOutputReference",
    "ConsumptionBudgetManagementGroupTimeouts",
    "ConsumptionBudgetManagementGroupTimeoutsOutputReference",
]

publication.publish()
