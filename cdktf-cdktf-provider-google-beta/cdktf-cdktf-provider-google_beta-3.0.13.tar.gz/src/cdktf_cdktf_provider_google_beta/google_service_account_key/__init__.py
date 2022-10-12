'''
# `google_service_account_key`

Refer to the Terraform Registory for docs: [`google_service_account_key`](https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key).
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


class GoogleServiceAccountKey(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleServiceAccountKey.GoogleServiceAccountKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key google_service_account_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        service_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        keepers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        key_algorithm: typing.Optional[builtins.str] = None,
        private_key_type: typing.Optional[builtins.str] = None,
        public_key_data: typing.Optional[builtins.str] = None,
        public_key_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key google_service_account_key} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service_account_id: The ID of the parent service account of the key. This can be a string in the format {ACCOUNT} or projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}, where {ACCOUNT} is the email address or unique id of the service account. If the {ACCOUNT} syntax is used, the project will be inferred from the provider's configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#service_account_id GoogleServiceAccountKey#service_account_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#id GoogleServiceAccountKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#keepers GoogleServiceAccountKey#keepers}
        :param key_algorithm: The algorithm used to generate the key, used only on create. KEY_ALG_RSA_2048 is the default algorithm. Valid values are: "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#key_algorithm GoogleServiceAccountKey#key_algorithm}
        :param private_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#private_key_type GoogleServiceAccountKey#private_key_type}.
        :param public_key_data: A field that allows clients to upload their own public key. If set, use this public key data to create a service account key for given service account. Please note, the expected format for this field is a base64 encoded X509_PEM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_data GoogleServiceAccountKey#public_key_data}
        :param public_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_type GoogleServiceAccountKey#public_key_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleServiceAccountKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleServiceAccountKeyConfig(
            service_account_id=service_account_id,
            id=id,
            keepers=keepers,
            key_algorithm=key_algorithm,
            private_key_type=private_key_type,
            public_key_data=public_key_data,
            public_key_type=public_key_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeepers")
    def reset_keepers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepers", []))

    @jsii.member(jsii_name="resetKeyAlgorithm")
    def reset_key_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyAlgorithm", []))

    @jsii.member(jsii_name="resetPrivateKeyType")
    def reset_private_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyType", []))

    @jsii.member(jsii_name="resetPublicKeyData")
    def reset_public_key_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKeyData", []))

    @jsii.member(jsii_name="resetPublicKeyType")
    def reset_public_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKeyType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @builtins.property
    @jsii.member(jsii_name="validAfter")
    def valid_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validAfter"))

    @builtins.property
    @jsii.member(jsii_name="validBefore")
    def valid_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validBefore"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keepersInput")
    def keepers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "keepersInput"))

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithmInput")
    def key_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyTypeInput")
    def private_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyDataInput")
    def public_key_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyDataInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyTypeInput")
    def public_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountIdInput")
    def service_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keepers")
    def keepers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "keepers"))

    @keepers.setter
    def keepers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "keepers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepers", value)

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyAlgorithm"))

    @key_algorithm.setter
    def key_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "key_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyType")
    def private_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyType"))

    @private_key_type.setter
    def private_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "private_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="publicKeyData")
    def public_key_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyData"))

    @public_key_data.setter
    def public_key_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "public_key_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyData", value)

    @builtins.property
    @jsii.member(jsii_name="publicKeyType")
    def public_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyType"))

    @public_key_type.setter
    def public_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "public_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountId")
    def service_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountId"))

    @service_account_id.setter
    def service_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceAccountKey, "service_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleServiceAccountKey.GoogleServiceAccountKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "service_account_id": "serviceAccountId",
        "id": "id",
        "keepers": "keepers",
        "key_algorithm": "keyAlgorithm",
        "private_key_type": "privateKeyType",
        "public_key_data": "publicKeyData",
        "public_key_type": "publicKeyType",
    },
)
class GoogleServiceAccountKeyConfig(cdktf.TerraformMetaArguments):
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
        service_account_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        keepers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        key_algorithm: typing.Optional[builtins.str] = None,
        private_key_type: typing.Optional[builtins.str] = None,
        public_key_data: typing.Optional[builtins.str] = None,
        public_key_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param service_account_id: The ID of the parent service account of the key. This can be a string in the format {ACCOUNT} or projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}, where {ACCOUNT} is the email address or unique id of the service account. If the {ACCOUNT} syntax is used, the project will be inferred from the provider's configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#service_account_id GoogleServiceAccountKey#service_account_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#id GoogleServiceAccountKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#keepers GoogleServiceAccountKey#keepers}
        :param key_algorithm: The algorithm used to generate the key, used only on create. KEY_ALG_RSA_2048 is the default algorithm. Valid values are: "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#key_algorithm GoogleServiceAccountKey#key_algorithm}
        :param private_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#private_key_type GoogleServiceAccountKey#private_key_type}.
        :param public_key_data: A field that allows clients to upload their own public key. If set, use this public key data to create a service account key for given service account. Please note, the expected format for this field is a base64 encoded X509_PEM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_data GoogleServiceAccountKey#public_key_data}
        :param public_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_type GoogleServiceAccountKey#public_key_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleServiceAccountKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument service_account_id", value=service_account_id, expected_type=type_hints["service_account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument keepers", value=keepers, expected_type=type_hints["keepers"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument private_key_type", value=private_key_type, expected_type=type_hints["private_key_type"])
            check_type(argname="argument public_key_data", value=public_key_data, expected_type=type_hints["public_key_data"])
            check_type(argname="argument public_key_type", value=public_key_type, expected_type=type_hints["public_key_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_account_id": service_account_id,
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
        if keepers is not None:
            self._values["keepers"] = keepers
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if private_key_type is not None:
            self._values["private_key_type"] = private_key_type
        if public_key_data is not None:
            self._values["public_key_data"] = public_key_data
        if public_key_type is not None:
            self._values["public_key_type"] = public_key_type

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
    def service_account_id(self) -> builtins.str:
        '''The ID of the parent service account of the key.

        This can be a string in the format {ACCOUNT} or projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}, where {ACCOUNT} is the email address or unique id of the service account. If the {ACCOUNT} syntax is used, the project will be inferred from the provider's configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#service_account_id GoogleServiceAccountKey#service_account_id}
        '''
        result = self._values.get("service_account_id")
        assert result is not None, "Required property 'service_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#id GoogleServiceAccountKey#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Arbitrary map of values that, when changed, will trigger recreation of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#keepers GoogleServiceAccountKey#keepers}
        '''
        result = self._values.get("keepers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def key_algorithm(self) -> typing.Optional[builtins.str]:
        '''The algorithm used to generate the key, used only on create.

        KEY_ALG_RSA_2048 is the default algorithm. Valid values are: "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#key_algorithm GoogleServiceAccountKey#key_algorithm}
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#private_key_type GoogleServiceAccountKey#private_key_type}.'''
        result = self._values.get("private_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key_data(self) -> typing.Optional[builtins.str]:
        '''A field that allows clients to upload their own public key.

        If set, use this public key data to create a service account key for given service account. Please note, the expected format for this field is a base64 encoded X509_PEM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_data GoogleServiceAccountKey#public_key_data}
        '''
        result = self._values.get("public_key_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_account_key#public_key_type GoogleServiceAccountKey#public_key_type}.'''
        result = self._values.get("public_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleServiceAccountKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GoogleServiceAccountKey",
    "GoogleServiceAccountKeyConfig",
]

publication.publish()
