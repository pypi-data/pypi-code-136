'''
# `google_dialogflow_cx_entity_type`

Refer to the Terraform Registory for docs: [`google_dialogflow_cx_entity_type`](https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type).
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


class GoogleDialogflowCxEntityType(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type google_dialogflow_cx_entity_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        entities: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeEntities", typing.Dict[str, typing.Any]]]],
        kind: builtins.str,
        auto_expansion_mode: typing.Optional[builtins.str] = None,
        enable_fuzzy_extraction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        excluded_phrases: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeExcludedPhrases", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        redact: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxEntityTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type google_dialogflow_cx_entity_type} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The human-readable name of the entity type, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#display_name GoogleDialogflowCxEntityType#display_name}
        :param entities: entities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#entities GoogleDialogflowCxEntityType#entities}
        :param kind: Indicates whether the entity type can be automatically expanded. KIND_MAP: Map entity types allow mapping of a group of synonyms to a canonical value. KIND_LIST: List entity types contain a set of entries that do not map to canonical values. However, list entity types can contain references to other entity types (with or without aliases). KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values. Possible values: ["KIND_MAP", "KIND_LIST", "KIND_REGEXP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#kind GoogleDialogflowCxEntityType#kind}
        :param auto_expansion_mode: Represents kinds of entities. AUTO_EXPANSION_MODE_UNSPECIFIED: Auto expansion disabled for the entity. AUTO_EXPANSION_MODE_DEFAULT: Allows an agent to recognize values that have not been explicitly listed in the entity. Possible values: ["AUTO_EXPANSION_MODE_DEFAULT", "AUTO_EXPANSION_MODE_UNSPECIFIED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#auto_expansion_mode GoogleDialogflowCxEntityType#auto_expansion_mode}
        :param enable_fuzzy_extraction: Enables fuzzy entity extraction during classification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#enable_fuzzy_extraction GoogleDialogflowCxEntityType#enable_fuzzy_extraction}
        :param excluded_phrases: excluded_phrases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#excluded_phrases GoogleDialogflowCxEntityType#excluded_phrases}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#id GoogleDialogflowCxEntityType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in entityType: EntityType.entities.value EntityType.entities.synonyms EntityType.excluded_phrases.value If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#language_code GoogleDialogflowCxEntityType#language_code}
        :param parent: The agent to create a entity type for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#parent GoogleDialogflowCxEntityType#parent}
        :param redact: Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name when logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#redact GoogleDialogflowCxEntityType#redact}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#timeouts GoogleDialogflowCxEntityType#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDialogflowCxEntityTypeConfig(
            display_name=display_name,
            entities=entities,
            kind=kind,
            auto_expansion_mode=auto_expansion_mode,
            enable_fuzzy_extraction=enable_fuzzy_extraction,
            excluded_phrases=excluded_phrases,
            id=id,
            language_code=language_code,
            parent=parent,
            redact=redact,
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

    @jsii.member(jsii_name="putEntities")
    def put_entities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeEntities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityType.put_entities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntities", [value]))

    @jsii.member(jsii_name="putExcludedPhrases")
    def put_excluded_phrases(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeExcludedPhrases", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityType.put_excluded_phrases)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExcludedPhrases", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#create GoogleDialogflowCxEntityType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#delete GoogleDialogflowCxEntityType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#update GoogleDialogflowCxEntityType#update}.
        '''
        value = GoogleDialogflowCxEntityTypeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoExpansionMode")
    def reset_auto_expansion_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoExpansionMode", []))

    @jsii.member(jsii_name="resetEnableFuzzyExtraction")
    def reset_enable_fuzzy_extraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFuzzyExtraction", []))

    @jsii.member(jsii_name="resetExcludedPhrases")
    def reset_excluded_phrases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedPhrases", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetRedact")
    def reset_redact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedact", []))

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
    @jsii.member(jsii_name="entities")
    def entities(self) -> "GoogleDialogflowCxEntityTypeEntitiesList":
        return typing.cast("GoogleDialogflowCxEntityTypeEntitiesList", jsii.get(self, "entities"))

    @builtins.property
    @jsii.member(jsii_name="excludedPhrases")
    def excluded_phrases(self) -> "GoogleDialogflowCxEntityTypeExcludedPhrasesList":
        return typing.cast("GoogleDialogflowCxEntityTypeExcludedPhrasesList", jsii.get(self, "excludedPhrases"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDialogflowCxEntityTypeTimeoutsOutputReference":
        return typing.cast("GoogleDialogflowCxEntityTypeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoExpansionModeInput")
    def auto_expansion_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoExpansionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableFuzzyExtractionInput")
    def enable_fuzzy_extraction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFuzzyExtractionInput"))

    @builtins.property
    @jsii.member(jsii_name="entitiesInput")
    def entities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeEntities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeEntities"]]], jsii.get(self, "entitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedPhrasesInput")
    def excluded_phrases_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeExcludedPhrases"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeExcludedPhrases"]]], jsii.get(self, "excludedPhrasesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="redactInput")
    def redact_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "redactInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDialogflowCxEntityTypeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDialogflowCxEntityTypeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoExpansionMode")
    def auto_expansion_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoExpansionMode"))

    @auto_expansion_mode.setter
    def auto_expansion_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "auto_expansion_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoExpansionMode", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFuzzyExtraction"))

    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "enable_fuzzy_extraction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFuzzyExtraction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "language_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="redact")
    def redact(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "redact"))

    @redact.setter
    def redact(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityType, "redact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redact", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "entities": "entities",
        "kind": "kind",
        "auto_expansion_mode": "autoExpansionMode",
        "enable_fuzzy_extraction": "enableFuzzyExtraction",
        "excluded_phrases": "excludedPhrases",
        "id": "id",
        "language_code": "languageCode",
        "parent": "parent",
        "redact": "redact",
        "timeouts": "timeouts",
    },
)
class GoogleDialogflowCxEntityTypeConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        entities: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeEntities", typing.Dict[str, typing.Any]]]],
        kind: builtins.str,
        auto_expansion_mode: typing.Optional[builtins.str] = None,
        enable_fuzzy_extraction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        excluded_phrases: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxEntityTypeExcludedPhrases", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        redact: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxEntityTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The human-readable name of the entity type, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#display_name GoogleDialogflowCxEntityType#display_name}
        :param entities: entities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#entities GoogleDialogflowCxEntityType#entities}
        :param kind: Indicates whether the entity type can be automatically expanded. KIND_MAP: Map entity types allow mapping of a group of synonyms to a canonical value. KIND_LIST: List entity types contain a set of entries that do not map to canonical values. However, list entity types can contain references to other entity types (with or without aliases). KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values. Possible values: ["KIND_MAP", "KIND_LIST", "KIND_REGEXP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#kind GoogleDialogflowCxEntityType#kind}
        :param auto_expansion_mode: Represents kinds of entities. AUTO_EXPANSION_MODE_UNSPECIFIED: Auto expansion disabled for the entity. AUTO_EXPANSION_MODE_DEFAULT: Allows an agent to recognize values that have not been explicitly listed in the entity. Possible values: ["AUTO_EXPANSION_MODE_DEFAULT", "AUTO_EXPANSION_MODE_UNSPECIFIED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#auto_expansion_mode GoogleDialogflowCxEntityType#auto_expansion_mode}
        :param enable_fuzzy_extraction: Enables fuzzy entity extraction during classification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#enable_fuzzy_extraction GoogleDialogflowCxEntityType#enable_fuzzy_extraction}
        :param excluded_phrases: excluded_phrases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#excluded_phrases GoogleDialogflowCxEntityType#excluded_phrases}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#id GoogleDialogflowCxEntityType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in entityType: EntityType.entities.value EntityType.entities.synonyms EntityType.excluded_phrases.value If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#language_code GoogleDialogflowCxEntityType#language_code}
        :param parent: The agent to create a entity type for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#parent GoogleDialogflowCxEntityType#parent}
        :param redact: Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name when logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#redact GoogleDialogflowCxEntityType#redact}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#timeouts GoogleDialogflowCxEntityType#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleDialogflowCxEntityTypeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument entities", value=entities, expected_type=type_hints["entities"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument auto_expansion_mode", value=auto_expansion_mode, expected_type=type_hints["auto_expansion_mode"])
            check_type(argname="argument enable_fuzzy_extraction", value=enable_fuzzy_extraction, expected_type=type_hints["enable_fuzzy_extraction"])
            check_type(argname="argument excluded_phrases", value=excluded_phrases, expected_type=type_hints["excluded_phrases"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument redact", value=redact, expected_type=type_hints["redact"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "entities": entities,
            "kind": kind,
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
        if auto_expansion_mode is not None:
            self._values["auto_expansion_mode"] = auto_expansion_mode
        if enable_fuzzy_extraction is not None:
            self._values["enable_fuzzy_extraction"] = enable_fuzzy_extraction
        if excluded_phrases is not None:
            self._values["excluded_phrases"] = excluded_phrases
        if id is not None:
            self._values["id"] = id
        if language_code is not None:
            self._values["language_code"] = language_code
        if parent is not None:
            self._values["parent"] = parent
        if redact is not None:
            self._values["redact"] = redact
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
    def display_name(self) -> builtins.str:
        '''The human-readable name of the entity type, unique within the agent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#display_name GoogleDialogflowCxEntityType#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entities(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeEntities"]]:
        '''entities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#entities GoogleDialogflowCxEntityType#entities}
        '''
        result = self._values.get("entities")
        assert result is not None, "Required property 'entities' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeEntities"]], result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''Indicates whether the entity type can be automatically expanded.

        KIND_MAP: Map entity types allow mapping of a group of synonyms to a canonical value.
        KIND_LIST: List entity types contain a set of entries that do not map to canonical values. However, list entity types can contain references to other entity types (with or without aliases).
        KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values. Possible values: ["KIND_MAP", "KIND_LIST", "KIND_REGEXP"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#kind GoogleDialogflowCxEntityType#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_expansion_mode(self) -> typing.Optional[builtins.str]:
        '''Represents kinds of entities.

        AUTO_EXPANSION_MODE_UNSPECIFIED: Auto expansion disabled for the entity.
        AUTO_EXPANSION_MODE_DEFAULT: Allows an agent to recognize values that have not been explicitly listed in the entity. Possible values: ["AUTO_EXPANSION_MODE_DEFAULT", "AUTO_EXPANSION_MODE_UNSPECIFIED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#auto_expansion_mode GoogleDialogflowCxEntityType#auto_expansion_mode}
        '''
        result = self._values.get("auto_expansion_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_fuzzy_extraction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables fuzzy entity extraction during classification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#enable_fuzzy_extraction GoogleDialogflowCxEntityType#enable_fuzzy_extraction}
        '''
        result = self._values.get("enable_fuzzy_extraction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def excluded_phrases(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeExcludedPhrases"]]]:
        '''excluded_phrases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#excluded_phrases GoogleDialogflowCxEntityType#excluded_phrases}
        '''
        result = self._values.get("excluded_phrases")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxEntityTypeExcludedPhrases"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#id GoogleDialogflowCxEntityType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''The language of the following fields in entityType: EntityType.entities.value EntityType.entities.synonyms EntityType.excluded_phrases.value If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#language_code GoogleDialogflowCxEntityType#language_code}
        '''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''The agent to create a entity type for. Format: projects//locations//agents/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#parent GoogleDialogflowCxEntityType#parent}
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redact(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether parameters of the entity type should be redacted in log.

        If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name when logging.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#redact GoogleDialogflowCxEntityType#redact}
        '''
        result = self._values.get("redact")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDialogflowCxEntityTypeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#timeouts GoogleDialogflowCxEntityType#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDialogflowCxEntityTypeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxEntityTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeEntities",
    jsii_struct_bases=[],
    name_mapping={"synonyms": "synonyms", "value": "value"},
)
class GoogleDialogflowCxEntityTypeEntities:
    def __init__(
        self,
        *,
        synonyms: typing.Optional[typing.Sequence[builtins.str]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param synonyms: A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym could be green onions. For KIND_LIST entity types: This collection must contain exactly one synonym equal to value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#synonyms GoogleDialogflowCxEntityType#synonyms}
        :param value: The primary value associated with this entity entry. For example, if the entity type is vegetable, the value could be scallions. For KIND_MAP entity types: A canonical value to be used in place of synonyms. For KIND_LIST entity types: A string that can contain references to other entity types (with or without aliases). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#value GoogleDialogflowCxEntityType#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeEntities.__init__)
            check_type(argname="argument synonyms", value=synonyms, expected_type=type_hints["synonyms"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if synonyms is not None:
            self._values["synonyms"] = synonyms
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def synonyms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of value synonyms.

        For example, if the entity type is vegetable, and value is scallions, a synonym could be green onions.
        For KIND_LIST entity types: This collection must contain exactly one synonym equal to value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#synonyms GoogleDialogflowCxEntityType#synonyms}
        '''
        result = self._values.get("synonyms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The primary value associated with this entity entry.

        For example, if the entity type is vegetable, the value could be scallions.
        For KIND_MAP entity types: A canonical value to be used in place of synonyms.
        For KIND_LIST entity types: A string that can contain references to other entity types (with or without aliases).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#value GoogleDialogflowCxEntityType#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxEntityTypeEntities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxEntityTypeEntitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeEntitiesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeEntitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxEntityTypeEntitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeEntitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxEntityTypeEntitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeEntities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeEntities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeEntities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxEntityTypeEntitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeEntitiesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeEntitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSynonyms")
    def reset_synonyms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSynonyms", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="synonymsInput")
    def synonyms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "synonymsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="synonyms")
    def synonyms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "synonyms"))

    @synonyms.setter
    def synonyms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesOutputReference, "synonyms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synonyms", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeEntities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeEntities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeEntities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeEntitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeExcludedPhrases",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class GoogleDialogflowCxEntityTypeExcludedPhrases:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: The word or phrase to be excluded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#value GoogleDialogflowCxEntityType#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeExcludedPhrases.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The word or phrase to be excluded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#value GoogleDialogflowCxEntityType#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxEntityTypeExcludedPhrases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxEntityTypeExcludedPhrasesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeExcludedPhrasesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeExcludedPhrasesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeExcludedPhrasesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeExcludedPhrases]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeExcludedPhrases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxEntityTypeExcludedPhrases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeExcludedPhrases, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeExcludedPhrases, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeExcludedPhrases, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDialogflowCxEntityTypeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#create GoogleDialogflowCxEntityType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#delete GoogleDialogflowCxEntityType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#update GoogleDialogflowCxEntityType#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#create GoogleDialogflowCxEntityType#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#delete GoogleDialogflowCxEntityType#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_entity_type#update GoogleDialogflowCxEntityType#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxEntityTypeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxEntityTypeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxEntityType.GoogleDialogflowCxEntityTypeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxEntityTypeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxEntityTypeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxEntityTypeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDialogflowCxEntityType",
    "GoogleDialogflowCxEntityTypeConfig",
    "GoogleDialogflowCxEntityTypeEntities",
    "GoogleDialogflowCxEntityTypeEntitiesList",
    "GoogleDialogflowCxEntityTypeEntitiesOutputReference",
    "GoogleDialogflowCxEntityTypeExcludedPhrases",
    "GoogleDialogflowCxEntityTypeExcludedPhrasesList",
    "GoogleDialogflowCxEntityTypeExcludedPhrasesOutputReference",
    "GoogleDialogflowCxEntityTypeTimeouts",
    "GoogleDialogflowCxEntityTypeTimeoutsOutputReference",
]

publication.publish()
