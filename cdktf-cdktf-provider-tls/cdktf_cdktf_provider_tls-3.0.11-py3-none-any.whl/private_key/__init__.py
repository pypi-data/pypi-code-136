'''
# `tls_private_key`

Refer to the Terraform Registory for docs: [`tls_private_key`](https://www.terraform.io/docs/providers/tls/r/private_key).
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


class PrivateKey(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tls.privateKey.PrivateKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tls/r/private_key tls_private_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        algorithm: builtins.str,
        ecdsa_curve: typing.Optional[builtins.str] = None,
        rsa_bits: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tls/r/private_key tls_private_key} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param algorithm: Name of the algorithm to use when generating the private key. Currently-supported values are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#algorithm PrivateKey#algorithm}
        :param ecdsa_curve: When ``algorithm`` is ``ECDSA``, the name of the elliptic curve to use. Currently-supported values are: ``P224``, ``P256``, ``P384``, ``P521``. (default: ``P224``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#ecdsa_curve PrivateKey#ecdsa_curve}
        :param rsa_bits: When ``algorithm`` is ``RSA``, the size of the generated RSA key, in bits (default: ``2048``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#rsa_bits PrivateKey#rsa_bits}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PrivateKeyConfig(
            algorithm=algorithm,
            ecdsa_curve=ecdsa_curve,
            rsa_bits=rsa_bits,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetEcdsaCurve")
    def reset_ecdsa_curve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEcdsaCurve", []))

    @jsii.member(jsii_name="resetRsaBits")
    def reset_rsa_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRsaBits", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyOpenssh")
    def private_key_openssh(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyOpenssh"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPem")
    def private_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyPem"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPemPkcs8")
    def private_key_pem_pkcs8(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyPemPkcs8"))

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
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="ecdsaCurveInput")
    def ecdsa_curve_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ecdsaCurveInput"))

    @builtins.property
    @jsii.member(jsii_name="rsaBitsInput")
    def rsa_bits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rsaBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateKey, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="ecdsaCurve")
    def ecdsa_curve(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ecdsaCurve"))

    @ecdsa_curve.setter
    def ecdsa_curve(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateKey, "ecdsa_curve").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ecdsaCurve", value)

    @builtins.property
    @jsii.member(jsii_name="rsaBits")
    def rsa_bits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rsaBits"))

    @rsa_bits.setter
    def rsa_bits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateKey, "rsa_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rsaBits", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tls.privateKey.PrivateKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "algorithm": "algorithm",
        "ecdsa_curve": "ecdsaCurve",
        "rsa_bits": "rsaBits",
    },
)
class PrivateKeyConfig(cdktf.TerraformMetaArguments):
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
        algorithm: builtins.str,
        ecdsa_curve: typing.Optional[builtins.str] = None,
        rsa_bits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param algorithm: Name of the algorithm to use when generating the private key. Currently-supported values are: ``RSA``, ``ECDSA``, ``ED25519``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#algorithm PrivateKey#algorithm}
        :param ecdsa_curve: When ``algorithm`` is ``ECDSA``, the name of the elliptic curve to use. Currently-supported values are: ``P224``, ``P256``, ``P384``, ``P521``. (default: ``P224``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#ecdsa_curve PrivateKey#ecdsa_curve}
        :param rsa_bits: When ``algorithm`` is ``RSA``, the size of the generated RSA key, in bits (default: ``2048``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#rsa_bits PrivateKey#rsa_bits}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(PrivateKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument ecdsa_curve", value=ecdsa_curve, expected_type=type_hints["ecdsa_curve"])
            check_type(argname="argument rsa_bits", value=rsa_bits, expected_type=type_hints["rsa_bits"])
        self._values: typing.Dict[str, typing.Any] = {
            "algorithm": algorithm,
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
        if ecdsa_curve is not None:
            self._values["ecdsa_curve"] = ecdsa_curve
        if rsa_bits is not None:
            self._values["rsa_bits"] = rsa_bits

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
    def algorithm(self) -> builtins.str:
        '''Name of the algorithm to use when generating the private key. Currently-supported values are: ``RSA``, ``ECDSA``, ``ED25519``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#algorithm PrivateKey#algorithm}
        '''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ecdsa_curve(self) -> typing.Optional[builtins.str]:
        '''When ``algorithm`` is ``ECDSA``, the name of the elliptic curve to use.

        Currently-supported values are: ``P224``, ``P256``, ``P384``, ``P521``. (default: ``P224``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#ecdsa_curve PrivateKey#ecdsa_curve}
        '''
        result = self._values.get("ecdsa_curve")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rsa_bits(self) -> typing.Optional[jsii.Number]:
        '''When ``algorithm`` is ``RSA``, the size of the generated RSA key, in bits (default: ``2048``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/private_key#rsa_bits PrivateKey#rsa_bits}
        '''
        result = self._values.get("rsa_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PrivateKey",
    "PrivateKeyConfig",
]

publication.publish()
