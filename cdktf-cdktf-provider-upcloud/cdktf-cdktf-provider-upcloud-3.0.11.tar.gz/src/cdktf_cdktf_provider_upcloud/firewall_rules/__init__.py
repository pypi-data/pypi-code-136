'''
# `upcloud_firewall_rules`

Refer to the Terraform Registory for docs: [`upcloud_firewall_rules`](https://www.terraform.io/docs/providers/upcloud/r/firewall_rules).
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


class FirewallRules(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.firewallRules.FirewallRules",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules upcloud_firewall_rules}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        firewall_rule: typing.Union[typing.Sequence[typing.Union["FirewallRulesFirewallRule", typing.Dict[str, typing.Any]]], cdktf.IResolvable],
        server_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules upcloud_firewall_rules} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param firewall_rule: firewall_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#firewall_rule FirewallRules#firewall_rule}
        :param server_id: The unique id of the server to be protected the firewall rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#server_id FirewallRules#server_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#id FirewallRules#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallRules.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FirewallRulesConfig(
            firewall_rule=firewall_rule,
            server_id=server_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFirewallRule")
    def put_firewall_rule(
        self,
        value: typing.Union[typing.Sequence[typing.Union["FirewallRulesFirewallRule", typing.Dict[str, typing.Any]]], cdktf.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallRules.put_firewall_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFirewallRule", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="firewallRule")
    def firewall_rule(self) -> "FirewallRulesFirewallRuleList":
        return typing.cast("FirewallRulesFirewallRuleList", jsii.get(self, "firewallRule"))

    @builtins.property
    @jsii.member(jsii_name="firewallRuleInput")
    def firewall_rule_input(
        self,
    ) -> typing.Optional[typing.Union[typing.List["FirewallRulesFirewallRule"], cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[typing.List["FirewallRulesFirewallRule"], cdktf.IResolvable]], jsii.get(self, "firewallRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIdInput")
    def server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRules, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRules, "server_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.firewallRules.FirewallRulesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "firewall_rule": "firewallRule",
        "server_id": "serverId",
        "id": "id",
    },
)
class FirewallRulesConfig(cdktf.TerraformMetaArguments):
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
        firewall_rule: typing.Union[typing.Sequence[typing.Union["FirewallRulesFirewallRule", typing.Dict[str, typing.Any]]], cdktf.IResolvable],
        server_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param firewall_rule: firewall_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#firewall_rule FirewallRules#firewall_rule}
        :param server_id: The unique id of the server to be protected the firewall rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#server_id FirewallRules#server_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#id FirewallRules#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(FirewallRulesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument firewall_rule", value=firewall_rule, expected_type=type_hints["firewall_rule"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_rule": firewall_rule,
            "server_id": server_id,
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
    def firewall_rule(
        self,
    ) -> typing.Union[typing.List["FirewallRulesFirewallRule"], cdktf.IResolvable]:
        '''firewall_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#firewall_rule FirewallRules#firewall_rule}
        '''
        result = self._values.get("firewall_rule")
        assert result is not None, "Required property 'firewall_rule' is missing"
        return typing.cast(typing.Union[typing.List["FirewallRulesFirewallRule"], cdktf.IResolvable], result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''The unique id of the server to be protected the firewall rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#server_id FirewallRules#server_id}
        '''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#id FirewallRules#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.firewallRules.FirewallRulesFirewallRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "direction": "direction",
        "comment": "comment",
        "destination_address_end": "destinationAddressEnd",
        "destination_address_start": "destinationAddressStart",
        "destination_port_end": "destinationPortEnd",
        "destination_port_start": "destinationPortStart",
        "family": "family",
        "icmp_type": "icmpType",
        "protocol": "protocol",
        "source_address_end": "sourceAddressEnd",
        "source_address_start": "sourceAddressStart",
        "source_port_end": "sourcePortEnd",
        "source_port_start": "sourcePortStart",
    },
)
class FirewallRulesFirewallRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        direction: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        destination_address_end: typing.Optional[builtins.str] = None,
        destination_address_start: typing.Optional[builtins.str] = None,
        destination_port_end: typing.Optional[builtins.str] = None,
        destination_port_start: typing.Optional[builtins.str] = None,
        family: typing.Optional[builtins.str] = None,
        icmp_type: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        source_address_end: typing.Optional[builtins.str] = None,
        source_address_start: typing.Optional[builtins.str] = None,
        source_port_end: typing.Optional[builtins.str] = None,
        source_port_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to take if the rule conditions are met. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#action FirewallRules#action}
        :param direction: The direction of network traffic this rule will be applied to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#direction FirewallRules#direction}
        :param comment: Freeform comment string for the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#comment FirewallRules#comment}
        :param destination_address_end: The destination address range ends from this address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_address_end FirewallRules#destination_address_end}
        :param destination_address_start: The destination address range starts from this address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_address_start FirewallRules#destination_address_start}
        :param destination_port_end: The destination port range ends from this port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_port_end FirewallRules#destination_port_end}
        :param destination_port_start: The destination port range starts from this port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_port_start FirewallRules#destination_port_start}
        :param family: The address family of new firewall rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#family FirewallRules#family}
        :param icmp_type: The ICMP type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#icmp_type FirewallRules#icmp_type}
        :param protocol: The protocol this rule will be applied to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#protocol FirewallRules#protocol}
        :param source_address_end: The source address range ends from this address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_address_end FirewallRules#source_address_end}
        :param source_address_start: The source address range starts from this address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_address_start FirewallRules#source_address_start}
        :param source_port_end: The source port range ends from this port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_port_end FirewallRules#source_port_end}
        :param source_port_start: The source port range starts from this port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_port_start FirewallRules#source_port_start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallRulesFirewallRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument destination_address_end", value=destination_address_end, expected_type=type_hints["destination_address_end"])
            check_type(argname="argument destination_address_start", value=destination_address_start, expected_type=type_hints["destination_address_start"])
            check_type(argname="argument destination_port_end", value=destination_port_end, expected_type=type_hints["destination_port_end"])
            check_type(argname="argument destination_port_start", value=destination_port_start, expected_type=type_hints["destination_port_start"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument source_address_end", value=source_address_end, expected_type=type_hints["source_address_end"])
            check_type(argname="argument source_address_start", value=source_address_start, expected_type=type_hints["source_address_start"])
            check_type(argname="argument source_port_end", value=source_port_end, expected_type=type_hints["source_port_end"])
            check_type(argname="argument source_port_start", value=source_port_start, expected_type=type_hints["source_port_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "direction": direction,
        }
        if comment is not None:
            self._values["comment"] = comment
        if destination_address_end is not None:
            self._values["destination_address_end"] = destination_address_end
        if destination_address_start is not None:
            self._values["destination_address_start"] = destination_address_start
        if destination_port_end is not None:
            self._values["destination_port_end"] = destination_port_end
        if destination_port_start is not None:
            self._values["destination_port_start"] = destination_port_start
        if family is not None:
            self._values["family"] = family
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if protocol is not None:
            self._values["protocol"] = protocol
        if source_address_end is not None:
            self._values["source_address_end"] = source_address_end
        if source_address_start is not None:
            self._values["source_address_start"] = source_address_start
        if source_port_end is not None:
            self._values["source_port_end"] = source_port_end
        if source_port_start is not None:
            self._values["source_port_start"] = source_port_start

    @builtins.property
    def action(self) -> builtins.str:
        '''Action to take if the rule conditions are met.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#action FirewallRules#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> builtins.str:
        '''The direction of network traffic this rule will be applied to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#direction FirewallRules#direction}
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Freeform comment string for the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#comment FirewallRules#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_end(self) -> typing.Optional[builtins.str]:
        '''The destination address range ends from this address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_address_end FirewallRules#destination_address_end}
        '''
        result = self._values.get("destination_address_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_start(self) -> typing.Optional[builtins.str]:
        '''The destination address range starts from this address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_address_start FirewallRules#destination_address_start}
        '''
        result = self._values.get("destination_address_start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_port_end(self) -> typing.Optional[builtins.str]:
        '''The destination port range ends from this port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_port_end FirewallRules#destination_port_end}
        '''
        result = self._values.get("destination_port_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_port_start(self) -> typing.Optional[builtins.str]:
        '''The destination port range starts from this port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#destination_port_start FirewallRules#destination_port_start}
        '''
        result = self._values.get("destination_port_start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''The address family of new firewall rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#family FirewallRules#family}
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[builtins.str]:
        '''The ICMP type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#icmp_type FirewallRules#icmp_type}
        '''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol this rule will be applied to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#protocol FirewallRules#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_end(self) -> typing.Optional[builtins.str]:
        '''The source address range ends from this address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_address_end FirewallRules#source_address_end}
        '''
        result = self._values.get("source_address_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_start(self) -> typing.Optional[builtins.str]:
        '''The source address range starts from this address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_address_start FirewallRules#source_address_start}
        '''
        result = self._values.get("source_address_start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_port_end(self) -> typing.Optional[builtins.str]:
        '''The source port range ends from this port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_port_end FirewallRules#source_port_end}
        '''
        result = self._values.get("source_port_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_port_start(self) -> typing.Optional[builtins.str]:
        '''The source port range starts from this port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/firewall_rules#source_port_start FirewallRules#source_port_start}
        '''
        result = self._values.get("source_port_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRulesFirewallRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallRulesFirewallRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.firewallRules.FirewallRulesFirewallRuleList",
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
            type_hints = typing.get_type_hints(FirewallRulesFirewallRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FirewallRulesFirewallRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallRulesFirewallRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallRulesFirewallRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[typing.List[FirewallRulesFirewallRule], cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[typing.List[FirewallRulesFirewallRule], cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[typing.List[FirewallRulesFirewallRule], cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallRulesFirewallRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.firewallRules.FirewallRulesFirewallRuleOutputReference",
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
            type_hints = typing.get_type_hints(FirewallRulesFirewallRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDestinationAddressEnd")
    def reset_destination_address_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressEnd", []))

    @jsii.member(jsii_name="resetDestinationAddressStart")
    def reset_destination_address_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressStart", []))

    @jsii.member(jsii_name="resetDestinationPortEnd")
    def reset_destination_port_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortEnd", []))

    @jsii.member(jsii_name="resetDestinationPortStart")
    def reset_destination_port_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortStart", []))

    @jsii.member(jsii_name="resetFamily")
    def reset_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFamily", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetSourceAddressEnd")
    def reset_source_address_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressEnd", []))

    @jsii.member(jsii_name="resetSourceAddressStart")
    def reset_source_address_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressStart", []))

    @jsii.member(jsii_name="resetSourcePortEnd")
    def reset_source_port_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortEnd", []))

    @jsii.member(jsii_name="resetSourcePortStart")
    def reset_source_port_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortStart", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressEndInput")
    def destination_address_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationAddressEndInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressStartInput")
    def destination_address_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationAddressStartInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortEndInput")
    def destination_port_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPortEndInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortStartInput")
    def destination_port_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPortStartInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressEndInput")
    def source_address_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAddressEndInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressStartInput")
    def source_address_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAddressStartInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortEndInput")
    def source_port_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePortEndInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortStartInput")
    def source_port_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePortStartInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressEnd")
    def destination_address_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationAddressEnd"))

    @destination_address_end.setter
    def destination_address_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "destination_address_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressEnd", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressStart")
    def destination_address_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationAddressStart"))

    @destination_address_start.setter
    def destination_address_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "destination_address_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressStart", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortEnd")
    def destination_port_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPortEnd"))

    @destination_port_end.setter
    def destination_port_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "destination_port_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortEnd", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortStart")
    def destination_port_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPortStart"))

    @destination_port_start.setter
    def destination_port_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "destination_port_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortStart", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "icmp_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressEnd")
    def source_address_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAddressEnd"))

    @source_address_end.setter
    def source_address_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "source_address_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressEnd", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressStart")
    def source_address_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAddressStart"))

    @source_address_start.setter
    def source_address_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "source_address_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressStart", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortEnd")
    def source_port_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePortEnd"))

    @source_port_end.setter
    def source_port_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "source_port_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortEnd", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortStart")
    def source_port_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePortStart"))

    @source_port_start.setter
    def source_port_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "source_port_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortStart", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallRulesFirewallRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallRulesFirewallRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallRulesFirewallRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallRulesFirewallRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FirewallRules",
    "FirewallRulesConfig",
    "FirewallRulesFirewallRule",
    "FirewallRulesFirewallRuleList",
    "FirewallRulesFirewallRuleOutputReference",
]

publication.publish()
