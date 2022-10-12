'''
# `azurerm_consumption_budget_subscription`

Refer to the Terraform Registory for docs: [`azurerm_consumption_budget_subscription`](https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription).
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


class ConsumptionBudgetSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription azurerm_consumption_budget_subscription}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        amount: jsii.Number,
        name: builtins.str,
        notification: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionNotification", typing.Dict[str, typing.Any]]]],
        subscription_id: builtins.str,
        time_period: typing.Union["ConsumptionBudgetSubscriptionTimePeriod", typing.Dict[str, typing.Any]],
        etag: typing.Optional[builtins.str] = None,
        filter: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        time_grain: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription azurerm_consumption_budget_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#amount ConsumptionBudgetSubscription#amount}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#notification ConsumptionBudgetSubscription#notification}
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#subscription_id ConsumptionBudgetSubscription#subscription_id}.
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_period ConsumptionBudgetSubscription#time_period}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#etag ConsumptionBudgetSubscription#etag}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#filter ConsumptionBudgetSubscription#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#id ConsumptionBudgetSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param time_grain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_grain ConsumptionBudgetSubscription#time_grain}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#timeouts ConsumptionBudgetSubscription#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConsumptionBudgetSubscriptionConfig(
            amount=amount,
            name=name,
            notification=notification,
            subscription_id=subscription_id,
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
        dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionFilterDimension", typing.Dict[str, typing.Any]]]]] = None,
        not_: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilterNot", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionFilterTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#not ConsumptionBudgetSubscription#not}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        value = ConsumptionBudgetSubscriptionFilter(
            dimension=dimension, not_=not_, tag=tag
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putNotification")
    def put_notification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionNotification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscription.put_notification)
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#create ConsumptionBudgetSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#delete ConsumptionBudgetSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#read ConsumptionBudgetSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#update ConsumptionBudgetSubscription#update}.
        '''
        value = ConsumptionBudgetSubscriptionTimeouts(
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
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#start_date ConsumptionBudgetSubscription#start_date}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#end_date ConsumptionBudgetSubscription#end_date}.
        '''
        value = ConsumptionBudgetSubscriptionTimePeriod(
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
    def filter(self) -> "ConsumptionBudgetSubscriptionFilterOutputReference":
        return typing.cast("ConsumptionBudgetSubscriptionFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="notification")
    def notification(self) -> "ConsumptionBudgetSubscriptionNotificationList":
        return typing.cast("ConsumptionBudgetSubscriptionNotificationList", jsii.get(self, "notification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConsumptionBudgetSubscriptionTimeoutsOutputReference":
        return typing.cast("ConsumptionBudgetSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="timePeriod")
    def time_period(self) -> "ConsumptionBudgetSubscriptionTimePeriodOutputReference":
        return typing.cast("ConsumptionBudgetSubscriptionTimePeriodOutputReference", jsii.get(self, "timePeriod"))

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
    def filter_input(self) -> typing.Optional["ConsumptionBudgetSubscriptionFilter"]:
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationInput")
    def notification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionNotification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionNotification"]]], jsii.get(self, "notificationInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeGrainInput")
    def time_grain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeGrainInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ConsumptionBudgetSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ConsumptionBudgetSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodInput")
    def time_period_input(
        self,
    ) -> typing.Optional["ConsumptionBudgetSubscriptionTimePeriod"]:
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionTimePeriod"], jsii.get(self, "timePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="amount")
    def amount(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "amount"))

    @amount.setter
    def amount(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "amount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amount", value)

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @etag.setter
    def etag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "etag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "etag", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "subscription_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="timeGrain")
    def time_grain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeGrain"))

    @time_grain.setter
    def time_grain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscription, "time_grain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeGrain", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionConfig",
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
        "name": "name",
        "notification": "notification",
        "subscription_id": "subscriptionId",
        "time_period": "timePeriod",
        "etag": "etag",
        "filter": "filter",
        "id": "id",
        "time_grain": "timeGrain",
        "timeouts": "timeouts",
    },
)
class ConsumptionBudgetSubscriptionConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        notification: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionNotification", typing.Dict[str, typing.Any]]]],
        subscription_id: builtins.str,
        time_period: typing.Union["ConsumptionBudgetSubscriptionTimePeriod", typing.Dict[str, typing.Any]],
        etag: typing.Optional[builtins.str] = None,
        filter: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        time_grain: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#amount ConsumptionBudgetSubscription#amount}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#notification ConsumptionBudgetSubscription#notification}
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#subscription_id ConsumptionBudgetSubscription#subscription_id}.
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_period ConsumptionBudgetSubscription#time_period}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#etag ConsumptionBudgetSubscription#etag}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#filter ConsumptionBudgetSubscription#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#id ConsumptionBudgetSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param time_grain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_grain ConsumptionBudgetSubscription#time_grain}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#timeouts ConsumptionBudgetSubscription#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(time_period, dict):
            time_period = ConsumptionBudgetSubscriptionTimePeriod(**time_period)
        if isinstance(filter, dict):
            filter = ConsumptionBudgetSubscriptionFilter(**filter)
        if isinstance(timeouts, dict):
            timeouts = ConsumptionBudgetSubscriptionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notification", value=notification, expected_type=type_hints["notification"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument time_grain", value=time_grain, expected_type=type_hints["time_grain"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "amount": amount,
            "name": name,
            "notification": notification,
            "subscription_id": subscription_id,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#amount ConsumptionBudgetSubscription#amount}.'''
        result = self._values.get("amount")
        assert result is not None, "Required property 'amount' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionNotification"]]:
        '''notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#notification ConsumptionBudgetSubscription#notification}
        '''
        result = self._values.get("notification")
        assert result is not None, "Required property 'notification' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionNotification"]], result)

    @builtins.property
    def subscription_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#subscription_id ConsumptionBudgetSubscription#subscription_id}.'''
        result = self._values.get("subscription_id")
        assert result is not None, "Required property 'subscription_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_period(self) -> "ConsumptionBudgetSubscriptionTimePeriod":
        '''time_period block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_period ConsumptionBudgetSubscription#time_period}
        '''
        result = self._values.get("time_period")
        assert result is not None, "Required property 'time_period' is missing"
        return typing.cast("ConsumptionBudgetSubscriptionTimePeriod", result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#etag ConsumptionBudgetSubscription#etag}.'''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional["ConsumptionBudgetSubscriptionFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#filter ConsumptionBudgetSubscription#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#id ConsumptionBudgetSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_grain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#time_grain ConsumptionBudgetSubscription#time_grain}.'''
        result = self._values.get("time_grain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConsumptionBudgetSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#timeouts ConsumptionBudgetSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilter",
    jsii_struct_bases=[],
    name_mapping={"dimension": "dimension", "not_": "not", "tag": "tag"},
)
class ConsumptionBudgetSubscriptionFilter:
    def __init__(
        self,
        *,
        dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionFilterDimension", typing.Dict[str, typing.Any]]]]] = None,
        not_: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilterNot", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionFilterTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#not ConsumptionBudgetSubscription#not}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        if isinstance(not_, dict):
            not_ = ConsumptionBudgetSubscriptionFilterNot(**not_)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilter.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterDimension"]]]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterDimension"]]], result)

    @builtins.property
    def not_(self) -> typing.Optional["ConsumptionBudgetSubscriptionFilterNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#not ConsumptionBudgetSubscription#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilterNot"], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetSubscriptionFilterDimension:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterDimension.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilterDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionFilterDimensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterDimensionList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterDimensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetSubscriptionFilterDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterDimensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetSubscriptionFilterDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetSubscriptionFilterDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterDimensionOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterDimensionOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterDimension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterDimension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterDimension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNot",
    jsii_struct_bases=[],
    name_mapping={"dimension": "dimension", "tag": "tag"},
)
class ConsumptionBudgetSubscriptionFilterNot:
    def __init__(
        self,
        *,
        dimension: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilterNotDimension", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union["ConsumptionBudgetSubscriptionFilterNotTag", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        if isinstance(dimension, dict):
            dimension = ConsumptionBudgetSubscriptionFilterNotDimension(**dimension)
        if isinstance(tag, dict):
            tag = ConsumptionBudgetSubscriptionFilterNotTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNot.__init__)
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
    ) -> typing.Optional["ConsumptionBudgetSubscriptionFilterNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilterNotDimension"], result)

    @builtins.property
    def tag(self) -> typing.Optional["ConsumptionBudgetSubscriptionFilterNotTag"]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilterNotTag"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilterNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNotDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetSubscriptionFilterNotDimension:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNotDimension.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilterNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetSubscriptionFilterNotDimension]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilterNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetSubscriptionFilterNotDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetSubscriptionFilterNotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNotOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNotOutputReference.__init__)
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        value = ConsumptionBudgetSubscriptionFilterNotDimension(
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        value = ConsumptionBudgetSubscriptionFilterNotTag(
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
    ) -> ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference:
        return typing.cast(ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "ConsumptionBudgetSubscriptionFilterNotTagOutputReference":
        return typing.cast("ConsumptionBudgetSubscriptionFilterNotTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[ConsumptionBudgetSubscriptionFilterNotDimension]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilterNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional["ConsumptionBudgetSubscriptionFilterNotTag"]:
        return typing.cast(typing.Optional["ConsumptionBudgetSubscriptionFilterNotTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConsumptionBudgetSubscriptionFilterNot]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilterNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetSubscriptionFilterNot],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNotTag",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetSubscriptionFilterNotTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNotTag.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilterNotTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionFilterNotTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterNotTagOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterNotTagOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotTagOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotTagOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetSubscriptionFilterNotTag]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilterNotTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetSubscriptionFilterNotTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterNotTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetSubscriptionFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ConsumptionBudgetSubscriptionFilterDimension, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterOutputReference.put_dimension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        dimension: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterNotDimension, typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterNotTag, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#dimension ConsumptionBudgetSubscription#dimension}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#tag ConsumptionBudgetSubscription#tag}
        '''
        value = ConsumptionBudgetSubscriptionFilterNot(dimension=dimension, tag=tag)

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsumptionBudgetSubscriptionFilterTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterOutputReference.put_tag)
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
    def dimension(self) -> ConsumptionBudgetSubscriptionFilterDimensionList:
        return typing.cast(ConsumptionBudgetSubscriptionFilterDimensionList, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> ConsumptionBudgetSubscriptionFilterNotOutputReference:
        return typing.cast(ConsumptionBudgetSubscriptionFilterNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "ConsumptionBudgetSubscriptionFilterTagList":
        return typing.cast("ConsumptionBudgetSubscriptionFilterTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterDimension]]], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[ConsumptionBudgetSubscriptionFilterNot]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilterNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsumptionBudgetSubscriptionFilterTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConsumptionBudgetSubscriptionFilter]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetSubscriptionFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterTag",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values", "operator": "operator"},
)
class ConsumptionBudgetSubscriptionFilterTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterTag.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#name ConsumptionBudgetSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#values ConsumptionBudgetSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionFilterTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionFilterTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterTagList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetSubscriptionFilterTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetSubscriptionFilterTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionFilterTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetSubscriptionFilterTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionFilterTagOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionFilterTagOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionFilterTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionFilterTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionNotification",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "threshold": "threshold",
        "contact_emails": "contactEmails",
        "contact_groups": "contactGroups",
        "contact_roles": "contactRoles",
        "enabled": "enabled",
        "threshold_type": "thresholdType",
    },
)
class ConsumptionBudgetSubscriptionNotification:
    def __init__(
        self,
        *,
        operator: builtins.str,
        threshold: jsii.Number,
        contact_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        contact_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        contact_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threshold_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#threshold ConsumptionBudgetSubscription#threshold}.
        :param contact_emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_emails ConsumptionBudgetSubscription#contact_emails}.
        :param contact_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_groups ConsumptionBudgetSubscription#contact_groups}.
        :param contact_roles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_roles ConsumptionBudgetSubscription#contact_roles}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#enabled ConsumptionBudgetSubscription#enabled}.
        :param threshold_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#threshold_type ConsumptionBudgetSubscription#threshold_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionNotification.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument contact_emails", value=contact_emails, expected_type=type_hints["contact_emails"])
            check_type(argname="argument contact_groups", value=contact_groups, expected_type=type_hints["contact_groups"])
            check_type(argname="argument contact_roles", value=contact_roles, expected_type=type_hints["contact_roles"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "threshold": threshold,
        }
        if contact_emails is not None:
            self._values["contact_emails"] = contact_emails
        if contact_groups is not None:
            self._values["contact_groups"] = contact_groups
        if contact_roles is not None:
            self._values["contact_roles"] = contact_roles
        if enabled is not None:
            self._values["enabled"] = enabled
        if threshold_type is not None:
            self._values["threshold_type"] = threshold_type

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#operator ConsumptionBudgetSubscription#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#threshold ConsumptionBudgetSubscription#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def contact_emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_emails ConsumptionBudgetSubscription#contact_emails}.'''
        result = self._values.get("contact_emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def contact_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_groups ConsumptionBudgetSubscription#contact_groups}.'''
        result = self._values.get("contact_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def contact_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#contact_roles ConsumptionBudgetSubscription#contact_roles}.'''
        result = self._values.get("contact_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#enabled ConsumptionBudgetSubscription#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def threshold_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#threshold_type ConsumptionBudgetSubscription#threshold_type}.'''
        result = self._values.get("threshold_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionNotificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionNotificationList",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionNotificationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConsumptionBudgetSubscriptionNotificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionNotificationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConsumptionBudgetSubscriptionNotificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionNotification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionNotification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConsumptionBudgetSubscriptionNotification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConsumptionBudgetSubscriptionNotificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionNotificationOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionNotificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContactEmails")
    def reset_contact_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactEmails", []))

    @jsii.member(jsii_name="resetContactGroups")
    def reset_contact_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactGroups", []))

    @jsii.member(jsii_name="resetContactRoles")
    def reset_contact_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactRoles", []))

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
    @jsii.member(jsii_name="contactGroupsInput")
    def contact_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contactGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="contactRolesInput")
    def contact_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contactRolesInput"))

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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "contact_emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactEmails", value)

    @builtins.property
    @jsii.member(jsii_name="contactGroups")
    def contact_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contactGroups"))

    @contact_groups.setter
    def contact_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "contact_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactGroups", value)

    @builtins.property
    @jsii.member(jsii_name="contactRoles")
    def contact_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contactRoles"))

    @contact_roles.setter
    def contact_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "contact_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactRoles", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdType")
    def threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdType"))

    @threshold_type.setter
    def threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "threshold_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetSubscriptionNotification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetSubscriptionNotification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionNotification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionNotificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionTimePeriod",
    jsii_struct_bases=[],
    name_mapping={"start_date": "startDate", "end_date": "endDate"},
)
class ConsumptionBudgetSubscriptionTimePeriod:
    def __init__(
        self,
        *,
        start_date: builtins.str,
        end_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#start_date ConsumptionBudgetSubscription#start_date}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#end_date ConsumptionBudgetSubscription#end_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionTimePeriod.__init__)
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "start_date": start_date,
        }
        if end_date is not None:
            self._values["end_date"] = end_date

    @builtins.property
    def start_date(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#start_date ConsumptionBudgetSubscription#start_date}.'''
        result = self._values.get("start_date")
        assert result is not None, "Required property 'start_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#end_date ConsumptionBudgetSubscription#end_date}.'''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionTimePeriod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionTimePeriodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionTimePeriodOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionTimePeriodOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimePeriodOutputReference, "end_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value)

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimePeriodOutputReference, "start_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConsumptionBudgetSubscriptionTimePeriod]:
        return typing.cast(typing.Optional[ConsumptionBudgetSubscriptionTimePeriod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConsumptionBudgetSubscriptionTimePeriod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimePeriodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ConsumptionBudgetSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#create ConsumptionBudgetSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#delete ConsumptionBudgetSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#read ConsumptionBudgetSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#update ConsumptionBudgetSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#create ConsumptionBudgetSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#delete ConsumptionBudgetSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#read ConsumptionBudgetSubscription#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/consumption_budget_subscription#update ConsumptionBudgetSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumptionBudgetSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsumptionBudgetSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.consumptionBudgetSubscription.ConsumptionBudgetSubscriptionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ConsumptionBudgetSubscriptionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsumptionBudgetSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsumptionBudgetSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsumptionBudgetSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsumptionBudgetSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConsumptionBudgetSubscription",
    "ConsumptionBudgetSubscriptionConfig",
    "ConsumptionBudgetSubscriptionFilter",
    "ConsumptionBudgetSubscriptionFilterDimension",
    "ConsumptionBudgetSubscriptionFilterDimensionList",
    "ConsumptionBudgetSubscriptionFilterDimensionOutputReference",
    "ConsumptionBudgetSubscriptionFilterNot",
    "ConsumptionBudgetSubscriptionFilterNotDimension",
    "ConsumptionBudgetSubscriptionFilterNotDimensionOutputReference",
    "ConsumptionBudgetSubscriptionFilterNotOutputReference",
    "ConsumptionBudgetSubscriptionFilterNotTag",
    "ConsumptionBudgetSubscriptionFilterNotTagOutputReference",
    "ConsumptionBudgetSubscriptionFilterOutputReference",
    "ConsumptionBudgetSubscriptionFilterTag",
    "ConsumptionBudgetSubscriptionFilterTagList",
    "ConsumptionBudgetSubscriptionFilterTagOutputReference",
    "ConsumptionBudgetSubscriptionNotification",
    "ConsumptionBudgetSubscriptionNotificationList",
    "ConsumptionBudgetSubscriptionNotificationOutputReference",
    "ConsumptionBudgetSubscriptionTimePeriod",
    "ConsumptionBudgetSubscriptionTimePeriodOutputReference",
    "ConsumptionBudgetSubscriptionTimeouts",
    "ConsumptionBudgetSubscriptionTimeoutsOutputReference",
]

publication.publish()
