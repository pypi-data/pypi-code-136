'''
# `google_container_analysis_note`

Refer to the Terraform Registory for docs: [`google_container_analysis_note`](https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note).
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


class GoogleContainerAnalysisNote(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNote",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note google_container_analysis_note}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        attestation_authority: typing.Union["GoogleContainerAnalysisNoteAttestationAuthority", typing.Dict[str, typing.Any]],
        name: builtins.str,
        expiration_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        long_description: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        related_note_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        related_url: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisNoteRelatedUrl", typing.Dict[str, typing.Any]]]]] = None,
        short_description: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAnalysisNoteTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note google_container_analysis_note} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param attestation_authority: attestation_authority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#attestation_authority GoogleContainerAnalysisNote#attestation_authority}
        :param name: The name of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#name GoogleContainerAnalysisNote#name}
        :param expiration_time: Time of expiration for this note. Leave empty if note does not expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#expiration_time GoogleContainerAnalysisNote#expiration_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#id GoogleContainerAnalysisNote#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param long_description: A detailed description of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#long_description GoogleContainerAnalysisNote#long_description}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#project GoogleContainerAnalysisNote#project}.
        :param related_note_names: Names of other notes related to this note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_note_names GoogleContainerAnalysisNote#related_note_names}
        :param related_url: related_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_url GoogleContainerAnalysisNote#related_url}
        :param short_description: A one sentence description of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#short_description GoogleContainerAnalysisNote#short_description}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#timeouts GoogleContainerAnalysisNote#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNote.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleContainerAnalysisNoteConfig(
            attestation_authority=attestation_authority,
            name=name,
            expiration_time=expiration_time,
            id=id,
            long_description=long_description,
            project=project,
            related_note_names=related_note_names,
            related_url=related_url,
            short_description=short_description,
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

    @jsii.member(jsii_name="putAttestationAuthority")
    def put_attestation_authority(
        self,
        *,
        hint: typing.Union["GoogleContainerAnalysisNoteAttestationAuthorityHint", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param hint: hint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#hint GoogleContainerAnalysisNote#hint}
        '''
        value = GoogleContainerAnalysisNoteAttestationAuthority(hint=hint)

        return typing.cast(None, jsii.invoke(self, "putAttestationAuthority", [value]))

    @jsii.member(jsii_name="putRelatedUrl")
    def put_related_url(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisNoteRelatedUrl", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNote.put_related_url)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRelatedUrl", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#create GoogleContainerAnalysisNote#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#delete GoogleContainerAnalysisNote#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#update GoogleContainerAnalysisNote#update}.
        '''
        value = GoogleContainerAnalysisNoteTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLongDescription")
    def reset_long_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongDescription", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRelatedNoteNames")
    def reset_related_note_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelatedNoteNames", []))

    @jsii.member(jsii_name="resetRelatedUrl")
    def reset_related_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelatedUrl", []))

    @jsii.member(jsii_name="resetShortDescription")
    def reset_short_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShortDescription", []))

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
    @jsii.member(jsii_name="attestationAuthority")
    def attestation_authority(
        self,
    ) -> "GoogleContainerAnalysisNoteAttestationAuthorityOutputReference":
        return typing.cast("GoogleContainerAnalysisNoteAttestationAuthorityOutputReference", jsii.get(self, "attestationAuthority"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="relatedUrl")
    def related_url(self) -> "GoogleContainerAnalysisNoteRelatedUrlList":
        return typing.cast("GoogleContainerAnalysisNoteRelatedUrlList", jsii.get(self, "relatedUrl"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleContainerAnalysisNoteTimeoutsOutputReference":
        return typing.cast("GoogleContainerAnalysisNoteTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="attestationAuthorityInput")
    def attestation_authority_input(
        self,
    ) -> typing.Optional["GoogleContainerAnalysisNoteAttestationAuthority"]:
        return typing.cast(typing.Optional["GoogleContainerAnalysisNoteAttestationAuthority"], jsii.get(self, "attestationAuthorityInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="longDescriptionInput")
    def long_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "longDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="relatedNoteNamesInput")
    def related_note_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "relatedNoteNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="relatedUrlInput")
    def related_url_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisNoteRelatedUrl"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisNoteRelatedUrl"]]], jsii.get(self, "relatedUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="shortDescriptionInput")
    def short_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleContainerAnalysisNoteTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleContainerAnalysisNoteTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "expiration_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="longDescription")
    def long_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longDescription"))

    @long_description.setter
    def long_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "long_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longDescription", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="relatedNoteNames")
    def related_note_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "relatedNoteNames"))

    @related_note_names.setter
    def related_note_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "related_note_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relatedNoteNames", value)

    @builtins.property
    @jsii.member(jsii_name="shortDescription")
    def short_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shortDescription"))

    @short_description.setter
    def short_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNote, "short_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortDescription", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteAttestationAuthority",
    jsii_struct_bases=[],
    name_mapping={"hint": "hint"},
)
class GoogleContainerAnalysisNoteAttestationAuthority:
    def __init__(
        self,
        *,
        hint: typing.Union["GoogleContainerAnalysisNoteAttestationAuthorityHint", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param hint: hint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#hint GoogleContainerAnalysisNote#hint}
        '''
        if isinstance(hint, dict):
            hint = GoogleContainerAnalysisNoteAttestationAuthorityHint(**hint)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteAttestationAuthority.__init__)
            check_type(argname="argument hint", value=hint, expected_type=type_hints["hint"])
        self._values: typing.Dict[str, typing.Any] = {
            "hint": hint,
        }

    @builtins.property
    def hint(self) -> "GoogleContainerAnalysisNoteAttestationAuthorityHint":
        '''hint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#hint GoogleContainerAnalysisNote#hint}
        '''
        result = self._values.get("hint")
        assert result is not None, "Required property 'hint' is missing"
        return typing.cast("GoogleContainerAnalysisNoteAttestationAuthorityHint", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisNoteAttestationAuthority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteAttestationAuthorityHint",
    jsii_struct_bases=[],
    name_mapping={"human_readable_name": "humanReadableName"},
)
class GoogleContainerAnalysisNoteAttestationAuthorityHint:
    def __init__(self, *, human_readable_name: builtins.str) -> None:
        '''
        :param human_readable_name: The human readable name of this Attestation Authority, for example "qa". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#human_readable_name GoogleContainerAnalysisNote#human_readable_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteAttestationAuthorityHint.__init__)
            check_type(argname="argument human_readable_name", value=human_readable_name, expected_type=type_hints["human_readable_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "human_readable_name": human_readable_name,
        }

    @builtins.property
    def human_readable_name(self) -> builtins.str:
        '''The human readable name of this Attestation Authority, for example "qa".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#human_readable_name GoogleContainerAnalysisNote#human_readable_name}
        '''
        result = self._values.get("human_readable_name")
        assert result is not None, "Required property 'human_readable_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisNoteAttestationAuthorityHint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="humanReadableNameInput")
    def human_readable_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "humanReadableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="humanReadableName")
    def human_readable_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "humanReadableName"))

    @human_readable_name.setter
    def human_readable_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference, "human_readable_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "humanReadableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAnalysisNoteAttestationAuthorityHint]:
        return typing.cast(typing.Optional[GoogleContainerAnalysisNoteAttestationAuthorityHint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAnalysisNoteAttestationAuthorityHint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerAnalysisNoteAttestationAuthorityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteAttestationAuthorityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteAttestationAuthorityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHint")
    def put_hint(self, *, human_readable_name: builtins.str) -> None:
        '''
        :param human_readable_name: The human readable name of this Attestation Authority, for example "qa". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#human_readable_name GoogleContainerAnalysisNote#human_readable_name}
        '''
        value = GoogleContainerAnalysisNoteAttestationAuthorityHint(
            human_readable_name=human_readable_name
        )

        return typing.cast(None, jsii.invoke(self, "putHint", [value]))

    @builtins.property
    @jsii.member(jsii_name="hint")
    def hint(
        self,
    ) -> GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference:
        return typing.cast(GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference, jsii.get(self, "hint"))

    @builtins.property
    @jsii.member(jsii_name="hintInput")
    def hint_input(
        self,
    ) -> typing.Optional[GoogleContainerAnalysisNoteAttestationAuthorityHint]:
        return typing.cast(typing.Optional[GoogleContainerAnalysisNoteAttestationAuthorityHint], jsii.get(self, "hintInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerAnalysisNoteAttestationAuthority]:
        return typing.cast(typing.Optional[GoogleContainerAnalysisNoteAttestationAuthority], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerAnalysisNoteAttestationAuthority],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteAttestationAuthorityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "attestation_authority": "attestationAuthority",
        "name": "name",
        "expiration_time": "expirationTime",
        "id": "id",
        "long_description": "longDescription",
        "project": "project",
        "related_note_names": "relatedNoteNames",
        "related_url": "relatedUrl",
        "short_description": "shortDescription",
        "timeouts": "timeouts",
    },
)
class GoogleContainerAnalysisNoteConfig(cdktf.TerraformMetaArguments):
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
        attestation_authority: typing.Union[GoogleContainerAnalysisNoteAttestationAuthority, typing.Dict[str, typing.Any]],
        name: builtins.str,
        expiration_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        long_description: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        related_note_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        related_url: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleContainerAnalysisNoteRelatedUrl", typing.Dict[str, typing.Any]]]]] = None,
        short_description: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerAnalysisNoteTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param attestation_authority: attestation_authority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#attestation_authority GoogleContainerAnalysisNote#attestation_authority}
        :param name: The name of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#name GoogleContainerAnalysisNote#name}
        :param expiration_time: Time of expiration for this note. Leave empty if note does not expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#expiration_time GoogleContainerAnalysisNote#expiration_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#id GoogleContainerAnalysisNote#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param long_description: A detailed description of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#long_description GoogleContainerAnalysisNote#long_description}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#project GoogleContainerAnalysisNote#project}.
        :param related_note_names: Names of other notes related to this note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_note_names GoogleContainerAnalysisNote#related_note_names}
        :param related_url: related_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_url GoogleContainerAnalysisNote#related_url}
        :param short_description: A one sentence description of the note. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#short_description GoogleContainerAnalysisNote#short_description}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#timeouts GoogleContainerAnalysisNote#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(attestation_authority, dict):
            attestation_authority = GoogleContainerAnalysisNoteAttestationAuthority(**attestation_authority)
        if isinstance(timeouts, dict):
            timeouts = GoogleContainerAnalysisNoteTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument attestation_authority", value=attestation_authority, expected_type=type_hints["attestation_authority"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument long_description", value=long_description, expected_type=type_hints["long_description"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument related_note_names", value=related_note_names, expected_type=type_hints["related_note_names"])
            check_type(argname="argument related_url", value=related_url, expected_type=type_hints["related_url"])
            check_type(argname="argument short_description", value=short_description, expected_type=type_hints["short_description"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "attestation_authority": attestation_authority,
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
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if id is not None:
            self._values["id"] = id
        if long_description is not None:
            self._values["long_description"] = long_description
        if project is not None:
            self._values["project"] = project
        if related_note_names is not None:
            self._values["related_note_names"] = related_note_names
        if related_url is not None:
            self._values["related_url"] = related_url
        if short_description is not None:
            self._values["short_description"] = short_description
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
    def attestation_authority(self) -> GoogleContainerAnalysisNoteAttestationAuthority:
        '''attestation_authority block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#attestation_authority GoogleContainerAnalysisNote#attestation_authority}
        '''
        result = self._values.get("attestation_authority")
        assert result is not None, "Required property 'attestation_authority' is missing"
        return typing.cast(GoogleContainerAnalysisNoteAttestationAuthority, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#name GoogleContainerAnalysisNote#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[builtins.str]:
        '''Time of expiration for this note. Leave empty if note does not expire.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#expiration_time GoogleContainerAnalysisNote#expiration_time}
        '''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#id GoogleContainerAnalysisNote#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_description(self) -> typing.Optional[builtins.str]:
        '''A detailed description of the note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#long_description GoogleContainerAnalysisNote#long_description}
        '''
        result = self._values.get("long_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#project GoogleContainerAnalysisNote#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def related_note_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of other notes related to this note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_note_names GoogleContainerAnalysisNote#related_note_names}
        '''
        result = self._values.get("related_note_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def related_url(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisNoteRelatedUrl"]]]:
        '''related_url block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#related_url GoogleContainerAnalysisNote#related_url}
        '''
        result = self._values.get("related_url")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleContainerAnalysisNoteRelatedUrl"]]], result)

    @builtins.property
    def short_description(self) -> typing.Optional[builtins.str]:
        '''A one sentence description of the note.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#short_description GoogleContainerAnalysisNote#short_description}
        '''
        result = self._values.get("short_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleContainerAnalysisNoteTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#timeouts GoogleContainerAnalysisNote#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleContainerAnalysisNoteTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisNoteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteRelatedUrl",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "label": "label"},
)
class GoogleContainerAnalysisNoteRelatedUrl:
    def __init__(
        self,
        *,
        url: builtins.str,
        label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Specific URL associated with the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#url GoogleContainerAnalysisNote#url}
        :param label: Label to describe usage of the URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#label GoogleContainerAnalysisNote#label}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteRelatedUrl.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if label is not None:
            self._values["label"] = label

    @builtins.property
    def url(self) -> builtins.str:
        '''Specific URL associated with the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#url GoogleContainerAnalysisNote#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label to describe usage of the URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#label GoogleContainerAnalysisNote#label}
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisNoteRelatedUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisNoteRelatedUrlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteRelatedUrlList",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteRelatedUrlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerAnalysisNoteRelatedUrlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteRelatedUrlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerAnalysisNoteRelatedUrlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisNoteRelatedUrl]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisNoteRelatedUrl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleContainerAnalysisNoteRelatedUrl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerAnalysisNoteRelatedUrlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteRelatedUrlOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteRelatedUrlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAnalysisNoteRelatedUrl, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAnalysisNoteRelatedUrl, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAnalysisNoteRelatedUrl, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteRelatedUrlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleContainerAnalysisNoteTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#create GoogleContainerAnalysisNote#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#delete GoogleContainerAnalysisNote#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#update GoogleContainerAnalysisNote#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#create GoogleContainerAnalysisNote#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#delete GoogleContainerAnalysisNote#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_analysis_note#update GoogleContainerAnalysisNote#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerAnalysisNoteTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerAnalysisNoteTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerAnalysisNote.GoogleContainerAnalysisNoteTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleContainerAnalysisNoteTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerAnalysisNoteTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerAnalysisNoteTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerAnalysisNoteTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleContainerAnalysisNoteTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleContainerAnalysisNote",
    "GoogleContainerAnalysisNoteAttestationAuthority",
    "GoogleContainerAnalysisNoteAttestationAuthorityHint",
    "GoogleContainerAnalysisNoteAttestationAuthorityHintOutputReference",
    "GoogleContainerAnalysisNoteAttestationAuthorityOutputReference",
    "GoogleContainerAnalysisNoteConfig",
    "GoogleContainerAnalysisNoteRelatedUrl",
    "GoogleContainerAnalysisNoteRelatedUrlList",
    "GoogleContainerAnalysisNoteRelatedUrlOutputReference",
    "GoogleContainerAnalysisNoteTimeouts",
    "GoogleContainerAnalysisNoteTimeoutsOutputReference",
]

publication.publish()
