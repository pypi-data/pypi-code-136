'''
# `azurerm_data_factory_managed_private_endpoint`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_managed_private_endpoint`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint).
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


class DataFactoryManagedPrivateEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryManagedPrivateEndpoint.DataFactoryManagedPrivateEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint azurerm_data_factory_managed_private_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        name: builtins.str,
        target_resource_id: builtins.str,
        fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        subresource_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryManagedPrivateEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint azurerm_data_factory_managed_private_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#data_factory_id DataFactoryManagedPrivateEndpoint#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#name DataFactoryManagedPrivateEndpoint#name}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#target_resource_id DataFactoryManagedPrivateEndpoint#target_resource_id}.
        :param fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#fqdns DataFactoryManagedPrivateEndpoint#fqdns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#id DataFactoryManagedPrivateEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subresource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#subresource_name DataFactoryManagedPrivateEndpoint#subresource_name}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#timeouts DataFactoryManagedPrivateEndpoint#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryManagedPrivateEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryManagedPrivateEndpointConfig(
            data_factory_id=data_factory_id,
            name=name,
            target_resource_id=target_resource_id,
            fqdns=fqdns,
            id=id,
            subresource_name=subresource_name,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#create DataFactoryManagedPrivateEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#delete DataFactoryManagedPrivateEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#read DataFactoryManagedPrivateEndpoint#read}.
        '''
        value = DataFactoryManagedPrivateEndpointTimeouts(
            create=create, delete=delete, read=read
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetFqdns")
    def reset_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFqdns", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSubresourceName")
    def reset_subresource_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubresourceName", []))

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
    def timeouts(self) -> "DataFactoryManagedPrivateEndpointTimeoutsOutputReference":
        return typing.cast("DataFactoryManagedPrivateEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryIdInput")
    def data_factory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFactoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fqdnsInput")
    def fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="subresourceNameInput")
    def subresource_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subresourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceIdInput")
    def target_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryManagedPrivateEndpointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryManagedPrivateEndpointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="fqdns")
    def fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fqdns"))

    @fqdns.setter
    def fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fqdns", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subresourceName")
    def subresource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subresourceName"))

    @subresource_name.setter
    def subresource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "subresource_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subresourceName", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceId")
    def target_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceId"))

    @target_resource_id.setter
    def target_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpoint, "target_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryManagedPrivateEndpoint.DataFactoryManagedPrivateEndpointConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_factory_id": "dataFactoryId",
        "name": "name",
        "target_resource_id": "targetResourceId",
        "fqdns": "fqdns",
        "id": "id",
        "subresource_name": "subresourceName",
        "timeouts": "timeouts",
    },
)
class DataFactoryManagedPrivateEndpointConfig(cdktf.TerraformMetaArguments):
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
        data_factory_id: builtins.str,
        name: builtins.str,
        target_resource_id: builtins.str,
        fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        subresource_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryManagedPrivateEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#data_factory_id DataFactoryManagedPrivateEndpoint#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#name DataFactoryManagedPrivateEndpoint#name}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#target_resource_id DataFactoryManagedPrivateEndpoint#target_resource_id}.
        :param fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#fqdns DataFactoryManagedPrivateEndpoint#fqdns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#id DataFactoryManagedPrivateEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subresource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#subresource_name DataFactoryManagedPrivateEndpoint#subresource_name}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#timeouts DataFactoryManagedPrivateEndpoint#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryManagedPrivateEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryManagedPrivateEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_resource_id", value=target_resource_id, expected_type=type_hints["target_resource_id"])
            check_type(argname="argument fqdns", value=fqdns, expected_type=type_hints["fqdns"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument subresource_name", value=subresource_name, expected_type=type_hints["subresource_name"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "name": name,
            "target_resource_id": target_resource_id,
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
        if fqdns is not None:
            self._values["fqdns"] = fqdns
        if id is not None:
            self._values["id"] = id
        if subresource_name is not None:
            self._values["subresource_name"] = subresource_name
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
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#data_factory_id DataFactoryManagedPrivateEndpoint#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#name DataFactoryManagedPrivateEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#target_resource_id DataFactoryManagedPrivateEndpoint#target_resource_id}.'''
        result = self._values.get("target_resource_id")
        assert result is not None, "Required property 'target_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#fqdns DataFactoryManagedPrivateEndpoint#fqdns}.'''
        result = self._values.get("fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#id DataFactoryManagedPrivateEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subresource_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#subresource_name DataFactoryManagedPrivateEndpoint#subresource_name}.'''
        result = self._values.get("subresource_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryManagedPrivateEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#timeouts DataFactoryManagedPrivateEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryManagedPrivateEndpointTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryManagedPrivateEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryManagedPrivateEndpoint.DataFactoryManagedPrivateEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class DataFactoryManagedPrivateEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#create DataFactoryManagedPrivateEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#delete DataFactoryManagedPrivateEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#read DataFactoryManagedPrivateEndpoint#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryManagedPrivateEndpointTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#create DataFactoryManagedPrivateEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#delete DataFactoryManagedPrivateEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_managed_private_endpoint#read DataFactoryManagedPrivateEndpoint#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryManagedPrivateEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryManagedPrivateEndpointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryManagedPrivateEndpoint.DataFactoryManagedPrivateEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryManagedPrivateEndpointTimeoutsOutputReference.__init__)
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
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpointTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpointTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpointTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryManagedPrivateEndpointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryManagedPrivateEndpointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryManagedPrivateEndpointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryManagedPrivateEndpointTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryManagedPrivateEndpoint",
    "DataFactoryManagedPrivateEndpointConfig",
    "DataFactoryManagedPrivateEndpointTimeouts",
    "DataFactoryManagedPrivateEndpointTimeoutsOutputReference",
]

publication.publish()
