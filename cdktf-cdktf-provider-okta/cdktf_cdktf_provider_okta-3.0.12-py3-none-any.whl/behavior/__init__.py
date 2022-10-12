'''
# `okta_behavior`

Refer to the Terraform Registory for docs: [`okta_behavior`](https://www.terraform.io/docs/providers/okta/r/behavior).
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


class Behavior(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.behavior.Behavior",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/behavior okta_behavior}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        location_granularity_type: typing.Optional[builtins.str] = None,
        number_of_authentications: typing.Optional[jsii.Number] = None,
        radius_from_location: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        velocity: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/behavior okta_behavior} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#name Behavior#name}
        :param type: Behavior type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#type Behavior#type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#id Behavior#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_granularity_type: Determines the method and level of detail used to evaluate the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#location_granularity_type Behavior#location_granularity_type}
        :param number_of_authentications: The number of recent authentications used to evaluate the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#number_of_authentications Behavior#number_of_authentications}
        :param radius_from_location: Radius from location (in kilometers). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#radius_from_location Behavior#radius_from_location}
        :param status: Behavior status: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#status Behavior#status}
        :param velocity: Velocity (in kilometers per hour). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#velocity Behavior#velocity}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Behavior.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BehaviorConfig(
            name=name,
            type=type,
            id=id,
            location_granularity_type=location_granularity_type,
            number_of_authentications=number_of_authentications,
            radius_from_location=radius_from_location,
            status=status,
            velocity=velocity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocationGranularityType")
    def reset_location_granularity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationGranularityType", []))

    @jsii.member(jsii_name="resetNumberOfAuthentications")
    def reset_number_of_authentications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfAuthentications", []))

    @jsii.member(jsii_name="resetRadiusFromLocation")
    def reset_radius_from_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadiusFromLocation", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetVelocity")
    def reset_velocity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVelocity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationGranularityTypeInput")
    def location_granularity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationGranularityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfAuthenticationsInput")
    def number_of_authentications_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfAuthenticationsInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusFromLocationInput")
    def radius_from_location_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "radiusFromLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="velocityInput")
    def velocity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "velocityInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locationGranularityType")
    def location_granularity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationGranularityType"))

    @location_granularity_type.setter
    def location_granularity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "location_granularity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationGranularityType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfAuthentications")
    def number_of_authentications(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfAuthentications"))

    @number_of_authentications.setter
    def number_of_authentications(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "number_of_authentications").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfAuthentications", value)

    @builtins.property
    @jsii.member(jsii_name="radiusFromLocation")
    def radius_from_location(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "radiusFromLocation"))

    @radius_from_location.setter
    def radius_from_location(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "radius_from_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusFromLocation", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="velocity")
    def velocity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "velocity"))

    @velocity.setter
    def velocity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Behavior, "velocity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "velocity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.behavior.BehaviorConfig",
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
        "type": "type",
        "id": "id",
        "location_granularity_type": "locationGranularityType",
        "number_of_authentications": "numberOfAuthentications",
        "radius_from_location": "radiusFromLocation",
        "status": "status",
        "velocity": "velocity",
    },
)
class BehaviorConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        location_granularity_type: typing.Optional[builtins.str] = None,
        number_of_authentications: typing.Optional[jsii.Number] = None,
        radius_from_location: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        velocity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#name Behavior#name}
        :param type: Behavior type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#type Behavior#type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#id Behavior#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_granularity_type: Determines the method and level of detail used to evaluate the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#location_granularity_type Behavior#location_granularity_type}
        :param number_of_authentications: The number of recent authentications used to evaluate the behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#number_of_authentications Behavior#number_of_authentications}
        :param radius_from_location: Radius from location (in kilometers). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#radius_from_location Behavior#radius_from_location}
        :param status: Behavior status: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#status Behavior#status}
        :param velocity: Velocity (in kilometers per hour). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#velocity Behavior#velocity}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(BehaviorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location_granularity_type", value=location_granularity_type, expected_type=type_hints["location_granularity_type"])
            check_type(argname="argument number_of_authentications", value=number_of_authentications, expected_type=type_hints["number_of_authentications"])
            check_type(argname="argument radius_from_location", value=radius_from_location, expected_type=type_hints["radius_from_location"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument velocity", value=velocity, expected_type=type_hints["velocity"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
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
        if location_granularity_type is not None:
            self._values["location_granularity_type"] = location_granularity_type
        if number_of_authentications is not None:
            self._values["number_of_authentications"] = number_of_authentications
        if radius_from_location is not None:
            self._values["radius_from_location"] = radius_from_location
        if status is not None:
            self._values["status"] = status
        if velocity is not None:
            self._values["velocity"] = velocity

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
        '''Name of the behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#name Behavior#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Behavior type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#type Behavior#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#id Behavior#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location_granularity_type(self) -> typing.Optional[builtins.str]:
        '''Determines the method and level of detail used to evaluate the behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#location_granularity_type Behavior#location_granularity_type}
        '''
        result = self._values.get("location_granularity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_authentications(self) -> typing.Optional[jsii.Number]:
        '''The number of recent authentications used to evaluate the behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#number_of_authentications Behavior#number_of_authentications}
        '''
        result = self._values.get("number_of_authentications")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def radius_from_location(self) -> typing.Optional[jsii.Number]:
        '''Radius from location (in kilometers).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#radius_from_location Behavior#radius_from_location}
        '''
        result = self._values.get("radius_from_location")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Behavior status: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#status Behavior#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def velocity(self) -> typing.Optional[jsii.Number]:
        '''Velocity (in kilometers per hour).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/behavior#velocity Behavior#velocity}
        '''
        result = self._values.get("velocity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BehaviorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Behavior",
    "BehaviorConfig",
]

publication.publish()
