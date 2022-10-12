'''
# `vault_rabbitmq_secret_backend_role`

Refer to the Terraform Registory for docs: [`vault_rabbitmq_secret_backend_role`](https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role).
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


class RabbitmqSecretBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role vault_rabbitmq_secret_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
        vhost: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhost", typing.Dict[str, typing.Any]]]]] = None,
        vhost_topic: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhostTopic", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role vault_rabbitmq_secret_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: The path of the Rabbitmq Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#backend RabbitmqSecretBackendRole#backend}
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#name RabbitmqSecretBackendRole#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#id RabbitmqSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#namespace RabbitmqSecretBackendRole#namespace}
        :param tags: Specifies a comma-separated RabbitMQ management tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#tags RabbitmqSecretBackendRole#tags}
        :param vhost: vhost block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost RabbitmqSecretBackendRole#vhost}
        :param vhost_topic: vhost_topic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost_topic RabbitmqSecretBackendRole#vhost_topic}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RabbitmqSecretBackendRoleConfig(
            backend=backend,
            name=name,
            id=id,
            namespace=namespace,
            tags=tags,
            vhost=vhost,
            vhost_topic=vhost_topic,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVhost")
    def put_vhost(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhost", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRole.put_vhost)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVhost", [value]))

    @jsii.member(jsii_name="putVhostTopic")
    def put_vhost_topic(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhostTopic", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRole.put_vhost_topic)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVhostTopic", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetVhost")
    def reset_vhost(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhost", []))

    @jsii.member(jsii_name="resetVhostTopic")
    def reset_vhost_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhostTopic", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="vhost")
    def vhost(self) -> "RabbitmqSecretBackendRoleVhostList":
        return typing.cast("RabbitmqSecretBackendRoleVhostList", jsii.get(self, "vhost"))

    @builtins.property
    @jsii.member(jsii_name="vhostTopic")
    def vhost_topic(self) -> "RabbitmqSecretBackendRoleVhostTopicList":
        return typing.cast("RabbitmqSecretBackendRoleVhostTopicList", jsii.get(self, "vhostTopic"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

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
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="vhostInput")
    def vhost_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhost"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhost"]]], jsii.get(self, "vhostInput"))

    @builtins.property
    @jsii.member(jsii_name="vhostTopicInput")
    def vhost_topic_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopic"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopic"]]], jsii.get(self, "vhostTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRole, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRole, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRole, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "name": "name",
        "id": "id",
        "namespace": "namespace",
        "tags": "tags",
        "vhost": "vhost",
        "vhost_topic": "vhostTopic",
    },
)
class RabbitmqSecretBackendRoleConfig(cdktf.TerraformMetaArguments):
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
        backend: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
        vhost: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhost", typing.Dict[str, typing.Any]]]]] = None,
        vhost_topic: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhostTopic", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: The path of the Rabbitmq Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#backend RabbitmqSecretBackendRole#backend}
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#name RabbitmqSecretBackendRole#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#id RabbitmqSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#namespace RabbitmqSecretBackendRole#namespace}
        :param tags: Specifies a comma-separated RabbitMQ management tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#tags RabbitmqSecretBackendRole#tags}
        :param vhost: vhost block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost RabbitmqSecretBackendRole#vhost}
        :param vhost_topic: vhost_topic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost_topic RabbitmqSecretBackendRole#vhost_topic}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vhost", value=vhost, expected_type=type_hints["vhost"])
            check_type(argname="argument vhost_topic", value=vhost_topic, expected_type=type_hints["vhost_topic"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
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
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if tags is not None:
            self._values["tags"] = tags
        if vhost is not None:
            self._values["vhost"] = vhost
        if vhost_topic is not None:
            self._values["vhost_topic"] = vhost_topic

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
    def backend(self) -> builtins.str:
        '''The path of the Rabbitmq Secret Backend the role belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#backend RabbitmqSecretBackendRole#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#name RabbitmqSecretBackendRole#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#id RabbitmqSecretBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#namespace RabbitmqSecretBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[builtins.str]:
        '''Specifies a comma-separated RabbitMQ management tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#tags RabbitmqSecretBackendRole#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vhost(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhost"]]]:
        '''vhost block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost RabbitmqSecretBackendRole#vhost}
        '''
        result = self._values.get("vhost")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhost"]]], result)

    @builtins.property
    def vhost_topic(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopic"]]]:
        '''vhost_topic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost_topic RabbitmqSecretBackendRole#vhost_topic}
        '''
        result = self._values.get("vhost_topic")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopic"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RabbitmqSecretBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhost",
    jsii_struct_bases=[],
    name_mapping={
        "configure": "configure",
        "host": "host",
        "read": "read",
        "write": "write",
    },
)
class RabbitmqSecretBackendRoleVhost:
    def __init__(
        self,
        *,
        configure: builtins.str,
        host: builtins.str,
        read: builtins.str,
        write: builtins.str,
    ) -> None:
        '''
        :param configure: The configure permissions for this vhost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#configure RabbitmqSecretBackendRole#configure}
        :param host: The vhost to set permissions for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#host RabbitmqSecretBackendRole#host}
        :param read: The read permissions for this vhost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#read RabbitmqSecretBackendRole#read}
        :param write: The write permissions for this vhost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#write RabbitmqSecretBackendRole#write}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhost.__init__)
            check_type(argname="argument configure", value=configure, expected_type=type_hints["configure"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
        self._values: typing.Dict[str, typing.Any] = {
            "configure": configure,
            "host": host,
            "read": read,
            "write": write,
        }

    @builtins.property
    def configure(self) -> builtins.str:
        '''The configure permissions for this vhost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#configure RabbitmqSecretBackendRole#configure}
        '''
        result = self._values.get("configure")
        assert result is not None, "Required property 'configure' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''The vhost to set permissions for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#host RabbitmqSecretBackendRole#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read(self) -> builtins.str:
        '''The read permissions for this vhost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#read RabbitmqSecretBackendRole#read}
        '''
        result = self._values.get("read")
        assert result is not None, "Required property 'read' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def write(self) -> builtins.str:
        '''The write permissions for this vhost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#write RabbitmqSecretBackendRole#write}
        '''
        result = self._values.get("write")
        assert result is not None, "Required property 'write' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RabbitmqSecretBackendRoleVhost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RabbitmqSecretBackendRoleVhostList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostList",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RabbitmqSecretBackendRoleVhostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RabbitmqSecretBackendRoleVhostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RabbitmqSecretBackendRoleVhostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostOutputReference",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="configureInput")
    def configure_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configureInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="writeInput")
    def write_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeInput"))

    @builtins.property
    @jsii.member(jsii_name="configure")
    def configure(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configure"))

    @configure.setter
    def configure(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostOutputReference, "configure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configure", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="write")
    def write(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "write"))

    @write.setter
    def write(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostOutputReference, "write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "write", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhost, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhost, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhost, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopic",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "vhost": "vhost"},
)
class RabbitmqSecretBackendRoleVhostTopic:
    def __init__(
        self,
        *,
        host: builtins.str,
        vhost: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhostTopicVhost", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param host: The vhost to set permissions for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#host RabbitmqSecretBackendRole#host}
        :param vhost: vhost block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost RabbitmqSecretBackendRole#vhost}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopic.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument vhost", value=vhost, expected_type=type_hints["vhost"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
        }
        if vhost is not None:
            self._values["vhost"] = vhost

    @builtins.property
    def host(self) -> builtins.str:
        '''The vhost to set permissions for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#host RabbitmqSecretBackendRole#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vhost(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopicVhost"]]]:
        '''vhost block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#vhost RabbitmqSecretBackendRole#vhost}
        '''
        result = self._values.get("vhost")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopicVhost"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RabbitmqSecretBackendRoleVhostTopic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RabbitmqSecretBackendRoleVhostTopicList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopicList",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RabbitmqSecretBackendRoleVhostTopicOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RabbitmqSecretBackendRoleVhostTopicOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopic]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopic]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopic]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RabbitmqSecretBackendRoleVhostTopicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopicOutputReference",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVhost")
    def put_vhost(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RabbitmqSecretBackendRoleVhostTopicVhost", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicOutputReference.put_vhost)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVhost", [value]))

    @jsii.member(jsii_name="resetVhost")
    def reset_vhost(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhost", []))

    @builtins.property
    @jsii.member(jsii_name="vhost")
    def vhost(self) -> "RabbitmqSecretBackendRoleVhostTopicVhostList":
        return typing.cast("RabbitmqSecretBackendRoleVhostTopicVhostList", jsii.get(self, "vhost"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="vhostInput")
    def vhost_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopicVhost"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RabbitmqSecretBackendRoleVhostTopicVhost"]]], jsii.get(self, "vhostInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopic, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopic, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopic, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopicVhost",
    jsii_struct_bases=[],
    name_mapping={"read": "read", "topic": "topic", "write": "write"},
)
class RabbitmqSecretBackendRoleVhostTopicVhost:
    def __init__(
        self,
        *,
        read: builtins.str,
        topic: builtins.str,
        write: builtins.str,
    ) -> None:
        '''
        :param read: The read permissions for this vhost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#read RabbitmqSecretBackendRole#read}
        :param topic: The vhost to set permissions for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#topic RabbitmqSecretBackendRole#topic}
        :param write: The write permissions for this vhost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#write RabbitmqSecretBackendRole#write}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicVhost.__init__)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
        self._values: typing.Dict[str, typing.Any] = {
            "read": read,
            "topic": topic,
            "write": write,
        }

    @builtins.property
    def read(self) -> builtins.str:
        '''The read permissions for this vhost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#read RabbitmqSecretBackendRole#read}
        '''
        result = self._values.get("read")
        assert result is not None, "Required property 'read' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''The vhost to set permissions for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#topic RabbitmqSecretBackendRole#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def write(self) -> builtins.str:
        '''The write permissions for this vhost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/rabbitmq_secret_backend_role#write RabbitmqSecretBackendRole#write}
        '''
        result = self._values.get("write")
        assert result is not None, "Required property 'write' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RabbitmqSecretBackendRoleVhostTopicVhost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RabbitmqSecretBackendRoleVhostTopicVhostList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopicVhostList",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicVhostList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RabbitmqSecretBackendRoleVhostTopicVhostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicVhostList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RabbitmqSecretBackendRoleVhostTopicVhostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopicVhost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopicVhost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RabbitmqSecretBackendRoleVhostTopicVhost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RabbitmqSecretBackendRoleVhostTopicVhostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.rabbitmqSecretBackendRole.RabbitmqSecretBackendRoleVhostTopicVhostOutputReference",
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
            type_hints = typing.get_type_hints(RabbitmqSecretBackendRoleVhostTopicVhostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="writeInput")
    def write_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="write")
    def write(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "write"))

    @write.setter
    def write(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostOutputReference, "write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "write", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopicVhost, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopicVhost, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RabbitmqSecretBackendRoleVhostTopicVhost, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RabbitmqSecretBackendRoleVhostTopicVhostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RabbitmqSecretBackendRole",
    "RabbitmqSecretBackendRoleConfig",
    "RabbitmqSecretBackendRoleVhost",
    "RabbitmqSecretBackendRoleVhostList",
    "RabbitmqSecretBackendRoleVhostOutputReference",
    "RabbitmqSecretBackendRoleVhostTopic",
    "RabbitmqSecretBackendRoleVhostTopicList",
    "RabbitmqSecretBackendRoleVhostTopicOutputReference",
    "RabbitmqSecretBackendRoleVhostTopicVhost",
    "RabbitmqSecretBackendRoleVhostTopicVhostList",
    "RabbitmqSecretBackendRoleVhostTopicVhostOutputReference",
]

publication.publish()
