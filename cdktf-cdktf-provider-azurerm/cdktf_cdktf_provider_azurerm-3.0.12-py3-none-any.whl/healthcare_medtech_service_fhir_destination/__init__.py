'''
# `azurerm_healthcare_medtech_service_fhir_destination`

Refer to the Terraform Registory for docs: [`azurerm_healthcare_medtech_service_fhir_destination`](https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination).
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


class HealthcareMedtechServiceFhirDestination(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.healthcareMedtechServiceFhirDestination.HealthcareMedtechServiceFhirDestination",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination azurerm_healthcare_medtech_service_fhir_destination}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination_fhir_mapping_json: builtins.str,
        destination_fhir_service_id: builtins.str,
        destination_identity_resolution_type: builtins.str,
        location: builtins.str,
        medtech_service_id: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HealthcareMedtechServiceFhirDestinationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination azurerm_healthcare_medtech_service_fhir_destination} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_fhir_mapping_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_mapping_json HealthcareMedtechServiceFhirDestination#destination_fhir_mapping_json}.
        :param destination_fhir_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_service_id HealthcareMedtechServiceFhirDestination#destination_fhir_service_id}.
        :param destination_identity_resolution_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_identity_resolution_type HealthcareMedtechServiceFhirDestination#destination_identity_resolution_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#location HealthcareMedtechServiceFhirDestination#location}.
        :param medtech_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#medtech_service_id HealthcareMedtechServiceFhirDestination#medtech_service_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#name HealthcareMedtechServiceFhirDestination#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#id HealthcareMedtechServiceFhirDestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#timeouts HealthcareMedtechServiceFhirDestination#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HealthcareMedtechServiceFhirDestination.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HealthcareMedtechServiceFhirDestinationConfig(
            destination_fhir_mapping_json=destination_fhir_mapping_json,
            destination_fhir_service_id=destination_fhir_service_id,
            destination_identity_resolution_type=destination_identity_resolution_type,
            location=location,
            medtech_service_id=medtech_service_id,
            name=name,
            id=id,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#create HealthcareMedtechServiceFhirDestination#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#delete HealthcareMedtechServiceFhirDestination#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#read HealthcareMedtechServiceFhirDestination#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#update HealthcareMedtechServiceFhirDestination#update}.
        '''
        value = HealthcareMedtechServiceFhirDestinationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    def timeouts(
        self,
    ) -> "HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference":
        return typing.cast("HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="destinationFhirMappingJsonInput")
    def destination_fhir_mapping_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFhirMappingJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFhirServiceIdInput")
    def destination_fhir_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFhirServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationIdentityResolutionTypeInput")
    def destination_identity_resolution_type_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationIdentityResolutionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="medtechServiceIdInput")
    def medtech_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "medtechServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["HealthcareMedtechServiceFhirDestinationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["HealthcareMedtechServiceFhirDestinationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFhirMappingJson")
    def destination_fhir_mapping_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationFhirMappingJson"))

    @destination_fhir_mapping_json.setter
    def destination_fhir_mapping_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "destination_fhir_mapping_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFhirMappingJson", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFhirServiceId")
    def destination_fhir_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationFhirServiceId"))

    @destination_fhir_service_id.setter
    def destination_fhir_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "destination_fhir_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFhirServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="destinationIdentityResolutionType")
    def destination_identity_resolution_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationIdentityResolutionType"))

    @destination_identity_resolution_type.setter
    def destination_identity_resolution_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "destination_identity_resolution_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationIdentityResolutionType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="medtechServiceId")
    def medtech_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "medtechServiceId"))

    @medtech_service_id.setter
    def medtech_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "medtech_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "medtechServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestination, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.healthcareMedtechServiceFhirDestination.HealthcareMedtechServiceFhirDestinationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_fhir_mapping_json": "destinationFhirMappingJson",
        "destination_fhir_service_id": "destinationFhirServiceId",
        "destination_identity_resolution_type": "destinationIdentityResolutionType",
        "location": "location",
        "medtech_service_id": "medtechServiceId",
        "name": "name",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class HealthcareMedtechServiceFhirDestinationConfig(cdktf.TerraformMetaArguments):
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
        destination_fhir_mapping_json: builtins.str,
        destination_fhir_service_id: builtins.str,
        destination_identity_resolution_type: builtins.str,
        location: builtins.str,
        medtech_service_id: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HealthcareMedtechServiceFhirDestinationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_fhir_mapping_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_mapping_json HealthcareMedtechServiceFhirDestination#destination_fhir_mapping_json}.
        :param destination_fhir_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_service_id HealthcareMedtechServiceFhirDestination#destination_fhir_service_id}.
        :param destination_identity_resolution_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_identity_resolution_type HealthcareMedtechServiceFhirDestination#destination_identity_resolution_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#location HealthcareMedtechServiceFhirDestination#location}.
        :param medtech_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#medtech_service_id HealthcareMedtechServiceFhirDestination#medtech_service_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#name HealthcareMedtechServiceFhirDestination#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#id HealthcareMedtechServiceFhirDestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#timeouts HealthcareMedtechServiceFhirDestination#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = HealthcareMedtechServiceFhirDestinationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(HealthcareMedtechServiceFhirDestinationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_fhir_mapping_json", value=destination_fhir_mapping_json, expected_type=type_hints["destination_fhir_mapping_json"])
            check_type(argname="argument destination_fhir_service_id", value=destination_fhir_service_id, expected_type=type_hints["destination_fhir_service_id"])
            check_type(argname="argument destination_identity_resolution_type", value=destination_identity_resolution_type, expected_type=type_hints["destination_identity_resolution_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument medtech_service_id", value=medtech_service_id, expected_type=type_hints["medtech_service_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_fhir_mapping_json": destination_fhir_mapping_json,
            "destination_fhir_service_id": destination_fhir_service_id,
            "destination_identity_resolution_type": destination_identity_resolution_type,
            "location": location,
            "medtech_service_id": medtech_service_id,
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
    def destination_fhir_mapping_json(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_mapping_json HealthcareMedtechServiceFhirDestination#destination_fhir_mapping_json}.'''
        result = self._values.get("destination_fhir_mapping_json")
        assert result is not None, "Required property 'destination_fhir_mapping_json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_fhir_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_fhir_service_id HealthcareMedtechServiceFhirDestination#destination_fhir_service_id}.'''
        result = self._values.get("destination_fhir_service_id")
        assert result is not None, "Required property 'destination_fhir_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_identity_resolution_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#destination_identity_resolution_type HealthcareMedtechServiceFhirDestination#destination_identity_resolution_type}.'''
        result = self._values.get("destination_identity_resolution_type")
        assert result is not None, "Required property 'destination_identity_resolution_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#location HealthcareMedtechServiceFhirDestination#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def medtech_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#medtech_service_id HealthcareMedtechServiceFhirDestination#medtech_service_id}.'''
        result = self._values.get("medtech_service_id")
        assert result is not None, "Required property 'medtech_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#name HealthcareMedtechServiceFhirDestination#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#id HealthcareMedtechServiceFhirDestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["HealthcareMedtechServiceFhirDestinationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#timeouts HealthcareMedtechServiceFhirDestination#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["HealthcareMedtechServiceFhirDestinationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthcareMedtechServiceFhirDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.healthcareMedtechServiceFhirDestination.HealthcareMedtechServiceFhirDestinationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class HealthcareMedtechServiceFhirDestinationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#create HealthcareMedtechServiceFhirDestination#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#delete HealthcareMedtechServiceFhirDestination#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#read HealthcareMedtechServiceFhirDestination#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#update HealthcareMedtechServiceFhirDestination#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HealthcareMedtechServiceFhirDestinationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#create HealthcareMedtechServiceFhirDestination#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#delete HealthcareMedtechServiceFhirDestination#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#read HealthcareMedtechServiceFhirDestination#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/healthcare_medtech_service_fhir_destination#update HealthcareMedtechServiceFhirDestination#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthcareMedtechServiceFhirDestinationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.healthcareMedtechServiceFhirDestination.HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HealthcareMedtechServiceFhirDestinationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HealthcareMedtechServiceFhirDestinationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HealthcareMedtechServiceFhirDestinationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HealthcareMedtechServiceFhirDestination",
    "HealthcareMedtechServiceFhirDestinationConfig",
    "HealthcareMedtechServiceFhirDestinationTimeouts",
    "HealthcareMedtechServiceFhirDestinationTimeoutsOutputReference",
]

publication.publish()
