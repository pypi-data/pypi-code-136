'''
# `azurerm_postgresql_flexible_server`

Refer to the Terraform Registory for docs: [`azurerm_postgresql_flexible_server`](https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server).
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


class PostgresqlFlexibleServer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server azurerm_postgresql_flexible_server}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        administrator_login: typing.Optional[builtins.str] = None,
        administrator_password: typing.Optional[builtins.str] = None,
        backup_retention_days: typing.Optional[jsii.Number] = None,
        create_mode: typing.Optional[builtins.str] = None,
        delegated_subnet_id: typing.Optional[builtins.str] = None,
        geo_redundant_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        high_availability: typing.Optional[typing.Union["PostgresqlFlexibleServerHighAvailability", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["PostgresqlFlexibleServerMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        point_in_time_restore_time_in_utc: typing.Optional[builtins.str] = None,
        private_dns_zone_id: typing.Optional[builtins.str] = None,
        sku_name: typing.Optional[builtins.str] = None,
        source_server_id: typing.Optional[builtins.str] = None,
        storage_mb: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PostgresqlFlexibleServerTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server azurerm_postgresql_flexible_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#location PostgresqlFlexibleServer#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#name PostgresqlFlexibleServer#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#resource_group_name PostgresqlFlexibleServer#resource_group_name}.
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_login PostgresqlFlexibleServer#administrator_login}.
        :param administrator_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_password PostgresqlFlexibleServer#administrator_password}.
        :param backup_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#backup_retention_days PostgresqlFlexibleServer#backup_retention_days}.
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create_mode PostgresqlFlexibleServer#create_mode}.
        :param delegated_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delegated_subnet_id PostgresqlFlexibleServer#delegated_subnet_id}.
        :param geo_redundant_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#geo_redundant_backup_enabled PostgresqlFlexibleServer#geo_redundant_backup_enabled}.
        :param high_availability: high_availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#high_availability PostgresqlFlexibleServer#high_availability}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#id PostgresqlFlexibleServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#maintenance_window PostgresqlFlexibleServer#maintenance_window}
        :param point_in_time_restore_time_in_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#point_in_time_restore_time_in_utc PostgresqlFlexibleServer#point_in_time_restore_time_in_utc}.
        :param private_dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#private_dns_zone_id PostgresqlFlexibleServer#private_dns_zone_id}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#sku_name PostgresqlFlexibleServer#sku_name}.
        :param source_server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#source_server_id PostgresqlFlexibleServer#source_server_id}.
        :param storage_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#storage_mb PostgresqlFlexibleServer#storage_mb}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#tags PostgresqlFlexibleServer#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#timeouts PostgresqlFlexibleServer#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#version PostgresqlFlexibleServer#version}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#zone PostgresqlFlexibleServer#zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlFlexibleServer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PostgresqlFlexibleServerConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            administrator_login=administrator_login,
            administrator_password=administrator_password,
            backup_retention_days=backup_retention_days,
            create_mode=create_mode,
            delegated_subnet_id=delegated_subnet_id,
            geo_redundant_backup_enabled=geo_redundant_backup_enabled,
            high_availability=high_availability,
            id=id,
            maintenance_window=maintenance_window,
            point_in_time_restore_time_in_utc=point_in_time_restore_time_in_utc,
            private_dns_zone_id=private_dns_zone_id,
            sku_name=sku_name,
            source_server_id=source_server_id,
            storage_mb=storage_mb,
            tags=tags,
            timeouts=timeouts,
            version=version,
            zone=zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHighAvailability")
    def put_high_availability(
        self,
        *,
        mode: builtins.str,
        standby_availability_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#mode PostgresqlFlexibleServer#mode}.
        :param standby_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#standby_availability_zone PostgresqlFlexibleServer#standby_availability_zone}.
        '''
        value = PostgresqlFlexibleServerHighAvailability(
            mode=mode, standby_availability_zone=standby_availability_zone
        )

        return typing.cast(None, jsii.invoke(self, "putHighAvailability", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day_of_week: typing.Optional[jsii.Number] = None,
        start_hour: typing.Optional[jsii.Number] = None,
        start_minute: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#day_of_week PostgresqlFlexibleServer#day_of_week}.
        :param start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_hour PostgresqlFlexibleServer#start_hour}.
        :param start_minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_minute PostgresqlFlexibleServer#start_minute}.
        '''
        value = PostgresqlFlexibleServerMaintenanceWindow(
            day_of_week=day_of_week, start_hour=start_hour, start_minute=start_minute
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create PostgresqlFlexibleServer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delete PostgresqlFlexibleServer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#read PostgresqlFlexibleServer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#update PostgresqlFlexibleServer#update}.
        '''
        value = PostgresqlFlexibleServerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdministratorLogin")
    def reset_administrator_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdministratorLogin", []))

    @jsii.member(jsii_name="resetAdministratorPassword")
    def reset_administrator_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdministratorPassword", []))

    @jsii.member(jsii_name="resetBackupRetentionDays")
    def reset_backup_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRetentionDays", []))

    @jsii.member(jsii_name="resetCreateMode")
    def reset_create_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateMode", []))

    @jsii.member(jsii_name="resetDelegatedSubnetId")
    def reset_delegated_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelegatedSubnetId", []))

    @jsii.member(jsii_name="resetGeoRedundantBackupEnabled")
    def reset_geo_redundant_backup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoRedundantBackupEnabled", []))

    @jsii.member(jsii_name="resetHighAvailability")
    def reset_high_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighAvailability", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetPointInTimeRestoreTimeInUtc")
    def reset_point_in_time_restore_time_in_utc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRestoreTimeInUtc", []))

    @jsii.member(jsii_name="resetPrivateDnsZoneId")
    def reset_private_dns_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateDnsZoneId", []))

    @jsii.member(jsii_name="resetSkuName")
    def reset_sku_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkuName", []))

    @jsii.member(jsii_name="resetSourceServerId")
    def reset_source_server_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServerId", []))

    @jsii.member(jsii_name="resetStorageMb")
    def reset_storage_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageMb", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="highAvailability")
    def high_availability(
        self,
    ) -> "PostgresqlFlexibleServerHighAvailabilityOutputReference":
        return typing.cast("PostgresqlFlexibleServerHighAvailabilityOutputReference", jsii.get(self, "highAvailability"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> "PostgresqlFlexibleServerMaintenanceWindowOutputReference":
        return typing.cast("PostgresqlFlexibleServerMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "publicNetworkAccessEnabled"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PostgresqlFlexibleServerTimeoutsOutputReference":
        return typing.cast("PostgresqlFlexibleServerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="administratorLoginInput")
    def administrator_login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorPasswordInput")
    def administrator_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRetentionDaysInput")
    def backup_retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="createModeInput")
    def create_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createModeInput"))

    @builtins.property
    @jsii.member(jsii_name="delegatedSubnetIdInput")
    def delegated_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delegatedSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="geoRedundantBackupEnabledInput")
    def geo_redundant_backup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "geoRedundantBackupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="highAvailabilityInput")
    def high_availability_input(
        self,
    ) -> typing.Optional["PostgresqlFlexibleServerHighAvailability"]:
        return typing.cast(typing.Optional["PostgresqlFlexibleServerHighAvailability"], jsii.get(self, "highAvailabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["PostgresqlFlexibleServerMaintenanceWindow"]:
        return typing.cast(typing.Optional["PostgresqlFlexibleServerMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRestoreTimeInUtcInput")
    def point_in_time_restore_time_in_utc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pointInTimeRestoreTimeInUtcInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneIdInput")
    def private_dns_zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateDnsZoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServerIdInput")
    def source_server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageMbInput")
    def storage_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageMbInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PostgresqlFlexibleServerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PostgresqlFlexibleServerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorLogin")
    def administrator_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorLogin"))

    @administrator_login.setter
    def administrator_login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "administrator_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorLogin", value)

    @builtins.property
    @jsii.member(jsii_name="administratorPassword")
    def administrator_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorPassword"))

    @administrator_password.setter
    def administrator_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "administrator_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorPassword", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionDays")
    def backup_retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupRetentionDays"))

    @backup_retention_days.setter
    def backup_retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "backup_retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="createMode")
    def create_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createMode"))

    @create_mode.setter
    def create_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "create_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createMode", value)

    @builtins.property
    @jsii.member(jsii_name="delegatedSubnetId")
    def delegated_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delegatedSubnetId"))

    @delegated_subnet_id.setter
    def delegated_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "delegated_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delegatedSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="geoRedundantBackupEnabled")
    def geo_redundant_backup_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "geoRedundantBackupEnabled"))

    @geo_redundant_backup_enabled.setter
    def geo_redundant_backup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "geo_redundant_backup_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoRedundantBackupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRestoreTimeInUtc")
    def point_in_time_restore_time_in_utc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pointInTimeRestoreTimeInUtc"))

    @point_in_time_restore_time_in_utc.setter
    def point_in_time_restore_time_in_utc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "point_in_time_restore_time_in_utc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeRestoreTimeInUtc", value)

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneId")
    def private_dns_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDnsZoneId"))

    @private_dns_zone_id.setter
    def private_dns_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "private_dns_zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateDnsZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServerId")
    def source_server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceServerId"))

    @source_server_id.setter
    def source_server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "source_server_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServerId", value)

    @builtins.property
    @jsii.member(jsii_name="storageMb")
    def storage_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageMb"))

    @storage_mb.setter
    def storage_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "storage_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageMb", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServer, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerConfig",
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
        "resource_group_name": "resourceGroupName",
        "administrator_login": "administratorLogin",
        "administrator_password": "administratorPassword",
        "backup_retention_days": "backupRetentionDays",
        "create_mode": "createMode",
        "delegated_subnet_id": "delegatedSubnetId",
        "geo_redundant_backup_enabled": "geoRedundantBackupEnabled",
        "high_availability": "highAvailability",
        "id": "id",
        "maintenance_window": "maintenanceWindow",
        "point_in_time_restore_time_in_utc": "pointInTimeRestoreTimeInUtc",
        "private_dns_zone_id": "privateDnsZoneId",
        "sku_name": "skuName",
        "source_server_id": "sourceServerId",
        "storage_mb": "storageMb",
        "tags": "tags",
        "timeouts": "timeouts",
        "version": "version",
        "zone": "zone",
    },
)
class PostgresqlFlexibleServerConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        administrator_login: typing.Optional[builtins.str] = None,
        administrator_password: typing.Optional[builtins.str] = None,
        backup_retention_days: typing.Optional[jsii.Number] = None,
        create_mode: typing.Optional[builtins.str] = None,
        delegated_subnet_id: typing.Optional[builtins.str] = None,
        geo_redundant_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        high_availability: typing.Optional[typing.Union["PostgresqlFlexibleServerHighAvailability", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["PostgresqlFlexibleServerMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        point_in_time_restore_time_in_utc: typing.Optional[builtins.str] = None,
        private_dns_zone_id: typing.Optional[builtins.str] = None,
        sku_name: typing.Optional[builtins.str] = None,
        source_server_id: typing.Optional[builtins.str] = None,
        storage_mb: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PostgresqlFlexibleServerTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#location PostgresqlFlexibleServer#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#name PostgresqlFlexibleServer#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#resource_group_name PostgresqlFlexibleServer#resource_group_name}.
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_login PostgresqlFlexibleServer#administrator_login}.
        :param administrator_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_password PostgresqlFlexibleServer#administrator_password}.
        :param backup_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#backup_retention_days PostgresqlFlexibleServer#backup_retention_days}.
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create_mode PostgresqlFlexibleServer#create_mode}.
        :param delegated_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delegated_subnet_id PostgresqlFlexibleServer#delegated_subnet_id}.
        :param geo_redundant_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#geo_redundant_backup_enabled PostgresqlFlexibleServer#geo_redundant_backup_enabled}.
        :param high_availability: high_availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#high_availability PostgresqlFlexibleServer#high_availability}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#id PostgresqlFlexibleServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#maintenance_window PostgresqlFlexibleServer#maintenance_window}
        :param point_in_time_restore_time_in_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#point_in_time_restore_time_in_utc PostgresqlFlexibleServer#point_in_time_restore_time_in_utc}.
        :param private_dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#private_dns_zone_id PostgresqlFlexibleServer#private_dns_zone_id}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#sku_name PostgresqlFlexibleServer#sku_name}.
        :param source_server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#source_server_id PostgresqlFlexibleServer#source_server_id}.
        :param storage_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#storage_mb PostgresqlFlexibleServer#storage_mb}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#tags PostgresqlFlexibleServer#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#timeouts PostgresqlFlexibleServer#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#version PostgresqlFlexibleServer#version}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#zone PostgresqlFlexibleServer#zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(high_availability, dict):
            high_availability = PostgresqlFlexibleServerHighAvailability(**high_availability)
        if isinstance(maintenance_window, dict):
            maintenance_window = PostgresqlFlexibleServerMaintenanceWindow(**maintenance_window)
        if isinstance(timeouts, dict):
            timeouts = PostgresqlFlexibleServerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument administrator_login", value=administrator_login, expected_type=type_hints["administrator_login"])
            check_type(argname="argument administrator_password", value=administrator_password, expected_type=type_hints["administrator_password"])
            check_type(argname="argument backup_retention_days", value=backup_retention_days, expected_type=type_hints["backup_retention_days"])
            check_type(argname="argument create_mode", value=create_mode, expected_type=type_hints["create_mode"])
            check_type(argname="argument delegated_subnet_id", value=delegated_subnet_id, expected_type=type_hints["delegated_subnet_id"])
            check_type(argname="argument geo_redundant_backup_enabled", value=geo_redundant_backup_enabled, expected_type=type_hints["geo_redundant_backup_enabled"])
            check_type(argname="argument high_availability", value=high_availability, expected_type=type_hints["high_availability"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument point_in_time_restore_time_in_utc", value=point_in_time_restore_time_in_utc, expected_type=type_hints["point_in_time_restore_time_in_utc"])
            check_type(argname="argument private_dns_zone_id", value=private_dns_zone_id, expected_type=type_hints["private_dns_zone_id"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument source_server_id", value=source_server_id, expected_type=type_hints["source_server_id"])
            check_type(argname="argument storage_mb", value=storage_mb, expected_type=type_hints["storage_mb"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if administrator_login is not None:
            self._values["administrator_login"] = administrator_login
        if administrator_password is not None:
            self._values["administrator_password"] = administrator_password
        if backup_retention_days is not None:
            self._values["backup_retention_days"] = backup_retention_days
        if create_mode is not None:
            self._values["create_mode"] = create_mode
        if delegated_subnet_id is not None:
            self._values["delegated_subnet_id"] = delegated_subnet_id
        if geo_redundant_backup_enabled is not None:
            self._values["geo_redundant_backup_enabled"] = geo_redundant_backup_enabled
        if high_availability is not None:
            self._values["high_availability"] = high_availability
        if id is not None:
            self._values["id"] = id
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if point_in_time_restore_time_in_utc is not None:
            self._values["point_in_time_restore_time_in_utc"] = point_in_time_restore_time_in_utc
        if private_dns_zone_id is not None:
            self._values["private_dns_zone_id"] = private_dns_zone_id
        if sku_name is not None:
            self._values["sku_name"] = sku_name
        if source_server_id is not None:
            self._values["source_server_id"] = source_server_id
        if storage_mb is not None:
            self._values["storage_mb"] = storage_mb
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version
        if zone is not None:
            self._values["zone"] = zone

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#location PostgresqlFlexibleServer#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#name PostgresqlFlexibleServer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#resource_group_name PostgresqlFlexibleServer#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administrator_login(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_login PostgresqlFlexibleServer#administrator_login}.'''
        result = self._values.get("administrator_login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def administrator_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#administrator_password PostgresqlFlexibleServer#administrator_password}.'''
        result = self._values.get("administrator_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#backup_retention_days PostgresqlFlexibleServer#backup_retention_days}.'''
        result = self._values.get("backup_retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def create_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create_mode PostgresqlFlexibleServer#create_mode}.'''
        result = self._values.get("create_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delegated_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delegated_subnet_id PostgresqlFlexibleServer#delegated_subnet_id}.'''
        result = self._values.get("delegated_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def geo_redundant_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#geo_redundant_backup_enabled PostgresqlFlexibleServer#geo_redundant_backup_enabled}.'''
        result = self._values.get("geo_redundant_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def high_availability(
        self,
    ) -> typing.Optional["PostgresqlFlexibleServerHighAvailability"]:
        '''high_availability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#high_availability PostgresqlFlexibleServer#high_availability}
        '''
        result = self._values.get("high_availability")
        return typing.cast(typing.Optional["PostgresqlFlexibleServerHighAvailability"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#id PostgresqlFlexibleServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional["PostgresqlFlexibleServerMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#maintenance_window PostgresqlFlexibleServer#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["PostgresqlFlexibleServerMaintenanceWindow"], result)

    @builtins.property
    def point_in_time_restore_time_in_utc(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#point_in_time_restore_time_in_utc PostgresqlFlexibleServer#point_in_time_restore_time_in_utc}.'''
        result = self._values.get("point_in_time_restore_time_in_utc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_dns_zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#private_dns_zone_id PostgresqlFlexibleServer#private_dns_zone_id}.'''
        result = self._values.get("private_dns_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#sku_name PostgresqlFlexibleServer#sku_name}.'''
        result = self._values.get("sku_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_server_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#source_server_id PostgresqlFlexibleServer#source_server_id}.'''
        result = self._values.get("source_server_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#storage_mb PostgresqlFlexibleServer#storage_mb}.'''
        result = self._values.get("storage_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#tags PostgresqlFlexibleServer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PostgresqlFlexibleServerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#timeouts PostgresqlFlexibleServer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PostgresqlFlexibleServerTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#version PostgresqlFlexibleServer#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#zone PostgresqlFlexibleServer#zone}.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlFlexibleServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerHighAvailability",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "standby_availability_zone": "standbyAvailabilityZone",
    },
)
class PostgresqlFlexibleServerHighAvailability:
    def __init__(
        self,
        *,
        mode: builtins.str,
        standby_availability_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#mode PostgresqlFlexibleServer#mode}.
        :param standby_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#standby_availability_zone PostgresqlFlexibleServer#standby_availability_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerHighAvailability.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument standby_availability_zone", value=standby_availability_zone, expected_type=type_hints["standby_availability_zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if standby_availability_zone is not None:
            self._values["standby_availability_zone"] = standby_availability_zone

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#mode PostgresqlFlexibleServer#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def standby_availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#standby_availability_zone PostgresqlFlexibleServer#standby_availability_zone}.'''
        result = self._values.get("standby_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlFlexibleServerHighAvailability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PostgresqlFlexibleServerHighAvailabilityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerHighAvailabilityOutputReference",
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
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerHighAvailabilityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStandbyAvailabilityZone")
    def reset_standby_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandbyAvailabilityZone", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="standbyAvailabilityZoneInput")
    def standby_availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "standbyAvailabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerHighAvailabilityOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "standbyAvailabilityZone"))

    @standby_availability_zone.setter
    def standby_availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerHighAvailabilityOutputReference, "standby_availability_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standbyAvailabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PostgresqlFlexibleServerHighAvailability]:
        return typing.cast(typing.Optional[PostgresqlFlexibleServerHighAvailability], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PostgresqlFlexibleServerHighAvailability],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerHighAvailabilityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "start_hour": "startHour",
        "start_minute": "startMinute",
    },
)
class PostgresqlFlexibleServerMaintenanceWindow:
    def __init__(
        self,
        *,
        day_of_week: typing.Optional[jsii.Number] = None,
        start_hour: typing.Optional[jsii.Number] = None,
        start_minute: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#day_of_week PostgresqlFlexibleServer#day_of_week}.
        :param start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_hour PostgresqlFlexibleServer#start_hour}.
        :param start_minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_minute PostgresqlFlexibleServer#start_minute}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerMaintenanceWindow.__init__)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument start_hour", value=start_hour, expected_type=type_hints["start_hour"])
            check_type(argname="argument start_minute", value=start_minute, expected_type=type_hints["start_minute"])
        self._values: typing.Dict[str, typing.Any] = {}
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if start_hour is not None:
            self._values["start_hour"] = start_hour
        if start_minute is not None:
            self._values["start_minute"] = start_minute

    @builtins.property
    def day_of_week(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#day_of_week PostgresqlFlexibleServer#day_of_week}.'''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_hour(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_hour PostgresqlFlexibleServer#start_hour}.'''
        result = self._values.get("start_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_minute(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#start_minute PostgresqlFlexibleServer#start_minute}.'''
        result = self._values.get("start_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlFlexibleServerMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PostgresqlFlexibleServerMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDayOfWeek")
    def reset_day_of_week(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayOfWeek", []))

    @jsii.member(jsii_name="resetStartHour")
    def reset_start_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartHour", []))

    @jsii.member(jsii_name="resetStartMinute")
    def reset_start_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartMinute", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="startHourInput")
    def start_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startHourInput"))

    @builtins.property
    @jsii.member(jsii_name="startMinuteInput")
    def start_minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startMinuteInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerMaintenanceWindowOutputReference, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="startHour")
    def start_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startHour"))

    @start_hour.setter
    def start_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerMaintenanceWindowOutputReference, "start_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startHour", value)

    @builtins.property
    @jsii.member(jsii_name="startMinute")
    def start_minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startMinute"))

    @start_minute.setter
    def start_minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerMaintenanceWindowOutputReference, "start_minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startMinute", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PostgresqlFlexibleServerMaintenanceWindow]:
        return typing.cast(typing.Optional[PostgresqlFlexibleServerMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PostgresqlFlexibleServerMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class PostgresqlFlexibleServerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create PostgresqlFlexibleServer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delete PostgresqlFlexibleServer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#read PostgresqlFlexibleServer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#update PostgresqlFlexibleServer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#create PostgresqlFlexibleServer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#delete PostgresqlFlexibleServer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#read PostgresqlFlexibleServer#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/postgresql_flexible_server#update PostgresqlFlexibleServer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlFlexibleServerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PostgresqlFlexibleServerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.postgresqlFlexibleServer.PostgresqlFlexibleServerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(PostgresqlFlexibleServerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PostgresqlFlexibleServerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PostgresqlFlexibleServerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PostgresqlFlexibleServerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PostgresqlFlexibleServerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PostgresqlFlexibleServer",
    "PostgresqlFlexibleServerConfig",
    "PostgresqlFlexibleServerHighAvailability",
    "PostgresqlFlexibleServerHighAvailabilityOutputReference",
    "PostgresqlFlexibleServerMaintenanceWindow",
    "PostgresqlFlexibleServerMaintenanceWindowOutputReference",
    "PostgresqlFlexibleServerTimeouts",
    "PostgresqlFlexibleServerTimeoutsOutputReference",
]

publication.publish()
