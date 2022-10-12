'''
# `vault_kv_secret_backend_v2`

Refer to the Terraform Registory for docs: [`vault_kv_secret_backend_v2`](https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2).
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


class KvSecretBackendV2(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.kvSecretBackendV2.KvSecretBackendV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2 vault_kv_secret_backend_v2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mount: builtins.str,
        cas_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        delete_version_after: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_versions: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2 vault_kv_secret_backend_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mount: Path where KV-V2 engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#mount KvSecretBackendV2#mount}
        :param cas_required: If true, all keys will require the cas parameter to be set on all write requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#cas_required KvSecretBackendV2#cas_required}
        :param delete_version_after: If set, specifies the length of time before a version is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#delete_version_after KvSecretBackendV2#delete_version_after}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#id KvSecretBackendV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_versions: The number of versions to keep per key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#max_versions KvSecretBackendV2#max_versions}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#namespace KvSecretBackendV2#namespace}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KvSecretBackendV2.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KvSecretBackendV2Config(
            mount=mount,
            cas_required=cas_required,
            delete_version_after=delete_version_after,
            id=id,
            max_versions=max_versions,
            namespace=namespace,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCasRequired")
    def reset_cas_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCasRequired", []))

    @jsii.member(jsii_name="resetDeleteVersionAfter")
    def reset_delete_version_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteVersionAfter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxVersions")
    def reset_max_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxVersions", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="casRequiredInput")
    def cas_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "casRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteVersionAfterInput")
    def delete_version_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteVersionAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxVersionsInput")
    def max_versions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="mountInput")
    def mount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="casRequired")
    def cas_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "casRequired"))

    @cas_required.setter
    def cas_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "cas_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "casRequired", value)

    @builtins.property
    @jsii.member(jsii_name="deleteVersionAfter")
    def delete_version_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteVersionAfter"))

    @delete_version_after.setter
    def delete_version_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "delete_version_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteVersionAfter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxVersions")
    def max_versions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVersions"))

    @max_versions.setter
    def max_versions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "max_versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVersions", value)

    @builtins.property
    @jsii.member(jsii_name="mount")
    def mount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mount"))

    @mount.setter
    def mount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "mount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mount", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KvSecretBackendV2, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.kvSecretBackendV2.KvSecretBackendV2Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mount": "mount",
        "cas_required": "casRequired",
        "delete_version_after": "deleteVersionAfter",
        "id": "id",
        "max_versions": "maxVersions",
        "namespace": "namespace",
    },
)
class KvSecretBackendV2Config(cdktf.TerraformMetaArguments):
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
        mount: builtins.str,
        cas_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        delete_version_after: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_versions: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mount: Path where KV-V2 engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#mount KvSecretBackendV2#mount}
        :param cas_required: If true, all keys will require the cas parameter to be set on all write requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#cas_required KvSecretBackendV2#cas_required}
        :param delete_version_after: If set, specifies the length of time before a version is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#delete_version_after KvSecretBackendV2#delete_version_after}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#id KvSecretBackendV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_versions: The number of versions to keep per key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#max_versions KvSecretBackendV2#max_versions}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#namespace KvSecretBackendV2#namespace}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(KvSecretBackendV2Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mount", value=mount, expected_type=type_hints["mount"])
            check_type(argname="argument cas_required", value=cas_required, expected_type=type_hints["cas_required"])
            check_type(argname="argument delete_version_after", value=delete_version_after, expected_type=type_hints["delete_version_after"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_versions", value=max_versions, expected_type=type_hints["max_versions"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "mount": mount,
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
        if cas_required is not None:
            self._values["cas_required"] = cas_required
        if delete_version_after is not None:
            self._values["delete_version_after"] = delete_version_after
        if id is not None:
            self._values["id"] = id
        if max_versions is not None:
            self._values["max_versions"] = max_versions
        if namespace is not None:
            self._values["namespace"] = namespace

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
    def mount(self) -> builtins.str:
        '''Path where KV-V2 engine is mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#mount KvSecretBackendV2#mount}
        '''
        result = self._values.get("mount")
        assert result is not None, "Required property 'mount' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cas_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, all keys will require the cas parameter to be set on all write requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#cas_required KvSecretBackendV2#cas_required}
        '''
        result = self._values.get("cas_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def delete_version_after(self) -> typing.Optional[jsii.Number]:
        '''If set, specifies the length of time before a version is deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#delete_version_after KvSecretBackendV2#delete_version_after}
        '''
        result = self._values.get("delete_version_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#id KvSecretBackendV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_versions(self) -> typing.Optional[jsii.Number]:
        '''The number of versions to keep per key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#max_versions KvSecretBackendV2#max_versions}
        '''
        result = self._values.get("max_versions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kv_secret_backend_v2#namespace KvSecretBackendV2#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KvSecretBackendV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KvSecretBackendV2",
    "KvSecretBackendV2Config",
]

publication.publish()
