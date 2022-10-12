'''
# `azurerm_mssql_managed_instance_active_directory_administrator`

Refer to the Terraform Registory for docs: [`azurerm_mssql_managed_instance_active_directory_administrator`](https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator).
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


class MssqlManagedInstanceActiveDirectoryAdministrator(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceActiveDirectoryAdministrator.MssqlManagedInstanceActiveDirectoryAdministrator",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator azurerm_mssql_managed_instance_active_directory_administrator}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        login_username: builtins.str,
        managed_instance_id: builtins.str,
        object_id: builtins.str,
        tenant_id: builtins.str,
        azuread_authentication_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator azurerm_mssql_managed_instance_active_directory_administrator} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param login_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#login_username MssqlManagedInstanceActiveDirectoryAdministrator#login_username}.
        :param managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#managed_instance_id MssqlManagedInstanceActiveDirectoryAdministrator#managed_instance_id}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#object_id MssqlManagedInstanceActiveDirectoryAdministrator#object_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#tenant_id MssqlManagedInstanceActiveDirectoryAdministrator#tenant_id}.
        :param azuread_authentication_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#azuread_authentication_only MssqlManagedInstanceActiveDirectoryAdministrator#azuread_authentication_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#id MssqlManagedInstanceActiveDirectoryAdministrator#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#timeouts MssqlManagedInstanceActiveDirectoryAdministrator#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceActiveDirectoryAdministrator.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MssqlManagedInstanceActiveDirectoryAdministratorConfig(
            login_username=login_username,
            managed_instance_id=managed_instance_id,
            object_id=object_id,
            tenant_id=tenant_id,
            azuread_authentication_only=azuread_authentication_only,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#create MssqlManagedInstanceActiveDirectoryAdministrator#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#delete MssqlManagedInstanceActiveDirectoryAdministrator#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#read MssqlManagedInstanceActiveDirectoryAdministrator#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#update MssqlManagedInstanceActiveDirectoryAdministrator#update}.
        '''
        value = MssqlManagedInstanceActiveDirectoryAdministratorTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAzureadAuthenticationOnly")
    def reset_azuread_authentication_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureadAuthenticationOnly", []))

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
    ) -> "MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference":
        return typing.cast("MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="azureadAuthenticationOnlyInput")
    def azuread_authentication_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azureadAuthenticationOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loginUsernameInput")
    def login_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceIdInput")
    def managed_instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureadAuthenticationOnly")
    def azuread_authentication_only(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "azureadAuthenticationOnly"))

    @azuread_authentication_only.setter
    def azuread_authentication_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "azuread_authentication_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureadAuthenticationOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loginUsername")
    def login_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginUsername"))

    @login_username.setter
    def login_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "login_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginUsername", value)

    @builtins.property
    @jsii.member(jsii_name="managedInstanceId")
    def managed_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedInstanceId"))

    @managed_instance_id.setter
    def managed_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "managed_instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministrator, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceActiveDirectoryAdministrator.MssqlManagedInstanceActiveDirectoryAdministratorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "login_username": "loginUsername",
        "managed_instance_id": "managedInstanceId",
        "object_id": "objectId",
        "tenant_id": "tenantId",
        "azuread_authentication_only": "azureadAuthenticationOnly",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class MssqlManagedInstanceActiveDirectoryAdministratorConfig(
    cdktf.TerraformMetaArguments,
):
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
        login_username: builtins.str,
        managed_instance_id: builtins.str,
        object_id: builtins.str,
        tenant_id: builtins.str,
        azuread_authentication_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param login_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#login_username MssqlManagedInstanceActiveDirectoryAdministrator#login_username}.
        :param managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#managed_instance_id MssqlManagedInstanceActiveDirectoryAdministrator#managed_instance_id}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#object_id MssqlManagedInstanceActiveDirectoryAdministrator#object_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#tenant_id MssqlManagedInstanceActiveDirectoryAdministrator#tenant_id}.
        :param azuread_authentication_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#azuread_authentication_only MssqlManagedInstanceActiveDirectoryAdministrator#azuread_authentication_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#id MssqlManagedInstanceActiveDirectoryAdministrator#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#timeouts MssqlManagedInstanceActiveDirectoryAdministrator#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MssqlManagedInstanceActiveDirectoryAdministratorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceActiveDirectoryAdministratorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument login_username", value=login_username, expected_type=type_hints["login_username"])
            check_type(argname="argument managed_instance_id", value=managed_instance_id, expected_type=type_hints["managed_instance_id"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument azuread_authentication_only", value=azuread_authentication_only, expected_type=type_hints["azuread_authentication_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "login_username": login_username,
            "managed_instance_id": managed_instance_id,
            "object_id": object_id,
            "tenant_id": tenant_id,
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
        if azuread_authentication_only is not None:
            self._values["azuread_authentication_only"] = azuread_authentication_only
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
    def login_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#login_username MssqlManagedInstanceActiveDirectoryAdministrator#login_username}.'''
        result = self._values.get("login_username")
        assert result is not None, "Required property 'login_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#managed_instance_id MssqlManagedInstanceActiveDirectoryAdministrator#managed_instance_id}.'''
        result = self._values.get("managed_instance_id")
        assert result is not None, "Required property 'managed_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#object_id MssqlManagedInstanceActiveDirectoryAdministrator#object_id}.'''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#tenant_id MssqlManagedInstanceActiveDirectoryAdministrator#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azuread_authentication_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#azuread_authentication_only MssqlManagedInstanceActiveDirectoryAdministrator#azuread_authentication_only}.'''
        result = self._values.get("azuread_authentication_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#id MssqlManagedInstanceActiveDirectoryAdministrator#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#timeouts MssqlManagedInstanceActiveDirectoryAdministrator#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlManagedInstanceActiveDirectoryAdministratorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceActiveDirectoryAdministratorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceActiveDirectoryAdministrator.MssqlManagedInstanceActiveDirectoryAdministratorTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlManagedInstanceActiveDirectoryAdministratorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#create MssqlManagedInstanceActiveDirectoryAdministrator#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#delete MssqlManagedInstanceActiveDirectoryAdministrator#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#read MssqlManagedInstanceActiveDirectoryAdministrator#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#update MssqlManagedInstanceActiveDirectoryAdministrator#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceActiveDirectoryAdministratorTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#create MssqlManagedInstanceActiveDirectoryAdministrator#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#delete MssqlManagedInstanceActiveDirectoryAdministrator#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#read MssqlManagedInstanceActiveDirectoryAdministrator#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_active_directory_administrator#update MssqlManagedInstanceActiveDirectoryAdministrator#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceActiveDirectoryAdministratorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceActiveDirectoryAdministrator.MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MssqlManagedInstanceActiveDirectoryAdministratorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlManagedInstanceActiveDirectoryAdministratorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlManagedInstanceActiveDirectoryAdministratorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlManagedInstanceActiveDirectoryAdministrator",
    "MssqlManagedInstanceActiveDirectoryAdministratorConfig",
    "MssqlManagedInstanceActiveDirectoryAdministratorTimeouts",
    "MssqlManagedInstanceActiveDirectoryAdministratorTimeoutsOutputReference",
]

publication.publish()
