'''
# `azurerm_storage_management_policy`

Refer to the Terraform Registory for docs: [`azurerm_storage_management_policy`](https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy).
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


class StorageManagementPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy azurerm_storage_management_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        storage_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageManagementPolicyRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["StorageManagementPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy azurerm_storage_management_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#storage_account_id StorageManagementPolicy#storage_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#id StorageManagementPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#rule StorageManagementPolicy#rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#timeouts StorageManagementPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageManagementPolicyConfig(
            storage_account_id=storage_account_id,
            id=id,
            rule=rule,
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

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageManagementPolicyRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicy.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#create StorageManagementPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete StorageManagementPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#read StorageManagementPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#update StorageManagementPolicy#update}.
        '''
        value = StorageManagementPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

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
    @jsii.member(jsii_name="rule")
    def rule(self) -> "StorageManagementPolicyRuleList":
        return typing.cast("StorageManagementPolicyRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageManagementPolicyTimeoutsOutputReference":
        return typing.cast("StorageManagementPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageManagementPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageManagementPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicy, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "storage_account_id": "storageAccountId",
        "id": "id",
        "rule": "rule",
        "timeouts": "timeouts",
    },
)
class StorageManagementPolicyConfig(cdktf.TerraformMetaArguments):
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
        storage_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageManagementPolicyRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["StorageManagementPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#storage_account_id StorageManagementPolicy#storage_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#id StorageManagementPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#rule StorageManagementPolicy#rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#timeouts StorageManagementPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = StorageManagementPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if rule is not None:
            self._values["rule"] = rule
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
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#storage_account_id StorageManagementPolicy#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#id StorageManagementPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#rule StorageManagementPolicy#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRule"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageManagementPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#timeouts StorageManagementPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageManagementPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRule",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "enabled": "enabled",
        "name": "name",
        "filters": "filters",
    },
)
class StorageManagementPolicyRule:
    def __init__(
        self,
        *,
        actions: typing.Union["StorageManagementPolicyRuleActions", typing.Dict[str, typing.Any]],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        filters: typing.Optional[typing.Union["StorageManagementPolicyRuleFilters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#actions StorageManagementPolicy#actions}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#enabled StorageManagementPolicy#enabled}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#name StorageManagementPolicy#name}.
        :param filters: filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#filters StorageManagementPolicy#filters}
        '''
        if isinstance(actions, dict):
            actions = StorageManagementPolicyRuleActions(**actions)
        if isinstance(filters, dict):
            filters = StorageManagementPolicyRuleFilters(**filters)
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRule.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "enabled": enabled,
            "name": name,
        }
        if filters is not None:
            self._values["filters"] = filters

    @builtins.property
    def actions(self) -> "StorageManagementPolicyRuleActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#actions StorageManagementPolicy#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("StorageManagementPolicyRuleActions", result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#enabled StorageManagementPolicy#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#name StorageManagementPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filters(self) -> typing.Optional["StorageManagementPolicyRuleFilters"]:
        '''filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#filters StorageManagementPolicy#filters}
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional["StorageManagementPolicyRuleFilters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "base_blob": "baseBlob",
        "snapshot": "snapshot",
        "version": "version",
    },
)
class StorageManagementPolicyRuleActions:
    def __init__(
        self,
        *,
        base_blob: typing.Optional[typing.Union["StorageManagementPolicyRuleActionsBaseBlob", typing.Dict[str, typing.Any]]] = None,
        snapshot: typing.Optional[typing.Union["StorageManagementPolicyRuleActionsSnapshot", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[typing.Union["StorageManagementPolicyRuleActionsVersion", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param base_blob: base_blob block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#base_blob StorageManagementPolicy#base_blob}
        :param snapshot: snapshot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#snapshot StorageManagementPolicy#snapshot}
        :param version: version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#version StorageManagementPolicy#version}
        '''
        if isinstance(base_blob, dict):
            base_blob = StorageManagementPolicyRuleActionsBaseBlob(**base_blob)
        if isinstance(snapshot, dict):
            snapshot = StorageManagementPolicyRuleActionsSnapshot(**snapshot)
        if isinstance(version, dict):
            version = StorageManagementPolicyRuleActionsVersion(**version)
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActions.__init__)
            check_type(argname="argument base_blob", value=base_blob, expected_type=type_hints["base_blob"])
            check_type(argname="argument snapshot", value=snapshot, expected_type=type_hints["snapshot"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if base_blob is not None:
            self._values["base_blob"] = base_blob
        if snapshot is not None:
            self._values["snapshot"] = snapshot
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def base_blob(
        self,
    ) -> typing.Optional["StorageManagementPolicyRuleActionsBaseBlob"]:
        '''base_blob block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#base_blob StorageManagementPolicy#base_blob}
        '''
        result = self._values.get("base_blob")
        return typing.cast(typing.Optional["StorageManagementPolicyRuleActionsBaseBlob"], result)

    @builtins.property
    def snapshot(self) -> typing.Optional["StorageManagementPolicyRuleActionsSnapshot"]:
        '''snapshot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#snapshot StorageManagementPolicy#snapshot}
        '''
        result = self._values.get("snapshot")
        return typing.cast(typing.Optional["StorageManagementPolicyRuleActionsSnapshot"], result)

    @builtins.property
    def version(self) -> typing.Optional["StorageManagementPolicyRuleActionsVersion"]:
        '''version block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#version StorageManagementPolicy#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional["StorageManagementPolicyRuleActionsVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsBaseBlob",
    jsii_struct_bases=[],
    name_mapping={
        "delete_after_days_since_last_access_time_greater_than": "deleteAfterDaysSinceLastAccessTimeGreaterThan",
        "delete_after_days_since_modification_greater_than": "deleteAfterDaysSinceModificationGreaterThan",
        "tier_to_archive_after_days_since_last_access_time_greater_than": "tierToArchiveAfterDaysSinceLastAccessTimeGreaterThan",
        "tier_to_archive_after_days_since_modification_greater_than": "tierToArchiveAfterDaysSinceModificationGreaterThan",
        "tier_to_cool_after_days_since_last_access_time_greater_than": "tierToCoolAfterDaysSinceLastAccessTimeGreaterThan",
        "tier_to_cool_after_days_since_modification_greater_than": "tierToCoolAfterDaysSinceModificationGreaterThan",
    },
)
class StorageManagementPolicyRuleActionsBaseBlob:
    def __init__(
        self,
        *,
        delete_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        delete_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_archive_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_archive_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_cool_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_cool_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delete_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_last_access_time_greater_than StorageManagementPolicy#delete_after_days_since_last_access_time_greater_than}.
        :param delete_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_modification_greater_than StorageManagementPolicy#delete_after_days_since_modification_greater_than}.
        :param tier_to_archive_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_last_access_time_greater_than}.
        :param tier_to_archive_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_modification_greater_than}.
        :param tier_to_cool_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_last_access_time_greater_than}.
        :param tier_to_cool_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_modification_greater_than}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsBaseBlob.__init__)
            check_type(argname="argument delete_after_days_since_last_access_time_greater_than", value=delete_after_days_since_last_access_time_greater_than, expected_type=type_hints["delete_after_days_since_last_access_time_greater_than"])
            check_type(argname="argument delete_after_days_since_modification_greater_than", value=delete_after_days_since_modification_greater_than, expected_type=type_hints["delete_after_days_since_modification_greater_than"])
            check_type(argname="argument tier_to_archive_after_days_since_last_access_time_greater_than", value=tier_to_archive_after_days_since_last_access_time_greater_than, expected_type=type_hints["tier_to_archive_after_days_since_last_access_time_greater_than"])
            check_type(argname="argument tier_to_archive_after_days_since_modification_greater_than", value=tier_to_archive_after_days_since_modification_greater_than, expected_type=type_hints["tier_to_archive_after_days_since_modification_greater_than"])
            check_type(argname="argument tier_to_cool_after_days_since_last_access_time_greater_than", value=tier_to_cool_after_days_since_last_access_time_greater_than, expected_type=type_hints["tier_to_cool_after_days_since_last_access_time_greater_than"])
            check_type(argname="argument tier_to_cool_after_days_since_modification_greater_than", value=tier_to_cool_after_days_since_modification_greater_than, expected_type=type_hints["tier_to_cool_after_days_since_modification_greater_than"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_after_days_since_last_access_time_greater_than is not None:
            self._values["delete_after_days_since_last_access_time_greater_than"] = delete_after_days_since_last_access_time_greater_than
        if delete_after_days_since_modification_greater_than is not None:
            self._values["delete_after_days_since_modification_greater_than"] = delete_after_days_since_modification_greater_than
        if tier_to_archive_after_days_since_last_access_time_greater_than is not None:
            self._values["tier_to_archive_after_days_since_last_access_time_greater_than"] = tier_to_archive_after_days_since_last_access_time_greater_than
        if tier_to_archive_after_days_since_modification_greater_than is not None:
            self._values["tier_to_archive_after_days_since_modification_greater_than"] = tier_to_archive_after_days_since_modification_greater_than
        if tier_to_cool_after_days_since_last_access_time_greater_than is not None:
            self._values["tier_to_cool_after_days_since_last_access_time_greater_than"] = tier_to_cool_after_days_since_last_access_time_greater_than
        if tier_to_cool_after_days_since_modification_greater_than is not None:
            self._values["tier_to_cool_after_days_since_modification_greater_than"] = tier_to_cool_after_days_since_modification_greater_than

    @builtins.property
    def delete_after_days_since_last_access_time_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_last_access_time_greater_than StorageManagementPolicy#delete_after_days_since_last_access_time_greater_than}.'''
        result = self._values.get("delete_after_days_since_last_access_time_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_after_days_since_modification_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_modification_greater_than StorageManagementPolicy#delete_after_days_since_modification_greater_than}.'''
        result = self._values.get("delete_after_days_since_modification_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tier_to_archive_after_days_since_last_access_time_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_last_access_time_greater_than}.'''
        result = self._values.get("tier_to_archive_after_days_since_last_access_time_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tier_to_archive_after_days_since_modification_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_modification_greater_than}.'''
        result = self._values.get("tier_to_archive_after_days_since_modification_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tier_to_cool_after_days_since_last_access_time_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_last_access_time_greater_than}.'''
        result = self._values.get("tier_to_cool_after_days_since_last_access_time_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tier_to_cool_after_days_since_modification_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_modification_greater_than}.'''
        result = self._values.get("tier_to_cool_after_days_since_modification_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleActionsBaseBlob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageManagementPolicyRuleActionsBaseBlobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsBaseBlobOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsBaseBlobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteAfterDaysSinceLastAccessTimeGreaterThan")
    def reset_delete_after_days_since_last_access_time_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfterDaysSinceLastAccessTimeGreaterThan", []))

    @jsii.member(jsii_name="resetDeleteAfterDaysSinceModificationGreaterThan")
    def reset_delete_after_days_since_modification_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfterDaysSinceModificationGreaterThan", []))

    @jsii.member(jsii_name="resetTierToArchiveAfterDaysSinceLastAccessTimeGreaterThan")
    def reset_tier_to_archive_after_days_since_last_access_time_greater_than(
        self,
    ) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTierToArchiveAfterDaysSinceLastAccessTimeGreaterThan", []))

    @jsii.member(jsii_name="resetTierToArchiveAfterDaysSinceModificationGreaterThan")
    def reset_tier_to_archive_after_days_since_modification_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTierToArchiveAfterDaysSinceModificationGreaterThan", []))

    @jsii.member(jsii_name="resetTierToCoolAfterDaysSinceLastAccessTimeGreaterThan")
    def reset_tier_to_cool_after_days_since_last_access_time_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTierToCoolAfterDaysSinceLastAccessTimeGreaterThan", []))

    @jsii.member(jsii_name="resetTierToCoolAfterDaysSinceModificationGreaterThan")
    def reset_tier_to_cool_after_days_since_modification_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTierToCoolAfterDaysSinceModificationGreaterThan", []))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceLastAccessTimeGreaterThanInput")
    def delete_after_days_since_last_access_time_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterDaysSinceLastAccessTimeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceModificationGreaterThanInput")
    def delete_after_days_since_modification_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterDaysSinceModificationGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="tierToArchiveAfterDaysSinceLastAccessTimeGreaterThanInput")
    def tier_to_archive_after_days_since_last_access_time_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tierToArchiveAfterDaysSinceLastAccessTimeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="tierToArchiveAfterDaysSinceModificationGreaterThanInput")
    def tier_to_archive_after_days_since_modification_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tierToArchiveAfterDaysSinceModificationGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="tierToCoolAfterDaysSinceLastAccessTimeGreaterThanInput")
    def tier_to_cool_after_days_since_last_access_time_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tierToCoolAfterDaysSinceLastAccessTimeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="tierToCoolAfterDaysSinceModificationGreaterThanInput")
    def tier_to_cool_after_days_since_modification_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tierToCoolAfterDaysSinceModificationGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceLastAccessTimeGreaterThan")
    def delete_after_days_since_last_access_time_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfterDaysSinceLastAccessTimeGreaterThan"))

    @delete_after_days_since_last_access_time_greater_than.setter
    def delete_after_days_since_last_access_time_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "delete_after_days_since_last_access_time_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfterDaysSinceLastAccessTimeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceModificationGreaterThan")
    def delete_after_days_since_modification_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfterDaysSinceModificationGreaterThan"))

    @delete_after_days_since_modification_greater_than.setter
    def delete_after_days_since_modification_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "delete_after_days_since_modification_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfterDaysSinceModificationGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="tierToArchiveAfterDaysSinceLastAccessTimeGreaterThan")
    def tier_to_archive_after_days_since_last_access_time_greater_than(
        self,
    ) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tierToArchiveAfterDaysSinceLastAccessTimeGreaterThan"))

    @tier_to_archive_after_days_since_last_access_time_greater_than.setter
    def tier_to_archive_after_days_since_last_access_time_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "tier_to_archive_after_days_since_last_access_time_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tierToArchiveAfterDaysSinceLastAccessTimeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="tierToArchiveAfterDaysSinceModificationGreaterThan")
    def tier_to_archive_after_days_since_modification_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tierToArchiveAfterDaysSinceModificationGreaterThan"))

    @tier_to_archive_after_days_since_modification_greater_than.setter
    def tier_to_archive_after_days_since_modification_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "tier_to_archive_after_days_since_modification_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tierToArchiveAfterDaysSinceModificationGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="tierToCoolAfterDaysSinceLastAccessTimeGreaterThan")
    def tier_to_cool_after_days_since_last_access_time_greater_than(
        self,
    ) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tierToCoolAfterDaysSinceLastAccessTimeGreaterThan"))

    @tier_to_cool_after_days_since_last_access_time_greater_than.setter
    def tier_to_cool_after_days_since_last_access_time_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "tier_to_cool_after_days_since_last_access_time_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tierToCoolAfterDaysSinceLastAccessTimeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="tierToCoolAfterDaysSinceModificationGreaterThan")
    def tier_to_cool_after_days_since_modification_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tierToCoolAfterDaysSinceModificationGreaterThan"))

    @tier_to_cool_after_days_since_modification_greater_than.setter
    def tier_to_cool_after_days_since_modification_greater_than(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "tier_to_cool_after_days_since_modification_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tierToCoolAfterDaysSinceModificationGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageManagementPolicyRuleActionsBaseBlob]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActionsBaseBlob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageManagementPolicyRuleActionsBaseBlob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsBaseBlobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageManagementPolicyRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBaseBlob")
    def put_base_blob(
        self,
        *,
        delete_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        delete_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_archive_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_archive_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_cool_after_days_since_last_access_time_greater_than: typing.Optional[jsii.Number] = None,
        tier_to_cool_after_days_since_modification_greater_than: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delete_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_last_access_time_greater_than StorageManagementPolicy#delete_after_days_since_last_access_time_greater_than}.
        :param delete_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_modification_greater_than StorageManagementPolicy#delete_after_days_since_modification_greater_than}.
        :param tier_to_archive_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_last_access_time_greater_than}.
        :param tier_to_archive_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_archive_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_archive_after_days_since_modification_greater_than}.
        :param tier_to_cool_after_days_since_last_access_time_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_last_access_time_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_last_access_time_greater_than}.
        :param tier_to_cool_after_days_since_modification_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#tier_to_cool_after_days_since_modification_greater_than StorageManagementPolicy#tier_to_cool_after_days_since_modification_greater_than}.
        '''
        value = StorageManagementPolicyRuleActionsBaseBlob(
            delete_after_days_since_last_access_time_greater_than=delete_after_days_since_last_access_time_greater_than,
            delete_after_days_since_modification_greater_than=delete_after_days_since_modification_greater_than,
            tier_to_archive_after_days_since_last_access_time_greater_than=tier_to_archive_after_days_since_last_access_time_greater_than,
            tier_to_archive_after_days_since_modification_greater_than=tier_to_archive_after_days_since_modification_greater_than,
            tier_to_cool_after_days_since_last_access_time_greater_than=tier_to_cool_after_days_since_last_access_time_greater_than,
            tier_to_cool_after_days_since_modification_greater_than=tier_to_cool_after_days_since_modification_greater_than,
        )

        return typing.cast(None, jsii.invoke(self, "putBaseBlob", [value]))

    @jsii.member(jsii_name="putSnapshot")
    def put_snapshot(
        self,
        *,
        change_tier_to_archive_after_days_since_creation: typing.Optional[jsii.Number] = None,
        change_tier_to_cool_after_days_since_creation: typing.Optional[jsii.Number] = None,
        delete_after_days_since_creation_greater_than: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param change_tier_to_archive_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.
        :param change_tier_to_cool_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.
        :param delete_after_days_since_creation_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation_greater_than StorageManagementPolicy#delete_after_days_since_creation_greater_than}.
        '''
        value = StorageManagementPolicyRuleActionsSnapshot(
            change_tier_to_archive_after_days_since_creation=change_tier_to_archive_after_days_since_creation,
            change_tier_to_cool_after_days_since_creation=change_tier_to_cool_after_days_since_creation,
            delete_after_days_since_creation_greater_than=delete_after_days_since_creation_greater_than,
        )

        return typing.cast(None, jsii.invoke(self, "putSnapshot", [value]))

    @jsii.member(jsii_name="putVersion")
    def put_version(
        self,
        *,
        change_tier_to_archive_after_days_since_creation: typing.Optional[jsii.Number] = None,
        change_tier_to_cool_after_days_since_creation: typing.Optional[jsii.Number] = None,
        delete_after_days_since_creation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param change_tier_to_archive_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.
        :param change_tier_to_cool_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.
        :param delete_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation StorageManagementPolicy#delete_after_days_since_creation}.
        '''
        value = StorageManagementPolicyRuleActionsVersion(
            change_tier_to_archive_after_days_since_creation=change_tier_to_archive_after_days_since_creation,
            change_tier_to_cool_after_days_since_creation=change_tier_to_cool_after_days_since_creation,
            delete_after_days_since_creation=delete_after_days_since_creation,
        )

        return typing.cast(None, jsii.invoke(self, "putVersion", [value]))

    @jsii.member(jsii_name="resetBaseBlob")
    def reset_base_blob(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseBlob", []))

    @jsii.member(jsii_name="resetSnapshot")
    def reset_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshot", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="baseBlob")
    def base_blob(self) -> StorageManagementPolicyRuleActionsBaseBlobOutputReference:
        return typing.cast(StorageManagementPolicyRuleActionsBaseBlobOutputReference, jsii.get(self, "baseBlob"))

    @builtins.property
    @jsii.member(jsii_name="snapshot")
    def snapshot(self) -> "StorageManagementPolicyRuleActionsSnapshotOutputReference":
        return typing.cast("StorageManagementPolicyRuleActionsSnapshotOutputReference", jsii.get(self, "snapshot"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> "StorageManagementPolicyRuleActionsVersionOutputReference":
        return typing.cast("StorageManagementPolicyRuleActionsVersionOutputReference", jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="baseBlobInput")
    def base_blob_input(
        self,
    ) -> typing.Optional[StorageManagementPolicyRuleActionsBaseBlob]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActionsBaseBlob], jsii.get(self, "baseBlobInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotInput")
    def snapshot_input(
        self,
    ) -> typing.Optional["StorageManagementPolicyRuleActionsSnapshot"]:
        return typing.cast(typing.Optional["StorageManagementPolicyRuleActionsSnapshot"], jsii.get(self, "snapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(
        self,
    ) -> typing.Optional["StorageManagementPolicyRuleActionsVersion"]:
        return typing.cast(typing.Optional["StorageManagementPolicyRuleActionsVersion"], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageManagementPolicyRuleActions]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageManagementPolicyRuleActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsSnapshot",
    jsii_struct_bases=[],
    name_mapping={
        "change_tier_to_archive_after_days_since_creation": "changeTierToArchiveAfterDaysSinceCreation",
        "change_tier_to_cool_after_days_since_creation": "changeTierToCoolAfterDaysSinceCreation",
        "delete_after_days_since_creation_greater_than": "deleteAfterDaysSinceCreationGreaterThan",
    },
)
class StorageManagementPolicyRuleActionsSnapshot:
    def __init__(
        self,
        *,
        change_tier_to_archive_after_days_since_creation: typing.Optional[jsii.Number] = None,
        change_tier_to_cool_after_days_since_creation: typing.Optional[jsii.Number] = None,
        delete_after_days_since_creation_greater_than: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param change_tier_to_archive_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.
        :param change_tier_to_cool_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.
        :param delete_after_days_since_creation_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation_greater_than StorageManagementPolicy#delete_after_days_since_creation_greater_than}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsSnapshot.__init__)
            check_type(argname="argument change_tier_to_archive_after_days_since_creation", value=change_tier_to_archive_after_days_since_creation, expected_type=type_hints["change_tier_to_archive_after_days_since_creation"])
            check_type(argname="argument change_tier_to_cool_after_days_since_creation", value=change_tier_to_cool_after_days_since_creation, expected_type=type_hints["change_tier_to_cool_after_days_since_creation"])
            check_type(argname="argument delete_after_days_since_creation_greater_than", value=delete_after_days_since_creation_greater_than, expected_type=type_hints["delete_after_days_since_creation_greater_than"])
        self._values: typing.Dict[str, typing.Any] = {}
        if change_tier_to_archive_after_days_since_creation is not None:
            self._values["change_tier_to_archive_after_days_since_creation"] = change_tier_to_archive_after_days_since_creation
        if change_tier_to_cool_after_days_since_creation is not None:
            self._values["change_tier_to_cool_after_days_since_creation"] = change_tier_to_cool_after_days_since_creation
        if delete_after_days_since_creation_greater_than is not None:
            self._values["delete_after_days_since_creation_greater_than"] = delete_after_days_since_creation_greater_than

    @builtins.property
    def change_tier_to_archive_after_days_since_creation(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.'''
        result = self._values.get("change_tier_to_archive_after_days_since_creation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def change_tier_to_cool_after_days_since_creation(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.'''
        result = self._values.get("change_tier_to_cool_after_days_since_creation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_after_days_since_creation_greater_than(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation_greater_than StorageManagementPolicy#delete_after_days_since_creation_greater_than}.'''
        result = self._values.get("delete_after_days_since_creation_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleActionsSnapshot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageManagementPolicyRuleActionsSnapshotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsSnapshotOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsSnapshotOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChangeTierToArchiveAfterDaysSinceCreation")
    def reset_change_tier_to_archive_after_days_since_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeTierToArchiveAfterDaysSinceCreation", []))

    @jsii.member(jsii_name="resetChangeTierToCoolAfterDaysSinceCreation")
    def reset_change_tier_to_cool_after_days_since_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeTierToCoolAfterDaysSinceCreation", []))

    @jsii.member(jsii_name="resetDeleteAfterDaysSinceCreationGreaterThan")
    def reset_delete_after_days_since_creation_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfterDaysSinceCreationGreaterThan", []))

    @builtins.property
    @jsii.member(jsii_name="changeTierToArchiveAfterDaysSinceCreationInput")
    def change_tier_to_archive_after_days_since_creation_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "changeTierToArchiveAfterDaysSinceCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="changeTierToCoolAfterDaysSinceCreationInput")
    def change_tier_to_cool_after_days_since_creation_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "changeTierToCoolAfterDaysSinceCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceCreationGreaterThanInput")
    def delete_after_days_since_creation_greater_than_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterDaysSinceCreationGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="changeTierToArchiveAfterDaysSinceCreation")
    def change_tier_to_archive_after_days_since_creation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changeTierToArchiveAfterDaysSinceCreation"))

    @change_tier_to_archive_after_days_since_creation.setter
    def change_tier_to_archive_after_days_since_creation(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsSnapshotOutputReference, "change_tier_to_archive_after_days_since_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeTierToArchiveAfterDaysSinceCreation", value)

    @builtins.property
    @jsii.member(jsii_name="changeTierToCoolAfterDaysSinceCreation")
    def change_tier_to_cool_after_days_since_creation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changeTierToCoolAfterDaysSinceCreation"))

    @change_tier_to_cool_after_days_since_creation.setter
    def change_tier_to_cool_after_days_since_creation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsSnapshotOutputReference, "change_tier_to_cool_after_days_since_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeTierToCoolAfterDaysSinceCreation", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceCreationGreaterThan")
    def delete_after_days_since_creation_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfterDaysSinceCreationGreaterThan"))

    @delete_after_days_since_creation_greater_than.setter
    def delete_after_days_since_creation_greater_than(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsSnapshotOutputReference, "delete_after_days_since_creation_greater_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfterDaysSinceCreationGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageManagementPolicyRuleActionsSnapshot]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActionsSnapshot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageManagementPolicyRuleActionsSnapshot],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsSnapshotOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsVersion",
    jsii_struct_bases=[],
    name_mapping={
        "change_tier_to_archive_after_days_since_creation": "changeTierToArchiveAfterDaysSinceCreation",
        "change_tier_to_cool_after_days_since_creation": "changeTierToCoolAfterDaysSinceCreation",
        "delete_after_days_since_creation": "deleteAfterDaysSinceCreation",
    },
)
class StorageManagementPolicyRuleActionsVersion:
    def __init__(
        self,
        *,
        change_tier_to_archive_after_days_since_creation: typing.Optional[jsii.Number] = None,
        change_tier_to_cool_after_days_since_creation: typing.Optional[jsii.Number] = None,
        delete_after_days_since_creation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param change_tier_to_archive_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.
        :param change_tier_to_cool_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.
        :param delete_after_days_since_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation StorageManagementPolicy#delete_after_days_since_creation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsVersion.__init__)
            check_type(argname="argument change_tier_to_archive_after_days_since_creation", value=change_tier_to_archive_after_days_since_creation, expected_type=type_hints["change_tier_to_archive_after_days_since_creation"])
            check_type(argname="argument change_tier_to_cool_after_days_since_creation", value=change_tier_to_cool_after_days_since_creation, expected_type=type_hints["change_tier_to_cool_after_days_since_creation"])
            check_type(argname="argument delete_after_days_since_creation", value=delete_after_days_since_creation, expected_type=type_hints["delete_after_days_since_creation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if change_tier_to_archive_after_days_since_creation is not None:
            self._values["change_tier_to_archive_after_days_since_creation"] = change_tier_to_archive_after_days_since_creation
        if change_tier_to_cool_after_days_since_creation is not None:
            self._values["change_tier_to_cool_after_days_since_creation"] = change_tier_to_cool_after_days_since_creation
        if delete_after_days_since_creation is not None:
            self._values["delete_after_days_since_creation"] = delete_after_days_since_creation

    @builtins.property
    def change_tier_to_archive_after_days_since_creation(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_archive_after_days_since_creation StorageManagementPolicy#change_tier_to_archive_after_days_since_creation}.'''
        result = self._values.get("change_tier_to_archive_after_days_since_creation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def change_tier_to_cool_after_days_since_creation(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#change_tier_to_cool_after_days_since_creation StorageManagementPolicy#change_tier_to_cool_after_days_since_creation}.'''
        result = self._values.get("change_tier_to_cool_after_days_since_creation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_after_days_since_creation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete_after_days_since_creation StorageManagementPolicy#delete_after_days_since_creation}.'''
        result = self._values.get("delete_after_days_since_creation")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleActionsVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageManagementPolicyRuleActionsVersionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleActionsVersionOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleActionsVersionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChangeTierToArchiveAfterDaysSinceCreation")
    def reset_change_tier_to_archive_after_days_since_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeTierToArchiveAfterDaysSinceCreation", []))

    @jsii.member(jsii_name="resetChangeTierToCoolAfterDaysSinceCreation")
    def reset_change_tier_to_cool_after_days_since_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeTierToCoolAfterDaysSinceCreation", []))

    @jsii.member(jsii_name="resetDeleteAfterDaysSinceCreation")
    def reset_delete_after_days_since_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfterDaysSinceCreation", []))

    @builtins.property
    @jsii.member(jsii_name="changeTierToArchiveAfterDaysSinceCreationInput")
    def change_tier_to_archive_after_days_since_creation_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "changeTierToArchiveAfterDaysSinceCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="changeTierToCoolAfterDaysSinceCreationInput")
    def change_tier_to_cool_after_days_since_creation_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "changeTierToCoolAfterDaysSinceCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceCreationInput")
    def delete_after_days_since_creation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterDaysSinceCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="changeTierToArchiveAfterDaysSinceCreation")
    def change_tier_to_archive_after_days_since_creation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changeTierToArchiveAfterDaysSinceCreation"))

    @change_tier_to_archive_after_days_since_creation.setter
    def change_tier_to_archive_after_days_since_creation(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsVersionOutputReference, "change_tier_to_archive_after_days_since_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeTierToArchiveAfterDaysSinceCreation", value)

    @builtins.property
    @jsii.member(jsii_name="changeTierToCoolAfterDaysSinceCreation")
    def change_tier_to_cool_after_days_since_creation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changeTierToCoolAfterDaysSinceCreation"))

    @change_tier_to_cool_after_days_since_creation.setter
    def change_tier_to_cool_after_days_since_creation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsVersionOutputReference, "change_tier_to_cool_after_days_since_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeTierToCoolAfterDaysSinceCreation", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAfterDaysSinceCreation")
    def delete_after_days_since_creation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfterDaysSinceCreation"))

    @delete_after_days_since_creation.setter
    def delete_after_days_since_creation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsVersionOutputReference, "delete_after_days_since_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfterDaysSinceCreation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageManagementPolicyRuleActionsVersion]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActionsVersion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageManagementPolicyRuleActionsVersion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleActionsVersionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleFilters",
    jsii_struct_bases=[],
    name_mapping={
        "blob_types": "blobTypes",
        "match_blob_index_tag": "matchBlobIndexTag",
        "prefix_match": "prefixMatch",
    },
)
class StorageManagementPolicyRuleFilters:
    def __init__(
        self,
        *,
        blob_types: typing.Sequence[builtins.str],
        match_blob_index_tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageManagementPolicyRuleFiltersMatchBlobIndexTag", typing.Dict[str, typing.Any]]]]] = None,
        prefix_match: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blob_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#blob_types StorageManagementPolicy#blob_types}.
        :param match_blob_index_tag: match_blob_index_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#match_blob_index_tag StorageManagementPolicy#match_blob_index_tag}
        :param prefix_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#prefix_match StorageManagementPolicy#prefix_match}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFilters.__init__)
            check_type(argname="argument blob_types", value=blob_types, expected_type=type_hints["blob_types"])
            check_type(argname="argument match_blob_index_tag", value=match_blob_index_tag, expected_type=type_hints["match_blob_index_tag"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "blob_types": blob_types,
        }
        if match_blob_index_tag is not None:
            self._values["match_blob_index_tag"] = match_blob_index_tag
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match

    @builtins.property
    def blob_types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#blob_types StorageManagementPolicy#blob_types}.'''
        result = self._values.get("blob_types")
        assert result is not None, "Required property 'blob_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def match_blob_index_tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRuleFiltersMatchBlobIndexTag"]]]:
        '''match_blob_index_tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#match_blob_index_tag StorageManagementPolicy#match_blob_index_tag}
        '''
        result = self._values.get("match_blob_index_tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageManagementPolicyRuleFiltersMatchBlobIndexTag"]]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#prefix_match StorageManagementPolicy#prefix_match}.'''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleFiltersMatchBlobIndexTag",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "operation": "operation"},
)
class StorageManagementPolicyRuleFiltersMatchBlobIndexTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        operation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#name StorageManagementPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#value StorageManagementPolicy#value}.
        :param operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#operation StorageManagementPolicy#operation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersMatchBlobIndexTag.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if operation is not None:
            self._values["operation"] = operation

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#name StorageManagementPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#value StorageManagementPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#operation StorageManagementPolicy#operation}.'''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyRuleFiltersMatchBlobIndexTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageManagementPolicyRuleFiltersMatchBlobIndexTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleFiltersMatchBlobIndexTagList",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRuleFiltersMatchBlobIndexTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRuleFiltersMatchBlobIndexTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRuleFiltersMatchBlobIndexTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference, "operation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageManagementPolicyRuleFiltersMatchBlobIndexTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageManagementPolicyRuleFiltersMatchBlobIndexTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageManagementPolicyRuleFiltersMatchBlobIndexTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageManagementPolicyRuleFiltersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleFiltersOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchBlobIndexTag")
    def put_match_blob_index_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[StorageManagementPolicyRuleFiltersMatchBlobIndexTag, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleFiltersOutputReference.put_match_blob_index_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchBlobIndexTag", [value]))

    @jsii.member(jsii_name="resetMatchBlobIndexTag")
    def reset_match_blob_index_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchBlobIndexTag", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @builtins.property
    @jsii.member(jsii_name="matchBlobIndexTag")
    def match_blob_index_tag(
        self,
    ) -> StorageManagementPolicyRuleFiltersMatchBlobIndexTagList:
        return typing.cast(StorageManagementPolicyRuleFiltersMatchBlobIndexTagList, jsii.get(self, "matchBlobIndexTag"))

    @builtins.property
    @jsii.member(jsii_name="blobTypesInput")
    def blob_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blobTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchBlobIndexTagInput")
    def match_blob_index_tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRuleFiltersMatchBlobIndexTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRuleFiltersMatchBlobIndexTag]]], jsii.get(self, "matchBlobIndexTagInput"))

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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersOutputReference, "blob_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobTypes", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageManagementPolicyRuleFilters]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleFilters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageManagementPolicyRuleFilters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleFiltersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageManagementPolicyRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleList",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageManagementPolicyRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageManagementPolicyRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageManagementPolicyRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageManagementPolicyRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyRuleOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        base_blob: typing.Optional[typing.Union[StorageManagementPolicyRuleActionsBaseBlob, typing.Dict[str, typing.Any]]] = None,
        snapshot: typing.Optional[typing.Union[StorageManagementPolicyRuleActionsSnapshot, typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[typing.Union[StorageManagementPolicyRuleActionsVersion, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param base_blob: base_blob block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#base_blob StorageManagementPolicy#base_blob}
        :param snapshot: snapshot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#snapshot StorageManagementPolicy#snapshot}
        :param version: version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#version StorageManagementPolicy#version}
        '''
        value = StorageManagementPolicyRuleActions(
            base_blob=base_blob, snapshot=snapshot, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putFilters")
    def put_filters(
        self,
        *,
        blob_types: typing.Sequence[builtins.str],
        match_blob_index_tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[StorageManagementPolicyRuleFiltersMatchBlobIndexTag, typing.Dict[str, typing.Any]]]]] = None,
        prefix_match: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blob_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#blob_types StorageManagementPolicy#blob_types}.
        :param match_blob_index_tag: match_blob_index_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#match_blob_index_tag StorageManagementPolicy#match_blob_index_tag}
        :param prefix_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#prefix_match StorageManagementPolicy#prefix_match}.
        '''
        value = StorageManagementPolicyRuleFilters(
            blob_types=blob_types,
            match_blob_index_tag=match_blob_index_tag,
            prefix_match=prefix_match,
        )

        return typing.cast(None, jsii.invoke(self, "putFilters", [value]))

    @jsii.member(jsii_name="resetFilters")
    def reset_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilters", []))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> StorageManagementPolicyRuleActionsOutputReference:
        return typing.cast(StorageManagementPolicyRuleActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(self) -> StorageManagementPolicyRuleFiltersOutputReference:
        return typing.cast(StorageManagementPolicyRuleFiltersOutputReference, jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[StorageManagementPolicyRuleActions]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filtersInput")
    def filters_input(self) -> typing.Optional[StorageManagementPolicyRuleFilters]:
        return typing.cast(typing.Optional[StorageManagementPolicyRuleFilters], jsii.get(self, "filtersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageManagementPolicyRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageManagementPolicyRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageManagementPolicyRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageManagementPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#create StorageManagementPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete StorageManagementPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#read StorageManagementPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#update StorageManagementPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageManagementPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#create StorageManagementPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#delete StorageManagementPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#read StorageManagementPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_management_policy#update StorageManagementPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageManagementPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageManagementPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageManagementPolicy.StorageManagementPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StorageManagementPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageManagementPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageManagementPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageManagementPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageManagementPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageManagementPolicy",
    "StorageManagementPolicyConfig",
    "StorageManagementPolicyRule",
    "StorageManagementPolicyRuleActions",
    "StorageManagementPolicyRuleActionsBaseBlob",
    "StorageManagementPolicyRuleActionsBaseBlobOutputReference",
    "StorageManagementPolicyRuleActionsOutputReference",
    "StorageManagementPolicyRuleActionsSnapshot",
    "StorageManagementPolicyRuleActionsSnapshotOutputReference",
    "StorageManagementPolicyRuleActionsVersion",
    "StorageManagementPolicyRuleActionsVersionOutputReference",
    "StorageManagementPolicyRuleFilters",
    "StorageManagementPolicyRuleFiltersMatchBlobIndexTag",
    "StorageManagementPolicyRuleFiltersMatchBlobIndexTagList",
    "StorageManagementPolicyRuleFiltersMatchBlobIndexTagOutputReference",
    "StorageManagementPolicyRuleFiltersOutputReference",
    "StorageManagementPolicyRuleList",
    "StorageManagementPolicyRuleOutputReference",
    "StorageManagementPolicyTimeouts",
    "StorageManagementPolicyTimeoutsOutputReference",
]

publication.publish()
