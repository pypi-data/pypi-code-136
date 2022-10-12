'''
# `google_kms_secret_ciphertext`

Refer to the Terraform Registory for docs: [`google_kms_secret_ciphertext`](https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext).
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


class GoogleKmsSecretCiphertext(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsSecretCiphertext.GoogleKmsSecretCiphertext",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext google_kms_secret_ciphertext}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        crypto_key: builtins.str,
        plaintext: builtins.str,
        additional_authenticated_data: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsSecretCiphertextTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext google_kms_secret_ciphertext} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#crypto_key GoogleKmsSecretCiphertext#crypto_key}
        :param plaintext: The plaintext to be encrypted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#plaintext GoogleKmsSecretCiphertext#plaintext}
        :param additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#additional_authenticated_data GoogleKmsSecretCiphertext#additional_authenticated_data}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#id GoogleKmsSecretCiphertext#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#timeouts GoogleKmsSecretCiphertext#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsSecretCiphertext.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleKmsSecretCiphertextConfig(
            crypto_key=crypto_key,
            plaintext=plaintext,
            additional_authenticated_data=additional_authenticated_data,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#create GoogleKmsSecretCiphertext#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#delete GoogleKmsSecretCiphertext#delete}.
        '''
        value = GoogleKmsSecretCiphertextTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdditionalAuthenticatedData")
    def reset_additional_authenticated_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalAuthenticatedData", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ciphertext")
    def ciphertext(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ciphertext"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleKmsSecretCiphertextTimeoutsOutputReference":
        return typing.cast("GoogleKmsSecretCiphertextTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticatedDataInput")
    def additional_authenticated_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalAuthenticatedDataInput"))

    @builtins.property
    @jsii.member(jsii_name="cryptoKeyInput")
    def crypto_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cryptoKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="plaintextInput")
    def plaintext_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "plaintextInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleKmsSecretCiphertextTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleKmsSecretCiphertextTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticatedData")
    def additional_authenticated_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalAuthenticatedData"))

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertext, "additional_authenticated_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalAuthenticatedData", value)

    @builtins.property
    @jsii.member(jsii_name="cryptoKey")
    def crypto_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cryptoKey"))

    @crypto_key.setter
    def crypto_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertext, "crypto_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cryptoKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertext, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="plaintext")
    def plaintext(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plaintext"))

    @plaintext.setter
    def plaintext(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertext, "plaintext").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plaintext", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsSecretCiphertext.GoogleKmsSecretCiphertextConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "crypto_key": "cryptoKey",
        "plaintext": "plaintext",
        "additional_authenticated_data": "additionalAuthenticatedData",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class GoogleKmsSecretCiphertextConfig(cdktf.TerraformMetaArguments):
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
        crypto_key: builtins.str,
        plaintext: builtins.str,
        additional_authenticated_data: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsSecretCiphertextTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#crypto_key GoogleKmsSecretCiphertext#crypto_key}
        :param plaintext: The plaintext to be encrypted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#plaintext GoogleKmsSecretCiphertext#plaintext}
        :param additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#additional_authenticated_data GoogleKmsSecretCiphertext#additional_authenticated_data}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#id GoogleKmsSecretCiphertext#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#timeouts GoogleKmsSecretCiphertext#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleKmsSecretCiphertextTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsSecretCiphertextConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument crypto_key", value=crypto_key, expected_type=type_hints["crypto_key"])
            check_type(argname="argument plaintext", value=plaintext, expected_type=type_hints["plaintext"])
            check_type(argname="argument additional_authenticated_data", value=additional_authenticated_data, expected_type=type_hints["additional_authenticated_data"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "crypto_key": crypto_key,
            "plaintext": plaintext,
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
        if additional_authenticated_data is not None:
            self._values["additional_authenticated_data"] = additional_authenticated_data
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def crypto_key(self) -> builtins.str:
        '''The full name of the CryptoKey that will be used to encrypt the provided plaintext. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}''.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#crypto_key GoogleKmsSecretCiphertext#crypto_key}
        '''
        result = self._values.get("crypto_key")
        assert result is not None, "Required property 'crypto_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plaintext(self) -> builtins.str:
        '''The plaintext to be encrypted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#plaintext GoogleKmsSecretCiphertext#plaintext}
        '''
        result = self._values.get("plaintext")
        assert result is not None, "Required property 'plaintext' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_authenticated_data(self) -> typing.Optional[builtins.str]:
        '''The additional authenticated data used for integrity checks during encryption and decryption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#additional_authenticated_data GoogleKmsSecretCiphertext#additional_authenticated_data}
        '''
        result = self._values.get("additional_authenticated_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#id GoogleKmsSecretCiphertext#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleKmsSecretCiphertextTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#timeouts GoogleKmsSecretCiphertext#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleKmsSecretCiphertextTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsSecretCiphertextConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsSecretCiphertext.GoogleKmsSecretCiphertextTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleKmsSecretCiphertextTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#create GoogleKmsSecretCiphertext#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#delete GoogleKmsSecretCiphertext#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsSecretCiphertextTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#create GoogleKmsSecretCiphertext#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_secret_ciphertext#delete GoogleKmsSecretCiphertext#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsSecretCiphertextTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsSecretCiphertextTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsSecretCiphertext.GoogleKmsSecretCiphertextTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsSecretCiphertextTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertextTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertextTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleKmsSecretCiphertextTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleKmsSecretCiphertextTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleKmsSecretCiphertextTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsSecretCiphertextTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleKmsSecretCiphertext",
    "GoogleKmsSecretCiphertextConfig",
    "GoogleKmsSecretCiphertextTimeouts",
    "GoogleKmsSecretCiphertextTimeoutsOutputReference",
]

publication.publish()
