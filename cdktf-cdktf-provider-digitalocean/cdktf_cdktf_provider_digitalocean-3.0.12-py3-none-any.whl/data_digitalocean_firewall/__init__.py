'''
# `data_digitalocean_firewall`

Refer to the Terraform Registory for docs: [`data_digitalocean_firewall`](https://www.terraform.io/docs/providers/digitalocean/d/firewall).
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


class DataDigitaloceanFirewall(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewall",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall digitalocean_firewall}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        firewall_id: builtins.str,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallInboundRule", typing.Dict[str, typing.Any]]]]] = None,
        outbound_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallOutboundRule", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall digitalocean_firewall} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param firewall_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#firewall_id DataDigitaloceanFirewall#firewall_id}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#droplet_ids DataDigitaloceanFirewall#droplet_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#id DataDigitaloceanFirewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_rule: inbound_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#inbound_rule DataDigitaloceanFirewall#inbound_rule}
        :param outbound_rule: outbound_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#outbound_rule DataDigitaloceanFirewall#outbound_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#tags DataDigitaloceanFirewall#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewall.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDigitaloceanFirewallConfig(
            firewall_id=firewall_id,
            droplet_ids=droplet_ids,
            id=id,
            inbound_rule=inbound_rule,
            outbound_rule=outbound_rule,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInboundRule")
    def put_inbound_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallInboundRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewall.put_inbound_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInboundRule", [value]))

    @jsii.member(jsii_name="putOutboundRule")
    def put_outbound_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallOutboundRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewall.put_outbound_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOutboundRule", [value]))

    @jsii.member(jsii_name="resetDropletIds")
    def reset_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInboundRule")
    def reset_inbound_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundRule", []))

    @jsii.member(jsii_name="resetOutboundRule")
    def reset_outbound_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundRule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="inboundRule")
    def inbound_rule(self) -> "DataDigitaloceanFirewallInboundRuleList":
        return typing.cast("DataDigitaloceanFirewallInboundRuleList", jsii.get(self, "inboundRule"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="outboundRule")
    def outbound_rule(self) -> "DataDigitaloceanFirewallOutboundRuleList":
        return typing.cast("DataDigitaloceanFirewallOutboundRuleList", jsii.get(self, "outboundRule"))

    @builtins.property
    @jsii.member(jsii_name="pendingChanges")
    def pending_changes(self) -> "DataDigitaloceanFirewallPendingChangesList":
        return typing.cast("DataDigitaloceanFirewallPendingChangesList", jsii.get(self, "pendingChanges"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="dropletIdsInput")
    def droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "dropletIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallIdInput")
    def firewall_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundRuleInput")
    def inbound_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallInboundRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallInboundRule"]]], jsii.get(self, "inboundRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundRuleInput")
    def outbound_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallOutboundRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallOutboundRule"]]], jsii.get(self, "outboundRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dropletIds")
    def droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "dropletIds"))

    @droplet_ids.setter
    def droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewall, "droplet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="firewallId")
    def firewall_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallId"))

    @firewall_id.setter
    def firewall_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewall, "firewall_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewall, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewall, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "firewall_id": "firewallId",
        "droplet_ids": "dropletIds",
        "id": "id",
        "inbound_rule": "inboundRule",
        "outbound_rule": "outboundRule",
        "tags": "tags",
    },
)
class DataDigitaloceanFirewallConfig(cdktf.TerraformMetaArguments):
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
        firewall_id: builtins.str,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallInboundRule", typing.Dict[str, typing.Any]]]]] = None,
        outbound_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataDigitaloceanFirewallOutboundRule", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param firewall_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#firewall_id DataDigitaloceanFirewall#firewall_id}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#droplet_ids DataDigitaloceanFirewall#droplet_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#id DataDigitaloceanFirewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_rule: inbound_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#inbound_rule DataDigitaloceanFirewall#inbound_rule}
        :param outbound_rule: outbound_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#outbound_rule DataDigitaloceanFirewall#outbound_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#tags DataDigitaloceanFirewall#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument firewall_id", value=firewall_id, expected_type=type_hints["firewall_id"])
            check_type(argname="argument droplet_ids", value=droplet_ids, expected_type=type_hints["droplet_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inbound_rule", value=inbound_rule, expected_type=type_hints["inbound_rule"])
            check_type(argname="argument outbound_rule", value=outbound_rule, expected_type=type_hints["outbound_rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_id": firewall_id,
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
        if droplet_ids is not None:
            self._values["droplet_ids"] = droplet_ids
        if id is not None:
            self._values["id"] = id
        if inbound_rule is not None:
            self._values["inbound_rule"] = inbound_rule
        if outbound_rule is not None:
            self._values["outbound_rule"] = outbound_rule
        if tags is not None:
            self._values["tags"] = tags

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
    def firewall_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#firewall_id DataDigitaloceanFirewall#firewall_id}.'''
        result = self._values.get("firewall_id")
        assert result is not None, "Required property 'firewall_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#droplet_ids DataDigitaloceanFirewall#droplet_ids}.'''
        result = self._values.get("droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#id DataDigitaloceanFirewall#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inbound_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallInboundRule"]]]:
        '''inbound_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#inbound_rule DataDigitaloceanFirewall#inbound_rule}
        '''
        result = self._values.get("inbound_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallInboundRule"]]], result)

    @builtins.property
    def outbound_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallOutboundRule"]]]:
        '''outbound_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#outbound_rule DataDigitaloceanFirewall#outbound_rule}
        '''
        result = self._values.get("outbound_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataDigitaloceanFirewallOutboundRule"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#tags DataDigitaloceanFirewall#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanFirewallConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallInboundRule",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "port_range": "portRange",
        "source_addresses": "sourceAddresses",
        "source_droplet_ids": "sourceDropletIds",
        "source_kubernetes_ids": "sourceKubernetesIds",
        "source_load_balancer_uids": "sourceLoadBalancerUids",
        "source_tags": "sourceTags",
    },
)
class DataDigitaloceanFirewallInboundRule:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        port_range: typing.Optional[builtins.str] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        source_kubernetes_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_load_balancer_uids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#protocol DataDigitaloceanFirewall#protocol}.
        :param port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#port_range DataDigitaloceanFirewall#port_range}.
        :param source_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_addresses DataDigitaloceanFirewall#source_addresses}.
        :param source_droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_droplet_ids DataDigitaloceanFirewall#source_droplet_ids}.
        :param source_kubernetes_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_kubernetes_ids DataDigitaloceanFirewall#source_kubernetes_ids}.
        :param source_load_balancer_uids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_load_balancer_uids DataDigitaloceanFirewall#source_load_balancer_uids}.
        :param source_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_tags DataDigitaloceanFirewall#source_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallInboundRule.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
            check_type(argname="argument source_addresses", value=source_addresses, expected_type=type_hints["source_addresses"])
            check_type(argname="argument source_droplet_ids", value=source_droplet_ids, expected_type=type_hints["source_droplet_ids"])
            check_type(argname="argument source_kubernetes_ids", value=source_kubernetes_ids, expected_type=type_hints["source_kubernetes_ids"])
            check_type(argname="argument source_load_balancer_uids", value=source_load_balancer_uids, expected_type=type_hints["source_load_balancer_uids"])
            check_type(argname="argument source_tags", value=source_tags, expected_type=type_hints["source_tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if port_range is not None:
            self._values["port_range"] = port_range
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_droplet_ids is not None:
            self._values["source_droplet_ids"] = source_droplet_ids
        if source_kubernetes_ids is not None:
            self._values["source_kubernetes_ids"] = source_kubernetes_ids
        if source_load_balancer_uids is not None:
            self._values["source_load_balancer_uids"] = source_load_balancer_uids
        if source_tags is not None:
            self._values["source_tags"] = source_tags

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#protocol DataDigitaloceanFirewall#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#port_range DataDigitaloceanFirewall#port_range}.'''
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_addresses DataDigitaloceanFirewall#source_addresses}.'''
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_droplet_ids DataDigitaloceanFirewall#source_droplet_ids}.'''
        result = self._values.get("source_droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def source_kubernetes_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_kubernetes_ids DataDigitaloceanFirewall#source_kubernetes_ids}.'''
        result = self._values.get("source_kubernetes_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_load_balancer_uids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_load_balancer_uids DataDigitaloceanFirewall#source_load_balancer_uids}.'''
        result = self._values.get("source_load_balancer_uids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#source_tags DataDigitaloceanFirewall#source_tags}.'''
        result = self._values.get("source_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanFirewallInboundRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanFirewallInboundRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallInboundRuleList",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallInboundRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanFirewallInboundRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallInboundRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDigitaloceanFirewallInboundRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallInboundRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallInboundRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallInboundRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDigitaloceanFirewallInboundRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallInboundRuleOutputReference",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallInboundRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceDropletIds")
    def reset_source_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDropletIds", []))

    @jsii.member(jsii_name="resetSourceKubernetesIds")
    def reset_source_kubernetes_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceKubernetesIds", []))

    @jsii.member(jsii_name="resetSourceLoadBalancerUids")
    def reset_source_load_balancer_uids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceLoadBalancerUids", []))

    @jsii.member(jsii_name="resetSourceTags")
    def reset_source_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceTags", []))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDropletIdsInput")
    def source_droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "sourceDropletIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceKubernetesIdsInput")
    def source_kubernetes_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceKubernetesIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceLoadBalancerUidsInput")
    def source_load_balancer_uids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceLoadBalancerUidsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTagsInput")
    def source_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "source_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDropletIds")
    def source_droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "sourceDropletIds"))

    @source_droplet_ids.setter
    def source_droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "source_droplet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceKubernetesIds")
    def source_kubernetes_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceKubernetesIds"))

    @source_kubernetes_ids.setter
    def source_kubernetes_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "source_kubernetes_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceKubernetesIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceLoadBalancerUids")
    def source_load_balancer_uids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceLoadBalancerUids"))

    @source_load_balancer_uids.setter
    def source_load_balancer_uids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "source_load_balancer_uids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLoadBalancerUids", value)

    @builtins.property
    @jsii.member(jsii_name="sourceTags")
    def source_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceTags"))

    @source_tags.setter
    def source_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "source_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDigitaloceanFirewallInboundRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDigitaloceanFirewallInboundRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDigitaloceanFirewallInboundRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallInboundRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallOutboundRule",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "destination_addresses": "destinationAddresses",
        "destination_droplet_ids": "destinationDropletIds",
        "destination_kubernetes_ids": "destinationKubernetesIds",
        "destination_load_balancer_uids": "destinationLoadBalancerUids",
        "destination_tags": "destinationTags",
        "port_range": "portRange",
    },
)
class DataDigitaloceanFirewallOutboundRule:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        destination_kubernetes_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_load_balancer_uids: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        port_range: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#protocol DataDigitaloceanFirewall#protocol}.
        :param destination_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_addresses DataDigitaloceanFirewall#destination_addresses}.
        :param destination_droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_droplet_ids DataDigitaloceanFirewall#destination_droplet_ids}.
        :param destination_kubernetes_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_kubernetes_ids DataDigitaloceanFirewall#destination_kubernetes_ids}.
        :param destination_load_balancer_uids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_load_balancer_uids DataDigitaloceanFirewall#destination_load_balancer_uids}.
        :param destination_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_tags DataDigitaloceanFirewall#destination_tags}.
        :param port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#port_range DataDigitaloceanFirewall#port_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallOutboundRule.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument destination_addresses", value=destination_addresses, expected_type=type_hints["destination_addresses"])
            check_type(argname="argument destination_droplet_ids", value=destination_droplet_ids, expected_type=type_hints["destination_droplet_ids"])
            check_type(argname="argument destination_kubernetes_ids", value=destination_kubernetes_ids, expected_type=type_hints["destination_kubernetes_ids"])
            check_type(argname="argument destination_load_balancer_uids", value=destination_load_balancer_uids, expected_type=type_hints["destination_load_balancer_uids"])
            check_type(argname="argument destination_tags", value=destination_tags, expected_type=type_hints["destination_tags"])
            check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if destination_addresses is not None:
            self._values["destination_addresses"] = destination_addresses
        if destination_droplet_ids is not None:
            self._values["destination_droplet_ids"] = destination_droplet_ids
        if destination_kubernetes_ids is not None:
            self._values["destination_kubernetes_ids"] = destination_kubernetes_ids
        if destination_load_balancer_uids is not None:
            self._values["destination_load_balancer_uids"] = destination_load_balancer_uids
        if destination_tags is not None:
            self._values["destination_tags"] = destination_tags
        if port_range is not None:
            self._values["port_range"] = port_range

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#protocol DataDigitaloceanFirewall#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_addresses DataDigitaloceanFirewall#destination_addresses}.'''
        result = self._values.get("destination_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_droplet_ids DataDigitaloceanFirewall#destination_droplet_ids}.'''
        result = self._values.get("destination_droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def destination_kubernetes_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_kubernetes_ids DataDigitaloceanFirewall#destination_kubernetes_ids}.'''
        result = self._values.get("destination_kubernetes_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_load_balancer_uids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_load_balancer_uids DataDigitaloceanFirewall#destination_load_balancer_uids}.'''
        result = self._values.get("destination_load_balancer_uids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#destination_tags DataDigitaloceanFirewall#destination_tags}.'''
        result = self._values.get("destination_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/d/firewall#port_range DataDigitaloceanFirewall#port_range}.'''
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanFirewallOutboundRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanFirewallOutboundRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallOutboundRuleList",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallOutboundRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanFirewallOutboundRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallOutboundRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDigitaloceanFirewallOutboundRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallOutboundRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallOutboundRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataDigitaloceanFirewallOutboundRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDigitaloceanFirewallOutboundRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallOutboundRuleOutputReference",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallOutboundRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDestinationAddresses")
    def reset_destination_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddresses", []))

    @jsii.member(jsii_name="resetDestinationDropletIds")
    def reset_destination_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationDropletIds", []))

    @jsii.member(jsii_name="resetDestinationKubernetesIds")
    def reset_destination_kubernetes_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationKubernetesIds", []))

    @jsii.member(jsii_name="resetDestinationLoadBalancerUids")
    def reset_destination_load_balancer_uids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationLoadBalancerUids", []))

    @jsii.member(jsii_name="resetDestinationTags")
    def reset_destination_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationTags", []))

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressesInput")
    def destination_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationDropletIdsInput")
    def destination_droplet_ids_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "destinationDropletIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationKubernetesIdsInput")
    def destination_kubernetes_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationKubernetesIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationLoadBalancerUidsInput")
    def destination_load_balancer_uids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationLoadBalancerUidsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationTagsInput")
    def destination_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @destination_addresses.setter
    def destination_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "destination_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="destinationDropletIds")
    def destination_droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "destinationDropletIds"))

    @destination_droplet_ids.setter
    def destination_droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "destination_droplet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationDropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="destinationKubernetesIds")
    def destination_kubernetes_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationKubernetesIds"))

    @destination_kubernetes_ids.setter
    def destination_kubernetes_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "destination_kubernetes_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationKubernetesIds", value)

    @builtins.property
    @jsii.member(jsii_name="destinationLoadBalancerUids")
    def destination_load_balancer_uids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationLoadBalancerUids"))

    @destination_load_balancer_uids.setter
    def destination_load_balancer_uids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "destination_load_balancer_uids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationLoadBalancerUids", value)

    @builtins.property
    @jsii.member(jsii_name="destinationTags")
    def destination_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationTags"))

    @destination_tags.setter
    def destination_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "destination_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationTags", value)

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDigitaloceanFirewallOutboundRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDigitaloceanFirewallOutboundRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDigitaloceanFirewallOutboundRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallOutboundRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallPendingChanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanFirewallPendingChanges:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanFirewallPendingChanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanFirewallPendingChangesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallPendingChangesList",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallPendingChangesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanFirewallPendingChangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallPendingChangesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDigitaloceanFirewallPendingChangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallPendingChangesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallPendingChangesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallPendingChangesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanFirewallPendingChangesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.dataDigitaloceanFirewall.DataDigitaloceanFirewallPendingChangesOutputReference",
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
            type_hints = typing.get_type_hints(DataDigitaloceanFirewallPendingChangesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dropletId")
    def droplet_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dropletId"))

    @builtins.property
    @jsii.member(jsii_name="removing")
    def removing(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "removing"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDigitaloceanFirewallPendingChanges]:
        return typing.cast(typing.Optional[DataDigitaloceanFirewallPendingChanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanFirewallPendingChanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDigitaloceanFirewallPendingChangesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDigitaloceanFirewall",
    "DataDigitaloceanFirewallConfig",
    "DataDigitaloceanFirewallInboundRule",
    "DataDigitaloceanFirewallInboundRuleList",
    "DataDigitaloceanFirewallInboundRuleOutputReference",
    "DataDigitaloceanFirewallOutboundRule",
    "DataDigitaloceanFirewallOutboundRuleList",
    "DataDigitaloceanFirewallOutboundRuleOutputReference",
    "DataDigitaloceanFirewallPendingChanges",
    "DataDigitaloceanFirewallPendingChangesList",
    "DataDigitaloceanFirewallPendingChangesOutputReference",
]

publication.publish()
