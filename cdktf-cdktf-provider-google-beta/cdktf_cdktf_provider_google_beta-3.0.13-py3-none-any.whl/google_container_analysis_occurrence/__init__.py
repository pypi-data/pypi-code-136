'''
# `google_container_analysis_occurrence`

Refer to the Terraform Registory for docs: [`google_container_analysis_occurrence`](https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence).
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


class GoogleContainerAnalysisOccurrence(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrence",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence google_container_analysis_occurrence}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        attestation: typing.Union["GoogleContainerAnalysisOccurrenceAttestation", typing.Dict[str, typing.Any]],
        note_name: builtins.str,
        resource_uri: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        remediation: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAnalysisOccurrenceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence google_container_analysis_occurrence} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param attestation: attestation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#attestation GoogleContainerAnalysisOccurrence#attestation}
        :param note_name: The analysis note associated with this occurrence, in the form of projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a filter in list requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#note_name GoogleContainerAnalysisOccurrence#note_name}
        :param resource_uri: Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, https://gcr.io/project/image@sha256:123abc for a Docker image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#resource_uri GoogleContainerAnalysisOccurrence#resource_uri}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#id GoogleContainerAnalysisOccurrence#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#project GoogleContainerAnalysisOccurrence#project}.
        :param remediation: A description of actions that can be taken to remedy the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#remediation GoogleContainerAnalysisOccurrence#remediation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#timeouts GoogleContainerAnalysisOccurrence#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrence.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleContainerAnalysisOccurrenceConfig(
            attestation=attestation,
            note_name=note_name,
            resource_uri=resource_uri,
            id=id,
            project=project,
            remediation=remediation,
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

    @jsii.member(jsii_name="putAttestation")
    def put_attestation(
        self,
        *,
        serialized_payload: builtins.str,
        signatures: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisOccurrenceAttestationSignatures", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param serialized_payload: The serialized payload that is verified by one or more signatures. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#serialized_payload GoogleContainerAnalysisOccurrence#serialized_payload}
        :param signatures: signatures block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#signatures GoogleContainerAnalysisOccurrence#signatures}
        '''
        value = GoogleContainerAnalysisOccurrenceAttestation(
            serialized_payload=serialized_payload, signatures=signatures
        )

        return typing.cast(None, jsii.invoke(self, "putAttestation", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#create GoogleContainerAnalysisOccurrence#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#delete GoogleContainerAnalysisOccurrence#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#update GoogleContainerAnalysisOccurrence#update}.
        '''
        value = GoogleContainerAnalysisOccurrenceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRemediation")
    def reset_remediation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemediation", []))

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
    def attestation(
        self,
    ) -> "GoogleContainerAnalysisOccurrenceAttestationOutputReference":
        return typing.cast("GoogleContainerAnalysisOccurrenceAttestationOutputReference", jsii.get(self, "attestation"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleContainerAnalysisOccurrenceTimeoutsOutputReference":
        return typing.cast("GoogleContainerAnalysisOccurrenceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="attestationInput")
    def attestation_input(
        self,
    ) -> typing.Optional["GoogleContainerAnalysisOccurrenceAttestation"]:
        return typing.cast(typing.Optional["GoogleContainerAnalysisOccurrenceAttestation"], jsii.get(self, "attestationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="noteNameInput")
    def note_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteNameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="remediationInput")
    def remediation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remediationInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceUriInput")
    def resource_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleContainerAnalysisOccurrenceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleContainerAnalysisOccurrenceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrence, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="noteName")
    def note_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noteName"))

    @note_name.setter
    def note_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrence, "note_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteName", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrence, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="remediation")
    def remediation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remediation"))

    @remediation.setter
    def remediation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrence, "remediation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remediation", value)

    @builtins.property
    @jsii.member(jsii_name="resourceUri")
    def resource_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceUri"))

    @resource_uri.setter
    def resource_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrence, "resource_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceUri", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceAttestation",
    jsii_struct_bases=[],
    name_mapping={
        "serialized_payload": "serializedPayload",
        "signatures": "signatures",
    },
)
class GoogleContainerAnalysisOccurrenceAttestation:
    def __init__(
        self,
        *,
        serialized_payload: builtins.str,
        signatures: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisOccurrenceAttestationSignatures", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param serialized_payload: The serialized payload that is verified by one or more signatures. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#serialized_payload GoogleContainerAnalysisOccurrence#serialized_payload}
        :param signatures: signatures block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#signatures GoogleContainerAnalysisOccurrence#signatures}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestation.__init__)
            check_type(argname="argument serialized_payload", value=serialized_payload, expected_type=type_hints["serialized_payload"])
            check_type(argname="argument signatures", value=signatures, expected_type=type_hints["signatures"])
        self._values: typing.Dict[str, typing.Any] = {
            "serialized_payload": serialized_payload,
            "signatures": signatures,
        }

    @builtins.property
    def serialized_payload(self) -> builtins.str:
        '''The serialized payload that is verified by one or more signatures. A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#serialized_payload GoogleContainerAnalysisOccurrence#serialized_payload}
        '''
        result = self._values.get("serialized_payload")
        assert result is not None, "Required property 'serialized_payload' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signatures(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisOccurrenceAttestationSignatures"]]:
        '''signatures block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#signatures GoogleContainerAnalysisOccurrence#signatures}
        '''
        result = self._values.get("signatures")
        assert result is not None, "Required property 'signatures' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisOccurrenceAttestationSignatures"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisOccurrenceAttestation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisOccurrenceAttestationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceAttestationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSignatures")
    def put_signatures(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisOccurrenceAttestationSignatures", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationOutputReference.put_signatures)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSignatures", [value]))

    @builtins.property
    @jsii.member(jsii_name="signatures")
    def signatures(
        self,
    ) -> "GoogleContainerAnalysisOccurrenceAttestationSignaturesList":
        return typing.cast("GoogleContainerAnalysisOccurrenceAttestationSignaturesList", jsii.get(self, "signatures"))

    @builtins.property
    @jsii.member(jsii_name="serializedPayloadInput")
    def serialized_payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serializedPayloadInput"))

    @builtins.property
    @jsii.member(jsii_name="signaturesInput")
    def signatures_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisOccurrenceAttestationSignatures"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisOccurrenceAttestationSignatures"]]], jsii.get(self, "signaturesInput"))

    @builtins.property
    @jsii.member(jsii_name="serializedPayload")
    def serialized_payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serializedPayload"))

    @serialized_payload.setter
    def serialized_payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationOutputReference, "serialized_payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serializedPayload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAnalysisOccurrenceAttestation]:
        return typing.cast(typing.Optional[GoogleContainerAnalysisOccurrenceAttestation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAnalysisOccurrenceAttestation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceAttestationSignatures",
    jsii_struct_bases=[],
    name_mapping={"public_key_id": "publicKeyId", "signature": "signature"},
)
class GoogleContainerAnalysisOccurrenceAttestationSignatures:
    def __init__(
        self,
        *,
        public_key_id: builtins.str,
        signature: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_key_id: The identifier for the public key that verifies this signature. MUST be an RFC3986 conformant URI. * When possible, the key id should be an immutable reference, such as a cryptographic digest. Examples of valid values: OpenPGP V4 public key fingerprint. See https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr for more details on this scheme. 'openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA' RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization): "ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#public_key_id GoogleContainerAnalysisOccurrence#public_key_id}
        :param signature: The content of the signature, an opaque bytestring. The payload that this signature verifies MUST be unambiguously provided with the Signature during verification. A wrapper message might provide the payload explicitly. Alternatively, a message might have a canonical serialization that can always be unambiguously computed to derive the payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#signature GoogleContainerAnalysisOccurrence#signature}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationSignatures.__init__)
            check_type(argname="argument public_key_id", value=public_key_id, expected_type=type_hints["public_key_id"])
            check_type(argname="argument signature", value=signature, expected_type=type_hints["signature"])
        self._values: typing.Dict[str, typing.Any] = {
            "public_key_id": public_key_id,
        }
        if signature is not None:
            self._values["signature"] = signature

    @builtins.property
    def public_key_id(self) -> builtins.str:
        '''The identifier for the public key that verifies this signature.

        MUST be an RFC3986 conformant
        URI. * When possible, the key id should be an
        immutable reference, such as a cryptographic digest.
        Examples of valid values:

        OpenPGP V4 public key fingerprint. See https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr
        for more details on this scheme.
        'openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA'
        RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):
        "ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#public_key_id GoogleContainerAnalysisOccurrence#public_key_id}
        '''
        result = self._values.get("public_key_id")
        assert result is not None, "Required property 'public_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signature(self) -> typing.Optional[builtins.str]:
        '''The content of the signature, an opaque bytestring.

        The payload that this signature verifies MUST be
        unambiguously provided with the Signature during
        verification. A wrapper message might provide the
        payload explicitly. Alternatively, a message might
        have a canonical serialization that can always be
        unambiguously computed to derive the payload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#signature GoogleContainerAnalysisOccurrence#signature}
        '''
        result = self._values.get("signature")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisOccurrenceAttestationSignatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisOccurrenceAttestationSignaturesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceAttestationSignaturesList",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationSignaturesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationSignaturesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisOccurrenceAttestationSignatures]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisOccurrenceAttestationSignatures]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisOccurrenceAttestationSignatures]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSignature")
    def reset_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignature", []))

    @builtins.property
    @jsii.member(jsii_name="publicKeyIdInput")
    def public_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureInput")
    def signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyId")
    def public_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyId"))

    @public_key_id.setter
    def public_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference, "public_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="signature")
    def signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signature"))

    @signature.setter
    def signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference, "signature").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signature", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceAttestationSignatures, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceAttestationSignatures, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceAttestationSignatures, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "attestation": "attestation",
        "note_name": "noteName",
        "resource_uri": "resourceUri",
        "id": "id",
        "project": "project",
        "remediation": "remediation",
        "timeouts": "timeouts",
    },
)
class GoogleContainerAnalysisOccurrenceConfig(cdktf.TerraformMetaArguments):
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
        attestation: typing.Union[GoogleContainerAnalysisOccurrenceAttestation, typing.Dict[str, typing.Any]],
        note_name: builtins.str,
        resource_uri: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        remediation: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAnalysisOccurrenceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param attestation: attestation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#attestation GoogleContainerAnalysisOccurrence#attestation}
        :param note_name: The analysis note associated with this occurrence, in the form of projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a filter in list requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#note_name GoogleContainerAnalysisOccurrence#note_name}
        :param resource_uri: Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, https://gcr.io/project/image@sha256:123abc for a Docker image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#resource_uri GoogleContainerAnalysisOccurrence#resource_uri}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#id GoogleContainerAnalysisOccurrence#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#project GoogleContainerAnalysisOccurrence#project}.
        :param remediation: A description of actions that can be taken to remedy the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#remediation GoogleContainerAnalysisOccurrence#remediation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#timeouts GoogleContainerAnalysisOccurrence#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(attestation, dict):
            attestation = GoogleContainerAnalysisOccurrenceAttestation(**attestation)
        if isinstance(timeouts, dict):
            timeouts = GoogleContainerAnalysisOccurrenceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument attestation", value=attestation, expected_type=type_hints["attestation"])
            check_type(argname="argument note_name", value=note_name, expected_type=type_hints["note_name"])
            check_type(argname="argument resource_uri", value=resource_uri, expected_type=type_hints["resource_uri"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument remediation", value=remediation, expected_type=type_hints["remediation"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "attestation": attestation,
            "note_name": note_name,
            "resource_uri": resource_uri,
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
        if project is not None:
            self._values["project"] = project
        if remediation is not None:
            self._values["remediation"] = remediation
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
    def attestation(self) -> GoogleContainerAnalysisOccurrenceAttestation:
        '''attestation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#attestation GoogleContainerAnalysisOccurrence#attestation}
        '''
        result = self._values.get("attestation")
        assert result is not None, "Required property 'attestation' is missing"
        return typing.cast(GoogleContainerAnalysisOccurrenceAttestation, result)

    @builtins.property
    def note_name(self) -> builtins.str:
        '''The analysis note associated with this occurrence, in the form of projects/[PROJECT]/notes/[NOTE_ID].

        This field can be used as a
        filter in list requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#note_name GoogleContainerAnalysisOccurrence#note_name}
        '''
        result = self._values.get("note_name")
        assert result is not None, "Required property 'note_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_uri(self) -> builtins.str:
        '''Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, https://gcr.io/project/image@sha256:123abc for a Docker image.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#resource_uri GoogleContainerAnalysisOccurrence#resource_uri}
        '''
        result = self._values.get("resource_uri")
        assert result is not None, "Required property 'resource_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#id GoogleContainerAnalysisOccurrence#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#project GoogleContainerAnalysisOccurrence#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remediation(self) -> typing.Optional[builtins.str]:
        '''A description of actions that can be taken to remedy the note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#remediation GoogleContainerAnalysisOccurrence#remediation}
        '''
        result = self._values.get("remediation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleContainerAnalysisOccurrenceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#timeouts GoogleContainerAnalysisOccurrence#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleContainerAnalysisOccurrenceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisOccurrenceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleContainerAnalysisOccurrenceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#create GoogleContainerAnalysisOccurrence#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#delete GoogleContainerAnalysisOccurrence#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#update GoogleContainerAnalysisOccurrence#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#create GoogleContainerAnalysisOccurrence#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#delete GoogleContainerAnalysisOccurrence#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_occurrence#update GoogleContainerAnalysisOccurrence#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisOccurrenceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisOccurrenceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisOccurrence.GoogleContainerAnalysisOccurrenceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisOccurrenceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAnalysisOccurrenceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisOccurrenceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleContainerAnalysisOccurrence",
    "GoogleContainerAnalysisOccurrenceAttestation",
    "GoogleContainerAnalysisOccurrenceAttestationOutputReference",
    "GoogleContainerAnalysisOccurrenceAttestationSignatures",
    "GoogleContainerAnalysisOccurrenceAttestationSignaturesList",
    "GoogleContainerAnalysisOccurrenceAttestationSignaturesOutputReference",
    "GoogleContainerAnalysisOccurrenceConfig",
    "GoogleContainerAnalysisOccurrenceTimeouts",
    "GoogleContainerAnalysisOccurrenceTimeoutsOutputReference",
]

publication.publish()
