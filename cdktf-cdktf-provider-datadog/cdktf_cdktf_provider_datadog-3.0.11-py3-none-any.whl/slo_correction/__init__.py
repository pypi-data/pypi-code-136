'''
# `datadog_slo_correction`

Refer to the Terraform Registory for docs: [`datadog_slo_correction`](https://www.terraform.io/docs/providers/datadog/r/slo_correction).
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


class SloCorrection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.sloCorrection.SloCorrection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction datadog_slo_correction}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        category: builtins.str,
        slo_id: builtins.str,
        start: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        duration: typing.Optional[jsii.Number] = None,
        end: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        rrule: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction datadog_slo_correction} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param category: Category the SLO correction belongs to. Valid values are ``Scheduled Maintenance``, ``Outside Business Hours``, ``Deployment``, ``Other``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#category SloCorrection#category}
        :param slo_id: ID of the SLO that this correction will be applied to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#slo_id SloCorrection#slo_id}
        :param start: Starting time of the correction in epoch seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#start SloCorrection#start}
        :param description: Description of the correction being made. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#description SloCorrection#description}
        :param duration: Length of time in seconds for a specified ``rrule`` recurring SLO correction (required if specifying ``rrule``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#duration SloCorrection#duration}
        :param end: Ending time of the correction in epoch seconds. Required for one time corrections, but optional if ``rrule`` is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#end SloCorrection#end}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#id SloCorrection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rrule: Recurrence rules as defined in the iCalendar RFC 5545. Supported rules for SLO corrections are ``FREQ``, ``INTERVAL``, ``COUNT`` and ``UNTIL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#rrule SloCorrection#rrule}
        :param timezone: The timezone to display in the UI for the correction times (defaults to "UTC"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#timezone SloCorrection#timezone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SloCorrection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SloCorrectionConfig(
            category=category,
            slo_id=slo_id,
            start=start,
            description=description,
            duration=duration,
            end=end,
            id=id,
            rrule=rrule,
            timezone=timezone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetEnd")
    def reset_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnd", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRrule")
    def reset_rrule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRrule", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="rruleInput")
    def rrule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rruleInput"))

    @builtins.property
    @jsii.member(jsii_name="sloIdInput")
    def slo_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sloIdInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "category").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="rrule")
    def rrule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rrule"))

    @rrule.setter
    def rrule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "rrule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rrule", value)

    @builtins.property
    @jsii.member(jsii_name="sloId")
    def slo_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sloId"))

    @slo_id.setter
    def slo_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "slo_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sloId", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SloCorrection, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.sloCorrection.SloCorrectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "category": "category",
        "slo_id": "sloId",
        "start": "start",
        "description": "description",
        "duration": "duration",
        "end": "end",
        "id": "id",
        "rrule": "rrule",
        "timezone": "timezone",
    },
)
class SloCorrectionConfig(cdktf.TerraformMetaArguments):
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
        category: builtins.str,
        slo_id: builtins.str,
        start: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        duration: typing.Optional[jsii.Number] = None,
        end: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        rrule: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param category: Category the SLO correction belongs to. Valid values are ``Scheduled Maintenance``, ``Outside Business Hours``, ``Deployment``, ``Other``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#category SloCorrection#category}
        :param slo_id: ID of the SLO that this correction will be applied to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#slo_id SloCorrection#slo_id}
        :param start: Starting time of the correction in epoch seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#start SloCorrection#start}
        :param description: Description of the correction being made. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#description SloCorrection#description}
        :param duration: Length of time in seconds for a specified ``rrule`` recurring SLO correction (required if specifying ``rrule``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#duration SloCorrection#duration}
        :param end: Ending time of the correction in epoch seconds. Required for one time corrections, but optional if ``rrule`` is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#end SloCorrection#end}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#id SloCorrection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rrule: Recurrence rules as defined in the iCalendar RFC 5545. Supported rules for SLO corrections are ``FREQ``, ``INTERVAL``, ``COUNT`` and ``UNTIL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#rrule SloCorrection#rrule}
        :param timezone: The timezone to display in the UI for the correction times (defaults to "UTC"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#timezone SloCorrection#timezone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SloCorrectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument slo_id", value=slo_id, expected_type=type_hints["slo_id"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rrule", value=rrule, expected_type=type_hints["rrule"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[str, typing.Any] = {
            "category": category,
            "slo_id": slo_id,
            "start": start,
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
        if description is not None:
            self._values["description"] = description
        if duration is not None:
            self._values["duration"] = duration
        if end is not None:
            self._values["end"] = end
        if id is not None:
            self._values["id"] = id
        if rrule is not None:
            self._values["rrule"] = rrule
        if timezone is not None:
            self._values["timezone"] = timezone

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
    def category(self) -> builtins.str:
        '''Category the SLO correction belongs to. Valid values are ``Scheduled Maintenance``, ``Outside Business Hours``, ``Deployment``, ``Other``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#category SloCorrection#category}
        '''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slo_id(self) -> builtins.str:
        '''ID of the SLO that this correction will be applied to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#slo_id SloCorrection#slo_id}
        '''
        result = self._values.get("slo_id")
        assert result is not None, "Required property 'slo_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Starting time of the correction in epoch seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#start SloCorrection#start}
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the correction being made.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#description SloCorrection#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''Length of time in seconds for a specified ``rrule`` recurring SLO correction (required if specifying ``rrule``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#duration SloCorrection#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''Ending time of the correction in epoch seconds. Required for one time corrections, but optional if ``rrule`` is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#end SloCorrection#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#id SloCorrection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rrule(self) -> typing.Optional[builtins.str]:
        '''Recurrence rules as defined in the iCalendar RFC 5545.

        Supported rules for SLO corrections are ``FREQ``, ``INTERVAL``, ``COUNT`` and ``UNTIL``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#rrule SloCorrection#rrule}
        '''
        result = self._values.get("rrule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone to display in the UI for the correction times (defaults to "UTC").

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/slo_correction#timezone SloCorrection#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SloCorrectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SloCorrection",
    "SloCorrectionConfig",
]

publication.publish()
