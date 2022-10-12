'''
# `azurerm_media_content_key_policy`

Refer to the Terraform Registory for docs: [`azurerm_media_content_key_policy`](https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy).
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


class MediaContentKeyPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy azurerm_media_content_key_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        media_services_account_name: builtins.str,
        name: builtins.str,
        policy_option: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOption", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MediaContentKeyPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy azurerm_media_content_key_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#media_services_account_name MediaContentKeyPolicy#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#name MediaContentKeyPolicy#name}.
        :param policy_option: policy_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#policy_option MediaContentKeyPolicy#policy_option}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#resource_group_name MediaContentKeyPolicy#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#description MediaContentKeyPolicy#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#id MediaContentKeyPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#timeouts MediaContentKeyPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaContentKeyPolicyConfig(
            media_services_account_name=media_services_account_name,
            name=name,
            policy_option=policy_option,
            resource_group_name=resource_group_name,
            description=description,
            id=id,
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

    @jsii.member(jsii_name="putPolicyOption")
    def put_policy_option(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOption", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicy.put_policy_option)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicyOption", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#create MediaContentKeyPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#delete MediaContentKeyPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#read MediaContentKeyPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#update MediaContentKeyPolicy#update}.
        '''
        value = MediaContentKeyPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="policyOption")
    def policy_option(self) -> "MediaContentKeyPolicyPolicyOptionList":
        return typing.cast("MediaContentKeyPolicyPolicyOptionList", jsii.get(self, "policyOption"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaContentKeyPolicyTimeoutsOutputReference":
        return typing.cast("MediaContentKeyPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="policyOptionInput")
    def policy_option_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOption"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOption"]]], jsii.get(self, "policyOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaContentKeyPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaContentKeyPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicy, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mediaServicesAccountName")
    def media_services_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaServicesAccountName"))

    @media_services_account_name.setter
    def media_services_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicy, "media_services_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaServicesAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyConfig",
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
        "policy_option": "policyOption",
        "resource_group_name": "resourceGroupName",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class MediaContentKeyPolicyConfig(cdktf.TerraformMetaArguments):
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
        policy_option: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOption", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MediaContentKeyPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param media_services_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#media_services_account_name MediaContentKeyPolicy#media_services_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#name MediaContentKeyPolicy#name}.
        :param policy_option: policy_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#policy_option MediaContentKeyPolicy#policy_option}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#resource_group_name MediaContentKeyPolicy#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#description MediaContentKeyPolicy#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#id MediaContentKeyPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#timeouts MediaContentKeyPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MediaContentKeyPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument media_services_account_name", value=media_services_account_name, expected_type=type_hints["media_services_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_option", value=policy_option, expected_type=type_hints["policy_option"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "media_services_account_name": media_services_account_name,
            "name": name,
            "policy_option": policy_option,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#media_services_account_name MediaContentKeyPolicy#media_services_account_name}.'''
        result = self._values.get("media_services_account_name")
        assert result is not None, "Required property 'media_services_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#name MediaContentKeyPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_option(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOption"]]:
        '''policy_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#policy_option MediaContentKeyPolicy#policy_option}
        '''
        result = self._values.get("policy_option")
        assert result is not None, "Required property 'policy_option' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOption"]], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#resource_group_name MediaContentKeyPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#description MediaContentKeyPolicy#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#id MediaContentKeyPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaContentKeyPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#timeouts MediaContentKeyPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaContentKeyPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOption",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "clear_key_configuration_enabled": "clearKeyConfigurationEnabled",
        "fairplay_configuration": "fairplayConfiguration",
        "open_restriction_enabled": "openRestrictionEnabled",
        "playready_configuration_license": "playreadyConfigurationLicense",
        "token_restriction": "tokenRestriction",
        "widevine_configuration_template": "widevineConfigurationTemplate",
    },
)
class MediaContentKeyPolicyPolicyOption:
    def __init__(
        self,
        *,
        name: builtins.str,
        clear_key_configuration_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fairplay_configuration: typing.Optional[typing.Union["MediaContentKeyPolicyPolicyOptionFairplayConfiguration", typing.Dict[str, typing.Any]]] = None,
        open_restriction_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        playready_configuration_license: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense", typing.Dict[str, typing.Any]]]]] = None,
        token_restriction: typing.Optional[typing.Union["MediaContentKeyPolicyPolicyOptionTokenRestriction", typing.Dict[str, typing.Any]]] = None,
        widevine_configuration_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#name MediaContentKeyPolicy#name}.
        :param clear_key_configuration_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#clear_key_configuration_enabled MediaContentKeyPolicy#clear_key_configuration_enabled}.
        :param fairplay_configuration: fairplay_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#fairplay_configuration MediaContentKeyPolicy#fairplay_configuration}
        :param open_restriction_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#open_restriction_enabled MediaContentKeyPolicy#open_restriction_enabled}.
        :param playready_configuration_license: playready_configuration_license block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#playready_configuration_license MediaContentKeyPolicy#playready_configuration_license}
        :param token_restriction: token_restriction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#token_restriction MediaContentKeyPolicy#token_restriction}
        :param widevine_configuration_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#widevine_configuration_template MediaContentKeyPolicy#widevine_configuration_template}.
        '''
        if isinstance(fairplay_configuration, dict):
            fairplay_configuration = MediaContentKeyPolicyPolicyOptionFairplayConfiguration(**fairplay_configuration)
        if isinstance(token_restriction, dict):
            token_restriction = MediaContentKeyPolicyPolicyOptionTokenRestriction(**token_restriction)
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOption.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument clear_key_configuration_enabled", value=clear_key_configuration_enabled, expected_type=type_hints["clear_key_configuration_enabled"])
            check_type(argname="argument fairplay_configuration", value=fairplay_configuration, expected_type=type_hints["fairplay_configuration"])
            check_type(argname="argument open_restriction_enabled", value=open_restriction_enabled, expected_type=type_hints["open_restriction_enabled"])
            check_type(argname="argument playready_configuration_license", value=playready_configuration_license, expected_type=type_hints["playready_configuration_license"])
            check_type(argname="argument token_restriction", value=token_restriction, expected_type=type_hints["token_restriction"])
            check_type(argname="argument widevine_configuration_template", value=widevine_configuration_template, expected_type=type_hints["widevine_configuration_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if clear_key_configuration_enabled is not None:
            self._values["clear_key_configuration_enabled"] = clear_key_configuration_enabled
        if fairplay_configuration is not None:
            self._values["fairplay_configuration"] = fairplay_configuration
        if open_restriction_enabled is not None:
            self._values["open_restriction_enabled"] = open_restriction_enabled
        if playready_configuration_license is not None:
            self._values["playready_configuration_license"] = playready_configuration_license
        if token_restriction is not None:
            self._values["token_restriction"] = token_restriction
        if widevine_configuration_template is not None:
            self._values["widevine_configuration_template"] = widevine_configuration_template

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#name MediaContentKeyPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clear_key_configuration_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#clear_key_configuration_enabled MediaContentKeyPolicy#clear_key_configuration_enabled}.'''
        result = self._values.get("clear_key_configuration_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fairplay_configuration(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionFairplayConfiguration"]:
        '''fairplay_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#fairplay_configuration MediaContentKeyPolicy#fairplay_configuration}
        '''
        result = self._values.get("fairplay_configuration")
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionFairplayConfiguration"], result)

    @builtins.property
    def open_restriction_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#open_restriction_enabled MediaContentKeyPolicy#open_restriction_enabled}.'''
        result = self._values.get("open_restriction_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def playready_configuration_license(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense"]]]:
        '''playready_configuration_license block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#playready_configuration_license MediaContentKeyPolicy#playready_configuration_license}
        '''
        result = self._values.get("playready_configuration_license")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense"]]], result)

    @builtins.property
    def token_restriction(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionTokenRestriction"]:
        '''token_restriction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#token_restriction MediaContentKeyPolicy#token_restriction}
        '''
        result = self._values.get("token_restriction")
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionTokenRestriction"], result)

    @builtins.property
    def widevine_configuration_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#widevine_configuration_template MediaContentKeyPolicy#widevine_configuration_template}.'''
        result = self._values.get("widevine_configuration_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionFairplayConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "ask": "ask",
        "offline_rental_configuration": "offlineRentalConfiguration",
        "pfx": "pfx",
        "pfx_password": "pfxPassword",
        "rental_and_lease_key_type": "rentalAndLeaseKeyType",
        "rental_duration_seconds": "rentalDurationSeconds",
    },
)
class MediaContentKeyPolicyPolicyOptionFairplayConfiguration:
    def __init__(
        self,
        *,
        ask: typing.Optional[builtins.str] = None,
        offline_rental_configuration: typing.Optional[typing.Union["MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration", typing.Dict[str, typing.Any]]] = None,
        pfx: typing.Optional[builtins.str] = None,
        pfx_password: typing.Optional[builtins.str] = None,
        rental_and_lease_key_type: typing.Optional[builtins.str] = None,
        rental_duration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ask: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#ask MediaContentKeyPolicy#ask}.
        :param offline_rental_configuration: offline_rental_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#offline_rental_configuration MediaContentKeyPolicy#offline_rental_configuration}
        :param pfx: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx MediaContentKeyPolicy#pfx}.
        :param pfx_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx_password MediaContentKeyPolicy#pfx_password}.
        :param rental_and_lease_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_and_lease_key_type MediaContentKeyPolicy#rental_and_lease_key_type}.
        :param rental_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_duration_seconds MediaContentKeyPolicy#rental_duration_seconds}.
        '''
        if isinstance(offline_rental_configuration, dict):
            offline_rental_configuration = MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration(**offline_rental_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionFairplayConfiguration.__init__)
            check_type(argname="argument ask", value=ask, expected_type=type_hints["ask"])
            check_type(argname="argument offline_rental_configuration", value=offline_rental_configuration, expected_type=type_hints["offline_rental_configuration"])
            check_type(argname="argument pfx", value=pfx, expected_type=type_hints["pfx"])
            check_type(argname="argument pfx_password", value=pfx_password, expected_type=type_hints["pfx_password"])
            check_type(argname="argument rental_and_lease_key_type", value=rental_and_lease_key_type, expected_type=type_hints["rental_and_lease_key_type"])
            check_type(argname="argument rental_duration_seconds", value=rental_duration_seconds, expected_type=type_hints["rental_duration_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ask is not None:
            self._values["ask"] = ask
        if offline_rental_configuration is not None:
            self._values["offline_rental_configuration"] = offline_rental_configuration
        if pfx is not None:
            self._values["pfx"] = pfx
        if pfx_password is not None:
            self._values["pfx_password"] = pfx_password
        if rental_and_lease_key_type is not None:
            self._values["rental_and_lease_key_type"] = rental_and_lease_key_type
        if rental_duration_seconds is not None:
            self._values["rental_duration_seconds"] = rental_duration_seconds

    @builtins.property
    def ask(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#ask MediaContentKeyPolicy#ask}.'''
        result = self._values.get("ask")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offline_rental_configuration(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration"]:
        '''offline_rental_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#offline_rental_configuration MediaContentKeyPolicy#offline_rental_configuration}
        '''
        result = self._values.get("offline_rental_configuration")
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration"], result)

    @builtins.property
    def pfx(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx MediaContentKeyPolicy#pfx}.'''
        result = self._values.get("pfx")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pfx_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx_password MediaContentKeyPolicy#pfx_password}.'''
        result = self._values.get("pfx_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rental_and_lease_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_and_lease_key_type MediaContentKeyPolicy#rental_and_lease_key_type}.'''
        result = self._values.get("rental_and_lease_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rental_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_duration_seconds MediaContentKeyPolicy#rental_duration_seconds}.'''
        result = self._values.get("rental_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionFairplayConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "playback_duration_seconds": "playbackDurationSeconds",
        "storage_duration_seconds": "storageDurationSeconds",
    },
)
class MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration:
    def __init__(
        self,
        *,
        playback_duration_seconds: typing.Optional[jsii.Number] = None,
        storage_duration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param playback_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#playback_duration_seconds MediaContentKeyPolicy#playback_duration_seconds}.
        :param storage_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#storage_duration_seconds MediaContentKeyPolicy#storage_duration_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration.__init__)
            check_type(argname="argument playback_duration_seconds", value=playback_duration_seconds, expected_type=type_hints["playback_duration_seconds"])
            check_type(argname="argument storage_duration_seconds", value=storage_duration_seconds, expected_type=type_hints["storage_duration_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if playback_duration_seconds is not None:
            self._values["playback_duration_seconds"] = playback_duration_seconds
        if storage_duration_seconds is not None:
            self._values["storage_duration_seconds"] = storage_duration_seconds

    @builtins.property
    def playback_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#playback_duration_seconds MediaContentKeyPolicy#playback_duration_seconds}.'''
        result = self._values.get("playback_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#storage_duration_seconds MediaContentKeyPolicy#storage_duration_seconds}.'''
        result = self._values.get("storage_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPlaybackDurationSeconds")
    def reset_playback_duration_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlaybackDurationSeconds", []))

    @jsii.member(jsii_name="resetStorageDurationSeconds")
    def reset_storage_duration_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDurationSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="playbackDurationSecondsInput")
    def playback_duration_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "playbackDurationSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDurationSecondsInput")
    def storage_duration_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageDurationSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="playbackDurationSeconds")
    def playback_duration_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "playbackDurationSeconds"))

    @playback_duration_seconds.setter
    def playback_duration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference, "playback_duration_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playbackDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="storageDurationSeconds")
    def storage_duration_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageDurationSeconds"))

    @storage_duration_seconds.setter
    def storage_duration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference, "storage_duration_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOfflineRentalConfiguration")
    def put_offline_rental_configuration(
        self,
        *,
        playback_duration_seconds: typing.Optional[jsii.Number] = None,
        storage_duration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param playback_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#playback_duration_seconds MediaContentKeyPolicy#playback_duration_seconds}.
        :param storage_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#storage_duration_seconds MediaContentKeyPolicy#storage_duration_seconds}.
        '''
        value = MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration(
            playback_duration_seconds=playback_duration_seconds,
            storage_duration_seconds=storage_duration_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putOfflineRentalConfiguration", [value]))

    @jsii.member(jsii_name="resetAsk")
    def reset_ask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsk", []))

    @jsii.member(jsii_name="resetOfflineRentalConfiguration")
    def reset_offline_rental_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOfflineRentalConfiguration", []))

    @jsii.member(jsii_name="resetPfx")
    def reset_pfx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPfx", []))

    @jsii.member(jsii_name="resetPfxPassword")
    def reset_pfx_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPfxPassword", []))

    @jsii.member(jsii_name="resetRentalAndLeaseKeyType")
    def reset_rental_and_lease_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRentalAndLeaseKeyType", []))

    @jsii.member(jsii_name="resetRentalDurationSeconds")
    def reset_rental_duration_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRentalDurationSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="offlineRentalConfiguration")
    def offline_rental_configuration(
        self,
    ) -> MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference:
        return typing.cast(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference, jsii.get(self, "offlineRentalConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="askInput")
    def ask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "askInput"))

    @builtins.property
    @jsii.member(jsii_name="offlineRentalConfigurationInput")
    def offline_rental_configuration_input(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration], jsii.get(self, "offlineRentalConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="pfxInput")
    def pfx_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfxInput"))

    @builtins.property
    @jsii.member(jsii_name="pfxPasswordInput")
    def pfx_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfxPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="rentalAndLeaseKeyTypeInput")
    def rental_and_lease_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rentalAndLeaseKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rentalDurationSecondsInput")
    def rental_duration_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rentalDurationSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="ask")
    def ask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ask"))

    @ask.setter
    def ask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "ask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ask", value)

    @builtins.property
    @jsii.member(jsii_name="pfx")
    def pfx(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfx"))

    @pfx.setter
    def pfx(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "pfx").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfx", value)

    @builtins.property
    @jsii.member(jsii_name="pfxPassword")
    def pfx_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfxPassword"))

    @pfx_password.setter
    def pfx_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "pfx_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfxPassword", value)

    @builtins.property
    @jsii.member(jsii_name="rentalAndLeaseKeyType")
    def rental_and_lease_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rentalAndLeaseKeyType"))

    @rental_and_lease_key_type.setter
    def rental_and_lease_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "rental_and_lease_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rentalAndLeaseKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="rentalDurationSeconds")
    def rental_duration_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rentalDurationSeconds"))

    @rental_duration_seconds.setter
    def rental_duration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "rental_duration_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rentalDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfiguration]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaContentKeyPolicyPolicyOptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionList",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaContentKeyPolicyPolicyOptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaContentKeyPolicyPolicyOptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOption]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaContentKeyPolicyPolicyOptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFairplayConfiguration")
    def put_fairplay_configuration(
        self,
        *,
        ask: typing.Optional[builtins.str] = None,
        offline_rental_configuration: typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration, typing.Dict[str, typing.Any]]] = None,
        pfx: typing.Optional[builtins.str] = None,
        pfx_password: typing.Optional[builtins.str] = None,
        rental_and_lease_key_type: typing.Optional[builtins.str] = None,
        rental_duration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ask: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#ask MediaContentKeyPolicy#ask}.
        :param offline_rental_configuration: offline_rental_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#offline_rental_configuration MediaContentKeyPolicy#offline_rental_configuration}
        :param pfx: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx MediaContentKeyPolicy#pfx}.
        :param pfx_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#pfx_password MediaContentKeyPolicy#pfx_password}.
        :param rental_and_lease_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_and_lease_key_type MediaContentKeyPolicy#rental_and_lease_key_type}.
        :param rental_duration_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#rental_duration_seconds MediaContentKeyPolicy#rental_duration_seconds}.
        '''
        value = MediaContentKeyPolicyPolicyOptionFairplayConfiguration(
            ask=ask,
            offline_rental_configuration=offline_rental_configuration,
            pfx=pfx,
            pfx_password=pfx_password,
            rental_and_lease_key_type=rental_and_lease_key_type,
            rental_duration_seconds=rental_duration_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putFairplayConfiguration", [value]))

    @jsii.member(jsii_name="putPlayreadyConfigurationLicense")
    def put_playready_configuration_license(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionOutputReference.put_playready_configuration_license)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlayreadyConfigurationLicense", [value]))

    @jsii.member(jsii_name="putTokenRestriction")
    def put_token_restriction(
        self,
        *,
        audience: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        open_id_connect_discovery_document: typing.Optional[builtins.str] = None,
        primary_rsa_token_key_exponent: typing.Optional[builtins.str] = None,
        primary_rsa_token_key_modulus: typing.Optional[builtins.str] = None,
        primary_symmetric_token_key: typing.Optional[builtins.str] = None,
        primary_x509_token_key_raw: typing.Optional[builtins.str] = None,
        required_claim: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim", typing.Dict[str, typing.Any]]]]] = None,
        token_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#audience MediaContentKeyPolicy#audience}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#issuer MediaContentKeyPolicy#issuer}.
        :param open_id_connect_discovery_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#open_id_connect_discovery_document MediaContentKeyPolicy#open_id_connect_discovery_document}.
        :param primary_rsa_token_key_exponent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_exponent MediaContentKeyPolicy#primary_rsa_token_key_exponent}.
        :param primary_rsa_token_key_modulus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_modulus MediaContentKeyPolicy#primary_rsa_token_key_modulus}.
        :param primary_symmetric_token_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_symmetric_token_key MediaContentKeyPolicy#primary_symmetric_token_key}.
        :param primary_x509_token_key_raw: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_x509_token_key_raw MediaContentKeyPolicy#primary_x509_token_key_raw}.
        :param required_claim: required_claim block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#required_claim MediaContentKeyPolicy#required_claim}
        :param token_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#token_type MediaContentKeyPolicy#token_type}.
        '''
        value = MediaContentKeyPolicyPolicyOptionTokenRestriction(
            audience=audience,
            issuer=issuer,
            open_id_connect_discovery_document=open_id_connect_discovery_document,
            primary_rsa_token_key_exponent=primary_rsa_token_key_exponent,
            primary_rsa_token_key_modulus=primary_rsa_token_key_modulus,
            primary_symmetric_token_key=primary_symmetric_token_key,
            primary_x509_token_key_raw=primary_x509_token_key_raw,
            required_claim=required_claim,
            token_type=token_type,
        )

        return typing.cast(None, jsii.invoke(self, "putTokenRestriction", [value]))

    @jsii.member(jsii_name="resetClearKeyConfigurationEnabled")
    def reset_clear_key_configuration_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClearKeyConfigurationEnabled", []))

    @jsii.member(jsii_name="resetFairplayConfiguration")
    def reset_fairplay_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFairplayConfiguration", []))

    @jsii.member(jsii_name="resetOpenRestrictionEnabled")
    def reset_open_restriction_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenRestrictionEnabled", []))

    @jsii.member(jsii_name="resetPlayreadyConfigurationLicense")
    def reset_playready_configuration_license(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlayreadyConfigurationLicense", []))

    @jsii.member(jsii_name="resetTokenRestriction")
    def reset_token_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenRestriction", []))

    @jsii.member(jsii_name="resetWidevineConfigurationTemplate")
    def reset_widevine_configuration_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidevineConfigurationTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="fairplayConfiguration")
    def fairplay_configuration(
        self,
    ) -> MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference:
        return typing.cast(MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference, jsii.get(self, "fairplayConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="playreadyConfigurationLicense")
    def playready_configuration_license(
        self,
    ) -> "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList":
        return typing.cast("MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList", jsii.get(self, "playreadyConfigurationLicense"))

    @builtins.property
    @jsii.member(jsii_name="tokenRestriction")
    def token_restriction(
        self,
    ) -> "MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference":
        return typing.cast("MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference", jsii.get(self, "tokenRestriction"))

    @builtins.property
    @jsii.member(jsii_name="clearKeyConfigurationEnabledInput")
    def clear_key_configuration_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "clearKeyConfigurationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="fairplayConfigurationInput")
    def fairplay_configuration_input(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfiguration]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionFairplayConfiguration], jsii.get(self, "fairplayConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="openRestrictionEnabledInput")
    def open_restriction_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "openRestrictionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="playreadyConfigurationLicenseInput")
    def playready_configuration_license_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense"]]], jsii.get(self, "playreadyConfigurationLicenseInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenRestrictionInput")
    def token_restriction_input(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionTokenRestriction"]:
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionTokenRestriction"], jsii.get(self, "tokenRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="widevineConfigurationTemplateInput")
    def widevine_configuration_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "widevineConfigurationTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="clearKeyConfigurationEnabled")
    def clear_key_configuration_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "clearKeyConfigurationEnabled"))

    @clear_key_configuration_enabled.setter
    def clear_key_configuration_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionOutputReference, "clear_key_configuration_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clearKeyConfigurationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="openRestrictionEnabled")
    def open_restriction_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "openRestrictionEnabled"))

    @open_restriction_enabled.setter
    def open_restriction_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionOutputReference, "open_restriction_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openRestrictionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="widevineConfigurationTemplate")
    def widevine_configuration_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "widevineConfigurationTemplate"))

    @widevine_configuration_template.setter
    def widevine_configuration_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionOutputReference, "widevine_configuration_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "widevineConfigurationTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOption, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOption, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOption, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense",
    jsii_struct_bases=[],
    name_mapping={
        "allow_test_devices": "allowTestDevices",
        "begin_date": "beginDate",
        "content_key_location_from_header_enabled": "contentKeyLocationFromHeaderEnabled",
        "content_key_location_from_key_id": "contentKeyLocationFromKeyId",
        "content_type": "contentType",
        "expiration_date": "expirationDate",
        "grace_period": "gracePeriod",
        "license_type": "licenseType",
        "play_right": "playRight",
        "relative_begin_date": "relativeBeginDate",
        "relative_expiration_date": "relativeExpirationDate",
    },
)
class MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense:
    def __init__(
        self,
        *,
        allow_test_devices: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        begin_date: typing.Optional[builtins.str] = None,
        content_key_location_from_header_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        content_key_location_from_key_id: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        expiration_date: typing.Optional[builtins.str] = None,
        grace_period: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        play_right: typing.Optional[typing.Union["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight", typing.Dict[str, typing.Any]]] = None,
        relative_begin_date: typing.Optional[builtins.str] = None,
        relative_expiration_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_test_devices: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#allow_test_devices MediaContentKeyPolicy#allow_test_devices}.
        :param begin_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#begin_date MediaContentKeyPolicy#begin_date}.
        :param content_key_location_from_header_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_key_location_from_header_enabled MediaContentKeyPolicy#content_key_location_from_header_enabled}.
        :param content_key_location_from_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_key_location_from_key_id MediaContentKeyPolicy#content_key_location_from_key_id}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_type MediaContentKeyPolicy#content_type}.
        :param expiration_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#expiration_date MediaContentKeyPolicy#expiration_date}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#grace_period MediaContentKeyPolicy#grace_period}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#license_type MediaContentKeyPolicy#license_type}.
        :param play_right: play_right block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#play_right MediaContentKeyPolicy#play_right}
        :param relative_begin_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#relative_begin_date MediaContentKeyPolicy#relative_begin_date}.
        :param relative_expiration_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#relative_expiration_date MediaContentKeyPolicy#relative_expiration_date}.
        '''
        if isinstance(play_right, dict):
            play_right = MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight(**play_right)
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense.__init__)
            check_type(argname="argument allow_test_devices", value=allow_test_devices, expected_type=type_hints["allow_test_devices"])
            check_type(argname="argument begin_date", value=begin_date, expected_type=type_hints["begin_date"])
            check_type(argname="argument content_key_location_from_header_enabled", value=content_key_location_from_header_enabled, expected_type=type_hints["content_key_location_from_header_enabled"])
            check_type(argname="argument content_key_location_from_key_id", value=content_key_location_from_key_id, expected_type=type_hints["content_key_location_from_key_id"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument expiration_date", value=expiration_date, expected_type=type_hints["expiration_date"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument play_right", value=play_right, expected_type=type_hints["play_right"])
            check_type(argname="argument relative_begin_date", value=relative_begin_date, expected_type=type_hints["relative_begin_date"])
            check_type(argname="argument relative_expiration_date", value=relative_expiration_date, expected_type=type_hints["relative_expiration_date"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_test_devices is not None:
            self._values["allow_test_devices"] = allow_test_devices
        if begin_date is not None:
            self._values["begin_date"] = begin_date
        if content_key_location_from_header_enabled is not None:
            self._values["content_key_location_from_header_enabled"] = content_key_location_from_header_enabled
        if content_key_location_from_key_id is not None:
            self._values["content_key_location_from_key_id"] = content_key_location_from_key_id
        if content_type is not None:
            self._values["content_type"] = content_type
        if expiration_date is not None:
            self._values["expiration_date"] = expiration_date
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if license_type is not None:
            self._values["license_type"] = license_type
        if play_right is not None:
            self._values["play_right"] = play_right
        if relative_begin_date is not None:
            self._values["relative_begin_date"] = relative_begin_date
        if relative_expiration_date is not None:
            self._values["relative_expiration_date"] = relative_expiration_date

    @builtins.property
    def allow_test_devices(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#allow_test_devices MediaContentKeyPolicy#allow_test_devices}.'''
        result = self._values.get("allow_test_devices")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def begin_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#begin_date MediaContentKeyPolicy#begin_date}.'''
        result = self._values.get("begin_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_key_location_from_header_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_key_location_from_header_enabled MediaContentKeyPolicy#content_key_location_from_header_enabled}.'''
        result = self._values.get("content_key_location_from_header_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_key_location_from_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_key_location_from_key_id MediaContentKeyPolicy#content_key_location_from_key_id}.'''
        result = self._values.get("content_key_location_from_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#content_type MediaContentKeyPolicy#content_type}.'''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#expiration_date MediaContentKeyPolicy#expiration_date}.'''
        result = self._values.get("expiration_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#grace_period MediaContentKeyPolicy#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#license_type MediaContentKeyPolicy#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_right(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight"]:
        '''play_right block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#play_right MediaContentKeyPolicy#play_right}
        '''
        result = self._values.get("play_right")
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight"], result)

    @builtins.property
    def relative_begin_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#relative_begin_date MediaContentKeyPolicy#relative_begin_date}.'''
        result = self._values.get("relative_begin_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relative_expiration_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#relative_expiration_date MediaContentKeyPolicy#relative_expiration_date}.'''
        result = self._values.get("relative_expiration_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPlayRight")
    def put_play_right(
        self,
        *,
        agc_and_color_stripe_restriction: typing.Optional[jsii.Number] = None,
        allow_passing_video_content_to_unknown_output: typing.Optional[builtins.str] = None,
        analog_video_opl: typing.Optional[jsii.Number] = None,
        compressed_digital_audio_opl: typing.Optional[jsii.Number] = None,
        digital_video_only_content_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        first_play_expiration: typing.Optional[builtins.str] = None,
        image_constraint_for_analog_component_video_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        image_constraint_for_analog_computer_monitor_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scms_restriction: typing.Optional[jsii.Number] = None,
        uncompressed_digital_audio_opl: typing.Optional[jsii.Number] = None,
        uncompressed_digital_video_opl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param agc_and_color_stripe_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#agc_and_color_stripe_restriction MediaContentKeyPolicy#agc_and_color_stripe_restriction}.
        :param allow_passing_video_content_to_unknown_output: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#allow_passing_video_content_to_unknown_output MediaContentKeyPolicy#allow_passing_video_content_to_unknown_output}.
        :param analog_video_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#analog_video_opl MediaContentKeyPolicy#analog_video_opl}.
        :param compressed_digital_audio_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#compressed_digital_audio_opl MediaContentKeyPolicy#compressed_digital_audio_opl}.
        :param digital_video_only_content_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#digital_video_only_content_restriction MediaContentKeyPolicy#digital_video_only_content_restriction}.
        :param first_play_expiration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#first_play_expiration MediaContentKeyPolicy#first_play_expiration}.
        :param image_constraint_for_analog_component_video_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_component_video_restriction MediaContentKeyPolicy#image_constraint_for_analog_component_video_restriction}.
        :param image_constraint_for_analog_computer_monitor_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_computer_monitor_restriction MediaContentKeyPolicy#image_constraint_for_analog_computer_monitor_restriction}.
        :param scms_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#scms_restriction MediaContentKeyPolicy#scms_restriction}.
        :param uncompressed_digital_audio_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_audio_opl MediaContentKeyPolicy#uncompressed_digital_audio_opl}.
        :param uncompressed_digital_video_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_video_opl MediaContentKeyPolicy#uncompressed_digital_video_opl}.
        '''
        value = MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight(
            agc_and_color_stripe_restriction=agc_and_color_stripe_restriction,
            allow_passing_video_content_to_unknown_output=allow_passing_video_content_to_unknown_output,
            analog_video_opl=analog_video_opl,
            compressed_digital_audio_opl=compressed_digital_audio_opl,
            digital_video_only_content_restriction=digital_video_only_content_restriction,
            first_play_expiration=first_play_expiration,
            image_constraint_for_analog_component_video_restriction=image_constraint_for_analog_component_video_restriction,
            image_constraint_for_analog_computer_monitor_restriction=image_constraint_for_analog_computer_monitor_restriction,
            scms_restriction=scms_restriction,
            uncompressed_digital_audio_opl=uncompressed_digital_audio_opl,
            uncompressed_digital_video_opl=uncompressed_digital_video_opl,
        )

        return typing.cast(None, jsii.invoke(self, "putPlayRight", [value]))

    @jsii.member(jsii_name="resetAllowTestDevices")
    def reset_allow_test_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowTestDevices", []))

    @jsii.member(jsii_name="resetBeginDate")
    def reset_begin_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBeginDate", []))

    @jsii.member(jsii_name="resetContentKeyLocationFromHeaderEnabled")
    def reset_content_key_location_from_header_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentKeyLocationFromHeaderEnabled", []))

    @jsii.member(jsii_name="resetContentKeyLocationFromKeyId")
    def reset_content_key_location_from_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentKeyLocationFromKeyId", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetExpirationDate")
    def reset_expiration_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationDate", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetPlayRight")
    def reset_play_right(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlayRight", []))

    @jsii.member(jsii_name="resetRelativeBeginDate")
    def reset_relative_begin_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelativeBeginDate", []))

    @jsii.member(jsii_name="resetRelativeExpirationDate")
    def reset_relative_expiration_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelativeExpirationDate", []))

    @builtins.property
    @jsii.member(jsii_name="playRight")
    def play_right(
        self,
    ) -> "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference":
        return typing.cast("MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference", jsii.get(self, "playRight"))

    @builtins.property
    @jsii.member(jsii_name="allowTestDevicesInput")
    def allow_test_devices_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowTestDevicesInput"))

    @builtins.property
    @jsii.member(jsii_name="beginDateInput")
    def begin_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "beginDateInput"))

    @builtins.property
    @jsii.member(jsii_name="contentKeyLocationFromHeaderEnabledInput")
    def content_key_location_from_header_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "contentKeyLocationFromHeaderEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="contentKeyLocationFromKeyIdInput")
    def content_key_location_from_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentKeyLocationFromKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationDateInput")
    def expiration_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationDateInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="playRightInput")
    def play_right_input(
        self,
    ) -> typing.Optional["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight"]:
        return typing.cast(typing.Optional["MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight"], jsii.get(self, "playRightInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeBeginDateInput")
    def relative_begin_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeBeginDateInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeExpirationDateInput")
    def relative_expiration_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeExpirationDateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowTestDevices")
    def allow_test_devices(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowTestDevices"))

    @allow_test_devices.setter
    def allow_test_devices(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "allow_test_devices").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowTestDevices", value)

    @builtins.property
    @jsii.member(jsii_name="beginDate")
    def begin_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "beginDate"))

    @begin_date.setter
    def begin_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "begin_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "beginDate", value)

    @builtins.property
    @jsii.member(jsii_name="contentKeyLocationFromHeaderEnabled")
    def content_key_location_from_header_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "contentKeyLocationFromHeaderEnabled"))

    @content_key_location_from_header_enabled.setter
    def content_key_location_from_header_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "content_key_location_from_header_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentKeyLocationFromHeaderEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="contentKeyLocationFromKeyId")
    def content_key_location_from_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentKeyLocationFromKeyId"))

    @content_key_location_from_key_id.setter
    def content_key_location_from_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "content_key_location_from_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentKeyLocationFromKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="expirationDate")
    def expiration_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationDate"))

    @expiration_date.setter
    def expiration_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "expiration_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationDate", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="relativeBeginDate")
    def relative_begin_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeBeginDate"))

    @relative_begin_date.setter
    def relative_begin_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "relative_begin_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeBeginDate", value)

    @builtins.property
    @jsii.member(jsii_name="relativeExpirationDate")
    def relative_expiration_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeExpirationDate"))

    @relative_expiration_date.setter
    def relative_expiration_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "relative_expiration_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeExpirationDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight",
    jsii_struct_bases=[],
    name_mapping={
        "agc_and_color_stripe_restriction": "agcAndColorStripeRestriction",
        "allow_passing_video_content_to_unknown_output": "allowPassingVideoContentToUnknownOutput",
        "analog_video_opl": "analogVideoOpl",
        "compressed_digital_audio_opl": "compressedDigitalAudioOpl",
        "digital_video_only_content_restriction": "digitalVideoOnlyContentRestriction",
        "first_play_expiration": "firstPlayExpiration",
        "image_constraint_for_analog_component_video_restriction": "imageConstraintForAnalogComponentVideoRestriction",
        "image_constraint_for_analog_computer_monitor_restriction": "imageConstraintForAnalogComputerMonitorRestriction",
        "scms_restriction": "scmsRestriction",
        "uncompressed_digital_audio_opl": "uncompressedDigitalAudioOpl",
        "uncompressed_digital_video_opl": "uncompressedDigitalVideoOpl",
    },
)
class MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight:
    def __init__(
        self,
        *,
        agc_and_color_stripe_restriction: typing.Optional[jsii.Number] = None,
        allow_passing_video_content_to_unknown_output: typing.Optional[builtins.str] = None,
        analog_video_opl: typing.Optional[jsii.Number] = None,
        compressed_digital_audio_opl: typing.Optional[jsii.Number] = None,
        digital_video_only_content_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        first_play_expiration: typing.Optional[builtins.str] = None,
        image_constraint_for_analog_component_video_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        image_constraint_for_analog_computer_monitor_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scms_restriction: typing.Optional[jsii.Number] = None,
        uncompressed_digital_audio_opl: typing.Optional[jsii.Number] = None,
        uncompressed_digital_video_opl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param agc_and_color_stripe_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#agc_and_color_stripe_restriction MediaContentKeyPolicy#agc_and_color_stripe_restriction}.
        :param allow_passing_video_content_to_unknown_output: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#allow_passing_video_content_to_unknown_output MediaContentKeyPolicy#allow_passing_video_content_to_unknown_output}.
        :param analog_video_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#analog_video_opl MediaContentKeyPolicy#analog_video_opl}.
        :param compressed_digital_audio_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#compressed_digital_audio_opl MediaContentKeyPolicy#compressed_digital_audio_opl}.
        :param digital_video_only_content_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#digital_video_only_content_restriction MediaContentKeyPolicy#digital_video_only_content_restriction}.
        :param first_play_expiration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#first_play_expiration MediaContentKeyPolicy#first_play_expiration}.
        :param image_constraint_for_analog_component_video_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_component_video_restriction MediaContentKeyPolicy#image_constraint_for_analog_component_video_restriction}.
        :param image_constraint_for_analog_computer_monitor_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_computer_monitor_restriction MediaContentKeyPolicy#image_constraint_for_analog_computer_monitor_restriction}.
        :param scms_restriction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#scms_restriction MediaContentKeyPolicy#scms_restriction}.
        :param uncompressed_digital_audio_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_audio_opl MediaContentKeyPolicy#uncompressed_digital_audio_opl}.
        :param uncompressed_digital_video_opl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_video_opl MediaContentKeyPolicy#uncompressed_digital_video_opl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight.__init__)
            check_type(argname="argument agc_and_color_stripe_restriction", value=agc_and_color_stripe_restriction, expected_type=type_hints["agc_and_color_stripe_restriction"])
            check_type(argname="argument allow_passing_video_content_to_unknown_output", value=allow_passing_video_content_to_unknown_output, expected_type=type_hints["allow_passing_video_content_to_unknown_output"])
            check_type(argname="argument analog_video_opl", value=analog_video_opl, expected_type=type_hints["analog_video_opl"])
            check_type(argname="argument compressed_digital_audio_opl", value=compressed_digital_audio_opl, expected_type=type_hints["compressed_digital_audio_opl"])
            check_type(argname="argument digital_video_only_content_restriction", value=digital_video_only_content_restriction, expected_type=type_hints["digital_video_only_content_restriction"])
            check_type(argname="argument first_play_expiration", value=first_play_expiration, expected_type=type_hints["first_play_expiration"])
            check_type(argname="argument image_constraint_for_analog_component_video_restriction", value=image_constraint_for_analog_component_video_restriction, expected_type=type_hints["image_constraint_for_analog_component_video_restriction"])
            check_type(argname="argument image_constraint_for_analog_computer_monitor_restriction", value=image_constraint_for_analog_computer_monitor_restriction, expected_type=type_hints["image_constraint_for_analog_computer_monitor_restriction"])
            check_type(argname="argument scms_restriction", value=scms_restriction, expected_type=type_hints["scms_restriction"])
            check_type(argname="argument uncompressed_digital_audio_opl", value=uncompressed_digital_audio_opl, expected_type=type_hints["uncompressed_digital_audio_opl"])
            check_type(argname="argument uncompressed_digital_video_opl", value=uncompressed_digital_video_opl, expected_type=type_hints["uncompressed_digital_video_opl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if agc_and_color_stripe_restriction is not None:
            self._values["agc_and_color_stripe_restriction"] = agc_and_color_stripe_restriction
        if allow_passing_video_content_to_unknown_output is not None:
            self._values["allow_passing_video_content_to_unknown_output"] = allow_passing_video_content_to_unknown_output
        if analog_video_opl is not None:
            self._values["analog_video_opl"] = analog_video_opl
        if compressed_digital_audio_opl is not None:
            self._values["compressed_digital_audio_opl"] = compressed_digital_audio_opl
        if digital_video_only_content_restriction is not None:
            self._values["digital_video_only_content_restriction"] = digital_video_only_content_restriction
        if first_play_expiration is not None:
            self._values["first_play_expiration"] = first_play_expiration
        if image_constraint_for_analog_component_video_restriction is not None:
            self._values["image_constraint_for_analog_component_video_restriction"] = image_constraint_for_analog_component_video_restriction
        if image_constraint_for_analog_computer_monitor_restriction is not None:
            self._values["image_constraint_for_analog_computer_monitor_restriction"] = image_constraint_for_analog_computer_monitor_restriction
        if scms_restriction is not None:
            self._values["scms_restriction"] = scms_restriction
        if uncompressed_digital_audio_opl is not None:
            self._values["uncompressed_digital_audio_opl"] = uncompressed_digital_audio_opl
        if uncompressed_digital_video_opl is not None:
            self._values["uncompressed_digital_video_opl"] = uncompressed_digital_video_opl

    @builtins.property
    def agc_and_color_stripe_restriction(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#agc_and_color_stripe_restriction MediaContentKeyPolicy#agc_and_color_stripe_restriction}.'''
        result = self._values.get("agc_and_color_stripe_restriction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_passing_video_content_to_unknown_output(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#allow_passing_video_content_to_unknown_output MediaContentKeyPolicy#allow_passing_video_content_to_unknown_output}.'''
        result = self._values.get("allow_passing_video_content_to_unknown_output")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def analog_video_opl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#analog_video_opl MediaContentKeyPolicy#analog_video_opl}.'''
        result = self._values.get("analog_video_opl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def compressed_digital_audio_opl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#compressed_digital_audio_opl MediaContentKeyPolicy#compressed_digital_audio_opl}.'''
        result = self._values.get("compressed_digital_audio_opl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def digital_video_only_content_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#digital_video_only_content_restriction MediaContentKeyPolicy#digital_video_only_content_restriction}.'''
        result = self._values.get("digital_video_only_content_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def first_play_expiration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#first_play_expiration MediaContentKeyPolicy#first_play_expiration}.'''
        result = self._values.get("first_play_expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_constraint_for_analog_component_video_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_component_video_restriction MediaContentKeyPolicy#image_constraint_for_analog_component_video_restriction}.'''
        result = self._values.get("image_constraint_for_analog_component_video_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def image_constraint_for_analog_computer_monitor_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#image_constraint_for_analog_computer_monitor_restriction MediaContentKeyPolicy#image_constraint_for_analog_computer_monitor_restriction}.'''
        result = self._values.get("image_constraint_for_analog_computer_monitor_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scms_restriction(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#scms_restriction MediaContentKeyPolicy#scms_restriction}.'''
        result = self._values.get("scms_restriction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uncompressed_digital_audio_opl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_audio_opl MediaContentKeyPolicy#uncompressed_digital_audio_opl}.'''
        result = self._values.get("uncompressed_digital_audio_opl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uncompressed_digital_video_opl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#uncompressed_digital_video_opl MediaContentKeyPolicy#uncompressed_digital_video_opl}.'''
        result = self._values.get("uncompressed_digital_video_opl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAgcAndColorStripeRestriction")
    def reset_agc_and_color_stripe_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgcAndColorStripeRestriction", []))

    @jsii.member(jsii_name="resetAllowPassingVideoContentToUnknownOutput")
    def reset_allow_passing_video_content_to_unknown_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPassingVideoContentToUnknownOutput", []))

    @jsii.member(jsii_name="resetAnalogVideoOpl")
    def reset_analog_video_opl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalogVideoOpl", []))

    @jsii.member(jsii_name="resetCompressedDigitalAudioOpl")
    def reset_compressed_digital_audio_opl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressedDigitalAudioOpl", []))

    @jsii.member(jsii_name="resetDigitalVideoOnlyContentRestriction")
    def reset_digital_video_only_content_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigitalVideoOnlyContentRestriction", []))

    @jsii.member(jsii_name="resetFirstPlayExpiration")
    def reset_first_play_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstPlayExpiration", []))

    @jsii.member(jsii_name="resetImageConstraintForAnalogComponentVideoRestriction")
    def reset_image_constraint_for_analog_component_video_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageConstraintForAnalogComponentVideoRestriction", []))

    @jsii.member(jsii_name="resetImageConstraintForAnalogComputerMonitorRestriction")
    def reset_image_constraint_for_analog_computer_monitor_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageConstraintForAnalogComputerMonitorRestriction", []))

    @jsii.member(jsii_name="resetScmsRestriction")
    def reset_scms_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmsRestriction", []))

    @jsii.member(jsii_name="resetUncompressedDigitalAudioOpl")
    def reset_uncompressed_digital_audio_opl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUncompressedDigitalAudioOpl", []))

    @jsii.member(jsii_name="resetUncompressedDigitalVideoOpl")
    def reset_uncompressed_digital_video_opl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUncompressedDigitalVideoOpl", []))

    @builtins.property
    @jsii.member(jsii_name="agcAndColorStripeRestrictionInput")
    def agc_and_color_stripe_restriction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "agcAndColorStripeRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPassingVideoContentToUnknownOutputInput")
    def allow_passing_video_content_to_unknown_output_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowPassingVideoContentToUnknownOutputInput"))

    @builtins.property
    @jsii.member(jsii_name="analogVideoOplInput")
    def analog_video_opl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "analogVideoOplInput"))

    @builtins.property
    @jsii.member(jsii_name="compressedDigitalAudioOplInput")
    def compressed_digital_audio_opl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "compressedDigitalAudioOplInput"))

    @builtins.property
    @jsii.member(jsii_name="digitalVideoOnlyContentRestrictionInput")
    def digital_video_only_content_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "digitalVideoOnlyContentRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="firstPlayExpirationInput")
    def first_play_expiration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstPlayExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="imageConstraintForAnalogComponentVideoRestrictionInput")
    def image_constraint_for_analog_component_video_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "imageConstraintForAnalogComponentVideoRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="imageConstraintForAnalogComputerMonitorRestrictionInput")
    def image_constraint_for_analog_computer_monitor_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "imageConstraintForAnalogComputerMonitorRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmsRestrictionInput")
    def scms_restriction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scmsRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="uncompressedDigitalAudioOplInput")
    def uncompressed_digital_audio_opl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uncompressedDigitalAudioOplInput"))

    @builtins.property
    @jsii.member(jsii_name="uncompressedDigitalVideoOplInput")
    def uncompressed_digital_video_opl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uncompressedDigitalVideoOplInput"))

    @builtins.property
    @jsii.member(jsii_name="agcAndColorStripeRestriction")
    def agc_and_color_stripe_restriction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "agcAndColorStripeRestriction"))

    @agc_and_color_stripe_restriction.setter
    def agc_and_color_stripe_restriction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "agc_and_color_stripe_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agcAndColorStripeRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="allowPassingVideoContentToUnknownOutput")
    def allow_passing_video_content_to_unknown_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowPassingVideoContentToUnknownOutput"))

    @allow_passing_video_content_to_unknown_output.setter
    def allow_passing_video_content_to_unknown_output(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "allow_passing_video_content_to_unknown_output").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPassingVideoContentToUnknownOutput", value)

    @builtins.property
    @jsii.member(jsii_name="analogVideoOpl")
    def analog_video_opl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "analogVideoOpl"))

    @analog_video_opl.setter
    def analog_video_opl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "analog_video_opl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analogVideoOpl", value)

    @builtins.property
    @jsii.member(jsii_name="compressedDigitalAudioOpl")
    def compressed_digital_audio_opl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "compressedDigitalAudioOpl"))

    @compressed_digital_audio_opl.setter
    def compressed_digital_audio_opl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "compressed_digital_audio_opl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressedDigitalAudioOpl", value)

    @builtins.property
    @jsii.member(jsii_name="digitalVideoOnlyContentRestriction")
    def digital_video_only_content_restriction(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "digitalVideoOnlyContentRestriction"))

    @digital_video_only_content_restriction.setter
    def digital_video_only_content_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "digital_video_only_content_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digitalVideoOnlyContentRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="firstPlayExpiration")
    def first_play_expiration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstPlayExpiration"))

    @first_play_expiration.setter
    def first_play_expiration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "first_play_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstPlayExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="imageConstraintForAnalogComponentVideoRestriction")
    def image_constraint_for_analog_component_video_restriction(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "imageConstraintForAnalogComponentVideoRestriction"))

    @image_constraint_for_analog_component_video_restriction.setter
    def image_constraint_for_analog_component_video_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "image_constraint_for_analog_component_video_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageConstraintForAnalogComponentVideoRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="imageConstraintForAnalogComputerMonitorRestriction")
    def image_constraint_for_analog_computer_monitor_restriction(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "imageConstraintForAnalogComputerMonitorRestriction"))

    @image_constraint_for_analog_computer_monitor_restriction.setter
    def image_constraint_for_analog_computer_monitor_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "image_constraint_for_analog_computer_monitor_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageConstraintForAnalogComputerMonitorRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="scmsRestriction")
    def scms_restriction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scmsRestriction"))

    @scms_restriction.setter
    def scms_restriction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "scms_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scmsRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="uncompressedDigitalAudioOpl")
    def uncompressed_digital_audio_opl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uncompressedDigitalAudioOpl"))

    @uncompressed_digital_audio_opl.setter
    def uncompressed_digital_audio_opl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "uncompressed_digital_audio_opl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uncompressedDigitalAudioOpl", value)

    @builtins.property
    @jsii.member(jsii_name="uncompressedDigitalVideoOpl")
    def uncompressed_digital_video_opl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uncompressedDigitalVideoOpl"))

    @uncompressed_digital_video_opl.setter
    def uncompressed_digital_video_opl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "uncompressed_digital_video_opl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uncompressedDigitalVideoOpl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionTokenRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "audience": "audience",
        "issuer": "issuer",
        "open_id_connect_discovery_document": "openIdConnectDiscoveryDocument",
        "primary_rsa_token_key_exponent": "primaryRsaTokenKeyExponent",
        "primary_rsa_token_key_modulus": "primaryRsaTokenKeyModulus",
        "primary_symmetric_token_key": "primarySymmetricTokenKey",
        "primary_x509_token_key_raw": "primaryX509TokenKeyRaw",
        "required_claim": "requiredClaim",
        "token_type": "tokenType",
    },
)
class MediaContentKeyPolicyPolicyOptionTokenRestriction:
    def __init__(
        self,
        *,
        audience: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        open_id_connect_discovery_document: typing.Optional[builtins.str] = None,
        primary_rsa_token_key_exponent: typing.Optional[builtins.str] = None,
        primary_rsa_token_key_modulus: typing.Optional[builtins.str] = None,
        primary_symmetric_token_key: typing.Optional[builtins.str] = None,
        primary_x509_token_key_raw: typing.Optional[builtins.str] = None,
        required_claim: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim", typing.Dict[str, typing.Any]]]]] = None,
        token_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#audience MediaContentKeyPolicy#audience}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#issuer MediaContentKeyPolicy#issuer}.
        :param open_id_connect_discovery_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#open_id_connect_discovery_document MediaContentKeyPolicy#open_id_connect_discovery_document}.
        :param primary_rsa_token_key_exponent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_exponent MediaContentKeyPolicy#primary_rsa_token_key_exponent}.
        :param primary_rsa_token_key_modulus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_modulus MediaContentKeyPolicy#primary_rsa_token_key_modulus}.
        :param primary_symmetric_token_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_symmetric_token_key MediaContentKeyPolicy#primary_symmetric_token_key}.
        :param primary_x509_token_key_raw: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_x509_token_key_raw MediaContentKeyPolicy#primary_x509_token_key_raw}.
        :param required_claim: required_claim block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#required_claim MediaContentKeyPolicy#required_claim}
        :param token_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#token_type MediaContentKeyPolicy#token_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestriction.__init__)
            check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument open_id_connect_discovery_document", value=open_id_connect_discovery_document, expected_type=type_hints["open_id_connect_discovery_document"])
            check_type(argname="argument primary_rsa_token_key_exponent", value=primary_rsa_token_key_exponent, expected_type=type_hints["primary_rsa_token_key_exponent"])
            check_type(argname="argument primary_rsa_token_key_modulus", value=primary_rsa_token_key_modulus, expected_type=type_hints["primary_rsa_token_key_modulus"])
            check_type(argname="argument primary_symmetric_token_key", value=primary_symmetric_token_key, expected_type=type_hints["primary_symmetric_token_key"])
            check_type(argname="argument primary_x509_token_key_raw", value=primary_x509_token_key_raw, expected_type=type_hints["primary_x509_token_key_raw"])
            check_type(argname="argument required_claim", value=required_claim, expected_type=type_hints["required_claim"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audience is not None:
            self._values["audience"] = audience
        if issuer is not None:
            self._values["issuer"] = issuer
        if open_id_connect_discovery_document is not None:
            self._values["open_id_connect_discovery_document"] = open_id_connect_discovery_document
        if primary_rsa_token_key_exponent is not None:
            self._values["primary_rsa_token_key_exponent"] = primary_rsa_token_key_exponent
        if primary_rsa_token_key_modulus is not None:
            self._values["primary_rsa_token_key_modulus"] = primary_rsa_token_key_modulus
        if primary_symmetric_token_key is not None:
            self._values["primary_symmetric_token_key"] = primary_symmetric_token_key
        if primary_x509_token_key_raw is not None:
            self._values["primary_x509_token_key_raw"] = primary_x509_token_key_raw
        if required_claim is not None:
            self._values["required_claim"] = required_claim
        if token_type is not None:
            self._values["token_type"] = token_type

    @builtins.property
    def audience(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#audience MediaContentKeyPolicy#audience}.'''
        result = self._values.get("audience")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#issuer MediaContentKeyPolicy#issuer}.'''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_id_connect_discovery_document(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#open_id_connect_discovery_document MediaContentKeyPolicy#open_id_connect_discovery_document}.'''
        result = self._values.get("open_id_connect_discovery_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_rsa_token_key_exponent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_exponent MediaContentKeyPolicy#primary_rsa_token_key_exponent}.'''
        result = self._values.get("primary_rsa_token_key_exponent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_rsa_token_key_modulus(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_rsa_token_key_modulus MediaContentKeyPolicy#primary_rsa_token_key_modulus}.'''
        result = self._values.get("primary_rsa_token_key_modulus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_symmetric_token_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_symmetric_token_key MediaContentKeyPolicy#primary_symmetric_token_key}.'''
        result = self._values.get("primary_symmetric_token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_x509_token_key_raw(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#primary_x509_token_key_raw MediaContentKeyPolicy#primary_x509_token_key_raw}.'''
        result = self._values.get("primary_x509_token_key_raw")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required_claim(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim"]]]:
        '''required_claim block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#required_claim MediaContentKeyPolicy#required_claim}
        '''
        result = self._values.get("required_claim")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim"]]], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#token_type MediaContentKeyPolicy#token_type}.'''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionTokenRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequiredClaim")
    def put_required_claim(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference.put_required_claim)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequiredClaim", [value]))

    @jsii.member(jsii_name="resetAudience")
    def reset_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudience", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetOpenIdConnectDiscoveryDocument")
    def reset_open_id_connect_discovery_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenIdConnectDiscoveryDocument", []))

    @jsii.member(jsii_name="resetPrimaryRsaTokenKeyExponent")
    def reset_primary_rsa_token_key_exponent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryRsaTokenKeyExponent", []))

    @jsii.member(jsii_name="resetPrimaryRsaTokenKeyModulus")
    def reset_primary_rsa_token_key_modulus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryRsaTokenKeyModulus", []))

    @jsii.member(jsii_name="resetPrimarySymmetricTokenKey")
    def reset_primary_symmetric_token_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimarySymmetricTokenKey", []))

    @jsii.member(jsii_name="resetPrimaryX509TokenKeyRaw")
    def reset_primary_x509_token_key_raw(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryX509TokenKeyRaw", []))

    @jsii.member(jsii_name="resetRequiredClaim")
    def reset_required_claim(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredClaim", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @builtins.property
    @jsii.member(jsii_name="requiredClaim")
    def required_claim(
        self,
    ) -> "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList":
        return typing.cast("MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList", jsii.get(self, "requiredClaim"))

    @builtins.property
    @jsii.member(jsii_name="audienceInput")
    def audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audienceInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectDiscoveryDocumentInput")
    def open_id_connect_discovery_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "openIdConnectDiscoveryDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryRsaTokenKeyExponentInput")
    def primary_rsa_token_key_exponent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryRsaTokenKeyExponentInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryRsaTokenKeyModulusInput")
    def primary_rsa_token_key_modulus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryRsaTokenKeyModulusInput"))

    @builtins.property
    @jsii.member(jsii_name="primarySymmetricTokenKeyInput")
    def primary_symmetric_token_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primarySymmetricTokenKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryX509TokenKeyRawInput")
    def primary_x509_token_key_raw_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryX509TokenKeyRawInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredClaimInput")
    def required_claim_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim"]]], jsii.get(self, "requiredClaimInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="audience")
    def audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audience"))

    @audience.setter
    def audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audience", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="openIdConnectDiscoveryDocument")
    def open_id_connect_discovery_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectDiscoveryDocument"))

    @open_id_connect_discovery_document.setter
    def open_id_connect_discovery_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "open_id_connect_discovery_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openIdConnectDiscoveryDocument", value)

    @builtins.property
    @jsii.member(jsii_name="primaryRsaTokenKeyExponent")
    def primary_rsa_token_key_exponent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryRsaTokenKeyExponent"))

    @primary_rsa_token_key_exponent.setter
    def primary_rsa_token_key_exponent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "primary_rsa_token_key_exponent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryRsaTokenKeyExponent", value)

    @builtins.property
    @jsii.member(jsii_name="primaryRsaTokenKeyModulus")
    def primary_rsa_token_key_modulus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryRsaTokenKeyModulus"))

    @primary_rsa_token_key_modulus.setter
    def primary_rsa_token_key_modulus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "primary_rsa_token_key_modulus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryRsaTokenKeyModulus", value)

    @builtins.property
    @jsii.member(jsii_name="primarySymmetricTokenKey")
    def primary_symmetric_token_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primarySymmetricTokenKey"))

    @primary_symmetric_token_key.setter
    def primary_symmetric_token_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "primary_symmetric_token_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primarySymmetricTokenKey", value)

    @builtins.property
    @jsii.member(jsii_name="primaryX509TokenKeyRaw")
    def primary_x509_token_key_raw(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryX509TokenKeyRaw"))

    @primary_x509_token_key_raw.setter
    def primary_x509_token_key_raw(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "primary_x509_token_key_raw").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryX509TokenKeyRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MediaContentKeyPolicyPolicyOptionTokenRestriction]:
        return typing.cast(typing.Optional[MediaContentKeyPolicyPolicyOptionTokenRestriction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaContentKeyPolicyPolicyOptionTokenRestriction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#type MediaContentKeyPolicy#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#value MediaContentKeyPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#type MediaContentKeyPolicy#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#value MediaContentKeyPolicy#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MediaContentKeyPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#create MediaContentKeyPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#delete MediaContentKeyPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#read MediaContentKeyPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#update MediaContentKeyPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaContentKeyPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#create MediaContentKeyPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#delete MediaContentKeyPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#read MediaContentKeyPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_content_key_policy#update MediaContentKeyPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaContentKeyPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaContentKeyPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaContentKeyPolicy.MediaContentKeyPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaContentKeyPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaContentKeyPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaContentKeyPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaContentKeyPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaContentKeyPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaContentKeyPolicy",
    "MediaContentKeyPolicyConfig",
    "MediaContentKeyPolicyPolicyOption",
    "MediaContentKeyPolicyPolicyOptionFairplayConfiguration",
    "MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfiguration",
    "MediaContentKeyPolicyPolicyOptionFairplayConfigurationOfflineRentalConfigurationOutputReference",
    "MediaContentKeyPolicyPolicyOptionFairplayConfigurationOutputReference",
    "MediaContentKeyPolicyPolicyOptionList",
    "MediaContentKeyPolicyPolicyOptionOutputReference",
    "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicense",
    "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseList",
    "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicenseOutputReference",
    "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRight",
    "MediaContentKeyPolicyPolicyOptionPlayreadyConfigurationLicensePlayRightOutputReference",
    "MediaContentKeyPolicyPolicyOptionTokenRestriction",
    "MediaContentKeyPolicyPolicyOptionTokenRestrictionOutputReference",
    "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaim",
    "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimList",
    "MediaContentKeyPolicyPolicyOptionTokenRestrictionRequiredClaimOutputReference",
    "MediaContentKeyPolicyTimeouts",
    "MediaContentKeyPolicyTimeoutsOutputReference",
]

publication.publish()
