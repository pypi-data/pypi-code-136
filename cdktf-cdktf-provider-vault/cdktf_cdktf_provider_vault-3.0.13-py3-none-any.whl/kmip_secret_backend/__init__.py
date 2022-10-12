'''
# `vault_kmip_secret_backend`

Refer to the Terraform Registory for docs: [`vault_kmip_secret_backend`](https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend).
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


class KmipSecretBackend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.kmipSecretBackend.KmipSecretBackend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend vault_kmip_secret_backend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        path: builtins.str,
        default_tls_client_key_bits: typing.Optional[jsii.Number] = None,
        default_tls_client_key_type: typing.Optional[builtins.str] = None,
        default_tls_client_ttl: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        listen_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        server_hostnames: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls_ca_key_bits: typing.Optional[jsii.Number] = None,
        tls_ca_key_type: typing.Optional[builtins.str] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend vault_kmip_secret_backend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param path: Path where KMIP secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#path KmipSecretBackend#path}
        :param default_tls_client_key_bits: Client certificate key bits, valid values depend on key type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_bits KmipSecretBackend#default_tls_client_key_bits}
        :param default_tls_client_key_type: Client certificate key type, rsa or ec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_type KmipSecretBackend#default_tls_client_key_type}
        :param default_tls_client_ttl: Client certificate TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_ttl KmipSecretBackend#default_tls_client_ttl}
        :param description: Human-friendly description of the mount for the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#description KmipSecretBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#disable_remount KmipSecretBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#id KmipSecretBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param listen_addrs: Addresses the KMIP server should listen on (host:port). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#listen_addrs KmipSecretBackend#listen_addrs}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#namespace KmipSecretBackend#namespace}
        :param server_hostnames: Hostnames to include in the server's TLS certificate as SAN DNS names. The first will be used as the common name (CN) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_hostnames KmipSecretBackend#server_hostnames}
        :param server_ips: IPs to include in the server's TLS certificate as SAN IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_ips KmipSecretBackend#server_ips}
        :param tls_ca_key_bits: CA key bits, valid values depend on key type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_bits KmipSecretBackend#tls_ca_key_bits}
        :param tls_ca_key_type: CA key type, rsa or ec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_type KmipSecretBackend#tls_ca_key_type}
        :param tls_min_version: Minimum TLS version to accept. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_min_version KmipSecretBackend#tls_min_version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KmipSecretBackend.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KmipSecretBackendConfig(
            path=path,
            default_tls_client_key_bits=default_tls_client_key_bits,
            default_tls_client_key_type=default_tls_client_key_type,
            default_tls_client_ttl=default_tls_client_ttl,
            description=description,
            disable_remount=disable_remount,
            id=id,
            listen_addrs=listen_addrs,
            namespace=namespace,
            server_hostnames=server_hostnames,
            server_ips=server_ips,
            tls_ca_key_bits=tls_ca_key_bits,
            tls_ca_key_type=tls_ca_key_type,
            tls_min_version=tls_min_version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultTlsClientKeyBits")
    def reset_default_tls_client_key_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTlsClientKeyBits", []))

    @jsii.member(jsii_name="resetDefaultTlsClientKeyType")
    def reset_default_tls_client_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTlsClientKeyType", []))

    @jsii.member(jsii_name="resetDefaultTlsClientTtl")
    def reset_default_tls_client_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTlsClientTtl", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableRemount")
    def reset_disable_remount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRemount", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetListenAddrs")
    def reset_listen_addrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListenAddrs", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetServerHostnames")
    def reset_server_hostnames(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerHostnames", []))

    @jsii.member(jsii_name="resetServerIps")
    def reset_server_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerIps", []))

    @jsii.member(jsii_name="resetTlsCaKeyBits")
    def reset_tls_ca_key_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCaKeyBits", []))

    @jsii.member(jsii_name="resetTlsCaKeyType")
    def reset_tls_ca_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCaKeyType", []))

    @jsii.member(jsii_name="resetTlsMinVersion")
    def reset_tls_min_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsMinVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientKeyBitsInput")
    def default_tls_client_key_bits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTlsClientKeyBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientKeyTypeInput")
    def default_tls_client_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTlsClientKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientTtlInput")
    def default_tls_client_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTlsClientTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRemountInput")
    def disable_remount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRemountInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listenAddrsInput")
    def listen_addrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listenAddrsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="serverHostnamesInput")
    def server_hostnames_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverHostnamesInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIpsInput")
    def server_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCaKeyBitsInput")
    def tls_ca_key_bits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tlsCaKeyBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCaKeyTypeInput")
    def tls_ca_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCaKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersionInput")
    def tls_min_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsMinVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientKeyBits")
    def default_tls_client_key_bits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTlsClientKeyBits"))

    @default_tls_client_key_bits.setter
    def default_tls_client_key_bits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "default_tls_client_key_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTlsClientKeyBits", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientKeyType")
    def default_tls_client_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTlsClientKeyType"))

    @default_tls_client_key_type.setter
    def default_tls_client_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "default_tls_client_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTlsClientKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTlsClientTtl")
    def default_tls_client_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTlsClientTtl"))

    @default_tls_client_ttl.setter
    def default_tls_client_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "default_tls_client_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTlsClientTtl", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableRemount")
    def disable_remount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRemount"))

    @disable_remount.setter
    def disable_remount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "disable_remount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRemount", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="listenAddrs")
    def listen_addrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listenAddrs"))

    @listen_addrs.setter
    def listen_addrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "listen_addrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenAddrs", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="serverHostnames")
    def server_hostnames(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serverHostnames"))

    @server_hostnames.setter
    def server_hostnames(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "server_hostnames").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverHostnames", value)

    @builtins.property
    @jsii.member(jsii_name="serverIps")
    def server_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serverIps"))

    @server_ips.setter
    def server_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "server_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverIps", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCaKeyBits")
    def tls_ca_key_bits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tlsCaKeyBits"))

    @tls_ca_key_bits.setter
    def tls_ca_key_bits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "tls_ca_key_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCaKeyBits", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCaKeyType")
    def tls_ca_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCaKeyType"))

    @tls_ca_key_type.setter
    def tls_ca_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "tls_ca_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCaKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersion")
    def tls_min_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsMinVersion"))

    @tls_min_version.setter
    def tls_min_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KmipSecretBackend, "tls_min_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsMinVersion", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.kmipSecretBackend.KmipSecretBackendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "path": "path",
        "default_tls_client_key_bits": "defaultTlsClientKeyBits",
        "default_tls_client_key_type": "defaultTlsClientKeyType",
        "default_tls_client_ttl": "defaultTlsClientTtl",
        "description": "description",
        "disable_remount": "disableRemount",
        "id": "id",
        "listen_addrs": "listenAddrs",
        "namespace": "namespace",
        "server_hostnames": "serverHostnames",
        "server_ips": "serverIps",
        "tls_ca_key_bits": "tlsCaKeyBits",
        "tls_ca_key_type": "tlsCaKeyType",
        "tls_min_version": "tlsMinVersion",
    },
)
class KmipSecretBackendConfig(cdktf.TerraformMetaArguments):
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
        path: builtins.str,
        default_tls_client_key_bits: typing.Optional[jsii.Number] = None,
        default_tls_client_key_type: typing.Optional[builtins.str] = None,
        default_tls_client_ttl: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        listen_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        server_hostnames: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        tls_ca_key_bits: typing.Optional[jsii.Number] = None,
        tls_ca_key_type: typing.Optional[builtins.str] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param path: Path where KMIP secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#path KmipSecretBackend#path}
        :param default_tls_client_key_bits: Client certificate key bits, valid values depend on key type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_bits KmipSecretBackend#default_tls_client_key_bits}
        :param default_tls_client_key_type: Client certificate key type, rsa or ec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_type KmipSecretBackend#default_tls_client_key_type}
        :param default_tls_client_ttl: Client certificate TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_ttl KmipSecretBackend#default_tls_client_ttl}
        :param description: Human-friendly description of the mount for the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#description KmipSecretBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#disable_remount KmipSecretBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#id KmipSecretBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param listen_addrs: Addresses the KMIP server should listen on (host:port). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#listen_addrs KmipSecretBackend#listen_addrs}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#namespace KmipSecretBackend#namespace}
        :param server_hostnames: Hostnames to include in the server's TLS certificate as SAN DNS names. The first will be used as the common name (CN) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_hostnames KmipSecretBackend#server_hostnames}
        :param server_ips: IPs to include in the server's TLS certificate as SAN IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_ips KmipSecretBackend#server_ips}
        :param tls_ca_key_bits: CA key bits, valid values depend on key type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_bits KmipSecretBackend#tls_ca_key_bits}
        :param tls_ca_key_type: CA key type, rsa or ec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_type KmipSecretBackend#tls_ca_key_type}
        :param tls_min_version: Minimum TLS version to accept. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_min_version KmipSecretBackend#tls_min_version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(KmipSecretBackendConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument default_tls_client_key_bits", value=default_tls_client_key_bits, expected_type=type_hints["default_tls_client_key_bits"])
            check_type(argname="argument default_tls_client_key_type", value=default_tls_client_key_type, expected_type=type_hints["default_tls_client_key_type"])
            check_type(argname="argument default_tls_client_ttl", value=default_tls_client_ttl, expected_type=type_hints["default_tls_client_ttl"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_remount", value=disable_remount, expected_type=type_hints["disable_remount"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument listen_addrs", value=listen_addrs, expected_type=type_hints["listen_addrs"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument server_hostnames", value=server_hostnames, expected_type=type_hints["server_hostnames"])
            check_type(argname="argument server_ips", value=server_ips, expected_type=type_hints["server_ips"])
            check_type(argname="argument tls_ca_key_bits", value=tls_ca_key_bits, expected_type=type_hints["tls_ca_key_bits"])
            check_type(argname="argument tls_ca_key_type", value=tls_ca_key_type, expected_type=type_hints["tls_ca_key_type"])
            check_type(argname="argument tls_min_version", value=tls_min_version, expected_type=type_hints["tls_min_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
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
        if default_tls_client_key_bits is not None:
            self._values["default_tls_client_key_bits"] = default_tls_client_key_bits
        if default_tls_client_key_type is not None:
            self._values["default_tls_client_key_type"] = default_tls_client_key_type
        if default_tls_client_ttl is not None:
            self._values["default_tls_client_ttl"] = default_tls_client_ttl
        if description is not None:
            self._values["description"] = description
        if disable_remount is not None:
            self._values["disable_remount"] = disable_remount
        if id is not None:
            self._values["id"] = id
        if listen_addrs is not None:
            self._values["listen_addrs"] = listen_addrs
        if namespace is not None:
            self._values["namespace"] = namespace
        if server_hostnames is not None:
            self._values["server_hostnames"] = server_hostnames
        if server_ips is not None:
            self._values["server_ips"] = server_ips
        if tls_ca_key_bits is not None:
            self._values["tls_ca_key_bits"] = tls_ca_key_bits
        if tls_ca_key_type is not None:
            self._values["tls_ca_key_type"] = tls_ca_key_type
        if tls_min_version is not None:
            self._values["tls_min_version"] = tls_min_version

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
    def path(self) -> builtins.str:
        '''Path where KMIP secret backend will be mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#path KmipSecretBackend#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_tls_client_key_bits(self) -> typing.Optional[jsii.Number]:
        '''Client certificate key bits, valid values depend on key type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_bits KmipSecretBackend#default_tls_client_key_bits}
        '''
        result = self._values.get("default_tls_client_key_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_tls_client_key_type(self) -> typing.Optional[builtins.str]:
        '''Client certificate key type, rsa or ec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_key_type KmipSecretBackend#default_tls_client_key_type}
        '''
        result = self._values.get("default_tls_client_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_tls_client_ttl(self) -> typing.Optional[jsii.Number]:
        '''Client certificate TTL in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#default_tls_client_ttl KmipSecretBackend#default_tls_client_ttl}
        '''
        result = self._values.get("default_tls_client_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-friendly description of the mount for the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#description KmipSecretBackend#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_remount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set, opts out of mount migration on path updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#disable_remount KmipSecretBackend#disable_remount}
        '''
        result = self._values.get("disable_remount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#id KmipSecretBackend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def listen_addrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Addresses the KMIP server should listen on (host:port).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#listen_addrs KmipSecretBackend#listen_addrs}
        '''
        result = self._values.get("listen_addrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#namespace KmipSecretBackend#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_hostnames(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hostnames to include in the server's TLS certificate as SAN DNS names.

        The first will be used as the common name (CN)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_hostnames KmipSecretBackend#server_hostnames}
        '''
        result = self._values.get("server_hostnames")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IPs to include in the server's TLS certificate as SAN IP addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#server_ips KmipSecretBackend#server_ips}
        '''
        result = self._values.get("server_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tls_ca_key_bits(self) -> typing.Optional[jsii.Number]:
        '''CA key bits, valid values depend on key type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_bits KmipSecretBackend#tls_ca_key_bits}
        '''
        result = self._values.get("tls_ca_key_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls_ca_key_type(self) -> typing.Optional[builtins.str]:
        '''CA key type, rsa or ec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_ca_key_type KmipSecretBackend#tls_ca_key_type}
        '''
        result = self._values.get("tls_ca_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_min_version(self) -> typing.Optional[builtins.str]:
        '''Minimum TLS version to accept.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kmip_secret_backend#tls_min_version KmipSecretBackend#tls_min_version}
        '''
        result = self._values.get("tls_min_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KmipSecretBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KmipSecretBackend",
    "KmipSecretBackendConfig",
]

publication.publish()
