'''
# `consul_acl_role`

Refer to the Terraform Registory for docs: [`consul_acl_role`](https://www.terraform.io/docs/providers/consul/r/acl_role).
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


class AclRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclRole.AclRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/r/acl_role consul_acl_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleNodeIdentities", typing.Dict[str, typing.Any]]]]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/r/acl_role consul_acl_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the ACL role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#name AclRole#name}
        :param description: A free form human readable description of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#description AclRole#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#id AclRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#namespace AclRole#namespace}.
        :param node_identities: node_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#node_identities AclRole#node_identities}
        :param partition: The partition the ACL role is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#partition AclRole#partition}
        :param policies: The list of policies that should be applied to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#policies AclRole#policies}
        :param service_identities: service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#service_identities AclRole#service_identities}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AclRoleConfig(
            name=name,
            description=description,
            id=id,
            namespace=namespace,
            node_identities=node_identities,
            partition=partition,
            policies=policies,
            service_identities=service_identities,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putNodeIdentities")
    def put_node_identities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleNodeIdentities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRole.put_node_identities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeIdentities", [value]))

    @jsii.member(jsii_name="putServiceIdentities")
    def put_service_identities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleServiceIdentities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRole.put_service_identities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServiceIdentities", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetNodeIdentities")
    def reset_node_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeIdentities", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @jsii.member(jsii_name="resetServiceIdentities")
    def reset_service_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceIdentities", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdentities")
    def node_identities(self) -> "AclRoleNodeIdentitiesList":
        return typing.cast("AclRoleNodeIdentitiesList", jsii.get(self, "nodeIdentities"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdentities")
    def service_identities(self) -> "AclRoleServiceIdentitiesList":
        return typing.cast("AclRoleServiceIdentitiesList", jsii.get(self, "serviceIdentities"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdentitiesInput")
    def node_identities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleNodeIdentities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleNodeIdentities"]]], jsii.get(self, "nodeIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdentitiesInput")
    def service_identities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleServiceIdentities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleServiceIdentities"]]], jsii.get(self, "serviceIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRole, "policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleConfig",
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
        "description": "description",
        "id": "id",
        "namespace": "namespace",
        "node_identities": "nodeIdentities",
        "partition": "partition",
        "policies": "policies",
        "service_identities": "serviceIdentities",
    },
)
class AclRoleConfig(cdktf.TerraformMetaArguments):
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
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleNodeIdentities", typing.Dict[str, typing.Any]]]]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclRoleServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the ACL role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#name AclRole#name}
        :param description: A free form human readable description of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#description AclRole#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#id AclRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#namespace AclRole#namespace}.
        :param node_identities: node_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#node_identities AclRole#node_identities}
        :param partition: The partition the ACL role is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#partition AclRole#partition}
        :param policies: The list of policies that should be applied to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#policies AclRole#policies}
        :param service_identities: service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#service_identities AclRole#service_identities}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AclRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument node_identities", value=node_identities, expected_type=type_hints["node_identities"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument service_identities", value=service_identities, expected_type=type_hints["service_identities"])
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if node_identities is not None:
            self._values["node_identities"] = node_identities
        if partition is not None:
            self._values["partition"] = partition
        if policies is not None:
            self._values["policies"] = policies
        if service_identities is not None:
            self._values["service_identities"] = service_identities

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
        '''The name of the ACL role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#name AclRole#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A free form human readable description of the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#description AclRole#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#id AclRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#namespace AclRole#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_identities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleNodeIdentities"]]]:
        '''node_identities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#node_identities AclRole#node_identities}
        '''
        result = self._values.get("node_identities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleNodeIdentities"]]], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''The partition the ACL role is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#partition AclRole#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of policies that should be applied to the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#policies AclRole#policies}
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_identities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleServiceIdentities"]]]:
        '''service_identities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#service_identities AclRole#service_identities}
        '''
        result = self._values.get("service_identities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclRoleServiceIdentities"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleNodeIdentities",
    jsii_struct_bases=[],
    name_mapping={"datacenter": "datacenter", "node_name": "nodeName"},
)
class AclRoleNodeIdentities:
    def __init__(self, *, datacenter: builtins.str, node_name: builtins.str) -> None:
        '''
        :param datacenter: Specifies the node's datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#datacenter AclRole#datacenter}
        :param node_name: The name of the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#node_name AclRole#node_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRoleNodeIdentities.__init__)
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument node_name", value=node_name, expected_type=type_hints["node_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "datacenter": datacenter,
            "node_name": node_name,
        }

    @builtins.property
    def datacenter(self) -> builtins.str:
        '''Specifies the node's datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#datacenter AclRole#datacenter}
        '''
        result = self._values.get("datacenter")
        assert result is not None, "Required property 'datacenter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_name(self) -> builtins.str:
        '''The name of the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#node_name AclRole#node_name}
        '''
        result = self._values.get("node_name")
        assert result is not None, "Required property 'node_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclRoleNodeIdentities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AclRoleNodeIdentitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleNodeIdentitiesList",
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
            type_hints = typing.get_type_hints(AclRoleNodeIdentitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AclRoleNodeIdentitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRoleNodeIdentitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AclRoleNodeIdentitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleNodeIdentities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleNodeIdentities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleNodeIdentities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AclRoleNodeIdentitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleNodeIdentitiesOutputReference",
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
            type_hints = typing.get_type_hints(AclRoleNodeIdentitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeNameInput")
    def node_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesOutputReference, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="nodeName")
    def node_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeName"))

    @node_name.setter
    def node_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesOutputReference, "node_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AclRoleNodeIdentities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AclRoleNodeIdentities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AclRoleNodeIdentities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleNodeIdentitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleServiceIdentities",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "datacenters": "datacenters"},
)
class AclRoleServiceIdentities:
    def __init__(
        self,
        *,
        service_name: builtins.str,
        datacenters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param service_name: The name of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#service_name AclRole#service_name}
        :param datacenters: The datacenters the effective policy is valid within. When no datacenters are provided the effective policy is valid in all datacenters including those which do not yet exist but may in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#datacenters AclRole#datacenters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRoleServiceIdentities.__init__)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument datacenters", value=datacenters, expected_type=type_hints["datacenters"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_name": service_name,
        }
        if datacenters is not None:
            self._values["datacenters"] = datacenters

    @builtins.property
    def service_name(self) -> builtins.str:
        '''The name of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#service_name AclRole#service_name}
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datacenters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The datacenters the effective policy is valid within.

        When no datacenters are provided the effective policy is valid in all datacenters including those which do not yet exist but may in the future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_role#datacenters AclRole#datacenters}
        '''
        result = self._values.get("datacenters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclRoleServiceIdentities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AclRoleServiceIdentitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleServiceIdentitiesList",
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
            type_hints = typing.get_type_hints(AclRoleServiceIdentitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AclRoleServiceIdentitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclRoleServiceIdentitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AclRoleServiceIdentitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleServiceIdentities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleServiceIdentities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclRoleServiceIdentities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AclRoleServiceIdentitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclRole.AclRoleServiceIdentitiesOutputReference",
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
            type_hints = typing.get_type_hints(AclRoleServiceIdentitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatacenters")
    def reset_datacenters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenters", []))

    @builtins.property
    @jsii.member(jsii_name="datacentersInput")
    def datacenters_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "datacentersInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenters")
    def datacenters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "datacenters"))

    @datacenters.setter
    def datacenters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesOutputReference, "datacenters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenters", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AclRoleServiceIdentities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AclRoleServiceIdentities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AclRoleServiceIdentities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclRoleServiceIdentitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AclRole",
    "AclRoleConfig",
    "AclRoleNodeIdentities",
    "AclRoleNodeIdentitiesList",
    "AclRoleNodeIdentitiesOutputReference",
    "AclRoleServiceIdentities",
    "AclRoleServiceIdentitiesList",
    "AclRoleServiceIdentitiesOutputReference",
]

publication.publish()
