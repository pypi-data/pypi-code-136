'''
# `google_kms_key_ring_import_job`

Refer to the Terraform Registory for docs: [`google_kms_key_ring_import_job`](https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job).
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


class GoogleKmsKeyRingImportJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job google_kms_key_ring_import_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        import_job_id: builtins.str,
        import_method: builtins.str,
        key_ring: builtins.str,
        protection_level: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsKeyRingImportJobTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job google_kms_key_ring_import_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param import_job_id: It must be unique within a KeyRing and match the regular expression [a-zA-Z0-9_-]{1,63}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_job_id GoogleKmsKeyRingImportJob#import_job_id}
        :param import_method: The wrapping method to be used for incoming key material. Possible values: ["RSA_OAEP_3072_SHA1_AES_256", "RSA_OAEP_4096_SHA1_AES_256"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_method GoogleKmsKeyRingImportJob#import_method}
        :param key_ring: The KeyRing that this import job belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#key_ring GoogleKmsKeyRingImportJob#key_ring}
        :param protection_level: The protection level of the ImportJob. This must match the protectionLevel of the versionTemplate on the CryptoKey you attempt to import into. Possible values: ["SOFTWARE", "HSM", "EXTERNAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#protection_level GoogleKmsKeyRingImportJob#protection_level}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#id GoogleKmsKeyRingImportJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#timeouts GoogleKmsKeyRingImportJob#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleKmsKeyRingImportJobConfig(
            import_job_id=import_job_id,
            import_method=import_method,
            key_ring=key_ring,
            protection_level=protection_level,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#create GoogleKmsKeyRingImportJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#delete GoogleKmsKeyRingImportJob#delete}.
        '''
        value = GoogleKmsKeyRingImportJobTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

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
    @jsii.member(jsii_name="attestation")
    def attestation(self) -> "GoogleKmsKeyRingImportJobAttestationList":
        return typing.cast("GoogleKmsKeyRingImportJobAttestationList", jsii.get(self, "attestation"))

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expireTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> "GoogleKmsKeyRingImportJobPublicKeyList":
        return typing.cast("GoogleKmsKeyRingImportJobPublicKeyList", jsii.get(self, "publicKey"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleKmsKeyRingImportJobTimeoutsOutputReference":
        return typing.cast("GoogleKmsKeyRingImportJobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importJobIdInput")
    def import_job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importJobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="importMethodInput")
    def import_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="keyRingInput")
    def key_ring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyRingInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionLevelInput")
    def protection_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectionLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleKmsKeyRingImportJobTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleKmsKeyRingImportJobTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importJobId")
    def import_job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "importJobId"))

    @import_job_id.setter
    def import_job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJob, "import_job_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importJobId", value)

    @builtins.property
    @jsii.member(jsii_name="importMethod")
    def import_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "importMethod"))

    @import_method.setter
    def import_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJob, "import_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importMethod", value)

    @builtins.property
    @jsii.member(jsii_name="keyRing")
    def key_ring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyRing"))

    @key_ring.setter
    def key_ring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJob, "key_ring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyRing", value)

    @builtins.property
    @jsii.member(jsii_name="protectionLevel")
    def protection_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectionLevel"))

    @protection_level.setter
    def protection_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJob, "protection_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectionLevel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobAttestation",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleKmsKeyRingImportJobAttestation:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsKeyRingImportJobAttestation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsKeyRingImportJobAttestationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobAttestationList",
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
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobAttestationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleKmsKeyRingImportJobAttestationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobAttestationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleKmsKeyRingImportJobAttestationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobAttestationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobAttestationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobAttestationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleKmsKeyRingImportJobAttestationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobAttestationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobAttestationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleKmsKeyRingImportJobAttestation]:
        return typing.cast(typing.Optional[GoogleKmsKeyRingImportJobAttestation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleKmsKeyRingImportJobAttestation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobAttestationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "import_job_id": "importJobId",
        "import_method": "importMethod",
        "key_ring": "keyRing",
        "protection_level": "protectionLevel",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class GoogleKmsKeyRingImportJobConfig(cdktf.TerraformMetaArguments):
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
        import_job_id: builtins.str,
        import_method: builtins.str,
        key_ring: builtins.str,
        protection_level: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsKeyRingImportJobTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param import_job_id: It must be unique within a KeyRing and match the regular expression [a-zA-Z0-9_-]{1,63}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_job_id GoogleKmsKeyRingImportJob#import_job_id}
        :param import_method: The wrapping method to be used for incoming key material. Possible values: ["RSA_OAEP_3072_SHA1_AES_256", "RSA_OAEP_4096_SHA1_AES_256"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_method GoogleKmsKeyRingImportJob#import_method}
        :param key_ring: The KeyRing that this import job belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#key_ring GoogleKmsKeyRingImportJob#key_ring}
        :param protection_level: The protection level of the ImportJob. This must match the protectionLevel of the versionTemplate on the CryptoKey you attempt to import into. Possible values: ["SOFTWARE", "HSM", "EXTERNAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#protection_level GoogleKmsKeyRingImportJob#protection_level}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#id GoogleKmsKeyRingImportJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#timeouts GoogleKmsKeyRingImportJob#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleKmsKeyRingImportJobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument import_job_id", value=import_job_id, expected_type=type_hints["import_job_id"])
            check_type(argname="argument import_method", value=import_method, expected_type=type_hints["import_method"])
            check_type(argname="argument key_ring", value=key_ring, expected_type=type_hints["key_ring"])
            check_type(argname="argument protection_level", value=protection_level, expected_type=type_hints["protection_level"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "import_job_id": import_job_id,
            "import_method": import_method,
            "key_ring": key_ring,
            "protection_level": protection_level,
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
    def import_job_id(self) -> builtins.str:
        '''It must be unique within a KeyRing and match the regular expression [a-zA-Z0-9_-]{1,63}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_job_id GoogleKmsKeyRingImportJob#import_job_id}
        '''
        result = self._values.get("import_job_id")
        assert result is not None, "Required property 'import_job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def import_method(self) -> builtins.str:
        '''The wrapping method to be used for incoming key material. Possible values: ["RSA_OAEP_3072_SHA1_AES_256", "RSA_OAEP_4096_SHA1_AES_256"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#import_method GoogleKmsKeyRingImportJob#import_method}
        '''
        result = self._values.get("import_method")
        assert result is not None, "Required property 'import_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_ring(self) -> builtins.str:
        '''The KeyRing that this import job belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#key_ring GoogleKmsKeyRingImportJob#key_ring}
        '''
        result = self._values.get("key_ring")
        assert result is not None, "Required property 'key_ring' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protection_level(self) -> builtins.str:
        '''The protection level of the ImportJob.

        This must match the protectionLevel of the
        versionTemplate on the CryptoKey you attempt to import into. Possible values: ["SOFTWARE", "HSM", "EXTERNAL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#protection_level GoogleKmsKeyRingImportJob#protection_level}
        '''
        result = self._values.get("protection_level")
        assert result is not None, "Required property 'protection_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#id GoogleKmsKeyRingImportJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleKmsKeyRingImportJobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#timeouts GoogleKmsKeyRingImportJob#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleKmsKeyRingImportJobTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsKeyRingImportJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobPublicKey",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleKmsKeyRingImportJobPublicKey:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsKeyRingImportJobPublicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsKeyRingImportJobPublicKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobPublicKeyList",
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
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobPublicKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleKmsKeyRingImportJobPublicKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobPublicKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleKmsKeyRingImportJobPublicKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobPublicKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobPublicKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobPublicKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleKmsKeyRingImportJobPublicKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobPublicKeyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobPublicKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="pem")
    def pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pem"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleKmsKeyRingImportJobPublicKey]:
        return typing.cast(typing.Optional[GoogleKmsKeyRingImportJobPublicKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleKmsKeyRingImportJobPublicKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobPublicKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleKmsKeyRingImportJobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#create GoogleKmsKeyRingImportJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#delete GoogleKmsKeyRingImportJob#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#create GoogleKmsKeyRingImportJob#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_key_ring_import_job#delete GoogleKmsKeyRingImportJob#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsKeyRingImportJobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsKeyRingImportJobTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsKeyRingImportJob.GoogleKmsKeyRingImportJobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsKeyRingImportJobTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleKmsKeyRingImportJobTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleKmsKeyRingImportJobTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleKmsKeyRingImportJobTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsKeyRingImportJobTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleKmsKeyRingImportJob",
    "GoogleKmsKeyRingImportJobAttestation",
    "GoogleKmsKeyRingImportJobAttestationList",
    "GoogleKmsKeyRingImportJobAttestationOutputReference",
    "GoogleKmsKeyRingImportJobConfig",
    "GoogleKmsKeyRingImportJobPublicKey",
    "GoogleKmsKeyRingImportJobPublicKeyList",
    "GoogleKmsKeyRingImportJobPublicKeyOutputReference",
    "GoogleKmsKeyRingImportJobTimeouts",
    "GoogleKmsKeyRingImportJobTimeoutsOutputReference",
]

publication.publish()
