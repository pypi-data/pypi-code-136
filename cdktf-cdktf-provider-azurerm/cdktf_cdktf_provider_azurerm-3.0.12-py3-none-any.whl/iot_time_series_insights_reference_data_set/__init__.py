'''
# `azurerm_iot_time_series_insights_reference_data_set`

Refer to the Terraform Registory for docs: [`azurerm_iot_time_series_insights_reference_data_set`](https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set).
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


class IotTimeSeriesInsightsReferenceDataSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set azurerm_iot_time_series_insights_reference_data_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        key_property: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotTimeSeriesInsightsReferenceDataSetKeyProperty", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        time_series_insights_environment_id: builtins.str,
        data_string_comparison_behavior: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsReferenceDataSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set azurerm_iot_time_series_insights_reference_data_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key_property: key_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#key_property IotTimeSeriesInsightsReferenceDataSet#key_property}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#location IotTimeSeriesInsightsReferenceDataSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#name IotTimeSeriesInsightsReferenceDataSet#name}.
        :param time_series_insights_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#time_series_insights_environment_id IotTimeSeriesInsightsReferenceDataSet#time_series_insights_environment_id}.
        :param data_string_comparison_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#data_string_comparison_behavior IotTimeSeriesInsightsReferenceDataSet#data_string_comparison_behavior}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#id IotTimeSeriesInsightsReferenceDataSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#tags IotTimeSeriesInsightsReferenceDataSet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#timeouts IotTimeSeriesInsightsReferenceDataSet#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotTimeSeriesInsightsReferenceDataSetConfig(
            key_property=key_property,
            location=location,
            name=name,
            time_series_insights_environment_id=time_series_insights_environment_id,
            data_string_comparison_behavior=data_string_comparison_behavior,
            id=id,
            tags=tags,
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

    @jsii.member(jsii_name="putKeyProperty")
    def put_key_property(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotTimeSeriesInsightsReferenceDataSetKeyProperty", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSet.put_key_property)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKeyProperty", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#create IotTimeSeriesInsightsReferenceDataSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#delete IotTimeSeriesInsightsReferenceDataSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#read IotTimeSeriesInsightsReferenceDataSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#update IotTimeSeriesInsightsReferenceDataSet#update}.
        '''
        value = IotTimeSeriesInsightsReferenceDataSetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDataStringComparisonBehavior")
    def reset_data_string_comparison_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataStringComparisonBehavior", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="keyProperty")
    def key_property(self) -> "IotTimeSeriesInsightsReferenceDataSetKeyPropertyList":
        return typing.cast("IotTimeSeriesInsightsReferenceDataSetKeyPropertyList", jsii.get(self, "keyProperty"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference":
        return typing.cast("IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="dataStringComparisonBehaviorInput")
    def data_string_comparison_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataStringComparisonBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPropertyInput")
    def key_property_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotTimeSeriesInsightsReferenceDataSetKeyProperty"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotTimeSeriesInsightsReferenceDataSetKeyProperty"]]], jsii.get(self, "keyPropertyInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IotTimeSeriesInsightsReferenceDataSetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IotTimeSeriesInsightsReferenceDataSetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesInsightsEnvironmentIdInput")
    def time_series_insights_environment_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeSeriesInsightsEnvironmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataStringComparisonBehavior"))

    @data_string_comparison_behavior.setter
    def data_string_comparison_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "data_string_comparison_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataStringComparisonBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeSeriesInsightsEnvironmentId"))

    @time_series_insights_environment_id.setter
    def time_series_insights_environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSet, "time_series_insights_environment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeSeriesInsightsEnvironmentId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key_property": "keyProperty",
        "location": "location",
        "name": "name",
        "time_series_insights_environment_id": "timeSeriesInsightsEnvironmentId",
        "data_string_comparison_behavior": "dataStringComparisonBehavior",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class IotTimeSeriesInsightsReferenceDataSetConfig(cdktf.TerraformMetaArguments):
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
        key_property: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotTimeSeriesInsightsReferenceDataSetKeyProperty", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        time_series_insights_environment_id: builtins.str,
        data_string_comparison_behavior: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsReferenceDataSetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key_property: key_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#key_property IotTimeSeriesInsightsReferenceDataSet#key_property}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#location IotTimeSeriesInsightsReferenceDataSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#name IotTimeSeriesInsightsReferenceDataSet#name}.
        :param time_series_insights_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#time_series_insights_environment_id IotTimeSeriesInsightsReferenceDataSet#time_series_insights_environment_id}.
        :param data_string_comparison_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#data_string_comparison_behavior IotTimeSeriesInsightsReferenceDataSet#data_string_comparison_behavior}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#id IotTimeSeriesInsightsReferenceDataSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#tags IotTimeSeriesInsightsReferenceDataSet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#timeouts IotTimeSeriesInsightsReferenceDataSet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = IotTimeSeriesInsightsReferenceDataSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key_property", value=key_property, expected_type=type_hints["key_property"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument time_series_insights_environment_id", value=time_series_insights_environment_id, expected_type=type_hints["time_series_insights_environment_id"])
            check_type(argname="argument data_string_comparison_behavior", value=data_string_comparison_behavior, expected_type=type_hints["data_string_comparison_behavior"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_property": key_property,
            "location": location,
            "name": name,
            "time_series_insights_environment_id": time_series_insights_environment_id,
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
        if data_string_comparison_behavior is not None:
            self._values["data_string_comparison_behavior"] = data_string_comparison_behavior
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
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
    def key_property(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["IotTimeSeriesInsightsReferenceDataSetKeyProperty"]]:
        '''key_property block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#key_property IotTimeSeriesInsightsReferenceDataSet#key_property}
        '''
        result = self._values.get("key_property")
        assert result is not None, "Required property 'key_property' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["IotTimeSeriesInsightsReferenceDataSetKeyProperty"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#location IotTimeSeriesInsightsReferenceDataSet#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#name IotTimeSeriesInsightsReferenceDataSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_series_insights_environment_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#time_series_insights_environment_id IotTimeSeriesInsightsReferenceDataSet#time_series_insights_environment_id}.'''
        result = self._values.get("time_series_insights_environment_id")
        assert result is not None, "Required property 'time_series_insights_environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_string_comparison_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#data_string_comparison_behavior IotTimeSeriesInsightsReferenceDataSet#data_string_comparison_behavior}.'''
        result = self._values.get("data_string_comparison_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#id IotTimeSeriesInsightsReferenceDataSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#tags IotTimeSeriesInsightsReferenceDataSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["IotTimeSeriesInsightsReferenceDataSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#timeouts IotTimeSeriesInsightsReferenceDataSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IotTimeSeriesInsightsReferenceDataSetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsReferenceDataSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetKeyProperty",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotTimeSeriesInsightsReferenceDataSetKeyProperty:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#name IotTimeSeriesInsightsReferenceDataSet#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#type IotTimeSeriesInsightsReferenceDataSet#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetKeyProperty.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#name IotTimeSeriesInsightsReferenceDataSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#type IotTimeSeriesInsightsReferenceDataSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsReferenceDataSetKeyProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTimeSeriesInsightsReferenceDataSetKeyPropertyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetKeyPropertyList",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotTimeSeriesInsightsReferenceDataSetKeyProperty]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotTimeSeriesInsightsReferenceDataSetKeyProperty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotTimeSeriesInsightsReferenceDataSetKeyProperty]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetKeyProperty, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetKeyProperty, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetKeyProperty, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IotTimeSeriesInsightsReferenceDataSetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#create IotTimeSeriesInsightsReferenceDataSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#delete IotTimeSeriesInsightsReferenceDataSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#read IotTimeSeriesInsightsReferenceDataSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#update IotTimeSeriesInsightsReferenceDataSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#create IotTimeSeriesInsightsReferenceDataSet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#delete IotTimeSeriesInsightsReferenceDataSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#read IotTimeSeriesInsightsReferenceDataSet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_reference_data_set#update IotTimeSeriesInsightsReferenceDataSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsReferenceDataSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsReferenceDataSet.IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTimeSeriesInsightsReferenceDataSetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotTimeSeriesInsightsReferenceDataSet",
    "IotTimeSeriesInsightsReferenceDataSetConfig",
    "IotTimeSeriesInsightsReferenceDataSetKeyProperty",
    "IotTimeSeriesInsightsReferenceDataSetKeyPropertyList",
    "IotTimeSeriesInsightsReferenceDataSetKeyPropertyOutputReference",
    "IotTimeSeriesInsightsReferenceDataSetTimeouts",
    "IotTimeSeriesInsightsReferenceDataSetTimeoutsOutputReference",
]

publication.publish()
