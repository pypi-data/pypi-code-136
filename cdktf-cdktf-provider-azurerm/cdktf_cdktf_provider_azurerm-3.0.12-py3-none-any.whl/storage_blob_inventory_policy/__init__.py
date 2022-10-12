'''
# `azurerm_storage_blob_inventory_policy`

Refer to the Terraform Registory for docs: [`azurerm_storage_blob_inventory_policy`](https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy).
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


class StorageBlobInventoryPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy azurerm_storage_blob_inventory_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        rules: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageBlobInventoryPolicyRules", typing.Dict[str, typing.Any]]]],
        storage_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StorageBlobInventoryPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy azurerm_storage_blob_inventory_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#rules StorageBlobInventoryPolicy#rules}
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#storage_account_id StorageBlobInventoryPolicy#storage_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#id StorageBlobInventoryPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#timeouts StorageBlobInventoryPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageBlobInventoryPolicyConfig(
            rules=rules,
            storage_account_id=storage_account_id,
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

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageBlobInventoryPolicyRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicy.put_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#create StorageBlobInventoryPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#delete StorageBlobInventoryPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#read StorageBlobInventoryPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#update StorageBlobInventoryPolicy#update}.
        '''
        value = StorageBlobInventoryPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

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
    @jsii.member(jsii_name="rules")
    def rules(self) -> "StorageBlobInventoryPolicyRulesList":
        return typing.cast("StorageBlobInventoryPolicyRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageBlobInventoryPolicyTimeoutsOutputReference":
        return typing.cast("StorageBlobInventoryPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageBlobInventoryPolicyRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageBlobInventoryPolicyRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageBlobInventoryPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageBlobInventoryPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicy, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "rules": "rules",
        "storage_account_id": "storageAccountId",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class StorageBlobInventoryPolicyConfig(cdktf.TerraformMetaArguments):
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
        rules: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageBlobInventoryPolicyRules", typing.Dict[str, typing.Any]]]],
        storage_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StorageBlobInventoryPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#rules StorageBlobInventoryPolicy#rules}
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#storage_account_id StorageBlobInventoryPolicy#storage_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#id StorageBlobInventoryPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#timeouts StorageBlobInventoryPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = StorageBlobInventoryPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "rules": rules,
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
    def rules(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["StorageBlobInventoryPolicyRules"]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#rules StorageBlobInventoryPolicy#rules}
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["StorageBlobInventoryPolicyRules"]], result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#storage_account_id StorageBlobInventoryPolicy#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#id StorageBlobInventoryPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageBlobInventoryPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#timeouts StorageBlobInventoryPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageBlobInventoryPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobInventoryPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyRules",
    jsii_struct_bases=[],
    name_mapping={
        "format": "format",
        "name": "name",
        "schedule": "schedule",
        "schema_fields": "schemaFields",
        "scope": "scope",
        "storage_container_name": "storageContainerName",
        "filter": "filter",
    },
)
class StorageBlobInventoryPolicyRules:
    def __init__(
        self,
        *,
        format: builtins.str,
        name: builtins.str,
        schedule: builtins.str,
        schema_fields: typing.Sequence[builtins.str],
        scope: builtins.str,
        storage_container_name: builtins.str,
        filter: typing.Optional[typing.Union["StorageBlobInventoryPolicyRulesFilter", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#format StorageBlobInventoryPolicy#format}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#name StorageBlobInventoryPolicy#name}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#schedule StorageBlobInventoryPolicy#schedule}.
        :param schema_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#schema_fields StorageBlobInventoryPolicy#schema_fields}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#scope StorageBlobInventoryPolicy#scope}.
        :param storage_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#storage_container_name StorageBlobInventoryPolicy#storage_container_name}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#filter StorageBlobInventoryPolicy#filter}
        '''
        if isinstance(filter, dict):
            filter = StorageBlobInventoryPolicyRulesFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRules.__init__)
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument schema_fields", value=schema_fields, expected_type=type_hints["schema_fields"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument storage_container_name", value=storage_container_name, expected_type=type_hints["storage_container_name"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "format": format,
            "name": name,
            "schedule": schedule,
            "schema_fields": schema_fields,
            "scope": scope,
            "storage_container_name": storage_container_name,
        }
        if filter is not None:
            self._values["filter"] = filter

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#format StorageBlobInventoryPolicy#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#name StorageBlobInventoryPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#schedule StorageBlobInventoryPolicy#schedule}.'''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#schema_fields StorageBlobInventoryPolicy#schema_fields}.'''
        result = self._values.get("schema_fields")
        assert result is not None, "Required property 'schema_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#scope StorageBlobInventoryPolicy#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#storage_container_name StorageBlobInventoryPolicy#storage_container_name}.'''
        result = self._values.get("storage_container_name")
        assert result is not None, "Required property 'storage_container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Optional["StorageBlobInventoryPolicyRulesFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#filter StorageBlobInventoryPolicy#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["StorageBlobInventoryPolicyRulesFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobInventoryPolicyRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyRulesFilter",
    jsii_struct_bases=[],
    name_mapping={
        "blob_types": "blobTypes",
        "include_blob_versions": "includeBlobVersions",
        "include_snapshots": "includeSnapshots",
        "prefix_match": "prefixMatch",
    },
)
class StorageBlobInventoryPolicyRulesFilter:
    def __init__(
        self,
        *,
        blob_types: typing.Sequence[builtins.str],
        include_blob_versions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prefix_match: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blob_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#blob_types StorageBlobInventoryPolicy#blob_types}.
        :param include_blob_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_blob_versions StorageBlobInventoryPolicy#include_blob_versions}.
        :param include_snapshots: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_snapshots StorageBlobInventoryPolicy#include_snapshots}.
        :param prefix_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#prefix_match StorageBlobInventoryPolicy#prefix_match}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRulesFilter.__init__)
            check_type(argname="argument blob_types", value=blob_types, expected_type=type_hints["blob_types"])
            check_type(argname="argument include_blob_versions", value=include_blob_versions, expected_type=type_hints["include_blob_versions"])
            check_type(argname="argument include_snapshots", value=include_snapshots, expected_type=type_hints["include_snapshots"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "blob_types": blob_types,
        }
        if include_blob_versions is not None:
            self._values["include_blob_versions"] = include_blob_versions
        if include_snapshots is not None:
            self._values["include_snapshots"] = include_snapshots
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match

    @builtins.property
    def blob_types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#blob_types StorageBlobInventoryPolicy#blob_types}.'''
        result = self._values.get("blob_types")
        assert result is not None, "Required property 'blob_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def include_blob_versions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_blob_versions StorageBlobInventoryPolicy#include_blob_versions}.'''
        result = self._values.get("include_blob_versions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_snapshots(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_snapshots StorageBlobInventoryPolicy#include_snapshots}.'''
        result = self._values.get("include_snapshots")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#prefix_match StorageBlobInventoryPolicy#prefix_match}.'''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobInventoryPolicyRulesFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBlobInventoryPolicyRulesFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyRulesFilterOutputReference",
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
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRulesFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeBlobVersions")
    def reset_include_blob_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeBlobVersions", []))

    @jsii.member(jsii_name="resetIncludeSnapshots")
    def reset_include_snapshots(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSnapshots", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @builtins.property
    @jsii.member(jsii_name="blobTypesInput")
    def blob_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blobTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="includeBlobVersionsInput")
    def include_blob_versions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeBlobVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSnapshotsInput")
    def include_snapshots_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeSnapshotsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixMatchInput")
    def prefix_match_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "prefixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="blobTypes")
    def blob_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blobTypes"))

    @blob_types.setter
    def blob_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesFilterOutputReference, "blob_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobTypes", value)

    @builtins.property
    @jsii.member(jsii_name="includeBlobVersions")
    def include_blob_versions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeBlobVersions"))

    @include_blob_versions.setter
    def include_blob_versions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesFilterOutputReference, "include_blob_versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeBlobVersions", value)

    @builtins.property
    @jsii.member(jsii_name="includeSnapshots")
    def include_snapshots(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeSnapshots"))

    @include_snapshots.setter
    def include_snapshots(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesFilterOutputReference, "include_snapshots").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSnapshots", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesFilterOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageBlobInventoryPolicyRulesFilter]:
        return typing.cast(typing.Optional[StorageBlobInventoryPolicyRulesFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageBlobInventoryPolicyRulesFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageBlobInventoryPolicyRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyRulesList",
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
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageBlobInventoryPolicyRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageBlobInventoryPolicyRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageBlobInventoryPolicyRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageBlobInventoryPolicyRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageBlobInventoryPolicyRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageBlobInventoryPolicyRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyRulesOutputReference",
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
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        blob_types: typing.Sequence[builtins.str],
        include_blob_versions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prefix_match: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blob_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#blob_types StorageBlobInventoryPolicy#blob_types}.
        :param include_blob_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_blob_versions StorageBlobInventoryPolicy#include_blob_versions}.
        :param include_snapshots: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#include_snapshots StorageBlobInventoryPolicy#include_snapshots}.
        :param prefix_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#prefix_match StorageBlobInventoryPolicy#prefix_match}.
        '''
        value = StorageBlobInventoryPolicyRulesFilter(
            blob_types=blob_types,
            include_blob_versions=include_blob_versions,
            include_snapshots=include_snapshots,
            prefix_match=prefix_match,
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> StorageBlobInventoryPolicyRulesFilterOutputReference:
        return typing.cast(StorageBlobInventoryPolicyRulesFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[StorageBlobInventoryPolicyRulesFilter]:
        return typing.cast(typing.Optional[StorageBlobInventoryPolicyRulesFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaFieldsInput")
    def schema_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "schemaFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageContainerNameInput")
    def storage_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="schemaFields")
    def schema_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemaFields"))

    @schema_fields.setter
    def schema_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "schema_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaFields", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="storageContainerName")
    def storage_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageContainerName"))

    @storage_container_name.setter
    def storage_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "storage_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageBlobInventoryPolicyRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageBlobInventoryPolicyRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageBlobInventoryPolicyRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageBlobInventoryPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#create StorageBlobInventoryPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#delete StorageBlobInventoryPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#read StorageBlobInventoryPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#update StorageBlobInventoryPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#create StorageBlobInventoryPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#delete StorageBlobInventoryPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#read StorageBlobInventoryPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_blob_inventory_policy#update StorageBlobInventoryPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobInventoryPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBlobInventoryPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageBlobInventoryPolicy.StorageBlobInventoryPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StorageBlobInventoryPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageBlobInventoryPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageBlobInventoryPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageBlobInventoryPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBlobInventoryPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageBlobInventoryPolicy",
    "StorageBlobInventoryPolicyConfig",
    "StorageBlobInventoryPolicyRules",
    "StorageBlobInventoryPolicyRulesFilter",
    "StorageBlobInventoryPolicyRulesFilterOutputReference",
    "StorageBlobInventoryPolicyRulesList",
    "StorageBlobInventoryPolicyRulesOutputReference",
    "StorageBlobInventoryPolicyTimeouts",
    "StorageBlobInventoryPolicyTimeoutsOutputReference",
]

publication.publish()
