'''
# `azurerm_storage_account_network_rules`

Refer to the Terraform Registory for docs: [`azurerm_storage_account_network_rules`](https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules).
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


class StorageAccountNetworkRulesA(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules azurerm_storage_account_network_rules}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_action: builtins.str,
        storage_account_id: builtins.str,
        bypass: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_link_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccessA", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountNetworkRulesTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules azurerm_storage_account_network_rules} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#default_action StorageAccountNetworkRulesA#default_action}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#storage_account_id StorageAccountNetworkRulesA#storage_account_id}.
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#bypass StorageAccountNetworkRulesA#bypass}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#id StorageAccountNetworkRulesA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#ip_rules StorageAccountNetworkRulesA#ip_rules}.
        :param private_link_access: private_link_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#private_link_access StorageAccountNetworkRulesA#private_link_access}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#timeouts StorageAccountNetworkRulesA#timeouts}
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#virtual_network_subnet_ids StorageAccountNetworkRulesA#virtual_network_subnet_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesA.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageAccountNetworkRulesAConfig(
            default_action=default_action,
            storage_account_id=storage_account_id,
            bypass=bypass,
            id=id,
            ip_rules=ip_rules,
            private_link_access=private_link_access,
            timeouts=timeouts,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPrivateLinkAccess")
    def put_private_link_access(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccessA", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesA.put_private_link_access)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPrivateLinkAccess", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#create StorageAccountNetworkRulesA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#delete StorageAccountNetworkRulesA#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#read StorageAccountNetworkRulesA#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#update StorageAccountNetworkRulesA#update}.
        '''
        value = StorageAccountNetworkRulesTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBypass")
    def reset_bypass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypass", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpRules")
    def reset_ip_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRules", []))

    @jsii.member(jsii_name="resetPrivateLinkAccess")
    def reset_private_link_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkAccess", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetIds")
    def reset_virtual_network_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkAccess")
    def private_link_access(self) -> "StorageAccountNetworkRulesPrivateLinkAccessAList":
        return typing.cast("StorageAccountNetworkRulesPrivateLinkAccessAList", jsii.get(self, "privateLinkAccess"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageAccountNetworkRulesTimeoutsOutputReference":
        return typing.cast("StorageAccountNetworkRulesTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bypassInput")
    def bypass_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bypassInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRulesInput")
    def ip_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkAccessInput")
    def private_link_access_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccessA"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccessA"]]], jsii.get(self, "privateLinkAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageAccountNetworkRulesTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageAccountNetworkRulesTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdsInput")
    def virtual_network_subnet_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualNetworkSubnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bypass")
    def bypass(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bypass"))

    @bypass.setter
    def bypass(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "bypass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypass", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipRules")
    def ip_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipRules"))

    @ip_rules.setter
    def ip_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "ip_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRules", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualNetworkSubnetIds"))

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesA, "virtual_network_subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesAConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_action": "defaultAction",
        "storage_account_id": "storageAccountId",
        "bypass": "bypass",
        "id": "id",
        "ip_rules": "ipRules",
        "private_link_access": "privateLinkAccess",
        "timeouts": "timeouts",
        "virtual_network_subnet_ids": "virtualNetworkSubnetIds",
    },
)
class StorageAccountNetworkRulesAConfig(cdktf.TerraformMetaArguments):
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
        default_action: builtins.str,
        storage_account_id: builtins.str,
        bypass: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_link_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccessA", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountNetworkRulesTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#default_action StorageAccountNetworkRulesA#default_action}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#storage_account_id StorageAccountNetworkRulesA#storage_account_id}.
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#bypass StorageAccountNetworkRulesA#bypass}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#id StorageAccountNetworkRulesA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#ip_rules StorageAccountNetworkRulesA#ip_rules}.
        :param private_link_access: private_link_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#private_link_access StorageAccountNetworkRulesA#private_link_access}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#timeouts StorageAccountNetworkRulesA#timeouts}
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#virtual_network_subnet_ids StorageAccountNetworkRulesA#virtual_network_subnet_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = StorageAccountNetworkRulesTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesAConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument bypass", value=bypass, expected_type=type_hints["bypass"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_rules", value=ip_rules, expected_type=type_hints["ip_rules"])
            check_type(argname="argument private_link_access", value=private_link_access, expected_type=type_hints["private_link_access"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_subnet_ids", value=virtual_network_subnet_ids, expected_type=type_hints["virtual_network_subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
            "storage_account_id": storage_account_id,
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
        if bypass is not None:
            self._values["bypass"] = bypass
        if id is not None:
            self._values["id"] = id
        if ip_rules is not None:
            self._values["ip_rules"] = ip_rules
        if private_link_access is not None:
            self._values["private_link_access"] = private_link_access
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_subnet_ids is not None:
            self._values["virtual_network_subnet_ids"] = virtual_network_subnet_ids

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
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#default_action StorageAccountNetworkRulesA#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#storage_account_id StorageAccountNetworkRulesA#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bypass(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#bypass StorageAccountNetworkRulesA#bypass}.'''
        result = self._values.get("bypass")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#id StorageAccountNetworkRulesA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#ip_rules StorageAccountNetworkRulesA#ip_rules}.'''
        result = self._values.get("ip_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_link_access(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccessA"]]]:
        '''private_link_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#private_link_access StorageAccountNetworkRulesA#private_link_access}
        '''
        result = self._values.get("private_link_access")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccessA"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageAccountNetworkRulesTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#timeouts StorageAccountNetworkRulesA#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageAccountNetworkRulesTimeouts"], result)

    @builtins.property
    def virtual_network_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#virtual_network_subnet_ids StorageAccountNetworkRulesA#virtual_network_subnet_ids}.'''
        result = self._values.get("virtual_network_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountNetworkRulesAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesPrivateLinkAccessA",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_resource_id": "endpointResourceId",
        "endpoint_tenant_id": "endpointTenantId",
    },
)
class StorageAccountNetworkRulesPrivateLinkAccessA:
    def __init__(
        self,
        *,
        endpoint_resource_id: builtins.str,
        endpoint_tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#endpoint_resource_id StorageAccountNetworkRulesA#endpoint_resource_id}.
        :param endpoint_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#endpoint_tenant_id StorageAccountNetworkRulesA#endpoint_tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessA.__init__)
            check_type(argname="argument endpoint_resource_id", value=endpoint_resource_id, expected_type=type_hints["endpoint_resource_id"])
            check_type(argname="argument endpoint_tenant_id", value=endpoint_tenant_id, expected_type=type_hints["endpoint_tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_resource_id": endpoint_resource_id,
        }
        if endpoint_tenant_id is not None:
            self._values["endpoint_tenant_id"] = endpoint_tenant_id

    @builtins.property
    def endpoint_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#endpoint_resource_id StorageAccountNetworkRulesA#endpoint_resource_id}.'''
        result = self._values.get("endpoint_resource_id")
        assert result is not None, "Required property 'endpoint_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#endpoint_tenant_id StorageAccountNetworkRulesA#endpoint_tenant_id}.'''
        result = self._values.get("endpoint_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountNetworkRulesPrivateLinkAccessA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountNetworkRulesPrivateLinkAccessAList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesPrivateLinkAccessAList",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessAList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageAccountNetworkRulesPrivateLinkAccessAOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessAList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageAccountNetworkRulesPrivateLinkAccessAOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccessA]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccessA]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccessA]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountNetworkRulesPrivateLinkAccessAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesPrivateLinkAccessAOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndpointTenantId")
    def reset_endpoint_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="endpointResourceIdInput")
    def endpoint_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTenantIdInput")
    def endpoint_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointResourceId")
    def endpoint_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointResourceId"))

    @endpoint_resource_id.setter
    def endpoint_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAOutputReference, "endpoint_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="endpointTenantId")
    def endpoint_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointTenantId"))

    @endpoint_tenant_id.setter
    def endpoint_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAOutputReference, "endpoint_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccessA, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccessA, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccessA, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageAccountNetworkRulesTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#create StorageAccountNetworkRulesA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#delete StorageAccountNetworkRulesA#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#read StorageAccountNetworkRulesA#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#update StorageAccountNetworkRulesA#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#create StorageAccountNetworkRulesA#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#delete StorageAccountNetworkRulesA#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#read StorageAccountNetworkRulesA#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account_network_rules#update StorageAccountNetworkRulesA#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountNetworkRulesTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountNetworkRulesTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccountNetworkRules.StorageAccountNetworkRulesTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountNetworkRulesTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountNetworkRulesTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountNetworkRulesTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageAccountNetworkRulesA",
    "StorageAccountNetworkRulesAConfig",
    "StorageAccountNetworkRulesPrivateLinkAccessA",
    "StorageAccountNetworkRulesPrivateLinkAccessAList",
    "StorageAccountNetworkRulesPrivateLinkAccessAOutputReference",
    "StorageAccountNetworkRulesTimeouts",
    "StorageAccountNetworkRulesTimeoutsOutputReference",
]

publication.publish()
