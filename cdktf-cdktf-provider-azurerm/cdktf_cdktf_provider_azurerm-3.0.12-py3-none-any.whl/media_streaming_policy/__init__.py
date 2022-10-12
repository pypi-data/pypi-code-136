'''
# `azurerm_media_streaming_policy`

Refer to the Terraform Registory for docs: [`azurerm_media_streaming_policy`](https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy).
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


class MediaStreamingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy azurerm_media_streaming_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        media_services_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        common_encryption_cbcs: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcs", typing.Dict[str, typing.Any]]] = None,
        common_encryption_cenc: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCenc", typing.Dict[str, typing.Any]]] = None,
        default_content_key_policy_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        no_encryption_enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyNoEncryptionEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MediaStreamingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy azurerm_media_streaming_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#media_services_account_name MediaStreamingPolicy#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#name MediaStreamingPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#resource_group_name MediaStreamingPolicy#resource_group_name}.
        :param common_encryption_cbcs: common_encryption_cbcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cbcs MediaStreamingPolicy#common_encryption_cbcs}
        :param common_encryption_cenc: common_encryption_cenc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cenc MediaStreamingPolicy#common_encryption_cenc}
        :param default_content_key_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key_policy_name MediaStreamingPolicy#default_content_key_policy_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#id MediaStreamingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param no_encryption_enabled_protocols: no_encryption_enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#no_encryption_enabled_protocols MediaStreamingPolicy#no_encryption_enabled_protocols}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#timeouts MediaStreamingPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaStreamingPolicyConfig(
            media_services_account_name=media_services_account_name,
            name=name,
            resource_group_name=resource_group_name,
            common_encryption_cbcs=common_encryption_cbcs,
            common_encryption_cenc=common_encryption_cenc,
            default_content_key_policy_name=default_content_key_policy_name,
            id=id,
            no_encryption_enabled_protocols=no_encryption_enabled_protocols,
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

    @jsii.member(jsii_name="putCommonEncryptionCbcs")
    def put_common_encryption_cbcs(
        self,
        *,
        default_content_key: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey", typing.Dict[str, typing.Any]]] = None,
        drm_fairplay: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay", typing.Dict[str, typing.Any]]] = None,
        enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_content_key: default_content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        :param drm_fairplay: drm_fairplay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_fairplay MediaStreamingPolicy#drm_fairplay}
        :param enabled_protocols: enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        value = MediaStreamingPolicyCommonEncryptionCbcs(
            default_content_key=default_content_key,
            drm_fairplay=drm_fairplay,
            enabled_protocols=enabled_protocols,
        )

        return typing.cast(None, jsii.invoke(self, "putCommonEncryptionCbcs", [value]))

    @jsii.member(jsii_name="putCommonEncryptionCenc")
    def put_common_encryption_cenc(
        self,
        *,
        default_content_key: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencDefaultContentKey", typing.Dict[str, typing.Any]]] = None,
        drm_playready: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencDrmPlayready", typing.Dict[str, typing.Any]]] = None,
        drm_widevine_custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
        enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_content_key: default_content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        :param drm_playready: drm_playready block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_playready MediaStreamingPolicy#drm_playready}
        :param drm_widevine_custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_widevine_custom_license_acquisition_url_template MediaStreamingPolicy#drm_widevine_custom_license_acquisition_url_template}.
        :param enabled_protocols: enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        value = MediaStreamingPolicyCommonEncryptionCenc(
            default_content_key=default_content_key,
            drm_playready=drm_playready,
            drm_widevine_custom_license_acquisition_url_template=drm_widevine_custom_license_acquisition_url_template,
            enabled_protocols=enabled_protocols,
        )

        return typing.cast(None, jsii.invoke(self, "putCommonEncryptionCenc", [value]))

    @jsii.member(jsii_name="putNoEncryptionEnabledProtocols")
    def put_no_encryption_enabled_protocols(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        value = MediaStreamingPolicyNoEncryptionEnabledProtocols(
            dash=dash, download=download, hls=hls, smooth_streaming=smooth_streaming
        )

        return typing.cast(None, jsii.invoke(self, "putNoEncryptionEnabledProtocols", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#create MediaStreamingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#delete MediaStreamingPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#read MediaStreamingPolicy#read}.
        '''
        value = MediaStreamingPolicyTimeouts(create=create, delete=delete, read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCommonEncryptionCbcs")
    def reset_common_encryption_cbcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonEncryptionCbcs", []))

    @jsii.member(jsii_name="resetCommonEncryptionCenc")
    def reset_common_encryption_cenc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonEncryptionCenc", []))

    @jsii.member(jsii_name="resetDefaultContentKeyPolicyName")
    def reset_default_content_key_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultContentKeyPolicyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNoEncryptionEnabledProtocols")
    def reset_no_encryption_enabled_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoEncryptionEnabledProtocols", []))

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
    @jsii.member(jsii_name="commonEncryptionCbcs")
    def common_encryption_cbcs(
        self,
    ) -> "MediaStreamingPolicyCommonEncryptionCbcsOutputReference":
        return typing.cast("MediaStreamingPolicyCommonEncryptionCbcsOutputReference", jsii.get(self, "commonEncryptionCbcs"))

    @builtins.property
    @jsii.member(jsii_name="commonEncryptionCenc")
    def common_encryption_cenc(
        self,
    ) -> "MediaStreamingPolicyCommonEncryptionCencOutputReference":
        return typing.cast("MediaStreamingPolicyCommonEncryptionCencOutputReference", jsii.get(self, "commonEncryptionCenc"))

    @builtins.property
    @jsii.member(jsii_name="noEncryptionEnabledProtocols")
    def no_encryption_enabled_protocols(
        self,
    ) -> "MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference":
        return typing.cast("MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference", jsii.get(self, "noEncryptionEnabledProtocols"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaStreamingPolicyTimeoutsOutputReference":
        return typing.cast("MediaStreamingPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="commonEncryptionCbcsInput")
    def common_encryption_cbcs_input(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCbcs"]:
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCbcs"], jsii.get(self, "commonEncryptionCbcsInput"))

    @builtins.property
    @jsii.member(jsii_name="commonEncryptionCencInput")
    def common_encryption_cenc_input(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCenc"]:
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCenc"], jsii.get(self, "commonEncryptionCencInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyPolicyNameInput")
    def default_content_key_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultContentKeyPolicyNameInput"))

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
    @jsii.member(jsii_name="noEncryptionEnabledProtocolsInput")
    def no_encryption_enabled_protocols_input(
        self,
    ) -> typing.Optional["MediaStreamingPolicyNoEncryptionEnabledProtocols"]:
        return typing.cast(typing.Optional["MediaStreamingPolicyNoEncryptionEnabledProtocols"], jsii.get(self, "noEncryptionEnabledProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaStreamingPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaStreamingPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyPolicyName")
    def default_content_key_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultContentKeyPolicyName"))

    @default_content_key_policy_name.setter
    def default_content_key_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicy, "default_content_key_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultContentKeyPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountName")
    def media_services_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaServicesAccountName"))

    @media_services_account_name.setter
    def media_services_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicy, "media_services_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaServicesAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcs",
    jsii_struct_bases=[],
    name_mapping={
        "default_content_key": "defaultContentKey",
        "drm_fairplay": "drmFairplay",
        "enabled_protocols": "enabledProtocols",
    },
)
class MediaStreamingPolicyCommonEncryptionCbcs:
    def __init__(
        self,
        *,
        default_content_key: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey", typing.Dict[str, typing.Any]]] = None,
        drm_fairplay: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay", typing.Dict[str, typing.Any]]] = None,
        enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_content_key: default_content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        :param drm_fairplay: drm_fairplay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_fairplay MediaStreamingPolicy#drm_fairplay}
        :param enabled_protocols: enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        if isinstance(default_content_key, dict):
            default_content_key = MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey(**default_content_key)
        if isinstance(drm_fairplay, dict):
            drm_fairplay = MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay(**drm_fairplay)
        if isinstance(enabled_protocols, dict):
            enabled_protocols = MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols(**enabled_protocols)
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcs.__init__)
            check_type(argname="argument default_content_key", value=default_content_key, expected_type=type_hints["default_content_key"])
            check_type(argname="argument drm_fairplay", value=drm_fairplay, expected_type=type_hints["drm_fairplay"])
            check_type(argname="argument enabled_protocols", value=enabled_protocols, expected_type=type_hints["enabled_protocols"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_content_key is not None:
            self._values["default_content_key"] = default_content_key
        if drm_fairplay is not None:
            self._values["drm_fairplay"] = drm_fairplay
        if enabled_protocols is not None:
            self._values["enabled_protocols"] = enabled_protocols

    @builtins.property
    def default_content_key(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey"]:
        '''default_content_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        '''
        result = self._values.get("default_content_key")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey"], result)

    @builtins.property
    def drm_fairplay(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay"]:
        '''drm_fairplay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_fairplay MediaStreamingPolicy#drm_fairplay}
        '''
        result = self._values.get("drm_fairplay")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay"], result)

    @builtins.property
    def enabled_protocols(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols"]:
        '''enabled_protocols block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        result = self._values.get("enabled_protocols")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCbcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "policy_name": "policyName"},
)
class MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey:
    def __init__(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey.__init__)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if label is not None:
            self._values["label"] = label
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.'''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetPolicyName")
    def reset_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyName", []))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay",
    jsii_struct_bases=[],
    name_mapping={
        "allow_persistent_license": "allowPersistentLicense",
        "custom_license_acquisition_url_template": "customLicenseAcquisitionUrlTemplate",
    },
)
class MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay:
    def __init__(
        self,
        *,
        allow_persistent_license: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_persistent_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#allow_persistent_license MediaStreamingPolicy#allow_persistent_license}.
        :param custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay.__init__)
            check_type(argname="argument allow_persistent_license", value=allow_persistent_license, expected_type=type_hints["allow_persistent_license"])
            check_type(argname="argument custom_license_acquisition_url_template", value=custom_license_acquisition_url_template, expected_type=type_hints["custom_license_acquisition_url_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_persistent_license is not None:
            self._values["allow_persistent_license"] = allow_persistent_license
        if custom_license_acquisition_url_template is not None:
            self._values["custom_license_acquisition_url_template"] = custom_license_acquisition_url_template

    @builtins.property
    def allow_persistent_license(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#allow_persistent_license MediaStreamingPolicy#allow_persistent_license}.'''
        result = self._values.get("allow_persistent_license")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_license_acquisition_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.'''
        result = self._values.get("custom_license_acquisition_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowPersistentLicense")
    def reset_allow_persistent_license(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPersistentLicense", []))

    @jsii.member(jsii_name="resetCustomLicenseAcquisitionUrlTemplate")
    def reset_custom_license_acquisition_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomLicenseAcquisitionUrlTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="allowPersistentLicenseInput")
    def allow_persistent_license_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowPersistentLicenseInput"))

    @builtins.property
    @jsii.member(jsii_name="customLicenseAcquisitionUrlTemplateInput")
    def custom_license_acquisition_url_template_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customLicenseAcquisitionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPersistentLicense")
    def allow_persistent_license(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowPersistentLicense"))

    @allow_persistent_license.setter
    def allow_persistent_license(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference, "allow_persistent_license").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPersistentLicense", value)

    @builtins.property
    @jsii.member(jsii_name="customLicenseAcquisitionUrlTemplate")
    def custom_license_acquisition_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customLicenseAcquisitionUrlTemplate"))

    @custom_license_acquisition_url_template.setter
    def custom_license_acquisition_url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference, "custom_license_acquisition_url_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLicenseAcquisitionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols",
    jsii_struct_bases=[],
    name_mapping={
        "dash": "dash",
        "download": "download",
        "hls": "hls",
        "smooth_streaming": "smoothStreaming",
    },
)
class MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols:
    def __init__(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols.__init__)
            check_type(argname="argument dash", value=dash, expected_type=type_hints["dash"])
            check_type(argname="argument download", value=download, expected_type=type_hints["download"])
            check_type(argname="argument hls", value=hls, expected_type=type_hints["hls"])
            check_type(argname="argument smooth_streaming", value=smooth_streaming, expected_type=type_hints["smooth_streaming"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dash is not None:
            self._values["dash"] = dash
        if download is not None:
            self._values["download"] = download
        if hls is not None:
            self._values["hls"] = hls
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming

    @builtins.property
    def dash(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.'''
        result = self._values.get("dash")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def download(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.'''
        result = self._values.get("download")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.'''
        result = self._values.get("hls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def smooth_streaming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.'''
        result = self._values.get("smooth_streaming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDash")
    def reset_dash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDash", []))

    @jsii.member(jsii_name="resetDownload")
    def reset_download(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownload", []))

    @jsii.member(jsii_name="resetHls")
    def reset_hls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHls", []))

    @jsii.member(jsii_name="resetSmoothStreaming")
    def reset_smooth_streaming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmoothStreaming", []))

    @builtins.property
    @jsii.member(jsii_name="dashInput")
    def dash_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dashInput"))

    @builtins.property
    @jsii.member(jsii_name="downloadInput")
    def download_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "downloadInput"))

    @builtins.property
    @jsii.member(jsii_name="hlsInput")
    def hls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hlsInput"))

    @builtins.property
    @jsii.member(jsii_name="smoothStreamingInput")
    def smooth_streaming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "smoothStreamingInput"))

    @builtins.property
    @jsii.member(jsii_name="dash")
    def dash(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dash"))

    @dash.setter
    def dash(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, "dash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dash", value)

    @builtins.property
    @jsii.member(jsii_name="download")
    def download(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "download"))

    @download.setter
    def download(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, "download").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "download", value)

    @builtins.property
    @jsii.member(jsii_name="hls")
    def hls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hls"))

    @hls.setter
    def hls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, "hls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hls", value)

    @builtins.property
    @jsii.member(jsii_name="smoothStreaming")
    def smooth_streaming(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "smoothStreaming"))

    @smooth_streaming.setter
    def smooth_streaming(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, "smooth_streaming").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothStreaming", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaStreamingPolicyCommonEncryptionCbcsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCbcsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCbcsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultContentKey")
    def put_default_content_key(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey(
            label=label, policy_name=policy_name
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultContentKey", [value]))

    @jsii.member(jsii_name="putDrmFairplay")
    def put_drm_fairplay(
        self,
        *,
        allow_persistent_license: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_persistent_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#allow_persistent_license MediaStreamingPolicy#allow_persistent_license}.
        :param custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay(
            allow_persistent_license=allow_persistent_license,
            custom_license_acquisition_url_template=custom_license_acquisition_url_template,
        )

        return typing.cast(None, jsii.invoke(self, "putDrmFairplay", [value]))

    @jsii.member(jsii_name="putEnabledProtocols")
    def put_enabled_protocols(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols(
            dash=dash, download=download, hls=hls, smooth_streaming=smooth_streaming
        )

        return typing.cast(None, jsii.invoke(self, "putEnabledProtocols", [value]))

    @jsii.member(jsii_name="resetDefaultContentKey")
    def reset_default_content_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultContentKey", []))

    @jsii.member(jsii_name="resetDrmFairplay")
    def reset_drm_fairplay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrmFairplay", []))

    @jsii.member(jsii_name="resetEnabledProtocols")
    def reset_enabled_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledProtocols", []))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKey")
    def default_content_key(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference, jsii.get(self, "defaultContentKey"))

    @builtins.property
    @jsii.member(jsii_name="drmFairplay")
    def drm_fairplay(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference, jsii.get(self, "drmFairplay"))

    @builtins.property
    @jsii.member(jsii_name="enabledProtocols")
    def enabled_protocols(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference, jsii.get(self, "enabledProtocols"))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyInput")
    def default_content_key_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey], jsii.get(self, "defaultContentKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="drmFairplayInput")
    def drm_fairplay_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay], jsii.get(self, "drmFairplayInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledProtocolsInput")
    def enabled_protocols_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols], jsii.get(self, "enabledProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcs]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCbcs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCbcsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCenc",
    jsii_struct_bases=[],
    name_mapping={
        "default_content_key": "defaultContentKey",
        "drm_playready": "drmPlayready",
        "drm_widevine_custom_license_acquisition_url_template": "drmWidevineCustomLicenseAcquisitionUrlTemplate",
        "enabled_protocols": "enabledProtocols",
    },
)
class MediaStreamingPolicyCommonEncryptionCenc:
    def __init__(
        self,
        *,
        default_content_key: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencDefaultContentKey", typing.Dict[str, typing.Any]]] = None,
        drm_playready: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencDrmPlayready", typing.Dict[str, typing.Any]]] = None,
        drm_widevine_custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
        enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyCommonEncryptionCencEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_content_key: default_content_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        :param drm_playready: drm_playready block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_playready MediaStreamingPolicy#drm_playready}
        :param drm_widevine_custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_widevine_custom_license_acquisition_url_template MediaStreamingPolicy#drm_widevine_custom_license_acquisition_url_template}.
        :param enabled_protocols: enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        if isinstance(default_content_key, dict):
            default_content_key = MediaStreamingPolicyCommonEncryptionCencDefaultContentKey(**default_content_key)
        if isinstance(drm_playready, dict):
            drm_playready = MediaStreamingPolicyCommonEncryptionCencDrmPlayready(**drm_playready)
        if isinstance(enabled_protocols, dict):
            enabled_protocols = MediaStreamingPolicyCommonEncryptionCencEnabledProtocols(**enabled_protocols)
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCenc.__init__)
            check_type(argname="argument default_content_key", value=default_content_key, expected_type=type_hints["default_content_key"])
            check_type(argname="argument drm_playready", value=drm_playready, expected_type=type_hints["drm_playready"])
            check_type(argname="argument drm_widevine_custom_license_acquisition_url_template", value=drm_widevine_custom_license_acquisition_url_template, expected_type=type_hints["drm_widevine_custom_license_acquisition_url_template"])
            check_type(argname="argument enabled_protocols", value=enabled_protocols, expected_type=type_hints["enabled_protocols"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_content_key is not None:
            self._values["default_content_key"] = default_content_key
        if drm_playready is not None:
            self._values["drm_playready"] = drm_playready
        if drm_widevine_custom_license_acquisition_url_template is not None:
            self._values["drm_widevine_custom_license_acquisition_url_template"] = drm_widevine_custom_license_acquisition_url_template
        if enabled_protocols is not None:
            self._values["enabled_protocols"] = enabled_protocols

    @builtins.property
    def default_content_key(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCencDefaultContentKey"]:
        '''default_content_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key MediaStreamingPolicy#default_content_key}
        '''
        result = self._values.get("default_content_key")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCencDefaultContentKey"], result)

    @builtins.property
    def drm_playready(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCencDrmPlayready"]:
        '''drm_playready block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_playready MediaStreamingPolicy#drm_playready}
        '''
        result = self._values.get("drm_playready")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCencDrmPlayready"], result)

    @builtins.property
    def drm_widevine_custom_license_acquisition_url_template(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#drm_widevine_custom_license_acquisition_url_template MediaStreamingPolicy#drm_widevine_custom_license_acquisition_url_template}.'''
        result = self._values.get("drm_widevine_custom_license_acquisition_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled_protocols(
        self,
    ) -> typing.Optional["MediaStreamingPolicyCommonEncryptionCencEnabledProtocols"]:
        '''enabled_protocols block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#enabled_protocols MediaStreamingPolicy#enabled_protocols}
        '''
        result = self._values.get("enabled_protocols")
        return typing.cast(typing.Optional["MediaStreamingPolicyCommonEncryptionCencEnabledProtocols"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCenc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencDefaultContentKey",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "policy_name": "policyName"},
)
class MediaStreamingPolicyCommonEncryptionCencDefaultContentKey:
    def __init__(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencDefaultContentKey.__init__)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if label is not None:
            self._values["label"] = label
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.'''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCencDefaultContentKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetPolicyName")
    def reset_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyName", []))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencDefaultContentKey]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencDefaultContentKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCencDefaultContentKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencDrmPlayready",
    jsii_struct_bases=[],
    name_mapping={
        "custom_attributes": "customAttributes",
        "custom_license_acquisition_url_template": "customLicenseAcquisitionUrlTemplate",
    },
)
class MediaStreamingPolicyCommonEncryptionCencDrmPlayready:
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[builtins.str] = None,
        custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_attributes MediaStreamingPolicy#custom_attributes}.
        :param custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencDrmPlayready.__init__)
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument custom_license_acquisition_url_template", value=custom_license_acquisition_url_template, expected_type=type_hints["custom_license_acquisition_url_template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if custom_license_acquisition_url_template is not None:
            self._values["custom_license_acquisition_url_template"] = custom_license_acquisition_url_template

    @builtins.property
    def custom_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_attributes MediaStreamingPolicy#custom_attributes}.'''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_license_acquisition_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.'''
        result = self._values.get("custom_license_acquisition_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCencDrmPlayready(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetCustomLicenseAcquisitionUrlTemplate")
    def reset_custom_license_acquisition_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomLicenseAcquisitionUrlTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="customLicenseAcquisitionUrlTemplateInput")
    def custom_license_acquisition_url_template_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customLicenseAcquisitionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="customLicenseAcquisitionUrlTemplate")
    def custom_license_acquisition_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customLicenseAcquisitionUrlTemplate"))

    @custom_license_acquisition_url_template.setter
    def custom_license_acquisition_url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference, "custom_license_acquisition_url_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLicenseAcquisitionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencDrmPlayready]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencDrmPlayready], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCencDrmPlayready],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencEnabledProtocols",
    jsii_struct_bases=[],
    name_mapping={
        "dash": "dash",
        "download": "download",
        "hls": "hls",
        "smooth_streaming": "smoothStreaming",
    },
)
class MediaStreamingPolicyCommonEncryptionCencEnabledProtocols:
    def __init__(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencEnabledProtocols.__init__)
            check_type(argname="argument dash", value=dash, expected_type=type_hints["dash"])
            check_type(argname="argument download", value=download, expected_type=type_hints["download"])
            check_type(argname="argument hls", value=hls, expected_type=type_hints["hls"])
            check_type(argname="argument smooth_streaming", value=smooth_streaming, expected_type=type_hints["smooth_streaming"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dash is not None:
            self._values["dash"] = dash
        if download is not None:
            self._values["download"] = download
        if hls is not None:
            self._values["hls"] = hls
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming

    @builtins.property
    def dash(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.'''
        result = self._values.get("dash")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def download(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.'''
        result = self._values.get("download")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.'''
        result = self._values.get("hls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def smooth_streaming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.'''
        result = self._values.get("smooth_streaming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyCommonEncryptionCencEnabledProtocols(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDash")
    def reset_dash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDash", []))

    @jsii.member(jsii_name="resetDownload")
    def reset_download(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownload", []))

    @jsii.member(jsii_name="resetHls")
    def reset_hls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHls", []))

    @jsii.member(jsii_name="resetSmoothStreaming")
    def reset_smooth_streaming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmoothStreaming", []))

    @builtins.property
    @jsii.member(jsii_name="dashInput")
    def dash_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dashInput"))

    @builtins.property
    @jsii.member(jsii_name="downloadInput")
    def download_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "downloadInput"))

    @builtins.property
    @jsii.member(jsii_name="hlsInput")
    def hls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hlsInput"))

    @builtins.property
    @jsii.member(jsii_name="smoothStreamingInput")
    def smooth_streaming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "smoothStreamingInput"))

    @builtins.property
    @jsii.member(jsii_name="dash")
    def dash(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dash"))

    @dash.setter
    def dash(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, "dash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dash", value)

    @builtins.property
    @jsii.member(jsii_name="download")
    def download(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "download"))

    @download.setter
    def download(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, "download").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "download", value)

    @builtins.property
    @jsii.member(jsii_name="hls")
    def hls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hls"))

    @hls.setter
    def hls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, "hls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hls", value)

    @builtins.property
    @jsii.member(jsii_name="smoothStreaming")
    def smooth_streaming(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "smoothStreaming"))

    @smooth_streaming.setter
    def smooth_streaming(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, "smooth_streaming").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothStreaming", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencEnabledProtocols]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencEnabledProtocols], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCencEnabledProtocols],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaStreamingPolicyCommonEncryptionCencOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyCommonEncryptionCencOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyCommonEncryptionCencOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultContentKey")
    def put_default_content_key(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#label MediaStreamingPolicy#label}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#policy_name MediaStreamingPolicy#policy_name}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCencDefaultContentKey(
            label=label, policy_name=policy_name
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultContentKey", [value]))

    @jsii.member(jsii_name="putDrmPlayready")
    def put_drm_playready(
        self,
        *,
        custom_attributes: typing.Optional[builtins.str] = None,
        custom_license_acquisition_url_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_attributes MediaStreamingPolicy#custom_attributes}.
        :param custom_license_acquisition_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#custom_license_acquisition_url_template MediaStreamingPolicy#custom_license_acquisition_url_template}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCencDrmPlayready(
            custom_attributes=custom_attributes,
            custom_license_acquisition_url_template=custom_license_acquisition_url_template,
        )

        return typing.cast(None, jsii.invoke(self, "putDrmPlayready", [value]))

    @jsii.member(jsii_name="putEnabledProtocols")
    def put_enabled_protocols(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        value = MediaStreamingPolicyCommonEncryptionCencEnabledProtocols(
            dash=dash, download=download, hls=hls, smooth_streaming=smooth_streaming
        )

        return typing.cast(None, jsii.invoke(self, "putEnabledProtocols", [value]))

    @jsii.member(jsii_name="resetDefaultContentKey")
    def reset_default_content_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultContentKey", []))

    @jsii.member(jsii_name="resetDrmPlayready")
    def reset_drm_playready(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrmPlayready", []))

    @jsii.member(jsii_name="resetDrmWidevineCustomLicenseAcquisitionUrlTemplate")
    def reset_drm_widevine_custom_license_acquisition_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrmWidevineCustomLicenseAcquisitionUrlTemplate", []))

    @jsii.member(jsii_name="resetEnabledProtocols")
    def reset_enabled_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledProtocols", []))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKey")
    def default_content_key(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference, jsii.get(self, "defaultContentKey"))

    @builtins.property
    @jsii.member(jsii_name="drmPlayready")
    def drm_playready(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference, jsii.get(self, "drmPlayready"))

    @builtins.property
    @jsii.member(jsii_name="enabledProtocols")
    def enabled_protocols(
        self,
    ) -> MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference:
        return typing.cast(MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference, jsii.get(self, "enabledProtocols"))

    @builtins.property
    @jsii.member(jsii_name="defaultContentKeyInput")
    def default_content_key_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencDefaultContentKey]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencDefaultContentKey], jsii.get(self, "defaultContentKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="drmPlayreadyInput")
    def drm_playready_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencDrmPlayready]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencDrmPlayready], jsii.get(self, "drmPlayreadyInput"))

    @builtins.property
    @jsii.member(jsii_name="drmWidevineCustomLicenseAcquisitionUrlTemplateInput")
    def drm_widevine_custom_license_acquisition_url_template_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "drmWidevineCustomLicenseAcquisitionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledProtocolsInput")
    def enabled_protocols_input(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCencEnabledProtocols]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCencEnabledProtocols], jsii.get(self, "enabledProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="drmWidevineCustomLicenseAcquisitionUrlTemplate")
    def drm_widevine_custom_license_acquisition_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "drmWidevineCustomLicenseAcquisitionUrlTemplate"))

    @drm_widevine_custom_license_acquisition_url_template.setter
    def drm_widevine_custom_license_acquisition_url_template(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencOutputReference, "drm_widevine_custom_license_acquisition_url_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drmWidevineCustomLicenseAcquisitionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCenc]:
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCenc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyCommonEncryptionCenc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyCommonEncryptionCencOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyConfig",
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
        "common_encryption_cbcs": "commonEncryptionCbcs",
        "common_encryption_cenc": "commonEncryptionCenc",
        "default_content_key_policy_name": "defaultContentKeyPolicyName",
        "id": "id",
        "no_encryption_enabled_protocols": "noEncryptionEnabledProtocols",
        "timeouts": "timeouts",
    },
)
class MediaStreamingPolicyConfig(cdktf.TerraformMetaArguments):
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
        common_encryption_cbcs: typing.Optional[typing.Union[MediaStreamingPolicyCommonEncryptionCbcs, typing.Dict[str, typing.Any]]] = None,
        common_encryption_cenc: typing.Optional[typing.Union[MediaStreamingPolicyCommonEncryptionCenc, typing.Dict[str, typing.Any]]] = None,
        default_content_key_policy_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        no_encryption_enabled_protocols: typing.Optional[typing.Union["MediaStreamingPolicyNoEncryptionEnabledProtocols", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MediaStreamingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#media_services_account_name MediaStreamingPolicy#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#name MediaStreamingPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#resource_group_name MediaStreamingPolicy#resource_group_name}.
        :param common_encryption_cbcs: common_encryption_cbcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cbcs MediaStreamingPolicy#common_encryption_cbcs}
        :param common_encryption_cenc: common_encryption_cenc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cenc MediaStreamingPolicy#common_encryption_cenc}
        :param default_content_key_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key_policy_name MediaStreamingPolicy#default_content_key_policy_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#id MediaStreamingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param no_encryption_enabled_protocols: no_encryption_enabled_protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#no_encryption_enabled_protocols MediaStreamingPolicy#no_encryption_enabled_protocols}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#timeouts MediaStreamingPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(common_encryption_cbcs, dict):
            common_encryption_cbcs = MediaStreamingPolicyCommonEncryptionCbcs(**common_encryption_cbcs)
        if isinstance(common_encryption_cenc, dict):
            common_encryption_cenc = MediaStreamingPolicyCommonEncryptionCenc(**common_encryption_cenc)
        if isinstance(no_encryption_enabled_protocols, dict):
            no_encryption_enabled_protocols = MediaStreamingPolicyNoEncryptionEnabledProtocols(**no_encryption_enabled_protocols)
        if isinstance(timeouts, dict):
            timeouts = MediaStreamingPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyConfig.__init__)
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
            check_type(argname="argument common_encryption_cbcs", value=common_encryption_cbcs, expected_type=type_hints["common_encryption_cbcs"])
            check_type(argname="argument common_encryption_cenc", value=common_encryption_cenc, expected_type=type_hints["common_encryption_cenc"])
            check_type(argname="argument default_content_key_policy_name", value=default_content_key_policy_name, expected_type=type_hints["default_content_key_policy_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument no_encryption_enabled_protocols", value=no_encryption_enabled_protocols, expected_type=type_hints["no_encryption_enabled_protocols"])
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
        if common_encryption_cbcs is not None:
            self._values["common_encryption_cbcs"] = common_encryption_cbcs
        if common_encryption_cenc is not None:
            self._values["common_encryption_cenc"] = common_encryption_cenc
        if default_content_key_policy_name is not None:
            self._values["default_content_key_policy_name"] = default_content_key_policy_name
        if id is not None:
            self._values["id"] = id
        if no_encryption_enabled_protocols is not None:
            self._values["no_encryption_enabled_protocols"] = no_encryption_enabled_protocols
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#media_services_account_name MediaStreamingPolicy#media_services_account_name}.'''
        result = self._values.get("media_services_account_name")
        assert result is not None, "Required property 'media_services_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#name MediaStreamingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#resource_group_name MediaStreamingPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def common_encryption_cbcs(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCbcs]:
        '''common_encryption_cbcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cbcs MediaStreamingPolicy#common_encryption_cbcs}
        '''
        result = self._values.get("common_encryption_cbcs")
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCbcs], result)

    @builtins.property
    def common_encryption_cenc(
        self,
    ) -> typing.Optional[MediaStreamingPolicyCommonEncryptionCenc]:
        '''common_encryption_cenc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#common_encryption_cenc MediaStreamingPolicy#common_encryption_cenc}
        '''
        result = self._values.get("common_encryption_cenc")
        return typing.cast(typing.Optional[MediaStreamingPolicyCommonEncryptionCenc], result)

    @builtins.property
    def default_content_key_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#default_content_key_policy_name MediaStreamingPolicy#default_content_key_policy_name}.'''
        result = self._values.get("default_content_key_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#id MediaStreamingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_encryption_enabled_protocols(
        self,
    ) -> typing.Optional["MediaStreamingPolicyNoEncryptionEnabledProtocols"]:
        '''no_encryption_enabled_protocols block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#no_encryption_enabled_protocols MediaStreamingPolicy#no_encryption_enabled_protocols}
        '''
        result = self._values.get("no_encryption_enabled_protocols")
        return typing.cast(typing.Optional["MediaStreamingPolicyNoEncryptionEnabledProtocols"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaStreamingPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#timeouts MediaStreamingPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaStreamingPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyNoEncryptionEnabledProtocols",
    jsii_struct_bases=[],
    name_mapping={
        "dash": "dash",
        "download": "download",
        "hls": "hls",
        "smooth_streaming": "smoothStreaming",
    },
)
class MediaStreamingPolicyNoEncryptionEnabledProtocols:
    def __init__(
        self,
        *,
        dash: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        download: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.
        :param download: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.
        :param hls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyNoEncryptionEnabledProtocols.__init__)
            check_type(argname="argument dash", value=dash, expected_type=type_hints["dash"])
            check_type(argname="argument download", value=download, expected_type=type_hints["download"])
            check_type(argname="argument hls", value=hls, expected_type=type_hints["hls"])
            check_type(argname="argument smooth_streaming", value=smooth_streaming, expected_type=type_hints["smooth_streaming"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dash is not None:
            self._values["dash"] = dash
        if download is not None:
            self._values["download"] = download
        if hls is not None:
            self._values["hls"] = hls
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming

    @builtins.property
    def dash(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#dash MediaStreamingPolicy#dash}.'''
        result = self._values.get("dash")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def download(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#download MediaStreamingPolicy#download}.'''
        result = self._values.get("download")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#hls MediaStreamingPolicy#hls}.'''
        result = self._values.get("hls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def smooth_streaming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#smooth_streaming MediaStreamingPolicy#smooth_streaming}.'''
        result = self._values.get("smooth_streaming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyNoEncryptionEnabledProtocols(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDash")
    def reset_dash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDash", []))

    @jsii.member(jsii_name="resetDownload")
    def reset_download(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownload", []))

    @jsii.member(jsii_name="resetHls")
    def reset_hls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHls", []))

    @jsii.member(jsii_name="resetSmoothStreaming")
    def reset_smooth_streaming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmoothStreaming", []))

    @builtins.property
    @jsii.member(jsii_name="dashInput")
    def dash_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dashInput"))

    @builtins.property
    @jsii.member(jsii_name="downloadInput")
    def download_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "downloadInput"))

    @builtins.property
    @jsii.member(jsii_name="hlsInput")
    def hls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hlsInput"))

    @builtins.property
    @jsii.member(jsii_name="smoothStreamingInput")
    def smooth_streaming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "smoothStreamingInput"))

    @builtins.property
    @jsii.member(jsii_name="dash")
    def dash(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dash"))

    @dash.setter
    def dash(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference, "dash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dash", value)

    @builtins.property
    @jsii.member(jsii_name="download")
    def download(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "download"))

    @download.setter
    def download(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference, "download").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "download", value)

    @builtins.property
    @jsii.member(jsii_name="hls")
    def hls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hls"))

    @hls.setter
    def hls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference, "hls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hls", value)

    @builtins.property
    @jsii.member(jsii_name="smoothStreaming")
    def smooth_streaming(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "smoothStreaming"))

    @smooth_streaming.setter
    def smooth_streaming(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference, "smooth_streaming").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothStreaming", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaStreamingPolicyNoEncryptionEnabledProtocols]:
        return typing.cast(typing.Optional[MediaStreamingPolicyNoEncryptionEnabledProtocols], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaStreamingPolicyNoEncryptionEnabledProtocols],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class MediaStreamingPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#create MediaStreamingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#delete MediaStreamingPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#read MediaStreamingPolicy#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaStreamingPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#create MediaStreamingPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#delete MediaStreamingPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_streaming_policy#read MediaStreamingPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaStreamingPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaStreamingPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaStreamingPolicy.MediaStreamingPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaStreamingPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaStreamingPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaStreamingPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaStreamingPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaStreamingPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaStreamingPolicy",
    "MediaStreamingPolicyCommonEncryptionCbcs",
    "MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKey",
    "MediaStreamingPolicyCommonEncryptionCbcsDefaultContentKeyOutputReference",
    "MediaStreamingPolicyCommonEncryptionCbcsDrmFairplay",
    "MediaStreamingPolicyCommonEncryptionCbcsDrmFairplayOutputReference",
    "MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocols",
    "MediaStreamingPolicyCommonEncryptionCbcsEnabledProtocolsOutputReference",
    "MediaStreamingPolicyCommonEncryptionCbcsOutputReference",
    "MediaStreamingPolicyCommonEncryptionCenc",
    "MediaStreamingPolicyCommonEncryptionCencDefaultContentKey",
    "MediaStreamingPolicyCommonEncryptionCencDefaultContentKeyOutputReference",
    "MediaStreamingPolicyCommonEncryptionCencDrmPlayready",
    "MediaStreamingPolicyCommonEncryptionCencDrmPlayreadyOutputReference",
    "MediaStreamingPolicyCommonEncryptionCencEnabledProtocols",
    "MediaStreamingPolicyCommonEncryptionCencEnabledProtocolsOutputReference",
    "MediaStreamingPolicyCommonEncryptionCencOutputReference",
    "MediaStreamingPolicyConfig",
    "MediaStreamingPolicyNoEncryptionEnabledProtocols",
    "MediaStreamingPolicyNoEncryptionEnabledProtocolsOutputReference",
    "MediaStreamingPolicyTimeouts",
    "MediaStreamingPolicyTimeoutsOutputReference",
]

publication.publish()
