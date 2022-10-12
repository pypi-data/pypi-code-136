'''
# `azurerm_media_transform`

Refer to the Terraform Registory for docs: [`azurerm_media_transform`](https://www.terraform.io/docs/providers/azurerm/r/media_transform).
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


class MediaTransform(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransform",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform azurerm_media_transform}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        output: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaTransformOutput", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["MediaTransformTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform azurerm_media_transform} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#media_services_account_name MediaTransform#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#name MediaTransform#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#resource_group_name MediaTransform#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#description MediaTransform#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#id MediaTransform#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#output MediaTransform#output}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#timeouts MediaTransform#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransform.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaTransformConfig(
            media_services_account_name=media_services_account_name,
            name=name,
            resource_group_name=resource_group_name,
            description=description,
            id=id,
            output=output,
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

    @jsii.member(jsii_name="putOutput")
    def put_output(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaTransformOutput", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransform.put_output)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOutput", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#create MediaTransform#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#delete MediaTransform#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#read MediaTransform#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#update MediaTransform#update}.
        '''
        value = MediaTransformTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOutput")
    def reset_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutput", []))

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
    @jsii.member(jsii_name="output")
    def output(self) -> "MediaTransformOutputList":
        return typing.cast("MediaTransformOutputList", jsii.get(self, "output"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaTransformTimeoutsOutputReference":
        return typing.cast("MediaTransformTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountNameInput")
    def media_services_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediaServicesAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputInput")
    def output_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaTransformOutput"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaTransformOutput"]]], jsii.get(self, "outputInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaTransformTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaTransformTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransform, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransform, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountName")
    def media_services_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaServicesAccountName"))

    @media_services_account_name.setter
    def media_services_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransform, "media_services_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaServicesAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransform, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransform, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "media_services_account_name": "mediaServicesAccountName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "description": "description",
        "id": "id",
        "output": "output",
        "timeouts": "timeouts",
    },
)
class MediaTransformConfig(cdktf.TerraformMetaArguments):
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
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        output: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaTransformOutput", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["MediaTransformTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#media_services_account_name MediaTransform#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#name MediaTransform#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#resource_group_name MediaTransform#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#description MediaTransform#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#id MediaTransform#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#output MediaTransform#output}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#timeouts MediaTransform#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MediaTransformTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument media_services_account_name", value=media_services_account_name, expected_type=type_hints["media_services_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "media_services_account_name": media_services_account_name,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if output is not None:
            self._values["output"] = output
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
    def media_services_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#media_services_account_name MediaTransform#media_services_account_name}.'''
        result = self._values.get("media_services_account_name")
        assert result is not None, "Required property 'media_services_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#name MediaTransform#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#resource_group_name MediaTransform#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#description MediaTransform#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#id MediaTransform#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaTransformOutput"]]]:
        '''output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#output MediaTransform#output}
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaTransformOutput"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaTransformTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#timeouts MediaTransform#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaTransformTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutput",
    jsii_struct_bases=[],
    name_mapping={
        "audio_analyzer_preset": "audioAnalyzerPreset",
        "builtin_preset": "builtinPreset",
        "face_detector_preset": "faceDetectorPreset",
        "on_error_action": "onErrorAction",
        "relative_priority": "relativePriority",
        "video_analyzer_preset": "videoAnalyzerPreset",
    },
)
class MediaTransformOutput:
    def __init__(
        self,
        *,
        audio_analyzer_preset: typing.Optional[typing.Union["MediaTransformOutputAudioAnalyzerPreset", typing.Dict[str, typing.Any]]] = None,
        builtin_preset: typing.Optional[typing.Union["MediaTransformOutputBuiltinPreset", typing.Dict[str, typing.Any]]] = None,
        face_detector_preset: typing.Optional[typing.Union["MediaTransformOutputFaceDetectorPreset", typing.Dict[str, typing.Any]]] = None,
        on_error_action: typing.Optional[builtins.str] = None,
        relative_priority: typing.Optional[builtins.str] = None,
        video_analyzer_preset: typing.Optional[typing.Union["MediaTransformOutputVideoAnalyzerPreset", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param audio_analyzer_preset: audio_analyzer_preset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analyzer_preset MediaTransform#audio_analyzer_preset}
        :param builtin_preset: builtin_preset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#builtin_preset MediaTransform#builtin_preset}
        :param face_detector_preset: face_detector_preset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#face_detector_preset MediaTransform#face_detector_preset}
        :param on_error_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#on_error_action MediaTransform#on_error_action}.
        :param relative_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#relative_priority MediaTransform#relative_priority}.
        :param video_analyzer_preset: video_analyzer_preset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#video_analyzer_preset MediaTransform#video_analyzer_preset}
        '''
        if isinstance(audio_analyzer_preset, dict):
            audio_analyzer_preset = MediaTransformOutputAudioAnalyzerPreset(**audio_analyzer_preset)
        if isinstance(builtin_preset, dict):
            builtin_preset = MediaTransformOutputBuiltinPreset(**builtin_preset)
        if isinstance(face_detector_preset, dict):
            face_detector_preset = MediaTransformOutputFaceDetectorPreset(**face_detector_preset)
        if isinstance(video_analyzer_preset, dict):
            video_analyzer_preset = MediaTransformOutputVideoAnalyzerPreset(**video_analyzer_preset)
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutput.__init__)
            check_type(argname="argument audio_analyzer_preset", value=audio_analyzer_preset, expected_type=type_hints["audio_analyzer_preset"])
            check_type(argname="argument builtin_preset", value=builtin_preset, expected_type=type_hints["builtin_preset"])
            check_type(argname="argument face_detector_preset", value=face_detector_preset, expected_type=type_hints["face_detector_preset"])
            check_type(argname="argument on_error_action", value=on_error_action, expected_type=type_hints["on_error_action"])
            check_type(argname="argument relative_priority", value=relative_priority, expected_type=type_hints["relative_priority"])
            check_type(argname="argument video_analyzer_preset", value=video_analyzer_preset, expected_type=type_hints["video_analyzer_preset"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audio_analyzer_preset is not None:
            self._values["audio_analyzer_preset"] = audio_analyzer_preset
        if builtin_preset is not None:
            self._values["builtin_preset"] = builtin_preset
        if face_detector_preset is not None:
            self._values["face_detector_preset"] = face_detector_preset
        if on_error_action is not None:
            self._values["on_error_action"] = on_error_action
        if relative_priority is not None:
            self._values["relative_priority"] = relative_priority
        if video_analyzer_preset is not None:
            self._values["video_analyzer_preset"] = video_analyzer_preset

    @builtins.property
    def audio_analyzer_preset(
        self,
    ) -> typing.Optional["MediaTransformOutputAudioAnalyzerPreset"]:
        '''audio_analyzer_preset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analyzer_preset MediaTransform#audio_analyzer_preset}
        '''
        result = self._values.get("audio_analyzer_preset")
        return typing.cast(typing.Optional["MediaTransformOutputAudioAnalyzerPreset"], result)

    @builtins.property
    def builtin_preset(self) -> typing.Optional["MediaTransformOutputBuiltinPreset"]:
        '''builtin_preset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#builtin_preset MediaTransform#builtin_preset}
        '''
        result = self._values.get("builtin_preset")
        return typing.cast(typing.Optional["MediaTransformOutputBuiltinPreset"], result)

    @builtins.property
    def face_detector_preset(
        self,
    ) -> typing.Optional["MediaTransformOutputFaceDetectorPreset"]:
        '''face_detector_preset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#face_detector_preset MediaTransform#face_detector_preset}
        '''
        result = self._values.get("face_detector_preset")
        return typing.cast(typing.Optional["MediaTransformOutputFaceDetectorPreset"], result)

    @builtins.property
    def on_error_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#on_error_action MediaTransform#on_error_action}.'''
        result = self._values.get("on_error_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relative_priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#relative_priority MediaTransform#relative_priority}.'''
        result = self._values.get("relative_priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video_analyzer_preset(
        self,
    ) -> typing.Optional["MediaTransformOutputVideoAnalyzerPreset"]:
        '''video_analyzer_preset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#video_analyzer_preset MediaTransform#video_analyzer_preset}
        '''
        result = self._values.get("video_analyzer_preset")
        return typing.cast(typing.Optional["MediaTransformOutputVideoAnalyzerPreset"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputAudioAnalyzerPreset",
    jsii_struct_bases=[],
    name_mapping={
        "audio_analysis_mode": "audioAnalysisMode",
        "audio_language": "audioLanguage",
    },
)
class MediaTransformOutputAudioAnalyzerPreset:
    def __init__(
        self,
        *,
        audio_analysis_mode: typing.Optional[builtins.str] = None,
        audio_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_analysis_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.
        :param audio_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutputAudioAnalyzerPreset.__init__)
            check_type(argname="argument audio_analysis_mode", value=audio_analysis_mode, expected_type=type_hints["audio_analysis_mode"])
            check_type(argname="argument audio_language", value=audio_language, expected_type=type_hints["audio_language"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audio_analysis_mode is not None:
            self._values["audio_analysis_mode"] = audio_analysis_mode
        if audio_language is not None:
            self._values["audio_language"] = audio_language

    @builtins.property
    def audio_analysis_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.'''
        result = self._values.get("audio_analysis_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audio_language(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.'''
        result = self._values.get("audio_language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformOutputAudioAnalyzerPreset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaTransformOutputAudioAnalyzerPresetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputAudioAnalyzerPresetOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformOutputAudioAnalyzerPresetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudioAnalysisMode")
    def reset_audio_analysis_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioAnalysisMode", []))

    @jsii.member(jsii_name="resetAudioLanguage")
    def reset_audio_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioLanguage", []))

    @builtins.property
    @jsii.member(jsii_name="audioAnalysisModeInput")
    def audio_analysis_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioAnalysisModeInput"))

    @builtins.property
    @jsii.member(jsii_name="audioLanguageInput")
    def audio_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="audioAnalysisMode")
    def audio_analysis_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioAnalysisMode"))

    @audio_analysis_mode.setter
    def audio_analysis_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputAudioAnalyzerPresetOutputReference, "audio_analysis_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioAnalysisMode", value)

    @builtins.property
    @jsii.member(jsii_name="audioLanguage")
    def audio_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioLanguage"))

    @audio_language.setter
    def audio_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputAudioAnalyzerPresetOutputReference, "audio_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaTransformOutputAudioAnalyzerPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputAudioAnalyzerPreset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaTransformOutputAudioAnalyzerPreset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputAudioAnalyzerPresetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputBuiltinPreset",
    jsii_struct_bases=[],
    name_mapping={"preset_name": "presetName"},
)
class MediaTransformOutputBuiltinPreset:
    def __init__(self, *, preset_name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param preset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#preset_name MediaTransform#preset_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutputBuiltinPreset.__init__)
            check_type(argname="argument preset_name", value=preset_name, expected_type=type_hints["preset_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if preset_name is not None:
            self._values["preset_name"] = preset_name

    @builtins.property
    def preset_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#preset_name MediaTransform#preset_name}.'''
        result = self._values.get("preset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformOutputBuiltinPreset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaTransformOutputBuiltinPresetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputBuiltinPresetOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformOutputBuiltinPresetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPresetName")
    def reset_preset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresetName", []))

    @builtins.property
    @jsii.member(jsii_name="presetNameInput")
    def preset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "presetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="presetName")
    def preset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "presetName"))

    @preset_name.setter
    def preset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputBuiltinPresetOutputReference, "preset_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaTransformOutputBuiltinPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputBuiltinPreset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaTransformOutputBuiltinPreset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputBuiltinPresetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputFaceDetectorPreset",
    jsii_struct_bases=[],
    name_mapping={"analysis_resolution": "analysisResolution"},
)
class MediaTransformOutputFaceDetectorPreset:
    def __init__(
        self,
        *,
        analysis_resolution: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#analysis_resolution MediaTransform#analysis_resolution}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutputFaceDetectorPreset.__init__)
            check_type(argname="argument analysis_resolution", value=analysis_resolution, expected_type=type_hints["analysis_resolution"])
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_resolution is not None:
            self._values["analysis_resolution"] = analysis_resolution

    @builtins.property
    def analysis_resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#analysis_resolution MediaTransform#analysis_resolution}.'''
        result = self._values.get("analysis_resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformOutputFaceDetectorPreset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaTransformOutputFaceDetectorPresetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputFaceDetectorPresetOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformOutputFaceDetectorPresetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnalysisResolution")
    def reset_analysis_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalysisResolution", []))

    @builtins.property
    @jsii.member(jsii_name="analysisResolutionInput")
    def analysis_resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analysisResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="analysisResolution")
    def analysis_resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "analysisResolution"))

    @analysis_resolution.setter
    def analysis_resolution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputFaceDetectorPresetOutputReference, "analysis_resolution").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisResolution", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaTransformOutputFaceDetectorPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputFaceDetectorPreset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaTransformOutputFaceDetectorPreset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputFaceDetectorPresetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaTransformOutputList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputList",
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
            type_hints = typing.get_type_hints(MediaTransformOutputList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MediaTransformOutputOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutputList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaTransformOutputOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaTransformOutput]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaTransformOutput]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaTransformOutput]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaTransformOutputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformOutputOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAudioAnalyzerPreset")
    def put_audio_analyzer_preset(
        self,
        *,
        audio_analysis_mode: typing.Optional[builtins.str] = None,
        audio_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_analysis_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.
        :param audio_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.
        '''
        value = MediaTransformOutputAudioAnalyzerPreset(
            audio_analysis_mode=audio_analysis_mode, audio_language=audio_language
        )

        return typing.cast(None, jsii.invoke(self, "putAudioAnalyzerPreset", [value]))

    @jsii.member(jsii_name="putBuiltinPreset")
    def put_builtin_preset(
        self,
        *,
        preset_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param preset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#preset_name MediaTransform#preset_name}.
        '''
        value = MediaTransformOutputBuiltinPreset(preset_name=preset_name)

        return typing.cast(None, jsii.invoke(self, "putBuiltinPreset", [value]))

    @jsii.member(jsii_name="putFaceDetectorPreset")
    def put_face_detector_preset(
        self,
        *,
        analysis_resolution: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#analysis_resolution MediaTransform#analysis_resolution}.
        '''
        value = MediaTransformOutputFaceDetectorPreset(
            analysis_resolution=analysis_resolution
        )

        return typing.cast(None, jsii.invoke(self, "putFaceDetectorPreset", [value]))

    @jsii.member(jsii_name="putVideoAnalyzerPreset")
    def put_video_analyzer_preset(
        self,
        *,
        audio_analysis_mode: typing.Optional[builtins.str] = None,
        audio_language: typing.Optional[builtins.str] = None,
        insights_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_analysis_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.
        :param audio_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.
        :param insights_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#insights_type MediaTransform#insights_type}.
        '''
        value = MediaTransformOutputVideoAnalyzerPreset(
            audio_analysis_mode=audio_analysis_mode,
            audio_language=audio_language,
            insights_type=insights_type,
        )

        return typing.cast(None, jsii.invoke(self, "putVideoAnalyzerPreset", [value]))

    @jsii.member(jsii_name="resetAudioAnalyzerPreset")
    def reset_audio_analyzer_preset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioAnalyzerPreset", []))

    @jsii.member(jsii_name="resetBuiltinPreset")
    def reset_builtin_preset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuiltinPreset", []))

    @jsii.member(jsii_name="resetFaceDetectorPreset")
    def reset_face_detector_preset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaceDetectorPreset", []))

    @jsii.member(jsii_name="resetOnErrorAction")
    def reset_on_error_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnErrorAction", []))

    @jsii.member(jsii_name="resetRelativePriority")
    def reset_relative_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelativePriority", []))

    @jsii.member(jsii_name="resetVideoAnalyzerPreset")
    def reset_video_analyzer_preset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoAnalyzerPreset", []))

    @builtins.property
    @jsii.member(jsii_name="audioAnalyzerPreset")
    def audio_analyzer_preset(
        self,
    ) -> MediaTransformOutputAudioAnalyzerPresetOutputReference:
        return typing.cast(MediaTransformOutputAudioAnalyzerPresetOutputReference, jsii.get(self, "audioAnalyzerPreset"))

    @builtins.property
    @jsii.member(jsii_name="builtinPreset")
    def builtin_preset(self) -> MediaTransformOutputBuiltinPresetOutputReference:
        return typing.cast(MediaTransformOutputBuiltinPresetOutputReference, jsii.get(self, "builtinPreset"))

    @builtins.property
    @jsii.member(jsii_name="faceDetectorPreset")
    def face_detector_preset(
        self,
    ) -> MediaTransformOutputFaceDetectorPresetOutputReference:
        return typing.cast(MediaTransformOutputFaceDetectorPresetOutputReference, jsii.get(self, "faceDetectorPreset"))

    @builtins.property
    @jsii.member(jsii_name="videoAnalyzerPreset")
    def video_analyzer_preset(
        self,
    ) -> "MediaTransformOutputVideoAnalyzerPresetOutputReference":
        return typing.cast("MediaTransformOutputVideoAnalyzerPresetOutputReference", jsii.get(self, "videoAnalyzerPreset"))

    @builtins.property
    @jsii.member(jsii_name="audioAnalyzerPresetInput")
    def audio_analyzer_preset_input(
        self,
    ) -> typing.Optional[MediaTransformOutputAudioAnalyzerPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputAudioAnalyzerPreset], jsii.get(self, "audioAnalyzerPresetInput"))

    @builtins.property
    @jsii.member(jsii_name="builtinPresetInput")
    def builtin_preset_input(
        self,
    ) -> typing.Optional[MediaTransformOutputBuiltinPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputBuiltinPreset], jsii.get(self, "builtinPresetInput"))

    @builtins.property
    @jsii.member(jsii_name="faceDetectorPresetInput")
    def face_detector_preset_input(
        self,
    ) -> typing.Optional[MediaTransformOutputFaceDetectorPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputFaceDetectorPreset], jsii.get(self, "faceDetectorPresetInput"))

    @builtins.property
    @jsii.member(jsii_name="onErrorActionInput")
    def on_error_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onErrorActionInput"))

    @builtins.property
    @jsii.member(jsii_name="relativePriorityInput")
    def relative_priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativePriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="videoAnalyzerPresetInput")
    def video_analyzer_preset_input(
        self,
    ) -> typing.Optional["MediaTransformOutputVideoAnalyzerPreset"]:
        return typing.cast(typing.Optional["MediaTransformOutputVideoAnalyzerPreset"], jsii.get(self, "videoAnalyzerPresetInput"))

    @builtins.property
    @jsii.member(jsii_name="onErrorAction")
    def on_error_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onErrorAction"))

    @on_error_action.setter
    def on_error_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputOutputReference, "on_error_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onErrorAction", value)

    @builtins.property
    @jsii.member(jsii_name="relativePriority")
    def relative_priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativePriority"))

    @relative_priority.setter
    def relative_priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputOutputReference, "relative_priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativePriority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaTransformOutput, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaTransformOutput, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaTransformOutput, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputVideoAnalyzerPreset",
    jsii_struct_bases=[],
    name_mapping={
        "audio_analysis_mode": "audioAnalysisMode",
        "audio_language": "audioLanguage",
        "insights_type": "insightsType",
    },
)
class MediaTransformOutputVideoAnalyzerPreset:
    def __init__(
        self,
        *,
        audio_analysis_mode: typing.Optional[builtins.str] = None,
        audio_language: typing.Optional[builtins.str] = None,
        insights_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_analysis_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.
        :param audio_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.
        :param insights_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#insights_type MediaTransform#insights_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformOutputVideoAnalyzerPreset.__init__)
            check_type(argname="argument audio_analysis_mode", value=audio_analysis_mode, expected_type=type_hints["audio_analysis_mode"])
            check_type(argname="argument audio_language", value=audio_language, expected_type=type_hints["audio_language"])
            check_type(argname="argument insights_type", value=insights_type, expected_type=type_hints["insights_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audio_analysis_mode is not None:
            self._values["audio_analysis_mode"] = audio_analysis_mode
        if audio_language is not None:
            self._values["audio_language"] = audio_language
        if insights_type is not None:
            self._values["insights_type"] = insights_type

    @builtins.property
    def audio_analysis_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_analysis_mode MediaTransform#audio_analysis_mode}.'''
        result = self._values.get("audio_analysis_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audio_language(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#audio_language MediaTransform#audio_language}.'''
        result = self._values.get("audio_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#insights_type MediaTransform#insights_type}.'''
        result = self._values.get("insights_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformOutputVideoAnalyzerPreset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaTransformOutputVideoAnalyzerPresetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformOutputVideoAnalyzerPresetOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformOutputVideoAnalyzerPresetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudioAnalysisMode")
    def reset_audio_analysis_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioAnalysisMode", []))

    @jsii.member(jsii_name="resetAudioLanguage")
    def reset_audio_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioLanguage", []))

    @jsii.member(jsii_name="resetInsightsType")
    def reset_insights_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightsType", []))

    @builtins.property
    @jsii.member(jsii_name="audioAnalysisModeInput")
    def audio_analysis_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioAnalysisModeInput"))

    @builtins.property
    @jsii.member(jsii_name="audioLanguageInput")
    def audio_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsTypeInput")
    def insights_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="audioAnalysisMode")
    def audio_analysis_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioAnalysisMode"))

    @audio_analysis_mode.setter
    def audio_analysis_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputVideoAnalyzerPresetOutputReference, "audio_analysis_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioAnalysisMode", value)

    @builtins.property
    @jsii.member(jsii_name="audioLanguage")
    def audio_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioLanguage"))

    @audio_language.setter
    def audio_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputVideoAnalyzerPresetOutputReference, "audio_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="insightsType")
    def insights_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "insightsType"))

    @insights_type.setter
    def insights_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputVideoAnalyzerPresetOutputReference, "insights_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaTransformOutputVideoAnalyzerPreset]:
        return typing.cast(typing.Optional[MediaTransformOutputVideoAnalyzerPreset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaTransformOutputVideoAnalyzerPreset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformOutputVideoAnalyzerPresetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MediaTransformTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#create MediaTransform#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#delete MediaTransform#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#read MediaTransform#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#update MediaTransform#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaTransformTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#create MediaTransform#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#delete MediaTransform#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#read MediaTransform#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_transform#update MediaTransform#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaTransformTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaTransformTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaTransform.MediaTransformTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaTransformTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(MediaTransformTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaTransformTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaTransformTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaTransformTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaTransformTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaTransform",
    "MediaTransformConfig",
    "MediaTransformOutput",
    "MediaTransformOutputAudioAnalyzerPreset",
    "MediaTransformOutputAudioAnalyzerPresetOutputReference",
    "MediaTransformOutputBuiltinPreset",
    "MediaTransformOutputBuiltinPresetOutputReference",
    "MediaTransformOutputFaceDetectorPreset",
    "MediaTransformOutputFaceDetectorPresetOutputReference",
    "MediaTransformOutputList",
    "MediaTransformOutputOutputReference",
    "MediaTransformOutputVideoAnalyzerPreset",
    "MediaTransformOutputVideoAnalyzerPresetOutputReference",
    "MediaTransformTimeouts",
    "MediaTransformTimeoutsOutputReference",
]

publication.publish()
