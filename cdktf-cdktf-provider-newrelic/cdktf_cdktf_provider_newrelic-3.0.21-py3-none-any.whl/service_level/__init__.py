'''
# `newrelic_service_level`

Refer to the Terraform Registory for docs: [`newrelic_service_level`](https://www.terraform.io/docs/providers/newrelic/r/service_level).
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


class ServiceLevel(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevel",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/service_level newrelic_service_level}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        events: typing.Union["ServiceLevelEvents", typing.Dict[str, typing.Any]],
        guid: builtins.str,
        name: builtins.str,
        objective: typing.Union["ServiceLevelObjective", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/service_level newrelic_service_level} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param events: events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#events ServiceLevel#events}
        :param guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#guid ServiceLevel#guid}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.
        :param objective: objective block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#objective ServiceLevel#objective}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#id ServiceLevel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevel.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceLevelConfig(
            events=events,
            guid=guid,
            name=name,
            objective=objective,
            description=description,
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

    @jsii.member(jsii_name="putEvents")
    def put_events(
        self,
        *,
        account_id: jsii.Number,
        valid_events: typing.Union["ServiceLevelEventsValidEvents", typing.Dict[str, typing.Any]],
        bad_events: typing.Optional[typing.Union["ServiceLevelEventsBadEvents", typing.Dict[str, typing.Any]]] = None,
        good_events: typing.Optional[typing.Union["ServiceLevelEventsGoodEvents", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#account_id ServiceLevel#account_id}.
        :param valid_events: valid_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#valid_events ServiceLevel#valid_events}
        :param bad_events: bad_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#bad_events ServiceLevel#bad_events}
        :param good_events: good_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#good_events ServiceLevel#good_events}
        '''
        value = ServiceLevelEvents(
            account_id=account_id,
            valid_events=valid_events,
            bad_events=bad_events,
            good_events=good_events,
        )

        return typing.cast(None, jsii.invoke(self, "putEvents", [value]))

    @jsii.member(jsii_name="putObjective")
    def put_objective(
        self,
        *,
        target: jsii.Number,
        time_window: typing.Union["ServiceLevelObjectiveTimeWindow", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#target ServiceLevel#target}.
        :param time_window: time_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#time_window ServiceLevel#time_window}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.
        '''
        value = ServiceLevelObjective(
            target=target, time_window=time_window, description=description, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putObjective", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

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
    @jsii.member(jsii_name="events")
    def events(self) -> "ServiceLevelEventsOutputReference":
        return typing.cast("ServiceLevelEventsOutputReference", jsii.get(self, "events"))

    @builtins.property
    @jsii.member(jsii_name="objective")
    def objective(self) -> "ServiceLevelObjectiveOutputReference":
        return typing.cast("ServiceLevelObjectiveOutputReference", jsii.get(self, "objective"))

    @builtins.property
    @jsii.member(jsii_name="sliGuid")
    def sli_guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sliGuid"))

    @builtins.property
    @jsii.member(jsii_name="sliId")
    def sli_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sliId"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional["ServiceLevelEvents"]:
        return typing.cast(typing.Optional["ServiceLevelEvents"], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="guidInput")
    def guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guidInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectiveInput")
    def objective_input(self) -> typing.Optional["ServiceLevelObjective"]:
        return typing.cast(typing.Optional["ServiceLevelObjective"], jsii.get(self, "objectiveInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevel, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @guid.setter
    def guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevel, "guid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guid", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevel, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevel, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "events": "events",
        "guid": "guid",
        "name": "name",
        "objective": "objective",
        "description": "description",
        "id": "id",
    },
)
class ServiceLevelConfig(cdktf.TerraformMetaArguments):
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
        events: typing.Union["ServiceLevelEvents", typing.Dict[str, typing.Any]],
        guid: builtins.str,
        name: builtins.str,
        objective: typing.Union["ServiceLevelObjective", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
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
        :param events: events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#events ServiceLevel#events}
        :param guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#guid ServiceLevel#guid}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.
        :param objective: objective block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#objective ServiceLevel#objective}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#id ServiceLevel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(events, dict):
            events = ServiceLevelEvents(**events)
        if isinstance(objective, dict):
            objective = ServiceLevelObjective(**objective)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument guid", value=guid, expected_type=type_hints["guid"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument objective", value=objective, expected_type=type_hints["objective"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "events": events,
            "guid": guid,
            "name": name,
            "objective": objective,
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
    def events(self) -> "ServiceLevelEvents":
        '''events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#events ServiceLevel#events}
        '''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast("ServiceLevelEvents", result)

    @builtins.property
    def guid(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#guid ServiceLevel#guid}.'''
        result = self._values.get("guid")
        assert result is not None, "Required property 'guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def objective(self) -> "ServiceLevelObjective":
        '''objective block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#objective ServiceLevel#objective}
        '''
        result = self._values.get("objective")
        assert result is not None, "Required property 'objective' is missing"
        return typing.cast("ServiceLevelObjective", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#id ServiceLevel#id}.

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
        return "ServiceLevelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEvents",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "valid_events": "validEvents",
        "bad_events": "badEvents",
        "good_events": "goodEvents",
    },
)
class ServiceLevelEvents:
    def __init__(
        self,
        *,
        account_id: jsii.Number,
        valid_events: typing.Union["ServiceLevelEventsValidEvents", typing.Dict[str, typing.Any]],
        bad_events: typing.Optional[typing.Union["ServiceLevelEventsBadEvents", typing.Dict[str, typing.Any]]] = None,
        good_events: typing.Optional[typing.Union["ServiceLevelEventsGoodEvents", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#account_id ServiceLevel#account_id}.
        :param valid_events: valid_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#valid_events ServiceLevel#valid_events}
        :param bad_events: bad_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#bad_events ServiceLevel#bad_events}
        :param good_events: good_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#good_events ServiceLevel#good_events}
        '''
        if isinstance(valid_events, dict):
            valid_events = ServiceLevelEventsValidEvents(**valid_events)
        if isinstance(bad_events, dict):
            bad_events = ServiceLevelEventsBadEvents(**bad_events)
        if isinstance(good_events, dict):
            good_events = ServiceLevelEventsGoodEvents(**good_events)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelEvents.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument valid_events", value=valid_events, expected_type=type_hints["valid_events"])
            check_type(argname="argument bad_events", value=bad_events, expected_type=type_hints["bad_events"])
            check_type(argname="argument good_events", value=good_events, expected_type=type_hints["good_events"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "valid_events": valid_events,
        }
        if bad_events is not None:
            self._values["bad_events"] = bad_events
        if good_events is not None:
            self._values["good_events"] = good_events

    @builtins.property
    def account_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#account_id ServiceLevel#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def valid_events(self) -> "ServiceLevelEventsValidEvents":
        '''valid_events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#valid_events ServiceLevel#valid_events}
        '''
        result = self._values.get("valid_events")
        assert result is not None, "Required property 'valid_events' is missing"
        return typing.cast("ServiceLevelEventsValidEvents", result)

    @builtins.property
    def bad_events(self) -> typing.Optional["ServiceLevelEventsBadEvents"]:
        '''bad_events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#bad_events ServiceLevel#bad_events}
        '''
        result = self._values.get("bad_events")
        return typing.cast(typing.Optional["ServiceLevelEventsBadEvents"], result)

    @builtins.property
    def good_events(self) -> typing.Optional["ServiceLevelEventsGoodEvents"]:
        '''good_events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#good_events ServiceLevel#good_events}
        '''
        result = self._values.get("good_events")
        return typing.cast(typing.Optional["ServiceLevelEventsGoodEvents"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsBadEvents",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "where": "where"},
)
class ServiceLevelEventsBadEvents:
    def __init__(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelEventsBadEvents.__init__)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument where", value=where, expected_type=type_hints["where"])
        self._values: typing.Dict[str, typing.Any] = {
            "from_": from_,
        }
        if where is not None:
            self._values["where"] = where

    @builtins.property
    def from_(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.'''
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def where(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.'''
        result = self._values.get("where")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelEventsBadEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelEventsBadEventsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsBadEventsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelEventsBadEventsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWhere")
    def reset_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhere", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="whereInput")
    def where_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whereInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsBadEventsOutputReference, "from_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="where")
    def where(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "where"))

    @where.setter
    def where(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsBadEventsOutputReference, "where").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "where", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelEventsBadEvents]:
        return typing.cast(typing.Optional[ServiceLevelEventsBadEvents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelEventsBadEvents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsBadEventsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsGoodEvents",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "where": "where"},
)
class ServiceLevelEventsGoodEvents:
    def __init__(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelEventsGoodEvents.__init__)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument where", value=where, expected_type=type_hints["where"])
        self._values: typing.Dict[str, typing.Any] = {
            "from_": from_,
        }
        if where is not None:
            self._values["where"] = where

    @builtins.property
    def from_(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.'''
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def where(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.'''
        result = self._values.get("where")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelEventsGoodEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelEventsGoodEventsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsGoodEventsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelEventsGoodEventsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWhere")
    def reset_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhere", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="whereInput")
    def where_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whereInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsGoodEventsOutputReference, "from_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="where")
    def where(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "where"))

    @where.setter
    def where(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsGoodEventsOutputReference, "where").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "where", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelEventsGoodEvents]:
        return typing.cast(typing.Optional[ServiceLevelEventsGoodEvents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelEventsGoodEvents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsGoodEventsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceLevelEventsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelEventsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBadEvents")
    def put_bad_events(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        value = ServiceLevelEventsBadEvents(from_=from_, where=where)

        return typing.cast(None, jsii.invoke(self, "putBadEvents", [value]))

    @jsii.member(jsii_name="putGoodEvents")
    def put_good_events(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        value = ServiceLevelEventsGoodEvents(from_=from_, where=where)

        return typing.cast(None, jsii.invoke(self, "putGoodEvents", [value]))

    @jsii.member(jsii_name="putValidEvents")
    def put_valid_events(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        value = ServiceLevelEventsValidEvents(from_=from_, where=where)

        return typing.cast(None, jsii.invoke(self, "putValidEvents", [value]))

    @jsii.member(jsii_name="resetBadEvents")
    def reset_bad_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBadEvents", []))

    @jsii.member(jsii_name="resetGoodEvents")
    def reset_good_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodEvents", []))

    @builtins.property
    @jsii.member(jsii_name="badEvents")
    def bad_events(self) -> ServiceLevelEventsBadEventsOutputReference:
        return typing.cast(ServiceLevelEventsBadEventsOutputReference, jsii.get(self, "badEvents"))

    @builtins.property
    @jsii.member(jsii_name="goodEvents")
    def good_events(self) -> ServiceLevelEventsGoodEventsOutputReference:
        return typing.cast(ServiceLevelEventsGoodEventsOutputReference, jsii.get(self, "goodEvents"))

    @builtins.property
    @jsii.member(jsii_name="validEvents")
    def valid_events(self) -> "ServiceLevelEventsValidEventsOutputReference":
        return typing.cast("ServiceLevelEventsValidEventsOutputReference", jsii.get(self, "validEvents"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="badEventsInput")
    def bad_events_input(self) -> typing.Optional[ServiceLevelEventsBadEvents]:
        return typing.cast(typing.Optional[ServiceLevelEventsBadEvents], jsii.get(self, "badEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="goodEventsInput")
    def good_events_input(self) -> typing.Optional[ServiceLevelEventsGoodEvents]:
        return typing.cast(typing.Optional[ServiceLevelEventsGoodEvents], jsii.get(self, "goodEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="validEventsInput")
    def valid_events_input(self) -> typing.Optional["ServiceLevelEventsValidEvents"]:
        return typing.cast(typing.Optional["ServiceLevelEventsValidEvents"], jsii.get(self, "validEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelEvents]:
        return typing.cast(typing.Optional[ServiceLevelEvents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceLevelEvents]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsValidEvents",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "where": "where"},
)
class ServiceLevelEventsValidEvents:
    def __init__(
        self,
        *,
        from_: builtins.str,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.
        :param where: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelEventsValidEvents.__init__)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument where", value=where, expected_type=type_hints["where"])
        self._values: typing.Dict[str, typing.Any] = {
            "from_": from_,
        }
        if where is not None:
            self._values["where"] = where

    @builtins.property
    def from_(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#from ServiceLevel#from}.'''
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def where(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#where ServiceLevel#where}.'''
        result = self._values.get("where")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelEventsValidEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelEventsValidEventsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelEventsValidEventsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelEventsValidEventsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWhere")
    def reset_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhere", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="whereInput")
    def where_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whereInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsValidEventsOutputReference, "from_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="where")
    def where(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "where"))

    @where.setter
    def where(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsValidEventsOutputReference, "where").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "where", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelEventsValidEvents]:
        return typing.cast(typing.Optional[ServiceLevelEventsValidEvents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelEventsValidEvents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelEventsValidEventsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjective",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "time_window": "timeWindow",
        "description": "description",
        "name": "name",
    },
)
class ServiceLevelObjective:
    def __init__(
        self,
        *,
        target: jsii.Number,
        time_window: typing.Union["ServiceLevelObjectiveTimeWindow", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#target ServiceLevel#target}.
        :param time_window: time_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#time_window ServiceLevel#time_window}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.
        '''
        if isinstance(time_window, dict):
            time_window = ServiceLevelObjectiveTimeWindow(**time_window)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjective.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument time_window", value=time_window, expected_type=type_hints["time_window"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
            "time_window": time_window,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def target(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#target ServiceLevel#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_window(self) -> "ServiceLevelObjectiveTimeWindow":
        '''time_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#time_window ServiceLevel#time_window}
        '''
        result = self._values.get("time_window")
        assert result is not None, "Required property 'time_window' is missing"
        return typing.cast("ServiceLevelObjectiveTimeWindow", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#description ServiceLevel#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#name ServiceLevel#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjective(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelObjectiveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjectiveOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTimeWindow")
    def put_time_window(
        self,
        *,
        rolling: typing.Union["ServiceLevelObjectiveTimeWindowRolling", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param rolling: rolling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#rolling ServiceLevel#rolling}
        '''
        value = ServiceLevelObjectiveTimeWindow(rolling=rolling)

        return typing.cast(None, jsii.invoke(self, "putTimeWindow", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="timeWindow")
    def time_window(self) -> "ServiceLevelObjectiveTimeWindowOutputReference":
        return typing.cast("ServiceLevelObjectiveTimeWindowOutputReference", jsii.get(self, "timeWindow"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowInput")
    def time_window_input(self) -> typing.Optional["ServiceLevelObjectiveTimeWindow"]:
        return typing.cast(typing.Optional["ServiceLevelObjectiveTimeWindow"], jsii.get(self, "timeWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "target"))

    @target.setter
    def target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelObjective]:
        return typing.cast(typing.Optional[ServiceLevelObjective], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceLevelObjective]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjectiveTimeWindow",
    jsii_struct_bases=[],
    name_mapping={"rolling": "rolling"},
)
class ServiceLevelObjectiveTimeWindow:
    def __init__(
        self,
        *,
        rolling: typing.Union["ServiceLevelObjectiveTimeWindowRolling", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param rolling: rolling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#rolling ServiceLevel#rolling}
        '''
        if isinstance(rolling, dict):
            rolling = ServiceLevelObjectiveTimeWindowRolling(**rolling)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveTimeWindow.__init__)
            check_type(argname="argument rolling", value=rolling, expected_type=type_hints["rolling"])
        self._values: typing.Dict[str, typing.Any] = {
            "rolling": rolling,
        }

    @builtins.property
    def rolling(self) -> "ServiceLevelObjectiveTimeWindowRolling":
        '''rolling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#rolling ServiceLevel#rolling}
        '''
        result = self._values.get("rolling")
        assert result is not None, "Required property 'rolling' is missing"
        return typing.cast("ServiceLevelObjectiveTimeWindowRolling", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveTimeWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelObjectiveTimeWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjectiveTimeWindowOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveTimeWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRolling")
    def put_rolling(self, *, count: jsii.Number, unit: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#count ServiceLevel#count}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#unit ServiceLevel#unit}.
        '''
        value = ServiceLevelObjectiveTimeWindowRolling(count=count, unit=unit)

        return typing.cast(None, jsii.invoke(self, "putRolling", [value]))

    @builtins.property
    @jsii.member(jsii_name="rolling")
    def rolling(self) -> "ServiceLevelObjectiveTimeWindowRollingOutputReference":
        return typing.cast("ServiceLevelObjectiveTimeWindowRollingOutputReference", jsii.get(self, "rolling"))

    @builtins.property
    @jsii.member(jsii_name="rollingInput")
    def rolling_input(
        self,
    ) -> typing.Optional["ServiceLevelObjectiveTimeWindowRolling"]:
        return typing.cast(typing.Optional["ServiceLevelObjectiveTimeWindowRolling"], jsii.get(self, "rollingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelObjectiveTimeWindow]:
        return typing.cast(typing.Optional[ServiceLevelObjectiveTimeWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelObjectiveTimeWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveTimeWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjectiveTimeWindowRolling",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "unit": "unit"},
)
class ServiceLevelObjectiveTimeWindowRolling:
    def __init__(self, *, count: jsii.Number, unit: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#count ServiceLevel#count}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#unit ServiceLevel#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveTimeWindowRolling.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "unit": unit,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#count ServiceLevel#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/service_level#unit ServiceLevel#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveTimeWindowRolling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelObjectiveTimeWindowRollingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.serviceLevel.ServiceLevelObjectiveTimeWindowRollingOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveTimeWindowRollingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveTimeWindowRollingOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveTimeWindowRollingOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelObjectiveTimeWindowRolling]:
        return typing.cast(typing.Optional[ServiceLevelObjectiveTimeWindowRolling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelObjectiveTimeWindowRolling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveTimeWindowRollingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceLevel",
    "ServiceLevelConfig",
    "ServiceLevelEvents",
    "ServiceLevelEventsBadEvents",
    "ServiceLevelEventsBadEventsOutputReference",
    "ServiceLevelEventsGoodEvents",
    "ServiceLevelEventsGoodEventsOutputReference",
    "ServiceLevelEventsOutputReference",
    "ServiceLevelEventsValidEvents",
    "ServiceLevelEventsValidEventsOutputReference",
    "ServiceLevelObjective",
    "ServiceLevelObjectiveOutputReference",
    "ServiceLevelObjectiveTimeWindow",
    "ServiceLevelObjectiveTimeWindowOutputReference",
    "ServiceLevelObjectiveTimeWindowRolling",
    "ServiceLevelObjectiveTimeWindowRollingOutputReference",
]

publication.publish()
