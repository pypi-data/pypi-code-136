'''
# `azurerm_media_live_event`

Refer to the Terraform Registory for docs: [`azurerm_media_live_event`](https://www.terraform.io/docs/providers/azurerm/r/media_live_event).
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


class MediaLiveEvent(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEvent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event azurerm_media_live_event}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        input: typing.Union["MediaLiveEventInput", typing.Dict[str, typing.Any]],
        location: builtins.str,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        auto_start_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cross_site_access_policy: typing.Optional[typing.Union["MediaLiveEventCrossSiteAccessPolicy", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        encoding: typing.Optional[typing.Union["MediaLiveEventEncoding", typing.Dict[str, typing.Any]]] = None,
        hostname_prefix: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        preview: typing.Optional[typing.Union["MediaLiveEventPreview", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MediaLiveEventTimeouts", typing.Dict[str, typing.Any]]] = None,
        transcription_languages: typing.Optional[typing.Sequence[builtins.str]] = None,
        use_static_hostname: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event azurerm_media_live_event} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#input MediaLiveEvent#input}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#location MediaLiveEvent#location}.
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#media_services_account_name MediaLiveEvent#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#resource_group_name MediaLiveEvent#resource_group_name}.
        :param auto_start_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#auto_start_enabled MediaLiveEvent#auto_start_enabled}.
        :param cross_site_access_policy: cross_site_access_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_site_access_policy MediaLiveEvent#cross_site_access_policy}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#description MediaLiveEvent#description}.
        :param encoding: encoding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#encoding MediaLiveEvent#encoding}
        :param hostname_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#hostname_prefix MediaLiveEvent#hostname_prefix}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#id MediaLiveEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param preview: preview block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview MediaLiveEvent#preview}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#tags MediaLiveEvent#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#timeouts MediaLiveEvent#timeouts}
        :param transcription_languages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#transcription_languages MediaLiveEvent#transcription_languages}.
        :param use_static_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#use_static_hostname MediaLiveEvent#use_static_hostname}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEvent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaLiveEventConfig(
            input=input,
            location=location,
            media_services_account_name=media_services_account_name,
            name=name,
            resource_group_name=resource_group_name,
            auto_start_enabled=auto_start_enabled,
            cross_site_access_policy=cross_site_access_policy,
            description=description,
            encoding=encoding,
            hostname_prefix=hostname_prefix,
            id=id,
            preview=preview,
            tags=tags,
            timeouts=timeouts,
            transcription_languages=transcription_languages,
            use_static_hostname=use_static_hostname,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCrossSiteAccessPolicy")
    def put_cross_site_access_policy(
        self,
        *,
        client_access_policy: typing.Optional[builtins.str] = None,
        cross_domain_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#client_access_policy MediaLiveEvent#client_access_policy}.
        :param cross_domain_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_domain_policy MediaLiveEvent#cross_domain_policy}.
        '''
        value = MediaLiveEventCrossSiteAccessPolicy(
            client_access_policy=client_access_policy,
            cross_domain_policy=cross_domain_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putCrossSiteAccessPolicy", [value]))

    @jsii.member(jsii_name="putEncoding")
    def put_encoding(
        self,
        *,
        key_frame_interval: typing.Optional[builtins.str] = None,
        preset_name: typing.Optional[builtins.str] = None,
        stretch_mode: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_frame_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval MediaLiveEvent#key_frame_interval}.
        :param preset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preset_name MediaLiveEvent#preset_name}.
        :param stretch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#stretch_mode MediaLiveEvent#stretch_mode}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#type MediaLiveEvent#type}.
        '''
        value = MediaLiveEventEncoding(
            key_frame_interval=key_frame_interval,
            preset_name=preset_name,
            stretch_mode=stretch_mode,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putEncoding", [value]))

    @jsii.member(jsii_name="putInput")
    def put_input(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        ip_access_control_allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaLiveEventInputIpAccessControlAllow", typing.Dict[str, typing.Any]]]]] = None,
        key_frame_interval_duration: typing.Optional[builtins.str] = None,
        streaming_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#access_token MediaLiveEvent#access_token}.
        :param ip_access_control_allow: ip_access_control_allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        :param key_frame_interval_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval_duration MediaLiveEvent#key_frame_interval_duration}.
        :param streaming_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_protocol MediaLiveEvent#streaming_protocol}.
        '''
        value = MediaLiveEventInput(
            access_token=access_token,
            ip_access_control_allow=ip_access_control_allow,
            key_frame_interval_duration=key_frame_interval_duration,
            streaming_protocol=streaming_protocol,
        )

        return typing.cast(None, jsii.invoke(self, "putInput", [value]))

    @jsii.member(jsii_name="putPreview")
    def put_preview(
        self,
        *,
        alternative_media_id: typing.Optional[builtins.str] = None,
        ip_access_control_allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaLiveEventPreviewIpAccessControlAllow", typing.Dict[str, typing.Any]]]]] = None,
        preview_locator: typing.Optional[builtins.str] = None,
        streaming_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alternative_media_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#alternative_media_id MediaLiveEvent#alternative_media_id}.
        :param ip_access_control_allow: ip_access_control_allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        :param preview_locator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview_locator MediaLiveEvent#preview_locator}.
        :param streaming_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_policy_name MediaLiveEvent#streaming_policy_name}.
        '''
        value = MediaLiveEventPreview(
            alternative_media_id=alternative_media_id,
            ip_access_control_allow=ip_access_control_allow,
            preview_locator=preview_locator,
            streaming_policy_name=streaming_policy_name,
        )

        return typing.cast(None, jsii.invoke(self, "putPreview", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#create MediaLiveEvent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#delete MediaLiveEvent#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#read MediaLiveEvent#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#update MediaLiveEvent#update}.
        '''
        value = MediaLiveEventTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoStartEnabled")
    def reset_auto_start_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStartEnabled", []))

    @jsii.member(jsii_name="resetCrossSiteAccessPolicy")
    def reset_cross_site_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSiteAccessPolicy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetHostnamePrefix")
    def reset_hostname_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostnamePrefix", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPreview")
    def reset_preview(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreview", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTranscriptionLanguages")
    def reset_transcription_languages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTranscriptionLanguages", []))

    @jsii.member(jsii_name="resetUseStaticHostname")
    def reset_use_static_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseStaticHostname", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="crossSiteAccessPolicy")
    def cross_site_access_policy(
        self,
    ) -> "MediaLiveEventCrossSiteAccessPolicyOutputReference":
        return typing.cast("MediaLiveEventCrossSiteAccessPolicyOutputReference", jsii.get(self, "crossSiteAccessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> "MediaLiveEventEncodingOutputReference":
        return typing.cast("MediaLiveEventEncodingOutputReference", jsii.get(self, "encoding"))

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> "MediaLiveEventInputOutputReference":
        return typing.cast("MediaLiveEventInputOutputReference", jsii.get(self, "input"))

    @builtins.property
    @jsii.member(jsii_name="preview")
    def preview(self) -> "MediaLiveEventPreviewOutputReference":
        return typing.cast("MediaLiveEventPreviewOutputReference", jsii.get(self, "preview"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaLiveEventTimeoutsOutputReference":
        return typing.cast("MediaLiveEventTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoStartEnabledInput")
    def auto_start_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoStartEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSiteAccessPolicyInput")
    def cross_site_access_policy_input(
        self,
    ) -> typing.Optional["MediaLiveEventCrossSiteAccessPolicy"]:
        return typing.cast(typing.Optional["MediaLiveEventCrossSiteAccessPolicy"], jsii.get(self, "crossSiteAccessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional["MediaLiveEventEncoding"]:
        return typing.cast(typing.Optional["MediaLiveEventEncoding"], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnamePrefixInput")
    def hostname_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(self) -> typing.Optional["MediaLiveEventInput"]:
        return typing.cast(typing.Optional["MediaLiveEventInput"], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountNameInput")
    def media_services_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediaServicesAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="previewInput")
    def preview_input(self) -> typing.Optional["MediaLiveEventPreview"]:
        return typing.cast(typing.Optional["MediaLiveEventPreview"], jsii.get(self, "previewInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaLiveEventTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaLiveEventTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transcriptionLanguagesInput")
    def transcription_languages_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transcriptionLanguagesInput"))

    @builtins.property
    @jsii.member(jsii_name="useStaticHostnameInput")
    def use_static_hostname_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useStaticHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStartEnabled")
    def auto_start_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoStartEnabled"))

    @auto_start_enabled.setter
    def auto_start_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "auto_start_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStartEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hostnamePrefix")
    def hostname_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostnamePrefix"))

    @hostname_prefix.setter
    def hostname_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "hostname_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountName")
    def media_services_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaServicesAccountName"))

    @media_services_account_name.setter
    def media_services_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "media_services_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaServicesAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="transcriptionLanguages")
    def transcription_languages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transcriptionLanguages"))

    @transcription_languages.setter
    def transcription_languages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "transcription_languages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transcriptionLanguages", value)

    @builtins.property
    @jsii.member(jsii_name="useStaticHostname")
    def use_static_hostname(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useStaticHostname"))

    @use_static_hostname.setter
    def use_static_hostname(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEvent, "use_static_hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useStaticHostname", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "input": "input",
        "location": "location",
        "media_services_account_name": "mediaServicesAccountName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "auto_start_enabled": "autoStartEnabled",
        "cross_site_access_policy": "crossSiteAccessPolicy",
        "description": "description",
        "encoding": "encoding",
        "hostname_prefix": "hostnamePrefix",
        "id": "id",
        "preview": "preview",
        "tags": "tags",
        "timeouts": "timeouts",
        "transcription_languages": "transcriptionLanguages",
        "use_static_hostname": "useStaticHostname",
    },
)
class MediaLiveEventConfig(cdktf.TerraformMetaArguments):
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
        input: typing.Union["MediaLiveEventInput", typing.Dict[str, typing.Any]],
        location: builtins.str,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        auto_start_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cross_site_access_policy: typing.Optional[typing.Union["MediaLiveEventCrossSiteAccessPolicy", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        encoding: typing.Optional[typing.Union["MediaLiveEventEncoding", typing.Dict[str, typing.Any]]] = None,
        hostname_prefix: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        preview: typing.Optional[typing.Union["MediaLiveEventPreview", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MediaLiveEventTimeouts", typing.Dict[str, typing.Any]]] = None,
        transcription_languages: typing.Optional[typing.Sequence[builtins.str]] = None,
        use_static_hostname: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#input MediaLiveEvent#input}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#location MediaLiveEvent#location}.
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#media_services_account_name MediaLiveEvent#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#resource_group_name MediaLiveEvent#resource_group_name}.
        :param auto_start_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#auto_start_enabled MediaLiveEvent#auto_start_enabled}.
        :param cross_site_access_policy: cross_site_access_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_site_access_policy MediaLiveEvent#cross_site_access_policy}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#description MediaLiveEvent#description}.
        :param encoding: encoding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#encoding MediaLiveEvent#encoding}
        :param hostname_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#hostname_prefix MediaLiveEvent#hostname_prefix}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#id MediaLiveEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param preview: preview block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview MediaLiveEvent#preview}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#tags MediaLiveEvent#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#timeouts MediaLiveEvent#timeouts}
        :param transcription_languages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#transcription_languages MediaLiveEvent#transcription_languages}.
        :param use_static_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#use_static_hostname MediaLiveEvent#use_static_hostname}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(input, dict):
            input = MediaLiveEventInput(**input)
        if isinstance(cross_site_access_policy, dict):
            cross_site_access_policy = MediaLiveEventCrossSiteAccessPolicy(**cross_site_access_policy)
        if isinstance(encoding, dict):
            encoding = MediaLiveEventEncoding(**encoding)
        if isinstance(preview, dict):
            preview = MediaLiveEventPreview(**preview)
        if isinstance(timeouts, dict):
            timeouts = MediaLiveEventTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument media_services_account_name", value=media_services_account_name, expected_type=type_hints["media_services_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument auto_start_enabled", value=auto_start_enabled, expected_type=type_hints["auto_start_enabled"])
            check_type(argname="argument cross_site_access_policy", value=cross_site_access_policy, expected_type=type_hints["cross_site_access_policy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument hostname_prefix", value=hostname_prefix, expected_type=type_hints["hostname_prefix"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument preview", value=preview, expected_type=type_hints["preview"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transcription_languages", value=transcription_languages, expected_type=type_hints["transcription_languages"])
            check_type(argname="argument use_static_hostname", value=use_static_hostname, expected_type=type_hints["use_static_hostname"])
        self._values: typing.Dict[str, typing.Any] = {
            "input": input,
            "location": location,
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
        if auto_start_enabled is not None:
            self._values["auto_start_enabled"] = auto_start_enabled
        if cross_site_access_policy is not None:
            self._values["cross_site_access_policy"] = cross_site_access_policy
        if description is not None:
            self._values["description"] = description
        if encoding is not None:
            self._values["encoding"] = encoding
        if hostname_prefix is not None:
            self._values["hostname_prefix"] = hostname_prefix
        if id is not None:
            self._values["id"] = id
        if preview is not None:
            self._values["preview"] = preview
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transcription_languages is not None:
            self._values["transcription_languages"] = transcription_languages
        if use_static_hostname is not None:
            self._values["use_static_hostname"] = use_static_hostname

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
    def input(self) -> "MediaLiveEventInput":
        '''input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#input MediaLiveEvent#input}
        '''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast("MediaLiveEventInput", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#location MediaLiveEvent#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def media_services_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#media_services_account_name MediaLiveEvent#media_services_account_name}.'''
        result = self._values.get("media_services_account_name")
        assert result is not None, "Required property 'media_services_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#resource_group_name MediaLiveEvent#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_start_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#auto_start_enabled MediaLiveEvent#auto_start_enabled}.'''
        result = self._values.get("auto_start_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cross_site_access_policy(
        self,
    ) -> typing.Optional["MediaLiveEventCrossSiteAccessPolicy"]:
        '''cross_site_access_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_site_access_policy MediaLiveEvent#cross_site_access_policy}
        '''
        result = self._values.get("cross_site_access_policy")
        return typing.cast(typing.Optional["MediaLiveEventCrossSiteAccessPolicy"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#description MediaLiveEvent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding(self) -> typing.Optional["MediaLiveEventEncoding"]:
        '''encoding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#encoding MediaLiveEvent#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional["MediaLiveEventEncoding"], result)

    @builtins.property
    def hostname_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#hostname_prefix MediaLiveEvent#hostname_prefix}.'''
        result = self._values.get("hostname_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#id MediaLiveEvent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preview(self) -> typing.Optional["MediaLiveEventPreview"]:
        '''preview block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview MediaLiveEvent#preview}
        '''
        result = self._values.get("preview")
        return typing.cast(typing.Optional["MediaLiveEventPreview"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#tags MediaLiveEvent#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaLiveEventTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#timeouts MediaLiveEvent#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaLiveEventTimeouts"], result)

    @builtins.property
    def transcription_languages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#transcription_languages MediaLiveEvent#transcription_languages}.'''
        result = self._values.get("transcription_languages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def use_static_hostname(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#use_static_hostname MediaLiveEvent#use_static_hostname}.'''
        result = self._values.get("use_static_hostname")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventCrossSiteAccessPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "client_access_policy": "clientAccessPolicy",
        "cross_domain_policy": "crossDomainPolicy",
    },
)
class MediaLiveEventCrossSiteAccessPolicy:
    def __init__(
        self,
        *,
        client_access_policy: typing.Optional[builtins.str] = None,
        cross_domain_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#client_access_policy MediaLiveEvent#client_access_policy}.
        :param cross_domain_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_domain_policy MediaLiveEvent#cross_domain_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventCrossSiteAccessPolicy.__init__)
            check_type(argname="argument client_access_policy", value=client_access_policy, expected_type=type_hints["client_access_policy"])
            check_type(argname="argument cross_domain_policy", value=cross_domain_policy, expected_type=type_hints["cross_domain_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_access_policy is not None:
            self._values["client_access_policy"] = client_access_policy
        if cross_domain_policy is not None:
            self._values["cross_domain_policy"] = cross_domain_policy

    @builtins.property
    def client_access_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#client_access_policy MediaLiveEvent#client_access_policy}.'''
        result = self._values.get("client_access_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_domain_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#cross_domain_policy MediaLiveEvent#cross_domain_policy}.'''
        result = self._values.get("cross_domain_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventCrossSiteAccessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventCrossSiteAccessPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventCrossSiteAccessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventCrossSiteAccessPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientAccessPolicy")
    def reset_client_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAccessPolicy", []))

    @jsii.member(jsii_name="resetCrossDomainPolicy")
    def reset_cross_domain_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossDomainPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientAccessPolicyInput")
    def client_access_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientAccessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="crossDomainPolicyInput")
    def cross_domain_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossDomainPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAccessPolicy")
    def client_access_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAccessPolicy"))

    @client_access_policy.setter
    def client_access_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventCrossSiteAccessPolicyOutputReference, "client_access_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAccessPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="crossDomainPolicy")
    def cross_domain_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossDomainPolicy"))

    @cross_domain_policy.setter
    def cross_domain_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventCrossSiteAccessPolicyOutputReference, "cross_domain_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossDomainPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventCrossSiteAccessPolicy]:
        return typing.cast(typing.Optional[MediaLiveEventCrossSiteAccessPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaLiveEventCrossSiteAccessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventCrossSiteAccessPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventEncoding",
    jsii_struct_bases=[],
    name_mapping={
        "key_frame_interval": "keyFrameInterval",
        "preset_name": "presetName",
        "stretch_mode": "stretchMode",
        "type": "type",
    },
)
class MediaLiveEventEncoding:
    def __init__(
        self,
        *,
        key_frame_interval: typing.Optional[builtins.str] = None,
        preset_name: typing.Optional[builtins.str] = None,
        stretch_mode: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_frame_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval MediaLiveEvent#key_frame_interval}.
        :param preset_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preset_name MediaLiveEvent#preset_name}.
        :param stretch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#stretch_mode MediaLiveEvent#stretch_mode}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#type MediaLiveEvent#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventEncoding.__init__)
            check_type(argname="argument key_frame_interval", value=key_frame_interval, expected_type=type_hints["key_frame_interval"])
            check_type(argname="argument preset_name", value=preset_name, expected_type=type_hints["preset_name"])
            check_type(argname="argument stretch_mode", value=stretch_mode, expected_type=type_hints["stretch_mode"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key_frame_interval is not None:
            self._values["key_frame_interval"] = key_frame_interval
        if preset_name is not None:
            self._values["preset_name"] = preset_name
        if stretch_mode is not None:
            self._values["stretch_mode"] = stretch_mode
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def key_frame_interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval MediaLiveEvent#key_frame_interval}.'''
        result = self._values.get("key_frame_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preset_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preset_name MediaLiveEvent#preset_name}.'''
        result = self._values.get("preset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stretch_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#stretch_mode MediaLiveEvent#stretch_mode}.'''
        result = self._values.get("stretch_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#type MediaLiveEvent#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventEncoding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventEncodingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventEncodingOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventEncodingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyFrameInterval")
    def reset_key_frame_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyFrameInterval", []))

    @jsii.member(jsii_name="resetPresetName")
    def reset_preset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresetName", []))

    @jsii.member(jsii_name="resetStretchMode")
    def reset_stretch_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStretchMode", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="keyFrameIntervalInput")
    def key_frame_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFrameIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="presetNameInput")
    def preset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "presetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="stretchModeInput")
    def stretch_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stretchModeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyFrameInterval")
    def key_frame_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyFrameInterval"))

    @key_frame_interval.setter
    def key_frame_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventEncodingOutputReference, "key_frame_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyFrameInterval", value)

    @builtins.property
    @jsii.member(jsii_name="presetName")
    def preset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "presetName"))

    @preset_name.setter
    def preset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventEncodingOutputReference, "preset_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presetName", value)

    @builtins.property
    @jsii.member(jsii_name="stretchMode")
    def stretch_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stretchMode"))

    @stretch_mode.setter
    def stretch_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventEncodingOutputReference, "stretch_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stretchMode", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventEncodingOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventEncoding]:
        return typing.cast(typing.Optional[MediaLiveEventEncoding], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MediaLiveEventEncoding]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventEncodingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInput",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "ip_access_control_allow": "ipAccessControlAllow",
        "key_frame_interval_duration": "keyFrameIntervalDuration",
        "streaming_protocol": "streamingProtocol",
    },
)
class MediaLiveEventInput:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        ip_access_control_allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaLiveEventInputIpAccessControlAllow", typing.Dict[str, typing.Any]]]]] = None,
        key_frame_interval_duration: typing.Optional[builtins.str] = None,
        streaming_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#access_token MediaLiveEvent#access_token}.
        :param ip_access_control_allow: ip_access_control_allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        :param key_frame_interval_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval_duration MediaLiveEvent#key_frame_interval_duration}.
        :param streaming_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_protocol MediaLiveEvent#streaming_protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventInput.__init__)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument ip_access_control_allow", value=ip_access_control_allow, expected_type=type_hints["ip_access_control_allow"])
            check_type(argname="argument key_frame_interval_duration", value=key_frame_interval_duration, expected_type=type_hints["key_frame_interval_duration"])
            check_type(argname="argument streaming_protocol", value=streaming_protocol, expected_type=type_hints["streaming_protocol"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if ip_access_control_allow is not None:
            self._values["ip_access_control_allow"] = ip_access_control_allow
        if key_frame_interval_duration is not None:
            self._values["key_frame_interval_duration"] = key_frame_interval_duration
        if streaming_protocol is not None:
            self._values["streaming_protocol"] = streaming_protocol

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#access_token MediaLiveEvent#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_access_control_allow(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaLiveEventInputIpAccessControlAllow"]]]:
        '''ip_access_control_allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        '''
        result = self._values.get("ip_access_control_allow")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaLiveEventInputIpAccessControlAllow"]]], result)

    @builtins.property
    def key_frame_interval_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#key_frame_interval_duration MediaLiveEvent#key_frame_interval_duration}.'''
        result = self._values.get("key_frame_interval_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def streaming_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_protocol MediaLiveEvent#streaming_protocol}.'''
        result = self._values.get("streaming_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputEndpoint",
    jsii_struct_bases=[],
    name_mapping={},
)
class MediaLiveEventInputEndpoint:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventInputEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventInputEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputEndpointList",
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
            type_hints = typing.get_type_hints(MediaLiveEventInputEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MediaLiveEventInputEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventInputEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaLiveEventInputEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MediaLiveEventInputEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputEndpointOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventInputEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventInputEndpoint]:
        return typing.cast(typing.Optional[MediaLiveEventInputEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaLiveEventInputEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputIpAccessControlAllow",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "name": "name",
        "subnet_prefix_length": "subnetPrefixLength",
    },
)
class MediaLiveEventInputIpAccessControlAllow:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        subnet_prefix_length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#address MediaLiveEvent#address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.
        :param subnet_prefix_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#subnet_prefix_length MediaLiveEvent#subnet_prefix_length}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventInputIpAccessControlAllow.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_prefix_length", value=subnet_prefix_length, expected_type=type_hints["subnet_prefix_length"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if name is not None:
            self._values["name"] = name
        if subnet_prefix_length is not None:
            self._values["subnet_prefix_length"] = subnet_prefix_length

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#address MediaLiveEvent#address}.'''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_prefix_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#subnet_prefix_length MediaLiveEvent#subnet_prefix_length}.'''
        result = self._values.get("subnet_prefix_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventInputIpAccessControlAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventInputIpAccessControlAllowList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputIpAccessControlAllowList",
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
            type_hints = typing.get_type_hints(MediaLiveEventInputIpAccessControlAllowList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaLiveEventInputIpAccessControlAllowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventInputIpAccessControlAllowList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaLiveEventInputIpAccessControlAllowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventInputIpAccessControlAllow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventInputIpAccessControlAllow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventInputIpAccessControlAllow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaLiveEventInputIpAccessControlAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputIpAccessControlAllowOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventInputIpAccessControlAllowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSubnetPrefixLength")
    def reset_subnet_prefix_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetPrefixLength", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetPrefixLengthInput")
    def subnet_prefix_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subnetPrefixLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subnetPrefixLength")
    def subnet_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subnetPrefixLength"))

    @subnet_prefix_length.setter
    def subnet_prefix_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowOutputReference, "subnet_prefix_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetPrefixLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaLiveEventInputIpAccessControlAllow, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaLiveEventInputIpAccessControlAllow, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaLiveEventInputIpAccessControlAllow, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputIpAccessControlAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaLiveEventInputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventInputOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventInputOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIpAccessControlAllow")
    def put_ip_access_control_allow(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MediaLiveEventInputIpAccessControlAllow, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventInputOutputReference.put_ip_access_control_allow)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpAccessControlAllow", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetIpAccessControlAllow")
    def reset_ip_access_control_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAccessControlAllow", []))

    @jsii.member(jsii_name="resetKeyFrameIntervalDuration")
    def reset_key_frame_interval_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyFrameIntervalDuration", []))

    @jsii.member(jsii_name="resetStreamingProtocol")
    def reset_streaming_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamingProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> MediaLiveEventInputEndpointList:
        return typing.cast(MediaLiveEventInputEndpointList, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessControlAllow")
    def ip_access_control_allow(self) -> MediaLiveEventInputIpAccessControlAllowList:
        return typing.cast(MediaLiveEventInputIpAccessControlAllowList, jsii.get(self, "ipAccessControlAllow"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessControlAllowInput")
    def ip_access_control_allow_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventInputIpAccessControlAllow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventInputIpAccessControlAllow]]], jsii.get(self, "ipAccessControlAllowInput"))

    @builtins.property
    @jsii.member(jsii_name="keyFrameIntervalDurationInput")
    def key_frame_interval_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFrameIntervalDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingProtocolInput")
    def streaming_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamingProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputOutputReference, "access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="keyFrameIntervalDuration")
    def key_frame_interval_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyFrameIntervalDuration"))

    @key_frame_interval_duration.setter
    def key_frame_interval_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputOutputReference, "key_frame_interval_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyFrameIntervalDuration", value)

    @builtins.property
    @jsii.member(jsii_name="streamingProtocol")
    def streaming_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamingProtocol"))

    @streaming_protocol.setter
    def streaming_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputOutputReference, "streaming_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventInput]:
        return typing.cast(typing.Optional[MediaLiveEventInput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MediaLiveEventInput]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventInputOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreview",
    jsii_struct_bases=[],
    name_mapping={
        "alternative_media_id": "alternativeMediaId",
        "ip_access_control_allow": "ipAccessControlAllow",
        "preview_locator": "previewLocator",
        "streaming_policy_name": "streamingPolicyName",
    },
)
class MediaLiveEventPreview:
    def __init__(
        self,
        *,
        alternative_media_id: typing.Optional[builtins.str] = None,
        ip_access_control_allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaLiveEventPreviewIpAccessControlAllow", typing.Dict[str, typing.Any]]]]] = None,
        preview_locator: typing.Optional[builtins.str] = None,
        streaming_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alternative_media_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#alternative_media_id MediaLiveEvent#alternative_media_id}.
        :param ip_access_control_allow: ip_access_control_allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        :param preview_locator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview_locator MediaLiveEvent#preview_locator}.
        :param streaming_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_policy_name MediaLiveEvent#streaming_policy_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventPreview.__init__)
            check_type(argname="argument alternative_media_id", value=alternative_media_id, expected_type=type_hints["alternative_media_id"])
            check_type(argname="argument ip_access_control_allow", value=ip_access_control_allow, expected_type=type_hints["ip_access_control_allow"])
            check_type(argname="argument preview_locator", value=preview_locator, expected_type=type_hints["preview_locator"])
            check_type(argname="argument streaming_policy_name", value=streaming_policy_name, expected_type=type_hints["streaming_policy_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alternative_media_id is not None:
            self._values["alternative_media_id"] = alternative_media_id
        if ip_access_control_allow is not None:
            self._values["ip_access_control_allow"] = ip_access_control_allow
        if preview_locator is not None:
            self._values["preview_locator"] = preview_locator
        if streaming_policy_name is not None:
            self._values["streaming_policy_name"] = streaming_policy_name

    @builtins.property
    def alternative_media_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#alternative_media_id MediaLiveEvent#alternative_media_id}.'''
        result = self._values.get("alternative_media_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_access_control_allow(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaLiveEventPreviewIpAccessControlAllow"]]]:
        '''ip_access_control_allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#ip_access_control_allow MediaLiveEvent#ip_access_control_allow}
        '''
        result = self._values.get("ip_access_control_allow")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaLiveEventPreviewIpAccessControlAllow"]]], result)

    @builtins.property
    def preview_locator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#preview_locator MediaLiveEvent#preview_locator}.'''
        result = self._values.get("preview_locator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def streaming_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#streaming_policy_name MediaLiveEvent#streaming_policy_name}.'''
        result = self._values.get("streaming_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventPreview(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewEndpoint",
    jsii_struct_bases=[],
    name_mapping={},
)
class MediaLiveEventPreviewEndpoint:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventPreviewEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventPreviewEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewEndpointList",
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
            type_hints = typing.get_type_hints(MediaLiveEventPreviewEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MediaLiveEventPreviewEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventPreviewEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaLiveEventPreviewEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MediaLiveEventPreviewEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewEndpointOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventPreviewEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventPreviewEndpoint]:
        return typing.cast(typing.Optional[MediaLiveEventPreviewEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaLiveEventPreviewEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewIpAccessControlAllow",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "name": "name",
        "subnet_prefix_length": "subnetPrefixLength",
    },
)
class MediaLiveEventPreviewIpAccessControlAllow:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        subnet_prefix_length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#address MediaLiveEvent#address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.
        :param subnet_prefix_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#subnet_prefix_length MediaLiveEvent#subnet_prefix_length}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventPreviewIpAccessControlAllow.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_prefix_length", value=subnet_prefix_length, expected_type=type_hints["subnet_prefix_length"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if name is not None:
            self._values["name"] = name
        if subnet_prefix_length is not None:
            self._values["subnet_prefix_length"] = subnet_prefix_length

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#address MediaLiveEvent#address}.'''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#name MediaLiveEvent#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_prefix_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#subnet_prefix_length MediaLiveEvent#subnet_prefix_length}.'''
        result = self._values.get("subnet_prefix_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventPreviewIpAccessControlAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventPreviewIpAccessControlAllowList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewIpAccessControlAllowList",
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
            type_hints = typing.get_type_hints(MediaLiveEventPreviewIpAccessControlAllowList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaLiveEventPreviewIpAccessControlAllowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventPreviewIpAccessControlAllowList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaLiveEventPreviewIpAccessControlAllowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventPreviewIpAccessControlAllow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventPreviewIpAccessControlAllow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventPreviewIpAccessControlAllow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaLiveEventPreviewIpAccessControlAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewIpAccessControlAllowOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventPreviewIpAccessControlAllowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSubnetPrefixLength")
    def reset_subnet_prefix_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetPrefixLength", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetPrefixLengthInput")
    def subnet_prefix_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subnetPrefixLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subnetPrefixLength")
    def subnet_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subnetPrefixLength"))

    @subnet_prefix_length.setter
    def subnet_prefix_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowOutputReference, "subnet_prefix_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetPrefixLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaLiveEventPreviewIpAccessControlAllow, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaLiveEventPreviewIpAccessControlAllow, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaLiveEventPreviewIpAccessControlAllow, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewIpAccessControlAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaLiveEventPreviewOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventPreviewOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventPreviewOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIpAccessControlAllow")
    def put_ip_access_control_allow(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MediaLiveEventPreviewIpAccessControlAllow, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventPreviewOutputReference.put_ip_access_control_allow)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpAccessControlAllow", [value]))

    @jsii.member(jsii_name="resetAlternativeMediaId")
    def reset_alternative_media_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternativeMediaId", []))

    @jsii.member(jsii_name="resetIpAccessControlAllow")
    def reset_ip_access_control_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAccessControlAllow", []))

    @jsii.member(jsii_name="resetPreviewLocator")
    def reset_preview_locator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreviewLocator", []))

    @jsii.member(jsii_name="resetStreamingPolicyName")
    def reset_streaming_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamingPolicyName", []))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> MediaLiveEventPreviewEndpointList:
        return typing.cast(MediaLiveEventPreviewEndpointList, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessControlAllow")
    def ip_access_control_allow(self) -> MediaLiveEventPreviewIpAccessControlAllowList:
        return typing.cast(MediaLiveEventPreviewIpAccessControlAllowList, jsii.get(self, "ipAccessControlAllow"))

    @builtins.property
    @jsii.member(jsii_name="alternativeMediaIdInput")
    def alternative_media_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alternativeMediaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessControlAllowInput")
    def ip_access_control_allow_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventPreviewIpAccessControlAllow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaLiveEventPreviewIpAccessControlAllow]]], jsii.get(self, "ipAccessControlAllowInput"))

    @builtins.property
    @jsii.member(jsii_name="previewLocatorInput")
    def preview_locator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "previewLocatorInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingPolicyNameInput")
    def streaming_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamingPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="alternativeMediaId")
    def alternative_media_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alternativeMediaId"))

    @alternative_media_id.setter
    def alternative_media_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewOutputReference, "alternative_media_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alternativeMediaId", value)

    @builtins.property
    @jsii.member(jsii_name="previewLocator")
    def preview_locator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "previewLocator"))

    @preview_locator.setter
    def preview_locator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewOutputReference, "preview_locator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previewLocator", value)

    @builtins.property
    @jsii.member(jsii_name="streamingPolicyName")
    def streaming_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamingPolicyName"))

    @streaming_policy_name.setter
    def streaming_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewOutputReference, "streaming_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaLiveEventPreview]:
        return typing.cast(typing.Optional[MediaLiveEventPreview], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MediaLiveEventPreview]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventPreviewOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MediaLiveEventTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#create MediaLiveEvent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#delete MediaLiveEvent#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#read MediaLiveEvent#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#update MediaLiveEvent#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaLiveEventTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#create MediaLiveEvent#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#delete MediaLiveEvent#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#read MediaLiveEvent#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_live_event#update MediaLiveEvent#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaLiveEventTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaLiveEventTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaLiveEvent.MediaLiveEventTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaLiveEventTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MediaLiveEventTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaLiveEventTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaLiveEventTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaLiveEventTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaLiveEventTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaLiveEvent",
    "MediaLiveEventConfig",
    "MediaLiveEventCrossSiteAccessPolicy",
    "MediaLiveEventCrossSiteAccessPolicyOutputReference",
    "MediaLiveEventEncoding",
    "MediaLiveEventEncodingOutputReference",
    "MediaLiveEventInput",
    "MediaLiveEventInputEndpoint",
    "MediaLiveEventInputEndpointList",
    "MediaLiveEventInputEndpointOutputReference",
    "MediaLiveEventInputIpAccessControlAllow",
    "MediaLiveEventInputIpAccessControlAllowList",
    "MediaLiveEventInputIpAccessControlAllowOutputReference",
    "MediaLiveEventInputOutputReference",
    "MediaLiveEventPreview",
    "MediaLiveEventPreviewEndpoint",
    "MediaLiveEventPreviewEndpointList",
    "MediaLiveEventPreviewEndpointOutputReference",
    "MediaLiveEventPreviewIpAccessControlAllow",
    "MediaLiveEventPreviewIpAccessControlAllowList",
    "MediaLiveEventPreviewIpAccessControlAllowOutputReference",
    "MediaLiveEventPreviewOutputReference",
    "MediaLiveEventTimeouts",
    "MediaLiveEventTimeoutsOutputReference",
]

publication.publish()
