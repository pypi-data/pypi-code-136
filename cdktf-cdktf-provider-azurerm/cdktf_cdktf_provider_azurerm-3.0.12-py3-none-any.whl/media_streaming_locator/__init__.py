'''
# `azurerm_media_streaming_locator`

Refer to the Terraform Registory for docs: [`azurerm_media_streaming_locator`](https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator).
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


class MediaStreamingLocator(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocator",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator azurerm_media_streaming_locator}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        asset_name: builtins.str,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        streaming_policy_name: builtins.str,
        alternative_media_id: typing.Optional[builtins.str] = None,
        content_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaStreamingLocatorContentKey", typing.Dict[str, typing.Any]]]]] = None,
        default_content_key_policy_name: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        streaming_locator_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MediaStreamingLocatorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator azurerm_media_streaming_locator} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param asset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#asset_name MediaStreamingLocator#asset_name}.
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#media_services_account_name MediaStreamingLocator#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#name MediaStreamingLocator#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#resource_group_name MediaStreamingLocator#resource_group_name}.
        :param streaming_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_policy_name MediaStreamingLocator#streaming_policy_name}.
        :param alternative_media_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#alternative_media_id MediaStreamingLocator#alternative_media_id}.
        :param content_key: content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#content_key MediaStreamingLocator#content_key}
        :param default_content_key_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#default_content_key_policy_name MediaStreamingLocator#default_content_key_policy_name}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#end_time MediaStreamingLocator#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#id MediaStreamingLocator#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#start_time MediaStreamingLocator#start_time}.
        :param streaming_locator_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_locator_id MediaStreamingLocator#streaming_locator_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#timeouts MediaStreamingLocator#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocator.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaStreamingLocatorConfig(
            asset_name=asset_name,
            media_services_account_name=media_services_account_name,
            name=name,
            resource_group_name=resource_group_name,
            streaming_policy_name=streaming_policy_name,
            alternative_media_id=alternative_media_id,
            content_key=content_key,
            default_content_key_policy_name=default_content_key_policy_name,
            end_time=end_time,
            id=id,
            start_time=start_time,
            streaming_locator_id=streaming_locator_id,
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

    @jsii.member(jsii_name="putContentKey")
    def put_content_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaStreamingLocatorContentKey", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocator.put_content_key)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContentKey", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#create MediaStreamingLocator#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#delete MediaStreamingLocator#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#read MediaStreamingLocator#read}.
        '''
        value = MediaStreamingLocatorTimeouts(create=create, delete=delete, read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlternativeMediaId")
    def reset_alternative_media_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternativeMediaId", []))

    @jsii.member(jsii_name="resetContentKey")
    def reset_content_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentKey", []))

    @jsii.member(jsii_name="resetDefaultContentKeyPolicyName")
    def reset_default_content_key_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultContentKeyPolicyName", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetStreamingLocatorId")
    def reset_streaming_locator_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamingLocatorId", []))

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
    @jsii.member(jsii_name="contentKey")
    def content_key(self) -> "MediaStreamingLocatorContentKeyList":
        return typing.cast("MediaStreamingLocatorContentKeyList", jsii.get(self, "contentKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaStreamingLocatorTimeoutsOutputReference":
        return typing.cast("MediaStreamingLocatorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alternativeMediaIdInput")
    def alternative_media_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alternativeMediaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="assetNameInput")
    def asset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contentKeyInput")
    def content_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaStreamingLocatorContentKey"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaStreamingLocatorContentKey"]]], jsii.get(self, "contentKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyPolicyNameInput")
    def default_content_key_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultContentKeyPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

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
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingLocatorIdInput")
    def streaming_locator_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamingLocatorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingPolicyNameInput")
    def streaming_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamingPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaStreamingLocatorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaStreamingLocatorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="alternativeMediaId")
    def alternative_media_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alternativeMediaId"))

    @alternative_media_id.setter
    def alternative_media_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "alternative_media_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alternativeMediaId", value)

    @builtins.property
    @jsii.member(jsii_name="assetName")
    def asset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assetName"))

    @asset_name.setter
    def asset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "asset_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyPolicyName")
    def default_content_key_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultContentKeyPolicyName"))

    @default_content_key_policy_name.setter
    def default_content_key_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "default_content_key_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultContentKeyPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountName")
    def media_services_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaServicesAccountName"))

    @media_services_account_name.setter
    def media_services_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "media_services_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaServicesAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="streamingLocatorId")
    def streaming_locator_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamingLocatorId"))

    @streaming_locator_id.setter
    def streaming_locator_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "streaming_locator_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingLocatorId", value)

    @builtins.property
    @jsii.member(jsii_name="streamingPolicyName")
    def streaming_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamingPolicyName"))

    @streaming_policy_name.setter
    def streaming_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocator, "streaming_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingPolicyName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "asset_name": "assetName",
        "media_services_account_name": "mediaServicesAccountName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "streaming_policy_name": "streamingPolicyName",
        "alternative_media_id": "alternativeMediaId",
        "content_key": "contentKey",
        "default_content_key_policy_name": "defaultContentKeyPolicyName",
        "end_time": "endTime",
        "id": "id",
        "start_time": "startTime",
        "streaming_locator_id": "streamingLocatorId",
        "timeouts": "timeouts",
    },
)
class MediaStreamingLocatorConfig(cdktf.TerraformMetaArguments):
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
        asset_name: builtins.str,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        streaming_policy_name: builtins.str,
        alternative_media_id: typing.Optional[builtins.str] = None,
        content_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaStreamingLocatorContentKey", typing.Dict[str, typing.Any]]]]] = None,
        default_content_key_policy_name: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        streaming_locator_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MediaStreamingLocatorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param asset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#asset_name MediaStreamingLocator#asset_name}.
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#media_services_account_name MediaStreamingLocator#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#name MediaStreamingLocator#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#resource_group_name MediaStreamingLocator#resource_group_name}.
        :param streaming_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_policy_name MediaStreamingLocator#streaming_policy_name}.
        :param alternative_media_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#alternative_media_id MediaStreamingLocator#alternative_media_id}.
        :param content_key: content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#content_key MediaStreamingLocator#content_key}
        :param default_content_key_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#default_content_key_policy_name MediaStreamingLocator#default_content_key_policy_name}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#end_time MediaStreamingLocator#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#id MediaStreamingLocator#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#start_time MediaStreamingLocator#start_time}.
        :param streaming_locator_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_locator_id MediaStreamingLocator#streaming_locator_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#timeouts MediaStreamingLocator#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MediaStreamingLocatorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocatorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument asset_name", value=asset_name, expected_type=type_hints["asset_name"])
            check_type(argname="argument media_services_account_name", value=media_services_account_name, expected_type=type_hints["media_services_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument streaming_policy_name", value=streaming_policy_name, expected_type=type_hints["streaming_policy_name"])
            check_type(argname="argument alternative_media_id", value=alternative_media_id, expected_type=type_hints["alternative_media_id"])
            check_type(argname="argument content_key", value=content_key, expected_type=type_hints["content_key"])
            check_type(argname="argument default_content_key_policy_name", value=default_content_key_policy_name, expected_type=type_hints["default_content_key_policy_name"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument streaming_locator_id", value=streaming_locator_id, expected_type=type_hints["streaming_locator_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "asset_name": asset_name,
            "media_services_account_name": media_services_account_name,
            "name": name,
            "resource_group_name": resource_group_name,
            "streaming_policy_name": streaming_policy_name,
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
        if alternative_media_id is not None:
            self._values["alternative_media_id"] = alternative_media_id
        if content_key is not None:
            self._values["content_key"] = content_key
        if default_content_key_policy_name is not None:
            self._values["default_content_key_policy_name"] = default_content_key_policy_name
        if end_time is not None:
            self._values["end_time"] = end_time
        if id is not None:
            self._values["id"] = id
        if start_time is not None:
            self._values["start_time"] = start_time
        if streaming_locator_id is not None:
            self._values["streaming_locator_id"] = streaming_locator_id
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
    def asset_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#asset_name MediaStreamingLocator#asset_name}.'''
        result = self._values.get("asset_name")
        assert result is not None, "Required property 'asset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def media_services_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#media_services_account_name MediaStreamingLocator#media_services_account_name}.'''
        result = self._values.get("media_services_account_name")
        assert result is not None, "Required property 'media_services_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#name MediaStreamingLocator#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#resource_group_name MediaStreamingLocator#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def streaming_policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_policy_name MediaStreamingLocator#streaming_policy_name}.'''
        result = self._values.get("streaming_policy_name")
        assert result is not None, "Required property 'streaming_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alternative_media_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#alternative_media_id MediaStreamingLocator#alternative_media_id}.'''
        result = self._values.get("alternative_media_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaStreamingLocatorContentKey"]]]:
        '''content_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#content_key MediaStreamingLocator#content_key}
        '''
        result = self._values.get("content_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaStreamingLocatorContentKey"]]], result)

    @builtins.property
    def default_content_key_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#default_content_key_policy_name MediaStreamingLocator#default_content_key_policy_name}.'''
        result = self._values.get("default_content_key_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#end_time MediaStreamingLocator#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#id MediaStreamingLocator#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#start_time MediaStreamingLocator#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def streaming_locator_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#streaming_locator_id MediaStreamingLocator#streaming_locator_id}.'''
        result = self._values.get("streaming_locator_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaStreamingLocatorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#timeouts MediaStreamingLocator#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaStreamingLocatorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingLocatorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorContentKey",
    jsii_struct_bases=[],
    name_mapping={
        "content_key_id": "contentKeyId",
        "label_reference_in_streaming_policy": "labelReferenceInStreamingPolicy",
        "policy_name": "policyName",
        "type": "type",
        "value": "value",
    },
)
class MediaStreamingLocatorContentKey:
    def __init__(
        self,
        *,
        content_key_id: typing.Optional[builtins.str] = None,
        label_reference_in_streaming_policy: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#content_key_id MediaStreamingLocator#content_key_id}.
        :param label_reference_in_streaming_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#label_reference_in_streaming_policy MediaStreamingLocator#label_reference_in_streaming_policy}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#policy_name MediaStreamingLocator#policy_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#type MediaStreamingLocator#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#value MediaStreamingLocator#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocatorContentKey.__init__)
            check_type(argname="argument content_key_id", value=content_key_id, expected_type=type_hints["content_key_id"])
            check_type(argname="argument label_reference_in_streaming_policy", value=label_reference_in_streaming_policy, expected_type=type_hints["label_reference_in_streaming_policy"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content_key_id is not None:
            self._values["content_key_id"] = content_key_id
        if label_reference_in_streaming_policy is not None:
            self._values["label_reference_in_streaming_policy"] = label_reference_in_streaming_policy
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def content_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#content_key_id MediaStreamingLocator#content_key_id}.'''
        result = self._values.get("content_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_reference_in_streaming_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#label_reference_in_streaming_policy MediaStreamingLocator#label_reference_in_streaming_policy}.'''
        result = self._values.get("label_reference_in_streaming_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#policy_name MediaStreamingLocator#policy_name}.'''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#type MediaStreamingLocator#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#value MediaStreamingLocator#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingLocatorContentKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingLocatorContentKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorContentKeyList",
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
            type_hints = typing.get_type_hints(MediaStreamingLocatorContentKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaStreamingLocatorContentKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocatorContentKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaStreamingLocatorContentKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaStreamingLocatorContentKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaStreamingLocatorContentKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaStreamingLocatorContentKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaStreamingLocatorContentKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorContentKeyOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingLocatorContentKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContentKeyId")
    def reset_content_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentKeyId", []))

    @jsii.member(jsii_name="resetLabelReferenceInStreamingPolicy")
    def reset_label_reference_in_streaming_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelReferenceInStreamingPolicy", []))

    @jsii.member(jsii_name="resetPolicyName")
    def reset_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="contentKeyIdInput")
    def content_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="labelReferenceInStreamingPolicyInput")
    def label_reference_in_streaming_policy_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelReferenceInStreamingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="contentKeyId")
    def content_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentKeyId"))

    @content_key_id.setter
    def content_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "content_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="labelReferenceInStreamingPolicy")
    def label_reference_in_streaming_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelReferenceInStreamingPolicy"))

    @label_reference_in_streaming_policy.setter
    def label_reference_in_streaming_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "label_reference_in_streaming_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelReferenceInStreamingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaStreamingLocatorContentKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaStreamingLocatorContentKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaStreamingLocatorContentKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorContentKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class MediaStreamingLocatorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#create MediaStreamingLocator#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#delete MediaStreamingLocator#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#read MediaStreamingLocator#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingLocatorTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#create MediaStreamingLocator#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#delete MediaStreamingLocator#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_locator#read MediaStreamingLocator#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingLocatorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingLocatorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingLocator.MediaStreamingLocatorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingLocatorTimeoutsOutputReference.__init__)
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
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaStreamingLocatorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaStreamingLocatorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaStreamingLocatorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingLocatorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaStreamingLocator",
    "MediaStreamingLocatorConfig",
    "MediaStreamingLocatorContentKey",
    "MediaStreamingLocatorContentKeyList",
    "MediaStreamingLocatorContentKeyOutputReference",
    "MediaStreamingLocatorTimeouts",
    "MediaStreamingLocatorTimeoutsOutputReference",
]

publication.publish()
