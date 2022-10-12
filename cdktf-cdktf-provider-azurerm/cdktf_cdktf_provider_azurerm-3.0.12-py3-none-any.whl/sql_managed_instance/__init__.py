'''
# `azurerm_sql_managed_instance`

Refer to the Terraform Registory for docs: [`azurerm_sql_managed_instance`](https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance).
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


class SqlManagedInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance azurerm_sql_managed_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        administrator_login: builtins.str,
        administrator_login_password: builtins.str,
        license_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        storage_size_in_gb: jsii.Number,
        subnet_id: builtins.str,
        vcores: jsii.Number,
        collation: typing.Optional[builtins.str] = None,
        dns_zone_partner_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SqlManagedInstanceIdentity", typing.Dict[str, typing.Any]]] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        proxy_override: typing.Optional[builtins.str] = None,
        public_data_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_account_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SqlManagedInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance azurerm_sql_managed_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login SqlManagedInstance#administrator_login}.
        :param administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login_password SqlManagedInstance#administrator_login_password}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#license_type SqlManagedInstance#license_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#location SqlManagedInstance#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#name SqlManagedInstance#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#resource_group_name SqlManagedInstance#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#sku_name SqlManagedInstance#sku_name}.
        :param storage_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_size_in_gb SqlManagedInstance#storage_size_in_gb}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#subnet_id SqlManagedInstance#subnet_id}.
        :param vcores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#vcores SqlManagedInstance#vcores}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#collation SqlManagedInstance#collation}.
        :param dns_zone_partner_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#dns_zone_partner_id SqlManagedInstance#dns_zone_partner_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#id SqlManagedInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#identity SqlManagedInstance#identity}
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#minimum_tls_version SqlManagedInstance#minimum_tls_version}.
        :param proxy_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#proxy_override SqlManagedInstance#proxy_override}.
        :param public_data_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#public_data_endpoint_enabled SqlManagedInstance#public_data_endpoint_enabled}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_account_type SqlManagedInstance#storage_account_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#tags SqlManagedInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timeouts SqlManagedInstance#timeouts}
        :param timezone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timezone_id SqlManagedInstance#timezone_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlManagedInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlManagedInstanceConfig(
            administrator_login=administrator_login,
            administrator_login_password=administrator_login_password,
            license_type=license_type,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            storage_size_in_gb=storage_size_in_gb,
            subnet_id=subnet_id,
            vcores=vcores,
            collation=collation,
            dns_zone_partner_id=dns_zone_partner_id,
            id=id,
            identity=identity,
            minimum_tls_version=minimum_tls_version,
            proxy_override=proxy_override,
            public_data_endpoint_enabled=public_data_endpoint_enabled,
            storage_account_type=storage_account_type,
            tags=tags,
            timeouts=timeouts,
            timezone_id=timezone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#type SqlManagedInstance#type}.
        '''
        value = SqlManagedInstanceIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#create SqlManagedInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#delete SqlManagedInstance#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#read SqlManagedInstance#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#update SqlManagedInstance#update}.
        '''
        value = SqlManagedInstanceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetDnsZonePartnerId")
    def reset_dns_zone_partner_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsZonePartnerId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetProxyOverride")
    def reset_proxy_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyOverride", []))

    @jsii.member(jsii_name="resetPublicDataEndpointEnabled")
    def reset_public_data_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicDataEndpointEnabled", []))

    @jsii.member(jsii_name="resetStorageAccountType")
    def reset_storage_account_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezoneId")
    def reset_timezone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezoneId", []))

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
    @jsii.member(jsii_name="identity")
    def identity(self) -> "SqlManagedInstanceIdentityOutputReference":
        return typing.cast("SqlManagedInstanceIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SqlManagedInstanceTimeoutsOutputReference":
        return typing.cast("SqlManagedInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="administratorLoginInput")
    def administrator_login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorLoginPasswordInput")
    def administrator_login_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorLoginPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsZonePartnerIdInput")
    def dns_zone_partner_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsZonePartnerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["SqlManagedInstanceIdentity"]:
        return typing.cast(typing.Optional["SqlManagedInstanceIdentity"], jsii.get(self, "identityInput"))

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
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyOverrideInput")
    def proxy_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="publicDataEndpointEnabledInput")
    def public_data_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicDataEndpointEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageSizeInGbInput")
    def storage_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SqlManagedInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SqlManagedInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneIdInput")
    def timezone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vcoresInput")
    def vcores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vcoresInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorLogin")
    def administrator_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorLogin"))

    @administrator_login.setter
    def administrator_login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "administrator_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorLogin", value)

    @builtins.property
    @jsii.member(jsii_name="administratorLoginPassword")
    def administrator_login_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorLoginPassword"))

    @administrator_login_password.setter
    def administrator_login_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "administrator_login_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorLoginPassword", value)

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "collation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="dnsZonePartnerId")
    def dns_zone_partner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsZonePartnerId"))

    @dns_zone_partner_id.setter
    def dns_zone_partner_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "dns_zone_partner_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsZonePartnerId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="proxyOverride")
    def proxy_override(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyOverride"))

    @proxy_override.setter
    def proxy_override(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "proxy_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyOverride", value)

    @builtins.property
    @jsii.member(jsii_name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicDataEndpointEnabled"))

    @public_data_endpoint_enabled.setter
    def public_data_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "public_data_endpoint_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDataEndpointEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="storageSizeInGb")
    def storage_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageSizeInGb"))

    @storage_size_in_gb.setter
    def storage_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "storage_size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageSizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timezoneId")
    def timezone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezoneId"))

    @timezone_id.setter
    def timezone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "timezone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezoneId", value)

    @builtins.property
    @jsii.member(jsii_name="vcores")
    def vcores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vcores"))

    @vcores.setter
    def vcores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstance, "vcores").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcores", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "administrator_login": "administratorLogin",
        "administrator_login_password": "administratorLoginPassword",
        "license_type": "licenseType",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "storage_size_in_gb": "storageSizeInGb",
        "subnet_id": "subnetId",
        "vcores": "vcores",
        "collation": "collation",
        "dns_zone_partner_id": "dnsZonePartnerId",
        "id": "id",
        "identity": "identity",
        "minimum_tls_version": "minimumTlsVersion",
        "proxy_override": "proxyOverride",
        "public_data_endpoint_enabled": "publicDataEndpointEnabled",
        "storage_account_type": "storageAccountType",
        "tags": "tags",
        "timeouts": "timeouts",
        "timezone_id": "timezoneId",
    },
)
class SqlManagedInstanceConfig(cdktf.TerraformMetaArguments):
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
        administrator_login: builtins.str,
        administrator_login_password: builtins.str,
        license_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        storage_size_in_gb: jsii.Number,
        subnet_id: builtins.str,
        vcores: jsii.Number,
        collation: typing.Optional[builtins.str] = None,
        dns_zone_partner_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SqlManagedInstanceIdentity", typing.Dict[str, typing.Any]]] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        proxy_override: typing.Optional[builtins.str] = None,
        public_data_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_account_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SqlManagedInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login SqlManagedInstance#administrator_login}.
        :param administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login_password SqlManagedInstance#administrator_login_password}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#license_type SqlManagedInstance#license_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#location SqlManagedInstance#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#name SqlManagedInstance#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#resource_group_name SqlManagedInstance#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#sku_name SqlManagedInstance#sku_name}.
        :param storage_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_size_in_gb SqlManagedInstance#storage_size_in_gb}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#subnet_id SqlManagedInstance#subnet_id}.
        :param vcores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#vcores SqlManagedInstance#vcores}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#collation SqlManagedInstance#collation}.
        :param dns_zone_partner_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#dns_zone_partner_id SqlManagedInstance#dns_zone_partner_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#id SqlManagedInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#identity SqlManagedInstance#identity}
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#minimum_tls_version SqlManagedInstance#minimum_tls_version}.
        :param proxy_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#proxy_override SqlManagedInstance#proxy_override}.
        :param public_data_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#public_data_endpoint_enabled SqlManagedInstance#public_data_endpoint_enabled}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_account_type SqlManagedInstance#storage_account_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#tags SqlManagedInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timeouts SqlManagedInstance#timeouts}
        :param timezone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timezone_id SqlManagedInstance#timezone_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = SqlManagedInstanceIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = SqlManagedInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SqlManagedInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument administrator_login", value=administrator_login, expected_type=type_hints["administrator_login"])
            check_type(argname="argument administrator_login_password", value=administrator_login_password, expected_type=type_hints["administrator_login_password"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument storage_size_in_gb", value=storage_size_in_gb, expected_type=type_hints["storage_size_in_gb"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument vcores", value=vcores, expected_type=type_hints["vcores"])
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument dns_zone_partner_id", value=dns_zone_partner_id, expected_type=type_hints["dns_zone_partner_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument proxy_override", value=proxy_override, expected_type=type_hints["proxy_override"])
            check_type(argname="argument public_data_endpoint_enabled", value=public_data_endpoint_enabled, expected_type=type_hints["public_data_endpoint_enabled"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone_id", value=timezone_id, expected_type=type_hints["timezone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "administrator_login": administrator_login,
            "administrator_login_password": administrator_login_password,
            "license_type": license_type,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "storage_size_in_gb": storage_size_in_gb,
            "subnet_id": subnet_id,
            "vcores": vcores,
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
        if collation is not None:
            self._values["collation"] = collation
        if dns_zone_partner_id is not None:
            self._values["dns_zone_partner_id"] = dns_zone_partner_id
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if proxy_override is not None:
            self._values["proxy_override"] = proxy_override
        if public_data_endpoint_enabled is not None:
            self._values["public_data_endpoint_enabled"] = public_data_endpoint_enabled
        if storage_account_type is not None:
            self._values["storage_account_type"] = storage_account_type
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone_id is not None:
            self._values["timezone_id"] = timezone_id

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
    def administrator_login(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login SqlManagedInstance#administrator_login}.'''
        result = self._values.get("administrator_login")
        assert result is not None, "Required property 'administrator_login' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administrator_login_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#administrator_login_password SqlManagedInstance#administrator_login_password}.'''
        result = self._values.get("administrator_login_password")
        assert result is not None, "Required property 'administrator_login_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def license_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#license_type SqlManagedInstance#license_type}.'''
        result = self._values.get("license_type")
        assert result is not None, "Required property 'license_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#location SqlManagedInstance#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#name SqlManagedInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#resource_group_name SqlManagedInstance#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#sku_name SqlManagedInstance#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_size_in_gb SqlManagedInstance#storage_size_in_gb}.'''
        result = self._values.get("storage_size_in_gb")
        assert result is not None, "Required property 'storage_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#subnet_id SqlManagedInstance#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vcores(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#vcores SqlManagedInstance#vcores}.'''
        result = self._values.get("vcores")
        assert result is not None, "Required property 'vcores' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#collation SqlManagedInstance#collation}.'''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_zone_partner_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#dns_zone_partner_id SqlManagedInstance#dns_zone_partner_id}.'''
        result = self._values.get("dns_zone_partner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#id SqlManagedInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["SqlManagedInstanceIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#identity SqlManagedInstance#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["SqlManagedInstanceIdentity"], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#minimum_tls_version SqlManagedInstance#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#proxy_override SqlManagedInstance#proxy_override}.'''
        result = self._values.get("proxy_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_data_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#public_data_endpoint_enabled SqlManagedInstance#public_data_endpoint_enabled}.'''
        result = self._values.get("public_data_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def storage_account_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#storage_account_type SqlManagedInstance#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#tags SqlManagedInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SqlManagedInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timeouts SqlManagedInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SqlManagedInstanceTimeouts"], result)

    @builtins.property
    def timezone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#timezone_id SqlManagedInstance#timezone_id}.'''
        result = self._values.get("timezone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlManagedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstanceIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class SqlManagedInstanceIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#type SqlManagedInstance#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlManagedInstanceIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#type SqlManagedInstance#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlManagedInstanceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlManagedInstanceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstanceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(SqlManagedInstanceIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlManagedInstanceIdentity]:
        return typing.cast(typing.Optional[SqlManagedInstanceIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlManagedInstanceIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SqlManagedInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#create SqlManagedInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#delete SqlManagedInstance#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#read SqlManagedInstance#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#update SqlManagedInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlManagedInstanceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#create SqlManagedInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#delete SqlManagedInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#read SqlManagedInstance#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_managed_instance#update SqlManagedInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlManagedInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlManagedInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlManagedInstance.SqlManagedInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SqlManagedInstanceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlManagedInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlManagedInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlManagedInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlManagedInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlManagedInstance",
    "SqlManagedInstanceConfig",
    "SqlManagedInstanceIdentity",
    "SqlManagedInstanceIdentityOutputReference",
    "SqlManagedInstanceTimeouts",
    "SqlManagedInstanceTimeoutsOutputReference",
]

publication.publish()
