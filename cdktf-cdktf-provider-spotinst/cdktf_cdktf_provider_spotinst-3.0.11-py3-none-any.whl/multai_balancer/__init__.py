'''
# `spotinst_multai_balancer`

Refer to the Terraform Registory for docs: [`spotinst_multai_balancer`](https://www.terraform.io/docs/providers/spotinst/r/multai_balancer).
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


class MultaiBalancer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer spotinst_multai_balancer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        connection_timeouts: typing.Optional[typing.Union["MultaiBalancerConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        dns_cname_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiBalancerTags", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer spotinst_multai_balancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#name MultaiBalancer#name}.
        :param connection_timeouts: connection_timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#connection_timeouts MultaiBalancer#connection_timeouts}
        :param dns_cname_aliases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#dns_cname_aliases MultaiBalancer#dns_cname_aliases}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#id MultaiBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#scheme MultaiBalancer#scheme}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#tags MultaiBalancer#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MultaiBalancerConfig(
            name=name,
            connection_timeouts=connection_timeouts,
            dns_cname_aliases=dns_cname_aliases,
            id=id,
            scheme=scheme,
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

    @jsii.member(jsii_name="putConnectionTimeouts")
    def put_connection_timeouts(
        self,
        *,
        draining: typing.Optional[jsii.Number] = None,
        idle: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#draining MultaiBalancer#draining}.
        :param idle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#idle MultaiBalancer#idle}.
        '''
        value = MultaiBalancerConnectionTimeouts(draining=draining, idle=idle)

        return typing.cast(None, jsii.invoke(self, "putConnectionTimeouts", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiBalancerTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancer.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetConnectionTimeouts")
    def reset_connection_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionTimeouts", []))

    @jsii.member(jsii_name="resetDnsCnameAliases")
    def reset_dns_cname_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsCnameAliases", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

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
    @jsii.member(jsii_name="connectionTimeouts")
    def connection_timeouts(self) -> "MultaiBalancerConnectionTimeoutsOutputReference":
        return typing.cast("MultaiBalancerConnectionTimeoutsOutputReference", jsii.get(self, "connectionTimeouts"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "MultaiBalancerTagsList":
        return typing.cast("MultaiBalancerTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="connectionTimeoutsInput")
    def connection_timeouts_input(
        self,
    ) -> typing.Optional["MultaiBalancerConnectionTimeouts"]:
        return typing.cast(typing.Optional["MultaiBalancerConnectionTimeouts"], jsii.get(self, "connectionTimeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsCnameAliasesInput")
    def dns_cname_aliases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsCnameAliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiBalancerTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiBalancerTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsCnameAliases")
    def dns_cname_aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsCnameAliases"))

    @dns_cname_aliases.setter
    def dns_cname_aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancer, "dns_cname_aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsCnameAliases", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancer, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "connection_timeouts": "connectionTimeouts",
        "dns_cname_aliases": "dnsCnameAliases",
        "id": "id",
        "scheme": "scheme",
        "tags": "tags",
    },
)
class MultaiBalancerConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        connection_timeouts: typing.Optional[typing.Union["MultaiBalancerConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        dns_cname_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiBalancerTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#name MultaiBalancer#name}.
        :param connection_timeouts: connection_timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#connection_timeouts MultaiBalancer#connection_timeouts}
        :param dns_cname_aliases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#dns_cname_aliases MultaiBalancer#dns_cname_aliases}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#id MultaiBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#scheme MultaiBalancer#scheme}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#tags MultaiBalancer#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connection_timeouts, dict):
            connection_timeouts = MultaiBalancerConnectionTimeouts(**connection_timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument connection_timeouts", value=connection_timeouts, expected_type=type_hints["connection_timeouts"])
            check_type(argname="argument dns_cname_aliases", value=dns_cname_aliases, expected_type=type_hints["dns_cname_aliases"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if connection_timeouts is not None:
            self._values["connection_timeouts"] = connection_timeouts
        if dns_cname_aliases is not None:
            self._values["dns_cname_aliases"] = dns_cname_aliases
        if id is not None:
            self._values["id"] = id
        if scheme is not None:
            self._values["scheme"] = scheme
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#name MultaiBalancer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_timeouts(
        self,
    ) -> typing.Optional["MultaiBalancerConnectionTimeouts"]:
        '''connection_timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#connection_timeouts MultaiBalancer#connection_timeouts}
        '''
        result = self._values.get("connection_timeouts")
        return typing.cast(typing.Optional["MultaiBalancerConnectionTimeouts"], result)

    @builtins.property
    def dns_cname_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#dns_cname_aliases MultaiBalancer#dns_cname_aliases}.'''
        result = self._values.get("dns_cname_aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#id MultaiBalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#scheme MultaiBalancer#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiBalancerTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#tags MultaiBalancer#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiBalancerTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultaiBalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"draining": "draining", "idle": "idle"},
)
class MultaiBalancerConnectionTimeouts:
    def __init__(
        self,
        *,
        draining: typing.Optional[jsii.Number] = None,
        idle: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param draining: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#draining MultaiBalancer#draining}.
        :param idle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#idle MultaiBalancer#idle}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancerConnectionTimeouts.__init__)
            check_type(argname="argument draining", value=draining, expected_type=type_hints["draining"])
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
        self._values: typing.Dict[str, typing.Any] = {}
        if draining is not None:
            self._values["draining"] = draining
        if idle is not None:
            self._values["idle"] = idle

    @builtins.property
    def draining(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#draining MultaiBalancer#draining}.'''
        result = self._values.get("draining")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#idle MultaiBalancer#idle}.'''
        result = self._values.get("idle")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultaiBalancerConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MultaiBalancerConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MultaiBalancerConnectionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDraining")
    def reset_draining(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDraining", []))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @builtins.property
    @jsii.member(jsii_name="drainingInput")
    def draining_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainingInput"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="draining")
    def draining(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "draining"))

    @draining.setter
    def draining(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerConnectionTimeoutsOutputReference, "draining").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "draining", value)

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idle"))

    @idle.setter
    def idle(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerConnectionTimeoutsOutputReference, "idle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idle", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MultaiBalancerConnectionTimeouts]:
        return typing.cast(typing.Optional[MultaiBalancerConnectionTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MultaiBalancerConnectionTimeouts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class MultaiBalancerTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#key MultaiBalancer#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#value MultaiBalancer#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancerTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#key MultaiBalancer#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_balancer#value MultaiBalancer#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultaiBalancerTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MultaiBalancerTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerTagsList",
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
            type_hints = typing.get_type_hints(MultaiBalancerTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MultaiBalancerTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiBalancerTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MultaiBalancerTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiBalancerTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiBalancerTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiBalancerTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MultaiBalancerTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiBalancer.MultaiBalancerTagsOutputReference",
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
            type_hints = typing.get_type_hints(MultaiBalancerTagsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MultaiBalancerTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MultaiBalancerTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MultaiBalancerTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiBalancerTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MultaiBalancer",
    "MultaiBalancerConfig",
    "MultaiBalancerConnectionTimeouts",
    "MultaiBalancerConnectionTimeoutsOutputReference",
    "MultaiBalancerTags",
    "MultaiBalancerTagsList",
    "MultaiBalancerTagsOutputReference",
]

publication.publish()
