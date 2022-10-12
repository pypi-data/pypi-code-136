'''
# `google_kms_crypto_key`

Refer to the Terraform Registory for docs: [`google_kms_crypto_key`](https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key).
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


class GoogleKmsCryptoKey(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key google_kms_crypto_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        key_ring: builtins.str,
        name: builtins.str,
        destroy_scheduled_duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        import_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        purpose: typing.Optional[builtins.str] = None,
        rotation_period: typing.Optional[builtins.str] = None,
        skip_initial_version_creation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsCryptoKeyTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_template: typing.Optional[typing.Union["GoogleKmsCryptoKeyVersionTemplate", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key google_kms_crypto_key} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key_ring: The KeyRing that this key belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#key_ring GoogleKmsCryptoKey#key_ring}
        :param name: The resource name for the CryptoKey. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#name GoogleKmsCryptoKey#name}
        :param destroy_scheduled_duration: The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#destroy_scheduled_duration GoogleKmsCryptoKey#destroy_scheduled_duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#id GoogleKmsCryptoKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_only: Whether this key may contain imported versions only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#import_only GoogleKmsCryptoKey#import_only}
        :param labels: Labels with user-defined metadata to apply to this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#labels GoogleKmsCryptoKey#labels}
        :param purpose: The immutable purpose of this CryptoKey. See the `purpose reference <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose>`_ for possible inputs. Default value: "ENCRYPT_DECRYPT" Possible values: ["ENCRYPT_DECRYPT", "ASYMMETRIC_SIGN", "ASYMMETRIC_DECRYPT", "MAC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#purpose GoogleKmsCryptoKey#purpose}
        :param rotation_period: Every time this period passes, generate a new CryptoKeyVersion and set it as the primary. The first rotation will take place after the specified period. The rotation period has the format of a decimal number with up to 9 fractional digits, followed by the letter 's' (seconds). It must be greater than a day (ie, 86400). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#rotation_period GoogleKmsCryptoKey#rotation_period}
        :param skip_initial_version_creation: If set to true, the request will create a CryptoKey without any CryptoKeyVersions. You must use the 'google_kms_key_ring_import_job' resource to import the CryptoKeyVersion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#skip_initial_version_creation GoogleKmsCryptoKey#skip_initial_version_creation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#timeouts GoogleKmsCryptoKey#timeouts}
        :param version_template: version_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#version_template GoogleKmsCryptoKey#version_template}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsCryptoKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleKmsCryptoKeyConfig(
            key_ring=key_ring,
            name=name,
            destroy_scheduled_duration=destroy_scheduled_duration,
            id=id,
            import_only=import_only,
            labels=labels,
            purpose=purpose,
            rotation_period=rotation_period,
            skip_initial_version_creation=skip_initial_version_creation,
            timeouts=timeouts,
            version_template=version_template,
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
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#create GoogleKmsCryptoKey#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#delete GoogleKmsCryptoKey#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#update GoogleKmsCryptoKey#update}.
        '''
        value = GoogleKmsCryptoKeyTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVersionTemplate")
    def put_version_template(
        self,
        *,
        algorithm: builtins.str,
        protection_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm to use when creating a version based on this template. See the `algorithm reference <https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm>`_ for possible inputs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#algorithm GoogleKmsCryptoKey#algorithm}
        :param protection_level: The protection level to use when creating a version based on this template. Possible values include "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC". Defaults to "SOFTWARE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#protection_level GoogleKmsCryptoKey#protection_level}
        '''
        value = GoogleKmsCryptoKeyVersionTemplate(
            algorithm=algorithm, protection_level=protection_level
        )

        return typing.cast(None, jsii.invoke(self, "putVersionTemplate", [value]))

    @jsii.member(jsii_name="resetDestroyScheduledDuration")
    def reset_destroy_scheduled_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestroyScheduledDuration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportOnly")
    def reset_import_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportOnly", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPurpose")
    def reset_purpose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurpose", []))

    @jsii.member(jsii_name="resetRotationPeriod")
    def reset_rotation_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationPeriod", []))

    @jsii.member(jsii_name="resetSkipInitialVersionCreation")
    def reset_skip_initial_version_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipInitialVersionCreation", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersionTemplate")
    def reset_version_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionTemplate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleKmsCryptoKeyTimeoutsOutputReference":
        return typing.cast("GoogleKmsCryptoKeyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="versionTemplate")
    def version_template(self) -> "GoogleKmsCryptoKeyVersionTemplateOutputReference":
        return typing.cast("GoogleKmsCryptoKeyVersionTemplateOutputReference", jsii.get(self, "versionTemplate"))

    @builtins.property
    @jsii.member(jsii_name="destroyScheduledDurationInput")
    def destroy_scheduled_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destroyScheduledDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importOnlyInput")
    def import_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "importOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="keyRingInput")
    def key_ring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyRingInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="purposeInput")
    def purpose_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "purposeInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationPeriodInput")
    def rotation_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="skipInitialVersionCreationInput")
    def skip_initial_version_creation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipInitialVersionCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleKmsCryptoKeyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleKmsCryptoKeyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionTemplateInput")
    def version_template_input(
        self,
    ) -> typing.Optional["GoogleKmsCryptoKeyVersionTemplate"]:
        return typing.cast(typing.Optional["GoogleKmsCryptoKeyVersionTemplate"], jsii.get(self, "versionTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destroyScheduledDuration"))

    @destroy_scheduled_duration.setter
    def destroy_scheduled_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "destroy_scheduled_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destroyScheduledDuration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importOnly")
    def import_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "importOnly"))

    @import_only.setter
    def import_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "import_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importOnly", value)

    @builtins.property
    @jsii.member(jsii_name="keyRing")
    def key_ring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyRing"))

    @key_ring.setter
    def key_ring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "key_ring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyRing", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="purpose")
    def purpose(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "purpose"))

    @purpose.setter
    def purpose(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "purpose").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purpose", value)

    @builtins.property
    @jsii.member(jsii_name="rotationPeriod")
    def rotation_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationPeriod"))

    @rotation_period.setter
    def rotation_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "rotation_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="skipInitialVersionCreation")
    def skip_initial_version_creation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipInitialVersionCreation"))

    @skip_initial_version_creation.setter
    def skip_initial_version_creation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKey, "skip_initial_version_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipInitialVersionCreation", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key_ring": "keyRing",
        "name": "name",
        "destroy_scheduled_duration": "destroyScheduledDuration",
        "id": "id",
        "import_only": "importOnly",
        "labels": "labels",
        "purpose": "purpose",
        "rotation_period": "rotationPeriod",
        "skip_initial_version_creation": "skipInitialVersionCreation",
        "timeouts": "timeouts",
        "version_template": "versionTemplate",
    },
)
class GoogleKmsCryptoKeyConfig(cdktf.TerraformMetaArguments):
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
        key_ring: builtins.str,
        name: builtins.str,
        destroy_scheduled_duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        import_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        purpose: typing.Optional[builtins.str] = None,
        rotation_period: typing.Optional[builtins.str] = None,
        skip_initial_version_creation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleKmsCryptoKeyTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_template: typing.Optional[typing.Union["GoogleKmsCryptoKeyVersionTemplate", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key_ring: The KeyRing that this key belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#key_ring GoogleKmsCryptoKey#key_ring}
        :param name: The resource name for the CryptoKey. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#name GoogleKmsCryptoKey#name}
        :param destroy_scheduled_duration: The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#destroy_scheduled_duration GoogleKmsCryptoKey#destroy_scheduled_duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#id GoogleKmsCryptoKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_only: Whether this key may contain imported versions only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#import_only GoogleKmsCryptoKey#import_only}
        :param labels: Labels with user-defined metadata to apply to this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#labels GoogleKmsCryptoKey#labels}
        :param purpose: The immutable purpose of this CryptoKey. See the `purpose reference <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose>`_ for possible inputs. Default value: "ENCRYPT_DECRYPT" Possible values: ["ENCRYPT_DECRYPT", "ASYMMETRIC_SIGN", "ASYMMETRIC_DECRYPT", "MAC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#purpose GoogleKmsCryptoKey#purpose}
        :param rotation_period: Every time this period passes, generate a new CryptoKeyVersion and set it as the primary. The first rotation will take place after the specified period. The rotation period has the format of a decimal number with up to 9 fractional digits, followed by the letter 's' (seconds). It must be greater than a day (ie, 86400). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#rotation_period GoogleKmsCryptoKey#rotation_period}
        :param skip_initial_version_creation: If set to true, the request will create a CryptoKey without any CryptoKeyVersions. You must use the 'google_kms_key_ring_import_job' resource to import the CryptoKeyVersion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#skip_initial_version_creation GoogleKmsCryptoKey#skip_initial_version_creation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#timeouts GoogleKmsCryptoKey#timeouts}
        :param version_template: version_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#version_template GoogleKmsCryptoKey#version_template}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleKmsCryptoKeyTimeouts(**timeouts)
        if isinstance(version_template, dict):
            version_template = GoogleKmsCryptoKeyVersionTemplate(**version_template)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsCryptoKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key_ring", value=key_ring, expected_type=type_hints["key_ring"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument destroy_scheduled_duration", value=destroy_scheduled_duration, expected_type=type_hints["destroy_scheduled_duration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument import_only", value=import_only, expected_type=type_hints["import_only"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument purpose", value=purpose, expected_type=type_hints["purpose"])
            check_type(argname="argument rotation_period", value=rotation_period, expected_type=type_hints["rotation_period"])
            check_type(argname="argument skip_initial_version_creation", value=skip_initial_version_creation, expected_type=type_hints["skip_initial_version_creation"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version_template", value=version_template, expected_type=type_hints["version_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_ring": key_ring,
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
        if destroy_scheduled_duration is not None:
            self._values["destroy_scheduled_duration"] = destroy_scheduled_duration
        if id is not None:
            self._values["id"] = id
        if import_only is not None:
            self._values["import_only"] = import_only
        if labels is not None:
            self._values["labels"] = labels
        if purpose is not None:
            self._values["purpose"] = purpose
        if rotation_period is not None:
            self._values["rotation_period"] = rotation_period
        if skip_initial_version_creation is not None:
            self._values["skip_initial_version_creation"] = skip_initial_version_creation
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version_template is not None:
            self._values["version_template"] = version_template

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
    def key_ring(self) -> builtins.str:
        '''The KeyRing that this key belongs to. Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#key_ring GoogleKmsCryptoKey#key_ring}
        '''
        result = self._values.get("key_ring")
        assert result is not None, "Required property 'key_ring' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The resource name for the CryptoKey.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#name GoogleKmsCryptoKey#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destroy_scheduled_duration(self) -> typing.Optional[builtins.str]:
        '''The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED.

        If not specified at creation time, the default duration is 24 hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#destroy_scheduled_duration GoogleKmsCryptoKey#destroy_scheduled_duration}
        '''
        result = self._values.get("destroy_scheduled_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#id GoogleKmsCryptoKey#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this key may contain imported versions only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#import_only GoogleKmsCryptoKey#import_only}
        '''
        result = self._values.get("import_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels with user-defined metadata to apply to this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#labels GoogleKmsCryptoKey#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def purpose(self) -> typing.Optional[builtins.str]:
        '''The immutable purpose of this CryptoKey.

        See the
        `purpose reference <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose>`_
        for possible inputs. Default value: "ENCRYPT_DECRYPT" Possible values: ["ENCRYPT_DECRYPT", "ASYMMETRIC_SIGN", "ASYMMETRIC_DECRYPT", "MAC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#purpose GoogleKmsCryptoKey#purpose}
        '''
        result = self._values.get("purpose")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation_period(self) -> typing.Optional[builtins.str]:
        '''Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.

        The first rotation will take place after the specified period. The rotation period has
        the format of a decimal number with up to 9 fractional digits, followed by the
        letter 's' (seconds). It must be greater than a day (ie, 86400).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#rotation_period GoogleKmsCryptoKey#rotation_period}
        '''
        result = self._values.get("rotation_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_initial_version_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the request will create a CryptoKey without any CryptoKeyVersions.

        You must use the 'google_kms_key_ring_import_job' resource to import the CryptoKeyVersion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#skip_initial_version_creation GoogleKmsCryptoKey#skip_initial_version_creation}
        '''
        result = self._values.get("skip_initial_version_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleKmsCryptoKeyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#timeouts GoogleKmsCryptoKey#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleKmsCryptoKeyTimeouts"], result)

    @builtins.property
    def version_template(self) -> typing.Optional["GoogleKmsCryptoKeyVersionTemplate"]:
        '''version_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#version_template GoogleKmsCryptoKey#version_template}
        '''
        result = self._values.get("version_template")
        return typing.cast(typing.Optional["GoogleKmsCryptoKeyVersionTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsCryptoKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKeyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleKmsCryptoKeyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#create GoogleKmsCryptoKey#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#delete GoogleKmsCryptoKey#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#update GoogleKmsCryptoKey#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsCryptoKeyTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#create GoogleKmsCryptoKey#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#delete GoogleKmsCryptoKey#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#update GoogleKmsCryptoKey#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsCryptoKeyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsCryptoKeyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKeyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsCryptoKeyTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleKmsCryptoKeyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleKmsCryptoKeyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleKmsCryptoKeyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKeyVersionTemplate",
    jsii_struct_bases=[],
    name_mapping={"algorithm": "algorithm", "protection_level": "protectionLevel"},
)
class GoogleKmsCryptoKeyVersionTemplate:
    def __init__(
        self,
        *,
        algorithm: builtins.str,
        protection_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm to use when creating a version based on this template. See the `algorithm reference <https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm>`_ for possible inputs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#algorithm GoogleKmsCryptoKey#algorithm}
        :param protection_level: The protection level to use when creating a version based on this template. Possible values include "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC". Defaults to "SOFTWARE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#protection_level GoogleKmsCryptoKey#protection_level}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleKmsCryptoKeyVersionTemplate.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument protection_level", value=protection_level, expected_type=type_hints["protection_level"])
        self._values: typing.Dict[str, typing.Any] = {
            "algorithm": algorithm,
        }
        if protection_level is not None:
            self._values["protection_level"] = protection_level

    @builtins.property
    def algorithm(self) -> builtins.str:
        '''The algorithm to use when creating a version based on this template. See the `algorithm reference <https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm>`_ for possible inputs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#algorithm GoogleKmsCryptoKey#algorithm}
        '''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protection_level(self) -> typing.Optional[builtins.str]:
        '''The protection level to use when creating a version based on this template.

        Possible values include "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC". Defaults to "SOFTWARE".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_kms_crypto_key#protection_level GoogleKmsCryptoKey#protection_level}
        '''
        result = self._values.get("protection_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleKmsCryptoKeyVersionTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleKmsCryptoKeyVersionTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleKmsCryptoKey.GoogleKmsCryptoKeyVersionTemplateOutputReference",
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
            type_hints = typing.get_type_hints(GoogleKmsCryptoKeyVersionTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProtectionLevel")
    def reset_protection_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectionLevel", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionLevelInput")
    def protection_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectionLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyVersionTemplateOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="protectionLevel")
    def protection_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectionLevel"))

    @protection_level.setter
    def protection_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyVersionTemplateOutputReference, "protection_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectionLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleKmsCryptoKeyVersionTemplate]:
        return typing.cast(typing.Optional[GoogleKmsCryptoKeyVersionTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleKmsCryptoKeyVersionTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleKmsCryptoKeyVersionTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleKmsCryptoKey",
    "GoogleKmsCryptoKeyConfig",
    "GoogleKmsCryptoKeyTimeouts",
    "GoogleKmsCryptoKeyTimeoutsOutputReference",
    "GoogleKmsCryptoKeyVersionTemplate",
    "GoogleKmsCryptoKeyVersionTemplateOutputReference",
]

publication.publish()
