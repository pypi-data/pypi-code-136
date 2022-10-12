'''
# `google_data_loss_prevention_stored_info_type`

Refer to the Terraform Registory for docs: [`google_data_loss_prevention_stored_info_type`](https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type).
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


class GoogleDataLossPreventionStoredInfoType(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type google_data_loss_prevention_stored_info_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        parent: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dictionary: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionary", typing.Dict[str, typing.Any]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        large_custom_dictionary: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary", typing.Dict[str, typing.Any]]] = None,
        regex: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeRegex", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type google_data_loss_prevention_stored_info_type} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param parent: The parent of the info type in any of the following formats:. 'projects/{{project}}' 'projects/{{project}}/locations/{{location}}' 'organizations/{{organization_id}}' 'organizations/{{organization_id}}/locations/{{location}}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#parent GoogleDataLossPreventionStoredInfoType#parent}
        :param description: A description of the info type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#description GoogleDataLossPreventionStoredInfoType#description}
        :param dictionary: dictionary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dictionary GoogleDataLossPreventionStoredInfoType#dictionary}
        :param display_name: User set display name of the info type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#display_name GoogleDataLossPreventionStoredInfoType#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#id GoogleDataLossPreventionStoredInfoType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param large_custom_dictionary: large_custom_dictionary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#large_custom_dictionary GoogleDataLossPreventionStoredInfoType#large_custom_dictionary}
        :param regex: regex block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#regex GoogleDataLossPreventionStoredInfoType#regex}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#timeouts GoogleDataLossPreventionStoredInfoType#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataLossPreventionStoredInfoTypeConfig(
            parent=parent,
            description=description,
            dictionary=dictionary,
            display_name=display_name,
            id=id,
            large_custom_dictionary=large_custom_dictionary,
            regex=regex,
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

    @jsii.member(jsii_name="putDictionary")
    def put_dictionary(
        self,
        *,
        cloud_storage_path: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath", typing.Dict[str, typing.Any]]] = None,
        word_list: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_storage_path: cloud_storage_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_path GoogleDataLossPreventionStoredInfoType#cloud_storage_path}
        :param word_list: word_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#word_list GoogleDataLossPreventionStoredInfoType#word_list}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeDictionary(
            cloud_storage_path=cloud_storage_path, word_list=word_list
        )

        return typing.cast(None, jsii.invoke(self, "putDictionary", [value]))

    @jsii.member(jsii_name="putLargeCustomDictionary")
    def put_large_custom_dictionary(
        self,
        *,
        output_path: typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath", typing.Dict[str, typing.Any]],
        big_query_field: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField", typing.Dict[str, typing.Any]]] = None,
        cloud_storage_file_set: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_path: output_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#output_path GoogleDataLossPreventionStoredInfoType#output_path}
        :param big_query_field: big_query_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#big_query_field GoogleDataLossPreventionStoredInfoType#big_query_field}
        :param cloud_storage_file_set: cloud_storage_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_file_set GoogleDataLossPreventionStoredInfoType#cloud_storage_file_set}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary(
            output_path=output_path,
            big_query_field=big_query_field,
            cloud_storage_file_set=cloud_storage_file_set,
        )

        return typing.cast(None, jsii.invoke(self, "putLargeCustomDictionary", [value]))

    @jsii.member(jsii_name="putRegex")
    def put_regex(
        self,
        *,
        pattern: builtins.str,
        group_indexes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param pattern: Pattern defining the regular expression. Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#pattern GoogleDataLossPreventionStoredInfoType#pattern}
        :param group_indexes: The index of the submatch to extract as findings. When not specified, the entire match is returned. No more than 3 may be included. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#group_indexes GoogleDataLossPreventionStoredInfoType#group_indexes}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeRegex(
            pattern=pattern, group_indexes=group_indexes
        )

        return typing.cast(None, jsii.invoke(self, "putRegex", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#create GoogleDataLossPreventionStoredInfoType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#delete GoogleDataLossPreventionStoredInfoType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#update GoogleDataLossPreventionStoredInfoType#update}.
        '''
        value = GoogleDataLossPreventionStoredInfoTypeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDictionary")
    def reset_dictionary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDictionary", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLargeCustomDictionary")
    def reset_large_custom_dictionary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLargeCustomDictionary", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

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
    @jsii.member(jsii_name="dictionary")
    def dictionary(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference", jsii.get(self, "dictionary"))

    @builtins.property
    @jsii.member(jsii_name="largeCustomDictionary")
    def large_custom_dictionary(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference", jsii.get(self, "largeCustomDictionary"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> "GoogleDataLossPreventionStoredInfoTypeRegexOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeRegexOutputReference", jsii.get(self, "regex"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dictionaryInput")
    def dictionary_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionary"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionary"], jsii.get(self, "dictionaryInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="largeCustomDictionaryInput")
    def large_custom_dictionary_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary"], jsii.get(self, "largeCustomDictionaryInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeRegex"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeRegex"], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoType, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoType, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoType, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoType, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "parent": "parent",
        "description": "description",
        "dictionary": "dictionary",
        "display_name": "displayName",
        "id": "id",
        "large_custom_dictionary": "largeCustomDictionary",
        "regex": "regex",
        "timeouts": "timeouts",
    },
)
class GoogleDataLossPreventionStoredInfoTypeConfig(cdktf.TerraformMetaArguments):
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
        parent: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dictionary: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionary", typing.Dict[str, typing.Any]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        large_custom_dictionary: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary", typing.Dict[str, typing.Any]]] = None,
        regex: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeRegex", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param parent: The parent of the info type in any of the following formats:. 'projects/{{project}}' 'projects/{{project}}/locations/{{location}}' 'organizations/{{organization_id}}' 'organizations/{{organization_id}}/locations/{{location}}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#parent GoogleDataLossPreventionStoredInfoType#parent}
        :param description: A description of the info type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#description GoogleDataLossPreventionStoredInfoType#description}
        :param dictionary: dictionary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dictionary GoogleDataLossPreventionStoredInfoType#dictionary}
        :param display_name: User set display name of the info type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#display_name GoogleDataLossPreventionStoredInfoType#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#id GoogleDataLossPreventionStoredInfoType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param large_custom_dictionary: large_custom_dictionary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#large_custom_dictionary GoogleDataLossPreventionStoredInfoType#large_custom_dictionary}
        :param regex: regex block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#regex GoogleDataLossPreventionStoredInfoType#regex}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#timeouts GoogleDataLossPreventionStoredInfoType#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dictionary, dict):
            dictionary = GoogleDataLossPreventionStoredInfoTypeDictionary(**dictionary)
        if isinstance(large_custom_dictionary, dict):
            large_custom_dictionary = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary(**large_custom_dictionary)
        if isinstance(regex, dict):
            regex = GoogleDataLossPreventionStoredInfoTypeRegex(**regex)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataLossPreventionStoredInfoTypeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dictionary", value=dictionary, expected_type=type_hints["dictionary"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument large_custom_dictionary", value=large_custom_dictionary, expected_type=type_hints["large_custom_dictionary"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "parent": parent,
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
        if dictionary is not None:
            self._values["dictionary"] = dictionary
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if large_custom_dictionary is not None:
            self._values["large_custom_dictionary"] = large_custom_dictionary
        if regex is not None:
            self._values["regex"] = regex
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
    def parent(self) -> builtins.str:
        '''The parent of the info type in any of the following formats:.

        'projects/{{project}}'
        'projects/{{project}}/locations/{{location}}'
        'organizations/{{organization_id}}'
        'organizations/{{organization_id}}/locations/{{location}}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#parent GoogleDataLossPreventionStoredInfoType#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the info type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#description GoogleDataLossPreventionStoredInfoType#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dictionary(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionary"]:
        '''dictionary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dictionary GoogleDataLossPreventionStoredInfoType#dictionary}
        '''
        result = self._values.get("dictionary")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionary"], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''User set display name of the info type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#display_name GoogleDataLossPreventionStoredInfoType#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#id GoogleDataLossPreventionStoredInfoType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def large_custom_dictionary(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary"]:
        '''large_custom_dictionary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#large_custom_dictionary GoogleDataLossPreventionStoredInfoType#large_custom_dictionary}
        '''
        result = self._values.get("large_custom_dictionary")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary"], result)

    @builtins.property
    def regex(self) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeRegex"]:
        '''regex block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#regex GoogleDataLossPreventionStoredInfoType#regex}
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeRegex"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#timeouts GoogleDataLossPreventionStoredInfoType#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionary",
    jsii_struct_bases=[],
    name_mapping={"cloud_storage_path": "cloudStoragePath", "word_list": "wordList"},
)
class GoogleDataLossPreventionStoredInfoTypeDictionary:
    def __init__(
        self,
        *,
        cloud_storage_path: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath", typing.Dict[str, typing.Any]]] = None,
        word_list: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_storage_path: cloud_storage_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_path GoogleDataLossPreventionStoredInfoType#cloud_storage_path}
        :param word_list: word_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#word_list GoogleDataLossPreventionStoredInfoType#word_list}
        '''
        if isinstance(cloud_storage_path, dict):
            cloud_storage_path = GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath(**cloud_storage_path)
        if isinstance(word_list, dict):
            word_list = GoogleDataLossPreventionStoredInfoTypeDictionaryWordList(**word_list)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionary.__init__)
            check_type(argname="argument cloud_storage_path", value=cloud_storage_path, expected_type=type_hints["cloud_storage_path"])
            check_type(argname="argument word_list", value=word_list, expected_type=type_hints["word_list"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_storage_path is not None:
            self._values["cloud_storage_path"] = cloud_storage_path
        if word_list is not None:
            self._values["word_list"] = word_list

    @builtins.property
    def cloud_storage_path(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath"]:
        '''cloud_storage_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_path GoogleDataLossPreventionStoredInfoType#cloud_storage_path}
        '''
        result = self._values.get("cloud_storage_path")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath"], result)

    @builtins.property
    def word_list(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList"]:
        '''word_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#word_list GoogleDataLossPreventionStoredInfoType#word_list}
        '''
        result = self._values.get("word_list")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeDictionary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudStoragePath")
    def put_cloud_storage_path(self, *, path: builtins.str) -> None:
        '''
        :param path: A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath(
            path=path
        )

        return typing.cast(None, jsii.invoke(self, "putCloudStoragePath", [value]))

    @jsii.member(jsii_name="putWordList")
    def put_word_list(self, *, words: typing.Sequence[builtins.str]) -> None:
        '''
        :param words: Words or phrases defining the dictionary. The dictionary must contain at least one phrase and every phrase must contain at least 2 characters that are letters or digits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#words GoogleDataLossPreventionStoredInfoType#words}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeDictionaryWordList(words=words)

        return typing.cast(None, jsii.invoke(self, "putWordList", [value]))

    @jsii.member(jsii_name="resetCloudStoragePath")
    def reset_cloud_storage_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePath", []))

    @jsii.member(jsii_name="resetWordList")
    def reset_word_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWordList", []))

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference:
        return typing.cast(GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference, jsii.get(self, "cloudStoragePath"))

    @builtins.property
    @jsii.member(jsii_name="wordList")
    def word_list(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference", jsii.get(self, "wordList"))

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePathInput")
    def cloud_storage_path_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath], jsii.get(self, "cloudStoragePathInput"))

    @builtins.property
    @jsii.member(jsii_name="wordListInput")
    def word_list_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeDictionaryWordList"], jsii.get(self, "wordListInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionary]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionaryWordList",
    jsii_struct_bases=[],
    name_mapping={"words": "words"},
)
class GoogleDataLossPreventionStoredInfoTypeDictionaryWordList:
    def __init__(self, *, words: typing.Sequence[builtins.str]) -> None:
        '''
        :param words: Words or phrases defining the dictionary. The dictionary must contain at least one phrase and every phrase must contain at least 2 characters that are letters or digits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#words GoogleDataLossPreventionStoredInfoType#words}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionaryWordList.__init__)
            check_type(argname="argument words", value=words, expected_type=type_hints["words"])
        self._values: typing.Dict[str, typing.Any] = {
            "words": words,
        }

    @builtins.property
    def words(self) -> typing.List[builtins.str]:
        '''Words or phrases defining the dictionary.

        The dictionary must contain at least one
        phrase and every phrase must contain at least 2 characters that are letters or digits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#words GoogleDataLossPreventionStoredInfoType#words}
        '''
        result = self._values.get("words")
        assert result is not None, "Required property 'words' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeDictionaryWordList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="wordsInput")
    def words_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "wordsInput"))

    @builtins.property
    @jsii.member(jsii_name="words")
    def words(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "words"))

    @words.setter
    def words(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference, "words").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "words", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryWordList]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryWordList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeDictionaryWordList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary",
    jsii_struct_bases=[],
    name_mapping={
        "output_path": "outputPath",
        "big_query_field": "bigQueryField",
        "cloud_storage_file_set": "cloudStorageFileSet",
    },
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary:
    def __init__(
        self,
        *,
        output_path: typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath", typing.Dict[str, typing.Any]],
        big_query_field: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField", typing.Dict[str, typing.Any]]] = None,
        cloud_storage_file_set: typing.Optional[typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_path: output_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#output_path GoogleDataLossPreventionStoredInfoType#output_path}
        :param big_query_field: big_query_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#big_query_field GoogleDataLossPreventionStoredInfoType#big_query_field}
        :param cloud_storage_file_set: cloud_storage_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_file_set GoogleDataLossPreventionStoredInfoType#cloud_storage_file_set}
        '''
        if isinstance(output_path, dict):
            output_path = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath(**output_path)
        if isinstance(big_query_field, dict):
            big_query_field = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField(**big_query_field)
        if isinstance(cloud_storage_file_set, dict):
            cloud_storage_file_set = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet(**cloud_storage_file_set)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary.__init__)
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument big_query_field", value=big_query_field, expected_type=type_hints["big_query_field"])
            check_type(argname="argument cloud_storage_file_set", value=cloud_storage_file_set, expected_type=type_hints["cloud_storage_file_set"])
        self._values: typing.Dict[str, typing.Any] = {
            "output_path": output_path,
        }
        if big_query_field is not None:
            self._values["big_query_field"] = big_query_field
        if cloud_storage_file_set is not None:
            self._values["cloud_storage_file_set"] = cloud_storage_file_set

    @builtins.property
    def output_path(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath":
        '''output_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#output_path GoogleDataLossPreventionStoredInfoType#output_path}
        '''
        result = self._values.get("output_path")
        assert result is not None, "Required property 'output_path' is missing"
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath", result)

    @builtins.property
    def big_query_field(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField"]:
        '''big_query_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#big_query_field GoogleDataLossPreventionStoredInfoType#big_query_field}
        '''
        result = self._values.get("big_query_field")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField"], result)

    @builtins.property
    def cloud_storage_file_set(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet"]:
        '''cloud_storage_file_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#cloud_storage_file_set GoogleDataLossPreventionStoredInfoType#cloud_storage_file_set}
        '''
        result = self._values.get("cloud_storage_file_set")
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField",
    jsii_struct_bases=[],
    name_mapping={"field": "field", "table": "table"},
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField:
    def __init__(
        self,
        *,
        field: typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField", typing.Dict[str, typing.Any]],
        table: typing.Union["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param field: field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#field GoogleDataLossPreventionStoredInfoType#field}
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table GoogleDataLossPreventionStoredInfoType#table}
        '''
        if isinstance(field, dict):
            field = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField(**field)
        if isinstance(table, dict):
            table = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable(**table)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField.__init__)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        self._values: typing.Dict[str, typing.Any] = {
            "field": field,
            "table": table,
        }

    @builtins.property
    def field(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField":
        '''field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#field GoogleDataLossPreventionStoredInfoType#field}
        '''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField", result)

    @builtins.property
    def table(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable":
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table GoogleDataLossPreventionStoredInfoType#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Name describing the field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#name GoogleDataLossPreventionStoredInfoType#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name describing the field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#name GoogleDataLossPreventionStoredInfoType#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putField")
    def put_field(self, *, name: builtins.str) -> None:
        '''
        :param name: Name describing the field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#name GoogleDataLossPreventionStoredInfoType#name}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putField", [value]))

    @jsii.member(jsii_name="putTable")
    def put_table(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dataset_id GoogleDataLossPreventionStoredInfoType#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#project_id GoogleDataLossPreventionStoredInfoType#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table_id GoogleDataLossPreventionStoredInfoType#table_id}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putTable", [value]))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(
        self,
    ) -> GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference:
        return typing.cast(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference, jsii.get(self, "field"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(
        self,
    ) -> "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference":
        return typing.cast("GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dataset_id GoogleDataLossPreventionStoredInfoType#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#project_id GoogleDataLossPreventionStoredInfoType#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table_id GoogleDataLossPreventionStoredInfoType#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The dataset ID of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#dataset_id GoogleDataLossPreventionStoredInfoType#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Google Cloud Platform project ID of the project containing the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#project_id GoogleDataLossPreventionStoredInfoType#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The name of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table_id GoogleDataLossPreventionStoredInfoType#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet",
    jsii_struct_bases=[],
    name_mapping={"url": "url"},
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet:
    def __init__(self, *, url: builtins.str) -> None:
        '''
        :param url: The url, in the format 'gs:///'. Trailing wildcard in the path is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#url GoogleDataLossPreventionStoredInfoType#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }

    @builtins.property
    def url(self) -> builtins.str:
        '''The url, in the format 'gs:///'. Trailing wildcard in the path is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#url GoogleDataLossPreventionStoredInfoType#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigQueryField")
    def put_big_query_field(
        self,
        *,
        field: typing.Union[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField, typing.Dict[str, typing.Any]],
        table: typing.Union[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param field: field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#field GoogleDataLossPreventionStoredInfoType#field}
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#table GoogleDataLossPreventionStoredInfoType#table}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField(
            field=field, table=table
        )

        return typing.cast(None, jsii.invoke(self, "putBigQueryField", [value]))

    @jsii.member(jsii_name="putCloudStorageFileSet")
    def put_cloud_storage_file_set(self, *, url: builtins.str) -> None:
        '''
        :param url: The url, in the format 'gs:///'. Trailing wildcard in the path is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#url GoogleDataLossPreventionStoredInfoType#url}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet(
            url=url
        )

        return typing.cast(None, jsii.invoke(self, "putCloudStorageFileSet", [value]))

    @jsii.member(jsii_name="putOutputPath")
    def put_output_path(self, *, path: builtins.str) -> None:
        '''
        :param path: A url representing a file or path (no wildcards) in Cloud Storage. Example: 'gs://[BUCKET_NAME]/dictionary.txt'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#path GoogleDataLossPreventionStoredInfoType#path}
        '''
        value = GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath(
            path=path
        )

        return typing.cast(None, jsii.invoke(self, "putOutputPath", [value]))

    @jsii.member(jsii_name="resetBigQueryField")
    def reset_big_query_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigQueryField", []))

    @jsii.member(jsii_name="resetCloudStorageFileSet")
    def reset_cloud_storage_file_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageFileSet", []))

    @builtins.property
    @jsii.member(jsii_name="bigQueryField")
    def big_query_field(
        self,
    ) -> GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference:
        return typing.cast(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference, jsii.get(self, "bigQueryField"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageFileSet")
    def cloud_storage_file_set(
        self,
    ) -> GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference:
        return typing.cast(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference, jsii.get(self, "cloudStorageFileSet"))

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def output_path(
        self,
    ) -> GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference:
        return typing.cast(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference, jsii.get(self, "outputPath"))

    @builtins.property
    @jsii.member(jsii_name="bigQueryFieldInput")
    def big_query_field_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField], jsii.get(self, "bigQueryFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageFileSetInput")
    def cloud_storage_file_set_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet], jsii.get(self, "cloudStorageFileSetInput"))

    @builtins.property
    @jsii.member(jsii_name="outputPathInput")
    def output_path_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath], jsii.get(self, "outputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeRegex",
    jsii_struct_bases=[],
    name_mapping={"pattern": "pattern", "group_indexes": "groupIndexes"},
)
class GoogleDataLossPreventionStoredInfoTypeRegex:
    def __init__(
        self,
        *,
        pattern: builtins.str,
        group_indexes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param pattern: Pattern defining the regular expression. Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#pattern GoogleDataLossPreventionStoredInfoType#pattern}
        :param group_indexes: The index of the submatch to extract as findings. When not specified, the entire match is returned. No more than 3 may be included. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#group_indexes GoogleDataLossPreventionStoredInfoType#group_indexes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeRegex.__init__)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument group_indexes", value=group_indexes, expected_type=type_hints["group_indexes"])
        self._values: typing.Dict[str, typing.Any] = {
            "pattern": pattern,
        }
        if group_indexes is not None:
            self._values["group_indexes"] = group_indexes

    @builtins.property
    def pattern(self) -> builtins.str:
        '''Pattern defining the regular expression. Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#pattern GoogleDataLossPreventionStoredInfoType#pattern}
        '''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_indexes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''The index of the submatch to extract as findings.

        When not specified, the entire match is returned. No more than 3 may be included.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#group_indexes GoogleDataLossPreventionStoredInfoType#group_indexes}
        '''
        result = self._values.get("group_indexes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeRegex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeRegexOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeRegexOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeRegexOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroupIndexes")
    def reset_group_indexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupIndexes", []))

    @builtins.property
    @jsii.member(jsii_name="groupIndexesInput")
    def group_indexes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "groupIndexesInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIndexes")
    def group_indexes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "groupIndexes"))

    @group_indexes.setter
    def group_indexes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeRegexOutputReference, "group_indexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupIndexes", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeRegexOutputReference, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionStoredInfoTypeRegex]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionStoredInfoTypeRegex], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionStoredInfoTypeRegex],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeRegexOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataLossPreventionStoredInfoTypeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#create GoogleDataLossPreventionStoredInfoType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#delete GoogleDataLossPreventionStoredInfoType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#update GoogleDataLossPreventionStoredInfoType#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#create GoogleDataLossPreventionStoredInfoType#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#delete GoogleDataLossPreventionStoredInfoType#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_stored_info_type#update GoogleDataLossPreventionStoredInfoType#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionStoredInfoTypeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionStoredInfoType.GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionStoredInfoTypeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionStoredInfoTypeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionStoredInfoTypeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataLossPreventionStoredInfoType",
    "GoogleDataLossPreventionStoredInfoTypeConfig",
    "GoogleDataLossPreventionStoredInfoTypeDictionary",
    "GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePath",
    "GoogleDataLossPreventionStoredInfoTypeDictionaryCloudStoragePathOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeDictionaryOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeDictionaryWordList",
    "GoogleDataLossPreventionStoredInfoTypeDictionaryWordListOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionary",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryField",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPath",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputPathOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeLargeCustomDictionaryOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeRegex",
    "GoogleDataLossPreventionStoredInfoTypeRegexOutputReference",
    "GoogleDataLossPreventionStoredInfoTypeTimeouts",
    "GoogleDataLossPreventionStoredInfoTypeTimeoutsOutputReference",
]

publication.publish()
