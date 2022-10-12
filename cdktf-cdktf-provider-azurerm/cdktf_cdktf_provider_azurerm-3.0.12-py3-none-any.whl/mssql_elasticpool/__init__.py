'''
# `azurerm_mssql_elasticpool`

Refer to the Terraform Registory for docs: [`azurerm_mssql_elasticpool`](https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool).
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


class MssqlElasticpool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool azurerm_mssql_elasticpool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        per_database_settings: typing.Union["MssqlElasticpoolPerDatabaseSettings", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        server_name: builtins.str,
        sku: typing.Union["MssqlElasticpoolSku", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        maintenance_configuration_name: typing.Optional[builtins.str] = None,
        max_size_bytes: typing.Optional[jsii.Number] = None,
        max_size_gb: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MssqlElasticpoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool azurerm_mssql_elasticpool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#location MssqlElasticpool#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.
        :param per_database_settings: per_database_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#per_database_settings MssqlElasticpool#per_database_settings}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#resource_group_name MssqlElasticpool#resource_group_name}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#server_name MssqlElasticpool#server_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#sku MssqlElasticpool#sku}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#id MssqlElasticpool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#license_type MssqlElasticpool#license_type}.
        :param maintenance_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#maintenance_configuration_name MssqlElasticpool#maintenance_configuration_name}.
        :param max_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_bytes MssqlElasticpool#max_size_bytes}.
        :param max_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_gb MssqlElasticpool#max_size_gb}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tags MssqlElasticpool#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#timeouts MssqlElasticpool#timeouts}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#zone_redundant MssqlElasticpool#zone_redundant}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlElasticpool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MssqlElasticpoolConfig(
            location=location,
            name=name,
            per_database_settings=per_database_settings,
            resource_group_name=resource_group_name,
            server_name=server_name,
            sku=sku,
            id=id,
            license_type=license_type,
            maintenance_configuration_name=maintenance_configuration_name,
            max_size_bytes=max_size_bytes,
            max_size_gb=max_size_gb,
            tags=tags,
            timeouts=timeouts,
            zone_redundant=zone_redundant,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPerDatabaseSettings")
    def put_per_database_settings(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> None:
        '''
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_capacity MssqlElasticpool#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#min_capacity MssqlElasticpool#min_capacity}.
        '''
        value = MssqlElasticpoolPerDatabaseSettings(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(None, jsii.invoke(self, "putPerDatabaseSettings", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(
        self,
        *,
        capacity: jsii.Number,
        name: builtins.str,
        tier: builtins.str,
        family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#capacity MssqlElasticpool#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tier MssqlElasticpool#tier}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#family MssqlElasticpool#family}.
        '''
        value = MssqlElasticpoolSku(
            capacity=capacity, name=name, tier=tier, family=family
        )

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#create MssqlElasticpool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#delete MssqlElasticpool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#read MssqlElasticpool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#update MssqlElasticpool#update}.
        '''
        value = MssqlElasticpoolTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetMaintenanceConfigurationName")
    def reset_maintenance_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceConfigurationName", []))

    @jsii.member(jsii_name="resetMaxSizeBytes")
    def reset_max_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSizeBytes", []))

    @jsii.member(jsii_name="resetMaxSizeGb")
    def reset_max_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSizeGb", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZoneRedundant")
    def reset_zone_redundant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneRedundant", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="perDatabaseSettings")
    def per_database_settings(
        self,
    ) -> "MssqlElasticpoolPerDatabaseSettingsOutputReference":
        return typing.cast("MssqlElasticpoolPerDatabaseSettingsOutputReference", jsii.get(self, "perDatabaseSettings"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "MssqlElasticpoolSkuOutputReference":
        return typing.cast("MssqlElasticpoolSkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MssqlElasticpoolTimeoutsOutputReference":
        return typing.cast("MssqlElasticpoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfigurationNameInput")
    def maintenance_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeBytesInput")
    def max_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeGbInput")
    def max_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="perDatabaseSettingsInput")
    def per_database_settings_input(
        self,
    ) -> typing.Optional["MssqlElasticpoolPerDatabaseSettings"]:
        return typing.cast(typing.Optional["MssqlElasticpoolPerDatabaseSettings"], jsii.get(self, "perDatabaseSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["MssqlElasticpoolSku"]:
        return typing.cast(typing.Optional["MssqlElasticpoolSku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlElasticpoolTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlElasticpoolTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneRedundantInput")
    def zone_redundant_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneRedundantInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfigurationName")
    def maintenance_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceConfigurationName"))

    @maintenance_configuration_name.setter
    def maintenance_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "maintenance_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="maxSizeBytes")
    def max_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSizeBytes"))

    @max_size_bytes.setter
    def max_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "max_size_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="maxSizeGb")
    def max_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSizeGb"))

    @max_size_gb.setter
    def max_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "max_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zoneRedundant")
    def zone_redundant(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zoneRedundant"))

    @zone_redundant.setter
    def zone_redundant(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpool, "zone_redundant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneRedundant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "per_database_settings": "perDatabaseSettings",
        "resource_group_name": "resourceGroupName",
        "server_name": "serverName",
        "sku": "sku",
        "id": "id",
        "license_type": "licenseType",
        "maintenance_configuration_name": "maintenanceConfigurationName",
        "max_size_bytes": "maxSizeBytes",
        "max_size_gb": "maxSizeGb",
        "tags": "tags",
        "timeouts": "timeouts",
        "zone_redundant": "zoneRedundant",
    },
)
class MssqlElasticpoolConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        per_database_settings: typing.Union["MssqlElasticpoolPerDatabaseSettings", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        server_name: builtins.str,
        sku: typing.Union["MssqlElasticpoolSku", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        maintenance_configuration_name: typing.Optional[builtins.str] = None,
        max_size_bytes: typing.Optional[jsii.Number] = None,
        max_size_gb: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MssqlElasticpoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#location MssqlElasticpool#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.
        :param per_database_settings: per_database_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#per_database_settings MssqlElasticpool#per_database_settings}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#resource_group_name MssqlElasticpool#resource_group_name}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#server_name MssqlElasticpool#server_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#sku MssqlElasticpool#sku}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#id MssqlElasticpool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#license_type MssqlElasticpool#license_type}.
        :param maintenance_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#maintenance_configuration_name MssqlElasticpool#maintenance_configuration_name}.
        :param max_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_bytes MssqlElasticpool#max_size_bytes}.
        :param max_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_gb MssqlElasticpool#max_size_gb}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tags MssqlElasticpool#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#timeouts MssqlElasticpool#timeouts}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#zone_redundant MssqlElasticpool#zone_redundant}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(per_database_settings, dict):
            per_database_settings = MssqlElasticpoolPerDatabaseSettings(**per_database_settings)
        if isinstance(sku, dict):
            sku = MssqlElasticpoolSku(**sku)
        if isinstance(timeouts, dict):
            timeouts = MssqlElasticpoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MssqlElasticpoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument per_database_settings", value=per_database_settings, expected_type=type_hints["per_database_settings"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument maintenance_configuration_name", value=maintenance_configuration_name, expected_type=type_hints["maintenance_configuration_name"])
            check_type(argname="argument max_size_bytes", value=max_size_bytes, expected_type=type_hints["max_size_bytes"])
            check_type(argname="argument max_size_gb", value=max_size_gb, expected_type=type_hints["max_size_gb"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone_redundant", value=zone_redundant, expected_type=type_hints["zone_redundant"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "per_database_settings": per_database_settings,
            "resource_group_name": resource_group_name,
            "server_name": server_name,
            "sku": sku,
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
        if license_type is not None:
            self._values["license_type"] = license_type
        if maintenance_configuration_name is not None:
            self._values["maintenance_configuration_name"] = maintenance_configuration_name
        if max_size_bytes is not None:
            self._values["max_size_bytes"] = max_size_bytes
        if max_size_gb is not None:
            self._values["max_size_gb"] = max_size_gb
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zone_redundant is not None:
            self._values["zone_redundant"] = zone_redundant

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#location MssqlElasticpool#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def per_database_settings(self) -> "MssqlElasticpoolPerDatabaseSettings":
        '''per_database_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#per_database_settings MssqlElasticpool#per_database_settings}
        '''
        result = self._values.get("per_database_settings")
        assert result is not None, "Required property 'per_database_settings' is missing"
        return typing.cast("MssqlElasticpoolPerDatabaseSettings", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#resource_group_name MssqlElasticpool#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#server_name MssqlElasticpool#server_name}.'''
        result = self._values.get("server_name")
        assert result is not None, "Required property 'server_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "MssqlElasticpoolSku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#sku MssqlElasticpool#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("MssqlElasticpoolSku", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#id MssqlElasticpool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#license_type MssqlElasticpool#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#maintenance_configuration_name MssqlElasticpool#maintenance_configuration_name}.'''
        result = self._values.get("maintenance_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_bytes MssqlElasticpool#max_size_bytes}.'''
        result = self._values.get("max_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_size_gb MssqlElasticpool#max_size_gb}.'''
        result = self._values.get("max_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tags MssqlElasticpool#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MssqlElasticpoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#timeouts MssqlElasticpool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlElasticpoolTimeouts"], result)

    @builtins.property
    def zone_redundant(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#zone_redundant MssqlElasticpool#zone_redundant}.'''
        result = self._values.get("zone_redundant")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlElasticpoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolPerDatabaseSettings",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class MssqlElasticpoolPerDatabaseSettings:
    def __init__(self, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> None:
        '''
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_capacity MssqlElasticpool#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#min_capacity MssqlElasticpool#min_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlElasticpoolPerDatabaseSettings.__init__)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
        }

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#max_capacity MssqlElasticpool#max_capacity}.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#min_capacity MssqlElasticpool#min_capacity}.'''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlElasticpoolPerDatabaseSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlElasticpoolPerDatabaseSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolPerDatabaseSettingsOutputReference",
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
            type_hints = typing.get_type_hints(MssqlElasticpoolPerDatabaseSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolPerDatabaseSettingsOutputReference, "max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolPerDatabaseSettingsOutputReference, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlElasticpoolPerDatabaseSettings]:
        return typing.cast(typing.Optional[MssqlElasticpoolPerDatabaseSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlElasticpoolPerDatabaseSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolPerDatabaseSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolSku",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "name": "name",
        "tier": "tier",
        "family": "family",
    },
)
class MssqlElasticpoolSku:
    def __init__(
        self,
        *,
        capacity: jsii.Number,
        name: builtins.str,
        tier: builtins.str,
        family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#capacity MssqlElasticpool#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tier MssqlElasticpool#tier}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#family MssqlElasticpool#family}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlElasticpoolSku.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "name": name,
            "tier": tier,
        }
        if family is not None:
            self._values["family"] = family

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#capacity MssqlElasticpool#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#name MssqlElasticpool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#tier MssqlElasticpool#tier}.'''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#family MssqlElasticpool#family}.'''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlElasticpoolSku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlElasticpoolSkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolSkuOutputReference",
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
            type_hints = typing.get_type_hints(MssqlElasticpoolSkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFamily")
    def reset_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFamily", []))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolSkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolSkuOutputReference, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolSkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolSkuOutputReference, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlElasticpoolSku]:
        return typing.cast(typing.Optional[MssqlElasticpoolSku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MssqlElasticpoolSku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolSkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlElasticpoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#create MssqlElasticpool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#delete MssqlElasticpool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#read MssqlElasticpool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#update MssqlElasticpool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlElasticpoolTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#create MssqlElasticpool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#delete MssqlElasticpool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#read MssqlElasticpool#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool#update MssqlElasticpool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlElasticpoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlElasticpoolTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlElasticpool.MssqlElasticpoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MssqlElasticpoolTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MssqlElasticpoolTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlElasticpoolTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlElasticpoolTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlElasticpoolTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlElasticpool",
    "MssqlElasticpoolConfig",
    "MssqlElasticpoolPerDatabaseSettings",
    "MssqlElasticpoolPerDatabaseSettingsOutputReference",
    "MssqlElasticpoolSku",
    "MssqlElasticpoolSkuOutputReference",
    "MssqlElasticpoolTimeouts",
    "MssqlElasticpoolTimeoutsOutputReference",
]

publication.publish()
