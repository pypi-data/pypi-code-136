'''
# `azurerm_logic_app_trigger_recurrence`

Refer to the Terraform Registory for docs: [`azurerm_logic_app_trigger_recurrence`](https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence).
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


class LogicAppTriggerRecurrence(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrence",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence azurerm_logic_app_trigger_recurrence}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        frequency: builtins.str,
        interval: jsii.Number,
        logic_app_id: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["LogicAppTriggerRecurrenceSchedule", typing.Dict[str, typing.Any]]] = None,
        start_time: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LogicAppTriggerRecurrenceTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence azurerm_logic_app_trigger_recurrence} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#frequency LogicAppTriggerRecurrence#frequency}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#interval LogicAppTriggerRecurrence#interval}.
        :param logic_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#logic_app_id LogicAppTriggerRecurrence#logic_app_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#name LogicAppTriggerRecurrence#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#id LogicAppTriggerRecurrence#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#schedule LogicAppTriggerRecurrence#schedule}
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#start_time LogicAppTriggerRecurrence#start_time}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#timeouts LogicAppTriggerRecurrence#timeouts}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#time_zone LogicAppTriggerRecurrence#time_zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrence.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogicAppTriggerRecurrenceConfig(
            frequency=frequency,
            interval=interval,
            logic_app_id=logic_app_id,
            name=name,
            id=id,
            schedule=schedule,
            start_time=start_time,
            timeouts=timeouts,
            time_zone=time_zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        at_these_hours: typing.Optional[typing.Sequence[jsii.Number]] = None,
        at_these_minutes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        on_these_days: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param at_these_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_hours LogicAppTriggerRecurrence#at_these_hours}.
        :param at_these_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_minutes LogicAppTriggerRecurrence#at_these_minutes}.
        :param on_these_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#on_these_days LogicAppTriggerRecurrence#on_these_days}.
        '''
        value = LogicAppTriggerRecurrenceSchedule(
            at_these_hours=at_these_hours,
            at_these_minutes=at_these_minutes,
            on_these_days=on_these_days,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#create LogicAppTriggerRecurrence#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#delete LogicAppTriggerRecurrence#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#read LogicAppTriggerRecurrence#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#update LogicAppTriggerRecurrence#update}.
        '''
        value = LogicAppTriggerRecurrenceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "LogicAppTriggerRecurrenceScheduleOutputReference":
        return typing.cast("LogicAppTriggerRecurrenceScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LogicAppTriggerRecurrenceTimeoutsOutputReference":
        return typing.cast("LogicAppTriggerRecurrenceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="logicAppIdInput")
    def logic_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["LogicAppTriggerRecurrenceSchedule"]:
        return typing.cast(typing.Optional["LogicAppTriggerRecurrenceSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LogicAppTriggerRecurrenceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LogicAppTriggerRecurrenceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="logicAppId")
    def logic_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logicAppId"))

    @logic_app_id.setter
    def logic_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "logic_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logicAppId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrence, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrenceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "frequency": "frequency",
        "interval": "interval",
        "logic_app_id": "logicAppId",
        "name": "name",
        "id": "id",
        "schedule": "schedule",
        "start_time": "startTime",
        "timeouts": "timeouts",
        "time_zone": "timeZone",
    },
)
class LogicAppTriggerRecurrenceConfig(cdktf.TerraformMetaArguments):
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
        frequency: builtins.str,
        interval: jsii.Number,
        logic_app_id: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["LogicAppTriggerRecurrenceSchedule", typing.Dict[str, typing.Any]]] = None,
        start_time: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LogicAppTriggerRecurrenceTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#frequency LogicAppTriggerRecurrence#frequency}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#interval LogicAppTriggerRecurrence#interval}.
        :param logic_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#logic_app_id LogicAppTriggerRecurrence#logic_app_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#name LogicAppTriggerRecurrence#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#id LogicAppTriggerRecurrence#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#schedule LogicAppTriggerRecurrence#schedule}
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#start_time LogicAppTriggerRecurrence#start_time}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#timeouts LogicAppTriggerRecurrence#timeouts}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#time_zone LogicAppTriggerRecurrence#time_zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schedule, dict):
            schedule = LogicAppTriggerRecurrenceSchedule(**schedule)
        if isinstance(timeouts, dict):
            timeouts = LogicAppTriggerRecurrenceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrenceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument logic_app_id", value=logic_app_id, expected_type=type_hints["logic_app_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency": frequency,
            "interval": interval,
            "logic_app_id": logic_app_id,
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
        if id is not None:
            self._values["id"] = id
        if schedule is not None:
            self._values["schedule"] = schedule
        if start_time is not None:
            self._values["start_time"] = start_time
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if time_zone is not None:
            self._values["time_zone"] = time_zone

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
    def frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#frequency LogicAppTriggerRecurrence#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#interval LogicAppTriggerRecurrence#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def logic_app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#logic_app_id LogicAppTriggerRecurrence#logic_app_id}.'''
        result = self._values.get("logic_app_id")
        assert result is not None, "Required property 'logic_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#name LogicAppTriggerRecurrence#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#id LogicAppTriggerRecurrence#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["LogicAppTriggerRecurrenceSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#schedule LogicAppTriggerRecurrence#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["LogicAppTriggerRecurrenceSchedule"], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#start_time LogicAppTriggerRecurrence#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LogicAppTriggerRecurrenceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#timeouts LogicAppTriggerRecurrence#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LogicAppTriggerRecurrenceTimeouts"], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#time_zone LogicAppTriggerRecurrence#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppTriggerRecurrenceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrenceSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "at_these_hours": "atTheseHours",
        "at_these_minutes": "atTheseMinutes",
        "on_these_days": "onTheseDays",
    },
)
class LogicAppTriggerRecurrenceSchedule:
    def __init__(
        self,
        *,
        at_these_hours: typing.Optional[typing.Sequence[jsii.Number]] = None,
        at_these_minutes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        on_these_days: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param at_these_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_hours LogicAppTriggerRecurrence#at_these_hours}.
        :param at_these_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_minutes LogicAppTriggerRecurrence#at_these_minutes}.
        :param on_these_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#on_these_days LogicAppTriggerRecurrence#on_these_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrenceSchedule.__init__)
            check_type(argname="argument at_these_hours", value=at_these_hours, expected_type=type_hints["at_these_hours"])
            check_type(argname="argument at_these_minutes", value=at_these_minutes, expected_type=type_hints["at_these_minutes"])
            check_type(argname="argument on_these_days", value=on_these_days, expected_type=type_hints["on_these_days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if at_these_hours is not None:
            self._values["at_these_hours"] = at_these_hours
        if at_these_minutes is not None:
            self._values["at_these_minutes"] = at_these_minutes
        if on_these_days is not None:
            self._values["on_these_days"] = on_these_days

    @builtins.property
    def at_these_hours(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_hours LogicAppTriggerRecurrence#at_these_hours}.'''
        result = self._values.get("at_these_hours")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def at_these_minutes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#at_these_minutes LogicAppTriggerRecurrence#at_these_minutes}.'''
        result = self._values.get("at_these_minutes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def on_these_days(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#on_these_days LogicAppTriggerRecurrence#on_these_days}.'''
        result = self._values.get("on_these_days")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppTriggerRecurrenceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppTriggerRecurrenceScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrenceScheduleOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrenceScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAtTheseHours")
    def reset_at_these_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAtTheseHours", []))

    @jsii.member(jsii_name="resetAtTheseMinutes")
    def reset_at_these_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAtTheseMinutes", []))

    @jsii.member(jsii_name="resetOnTheseDays")
    def reset_on_these_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnTheseDays", []))

    @builtins.property
    @jsii.member(jsii_name="atTheseHoursInput")
    def at_these_hours_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "atTheseHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="atTheseMinutesInput")
    def at_these_minutes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "atTheseMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="onTheseDaysInput")
    def on_these_days_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "onTheseDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="atTheseHours")
    def at_these_hours(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "atTheseHours"))

    @at_these_hours.setter
    def at_these_hours(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceScheduleOutputReference, "at_these_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atTheseHours", value)

    @builtins.property
    @jsii.member(jsii_name="atTheseMinutes")
    def at_these_minutes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "atTheseMinutes"))

    @at_these_minutes.setter
    def at_these_minutes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceScheduleOutputReference, "at_these_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atTheseMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="onTheseDays")
    def on_these_days(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "onTheseDays"))

    @on_these_days.setter
    def on_these_days(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceScheduleOutputReference, "on_these_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onTheseDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppTriggerRecurrenceSchedule]:
        return typing.cast(typing.Optional[LogicAppTriggerRecurrenceSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppTriggerRecurrenceSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrenceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LogicAppTriggerRecurrenceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#create LogicAppTriggerRecurrence#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#delete LogicAppTriggerRecurrence#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#read LogicAppTriggerRecurrence#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#update LogicAppTriggerRecurrence#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrenceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#create LogicAppTriggerRecurrence#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#delete LogicAppTriggerRecurrence#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#read LogicAppTriggerRecurrence#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence#update LogicAppTriggerRecurrence#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppTriggerRecurrenceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppTriggerRecurrenceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppTriggerRecurrence.LogicAppTriggerRecurrenceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppTriggerRecurrenceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppTriggerRecurrenceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppTriggerRecurrenceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppTriggerRecurrenceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppTriggerRecurrenceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogicAppTriggerRecurrence",
    "LogicAppTriggerRecurrenceConfig",
    "LogicAppTriggerRecurrenceSchedule",
    "LogicAppTriggerRecurrenceScheduleOutputReference",
    "LogicAppTriggerRecurrenceTimeouts",
    "LogicAppTriggerRecurrenceTimeoutsOutputReference",
]

publication.publish()
