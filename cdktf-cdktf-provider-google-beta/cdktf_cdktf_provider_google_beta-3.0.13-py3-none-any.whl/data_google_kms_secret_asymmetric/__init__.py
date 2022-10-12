'''
# `data_google_kms_secret_asymmetric`

Refer to the Terraform Registory for docs: [`data_google_kms_secret_asymmetric`](https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric).
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


class DataGoogleKmsSecretAsymmetric(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleKmsSecretAsymmetric.DataGoogleKmsSecretAsymmetric",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric google_kms_secret_asymmetric}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        ciphertext: builtins.str,
        crypto_key_version: builtins.str,
        crc32: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric google_kms_secret_asymmetric} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ciphertext: The public key encrypted ciphertext in base64 encoding. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#ciphertext DataGoogleKmsSecretAsymmetric#ciphertext}
        :param crypto_key_version: The fully qualified KMS crypto key version name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crypto_key_version DataGoogleKmsSecretAsymmetric#crypto_key_version}
        :param crc32: The crc32 checksum of the ciphertext, hexadecimal encoding. If not specified, it will be computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crc32 DataGoogleKmsSecretAsymmetric#crc32}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#id DataGoogleKmsSecretAsymmetric#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleKmsSecretAsymmetric.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleKmsSecretAsymmetricConfig(
            ciphertext=ciphertext,
            crypto_key_version=crypto_key_version,
            crc32=crc32,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCrc32")
    def reset_crc32(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrc32", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="plaintext")
    def plaintext(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plaintext"))

    @builtins.property
    @jsii.member(jsii_name="ciphertextInput")
    def ciphertext_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ciphertextInput"))

    @builtins.property
    @jsii.member(jsii_name="crc32Input")
    def crc32_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crc32Input"))

    @builtins.property
    @jsii.member(jsii_name="cryptoKeyVersionInput")
    def crypto_key_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cryptoKeyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ciphertext")
    def ciphertext(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ciphertext"))

    @ciphertext.setter
    def ciphertext(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleKmsSecretAsymmetric, "ciphertext").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciphertext", value)

    @builtins.property
    @jsii.member(jsii_name="crc32")
    def crc32(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crc32"))

    @crc32.setter
    def crc32(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleKmsSecretAsymmetric, "crc32").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crc32", value)

    @builtins.property
    @jsii.member(jsii_name="cryptoKeyVersion")
    def crypto_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cryptoKeyVersion"))

    @crypto_key_version.setter
    def crypto_key_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleKmsSecretAsymmetric, "crypto_key_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cryptoKeyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleKmsSecretAsymmetric, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleKmsSecretAsymmetric.DataGoogleKmsSecretAsymmetricConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ciphertext": "ciphertext",
        "crypto_key_version": "cryptoKeyVersion",
        "crc32": "crc32",
        "id": "id",
    },
)
class DataGoogleKmsSecretAsymmetricConfig(cdktf.TerraformMetaArguments):
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
        ciphertext: builtins.str,
        crypto_key_version: builtins.str,
        crc32: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ciphertext: The public key encrypted ciphertext in base64 encoding. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#ciphertext DataGoogleKmsSecretAsymmetric#ciphertext}
        :param crypto_key_version: The fully qualified KMS crypto key version name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crypto_key_version DataGoogleKmsSecretAsymmetric#crypto_key_version}
        :param crc32: The crc32 checksum of the ciphertext, hexadecimal encoding. If not specified, it will be computed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crc32 DataGoogleKmsSecretAsymmetric#crc32}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#id DataGoogleKmsSecretAsymmetric#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleKmsSecretAsymmetricConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ciphertext", value=ciphertext, expected_type=type_hints["ciphertext"])
            check_type(argname="argument crypto_key_version", value=crypto_key_version, expected_type=type_hints["crypto_key_version"])
            check_type(argname="argument crc32", value=crc32, expected_type=type_hints["crc32"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "ciphertext": ciphertext,
            "crypto_key_version": crypto_key_version,
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
        if crc32 is not None:
            self._values["crc32"] = crc32
        if id is not None:
            self._values["id"] = id

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
    def ciphertext(self) -> builtins.str:
        '''The public key encrypted ciphertext in base64 encoding.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#ciphertext DataGoogleKmsSecretAsymmetric#ciphertext}
        '''
        result = self._values.get("ciphertext")
        assert result is not None, "Required property 'ciphertext' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def crypto_key_version(self) -> builtins.str:
        '''The fully qualified KMS crypto key version name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crypto_key_version DataGoogleKmsSecretAsymmetric#crypto_key_version}
        '''
        result = self._values.get("crypto_key_version")
        assert result is not None, "Required property 'crypto_key_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def crc32(self) -> typing.Optional[builtins.str]:
        '''The crc32 checksum of the ciphertext, hexadecimal encoding. If not specified, it will be computed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#crc32 DataGoogleKmsSecretAsymmetric#crc32}
        '''
        result = self._values.get("crc32")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_kms_secret_asymmetric#id DataGoogleKmsSecretAsymmetric#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleKmsSecretAsymmetricConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleKmsSecretAsymmetric",
    "DataGoogleKmsSecretAsymmetricConfig",
]

publication.publish()
