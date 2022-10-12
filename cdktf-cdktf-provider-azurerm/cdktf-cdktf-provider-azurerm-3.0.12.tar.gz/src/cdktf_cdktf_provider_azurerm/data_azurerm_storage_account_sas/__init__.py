'''
# `data_azurerm_storage_account_sas`

Refer to the Terraform Registory for docs: [`data_azurerm_storage_account_sas`](https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas).
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


class DataAzurermStorageAccountSas(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSas",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas azurerm_storage_account_sas}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        connection_string: builtins.str,
        expiry: builtins.str,
        permissions: typing.Union["DataAzurermStorageAccountSasPermissions", typing.Dict[str, typing.Any]],
        resource_types: typing.Union["DataAzurermStorageAccountSasResourceTypes", typing.Dict[str, typing.Any]],
        services: typing.Union["DataAzurermStorageAccountSasServices", typing.Dict[str, typing.Any]],
        start: builtins.str,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_addresses: typing.Optional[builtins.str] = None,
        signed_version: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAzurermStorageAccountSasTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas azurerm_storage_account_sas} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#connection_string DataAzurermStorageAccountSas#connection_string}.
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#expiry DataAzurermStorageAccountSas#expiry}.
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#permissions DataAzurermStorageAccountSas#permissions}
        :param resource_types: resource_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#resource_types DataAzurermStorageAccountSas#resource_types}
        :param services: services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#services DataAzurermStorageAccountSas#services}
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#start DataAzurermStorageAccountSas#start}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#https_only DataAzurermStorageAccountSas#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#id DataAzurermStorageAccountSas#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#ip_addresses DataAzurermStorageAccountSas#ip_addresses}.
        :param signed_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#signed_version DataAzurermStorageAccountSas#signed_version}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#timeouts DataAzurermStorageAccountSas#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSas.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAzurermStorageAccountSasConfig(
            connection_string=connection_string,
            expiry=expiry,
            permissions=permissions,
            resource_types=resource_types,
            services=services,
            start=start,
            https_only=https_only,
            id=id,
            ip_addresses=ip_addresses,
            signed_version=signed_version,
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

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        *,
        add: typing.Union[builtins.bool, cdktf.IResolvable],
        create: typing.Union[builtins.bool, cdktf.IResolvable],
        delete: typing.Union[builtins.bool, cdktf.IResolvable],
        filter: typing.Union[builtins.bool, cdktf.IResolvable],
        list: typing.Union[builtins.bool, cdktf.IResolvable],
        process: typing.Union[builtins.bool, cdktf.IResolvable],
        read: typing.Union[builtins.bool, cdktf.IResolvable],
        tag: typing.Union[builtins.bool, cdktf.IResolvable],
        update: typing.Union[builtins.bool, cdktf.IResolvable],
        write: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param add: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#add DataAzurermStorageAccountSas#add}.
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#create DataAzurermStorageAccountSas#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#delete DataAzurermStorageAccountSas#delete}.
        :param filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#filter DataAzurermStorageAccountSas#filter}.
        :param list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#list DataAzurermStorageAccountSas#list}.
        :param process: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#process DataAzurermStorageAccountSas#process}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#tag DataAzurermStorageAccountSas#tag}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#update DataAzurermStorageAccountSas#update}.
        :param write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#write DataAzurermStorageAccountSas#write}.
        '''
        value = DataAzurermStorageAccountSasPermissions(
            add=add,
            create=create,
            delete=delete,
            filter=filter,
            list=list,
            process=process,
            read=read,
            tag=tag,
            update=update,
            write=write,
        )

        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="putResourceTypes")
    def put_resource_types(
        self,
        *,
        container: typing.Union[builtins.bool, cdktf.IResolvable],
        object: typing.Union[builtins.bool, cdktf.IResolvable],
        service: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#container DataAzurermStorageAccountSas#container}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#object DataAzurermStorageAccountSas#object}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#service DataAzurermStorageAccountSas#service}.
        '''
        value = DataAzurermStorageAccountSasResourceTypes(
            container=container, object=object, service=service
        )

        return typing.cast(None, jsii.invoke(self, "putResourceTypes", [value]))

    @jsii.member(jsii_name="putServices")
    def put_services(
        self,
        *,
        blob: typing.Union[builtins.bool, cdktf.IResolvable],
        file: typing.Union[builtins.bool, cdktf.IResolvable],
        queue: typing.Union[builtins.bool, cdktf.IResolvable],
        table: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param blob: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#blob DataAzurermStorageAccountSas#blob}.
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#file DataAzurermStorageAccountSas#file}.
        :param queue: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#queue DataAzurermStorageAccountSas#queue}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#table DataAzurermStorageAccountSas#table}.
        '''
        value = DataAzurermStorageAccountSasServices(
            blob=blob, file=file, queue=queue, table=table
        )

        return typing.cast(None, jsii.invoke(self, "putServices", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.
        '''
        value = DataAzurermStorageAccountSasTimeouts(read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetHttpsOnly")
    def reset_https_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpAddresses")
    def reset_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddresses", []))

    @jsii.member(jsii_name="resetSignedVersion")
    def reset_signed_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignedVersion", []))

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
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "DataAzurermStorageAccountSasPermissionsOutputReference":
        return typing.cast("DataAzurermStorageAccountSasPermissionsOutputReference", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypes")
    def resource_types(
        self,
    ) -> "DataAzurermStorageAccountSasResourceTypesOutputReference":
        return typing.cast("DataAzurermStorageAccountSasResourceTypesOutputReference", jsii.get(self, "resourceTypes"))

    @builtins.property
    @jsii.member(jsii_name="sas")
    def sas(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sas"))

    @builtins.property
    @jsii.member(jsii_name="services")
    def services(self) -> "DataAzurermStorageAccountSasServicesOutputReference":
        return typing.cast("DataAzurermStorageAccountSasServicesOutputReference", jsii.get(self, "services"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataAzurermStorageAccountSasTimeoutsOutputReference":
        return typing.cast("DataAzurermStorageAccountSasTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="expiryInput")
    def expiry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressesInput")
    def ip_addresses_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional["DataAzurermStorageAccountSasPermissions"]:
        return typing.cast(typing.Optional["DataAzurermStorageAccountSasPermissions"], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypesInput")
    def resource_types_input(
        self,
    ) -> typing.Optional["DataAzurermStorageAccountSasResourceTypes"]:
        return typing.cast(typing.Optional["DataAzurermStorageAccountSasResourceTypes"], jsii.get(self, "resourceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesInput")
    def services_input(self) -> typing.Optional["DataAzurermStorageAccountSasServices"]:
        return typing.cast(typing.Optional["DataAzurermStorageAccountSasServices"], jsii.get(self, "servicesInput"))

    @builtins.property
    @jsii.member(jsii_name="signedVersionInput")
    def signed_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signedVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataAzurermStorageAccountSasTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataAzurermStorageAccountSasTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionString", value)

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @expiry.setter
    def expiry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "expiry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiry", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="signedVersion")
    def signed_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signedVersion"))

    @signed_version.setter
    def signed_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "signed_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signedVersion", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSas, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_string": "connectionString",
        "expiry": "expiry",
        "permissions": "permissions",
        "resource_types": "resourceTypes",
        "services": "services",
        "start": "start",
        "https_only": "httpsOnly",
        "id": "id",
        "ip_addresses": "ipAddresses",
        "signed_version": "signedVersion",
        "timeouts": "timeouts",
    },
)
class DataAzurermStorageAccountSasConfig(cdktf.TerraformMetaArguments):
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
        connection_string: builtins.str,
        expiry: builtins.str,
        permissions: typing.Union["DataAzurermStorageAccountSasPermissions", typing.Dict[str, typing.Any]],
        resource_types: typing.Union["DataAzurermStorageAccountSasResourceTypes", typing.Dict[str, typing.Any]],
        services: typing.Union["DataAzurermStorageAccountSasServices", typing.Dict[str, typing.Any]],
        start: builtins.str,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_addresses: typing.Optional[builtins.str] = None,
        signed_version: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAzurermStorageAccountSasTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#connection_string DataAzurermStorageAccountSas#connection_string}.
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#expiry DataAzurermStorageAccountSas#expiry}.
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#permissions DataAzurermStorageAccountSas#permissions}
        :param resource_types: resource_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#resource_types DataAzurermStorageAccountSas#resource_types}
        :param services: services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#services DataAzurermStorageAccountSas#services}
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#start DataAzurermStorageAccountSas#start}.
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#https_only DataAzurermStorageAccountSas#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#id DataAzurermStorageAccountSas#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#ip_addresses DataAzurermStorageAccountSas#ip_addresses}.
        :param signed_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#signed_version DataAzurermStorageAccountSas#signed_version}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#timeouts DataAzurermStorageAccountSas#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(permissions, dict):
            permissions = DataAzurermStorageAccountSasPermissions(**permissions)
        if isinstance(resource_types, dict):
            resource_types = DataAzurermStorageAccountSasResourceTypes(**resource_types)
        if isinstance(services, dict):
            services = DataAzurermStorageAccountSasServices(**services)
        if isinstance(timeouts, dict):
            timeouts = DataAzurermStorageAccountSasTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument expiry", value=expiry, expected_type=type_hints["expiry"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            check_type(argname="argument services", value=services, expected_type=type_hints["services"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
            check_type(argname="argument signed_version", value=signed_version, expected_type=type_hints["signed_version"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_string": connection_string,
            "expiry": expiry,
            "permissions": permissions,
            "resource_types": resource_types,
            "services": services,
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
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if signed_version is not None:
            self._values["signed_version"] = signed_version
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
    def connection_string(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#connection_string DataAzurermStorageAccountSas#connection_string}.'''
        result = self._values.get("connection_string")
        assert result is not None, "Required property 'connection_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiry(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#expiry DataAzurermStorageAccountSas#expiry}.'''
        result = self._values.get("expiry")
        assert result is not None, "Required property 'expiry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permissions(self) -> "DataAzurermStorageAccountSasPermissions":
        '''permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#permissions DataAzurermStorageAccountSas#permissions}
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast("DataAzurermStorageAccountSasPermissions", result)

    @builtins.property
    def resource_types(self) -> "DataAzurermStorageAccountSasResourceTypes":
        '''resource_types block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#resource_types DataAzurermStorageAccountSas#resource_types}
        '''
        result = self._values.get("resource_types")
        assert result is not None, "Required property 'resource_types' is missing"
        return typing.cast("DataAzurermStorageAccountSasResourceTypes", result)

    @builtins.property
    def services(self) -> "DataAzurermStorageAccountSasServices":
        '''services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#services DataAzurermStorageAccountSas#services}
        '''
        result = self._values.get("services")
        assert result is not None, "Required property 'services' is missing"
        return typing.cast("DataAzurermStorageAccountSasServices", result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#start DataAzurermStorageAccountSas#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#https_only DataAzurermStorageAccountSas#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#id DataAzurermStorageAccountSas#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#ip_addresses DataAzurermStorageAccountSas#ip_addresses}.'''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signed_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#signed_version DataAzurermStorageAccountSas#signed_version}.'''
        result = self._values.get("signed_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataAzurermStorageAccountSasTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#timeouts DataAzurermStorageAccountSas#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataAzurermStorageAccountSasTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurermStorageAccountSasConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "add": "add",
        "create": "create",
        "delete": "delete",
        "filter": "filter",
        "list": "list",
        "process": "process",
        "read": "read",
        "tag": "tag",
        "update": "update",
        "write": "write",
    },
)
class DataAzurermStorageAccountSasPermissions:
    def __init__(
        self,
        *,
        add: typing.Union[builtins.bool, cdktf.IResolvable],
        create: typing.Union[builtins.bool, cdktf.IResolvable],
        delete: typing.Union[builtins.bool, cdktf.IResolvable],
        filter: typing.Union[builtins.bool, cdktf.IResolvable],
        list: typing.Union[builtins.bool, cdktf.IResolvable],
        process: typing.Union[builtins.bool, cdktf.IResolvable],
        read: typing.Union[builtins.bool, cdktf.IResolvable],
        tag: typing.Union[builtins.bool, cdktf.IResolvable],
        update: typing.Union[builtins.bool, cdktf.IResolvable],
        write: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param add: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#add DataAzurermStorageAccountSas#add}.
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#create DataAzurermStorageAccountSas#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#delete DataAzurermStorageAccountSas#delete}.
        :param filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#filter DataAzurermStorageAccountSas#filter}.
        :param list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#list DataAzurermStorageAccountSas#list}.
        :param process: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#process DataAzurermStorageAccountSas#process}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#tag DataAzurermStorageAccountSas#tag}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#update DataAzurermStorageAccountSas#update}.
        :param write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#write DataAzurermStorageAccountSas#write}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasPermissions.__init__)
            check_type(argname="argument add", value=add, expected_type=type_hints["add"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument list", value=list, expected_type=type_hints["list"])
            check_type(argname="argument process", value=process, expected_type=type_hints["process"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
        self._values: typing.Dict[str, typing.Any] = {
            "add": add,
            "create": create,
            "delete": delete,
            "filter": filter,
            "list": list,
            "process": process,
            "read": read,
            "tag": tag,
            "update": update,
            "write": write,
        }

    @builtins.property
    def add(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#add DataAzurermStorageAccountSas#add}.'''
        result = self._values.get("add")
        assert result is not None, "Required property 'add' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def create(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#create DataAzurermStorageAccountSas#create}.'''
        result = self._values.get("create")
        assert result is not None, "Required property 'create' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#delete DataAzurermStorageAccountSas#delete}.'''
        result = self._values.get("delete")
        assert result is not None, "Required property 'delete' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def filter(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#filter DataAzurermStorageAccountSas#filter}.'''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def list(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#list DataAzurermStorageAccountSas#list}.'''
        result = self._values.get("list")
        assert result is not None, "Required property 'list' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def process(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#process DataAzurermStorageAccountSas#process}.'''
        result = self._values.get("process")
        assert result is not None, "Required property 'process' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.'''
        result = self._values.get("read")
        assert result is not None, "Required property 'read' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def tag(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#tag DataAzurermStorageAccountSas#tag}.'''
        result = self._values.get("tag")
        assert result is not None, "Required property 'tag' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def update(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#update DataAzurermStorageAccountSas#update}.'''
        result = self._values.get("update")
        assert result is not None, "Required property 'update' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#write DataAzurermStorageAccountSas#write}.'''
        result = self._values.get("write")
        assert result is not None, "Required property 'write' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurermStorageAccountSasPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurermStorageAccountSasPermissionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasPermissionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="addInput")
    def add_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "addInput"))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="listInput")
    def list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "listInput"))

    @builtins.property
    @jsii.member(jsii_name="processInput")
    def process_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "processInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="writeInput")
    def write_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeInput"))

    @builtins.property
    @jsii.member(jsii_name="add")
    def add(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "add"))

    @add.setter
    def add(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "add").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "add", value)

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "create"))

    @create.setter
    def create(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="list")
    def list(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "list"))

    @list.setter
    def list(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "list", value)

    @builtins.property
    @jsii.member(jsii_name="process")
    def process(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "process"))

    @process.setter
    def process(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "process").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "process", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "read"))

    @read.setter
    def read(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "update"))

    @update.setter
    def update(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="write")
    def write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "write"))

    @write.setter
    def write(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "write", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAzurermStorageAccountSasPermissions]:
        return typing.cast(typing.Optional[DataAzurermStorageAccountSasPermissions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAzurermStorageAccountSasPermissions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasPermissionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasResourceTypes",
    jsii_struct_bases=[],
    name_mapping={"container": "container", "object": "object", "service": "service"},
)
class DataAzurermStorageAccountSasResourceTypes:
    def __init__(
        self,
        *,
        container: typing.Union[builtins.bool, cdktf.IResolvable],
        object: typing.Union[builtins.bool, cdktf.IResolvable],
        service: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#container DataAzurermStorageAccountSas#container}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#object DataAzurermStorageAccountSas#object}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#service DataAzurermStorageAccountSas#service}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasResourceTypes.__init__)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
            "object": object,
            "service": service,
        }

    @builtins.property
    def container(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#container DataAzurermStorageAccountSas#container}.'''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def object(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#object DataAzurermStorageAccountSas#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def service(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#service DataAzurermStorageAccountSas#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurermStorageAccountSasResourceTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurermStorageAccountSasResourceTypesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasResourceTypesOutputReference",
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
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasResourceTypesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "container"))

    @container.setter
    def container(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasResourceTypesOutputReference, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "object"))

    @object.setter
    def object(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasResourceTypesOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "service"))

    @service.setter
    def service(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasResourceTypesOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAzurermStorageAccountSasResourceTypes]:
        return typing.cast(typing.Optional[DataAzurermStorageAccountSasResourceTypes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAzurermStorageAccountSasResourceTypes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasResourceTypesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasServices",
    jsii_struct_bases=[],
    name_mapping={"blob": "blob", "file": "file", "queue": "queue", "table": "table"},
)
class DataAzurermStorageAccountSasServices:
    def __init__(
        self,
        *,
        blob: typing.Union[builtins.bool, cdktf.IResolvable],
        file: typing.Union[builtins.bool, cdktf.IResolvable],
        queue: typing.Union[builtins.bool, cdktf.IResolvable],
        table: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param blob: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#blob DataAzurermStorageAccountSas#blob}.
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#file DataAzurermStorageAccountSas#file}.
        :param queue: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#queue DataAzurermStorageAccountSas#queue}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#table DataAzurermStorageAccountSas#table}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasServices.__init__)
            check_type(argname="argument blob", value=blob, expected_type=type_hints["blob"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        self._values: typing.Dict[str, typing.Any] = {
            "blob": blob,
            "file": file,
            "queue": queue,
            "table": table,
        }

    @builtins.property
    def blob(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#blob DataAzurermStorageAccountSas#blob}.'''
        result = self._values.get("blob")
        assert result is not None, "Required property 'blob' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def file(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#file DataAzurermStorageAccountSas#file}.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def queue(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#queue DataAzurermStorageAccountSas#queue}.'''
        result = self._values.get("queue")
        assert result is not None, "Required property 'queue' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def table(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#table DataAzurermStorageAccountSas#table}.'''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurermStorageAccountSasServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurermStorageAccountSasServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasServicesOutputReference",
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
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="blobInput")
    def blob_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blobInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="queueInput")
    def queue_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "queueInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="blob")
    def blob(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blob"))

    @blob.setter
    def blob(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasServicesOutputReference, "blob").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blob", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "file"))

    @file.setter
    def file(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasServicesOutputReference, "file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "queue"))

    @queue.setter
    def queue(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasServicesOutputReference, "queue").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queue", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "table"))

    @table.setter
    def table(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasServicesOutputReference, "table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAzurermStorageAccountSasServices]:
        return typing.cast(typing.Optional[DataAzurermStorageAccountSasServices], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAzurermStorageAccountSasServices],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasTimeouts",
    jsii_struct_bases=[],
    name_mapping={"read": "read"},
)
class DataAzurermStorageAccountSasTimeouts:
    def __init__(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasTimeouts.__init__)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/d/storage_account_sas#read DataAzurermStorageAccountSas#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurermStorageAccountSasTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurermStorageAccountSasTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataAzurermStorageAccountSas.DataAzurermStorageAccountSasTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataAzurermStorageAccountSasTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAzurermStorageAccountSasTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAzurermStorageAccountSasTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAzurermStorageAccountSasTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzurermStorageAccountSasTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAzurermStorageAccountSas",
    "DataAzurermStorageAccountSasConfig",
    "DataAzurermStorageAccountSasPermissions",
    "DataAzurermStorageAccountSasPermissionsOutputReference",
    "DataAzurermStorageAccountSasResourceTypes",
    "DataAzurermStorageAccountSasResourceTypesOutputReference",
    "DataAzurermStorageAccountSasServices",
    "DataAzurermStorageAccountSasServicesOutputReference",
    "DataAzurermStorageAccountSasTimeouts",
    "DataAzurermStorageAccountSasTimeoutsOutputReference",
]

publication.publish()
