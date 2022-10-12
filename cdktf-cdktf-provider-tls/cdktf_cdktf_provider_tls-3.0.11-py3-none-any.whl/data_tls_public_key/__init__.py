'''
# `data_tls_public_key`

Refer to the Terraform Registory for docs: [`data_tls_public_key`](https://www.terraform.io/docs/providers/tls/d/public_key).
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


class DataTlsPublicKey(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tls.dataTlsPublicKey.DataTlsPublicKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tls/d/public_key tls_public_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        private_key_openssh: typing.Optional[builtins.str] = None,
        private_key_pem: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tls/d/public_key tls_public_key} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param private_key_openssh: The private key (in `OpenSSH PEM (RFC 4716) <https://datatracker.ietf.org/doc/html/rfc4716>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_pem``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_openssh DataTlsPublicKey#private_key_openssh}
        :param private_key_pem: The private key (in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_openssh``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_pem DataTlsPublicKey#private_key_pem}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataTlsPublicKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataTlsPublicKeyConfig(
            private_key_openssh=private_key_openssh,
            private_key_pem=private_key_pem,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetPrivateKeyOpenssh")
    def reset_private_key_openssh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyOpenssh", []))

    @jsii.member(jsii_name="resetPrivateKeyPem")
    def reset_private_key_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyPem", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyFingerprintMd5")
    def public_key_fingerprint_md5(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyFingerprintMd5"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyFingerprintSha256")
    def public_key_fingerprint_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyFingerprintSha256"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyOpenssh")
    def public_key_openssh(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyOpenssh"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyPem")
    def public_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyPem"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyOpensshInput")
    def private_key_openssh_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyOpensshInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPemInput")
    def private_key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyOpenssh")
    def private_key_openssh(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyOpenssh"))

    @private_key_openssh.setter
    def private_key_openssh(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataTlsPublicKey, "private_key_openssh").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyOpenssh", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPem")
    def private_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyPem"))

    @private_key_pem.setter
    def private_key_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataTlsPublicKey, "private_key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPem", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tls.dataTlsPublicKey.DataTlsPublicKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "private_key_openssh": "privateKeyOpenssh",
        "private_key_pem": "privateKeyPem",
    },
)
class DataTlsPublicKeyConfig(cdktf.TerraformMetaArguments):
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
        private_key_openssh: typing.Optional[builtins.str] = None,
        private_key_pem: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param private_key_openssh: The private key (in `OpenSSH PEM (RFC 4716) <https://datatracker.ietf.org/doc/html/rfc4716>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_pem``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_openssh DataTlsPublicKey#private_key_openssh}
        :param private_key_pem: The private key (in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_openssh``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_pem DataTlsPublicKey#private_key_pem}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataTlsPublicKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument private_key_openssh", value=private_key_openssh, expected_type=type_hints["private_key_openssh"])
            check_type(argname="argument private_key_pem", value=private_key_pem, expected_type=type_hints["private_key_pem"])
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
        if private_key_openssh is not None:
            self._values["private_key_openssh"] = private_key_openssh
        if private_key_pem is not None:
            self._values["private_key_pem"] = private_key_pem

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
    def private_key_openssh(self) -> typing.Optional[builtins.str]:
        '''The private key (in  `OpenSSH PEM (RFC 4716) <https://datatracker.ietf.org/doc/html/rfc4716>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_pem``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_openssh DataTlsPublicKey#private_key_openssh}
        '''
        result = self._values.get("private_key_openssh")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_pem(self) -> typing.Optional[builtins.str]:
        '''The private key (in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format) to extract the public key from. This is *mutually exclusive* with ``private_key_openssh``. Currently-supported algorithms for keys are: ``RSA``, ``ECDSA``, ``ED25519``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/d/public_key#private_key_pem DataTlsPublicKey#private_key_pem}
        '''
        result = self._values.get("private_key_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTlsPublicKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataTlsPublicKey",
    "DataTlsPublicKeyConfig",
]

publication.publish()
