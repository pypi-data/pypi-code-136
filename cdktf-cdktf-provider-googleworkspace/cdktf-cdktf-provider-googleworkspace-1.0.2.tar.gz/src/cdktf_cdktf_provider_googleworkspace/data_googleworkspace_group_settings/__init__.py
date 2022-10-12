'''
# `data_googleworkspace_group_settings`

Refer to the Terraform Registory for docs: [`data_googleworkspace_group_settings`](https://www.terraform.io/docs/providers/googleworkspace/d/group_settings).
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


class DataGoogleworkspaceGroupSettings(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.dataGoogleworkspaceGroupSettings.DataGoogleworkspaceGroupSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings googleworkspace_group_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        email: builtins.str,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings googleworkspace_group_settings} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleworkspaceGroupSettings.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataGoogleworkspaceGroupSettingsConfig(
            email=email,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowExternalMembers")
    def allow_external_members(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowExternalMembers"))

    @builtins.property
    @jsii.member(jsii_name="allowWebPosting")
    def allow_web_posting(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowWebPosting"))

    @builtins.property
    @jsii.member(jsii_name="archiveOnly")
    def archive_only(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "archiveOnly"))

    @builtins.property
    @jsii.member(jsii_name="customFooterText")
    def custom_footer_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customFooterText"))

    @builtins.property
    @jsii.member(jsii_name="customReplyTo")
    def custom_reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customReplyTo"))

    @builtins.property
    @jsii.member(jsii_name="customRolesEnabledForSettingsToBeMerged")
    def custom_roles_enabled_for_settings_to_be_merged(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "customRolesEnabledForSettingsToBeMerged"))

    @builtins.property
    @jsii.member(jsii_name="defaultMessageDenyNotificationText")
    def default_message_deny_notification_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultMessageDenyNotificationText"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="enableCollaborativeInbox")
    def enable_collaborative_inbox(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableCollaborativeInbox"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="includeCustomFooter")
    def include_custom_footer(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeCustomFooter"))

    @builtins.property
    @jsii.member(jsii_name="includeInGlobalAddressList")
    def include_in_global_address_list(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeInGlobalAddressList"))

    @builtins.property
    @jsii.member(jsii_name="isArchived")
    def is_archived(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isArchived"))

    @builtins.property
    @jsii.member(jsii_name="membersCanPostAsTheGroup")
    def members_can_post_as_the_group(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "membersCanPostAsTheGroup"))

    @builtins.property
    @jsii.member(jsii_name="messageModerationLevel")
    def message_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageModerationLevel"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="primaryLanguage")
    def primary_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLanguage"))

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @builtins.property
    @jsii.member(jsii_name="sendMessageDenyNotification")
    def send_message_deny_notification(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "sendMessageDenyNotification"))

    @builtins.property
    @jsii.member(jsii_name="spamModerationLevel")
    def spam_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spamModerationLevel"))

    @builtins.property
    @jsii.member(jsii_name="whoCanAssistContent")
    def who_can_assist_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanAssistContent"))

    @builtins.property
    @jsii.member(jsii_name="whoCanContactOwner")
    def who_can_contact_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanContactOwner"))

    @builtins.property
    @jsii.member(jsii_name="whoCanDiscoverGroup")
    def who_can_discover_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanDiscoverGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanJoin")
    def who_can_join(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanJoin"))

    @builtins.property
    @jsii.member(jsii_name="whoCanLeaveGroup")
    def who_can_leave_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanLeaveGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateContent")
    def who_can_moderate_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateContent"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateMembers")
    def who_can_moderate_members(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateMembers"))

    @builtins.property
    @jsii.member(jsii_name="whoCanPostMessage")
    def who_can_post_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanPostMessage"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewGroup")
    def who_can_view_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewMembership")
    def who_can_view_membership(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewMembership"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleworkspaceGroupSettings, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.dataGoogleworkspaceGroupSettings.DataGoogleworkspaceGroupSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "email": "email",
    },
)
class DataGoogleworkspaceGroupSettingsConfig(cdktf.TerraformMetaArguments):
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
        email: builtins.str,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleworkspaceGroupSettingsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
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
    def email(self) -> builtins.str:
        '''The group's email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleworkspaceGroupSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleworkspaceGroupSettings",
    "DataGoogleworkspaceGroupSettingsConfig",
]

publication.publish()
