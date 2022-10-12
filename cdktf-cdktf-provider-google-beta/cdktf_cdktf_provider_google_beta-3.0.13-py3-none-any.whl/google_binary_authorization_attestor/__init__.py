'''
# `google_binary_authorization_attestor`

Refer to the Terraform Registory for docs: [`google_binary_authorization_attestor`](https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor).
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


class GoogleBinaryAuthorizationAttestor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor google_binary_authorization_attestor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        attestation_authority_note: typing.Union["GoogleBinaryAuthorizationAttestorAttestationAuthorityNote", typing.Dict[str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBinaryAuthorizationAttestorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor google_binary_authorization_attestor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param attestation_authority_note: attestation_authority_note block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#attestation_authority_note GoogleBinaryAuthorizationAttestor#attestation_authority_note}
        :param name: The resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#name GoogleBinaryAuthorizationAttestor#name}
        :param description: A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#description GoogleBinaryAuthorizationAttestor#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#id GoogleBinaryAuthorizationAttestor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#project GoogleBinaryAuthorizationAttestor#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#timeouts GoogleBinaryAuthorizationAttestor#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBinaryAuthorizationAttestorConfig(
            attestation_authority_note=attestation_authority_note,
            name=name,
            description=description,
            id=id,
            project=project,
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

    @jsii.member(jsii_name="putAttestationAuthorityNote")
    def put_attestation_authority_note(
        self,
        *,
        note_reference: builtins.str,
        public_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param note_reference: The resource name of a ATTESTATION_AUTHORITY Note, created by the user. If the Note is in a different project from the Attestor, it should be specified in the format 'projects/*/notes/*' (or the legacy 'providers/*/notes/*'). This field may not be updated. An attestation by this attestor is stored as a Container Analysis ATTESTATION_AUTHORITY Occurrence that names a container image and that links to this Note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#note_reference GoogleBinaryAuthorizationAttestor#note_reference}
        :param public_keys: public_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_keys GoogleBinaryAuthorizationAttestor#public_keys}
        '''
        value = GoogleBinaryAuthorizationAttestorAttestationAuthorityNote(
            note_reference=note_reference, public_keys=public_keys
        )

        return typing.cast(None, jsii.invoke(self, "putAttestationAuthorityNote", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#create GoogleBinaryAuthorizationAttestor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#delete GoogleBinaryAuthorizationAttestor#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#update GoogleBinaryAuthorizationAttestor#update}.
        '''
        value = GoogleBinaryAuthorizationAttestorTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="attestationAuthorityNote")
    def attestation_authority_note(
        self,
    ) -> "GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference":
        return typing.cast("GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference", jsii.get(self, "attestationAuthorityNote"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleBinaryAuthorizationAttestorTimeoutsOutputReference":
        return typing.cast("GoogleBinaryAuthorizationAttestorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="attestationAuthorityNoteInput")
    def attestation_authority_note_input(
        self,
    ) -> typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNote"]:
        return typing.cast(typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNote"], jsii.get(self, "attestationAuthorityNoteInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleBinaryAuthorizationAttestorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleBinaryAuthorizationAttestorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestor, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestor, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNote",
    jsii_struct_bases=[],
    name_mapping={"note_reference": "noteReference", "public_keys": "publicKeys"},
)
class GoogleBinaryAuthorizationAttestorAttestationAuthorityNote:
    def __init__(
        self,
        *,
        note_reference: builtins.str,
        public_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param note_reference: The resource name of a ATTESTATION_AUTHORITY Note, created by the user. If the Note is in a different project from the Attestor, it should be specified in the format 'projects/*/notes/*' (or the legacy 'providers/*/notes/*'). This field may not be updated. An attestation by this attestor is stored as a Container Analysis ATTESTATION_AUTHORITY Occurrence that names a container image and that links to this Note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#note_reference GoogleBinaryAuthorizationAttestor#note_reference}
        :param public_keys: public_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_keys GoogleBinaryAuthorizationAttestor#public_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNote.__init__)
            check_type(argname="argument note_reference", value=note_reference, expected_type=type_hints["note_reference"])
            check_type(argname="argument public_keys", value=public_keys, expected_type=type_hints["public_keys"])
        self._values: typing.Dict[str, typing.Any] = {
            "note_reference": note_reference,
        }
        if public_keys is not None:
            self._values["public_keys"] = public_keys

    @builtins.property
    def note_reference(self) -> builtins.str:
        '''The resource name of a ATTESTATION_AUTHORITY Note, created by the user.

        If the Note is in a different project from the Attestor, it
        should be specified in the format 'projects/*/notes/*' (or the legacy
        'providers/*/notes/*'). This field may not be updated.
        An attestation by this attestor is stored as a Container Analysis
        ATTESTATION_AUTHORITY Occurrence that names a container image
        and that links to this Note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#note_reference GoogleBinaryAuthorizationAttestor#note_reference}
        '''
        result = self._values.get("note_reference")
        assert result is not None, "Required property 'note_reference' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_keys(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys"]]]:
        '''public_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_keys GoogleBinaryAuthorizationAttestor#public_keys}
        '''
        result = self._values.get("public_keys")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBinaryAuthorizationAttestorAttestationAuthorityNote(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPublicKeys")
    def put_public_keys(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference.put_public_keys)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPublicKeys", [value]))

    @jsii.member(jsii_name="resetPublicKeys")
    def reset_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKeys", []))

    @builtins.property
    @jsii.member(jsii_name="delegationServiceAccountEmail")
    def delegation_service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delegationServiceAccountEmail"))

    @builtins.property
    @jsii.member(jsii_name="publicKeys")
    def public_keys(
        self,
    ) -> "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList":
        return typing.cast("GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList", jsii.get(self, "publicKeys"))

    @builtins.property
    @jsii.member(jsii_name="noteReferenceInput")
    def note_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeysInput")
    def public_keys_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys"]]], jsii.get(self, "publicKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="noteReference")
    def note_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noteReference"))

    @note_reference.setter
    def note_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference, "note_reference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNote]:
        return typing.cast(typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNote], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNote],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys",
    jsii_struct_bases=[],
    name_mapping={
        "ascii_armored_pgp_public_key": "asciiArmoredPgpPublicKey",
        "comment": "comment",
        "id": "id",
        "pkix_public_key": "pkixPublicKey",
    },
)
class GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys:
    def __init__(
        self,
        *,
        ascii_armored_pgp_public_key: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        pkix_public_key: typing.Optional[typing.Union["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ascii_armored_pgp_public_key: ASCII-armored representation of a PGP public key, as the entire output by the command 'gpg --export --armor foo@example.com' (either LF or CRLF line endings). When using this field, id should be left blank. The BinAuthz API handlers will calculate the ID and fill it in automatically. BinAuthz computes this ID as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If id is provided by the caller, it will be overwritten by the API-calculated ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#ascii_armored_pgp_public_key GoogleBinaryAuthorizationAttestor#ascii_armored_pgp_public_key}
        :param comment: A descriptive comment. This field may be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#comment GoogleBinaryAuthorizationAttestor#comment}
        :param id: The ID of this public key. Signatures verified by BinAuthz must include the ID of the public key that can be used to verify them, and that ID must match the contents of this field exactly. Additional restrictions on this field can be imposed based on which public key type is encapsulated. See the documentation on publicKey cases below for details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#id GoogleBinaryAuthorizationAttestor#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pkix_public_key: pkix_public_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#pkix_public_key GoogleBinaryAuthorizationAttestor#pkix_public_key}
        '''
        if isinstance(pkix_public_key, dict):
            pkix_public_key = GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey(**pkix_public_key)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys.__init__)
            check_type(argname="argument ascii_armored_pgp_public_key", value=ascii_armored_pgp_public_key, expected_type=type_hints["ascii_armored_pgp_public_key"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pkix_public_key", value=pkix_public_key, expected_type=type_hints["pkix_public_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ascii_armored_pgp_public_key is not None:
            self._values["ascii_armored_pgp_public_key"] = ascii_armored_pgp_public_key
        if comment is not None:
            self._values["comment"] = comment
        if id is not None:
            self._values["id"] = id
        if pkix_public_key is not None:
            self._values["pkix_public_key"] = pkix_public_key

    @builtins.property
    def ascii_armored_pgp_public_key(self) -> typing.Optional[builtins.str]:
        '''ASCII-armored representation of a PGP public key, as the entire output by the command 'gpg --export --armor foo@example.com' (either LF or CRLF line endings). When using this field, id should be left blank. The BinAuthz API handlers will calculate the ID and fill it in automatically. BinAuthz computes this ID as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If id is provided by the caller, it will be overwritten by the API-calculated ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#ascii_armored_pgp_public_key GoogleBinaryAuthorizationAttestor#ascii_armored_pgp_public_key}
        '''
        result = self._values.get("ascii_armored_pgp_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A descriptive comment. This field may be updated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#comment GoogleBinaryAuthorizationAttestor#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''The ID of this public key.

        Signatures verified by BinAuthz
        must include the ID of the public key that can be used to
        verify them, and that ID must match the contents of this
        field exactly. Additional restrictions on this field can
        be imposed based on which public key type is encapsulated.
        See the documentation on publicKey cases below for details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#id GoogleBinaryAuthorizationAttestor#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pkix_public_key(
        self,
    ) -> typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey"]:
        '''pkix_public_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#pkix_public_key GoogleBinaryAuthorizationAttestor#pkix_public_key}
        '''
        result = self._values.get("pkix_public_key")
        return typing.cast(typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList",
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
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPkixPublicKey")
    def put_pkix_public_key(
        self,
        *,
        public_key_pem: typing.Optional[builtins.str] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_key_pem: A PEM-encoded public key, as described in 'https://tools.ietf.org/html/rfc7468#section-13'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_key_pem GoogleBinaryAuthorizationAttestor#public_key_pem}
        :param signature_algorithm: The signature algorithm used to verify a message against a signature using this key. These signature algorithm must match the structure and any object identifiers encoded in publicKeyPem (i.e. this algorithm must match that of the public key). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#signature_algorithm GoogleBinaryAuthorizationAttestor#signature_algorithm}
        '''
        value = GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey(
            public_key_pem=public_key_pem, signature_algorithm=signature_algorithm
        )

        return typing.cast(None, jsii.invoke(self, "putPkixPublicKey", [value]))

    @jsii.member(jsii_name="resetAsciiArmoredPgpPublicKey")
    def reset_ascii_armored_pgp_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsciiArmoredPgpPublicKey", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPkixPublicKey")
    def reset_pkix_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPkixPublicKey", []))

    @builtins.property
    @jsii.member(jsii_name="pkixPublicKey")
    def pkix_public_key(
        self,
    ) -> "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference":
        return typing.cast("GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference", jsii.get(self, "pkixPublicKey"))

    @builtins.property
    @jsii.member(jsii_name="asciiArmoredPgpPublicKeyInput")
    def ascii_armored_pgp_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "asciiArmoredPgpPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="pkixPublicKeyInput")
    def pkix_public_key_input(
        self,
    ) -> typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey"]:
        return typing.cast(typing.Optional["GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey"], jsii.get(self, "pkixPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="asciiArmoredPgpPublicKey")
    def ascii_armored_pgp_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "asciiArmoredPgpPublicKey"))

    @ascii_armored_pgp_public_key.setter
    def ascii_armored_pgp_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference, "ascii_armored_pgp_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asciiArmoredPgpPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey",
    jsii_struct_bases=[],
    name_mapping={
        "public_key_pem": "publicKeyPem",
        "signature_algorithm": "signatureAlgorithm",
    },
)
class GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey:
    def __init__(
        self,
        *,
        public_key_pem: typing.Optional[builtins.str] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_key_pem: A PEM-encoded public key, as described in 'https://tools.ietf.org/html/rfc7468#section-13'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_key_pem GoogleBinaryAuthorizationAttestor#public_key_pem}
        :param signature_algorithm: The signature algorithm used to verify a message against a signature using this key. These signature algorithm must match the structure and any object identifiers encoded in publicKeyPem (i.e. this algorithm must match that of the public key). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#signature_algorithm GoogleBinaryAuthorizationAttestor#signature_algorithm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey.__init__)
            check_type(argname="argument public_key_pem", value=public_key_pem, expected_type=type_hints["public_key_pem"])
            check_type(argname="argument signature_algorithm", value=signature_algorithm, expected_type=type_hints["signature_algorithm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if public_key_pem is not None:
            self._values["public_key_pem"] = public_key_pem
        if signature_algorithm is not None:
            self._values["signature_algorithm"] = signature_algorithm

    @builtins.property
    def public_key_pem(self) -> typing.Optional[builtins.str]:
        '''A PEM-encoded public key, as described in 'https://tools.ietf.org/html/rfc7468#section-13'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#public_key_pem GoogleBinaryAuthorizationAttestor#public_key_pem}
        '''
        result = self._values.get("public_key_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_algorithm(self) -> typing.Optional[builtins.str]:
        '''The signature algorithm used to verify a message against a signature using this key.

        These signature algorithm must
        match the structure and any object identifiers encoded in
        publicKeyPem (i.e. this algorithm must match that of the
        public key).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#signature_algorithm GoogleBinaryAuthorizationAttestor#signature_algorithm}
        '''
        result = self._values.get("signature_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPublicKeyPem")
    def reset_public_key_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKeyPem", []))

    @jsii.member(jsii_name="resetSignatureAlgorithm")
    def reset_signature_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithm", []))

    @builtins.property
    @jsii.member(jsii_name="publicKeyPemInput")
    def public_key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmInput")
    def signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyPem")
    def public_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKeyPem"))

    @public_key_pem.setter
    def public_key_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference, "public_key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyPem", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference, "signature_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey]:
        return typing.cast(typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "attestation_authority_note": "attestationAuthorityNote",
        "name": "name",
        "description": "description",
        "id": "id",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleBinaryAuthorizationAttestorConfig(cdktf.TerraformMetaArguments):
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
        attestation_authority_note: typing.Union[GoogleBinaryAuthorizationAttestorAttestationAuthorityNote, typing.Dict[str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBinaryAuthorizationAttestorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param attestation_authority_note: attestation_authority_note block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#attestation_authority_note GoogleBinaryAuthorizationAttestor#attestation_authority_note}
        :param name: The resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#name GoogleBinaryAuthorizationAttestor#name}
        :param description: A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#description GoogleBinaryAuthorizationAttestor#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#id GoogleBinaryAuthorizationAttestor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#project GoogleBinaryAuthorizationAttestor#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#timeouts GoogleBinaryAuthorizationAttestor#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(attestation_authority_note, dict):
            attestation_authority_note = GoogleBinaryAuthorizationAttestorAttestationAuthorityNote(**attestation_authority_note)
        if isinstance(timeouts, dict):
            timeouts = GoogleBinaryAuthorizationAttestorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument attestation_authority_note", value=attestation_authority_note, expected_type=type_hints["attestation_authority_note"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "attestation_authority_note": attestation_authority_note,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
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
    def attestation_authority_note(
        self,
    ) -> GoogleBinaryAuthorizationAttestorAttestationAuthorityNote:
        '''attestation_authority_note block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#attestation_authority_note GoogleBinaryAuthorizationAttestor#attestation_authority_note}
        '''
        result = self._values.get("attestation_authority_note")
        assert result is not None, "Required property 'attestation_authority_note' is missing"
        return typing.cast(GoogleBinaryAuthorizationAttestorAttestationAuthorityNote, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#name GoogleBinaryAuthorizationAttestor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#description GoogleBinaryAuthorizationAttestor#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#id GoogleBinaryAuthorizationAttestor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#project GoogleBinaryAuthorizationAttestor#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleBinaryAuthorizationAttestorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#timeouts GoogleBinaryAuthorizationAttestor#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleBinaryAuthorizationAttestorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBinaryAuthorizationAttestorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleBinaryAuthorizationAttestorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#create GoogleBinaryAuthorizationAttestor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#delete GoogleBinaryAuthorizationAttestor#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#update GoogleBinaryAuthorizationAttestor#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#create GoogleBinaryAuthorizationAttestor#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#delete GoogleBinaryAuthorizationAttestor#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_binary_authorization_attestor#update GoogleBinaryAuthorizationAttestor#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBinaryAuthorizationAttestorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBinaryAuthorizationAttestorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBinaryAuthorizationAttestor.GoogleBinaryAuthorizationAttestorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBinaryAuthorizationAttestorTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBinaryAuthorizationAttestorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBinaryAuthorizationAttestorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBinaryAuthorizationAttestor",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNote",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNoteOutputReference",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeys",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysList",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysOutputReference",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKey",
    "GoogleBinaryAuthorizationAttestorAttestationAuthorityNotePublicKeysPkixPublicKeyOutputReference",
    "GoogleBinaryAuthorizationAttestorConfig",
    "GoogleBinaryAuthorizationAttestorTimeouts",
    "GoogleBinaryAuthorizationAttestorTimeoutsOutputReference",
]

publication.publish()
