'''
# `azurerm_firewall_policy_rule_collection_group`

Refer to the Terraform Registory for docs: [`azurerm_firewall_policy_rule_collection_group`](https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group).
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


class FirewallPolicyRuleCollectionGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group azurerm_firewall_policy_rule_collection_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        firewall_policy_id: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        application_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollection", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        nat_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNatRuleCollection", typing.Dict[str, typing.Any]]]]] = None,
        network_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNetworkRuleCollection", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["FirewallPolicyRuleCollectionGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group azurerm_firewall_policy_rule_collection_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#firewall_policy_id FirewallPolicyRuleCollectionGroup#firewall_policy_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.
        :param application_rule_collection: application_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#application_rule_collection FirewallPolicyRuleCollectionGroup#application_rule_collection}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#id FirewallPolicyRuleCollectionGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param nat_rule_collection: nat_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#nat_rule_collection FirewallPolicyRuleCollectionGroup#nat_rule_collection}
        :param network_rule_collection: network_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#network_rule_collection FirewallPolicyRuleCollectionGroup#network_rule_collection}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#timeouts FirewallPolicyRuleCollectionGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FirewallPolicyRuleCollectionGroupConfig(
            firewall_policy_id=firewall_policy_id,
            name=name,
            priority=priority,
            application_rule_collection=application_rule_collection,
            id=id,
            nat_rule_collection=nat_rule_collection,
            network_rule_collection=network_rule_collection,
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

    @jsii.member(jsii_name="putApplicationRuleCollection")
    def put_application_rule_collection(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollection", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroup.put_application_rule_collection)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplicationRuleCollection", [value]))

    @jsii.member(jsii_name="putNatRuleCollection")
    def put_nat_rule_collection(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNatRuleCollection", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroup.put_nat_rule_collection)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNatRuleCollection", [value]))

    @jsii.member(jsii_name="putNetworkRuleCollection")
    def put_network_rule_collection(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNetworkRuleCollection", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroup.put_network_rule_collection)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkRuleCollection", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#create FirewallPolicyRuleCollectionGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#delete FirewallPolicyRuleCollectionGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#read FirewallPolicyRuleCollectionGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#update FirewallPolicyRuleCollectionGroup#update}.
        '''
        value = FirewallPolicyRuleCollectionGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplicationRuleCollection")
    def reset_application_rule_collection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationRuleCollection", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNatRuleCollection")
    def reset_nat_rule_collection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNatRuleCollection", []))

    @jsii.member(jsii_name="resetNetworkRuleCollection")
    def reset_network_rule_collection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkRuleCollection", []))

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
    @jsii.member(jsii_name="applicationRuleCollection")
    def application_rule_collection(
        self,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList":
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList", jsii.get(self, "applicationRuleCollection"))

    @builtins.property
    @jsii.member(jsii_name="natRuleCollection")
    def nat_rule_collection(
        self,
    ) -> "FirewallPolicyRuleCollectionGroupNatRuleCollectionList":
        return typing.cast("FirewallPolicyRuleCollectionGroupNatRuleCollectionList", jsii.get(self, "natRuleCollection"))

    @builtins.property
    @jsii.member(jsii_name="networkRuleCollection")
    def network_rule_collection(
        self,
    ) -> "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList":
        return typing.cast("FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList", jsii.get(self, "networkRuleCollection"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FirewallPolicyRuleCollectionGroupTimeoutsOutputReference":
        return typing.cast("FirewallPolicyRuleCollectionGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applicationRuleCollectionInput")
    def application_rule_collection_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollection"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollection"]]], jsii.get(self, "applicationRuleCollectionInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyIdInput")
    def firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="natRuleCollectionInput")
    def nat_rule_collection_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollection"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollection"]]], jsii.get(self, "natRuleCollectionInput"))

    @builtins.property
    @jsii.member(jsii_name="networkRuleCollectionInput")
    def network_rule_collection_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollection"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollection"]]], jsii.get(self, "networkRuleCollectionInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FirewallPolicyRuleCollectionGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FirewallPolicyRuleCollectionGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyId")
    def firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyId"))

    @firewall_policy_id.setter
    def firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroup, "firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroup, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollection",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "priority": "priority",
        "rule": "rule",
    },
)
class FirewallPolicyRuleCollectionGroupApplicationRuleCollection:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollection.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
            "priority": priority,
            "rule": rule,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupApplicationRuleCollection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollection]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList":
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollection, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollection, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollection, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "destination_addresses": "destinationAddresses",
        "destination_fqdns": "destinationFqdns",
        "destination_fqdn_tags": "destinationFqdnTags",
        "destination_urls": "destinationUrls",
        "protocols": "protocols",
        "source_addresses": "sourceAddresses",
        "source_ip_groups": "sourceIpGroups",
        "terminate_tls": "terminateTls",
        "web_categories": "webCategories",
    },
)
class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_fqdn_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        protocols: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols", typing.Dict[str, typing.Any]]]]] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        terminate_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        web_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#description FirewallPolicyRuleCollectionGroup#description}.
        :param destination_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_addresses FirewallPolicyRuleCollectionGroup#destination_addresses}.
        :param destination_fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdns FirewallPolicyRuleCollectionGroup#destination_fqdns}.
        :param destination_fqdn_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdn_tags FirewallPolicyRuleCollectionGroup#destination_fqdn_tags}.
        :param destination_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_urls FirewallPolicyRuleCollectionGroup#destination_urls}.
        :param protocols: protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}
        :param source_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.
        :param source_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.
        :param terminate_tls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#terminate_tls FirewallPolicyRuleCollectionGroup#terminate_tls}.
        :param web_categories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#web_categories FirewallPolicyRuleCollectionGroup#web_categories}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_addresses", value=destination_addresses, expected_type=type_hints["destination_addresses"])
            check_type(argname="argument destination_fqdns", value=destination_fqdns, expected_type=type_hints["destination_fqdns"])
            check_type(argname="argument destination_fqdn_tags", value=destination_fqdn_tags, expected_type=type_hints["destination_fqdn_tags"])
            check_type(argname="argument destination_urls", value=destination_urls, expected_type=type_hints["destination_urls"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument source_addresses", value=source_addresses, expected_type=type_hints["source_addresses"])
            check_type(argname="argument source_ip_groups", value=source_ip_groups, expected_type=type_hints["source_ip_groups"])
            check_type(argname="argument terminate_tls", value=terminate_tls, expected_type=type_hints["terminate_tls"])
            check_type(argname="argument web_categories", value=web_categories, expected_type=type_hints["web_categories"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if destination_addresses is not None:
            self._values["destination_addresses"] = destination_addresses
        if destination_fqdns is not None:
            self._values["destination_fqdns"] = destination_fqdns
        if destination_fqdn_tags is not None:
            self._values["destination_fqdn_tags"] = destination_fqdn_tags
        if destination_urls is not None:
            self._values["destination_urls"] = destination_urls
        if protocols is not None:
            self._values["protocols"] = protocols
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_ip_groups is not None:
            self._values["source_ip_groups"] = source_ip_groups
        if terminate_tls is not None:
            self._values["terminate_tls"] = terminate_tls
        if web_categories is not None:
            self._values["web_categories"] = web_categories

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#description FirewallPolicyRuleCollectionGroup#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_addresses FirewallPolicyRuleCollectionGroup#destination_addresses}.'''
        result = self._values.get("destination_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdns FirewallPolicyRuleCollectionGroup#destination_fqdns}.'''
        result = self._values.get("destination_fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_fqdn_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdn_tags FirewallPolicyRuleCollectionGroup#destination_fqdn_tags}.'''
        result = self._values.get("destination_fqdn_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_urls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_urls FirewallPolicyRuleCollectionGroup#destination_urls}.'''
        result = self._values.get("destination_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def protocols(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols"]]]:
        '''protocols block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}
        '''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols"]]], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.'''
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.'''
        result = self._values.get("source_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def terminate_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#terminate_tls FirewallPolicyRuleCollectionGroup#terminate_tls}.'''
        result = self._values.get("terminate_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def web_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#web_categories FirewallPolicyRuleCollectionGroup#web_categories}.'''
        result = self._values.get("web_categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putProtocols")
    def put_protocols(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference.put_protocols)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProtocols", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDestinationAddresses")
    def reset_destination_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddresses", []))

    @jsii.member(jsii_name="resetDestinationFqdns")
    def reset_destination_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFqdns", []))

    @jsii.member(jsii_name="resetDestinationFqdnTags")
    def reset_destination_fqdn_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFqdnTags", []))

    @jsii.member(jsii_name="resetDestinationUrls")
    def reset_destination_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationUrls", []))

    @jsii.member(jsii_name="resetProtocols")
    def reset_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocols", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceIpGroups")
    def reset_source_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpGroups", []))

    @jsii.member(jsii_name="resetTerminateTls")
    def reset_terminate_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateTls", []))

    @jsii.member(jsii_name="resetWebCategories")
    def reset_web_categories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebCategories", []))

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(
        self,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList":
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList", jsii.get(self, "protocols"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressesInput")
    def destination_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFqdnsInput")
    def destination_fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationFqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFqdnTagsInput")
    def destination_fqdn_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationFqdnTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationUrlsInput")
    def destination_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolsInput")
    def protocols_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols"]]], jsii.get(self, "protocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroupsInput")
    def source_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateTlsInput")
    def terminate_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "terminateTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="webCategoriesInput")
    def web_categories_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "webCategoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @destination_addresses.setter
    def destination_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "destination_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFqdns")
    def destination_fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationFqdns"))

    @destination_fqdns.setter
    def destination_fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "destination_fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFqdns", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFqdnTags")
    def destination_fqdn_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationFqdnTags"))

    @destination_fqdn_tags.setter
    def destination_fqdn_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "destination_fqdn_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFqdnTags", value)

    @builtins.property
    @jsii.member(jsii_name="destinationUrls")
    def destination_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationUrls"))

    @destination_urls.setter
    def destination_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "destination_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationUrls", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "source_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroups")
    def source_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceIpGroups"))

    @source_ip_groups.setter
    def source_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "source_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="terminateTls")
    def terminate_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "terminateTls"))

    @terminate_tls.setter
    def terminate_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "terminate_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminateTls", value)

    @builtins.property
    @jsii.member(jsii_name="webCategories")
    def web_categories(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "webCategories"))

    @web_categories.setter
    def web_categories(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "web_categories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webCategories", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "type": "type"},
)
class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols:
    def __init__(self, *, port: jsii.Number, type: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#port FirewallPolicyRuleCollectionGroup#port}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#type FirewallPolicyRuleCollectionGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
            "type": type,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#port FirewallPolicyRuleCollectionGroup#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#type FirewallPolicyRuleCollectionGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "firewall_policy_id": "firewallPolicyId",
        "name": "name",
        "priority": "priority",
        "application_rule_collection": "applicationRuleCollection",
        "id": "id",
        "nat_rule_collection": "natRuleCollection",
        "network_rule_collection": "networkRuleCollection",
        "timeouts": "timeouts",
    },
)
class FirewallPolicyRuleCollectionGroupConfig(cdktf.TerraformMetaArguments):
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
        firewall_policy_id: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        application_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FirewallPolicyRuleCollectionGroupApplicationRuleCollection, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        nat_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNatRuleCollection", typing.Dict[str, typing.Any]]]]] = None,
        network_rule_collection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNetworkRuleCollection", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["FirewallPolicyRuleCollectionGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#firewall_policy_id FirewallPolicyRuleCollectionGroup#firewall_policy_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.
        :param application_rule_collection: application_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#application_rule_collection FirewallPolicyRuleCollectionGroup#application_rule_collection}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#id FirewallPolicyRuleCollectionGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param nat_rule_collection: nat_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#nat_rule_collection FirewallPolicyRuleCollectionGroup#nat_rule_collection}
        :param network_rule_collection: network_rule_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#network_rule_collection FirewallPolicyRuleCollectionGroup#network_rule_collection}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#timeouts FirewallPolicyRuleCollectionGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = FirewallPolicyRuleCollectionGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument firewall_policy_id", value=firewall_policy_id, expected_type=type_hints["firewall_policy_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument application_rule_collection", value=application_rule_collection, expected_type=type_hints["application_rule_collection"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument nat_rule_collection", value=nat_rule_collection, expected_type=type_hints["nat_rule_collection"])
            check_type(argname="argument network_rule_collection", value=network_rule_collection, expected_type=type_hints["network_rule_collection"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_policy_id": firewall_policy_id,
            "name": name,
            "priority": priority,
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
        if application_rule_collection is not None:
            self._values["application_rule_collection"] = application_rule_collection
        if id is not None:
            self._values["id"] = id
        if nat_rule_collection is not None:
            self._values["nat_rule_collection"] = nat_rule_collection
        if network_rule_collection is not None:
            self._values["network_rule_collection"] = network_rule_collection
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
    def firewall_policy_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#firewall_policy_id FirewallPolicyRuleCollectionGroup#firewall_policy_id}.'''
        result = self._values.get("firewall_policy_id")
        assert result is not None, "Required property 'firewall_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def application_rule_collection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollection]]]:
        '''application_rule_collection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#application_rule_collection FirewallPolicyRuleCollectionGroup#application_rule_collection}
        '''
        result = self._values.get("application_rule_collection")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupApplicationRuleCollection]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#id FirewallPolicyRuleCollectionGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nat_rule_collection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollection"]]]:
        '''nat_rule_collection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#nat_rule_collection FirewallPolicyRuleCollectionGroup#nat_rule_collection}
        '''
        result = self._values.get("nat_rule_collection")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollection"]]], result)

    @builtins.property
    def network_rule_collection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollection"]]]:
        '''network_rule_collection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#network_rule_collection FirewallPolicyRuleCollectionGroup#network_rule_collection}
        '''
        result = self._values.get("network_rule_collection")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollection"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FirewallPolicyRuleCollectionGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#timeouts FirewallPolicyRuleCollectionGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FirewallPolicyRuleCollectionGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollection",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "priority": "priority",
        "rule": "rule",
    },
)
class FirewallPolicyRuleCollectionGroupNatRuleCollection:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollection.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
            "priority": priority,
            "rule": rule,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupNatRuleCollection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupNatRuleCollectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollectionList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollection]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList":
        return typing.cast("FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNatRuleCollectionRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollection, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollection, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollection, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollectionRule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "protocols": "protocols",
        "translated_port": "translatedPort",
        "destination_address": "destinationAddress",
        "destination_ports": "destinationPorts",
        "source_addresses": "sourceAddresses",
        "source_ip_groups": "sourceIpGroups",
        "translated_address": "translatedAddress",
        "translated_fqdn": "translatedFqdn",
    },
)
class FirewallPolicyRuleCollectionGroupNatRuleCollectionRule:
    def __init__(
        self,
        *,
        name: builtins.str,
        protocols: typing.Sequence[builtins.str],
        translated_port: jsii.Number,
        destination_address: typing.Optional[builtins.str] = None,
        destination_ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        translated_address: typing.Optional[builtins.str] = None,
        translated_fqdn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}.
        :param translated_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_port FirewallPolicyRuleCollectionGroup#translated_port}.
        :param destination_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_address FirewallPolicyRuleCollectionGroup#destination_address}.
        :param destination_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ports FirewallPolicyRuleCollectionGroup#destination_ports}.
        :param source_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.
        :param source_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.
        :param translated_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_address FirewallPolicyRuleCollectionGroup#translated_address}.
        :param translated_fqdn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_fqdn FirewallPolicyRuleCollectionGroup#translated_fqdn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionRule.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument translated_port", value=translated_port, expected_type=type_hints["translated_port"])
            check_type(argname="argument destination_address", value=destination_address, expected_type=type_hints["destination_address"])
            check_type(argname="argument destination_ports", value=destination_ports, expected_type=type_hints["destination_ports"])
            check_type(argname="argument source_addresses", value=source_addresses, expected_type=type_hints["source_addresses"])
            check_type(argname="argument source_ip_groups", value=source_ip_groups, expected_type=type_hints["source_ip_groups"])
            check_type(argname="argument translated_address", value=translated_address, expected_type=type_hints["translated_address"])
            check_type(argname="argument translated_fqdn", value=translated_fqdn, expected_type=type_hints["translated_fqdn"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "protocols": protocols,
            "translated_port": translated_port,
        }
        if destination_address is not None:
            self._values["destination_address"] = destination_address
        if destination_ports is not None:
            self._values["destination_ports"] = destination_ports
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_ip_groups is not None:
            self._values["source_ip_groups"] = source_ip_groups
        if translated_address is not None:
            self._values["translated_address"] = translated_address
        if translated_fqdn is not None:
            self._values["translated_fqdn"] = translated_fqdn

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocols(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}.'''
        result = self._values.get("protocols")
        assert result is not None, "Required property 'protocols' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def translated_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_port FirewallPolicyRuleCollectionGroup#translated_port}.'''
        result = self._values.get("translated_port")
        assert result is not None, "Required property 'translated_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def destination_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_address FirewallPolicyRuleCollectionGroup#destination_address}.'''
        result = self._values.get("destination_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ports FirewallPolicyRuleCollectionGroup#destination_ports}.'''
        result = self._values.get("destination_ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.'''
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.'''
        result = self._values.get("source_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def translated_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_address FirewallPolicyRuleCollectionGroup#translated_address}.'''
        result = self._values.get("translated_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def translated_fqdn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#translated_fqdn FirewallPolicyRuleCollectionGroup#translated_fqdn}.'''
        result = self._values.get("translated_fqdn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupNatRuleCollectionRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDestinationAddress")
    def reset_destination_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddress", []))

    @jsii.member(jsii_name="resetDestinationPorts")
    def reset_destination_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPorts", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceIpGroups")
    def reset_source_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpGroups", []))

    @jsii.member(jsii_name="resetTranslatedAddress")
    def reset_translated_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTranslatedAddress", []))

    @jsii.member(jsii_name="resetTranslatedFqdn")
    def reset_translated_fqdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTranslatedFqdn", []))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressInput")
    def destination_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortsInput")
    def destination_ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolsInput")
    def protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroupsInput")
    def source_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="translatedAddressInput")
    def translated_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "translatedAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="translatedFqdnInput")
    def translated_fqdn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "translatedFqdnInput"))

    @builtins.property
    @jsii.member(jsii_name="translatedPortInput")
    def translated_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "translatedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddress")
    def destination_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationAddress"))

    @destination_address.setter
    def destination_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "destination_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddress", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPorts")
    def destination_ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationPorts"))

    @destination_ports.setter
    def destination_ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "destination_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPorts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocols", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "source_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroups")
    def source_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceIpGroups"))

    @source_ip_groups.setter
    def source_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "source_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="translatedAddress")
    def translated_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "translatedAddress"))

    @translated_address.setter
    def translated_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "translated_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "translatedAddress", value)

    @builtins.property
    @jsii.member(jsii_name="translatedFqdn")
    def translated_fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "translatedFqdn"))

    @translated_fqdn.setter
    def translated_fqdn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "translated_fqdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "translatedFqdn", value)

    @builtins.property
    @jsii.member(jsii_name="translatedPort")
    def translated_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "translatedPort"))

    @translated_port.setter
    def translated_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "translated_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "translatedPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNatRuleCollectionRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollection",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "priority": "priority",
        "rule": "rule",
    },
)
class FirewallPolicyRuleCollectionGroupNetworkRuleCollection:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollection.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
            "priority": priority,
            "rule": rule,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#action FirewallPolicyRuleCollectionGroup#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#priority FirewallPolicyRuleCollectionGroup#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#rule FirewallPolicyRuleCollectionGroup#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupNetworkRuleCollection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollection]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList":
        return typing.cast("FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollection, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollection, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollection, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule",
    jsii_struct_bases=[],
    name_mapping={
        "destination_ports": "destinationPorts",
        "name": "name",
        "protocols": "protocols",
        "destination_addresses": "destinationAddresses",
        "destination_fqdns": "destinationFqdns",
        "destination_ip_groups": "destinationIpGroups",
        "source_addresses": "sourceAddresses",
        "source_ip_groups": "sourceIpGroups",
    },
)
class FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule:
    def __init__(
        self,
        *,
        destination_ports: typing.Sequence[builtins.str],
        name: builtins.str,
        protocols: typing.Sequence[builtins.str],
        destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param destination_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ports FirewallPolicyRuleCollectionGroup#destination_ports}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.
        :param protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}.
        :param destination_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_addresses FirewallPolicyRuleCollectionGroup#destination_addresses}.
        :param destination_fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdns FirewallPolicyRuleCollectionGroup#destination_fqdns}.
        :param destination_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ip_groups FirewallPolicyRuleCollectionGroup#destination_ip_groups}.
        :param source_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.
        :param source_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule.__init__)
            check_type(argname="argument destination_ports", value=destination_ports, expected_type=type_hints["destination_ports"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument destination_addresses", value=destination_addresses, expected_type=type_hints["destination_addresses"])
            check_type(argname="argument destination_fqdns", value=destination_fqdns, expected_type=type_hints["destination_fqdns"])
            check_type(argname="argument destination_ip_groups", value=destination_ip_groups, expected_type=type_hints["destination_ip_groups"])
            check_type(argname="argument source_addresses", value=source_addresses, expected_type=type_hints["source_addresses"])
            check_type(argname="argument source_ip_groups", value=source_ip_groups, expected_type=type_hints["source_ip_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_ports": destination_ports,
            "name": name,
            "protocols": protocols,
        }
        if destination_addresses is not None:
            self._values["destination_addresses"] = destination_addresses
        if destination_fqdns is not None:
            self._values["destination_fqdns"] = destination_fqdns
        if destination_ip_groups is not None:
            self._values["destination_ip_groups"] = destination_ip_groups
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_ip_groups is not None:
            self._values["source_ip_groups"] = source_ip_groups

    @builtins.property
    def destination_ports(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ports FirewallPolicyRuleCollectionGroup#destination_ports}.'''
        result = self._values.get("destination_ports")
        assert result is not None, "Required property 'destination_ports' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#name FirewallPolicyRuleCollectionGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocols(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#protocols FirewallPolicyRuleCollectionGroup#protocols}.'''
        result = self._values.get("protocols")
        assert result is not None, "Required property 'protocols' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def destination_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_addresses FirewallPolicyRuleCollectionGroup#destination_addresses}.'''
        result = self._values.get("destination_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_fqdns FirewallPolicyRuleCollectionGroup#destination_fqdns}.'''
        result = self._values.get("destination_fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#destination_ip_groups FirewallPolicyRuleCollectionGroup#destination_ip_groups}.'''
        result = self._values.get("destination_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_addresses FirewallPolicyRuleCollectionGroup#source_addresses}.'''
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#source_ip_groups FirewallPolicyRuleCollectionGroup#source_ip_groups}.'''
        result = self._values.get("source_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDestinationAddresses")
    def reset_destination_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddresses", []))

    @jsii.member(jsii_name="resetDestinationFqdns")
    def reset_destination_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFqdns", []))

    @jsii.member(jsii_name="resetDestinationIpGroups")
    def reset_destination_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationIpGroups", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceIpGroups")
    def reset_source_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpGroups", []))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressesInput")
    def destination_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFqdnsInput")
    def destination_fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationFqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationIpGroupsInput")
    def destination_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortsInput")
    def destination_ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolsInput")
    def protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroupsInput")
    def source_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @destination_addresses.setter
    def destination_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "destination_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFqdns")
    def destination_fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationFqdns"))

    @destination_fqdns.setter
    def destination_fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "destination_fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFqdns", value)

    @builtins.property
    @jsii.member(jsii_name="destinationIpGroups")
    def destination_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationIpGroups"))

    @destination_ip_groups.setter
    def destination_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "destination_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPorts")
    def destination_ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationPorts"))

    @destination_ports.setter
    def destination_ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "destination_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPorts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocols", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "source_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroups")
    def source_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceIpGroups"))

    @source_ip_groups.setter
    def source_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "source_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FirewallPolicyRuleCollectionGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#create FirewallPolicyRuleCollectionGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#delete FirewallPolicyRuleCollectionGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#read FirewallPolicyRuleCollectionGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#update FirewallPolicyRuleCollectionGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#create FirewallPolicyRuleCollectionGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#delete FirewallPolicyRuleCollectionGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#read FirewallPolicyRuleCollectionGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy_rule_collection_group#update FirewallPolicyRuleCollectionGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyRuleCollectionGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyRuleCollectionGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicyRuleCollectionGroup.FirewallPolicyRuleCollectionGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyRuleCollectionGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyRuleCollectionGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FirewallPolicyRuleCollectionGroup",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollection",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionList",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionOutputReference",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRule",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleList",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleOutputReference",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocols",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsList",
    "FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolsOutputReference",
    "FirewallPolicyRuleCollectionGroupConfig",
    "FirewallPolicyRuleCollectionGroupNatRuleCollection",
    "FirewallPolicyRuleCollectionGroupNatRuleCollectionList",
    "FirewallPolicyRuleCollectionGroupNatRuleCollectionOutputReference",
    "FirewallPolicyRuleCollectionGroupNatRuleCollectionRule",
    "FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleList",
    "FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleOutputReference",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollection",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionList",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionOutputReference",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRule",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleList",
    "FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleOutputReference",
    "FirewallPolicyRuleCollectionGroupTimeouts",
    "FirewallPolicyRuleCollectionGroupTimeoutsOutputReference",
]

publication.publish()
