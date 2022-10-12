'''
# `azurerm_mssql_managed_instance_failover_group`

Refer to the Terraform Registory for docs: [`azurerm_mssql_managed_instance_failover_group`](https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group).
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


class MssqlManagedInstanceFailoverGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group azurerm_mssql_managed_instance_failover_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        managed_instance_id: builtins.str,
        name: builtins.str,
        partner_managed_instance_id: builtins.str,
        read_write_endpoint_failover_policy: typing.Union["MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        readonly_endpoint_failover_policy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["MssqlManagedInstanceFailoverGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group azurerm_mssql_managed_instance_failover_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#location MssqlManagedInstanceFailoverGroup#location}.
        :param managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#managed_instance_id MssqlManagedInstanceFailoverGroup#managed_instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#name MssqlManagedInstanceFailoverGroup#name}.
        :param partner_managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#partner_managed_instance_id MssqlManagedInstanceFailoverGroup#partner_managed_instance_id}.
        :param read_write_endpoint_failover_policy: read_write_endpoint_failover_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read_write_endpoint_failover_policy MssqlManagedInstanceFailoverGroup#read_write_endpoint_failover_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#id MssqlManagedInstanceFailoverGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param readonly_endpoint_failover_policy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#readonly_endpoint_failover_policy_enabled MssqlManagedInstanceFailoverGroup#readonly_endpoint_failover_policy_enabled}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#timeouts MssqlManagedInstanceFailoverGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MssqlManagedInstanceFailoverGroupConfig(
            location=location,
            managed_instance_id=managed_instance_id,
            name=name,
            partner_managed_instance_id=partner_managed_instance_id,
            read_write_endpoint_failover_policy=read_write_endpoint_failover_policy,
            id=id,
            readonly_endpoint_failover_policy_enabled=readonly_endpoint_failover_policy_enabled,
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

    @jsii.member(jsii_name="putReadWriteEndpointFailoverPolicy")
    def put_read_write_endpoint_failover_policy(
        self,
        *,
        mode: builtins.str,
        grace_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#mode MssqlManagedInstanceFailoverGroup#mode}.
        :param grace_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#grace_minutes MssqlManagedInstanceFailoverGroup#grace_minutes}.
        '''
        value = MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy(
            mode=mode, grace_minutes=grace_minutes
        )

        return typing.cast(None, jsii.invoke(self, "putReadWriteEndpointFailoverPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#create MssqlManagedInstanceFailoverGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#delete MssqlManagedInstanceFailoverGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read MssqlManagedInstanceFailoverGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#update MssqlManagedInstanceFailoverGroup#update}.
        '''
        value = MssqlManagedInstanceFailoverGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReadonlyEndpointFailoverPolicyEnabled")
    def reset_readonly_endpoint_failover_policy_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadonlyEndpointFailoverPolicyEnabled", []))

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
    @jsii.member(jsii_name="partnerRegion")
    def partner_region(self) -> "MssqlManagedInstanceFailoverGroupPartnerRegionList":
        return typing.cast("MssqlManagedInstanceFailoverGroupPartnerRegionList", jsii.get(self, "partnerRegion"))

    @builtins.property
    @jsii.member(jsii_name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(
        self,
    ) -> "MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference":
        return typing.cast("MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference", jsii.get(self, "readWriteEndpointFailoverPolicy"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MssqlManagedInstanceFailoverGroupTimeoutsOutputReference":
        return typing.cast("MssqlManagedInstanceFailoverGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceIdInput")
    def managed_instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partnerManagedInstanceIdInput")
    def partner_managed_instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerManagedInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="readonlyEndpointFailoverPolicyEnabledInput")
    def readonly_endpoint_failover_policy_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readonlyEndpointFailoverPolicyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="readWriteEndpointFailoverPolicyInput")
    def read_write_endpoint_failover_policy_input(
        self,
    ) -> typing.Optional["MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy"]:
        return typing.cast(typing.Optional["MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy"], jsii.get(self, "readWriteEndpointFailoverPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlManagedInstanceFailoverGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlManagedInstanceFailoverGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedInstanceId")
    def managed_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedInstanceId"))

    @managed_instance_id.setter
    def managed_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "managed_instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partnerManagedInstanceId"))

    @partner_managed_instance_id.setter
    def partner_managed_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "partner_managed_instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerManagedInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="readonlyEndpointFailoverPolicyEnabled")
    def readonly_endpoint_failover_policy_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readonlyEndpointFailoverPolicyEnabled"))

    @readonly_endpoint_failover_policy_enabled.setter
    def readonly_endpoint_failover_policy_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroup, "readonly_endpoint_failover_policy_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readonlyEndpointFailoverPolicyEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupConfig",
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
        "managed_instance_id": "managedInstanceId",
        "name": "name",
        "partner_managed_instance_id": "partnerManagedInstanceId",
        "read_write_endpoint_failover_policy": "readWriteEndpointFailoverPolicy",
        "id": "id",
        "readonly_endpoint_failover_policy_enabled": "readonlyEndpointFailoverPolicyEnabled",
        "timeouts": "timeouts",
    },
)
class MssqlManagedInstanceFailoverGroupConfig(cdktf.TerraformMetaArguments):
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
        managed_instance_id: builtins.str,
        name: builtins.str,
        partner_managed_instance_id: builtins.str,
        read_write_endpoint_failover_policy: typing.Union["MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        readonly_endpoint_failover_policy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["MssqlManagedInstanceFailoverGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#location MssqlManagedInstanceFailoverGroup#location}.
        :param managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#managed_instance_id MssqlManagedInstanceFailoverGroup#managed_instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#name MssqlManagedInstanceFailoverGroup#name}.
        :param partner_managed_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#partner_managed_instance_id MssqlManagedInstanceFailoverGroup#partner_managed_instance_id}.
        :param read_write_endpoint_failover_policy: read_write_endpoint_failover_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read_write_endpoint_failover_policy MssqlManagedInstanceFailoverGroup#read_write_endpoint_failover_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#id MssqlManagedInstanceFailoverGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param readonly_endpoint_failover_policy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#readonly_endpoint_failover_policy_enabled MssqlManagedInstanceFailoverGroup#readonly_endpoint_failover_policy_enabled}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#timeouts MssqlManagedInstanceFailoverGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(read_write_endpoint_failover_policy, dict):
            read_write_endpoint_failover_policy = MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy(**read_write_endpoint_failover_policy)
        if isinstance(timeouts, dict):
            timeouts = MssqlManagedInstanceFailoverGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument managed_instance_id", value=managed_instance_id, expected_type=type_hints["managed_instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partner_managed_instance_id", value=partner_managed_instance_id, expected_type=type_hints["partner_managed_instance_id"])
            check_type(argname="argument read_write_endpoint_failover_policy", value=read_write_endpoint_failover_policy, expected_type=type_hints["read_write_endpoint_failover_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument readonly_endpoint_failover_policy_enabled", value=readonly_endpoint_failover_policy_enabled, expected_type=type_hints["readonly_endpoint_failover_policy_enabled"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "managed_instance_id": managed_instance_id,
            "name": name,
            "partner_managed_instance_id": partner_managed_instance_id,
            "read_write_endpoint_failover_policy": read_write_endpoint_failover_policy,
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
        if readonly_endpoint_failover_policy_enabled is not None:
            self._values["readonly_endpoint_failover_policy_enabled"] = readonly_endpoint_failover_policy_enabled
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#location MssqlManagedInstanceFailoverGroup#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#managed_instance_id MssqlManagedInstanceFailoverGroup#managed_instance_id}.'''
        result = self._values.get("managed_instance_id")
        assert result is not None, "Required property 'managed_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#name MssqlManagedInstanceFailoverGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partner_managed_instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#partner_managed_instance_id MssqlManagedInstanceFailoverGroup#partner_managed_instance_id}.'''
        result = self._values.get("partner_managed_instance_id")
        assert result is not None, "Required property 'partner_managed_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_write_endpoint_failover_policy(
        self,
    ) -> "MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy":
        '''read_write_endpoint_failover_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read_write_endpoint_failover_policy MssqlManagedInstanceFailoverGroup#read_write_endpoint_failover_policy}
        '''
        result = self._values.get("read_write_endpoint_failover_policy")
        assert result is not None, "Required property 'read_write_endpoint_failover_policy' is missing"
        return typing.cast("MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#id MssqlManagedInstanceFailoverGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readonly_endpoint_failover_policy_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#readonly_endpoint_failover_policy_enabled MssqlManagedInstanceFailoverGroup#readonly_endpoint_failover_policy_enabled}.'''
        result = self._values.get("readonly_endpoint_failover_policy_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MssqlManagedInstanceFailoverGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#timeouts MssqlManagedInstanceFailoverGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlManagedInstanceFailoverGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceFailoverGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupPartnerRegion",
    jsii_struct_bases=[],
    name_mapping={},
)
class MssqlManagedInstanceFailoverGroupPartnerRegion:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceFailoverGroupPartnerRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlManagedInstanceFailoverGroupPartnerRegionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupPartnerRegionList",
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
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupPartnerRegionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupPartnerRegionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupPartnerRegionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupPartnerRegionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupPartnerRegionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference",
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
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlManagedInstanceFailoverGroupPartnerRegion]:
        return typing.cast(typing.Optional[MssqlManagedInstanceFailoverGroupPartnerRegion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlManagedInstanceFailoverGroupPartnerRegion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "grace_minutes": "graceMinutes"},
)
class MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy:
    def __init__(
        self,
        *,
        mode: builtins.str,
        grace_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#mode MssqlManagedInstanceFailoverGroup#mode}.
        :param grace_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#grace_minutes MssqlManagedInstanceFailoverGroup#grace_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument grace_minutes", value=grace_minutes, expected_type=type_hints["grace_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if grace_minutes is not None:
            self._values["grace_minutes"] = grace_minutes

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#mode MssqlManagedInstanceFailoverGroup#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grace_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#grace_minutes MssqlManagedInstanceFailoverGroup#grace_minutes}.'''
        result = self._values.get("grace_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGraceMinutes")
    def reset_grace_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraceMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="graceMinutesInput")
    def grace_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "graceMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="graceMinutes")
    def grace_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "graceMinutes"))

    @grace_minutes.setter
    def grace_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference, "grace_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graceMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy]:
        return typing.cast(typing.Optional[MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlManagedInstanceFailoverGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#create MssqlManagedInstanceFailoverGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#delete MssqlManagedInstanceFailoverGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read MssqlManagedInstanceFailoverGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#update MssqlManagedInstanceFailoverGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#create MssqlManagedInstanceFailoverGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#delete MssqlManagedInstanceFailoverGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#read MssqlManagedInstanceFailoverGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_managed_instance_failover_group#update MssqlManagedInstanceFailoverGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlManagedInstanceFailoverGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlManagedInstanceFailoverGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlManagedInstanceFailoverGroup.MssqlManagedInstanceFailoverGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MssqlManagedInstanceFailoverGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlManagedInstanceFailoverGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlManagedInstanceFailoverGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlManagedInstanceFailoverGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlManagedInstanceFailoverGroup",
    "MssqlManagedInstanceFailoverGroupConfig",
    "MssqlManagedInstanceFailoverGroupPartnerRegion",
    "MssqlManagedInstanceFailoverGroupPartnerRegionList",
    "MssqlManagedInstanceFailoverGroupPartnerRegionOutputReference",
    "MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy",
    "MssqlManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyOutputReference",
    "MssqlManagedInstanceFailoverGroupTimeouts",
    "MssqlManagedInstanceFailoverGroupTimeoutsOutputReference",
]

publication.publish()
