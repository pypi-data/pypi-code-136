'''
# `googleworkspace_group_settings`

Refer to the Terraform Registory for docs: [`googleworkspace_group_settings`](https://www.terraform.io/docs/providers/googleworkspace/r/group_settings).
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


class GroupSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.groupSettings.GroupSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings googleworkspace_group_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        email: builtins.str,
        allow_external_members: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_web_posting: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_footer_text: typing.Optional[builtins.str] = None,
        custom_reply_to: typing.Optional[builtins.str] = None,
        default_message_deny_notification_text: typing.Optional[builtins.str] = None,
        enable_collaborative_inbox: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_custom_footer: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_in_global_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        members_can_post_as_the_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_moderation_level: typing.Optional[builtins.str] = None,
        primary_language: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        send_message_deny_notification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spam_moderation_level: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GroupSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
        who_can_assist_content: typing.Optional[builtins.str] = None,
        who_can_contact_owner: typing.Optional[builtins.str] = None,
        who_can_discover_group: typing.Optional[builtins.str] = None,
        who_can_join: typing.Optional[builtins.str] = None,
        who_can_leave_group: typing.Optional[builtins.str] = None,
        who_can_moderate_content: typing.Optional[builtins.str] = None,
        who_can_moderate_members: typing.Optional[builtins.str] = None,
        who_can_post_message: typing.Optional[builtins.str] = None,
        who_can_view_group: typing.Optional[builtins.str] = None,
        who_can_view_membership: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings googleworkspace_group_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#email GroupSettings#email}
        :param allow_external_members: Defaults to ``false``. Identifies whether members external to your organization can join the group. If true, Google Workspace users external to your organization can become members of this group. If false, users not belonging to the organization are not allowed to become members of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_external_members GroupSettings#allow_external_members}
        :param allow_web_posting: Defaults to ``true``. Allows posting from web. If true, allows any member to post to the group forum. If false, Members only use Gmail to communicate with the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_web_posting GroupSettings#allow_web_posting}
        :param archive_only: Defaults to ``false``. Allows the group to be archived only. If true, Group is archived and the group is inactive. New messages to this group are rejected. The older archived messages are browsable and searchable. If true, the ``who_can_post_message`` property is set to ``NONE_CAN_POST``. If reverted from true to false, ``who_can_post_message`` is set to ``ALL_MANAGERS_CAN_POST``. If false, The group is active and can receive messages. When false, updating ``who_can_post_message`` to ``NONE_CAN_POST``, results in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#archive_only GroupSettings#archive_only}
        :param custom_footer_text: Set the content of custom footer text. The maximum number of characters is 1,000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_footer_text GroupSettings#custom_footer_text}
        :param custom_reply_to: An email address used when replying to a message if the ``reply_to`` property is set to ``REPLY_TO_CUSTOM``. This address is defined by an account administrator. When the group's ``reply_to`` property is set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds a custom email address used when replying to a message, the ``custom_reply_to`` property must have a text value or an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_reply_to GroupSettings#custom_reply_to}
        :param default_message_deny_notification_text: When a message is rejected, this is text for the rejection notification sent to the message's author. By default, this property is empty and has no value in the API's response body. The maximum notification text size is 10,000 characters. Requires ``send_message_deny_notification`` property to be true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#default_message_deny_notification_text GroupSettings#default_message_deny_notification_text}
        :param enable_collaborative_inbox: Defaults to ``false``. Specifies whether a collaborative inbox will remain turned on for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#enable_collaborative_inbox GroupSettings#enable_collaborative_inbox}
        :param include_custom_footer: Defaults to ``false``. Whether to include custom footer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_custom_footer GroupSettings#include_custom_footer}
        :param include_in_global_address_list: Defaults to ``true``. Enables the group to be included in the Global Address List. If true, the group is included in the Global Address List. If false, it is not included in the Global Address List. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_in_global_address_list GroupSettings#include_in_global_address_list}
        :param is_archived: Defaults to ``false``. Allows the Group contents to be archived. If true, archive messages sent to the group. If false, Do not keep an archive of messages sent to this group. If false, previously archived messages remain in the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#is_archived GroupSettings#is_archived}
        :param members_can_post_as_the_group: Defaults to ``false``. Enables members to post messages as the group. If true, group member can post messages using the group's email address instead of their own email address. Message appear to originate from the group itself. Any message moderation settings on individual users or new members do not apply to posts made on behalf of the group. If false, members can not post in behalf of the group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#members_can_post_as_the_group GroupSettings#members_can_post_as_the_group}
        :param message_moderation_level: Defaults to ``MODERATE_NONE``. Moderation level of incoming messages. Possible values are: - ``MODERATE_ALL_MESSAGES``: All messages are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NON_MEMBERS``: All messages from non group members are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NEW_MEMBERS``: All messages from new members are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NONE``: No moderator approval is required. Messages are delivered directly to the group. Note: When the ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the ``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam.When ``member_can_post_as_the_group`` is true, any message moderation settings on individual users or new members will not apply to posts made on behalf of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#message_moderation_level GroupSettings#message_moderation_level}
        :param primary_language: The primary language for group. For a group's primary language use the language tags from the Google Workspace languages found at Google Workspace Email Settings API Email Language Tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#primary_language GroupSettings#primary_language}
        :param reply_to: Defaults to ``REPLY_TO_IGNORE``. Specifies who receives the default reply. Possible values are: - ``REPLY_TO_CUSTOM``: For replies to messages, use the group's custom email address. When set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds the custom email address used when replying to a message, the customReplyTo property must have a value. Otherwise an error is returned. - ``REPLY_TO_SENDER``: The reply sent to author of message. - ``REPLY_TO_LIST``: This reply message is sent to the group. - ``REPLY_TO_OWNER``: The reply is sent to the owner(s) of the group. This does not include the group's managers. - ``REPLY_TO_IGNORE``: Group users individually decide where the message reply is sent. - ``REPLY_TO_MANAGERS``: This reply message is sent to the group's managers, which includes all managers and the group owner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#reply_to GroupSettings#reply_to}
        :param send_message_deny_notification: Defaults to ``false``. Allows a member to be notified if the member's message to the group is denied by the group owner. If true, when a message is rejected, send the deny message notification to the message author. The ``default_message_deny_notification_text`` property is dependent on the ``send_message_deny_notification`` property being true. If false, when a message is rejected, no notification is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#send_message_deny_notification GroupSettings#send_message_deny_notification}
        :param spam_moderation_level: Defaults to ``MODERATE``. Specifies moderation levels for messages detected as spam. Possible values are: - ``ALLOW``: Post the message to the group. - ``MODERATE``: Send the message to the moderation queue. This is the default. - ``SILENTLY_MODERATE``: Send the message to the moderation queue, but do not send notification to moderators. - ``REJECT``: Immediately reject the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#spam_moderation_level GroupSettings#spam_moderation_level}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#timeouts GroupSettings#timeouts}
        :param who_can_assist_content: Defaults to ``NONE``. Specifies who can moderate metadata. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``MANAGERS_ONLY`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_assist_content GroupSettings#who_can_assist_content}
        :param who_can_contact_owner: Defaults to ``ANYONE_CAN_CONTACT``. Permission to contact owner of the group via web UI. Possible values are: - ``ALL_IN_DOMAIN_CAN_CONTACT`` - ``ALL_MANAGERS_CAN_CONTACT`` - ``ALL_MEMBERS_CAN_CONTACT`` - ``ANYONE_CAN_CONTACT`` - ``ALL_OWNERS_CAN_CONTACT`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_contact_owner GroupSettings#who_can_contact_owner}
        :param who_can_discover_group: Defaults to ``ALL_IN_DOMAIN_CAN_DISCOVER``. Specifies the set of users for whom this group is discoverable. Possible values are: - ``ANYONE_CAN_DISCOVER`` - ``ALL_IN_DOMAIN_CAN_DISCOVER`` - ``ALL_MEMBERS_CAN_DISCOVER`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_discover_group GroupSettings#who_can_discover_group}
        :param who_can_join: Defaults to ``CAN_REQUEST_TO_JOIN``. Permission to join group. Possible values are: - ``ANYONE_CAN_JOIN``: Any Internet user, both inside and outside your domain, can join the group. - ``ALL_IN_DOMAIN_CAN_JOIN``: Anyone in the account domain can join. This includes accounts with multiple domains. - ``INVITED_CAN_JOIN``: Candidates for membership can be invited to join. - ``CAN_REQUEST_TO_JOIN``: Non members can request an invitation to join. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_join GroupSettings#who_can_join}
        :param who_can_leave_group: Defaults to ``ALL_MEMBERS_CAN_LEAVE``. Permission to leave the group. Possible values are: - ``ALL_MANAGERS_CAN_LEAVE`` - ``ALL_MEMBERS_CAN_LEAVE`` - ``NONE_CAN_LEAVE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_leave_group GroupSettings#who_can_leave_group}
        :param who_can_moderate_content: Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can moderate content. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_content GroupSettings#who_can_moderate_content}
        :param who_can_moderate_members: Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can manage members. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_members GroupSettings#who_can_moderate_members}
        :param who_can_post_message: Permissions to post messages. Possible values are: - ``NONE_CAN_POST``: The group is disabled and archived. No one can post a message to this group. * When archiveOnly is false, updating whoCanPostMessage to NONE_CAN_POST, results in an error. * If archiveOnly is reverted from true to false, whoCanPostMessages is set to ALL_MANAGERS_CAN_POST. - ``ALL_MANAGERS_CAN_POST``: Managers, including group owners, can post messages. - ``ALL_MEMBERS_CAN_POST``: Any group member can post a message. - ``ALL_OWNERS_CAN_POST``: Only group owners can post a message. - ``ALL_IN_DOMAIN_CAN_POST``: Anyone in the account can post a message. - ``ANYONE_CAN_POST``: Any Internet user who outside your account can access your Google Groups service and post a message. Note: When ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam. Users not belonging to the organization are not allowed to become members of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_post_message GroupSettings#who_can_post_message}
        :param who_can_view_group: Defaults to ``ALL_MEMBERS_CAN_VIEW``. Permissions to view group messages. Possible values are: - ``ANYONE_CAN_VIEW``: Any Internet user can view the group's messages. - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in your account can view this group's messages. - ``ALL_MEMBERS_CAN_VIEW``: All group members can view the group's messages. - ``ALL_MANAGERS_CAN_VIEW``: Any group manager can view this group's messages. - ``ALL_OWNERS_CAN_VIEW``: The group owners can view this group's messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_group GroupSettings#who_can_view_group}
        :param who_can_view_membership: Defaults to ``ALL_MEMBERS_CAN_VIEW``. Permissions to view membership. Possible values are: - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in the account can view the group members list. If a group already has external members, those members can still send email to this group. - ``ALL_MEMBERS_CAN_VIEW``: The group members can view the group members list. - ``ALL_MANAGERS_CAN_VIEW``: The group managers can view group members list. - ``ALL_OWNERS_CAN_VIEW``: The group owners can view group members list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_membership GroupSettings#who_can_view_membership}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSettings.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GroupSettingsConfig(
            email=email,
            allow_external_members=allow_external_members,
            allow_web_posting=allow_web_posting,
            archive_only=archive_only,
            custom_footer_text=custom_footer_text,
            custom_reply_to=custom_reply_to,
            default_message_deny_notification_text=default_message_deny_notification_text,
            enable_collaborative_inbox=enable_collaborative_inbox,
            include_custom_footer=include_custom_footer,
            include_in_global_address_list=include_in_global_address_list,
            is_archived=is_archived,
            members_can_post_as_the_group=members_can_post_as_the_group,
            message_moderation_level=message_moderation_level,
            primary_language=primary_language,
            reply_to=reply_to,
            send_message_deny_notification=send_message_deny_notification,
            spam_moderation_level=spam_moderation_level,
            timeouts=timeouts,
            who_can_assist_content=who_can_assist_content,
            who_can_contact_owner=who_can_contact_owner,
            who_can_discover_group=who_can_discover_group,
            who_can_join=who_can_join,
            who_can_leave_group=who_can_leave_group,
            who_can_moderate_content=who_can_moderate_content,
            who_can_moderate_members=who_can_moderate_members,
            who_can_post_message=who_can_post_message,
            who_can_view_group=who_can_view_group,
            who_can_view_membership=who_can_view_membership,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#create GroupSettings#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#update GroupSettings#update}.
        '''
        value = GroupSettingsTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowExternalMembers")
    def reset_allow_external_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowExternalMembers", []))

    @jsii.member(jsii_name="resetAllowWebPosting")
    def reset_allow_web_posting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowWebPosting", []))

    @jsii.member(jsii_name="resetArchiveOnly")
    def reset_archive_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveOnly", []))

    @jsii.member(jsii_name="resetCustomFooterText")
    def reset_custom_footer_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomFooterText", []))

    @jsii.member(jsii_name="resetCustomReplyTo")
    def reset_custom_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomReplyTo", []))

    @jsii.member(jsii_name="resetDefaultMessageDenyNotificationText")
    def reset_default_message_deny_notification_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultMessageDenyNotificationText", []))

    @jsii.member(jsii_name="resetEnableCollaborativeInbox")
    def reset_enable_collaborative_inbox(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableCollaborativeInbox", []))

    @jsii.member(jsii_name="resetIncludeCustomFooter")
    def reset_include_custom_footer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeCustomFooter", []))

    @jsii.member(jsii_name="resetIncludeInGlobalAddressList")
    def reset_include_in_global_address_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeInGlobalAddressList", []))

    @jsii.member(jsii_name="resetIsArchived")
    def reset_is_archived(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsArchived", []))

    @jsii.member(jsii_name="resetMembersCanPostAsTheGroup")
    def reset_members_can_post_as_the_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembersCanPostAsTheGroup", []))

    @jsii.member(jsii_name="resetMessageModerationLevel")
    def reset_message_moderation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageModerationLevel", []))

    @jsii.member(jsii_name="resetPrimaryLanguage")
    def reset_primary_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryLanguage", []))

    @jsii.member(jsii_name="resetReplyTo")
    def reset_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyTo", []))

    @jsii.member(jsii_name="resetSendMessageDenyNotification")
    def reset_send_message_deny_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendMessageDenyNotification", []))

    @jsii.member(jsii_name="resetSpamModerationLevel")
    def reset_spam_moderation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpamModerationLevel", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWhoCanAssistContent")
    def reset_who_can_assist_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanAssistContent", []))

    @jsii.member(jsii_name="resetWhoCanContactOwner")
    def reset_who_can_contact_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanContactOwner", []))

    @jsii.member(jsii_name="resetWhoCanDiscoverGroup")
    def reset_who_can_discover_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanDiscoverGroup", []))

    @jsii.member(jsii_name="resetWhoCanJoin")
    def reset_who_can_join(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanJoin", []))

    @jsii.member(jsii_name="resetWhoCanLeaveGroup")
    def reset_who_can_leave_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanLeaveGroup", []))

    @jsii.member(jsii_name="resetWhoCanModerateContent")
    def reset_who_can_moderate_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanModerateContent", []))

    @jsii.member(jsii_name="resetWhoCanModerateMembers")
    def reset_who_can_moderate_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanModerateMembers", []))

    @jsii.member(jsii_name="resetWhoCanPostMessage")
    def reset_who_can_post_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanPostMessage", []))

    @jsii.member(jsii_name="resetWhoCanViewGroup")
    def reset_who_can_view_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanViewGroup", []))

    @jsii.member(jsii_name="resetWhoCanViewMembership")
    def reset_who_can_view_membership(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhoCanViewMembership", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customRolesEnabledForSettingsToBeMerged")
    def custom_roles_enabled_for_settings_to_be_merged(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "customRolesEnabledForSettingsToBeMerged"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GroupSettingsTimeoutsOutputReference":
        return typing.cast("GroupSettingsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowExternalMembersInput")
    def allow_external_members_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowExternalMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowWebPostingInput")
    def allow_web_posting_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowWebPostingInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveOnlyInput")
    def archive_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "archiveOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="customFooterTextInput")
    def custom_footer_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customFooterTextInput"))

    @builtins.property
    @jsii.member(jsii_name="customReplyToInput")
    def custom_reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customReplyToInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultMessageDenyNotificationTextInput")
    def default_message_deny_notification_text_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultMessageDenyNotificationTextInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCollaborativeInboxInput")
    def enable_collaborative_inbox_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableCollaborativeInboxInput"))

    @builtins.property
    @jsii.member(jsii_name="includeCustomFooterInput")
    def include_custom_footer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeCustomFooterInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInGlobalAddressListInput")
    def include_in_global_address_list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeInGlobalAddressListInput"))

    @builtins.property
    @jsii.member(jsii_name="isArchivedInput")
    def is_archived_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isArchivedInput"))

    @builtins.property
    @jsii.member(jsii_name="membersCanPostAsTheGroupInput")
    def members_can_post_as_the_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "membersCanPostAsTheGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="messageModerationLevelInput")
    def message_moderation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageModerationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryLanguageInput")
    def primary_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToInput")
    def reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToInput"))

    @builtins.property
    @jsii.member(jsii_name="sendMessageDenyNotificationInput")
    def send_message_deny_notification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sendMessageDenyNotificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spamModerationLevelInput")
    def spam_moderation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spamModerationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GroupSettingsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GroupSettingsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanAssistContentInput")
    def who_can_assist_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanAssistContentInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanContactOwnerInput")
    def who_can_contact_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanContactOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanDiscoverGroupInput")
    def who_can_discover_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanDiscoverGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanJoinInput")
    def who_can_join_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanJoinInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanLeaveGroupInput")
    def who_can_leave_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanLeaveGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateContentInput")
    def who_can_moderate_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanModerateContentInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateMembersInput")
    def who_can_moderate_members_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanModerateMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanPostMessageInput")
    def who_can_post_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanPostMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewGroupInput")
    def who_can_view_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanViewGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewMembershipInput")
    def who_can_view_membership_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whoCanViewMembershipInput"))

    @builtins.property
    @jsii.member(jsii_name="allowExternalMembers")
    def allow_external_members(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowExternalMembers"))

    @allow_external_members.setter
    def allow_external_members(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "allow_external_members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExternalMembers", value)

    @builtins.property
    @jsii.member(jsii_name="allowWebPosting")
    def allow_web_posting(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowWebPosting"))

    @allow_web_posting.setter
    def allow_web_posting(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "allow_web_posting").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowWebPosting", value)

    @builtins.property
    @jsii.member(jsii_name="archiveOnly")
    def archive_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "archiveOnly"))

    @archive_only.setter
    def archive_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "archive_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveOnly", value)

    @builtins.property
    @jsii.member(jsii_name="customFooterText")
    def custom_footer_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customFooterText"))

    @custom_footer_text.setter
    def custom_footer_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "custom_footer_text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customFooterText", value)

    @builtins.property
    @jsii.member(jsii_name="customReplyTo")
    def custom_reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customReplyTo"))

    @custom_reply_to.setter
    def custom_reply_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "custom_reply_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customReplyTo", value)

    @builtins.property
    @jsii.member(jsii_name="defaultMessageDenyNotificationText")
    def default_message_deny_notification_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultMessageDenyNotificationText"))

    @default_message_deny_notification_text.setter
    def default_message_deny_notification_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "default_message_deny_notification_text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultMessageDenyNotificationText", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="enableCollaborativeInbox")
    def enable_collaborative_inbox(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableCollaborativeInbox"))

    @enable_collaborative_inbox.setter
    def enable_collaborative_inbox(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "enable_collaborative_inbox").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCollaborativeInbox", value)

    @builtins.property
    @jsii.member(jsii_name="includeCustomFooter")
    def include_custom_footer(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeCustomFooter"))

    @include_custom_footer.setter
    def include_custom_footer(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "include_custom_footer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeCustomFooter", value)

    @builtins.property
    @jsii.member(jsii_name="includeInGlobalAddressList")
    def include_in_global_address_list(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeInGlobalAddressList"))

    @include_in_global_address_list.setter
    def include_in_global_address_list(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "include_in_global_address_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeInGlobalAddressList", value)

    @builtins.property
    @jsii.member(jsii_name="isArchived")
    def is_archived(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isArchived"))

    @is_archived.setter
    def is_archived(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "is_archived").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isArchived", value)

    @builtins.property
    @jsii.member(jsii_name="membersCanPostAsTheGroup")
    def members_can_post_as_the_group(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "membersCanPostAsTheGroup"))

    @members_can_post_as_the_group.setter
    def members_can_post_as_the_group(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "members_can_post_as_the_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membersCanPostAsTheGroup", value)

    @builtins.property
    @jsii.member(jsii_name="messageModerationLevel")
    def message_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageModerationLevel"))

    @message_moderation_level.setter
    def message_moderation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "message_moderation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageModerationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="primaryLanguage")
    def primary_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLanguage"))

    @primary_language.setter
    def primary_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "primary_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @reply_to.setter
    def reply_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "reply_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyTo", value)

    @builtins.property
    @jsii.member(jsii_name="sendMessageDenyNotification")
    def send_message_deny_notification(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sendMessageDenyNotification"))

    @send_message_deny_notification.setter
    def send_message_deny_notification(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "send_message_deny_notification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendMessageDenyNotification", value)

    @builtins.property
    @jsii.member(jsii_name="spamModerationLevel")
    def spam_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spamModerationLevel"))

    @spam_moderation_level.setter
    def spam_moderation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "spam_moderation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spamModerationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanAssistContent")
    def who_can_assist_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanAssistContent"))

    @who_can_assist_content.setter
    def who_can_assist_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_assist_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanAssistContent", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanContactOwner")
    def who_can_contact_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanContactOwner"))

    @who_can_contact_owner.setter
    def who_can_contact_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_contact_owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanContactOwner", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanDiscoverGroup")
    def who_can_discover_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanDiscoverGroup"))

    @who_can_discover_group.setter
    def who_can_discover_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_discover_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanDiscoverGroup", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanJoin")
    def who_can_join(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanJoin"))

    @who_can_join.setter
    def who_can_join(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_join").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanJoin", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanLeaveGroup")
    def who_can_leave_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanLeaveGroup"))

    @who_can_leave_group.setter
    def who_can_leave_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_leave_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanLeaveGroup", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateContent")
    def who_can_moderate_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateContent"))

    @who_can_moderate_content.setter
    def who_can_moderate_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_moderate_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanModerateContent", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateMembers")
    def who_can_moderate_members(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateMembers"))

    @who_can_moderate_members.setter
    def who_can_moderate_members(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_moderate_members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanModerateMembers", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanPostMessage")
    def who_can_post_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanPostMessage"))

    @who_can_post_message.setter
    def who_can_post_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_post_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanPostMessage", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanViewGroup")
    def who_can_view_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewGroup"))

    @who_can_view_group.setter
    def who_can_view_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_view_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanViewGroup", value)

    @builtins.property
    @jsii.member(jsii_name="whoCanViewMembership")
    def who_can_view_membership(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewMembership"))

    @who_can_view_membership.setter
    def who_can_view_membership(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettings, "who_can_view_membership").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whoCanViewMembership", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.groupSettings.GroupSettingsConfig",
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
        "allow_external_members": "allowExternalMembers",
        "allow_web_posting": "allowWebPosting",
        "archive_only": "archiveOnly",
        "custom_footer_text": "customFooterText",
        "custom_reply_to": "customReplyTo",
        "default_message_deny_notification_text": "defaultMessageDenyNotificationText",
        "enable_collaborative_inbox": "enableCollaborativeInbox",
        "include_custom_footer": "includeCustomFooter",
        "include_in_global_address_list": "includeInGlobalAddressList",
        "is_archived": "isArchived",
        "members_can_post_as_the_group": "membersCanPostAsTheGroup",
        "message_moderation_level": "messageModerationLevel",
        "primary_language": "primaryLanguage",
        "reply_to": "replyTo",
        "send_message_deny_notification": "sendMessageDenyNotification",
        "spam_moderation_level": "spamModerationLevel",
        "timeouts": "timeouts",
        "who_can_assist_content": "whoCanAssistContent",
        "who_can_contact_owner": "whoCanContactOwner",
        "who_can_discover_group": "whoCanDiscoverGroup",
        "who_can_join": "whoCanJoin",
        "who_can_leave_group": "whoCanLeaveGroup",
        "who_can_moderate_content": "whoCanModerateContent",
        "who_can_moderate_members": "whoCanModerateMembers",
        "who_can_post_message": "whoCanPostMessage",
        "who_can_view_group": "whoCanViewGroup",
        "who_can_view_membership": "whoCanViewMembership",
    },
)
class GroupSettingsConfig(cdktf.TerraformMetaArguments):
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
        allow_external_members: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_web_posting: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_footer_text: typing.Optional[builtins.str] = None,
        custom_reply_to: typing.Optional[builtins.str] = None,
        default_message_deny_notification_text: typing.Optional[builtins.str] = None,
        enable_collaborative_inbox: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_custom_footer: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_in_global_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        members_can_post_as_the_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_moderation_level: typing.Optional[builtins.str] = None,
        primary_language: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        send_message_deny_notification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spam_moderation_level: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GroupSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
        who_can_assist_content: typing.Optional[builtins.str] = None,
        who_can_contact_owner: typing.Optional[builtins.str] = None,
        who_can_discover_group: typing.Optional[builtins.str] = None,
        who_can_join: typing.Optional[builtins.str] = None,
        who_can_leave_group: typing.Optional[builtins.str] = None,
        who_can_moderate_content: typing.Optional[builtins.str] = None,
        who_can_moderate_members: typing.Optional[builtins.str] = None,
        who_can_post_message: typing.Optional[builtins.str] = None,
        who_can_view_group: typing.Optional[builtins.str] = None,
        who_can_view_membership: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#email GroupSettings#email}
        :param allow_external_members: Defaults to ``false``. Identifies whether members external to your organization can join the group. If true, Google Workspace users external to your organization can become members of this group. If false, users not belonging to the organization are not allowed to become members of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_external_members GroupSettings#allow_external_members}
        :param allow_web_posting: Defaults to ``true``. Allows posting from web. If true, allows any member to post to the group forum. If false, Members only use Gmail to communicate with the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_web_posting GroupSettings#allow_web_posting}
        :param archive_only: Defaults to ``false``. Allows the group to be archived only. If true, Group is archived and the group is inactive. New messages to this group are rejected. The older archived messages are browsable and searchable. If true, the ``who_can_post_message`` property is set to ``NONE_CAN_POST``. If reverted from true to false, ``who_can_post_message`` is set to ``ALL_MANAGERS_CAN_POST``. If false, The group is active and can receive messages. When false, updating ``who_can_post_message`` to ``NONE_CAN_POST``, results in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#archive_only GroupSettings#archive_only}
        :param custom_footer_text: Set the content of custom footer text. The maximum number of characters is 1,000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_footer_text GroupSettings#custom_footer_text}
        :param custom_reply_to: An email address used when replying to a message if the ``reply_to`` property is set to ``REPLY_TO_CUSTOM``. This address is defined by an account administrator. When the group's ``reply_to`` property is set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds a custom email address used when replying to a message, the ``custom_reply_to`` property must have a text value or an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_reply_to GroupSettings#custom_reply_to}
        :param default_message_deny_notification_text: When a message is rejected, this is text for the rejection notification sent to the message's author. By default, this property is empty and has no value in the API's response body. The maximum notification text size is 10,000 characters. Requires ``send_message_deny_notification`` property to be true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#default_message_deny_notification_text GroupSettings#default_message_deny_notification_text}
        :param enable_collaborative_inbox: Defaults to ``false``. Specifies whether a collaborative inbox will remain turned on for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#enable_collaborative_inbox GroupSettings#enable_collaborative_inbox}
        :param include_custom_footer: Defaults to ``false``. Whether to include custom footer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_custom_footer GroupSettings#include_custom_footer}
        :param include_in_global_address_list: Defaults to ``true``. Enables the group to be included in the Global Address List. If true, the group is included in the Global Address List. If false, it is not included in the Global Address List. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_in_global_address_list GroupSettings#include_in_global_address_list}
        :param is_archived: Defaults to ``false``. Allows the Group contents to be archived. If true, archive messages sent to the group. If false, Do not keep an archive of messages sent to this group. If false, previously archived messages remain in the archive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#is_archived GroupSettings#is_archived}
        :param members_can_post_as_the_group: Defaults to ``false``. Enables members to post messages as the group. If true, group member can post messages using the group's email address instead of their own email address. Message appear to originate from the group itself. Any message moderation settings on individual users or new members do not apply to posts made on behalf of the group. If false, members can not post in behalf of the group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#members_can_post_as_the_group GroupSettings#members_can_post_as_the_group}
        :param message_moderation_level: Defaults to ``MODERATE_NONE``. Moderation level of incoming messages. Possible values are: - ``MODERATE_ALL_MESSAGES``: All messages are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NON_MEMBERS``: All messages from non group members are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NEW_MEMBERS``: All messages from new members are sent to the group owner's email address for approval. If approved, the message is sent to the group. - ``MODERATE_NONE``: No moderator approval is required. Messages are delivered directly to the group. Note: When the ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the ``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam.When ``member_can_post_as_the_group`` is true, any message moderation settings on individual users or new members will not apply to posts made on behalf of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#message_moderation_level GroupSettings#message_moderation_level}
        :param primary_language: The primary language for group. For a group's primary language use the language tags from the Google Workspace languages found at Google Workspace Email Settings API Email Language Tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#primary_language GroupSettings#primary_language}
        :param reply_to: Defaults to ``REPLY_TO_IGNORE``. Specifies who receives the default reply. Possible values are: - ``REPLY_TO_CUSTOM``: For replies to messages, use the group's custom email address. When set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds the custom email address used when replying to a message, the customReplyTo property must have a value. Otherwise an error is returned. - ``REPLY_TO_SENDER``: The reply sent to author of message. - ``REPLY_TO_LIST``: This reply message is sent to the group. - ``REPLY_TO_OWNER``: The reply is sent to the owner(s) of the group. This does not include the group's managers. - ``REPLY_TO_IGNORE``: Group users individually decide where the message reply is sent. - ``REPLY_TO_MANAGERS``: This reply message is sent to the group's managers, which includes all managers and the group owner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#reply_to GroupSettings#reply_to}
        :param send_message_deny_notification: Defaults to ``false``. Allows a member to be notified if the member's message to the group is denied by the group owner. If true, when a message is rejected, send the deny message notification to the message author. The ``default_message_deny_notification_text`` property is dependent on the ``send_message_deny_notification`` property being true. If false, when a message is rejected, no notification is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#send_message_deny_notification GroupSettings#send_message_deny_notification}
        :param spam_moderation_level: Defaults to ``MODERATE``. Specifies moderation levels for messages detected as spam. Possible values are: - ``ALLOW``: Post the message to the group. - ``MODERATE``: Send the message to the moderation queue. This is the default. - ``SILENTLY_MODERATE``: Send the message to the moderation queue, but do not send notification to moderators. - ``REJECT``: Immediately reject the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#spam_moderation_level GroupSettings#spam_moderation_level}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#timeouts GroupSettings#timeouts}
        :param who_can_assist_content: Defaults to ``NONE``. Specifies who can moderate metadata. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``MANAGERS_ONLY`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_assist_content GroupSettings#who_can_assist_content}
        :param who_can_contact_owner: Defaults to ``ANYONE_CAN_CONTACT``. Permission to contact owner of the group via web UI. Possible values are: - ``ALL_IN_DOMAIN_CAN_CONTACT`` - ``ALL_MANAGERS_CAN_CONTACT`` - ``ALL_MEMBERS_CAN_CONTACT`` - ``ANYONE_CAN_CONTACT`` - ``ALL_OWNERS_CAN_CONTACT`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_contact_owner GroupSettings#who_can_contact_owner}
        :param who_can_discover_group: Defaults to ``ALL_IN_DOMAIN_CAN_DISCOVER``. Specifies the set of users for whom this group is discoverable. Possible values are: - ``ANYONE_CAN_DISCOVER`` - ``ALL_IN_DOMAIN_CAN_DISCOVER`` - ``ALL_MEMBERS_CAN_DISCOVER`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_discover_group GroupSettings#who_can_discover_group}
        :param who_can_join: Defaults to ``CAN_REQUEST_TO_JOIN``. Permission to join group. Possible values are: - ``ANYONE_CAN_JOIN``: Any Internet user, both inside and outside your domain, can join the group. - ``ALL_IN_DOMAIN_CAN_JOIN``: Anyone in the account domain can join. This includes accounts with multiple domains. - ``INVITED_CAN_JOIN``: Candidates for membership can be invited to join. - ``CAN_REQUEST_TO_JOIN``: Non members can request an invitation to join. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_join GroupSettings#who_can_join}
        :param who_can_leave_group: Defaults to ``ALL_MEMBERS_CAN_LEAVE``. Permission to leave the group. Possible values are: - ``ALL_MANAGERS_CAN_LEAVE`` - ``ALL_MEMBERS_CAN_LEAVE`` - ``NONE_CAN_LEAVE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_leave_group GroupSettings#who_can_leave_group}
        :param who_can_moderate_content: Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can moderate content. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_content GroupSettings#who_can_moderate_content}
        :param who_can_moderate_members: Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can manage members. Possible values are: - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_members GroupSettings#who_can_moderate_members}
        :param who_can_post_message: Permissions to post messages. Possible values are: - ``NONE_CAN_POST``: The group is disabled and archived. No one can post a message to this group. * When archiveOnly is false, updating whoCanPostMessage to NONE_CAN_POST, results in an error. * If archiveOnly is reverted from true to false, whoCanPostMessages is set to ALL_MANAGERS_CAN_POST. - ``ALL_MANAGERS_CAN_POST``: Managers, including group owners, can post messages. - ``ALL_MEMBERS_CAN_POST``: Any group member can post a message. - ``ALL_OWNERS_CAN_POST``: Only group owners can post a message. - ``ALL_IN_DOMAIN_CAN_POST``: Anyone in the account can post a message. - ``ANYONE_CAN_POST``: Any Internet user who outside your account can access your Google Groups service and post a message. Note: When ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam. Users not belonging to the organization are not allowed to become members of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_post_message GroupSettings#who_can_post_message}
        :param who_can_view_group: Defaults to ``ALL_MEMBERS_CAN_VIEW``. Permissions to view group messages. Possible values are: - ``ANYONE_CAN_VIEW``: Any Internet user can view the group's messages. - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in your account can view this group's messages. - ``ALL_MEMBERS_CAN_VIEW``: All group members can view the group's messages. - ``ALL_MANAGERS_CAN_VIEW``: Any group manager can view this group's messages. - ``ALL_OWNERS_CAN_VIEW``: The group owners can view this group's messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_group GroupSettings#who_can_view_group}
        :param who_can_view_membership: Defaults to ``ALL_MEMBERS_CAN_VIEW``. Permissions to view membership. Possible values are: - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in the account can view the group members list. If a group already has external members, those members can still send email to this group. - ``ALL_MEMBERS_CAN_VIEW``: The group members can view the group members list. - ``ALL_MANAGERS_CAN_VIEW``: The group managers can view group members list. - ``ALL_OWNERS_CAN_VIEW``: The group owners can view group members list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_membership GroupSettings#who_can_view_membership}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GroupSettingsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GroupSettingsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument allow_external_members", value=allow_external_members, expected_type=type_hints["allow_external_members"])
            check_type(argname="argument allow_web_posting", value=allow_web_posting, expected_type=type_hints["allow_web_posting"])
            check_type(argname="argument archive_only", value=archive_only, expected_type=type_hints["archive_only"])
            check_type(argname="argument custom_footer_text", value=custom_footer_text, expected_type=type_hints["custom_footer_text"])
            check_type(argname="argument custom_reply_to", value=custom_reply_to, expected_type=type_hints["custom_reply_to"])
            check_type(argname="argument default_message_deny_notification_text", value=default_message_deny_notification_text, expected_type=type_hints["default_message_deny_notification_text"])
            check_type(argname="argument enable_collaborative_inbox", value=enable_collaborative_inbox, expected_type=type_hints["enable_collaborative_inbox"])
            check_type(argname="argument include_custom_footer", value=include_custom_footer, expected_type=type_hints["include_custom_footer"])
            check_type(argname="argument include_in_global_address_list", value=include_in_global_address_list, expected_type=type_hints["include_in_global_address_list"])
            check_type(argname="argument is_archived", value=is_archived, expected_type=type_hints["is_archived"])
            check_type(argname="argument members_can_post_as_the_group", value=members_can_post_as_the_group, expected_type=type_hints["members_can_post_as_the_group"])
            check_type(argname="argument message_moderation_level", value=message_moderation_level, expected_type=type_hints["message_moderation_level"])
            check_type(argname="argument primary_language", value=primary_language, expected_type=type_hints["primary_language"])
            check_type(argname="argument reply_to", value=reply_to, expected_type=type_hints["reply_to"])
            check_type(argname="argument send_message_deny_notification", value=send_message_deny_notification, expected_type=type_hints["send_message_deny_notification"])
            check_type(argname="argument spam_moderation_level", value=spam_moderation_level, expected_type=type_hints["spam_moderation_level"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument who_can_assist_content", value=who_can_assist_content, expected_type=type_hints["who_can_assist_content"])
            check_type(argname="argument who_can_contact_owner", value=who_can_contact_owner, expected_type=type_hints["who_can_contact_owner"])
            check_type(argname="argument who_can_discover_group", value=who_can_discover_group, expected_type=type_hints["who_can_discover_group"])
            check_type(argname="argument who_can_join", value=who_can_join, expected_type=type_hints["who_can_join"])
            check_type(argname="argument who_can_leave_group", value=who_can_leave_group, expected_type=type_hints["who_can_leave_group"])
            check_type(argname="argument who_can_moderate_content", value=who_can_moderate_content, expected_type=type_hints["who_can_moderate_content"])
            check_type(argname="argument who_can_moderate_members", value=who_can_moderate_members, expected_type=type_hints["who_can_moderate_members"])
            check_type(argname="argument who_can_post_message", value=who_can_post_message, expected_type=type_hints["who_can_post_message"])
            check_type(argname="argument who_can_view_group", value=who_can_view_group, expected_type=type_hints["who_can_view_group"])
            check_type(argname="argument who_can_view_membership", value=who_can_view_membership, expected_type=type_hints["who_can_view_membership"])
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
        if allow_external_members is not None:
            self._values["allow_external_members"] = allow_external_members
        if allow_web_posting is not None:
            self._values["allow_web_posting"] = allow_web_posting
        if archive_only is not None:
            self._values["archive_only"] = archive_only
        if custom_footer_text is not None:
            self._values["custom_footer_text"] = custom_footer_text
        if custom_reply_to is not None:
            self._values["custom_reply_to"] = custom_reply_to
        if default_message_deny_notification_text is not None:
            self._values["default_message_deny_notification_text"] = default_message_deny_notification_text
        if enable_collaborative_inbox is not None:
            self._values["enable_collaborative_inbox"] = enable_collaborative_inbox
        if include_custom_footer is not None:
            self._values["include_custom_footer"] = include_custom_footer
        if include_in_global_address_list is not None:
            self._values["include_in_global_address_list"] = include_in_global_address_list
        if is_archived is not None:
            self._values["is_archived"] = is_archived
        if members_can_post_as_the_group is not None:
            self._values["members_can_post_as_the_group"] = members_can_post_as_the_group
        if message_moderation_level is not None:
            self._values["message_moderation_level"] = message_moderation_level
        if primary_language is not None:
            self._values["primary_language"] = primary_language
        if reply_to is not None:
            self._values["reply_to"] = reply_to
        if send_message_deny_notification is not None:
            self._values["send_message_deny_notification"] = send_message_deny_notification
        if spam_moderation_level is not None:
            self._values["spam_moderation_level"] = spam_moderation_level
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if who_can_assist_content is not None:
            self._values["who_can_assist_content"] = who_can_assist_content
        if who_can_contact_owner is not None:
            self._values["who_can_contact_owner"] = who_can_contact_owner
        if who_can_discover_group is not None:
            self._values["who_can_discover_group"] = who_can_discover_group
        if who_can_join is not None:
            self._values["who_can_join"] = who_can_join
        if who_can_leave_group is not None:
            self._values["who_can_leave_group"] = who_can_leave_group
        if who_can_moderate_content is not None:
            self._values["who_can_moderate_content"] = who_can_moderate_content
        if who_can_moderate_members is not None:
            self._values["who_can_moderate_members"] = who_can_moderate_members
        if who_can_post_message is not None:
            self._values["who_can_post_message"] = who_can_post_message
        if who_can_view_group is not None:
            self._values["who_can_view_group"] = who_can_view_group
        if who_can_view_membership is not None:
            self._values["who_can_view_membership"] = who_can_view_membership

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#email GroupSettings#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_external_members(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Identifies whether members external to your organization can join the group. If true, Google Workspace users external to your organization can become members of this group. If false, users not belonging to the organization are not allowed to become members of this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_external_members GroupSettings#allow_external_members}
        '''
        result = self._values.get("allow_external_members")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_web_posting(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Allows posting from web. If true, allows any member to post to the group forum. If false, Members only use Gmail to communicate with the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#allow_web_posting GroupSettings#allow_web_posting}
        '''
        result = self._values.get("allow_web_posting")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def archive_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Allows the group to be archived only. If true, Group is archived and the group is inactive. New messages to this group are rejected. The older archived messages are browsable and searchable. If true, the ``who_can_post_message`` property is set to ``NONE_CAN_POST``. If reverted from true to false, ``who_can_post_message`` is set to ``ALL_MANAGERS_CAN_POST``. If false, The group is active and can receive messages. When false, updating ``who_can_post_message`` to ``NONE_CAN_POST``, results in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#archive_only GroupSettings#archive_only}
        '''
        result = self._values.get("archive_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_footer_text(self) -> typing.Optional[builtins.str]:
        '''Set the content of custom footer text. The maximum number of characters is 1,000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_footer_text GroupSettings#custom_footer_text}
        '''
        result = self._values.get("custom_footer_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_reply_to(self) -> typing.Optional[builtins.str]:
        '''An email address used when replying to a message if the ``reply_to`` property is set to ``REPLY_TO_CUSTOM``.

        This address is defined by an account administrator. When the group's ``reply_to`` property is set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds a custom email address used when replying to a message, the ``custom_reply_to`` property must have a text value or an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#custom_reply_to GroupSettings#custom_reply_to}
        '''
        result = self._values.get("custom_reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_message_deny_notification_text(self) -> typing.Optional[builtins.str]:
        '''When a message is rejected, this is text for the rejection notification sent to the message's author.

        By default, this property is empty and has no value in the API's response body. The maximum notification text size is 10,000 characters. Requires ``send_message_deny_notification`` property to be true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#default_message_deny_notification_text GroupSettings#default_message_deny_notification_text}
        '''
        result = self._values.get("default_message_deny_notification_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_collaborative_inbox(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``. Specifies whether a collaborative inbox will remain turned on for the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#enable_collaborative_inbox GroupSettings#enable_collaborative_inbox}
        '''
        result = self._values.get("enable_collaborative_inbox")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_custom_footer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``. Whether to include custom footer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_custom_footer GroupSettings#include_custom_footer}
        '''
        result = self._values.get("include_custom_footer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_in_global_address_list(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Enables the group to be included in the Global Address List. If true, the group is included in the Global Address List. If false, it is not included in the Global Address List.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#include_in_global_address_list GroupSettings#include_in_global_address_list}
        '''
        result = self._values.get("include_in_global_address_list")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_archived(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Allows the Group contents to be archived. If true, archive messages sent to the group. If false, Do not keep an archive of messages sent to this group. If false, previously archived messages remain in the archive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#is_archived GroupSettings#is_archived}
        '''
        result = self._values.get("is_archived")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def members_can_post_as_the_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Enables members to post messages as the group. If true, group member can post messages using the group's email address instead of their own email address. Message appear to originate from the group itself. Any message moderation settings on individual users or new members do not apply to posts made on behalf of the group. If false, members can not post in behalf of the group's email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#members_can_post_as_the_group GroupSettings#members_can_post_as_the_group}
        '''
        result = self._values.get("members_can_post_as_the_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def message_moderation_level(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``MODERATE_NONE``.

        Moderation level of incoming messages. Possible values are:

        - ``MODERATE_ALL_MESSAGES``: All messages are sent to the group owner's email address for approval. If approved, the message is sent to the group.
        - ``MODERATE_NON_MEMBERS``: All messages from non group members are sent to the group owner's email address for approval. If approved, the message is sent to the group.
        - ``MODERATE_NEW_MEMBERS``: All messages from new members are sent to the group owner's email address for approval. If approved, the message is sent to the group.
        - ``MODERATE_NONE``: No moderator approval is required. Messages are delivered directly to the group.
          Note: When the ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the ``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam.When ``member_can_post_as_the_group`` is true, any message moderation settings on individual users or new members will not apply to posts made on behalf of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#message_moderation_level GroupSettings#message_moderation_level}
        '''
        result = self._values.get("message_moderation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_language(self) -> typing.Optional[builtins.str]:
        '''The primary language for group.

        For a group's primary language use the language tags from the Google Workspace languages found at Google Workspace Email Settings API Email Language Tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#primary_language GroupSettings#primary_language}
        '''
        result = self._values.get("primary_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reply_to(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``REPLY_TO_IGNORE``.

        Specifies who receives the default reply. Possible values are:

        - ``REPLY_TO_CUSTOM``: For replies to messages, use the group's custom email address. When set to ``REPLY_TO_CUSTOM``, the ``custom_reply_to`` property holds the custom email address used when replying to a message, the customReplyTo property must have a value. Otherwise an error is returned.
        - ``REPLY_TO_SENDER``: The reply sent to author of message.
        - ``REPLY_TO_LIST``: This reply message is sent to the group.
        - ``REPLY_TO_OWNER``: The reply is sent to the owner(s) of the group. This does not include the group's managers.
        - ``REPLY_TO_IGNORE``: Group users individually decide where the message reply is sent.
        - ``REPLY_TO_MANAGERS``: This reply message is sent to the group's managers, which includes all managers and the group owner.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#reply_to GroupSettings#reply_to}
        '''
        result = self._values.get("reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def send_message_deny_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Allows a member to be notified if the member's message to the group is denied by the group owner. If true, when a message is rejected, send the deny message notification to the message author. The ``default_message_deny_notification_text`` property is dependent on the ``send_message_deny_notification`` property being true. If false, when a message is rejected, no notification is sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#send_message_deny_notification GroupSettings#send_message_deny_notification}
        '''
        result = self._values.get("send_message_deny_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def spam_moderation_level(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``MODERATE``.

        Specifies moderation levels for messages detected as spam. Possible values are:

        - ``ALLOW``: Post the message to the group.
        - ``MODERATE``: Send the message to the moderation queue. This is the default.
        - ``SILENTLY_MODERATE``: Send the message to the moderation queue, but do not send notification to moderators.
        - ``REJECT``: Immediately reject the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#spam_moderation_level GroupSettings#spam_moderation_level}
        '''
        result = self._values.get("spam_moderation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GroupSettingsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#timeouts GroupSettings#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GroupSettingsTimeouts"], result)

    @builtins.property
    def who_can_assist_content(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``NONE``. Specifies who can moderate metadata. Possible values are:  - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``MANAGERS_ONLY`` - ``OWNERS_ONLY`` - ``NONE``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_assist_content GroupSettings#who_can_assist_content}
        '''
        result = self._values.get("who_can_assist_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_contact_owner(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ANYONE_CAN_CONTACT``.

        Permission to contact owner of the group via web UI. Possible values are:

        - ``ALL_IN_DOMAIN_CAN_CONTACT``
        - ``ALL_MANAGERS_CAN_CONTACT``
        - ``ALL_MEMBERS_CAN_CONTACT``
        - ``ANYONE_CAN_CONTACT``
        - ``ALL_OWNERS_CAN_CONTACT``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_contact_owner GroupSettings#who_can_contact_owner}
        '''
        result = self._values.get("who_can_contact_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_discover_group(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_IN_DOMAIN_CAN_DISCOVER``.

        Specifies the set of users for whom this group is discoverable. Possible values are:

        - ``ANYONE_CAN_DISCOVER``
        - ``ALL_IN_DOMAIN_CAN_DISCOVER``
        - ``ALL_MEMBERS_CAN_DISCOVER``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_discover_group GroupSettings#who_can_discover_group}
        '''
        result = self._values.get("who_can_discover_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_join(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``CAN_REQUEST_TO_JOIN``.

        Permission to join group. Possible values are:

        - ``ANYONE_CAN_JOIN``: Any Internet user, both inside and outside your domain, can join the group.
        - ``ALL_IN_DOMAIN_CAN_JOIN``: Anyone in the account domain can join. This includes accounts with multiple domains.
        - ``INVITED_CAN_JOIN``: Candidates for membership can be invited to join.
        - ``CAN_REQUEST_TO_JOIN``: Non members can request an invitation to join.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_join GroupSettings#who_can_join}
        '''
        result = self._values.get("who_can_join")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_leave_group(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_MEMBERS_CAN_LEAVE``. Permission to leave the group. Possible values are: - ``ALL_MANAGERS_CAN_LEAVE`` - ``ALL_MEMBERS_CAN_LEAVE`` - ``NONE_CAN_LEAVE``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_leave_group GroupSettings#who_can_leave_group}
        '''
        result = self._values.get("who_can_leave_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_moderate_content(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can moderate content. Possible values are:  - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_content GroupSettings#who_can_moderate_content}
        '''
        result = self._values.get("who_can_moderate_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_moderate_members(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``OWNERS_AND_MANAGERS``. Specifies who can manage members. Possible values are:  - ``ALL_MEMBERS`` - ``OWNERS_AND_MANAGERS`` - ``OWNERS_ONLY`` - ``NONE``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_moderate_members GroupSettings#who_can_moderate_members}
        '''
        result = self._values.get("who_can_moderate_members")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_post_message(self) -> typing.Optional[builtins.str]:
        '''Permissions to post messages.

        Possible values are:

        - ``NONE_CAN_POST``: The group is disabled and archived. No one can post a message to this group. * When archiveOnly is false, updating whoCanPostMessage to NONE_CAN_POST, results in an error. * If archiveOnly is reverted from true to false, whoCanPostMessages is set to ALL_MANAGERS_CAN_POST.
        - ``ALL_MANAGERS_CAN_POST``: Managers, including group owners, can post messages.
        - ``ALL_MEMBERS_CAN_POST``: Any group member can post a message.
        - ``ALL_OWNERS_CAN_POST``: Only group owners can post a message.
        - ``ALL_IN_DOMAIN_CAN_POST``: Anyone in the account can post a message.
        - ``ANYONE_CAN_POST``: Any Internet user who outside your account can access your Google Groups service and post a message.
          Note: When ``who_can_post_message`` is set to ``ANYONE_CAN_POST``, we recommend the``message_moderation_level`` be set to ``MODERATE_NON_MEMBERS`` to protect the group from possible spam. Users not belonging to the organization are not allowed to become members of this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_post_message GroupSettings#who_can_post_message}
        '''
        result = self._values.get("who_can_post_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_view_group(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_MEMBERS_CAN_VIEW``.

        Permissions to view group messages. Possible values are:

        - ``ANYONE_CAN_VIEW``: Any Internet user can view the group's messages.
        - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in your account can view this group's messages.
        - ``ALL_MEMBERS_CAN_VIEW``: All group members can view the group's messages.
        - ``ALL_MANAGERS_CAN_VIEW``: Any group manager can view this group's messages.
        - ``ALL_OWNERS_CAN_VIEW``: The group owners can view this group's messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_group GroupSettings#who_can_view_group}
        '''
        result = self._values.get("who_can_view_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def who_can_view_membership(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_MEMBERS_CAN_VIEW``.

        Permissions to view membership. Possible values are:

        - ``ALL_IN_DOMAIN_CAN_VIEW``: Anyone in the account can view the group members list. If a group already has external members, those members can still send email to this group.
        - ``ALL_MEMBERS_CAN_VIEW``: The group members can view the group members list.
        - ``ALL_MANAGERS_CAN_VIEW``: The group managers can view group members list.
        - ``ALL_OWNERS_CAN_VIEW``: The group owners can view group members list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#who_can_view_membership GroupSettings#who_can_view_membership}
        '''
        result = self._values.get("who_can_view_membership")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.groupSettings.GroupSettingsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class GroupSettingsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#create GroupSettings#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#update GroupSettings#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSettingsTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#create GroupSettings#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_settings#update GroupSettings#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSettingsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupSettingsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.groupSettings.GroupSettingsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GroupSettingsTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(getattr(GroupSettingsTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettingsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupSettingsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupSettingsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupSettingsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSettingsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GroupSettings",
    "GroupSettingsConfig",
    "GroupSettingsTimeouts",
    "GroupSettingsTimeoutsOutputReference",
]

publication.publish()
