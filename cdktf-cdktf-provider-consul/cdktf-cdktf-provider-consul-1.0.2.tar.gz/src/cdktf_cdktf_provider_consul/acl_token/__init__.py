'''
# `consul_acl_token`

Refer to the Terraform Registory for docs: [`consul_acl_token`](https://www.terraform.io/docs/providers/consul/r/acl_token).
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


class AclToken(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclToken.AclToken",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/r/acl_token consul_acl_token}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        accessor_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expiration_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenNodeIdentities", typing.Dict[str, typing.Any]]]]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/r/acl_token consul_acl_token} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param accessor_id: The token id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#accessor_id AclToken#accessor_id}
        :param description: The token description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#description AclToken#description}
        :param expiration_time: If set this represents the point after which a token should be considered revoked and is eligible for destruction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#expiration_time AclToken#expiration_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#id AclToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Flag to set the token local to the current datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#local AclToken#local}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#namespace AclToken#namespace}.
        :param node_identities: node_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#node_identities AclToken#node_identities}
        :param partition: The partition the ACL token is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#partition AclToken#partition}
        :param policies: List of policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#policies AclToken#policies}
        :param roles: List of roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#roles AclToken#roles}
        :param service_identities: service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#service_identities AclToken#service_identities}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclToken.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AclTokenConfig(
            accessor_id=accessor_id,
            description=description,
            expiration_time=expiration_time,
            id=id,
            local=local,
            namespace=namespace,
            node_identities=node_identities,
            partition=partition,
            policies=policies,
            roles=roles,
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenNodeIdentities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclToken.put_node_identities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeIdentities", [value]))

    @jsii.member(jsii_name="putServiceIdentities")
    def put_service_identities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenServiceIdentities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclToken.put_service_identities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServiceIdentities", [value]))

    @jsii.member(jsii_name="resetAccessorId")
    def reset_accessor_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessorId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

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

    @jsii.member(jsii_name="resetRoles")
    def reset_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoles", []))

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
    def node_identities(self) -> "AclTokenNodeIdentitiesList":
        return typing.cast("AclTokenNodeIdentitiesList", jsii.get(self, "nodeIdentities"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdentities")
    def service_identities(self) -> "AclTokenServiceIdentitiesList":
        return typing.cast("AclTokenServiceIdentitiesList", jsii.get(self, "serviceIdentities"))

    @builtins.property
    @jsii.member(jsii_name="accessorIdInput")
    def accessor_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdentitiesInput")
    def node_identities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenNodeIdentities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenNodeIdentities"]]], jsii.get(self, "nodeIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdentitiesInput")
    def service_identities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenServiceIdentities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenServiceIdentities"]]], jsii.get(self, "serviceIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="accessorId")
    def accessor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessorId"))

    @accessor_id.setter
    def accessor_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "accessor_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessorId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "expiration_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclToken, "roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "accessor_id": "accessorId",
        "description": "description",
        "expiration_time": "expirationTime",
        "id": "id",
        "local": "local",
        "namespace": "namespace",
        "node_identities": "nodeIdentities",
        "partition": "partition",
        "policies": "policies",
        "roles": "roles",
        "service_identities": "serviceIdentities",
    },
)
class AclTokenConfig(cdktf.TerraformMetaArguments):
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
        accessor_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expiration_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenNodeIdentities", typing.Dict[str, typing.Any]]]]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AclTokenServiceIdentities", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param accessor_id: The token id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#accessor_id AclToken#accessor_id}
        :param description: The token description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#description AclToken#description}
        :param expiration_time: If set this represents the point after which a token should be considered revoked and is eligible for destruction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#expiration_time AclToken#expiration_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#id AclToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Flag to set the token local to the current datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#local AclToken#local}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#namespace AclToken#namespace}.
        :param node_identities: node_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#node_identities AclToken#node_identities}
        :param partition: The partition the ACL token is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#partition AclToken#partition}
        :param policies: List of policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#policies AclToken#policies}
        :param roles: List of roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#roles AclToken#roles}
        :param service_identities: service_identities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#service_identities AclToken#service_identities}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AclTokenConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument accessor_id", value=accessor_id, expected_type=type_hints["accessor_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument node_identities", value=node_identities, expected_type=type_hints["node_identities"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument service_identities", value=service_identities, expected_type=type_hints["service_identities"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if accessor_id is not None:
            self._values["accessor_id"] = accessor_id
        if description is not None:
            self._values["description"] = description
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if id is not None:
            self._values["id"] = id
        if local is not None:
            self._values["local"] = local
        if namespace is not None:
            self._values["namespace"] = namespace
        if node_identities is not None:
            self._values["node_identities"] = node_identities
        if partition is not None:
            self._values["partition"] = partition
        if policies is not None:
            self._values["policies"] = policies
        if roles is not None:
            self._values["roles"] = roles
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
    def accessor_id(self) -> typing.Optional[builtins.str]:
        '''The token id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#accessor_id AclToken#accessor_id}
        '''
        result = self._values.get("accessor_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The token description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#description AclToken#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[builtins.str]:
        '''If set this represents the point after which a token should be considered revoked and is eligible for destruction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#expiration_time AclToken#expiration_time}
        '''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#id AclToken#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to set the token local to the current datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#local AclToken#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#namespace AclToken#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_identities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenNodeIdentities"]]]:
        '''node_identities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#node_identities AclToken#node_identities}
        '''
        result = self._values.get("node_identities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenNodeIdentities"]]], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''The partition the ACL token is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#partition AclToken#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#policies AclToken#policies}
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of roles.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#roles AclToken#roles}
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_identities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenServiceIdentities"]]]:
        '''service_identities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#service_identities AclToken#service_identities}
        '''
        result = self._values.get("service_identities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AclTokenServiceIdentities"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclTokenConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenNodeIdentities",
    jsii_struct_bases=[],
    name_mapping={"datacenter": "datacenter", "node_name": "nodeName"},
)
class AclTokenNodeIdentities:
    def __init__(self, *, datacenter: builtins.str, node_name: builtins.str) -> None:
        '''
        :param datacenter: Specifies the node's datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#datacenter AclToken#datacenter}
        :param node_name: The name of the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#node_name AclToken#node_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclTokenNodeIdentities.__init__)
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument node_name", value=node_name, expected_type=type_hints["node_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "datacenter": datacenter,
            "node_name": node_name,
        }

    @builtins.property
    def datacenter(self) -> builtins.str:
        '''Specifies the node's datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#datacenter AclToken#datacenter}
        '''
        result = self._values.get("datacenter")
        assert result is not None, "Required property 'datacenter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_name(self) -> builtins.str:
        '''The name of the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#node_name AclToken#node_name}
        '''
        result = self._values.get("node_name")
        assert result is not None, "Required property 'node_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclTokenNodeIdentities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AclTokenNodeIdentitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenNodeIdentitiesList",
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
            type_hints = typing.get_type_hints(AclTokenNodeIdentitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AclTokenNodeIdentitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclTokenNodeIdentitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AclTokenNodeIdentitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenNodeIdentities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenNodeIdentities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenNodeIdentities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AclTokenNodeIdentitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenNodeIdentitiesOutputReference",
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
            type_hints = typing.get_type_hints(AclTokenNodeIdentitiesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesOutputReference, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="nodeName")
    def node_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeName"))

    @node_name.setter
    def node_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesOutputReference, "node_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AclTokenNodeIdentities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AclTokenNodeIdentities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AclTokenNodeIdentities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenNodeIdentitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenServiceIdentities",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "datacenters": "datacenters"},
)
class AclTokenServiceIdentities:
    def __init__(
        self,
        *,
        service_name: builtins.str,
        datacenters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param service_name: The name of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#service_name AclToken#service_name}
        :param datacenters: Specifies the datacenters the effective policy is valid within. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#datacenters AclToken#datacenters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclTokenServiceIdentities.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#service_name AclToken#service_name}
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datacenters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the datacenters the effective policy is valid within.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/acl_token#datacenters AclToken#datacenters}
        '''
        result = self._values.get("datacenters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AclTokenServiceIdentities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AclTokenServiceIdentitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenServiceIdentitiesList",
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
            type_hints = typing.get_type_hints(AclTokenServiceIdentitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AclTokenServiceIdentitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AclTokenServiceIdentitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AclTokenServiceIdentitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenServiceIdentities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenServiceIdentities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AclTokenServiceIdentities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AclTokenServiceIdentitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.aclToken.AclTokenServiceIdentitiesOutputReference",
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
            type_hints = typing.get_type_hints(AclTokenServiceIdentitiesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesOutputReference, "datacenters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenters", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AclTokenServiceIdentities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AclTokenServiceIdentities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AclTokenServiceIdentities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AclTokenServiceIdentitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AclToken",
    "AclTokenConfig",
    "AclTokenNodeIdentities",
    "AclTokenNodeIdentitiesList",
    "AclTokenNodeIdentitiesOutputReference",
    "AclTokenServiceIdentities",
    "AclTokenServiceIdentitiesList",
    "AclTokenServiceIdentitiesOutputReference",
]

publication.publish()
