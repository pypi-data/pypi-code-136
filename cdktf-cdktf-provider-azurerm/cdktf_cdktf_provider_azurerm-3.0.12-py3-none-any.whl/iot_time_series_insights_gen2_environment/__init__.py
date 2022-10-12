'''
# `azurerm_iot_time_series_insights_gen2_environment`

Refer to the Terraform Registory for docs: [`azurerm_iot_time_series_insights_gen2_environment`](https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment).
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


class IotTimeSeriesInsightsGen2Environment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2Environment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment azurerm_iot_time_series_insights_gen2_environment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id_properties: typing.Sequence[builtins.str],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        storage: typing.Union["IotTimeSeriesInsightsGen2EnvironmentStorage", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsGen2EnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        warm_store_data_retention_time: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment azurerm_iot_time_series_insights_gen2_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id_properties IotTimeSeriesInsightsGen2Environment#id_properties}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#location IotTimeSeriesInsightsGen2Environment#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#resource_group_name IotTimeSeriesInsightsGen2Environment#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#sku_name IotTimeSeriesInsightsGen2Environment#sku_name}.
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#storage IotTimeSeriesInsightsGen2Environment#storage}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id IotTimeSeriesInsightsGen2Environment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#tags IotTimeSeriesInsightsGen2Environment#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#timeouts IotTimeSeriesInsightsGen2Environment#timeouts}
        :param warm_store_data_retention_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#warm_store_data_retention_time IotTimeSeriesInsightsGen2Environment#warm_store_data_retention_time}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2Environment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotTimeSeriesInsightsGen2EnvironmentConfig(
            id_properties=id_properties,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            storage=storage,
            id=id,
            tags=tags,
            timeouts=timeouts,
            warm_store_data_retention_time=warm_store_data_retention_time,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putStorage")
    def put_storage(self, *, key: builtins.str, name: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#key IotTimeSeriesInsightsGen2Environment#key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.
        '''
        value = IotTimeSeriesInsightsGen2EnvironmentStorage(key=key, name=name)

        return typing.cast(None, jsii.invoke(self, "putStorage", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#create IotTimeSeriesInsightsGen2Environment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#delete IotTimeSeriesInsightsGen2Environment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#read IotTimeSeriesInsightsGen2Environment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#update IotTimeSeriesInsightsGen2Environment#update}.
        '''
        value = IotTimeSeriesInsightsGen2EnvironmentTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWarmStoreDataRetentionTime")
    def reset_warm_store_data_retention_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmStoreDataRetentionTime", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessFqdn")
    def data_access_fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataAccessFqdn"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> "IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference":
        return typing.cast("IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference", jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference":
        return typing.cast("IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idPropertiesInput")
    def id_properties_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(
        self,
    ) -> typing.Optional["IotTimeSeriesInsightsGen2EnvironmentStorage"]:
        return typing.cast(typing.Optional["IotTimeSeriesInsightsGen2EnvironmentStorage"], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IotTimeSeriesInsightsGen2EnvironmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IotTimeSeriesInsightsGen2EnvironmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="warmStoreDataRetentionTimeInput")
    def warm_store_data_retention_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warmStoreDataRetentionTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idProperties")
    def id_properties(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idProperties"))

    @id_properties.setter
    def id_properties(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "id_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idProperties", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="warmStoreDataRetentionTime")
    def warm_store_data_retention_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warmStoreDataRetentionTime"))

    @warm_store_data_retention_time.setter
    def warm_store_data_retention_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2Environment, "warm_store_data_retention_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmStoreDataRetentionTime", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2EnvironmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id_properties": "idProperties",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "storage": "storage",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
        "warm_store_data_retention_time": "warmStoreDataRetentionTime",
    },
)
class IotTimeSeriesInsightsGen2EnvironmentConfig(cdktf.TerraformMetaArguments):
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
        id_properties: typing.Sequence[builtins.str],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        storage: typing.Union["IotTimeSeriesInsightsGen2EnvironmentStorage", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsGen2EnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        warm_store_data_retention_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id_properties IotTimeSeriesInsightsGen2Environment#id_properties}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#location IotTimeSeriesInsightsGen2Environment#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#resource_group_name IotTimeSeriesInsightsGen2Environment#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#sku_name IotTimeSeriesInsightsGen2Environment#sku_name}.
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#storage IotTimeSeriesInsightsGen2Environment#storage}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id IotTimeSeriesInsightsGen2Environment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#tags IotTimeSeriesInsightsGen2Environment#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#timeouts IotTimeSeriesInsightsGen2Environment#timeouts}
        :param warm_store_data_retention_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#warm_store_data_retention_time IotTimeSeriesInsightsGen2Environment#warm_store_data_retention_time}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage, dict):
            storage = IotTimeSeriesInsightsGen2EnvironmentStorage(**storage)
        if isinstance(timeouts, dict):
            timeouts = IotTimeSeriesInsightsGen2EnvironmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2EnvironmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id_properties", value=id_properties, expected_type=type_hints["id_properties"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument warm_store_data_retention_time", value=warm_store_data_retention_time, expected_type=type_hints["warm_store_data_retention_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "id_properties": id_properties,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "storage": storage,
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
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if warm_store_data_retention_time is not None:
            self._values["warm_store_data_retention_time"] = warm_store_data_retention_time

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
    def id_properties(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id_properties IotTimeSeriesInsightsGen2Environment#id_properties}.'''
        result = self._values.get("id_properties")
        assert result is not None, "Required property 'id_properties' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#location IotTimeSeriesInsightsGen2Environment#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#resource_group_name IotTimeSeriesInsightsGen2Environment#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#sku_name IotTimeSeriesInsightsGen2Environment#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage(self) -> "IotTimeSeriesInsightsGen2EnvironmentStorage":
        '''storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#storage IotTimeSeriesInsightsGen2Environment#storage}
        '''
        result = self._values.get("storage")
        assert result is not None, "Required property 'storage' is missing"
        return typing.cast("IotTimeSeriesInsightsGen2EnvironmentStorage", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#id IotTimeSeriesInsightsGen2Environment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#tags IotTimeSeriesInsightsGen2Environment#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["IotTimeSeriesInsightsGen2EnvironmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#timeouts IotTimeSeriesInsightsGen2Environment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IotTimeSeriesInsightsGen2EnvironmentTimeouts"], result)

    @builtins.property
    def warm_store_data_retention_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#warm_store_data_retention_time IotTimeSeriesInsightsGen2Environment#warm_store_data_retention_time}.'''
        result = self._values.get("warm_store_data_retention_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsGen2EnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2EnvironmentStorage",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name"},
)
class IotTimeSeriesInsightsGen2EnvironmentStorage:
    def __init__(self, *, key: builtins.str, name: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#key IotTimeSeriesInsightsGen2Environment#key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2EnvironmentStorage.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "name": name,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#key IotTimeSeriesInsightsGen2Environment#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#name IotTimeSeriesInsightsGen2Environment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsGen2EnvironmentStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotTimeSeriesInsightsGen2EnvironmentStorage]:
        return typing.cast(typing.Optional[IotTimeSeriesInsightsGen2EnvironmentStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTimeSeriesInsightsGen2EnvironmentStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2EnvironmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IotTimeSeriesInsightsGen2EnvironmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#create IotTimeSeriesInsightsGen2Environment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#delete IotTimeSeriesInsightsGen2Environment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#read IotTimeSeriesInsightsGen2Environment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#update IotTimeSeriesInsightsGen2Environment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2EnvironmentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#create IotTimeSeriesInsightsGen2Environment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#delete IotTimeSeriesInsightsGen2Environment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#read IotTimeSeriesInsightsGen2Environment#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_gen2_environment#update IotTimeSeriesInsightsGen2Environment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsGen2EnvironmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsGen2Environment.IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTimeSeriesInsightsGen2EnvironmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTimeSeriesInsightsGen2EnvironmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTimeSeriesInsightsGen2EnvironmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotTimeSeriesInsightsGen2Environment",
    "IotTimeSeriesInsightsGen2EnvironmentConfig",
    "IotTimeSeriesInsightsGen2EnvironmentStorage",
    "IotTimeSeriesInsightsGen2EnvironmentStorageOutputReference",
    "IotTimeSeriesInsightsGen2EnvironmentTimeouts",
    "IotTimeSeriesInsightsGen2EnvironmentTimeoutsOutputReference",
]

publication.publish()
