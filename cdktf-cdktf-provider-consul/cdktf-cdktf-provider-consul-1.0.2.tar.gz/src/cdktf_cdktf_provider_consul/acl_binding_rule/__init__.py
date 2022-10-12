'''
# `consul_acl_binding_rule`

Refer to the Terraform Registory for docs: [`consul_acl_binding_rule`](https://www.terraform.io/docs/providers/consul/r/acl_binding_rule).
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


class AclBindingRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclBindingRule.AclBindingRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule consul_acl_binding_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        auth_method: builtins.str,
        bind_name: builtins.str,
        bind_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
        selector: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule consul_acl_binding_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_method: The name of the ACL auth method this rule apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#auth_method AclBindingRule#auth_method}
        :param bind_name: The name to bind to a token at login-time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_name AclBindingRule#bind_name}
        :param bind_type: Specifies the way the binding rule affects a token created at login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_type AclBindingRule#bind_type}
        :param description: A free form human readable description of the binding rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#description AclBindingRule#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#id AclBindingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#namespace AclBindingRule#namespace}.
        :param partition: The partition the ACL binding rule is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#partition AclBindingRule#partition}
        :param selector: The expression used to math this rule against valid identities returned from an auth method validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#selector AclBindingRule#selector}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclBindingRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AclBindingRuleConfig(
            auth_method=auth_method,
            bind_name=bind_name,
            bind_type=bind_type,
            description=description,
            id=id,
            namespace=namespace,
            partition=partition,
            selector=selector,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="bindNameInput")
    def bind_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bindNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bindTypeInput")
    def bind_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bindTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="bindName")
    def bind_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindName"))

    @bind_name.setter
    def bind_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "bind_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bindName", value)

    @builtins.property
    @jsii.member(jsii_name="bindType")
    def bind_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindType"))

    @bind_type.setter
    def bind_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "bind_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bindType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclBindingRule, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclBindingRule.AclBindingRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_method": "authMethod",
        "bind_name": "bindName",
        "bind_type": "bindType",
        "description": "description",
        "id": "id",
        "namespace": "namespace",
        "partition": "partition",
        "selector": "selector",
    },
)
class AclBindingRuleConfig(cdktf.TerraformMetaArguments):
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
        auth_method: builtins.str,
        bind_name: builtins.str,
        bind_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
        selector: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auth_method: The name of the ACL auth method this rule apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#auth_method AclBindingRule#auth_method}
        :param bind_name: The name to bind to a token at login-time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_name AclBindingRule#bind_name}
        :param bind_type: Specifies the way the binding rule affects a token created at login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_type AclBindingRule#bind_type}
        :param description: A free form human readable description of the binding rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#description AclBindingRule#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#id AclBindingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#namespace AclBindingRule#namespace}.
        :param partition: The partition the ACL binding rule is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#partition AclBindingRule#partition}
        :param selector: The expression used to math this rule against valid identities returned from an auth method validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#selector AclBindingRule#selector}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AclBindingRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument bind_name", value=bind_name, expected_type=type_hints["bind_name"])
            check_type(argname="argument bind_type", value=bind_type, expected_type=type_hints["bind_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "auth_method": auth_method,
            "bind_name": bind_name,
            "bind_type": bind_type,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if partition is not None:
            self._values["partition"] = partition
        if selector is not None:
            self._values["selector"] = selector

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
    def auth_method(self) -> builtins.str:
        '''The name of the ACL auth method this rule apply.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#auth_method AclBindingRule#auth_method}
        '''
        result = self._values.get("auth_method")
        assert result is not None, "Required property 'auth_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_name(self) -> builtins.str:
        '''The name to bind to a token at login-time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_name AclBindingRule#bind_name}
        '''
        result = self._values.get("bind_name")
        assert result is not None, "Required property 'bind_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_type(self) -> builtins.str:
        '''Specifies the way the binding rule affects a token created at login.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#bind_type AclBindingRule#bind_type}
        '''
        result = self._values.get("bind_type")
        assert result is not None, "Required property 'bind_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A free form human readable description of the binding rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#description AclBindingRule#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#id AclBindingRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#namespace AclBindingRule#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''The partition the ACL binding rule is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#partition AclBindingRule#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector(self) -> typing.Optional[builtins.str]:
        '''The expression used to math this rule against valid identities returned from an auth method validation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_binding_rule#selector AclBindingRule#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclBindingRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AclBindingRule",
    "AclBindingRuleConfig",
]

publication.publish()
