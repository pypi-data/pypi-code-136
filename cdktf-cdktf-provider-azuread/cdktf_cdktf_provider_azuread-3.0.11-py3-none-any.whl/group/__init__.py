'''
# `azuread_group`

Refer to the Terraform Registory for docs: [`azuread_group`](https://www.terraform.io/docs/providers/azuread/r/group).
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


class Group(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.group.Group",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/group azuread_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        assignable_to_role: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_subscribe_new_members: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        behaviors: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamic_membership: typing.Optional[typing.Union["GroupDynamicMembership", typing.Dict[str, typing.Any]]] = None,
        external_senders_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide_from_address_lists: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide_from_outlook_clients: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mail_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        theme: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        types: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/group azuread_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The display name for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#display_name Group#display_name}
        :param assignable_to_role: Indicates whether this group can be assigned to an Azure Active Directory role. This property can only be ``true`` for security-enabled groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#assignable_to_role Group#assignable_to_role}
        :param auto_subscribe_new_members: Indicates whether new members added to the group will be auto-subscribed to receive email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#auto_subscribe_new_members Group#auto_subscribe_new_members}
        :param behaviors: The group behaviours for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#behaviors Group#behaviors}
        :param description: The description for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#description Group#description}
        :param dynamic_membership: dynamic_membership block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#dynamic_membership Group#dynamic_membership}
        :param external_senders_allowed: Indicates whether people external to the organization can send messages to the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#external_senders_allowed Group#external_senders_allowed}
        :param hide_from_address_lists: Indicates whether the group is displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_address_lists Group#hide_from_address_lists}
        :param hide_from_outlook_clients: Indicates whether the group is displayed in Outlook clients, such as Outlook for Windows and Outlook on the web. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_outlook_clients Group#hide_from_outlook_clients}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#id Group#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mail_enabled: Whether the group is a mail enabled, with a shared group mailbox. At least one of ``mail_enabled`` or ``security_enabled`` must be specified. A group can be mail enabled *and* security enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_enabled Group#mail_enabled}
        :param mail_nickname: The mail alias for the group, unique in the organisation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_nickname Group#mail_nickname}
        :param members: A set of members who should be present in this group. Supported object types are Users, Groups or Service Principals Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#members Group#members}
        :param owners: A set of owners who own this group. Supported object types are Users or Service Principals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#owners Group#owners}
        :param prevent_duplicate_names: If ``true``, will return an error if an existing group is found with the same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#prevent_duplicate_names Group#prevent_duplicate_names}
        :param provisioning_options: The group provisioning options for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#provisioning_options Group#provisioning_options}
        :param security_enabled: Whether the group is a security group for controlling access to in-app resources. At least one of ``security_enabled`` or ``mail_enabled`` must be specified. A group can be security enabled *and* mail enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#security_enabled Group#security_enabled}
        :param theme: The colour theme for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#theme Group#theme}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#timeouts Group#timeouts}
        :param types: A set of group types to configure for the group. ``Unified`` specifies a Microsoft 365 group. Required when ``mail_enabled`` is true Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#types Group#types}
        :param visibility: Specifies the group join policy and group content visibility. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#visibility Group#visibility}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Group.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupConfig(
            display_name=display_name,
            assignable_to_role=assignable_to_role,
            auto_subscribe_new_members=auto_subscribe_new_members,
            behaviors=behaviors,
            description=description,
            dynamic_membership=dynamic_membership,
            external_senders_allowed=external_senders_allowed,
            hide_from_address_lists=hide_from_address_lists,
            hide_from_outlook_clients=hide_from_outlook_clients,
            id=id,
            mail_enabled=mail_enabled,
            mail_nickname=mail_nickname,
            members=members,
            owners=owners,
            prevent_duplicate_names=prevent_duplicate_names,
            provisioning_options=provisioning_options,
            security_enabled=security_enabled,
            theme=theme,
            timeouts=timeouts,
            types=types,
            visibility=visibility,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDynamicMembership")
    def put_dynamic_membership(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        rule: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#enabled Group#enabled}.
        :param rule: Rule to determine members for a dynamic group. Required when ``group_types`` contains 'DynamicMembership'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#rule Group#rule}
        '''
        value = GroupDynamicMembership(enabled=enabled, rule=rule)

        return typing.cast(None, jsii.invoke(self, "putDynamicMembership", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#create Group#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#delete Group#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#read Group#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#update Group#update}.
        '''
        value = GroupTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAssignableToRole")
    def reset_assignable_to_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignableToRole", []))

    @jsii.member(jsii_name="resetAutoSubscribeNewMembers")
    def reset_auto_subscribe_new_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSubscribeNewMembers", []))

    @jsii.member(jsii_name="resetBehaviors")
    def reset_behaviors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBehaviors", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamicMembership")
    def reset_dynamic_membership(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicMembership", []))

    @jsii.member(jsii_name="resetExternalSendersAllowed")
    def reset_external_senders_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalSendersAllowed", []))

    @jsii.member(jsii_name="resetHideFromAddressLists")
    def reset_hide_from_address_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHideFromAddressLists", []))

    @jsii.member(jsii_name="resetHideFromOutlookClients")
    def reset_hide_from_outlook_clients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHideFromOutlookClients", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMailEnabled")
    def reset_mail_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMailEnabled", []))

    @jsii.member(jsii_name="resetMailNickname")
    def reset_mail_nickname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMailNickname", []))

    @jsii.member(jsii_name="resetMembers")
    def reset_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembers", []))

    @jsii.member(jsii_name="resetOwners")
    def reset_owners(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwners", []))

    @jsii.member(jsii_name="resetPreventDuplicateNames")
    def reset_prevent_duplicate_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreventDuplicateNames", []))

    @jsii.member(jsii_name="resetProvisioningOptions")
    def reset_provisioning_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisioningOptions", []))

    @jsii.member(jsii_name="resetSecurityEnabled")
    def reset_security_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityEnabled", []))

    @jsii.member(jsii_name="resetTheme")
    def reset_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTheme", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTypes")
    def reset_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypes", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dynamicMembership")
    def dynamic_membership(self) -> "GroupDynamicMembershipOutputReference":
        return typing.cast("GroupDynamicMembershipOutputReference", jsii.get(self, "dynamicMembership"))

    @builtins.property
    @jsii.member(jsii_name="mail")
    def mail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mail"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesDomainName")
    def onpremises_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesDomainName"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesNetbiosName")
    def onpremises_netbios_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesNetbiosName"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesSamAccountName")
    def onpremises_sam_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesSamAccountName"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesSecurityIdentifier")
    def onpremises_security_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesSecurityIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesSyncEnabled")
    def onpremises_sync_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "onpremisesSyncEnabled"))

    @builtins.property
    @jsii.member(jsii_name="preferredLanguage")
    def preferred_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredLanguage"))

    @builtins.property
    @jsii.member(jsii_name="proxyAddresses")
    def proxy_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "proxyAddresses"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GroupTimeoutsOutputReference":
        return typing.cast("GroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="assignableToRoleInput")
    def assignable_to_role_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assignableToRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSubscribeNewMembersInput")
    def auto_subscribe_new_members_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoSubscribeNewMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="behaviorsInput")
    def behaviors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "behaviorsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicMembershipInput")
    def dynamic_membership_input(self) -> typing.Optional["GroupDynamicMembership"]:
        return typing.cast(typing.Optional["GroupDynamicMembership"], jsii.get(self, "dynamicMembershipInput"))

    @builtins.property
    @jsii.member(jsii_name="externalSendersAllowedInput")
    def external_senders_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "externalSendersAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="hideFromAddressListsInput")
    def hide_from_address_lists_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hideFromAddressListsInput"))

    @builtins.property
    @jsii.member(jsii_name="hideFromOutlookClientsInput")
    def hide_from_outlook_clients_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hideFromOutlookClientsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mailEnabledInput")
    def mail_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mailEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mailNicknameInput")
    def mail_nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mailNicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="ownersInput")
    def owners_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ownersInput"))

    @builtins.property
    @jsii.member(jsii_name="preventDuplicateNamesInput")
    def prevent_duplicate_names_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preventDuplicateNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="provisioningOptionsInput")
    def provisioning_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "provisioningOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityEnabledInput")
    def security_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "securityEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="themeInput")
    def theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typesInput")
    def types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "typesInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="assignableToRole")
    def assignable_to_role(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assignableToRole"))

    @assignable_to_role.setter
    def assignable_to_role(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "assignable_to_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignableToRole", value)

    @builtins.property
    @jsii.member(jsii_name="autoSubscribeNewMembers")
    def auto_subscribe_new_members(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoSubscribeNewMembers"))

    @auto_subscribe_new_members.setter
    def auto_subscribe_new_members(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "auto_subscribe_new_members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSubscribeNewMembers", value)

    @builtins.property
    @jsii.member(jsii_name="behaviors")
    def behaviors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "behaviors"))

    @behaviors.setter
    def behaviors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "behaviors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behaviors", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="externalSendersAllowed")
    def external_senders_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "externalSendersAllowed"))

    @external_senders_allowed.setter
    def external_senders_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "external_senders_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalSendersAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="hideFromAddressLists")
    def hide_from_address_lists(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hideFromAddressLists"))

    @hide_from_address_lists.setter
    def hide_from_address_lists(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "hide_from_address_lists").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hideFromAddressLists", value)

    @builtins.property
    @jsii.member(jsii_name="hideFromOutlookClients")
    def hide_from_outlook_clients(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hideFromOutlookClients"))

    @hide_from_outlook_clients.setter
    def hide_from_outlook_clients(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "hide_from_outlook_clients").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hideFromOutlookClients", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mailEnabled")
    def mail_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mailEnabled"))

    @mail_enabled.setter
    def mail_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "mail_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mailNickname")
    def mail_nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mailNickname"))

    @mail_nickname.setter
    def mail_nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "mail_nickname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailNickname", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="owners")
    def owners(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "owners"))

    @owners.setter
    def owners(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "owners").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owners", value)

    @builtins.property
    @jsii.member(jsii_name="preventDuplicateNames")
    def prevent_duplicate_names(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preventDuplicateNames"))

    @prevent_duplicate_names.setter
    def prevent_duplicate_names(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "prevent_duplicate_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preventDuplicateNames", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningOptions")
    def provisioning_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisioningOptions"))

    @provisioning_options.setter
    def provisioning_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "provisioning_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningOptions", value)

    @builtins.property
    @jsii.member(jsii_name="securityEnabled")
    def security_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "securityEnabled"))

    @security_enabled.setter
    def security_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "security_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "theme"))

    @theme.setter
    def theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "theme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "theme", value)

    @builtins.property
    @jsii.member(jsii_name="types")
    def types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "types"))

    @types.setter
    def types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "types", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Group, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.group.GroupConfig",
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
        "assignable_to_role": "assignableToRole",
        "auto_subscribe_new_members": "autoSubscribeNewMembers",
        "behaviors": "behaviors",
        "description": "description",
        "dynamic_membership": "dynamicMembership",
        "external_senders_allowed": "externalSendersAllowed",
        "hide_from_address_lists": "hideFromAddressLists",
        "hide_from_outlook_clients": "hideFromOutlookClients",
        "id": "id",
        "mail_enabled": "mailEnabled",
        "mail_nickname": "mailNickname",
        "members": "members",
        "owners": "owners",
        "prevent_duplicate_names": "preventDuplicateNames",
        "provisioning_options": "provisioningOptions",
        "security_enabled": "securityEnabled",
        "theme": "theme",
        "timeouts": "timeouts",
        "types": "types",
        "visibility": "visibility",
    },
)
class GroupConfig(cdktf.TerraformMetaArguments):
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
        assignable_to_role: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_subscribe_new_members: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        behaviors: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamic_membership: typing.Optional[typing.Union["GroupDynamicMembership", typing.Dict[str, typing.Any]]] = None,
        external_senders_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide_from_address_lists: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hide_from_outlook_clients: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mail_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        theme: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        types: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The display name for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#display_name Group#display_name}
        :param assignable_to_role: Indicates whether this group can be assigned to an Azure Active Directory role. This property can only be ``true`` for security-enabled groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#assignable_to_role Group#assignable_to_role}
        :param auto_subscribe_new_members: Indicates whether new members added to the group will be auto-subscribed to receive email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#auto_subscribe_new_members Group#auto_subscribe_new_members}
        :param behaviors: The group behaviours for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#behaviors Group#behaviors}
        :param description: The description for the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#description Group#description}
        :param dynamic_membership: dynamic_membership block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#dynamic_membership Group#dynamic_membership}
        :param external_senders_allowed: Indicates whether people external to the organization can send messages to the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#external_senders_allowed Group#external_senders_allowed}
        :param hide_from_address_lists: Indicates whether the group is displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_address_lists Group#hide_from_address_lists}
        :param hide_from_outlook_clients: Indicates whether the group is displayed in Outlook clients, such as Outlook for Windows and Outlook on the web. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_outlook_clients Group#hide_from_outlook_clients}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#id Group#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mail_enabled: Whether the group is a mail enabled, with a shared group mailbox. At least one of ``mail_enabled`` or ``security_enabled`` must be specified. A group can be mail enabled *and* security enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_enabled Group#mail_enabled}
        :param mail_nickname: The mail alias for the group, unique in the organisation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_nickname Group#mail_nickname}
        :param members: A set of members who should be present in this group. Supported object types are Users, Groups or Service Principals Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#members Group#members}
        :param owners: A set of owners who own this group. Supported object types are Users or Service Principals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#owners Group#owners}
        :param prevent_duplicate_names: If ``true``, will return an error if an existing group is found with the same name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#prevent_duplicate_names Group#prevent_duplicate_names}
        :param provisioning_options: The group provisioning options for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#provisioning_options Group#provisioning_options}
        :param security_enabled: Whether the group is a security group for controlling access to in-app resources. At least one of ``security_enabled`` or ``mail_enabled`` must be specified. A group can be security enabled *and* mail enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#security_enabled Group#security_enabled}
        :param theme: The colour theme for a Microsoft 365 group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#theme Group#theme}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#timeouts Group#timeouts}
        :param types: A set of group types to configure for the group. ``Unified`` specifies a Microsoft 365 group. Required when ``mail_enabled`` is true Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#types Group#types}
        :param visibility: Specifies the group join policy and group content visibility. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#visibility Group#visibility}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dynamic_membership, dict):
            dynamic_membership = GroupDynamicMembership(**dynamic_membership)
        if isinstance(timeouts, dict):
            timeouts = GroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument assignable_to_role", value=assignable_to_role, expected_type=type_hints["assignable_to_role"])
            check_type(argname="argument auto_subscribe_new_members", value=auto_subscribe_new_members, expected_type=type_hints["auto_subscribe_new_members"])
            check_type(argname="argument behaviors", value=behaviors, expected_type=type_hints["behaviors"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamic_membership", value=dynamic_membership, expected_type=type_hints["dynamic_membership"])
            check_type(argname="argument external_senders_allowed", value=external_senders_allowed, expected_type=type_hints["external_senders_allowed"])
            check_type(argname="argument hide_from_address_lists", value=hide_from_address_lists, expected_type=type_hints["hide_from_address_lists"])
            check_type(argname="argument hide_from_outlook_clients", value=hide_from_outlook_clients, expected_type=type_hints["hide_from_outlook_clients"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mail_enabled", value=mail_enabled, expected_type=type_hints["mail_enabled"])
            check_type(argname="argument mail_nickname", value=mail_nickname, expected_type=type_hints["mail_nickname"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument owners", value=owners, expected_type=type_hints["owners"])
            check_type(argname="argument prevent_duplicate_names", value=prevent_duplicate_names, expected_type=type_hints["prevent_duplicate_names"])
            check_type(argname="argument provisioning_options", value=provisioning_options, expected_type=type_hints["provisioning_options"])
            check_type(argname="argument security_enabled", value=security_enabled, expected_type=type_hints["security_enabled"])
            check_type(argname="argument theme", value=theme, expected_type=type_hints["theme"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument types", value=types, expected_type=type_hints["types"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
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
        if assignable_to_role is not None:
            self._values["assignable_to_role"] = assignable_to_role
        if auto_subscribe_new_members is not None:
            self._values["auto_subscribe_new_members"] = auto_subscribe_new_members
        if behaviors is not None:
            self._values["behaviors"] = behaviors
        if description is not None:
            self._values["description"] = description
        if dynamic_membership is not None:
            self._values["dynamic_membership"] = dynamic_membership
        if external_senders_allowed is not None:
            self._values["external_senders_allowed"] = external_senders_allowed
        if hide_from_address_lists is not None:
            self._values["hide_from_address_lists"] = hide_from_address_lists
        if hide_from_outlook_clients is not None:
            self._values["hide_from_outlook_clients"] = hide_from_outlook_clients
        if id is not None:
            self._values["id"] = id
        if mail_enabled is not None:
            self._values["mail_enabled"] = mail_enabled
        if mail_nickname is not None:
            self._values["mail_nickname"] = mail_nickname
        if members is not None:
            self._values["members"] = members
        if owners is not None:
            self._values["owners"] = owners
        if prevent_duplicate_names is not None:
            self._values["prevent_duplicate_names"] = prevent_duplicate_names
        if provisioning_options is not None:
            self._values["provisioning_options"] = provisioning_options
        if security_enabled is not None:
            self._values["security_enabled"] = security_enabled
        if theme is not None:
            self._values["theme"] = theme
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if types is not None:
            self._values["types"] = types
        if visibility is not None:
            self._values["visibility"] = visibility

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
        '''The display name for the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#display_name Group#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignable_to_role(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether this group can be assigned to an Azure Active Directory role.

        This property can only be ``true`` for security-enabled groups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#assignable_to_role Group#assignable_to_role}
        '''
        result = self._values.get("assignable_to_role")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_subscribe_new_members(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether new members added to the group will be auto-subscribed to receive email notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#auto_subscribe_new_members Group#auto_subscribe_new_members}
        '''
        result = self._values.get("auto_subscribe_new_members")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def behaviors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The group behaviours for a Microsoft 365 group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#behaviors Group#behaviors}
        '''
        result = self._values.get("behaviors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#description Group#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamic_membership(self) -> typing.Optional["GroupDynamicMembership"]:
        '''dynamic_membership block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#dynamic_membership Group#dynamic_membership}
        '''
        result = self._values.get("dynamic_membership")
        return typing.cast(typing.Optional["GroupDynamicMembership"], result)

    @builtins.property
    def external_senders_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether people external to the organization can send messages to the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#external_senders_allowed Group#external_senders_allowed}
        '''
        result = self._values.get("external_senders_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hide_from_address_lists(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the group is displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_address_lists Group#hide_from_address_lists}
        '''
        result = self._values.get("hide_from_address_lists")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hide_from_outlook_clients(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the group is displayed in Outlook clients, such as Outlook for Windows and Outlook on the web.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#hide_from_outlook_clients Group#hide_from_outlook_clients}
        '''
        result = self._values.get("hide_from_outlook_clients")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#id Group#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mail_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the group is a mail enabled, with a shared group mailbox.

        At least one of ``mail_enabled`` or ``security_enabled`` must be specified. A group can be mail enabled *and* security enabled

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_enabled Group#mail_enabled}
        '''
        result = self._values.get("mail_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mail_nickname(self) -> typing.Optional[builtins.str]:
        '''The mail alias for the group, unique in the organisation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#mail_nickname Group#mail_nickname}
        '''
        result = self._values.get("mail_nickname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of members who should be present in this group.

        Supported object types are Users, Groups or Service Principals

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#members Group#members}
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of owners who own this group. Supported object types are Users or Service Principals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#owners Group#owners}
        '''
        result = self._values.get("owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prevent_duplicate_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, will return an error if an existing group is found with the same name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#prevent_duplicate_names Group#prevent_duplicate_names}
        '''
        result = self._values.get("prevent_duplicate_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def provisioning_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The group provisioning options for a Microsoft 365 group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#provisioning_options Group#provisioning_options}
        '''
        result = self._values.get("provisioning_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the group is a security group for controlling access to in-app resources.

        At least one of ``security_enabled`` or ``mail_enabled`` must be specified. A group can be security enabled *and* mail enabled

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#security_enabled Group#security_enabled}
        '''
        result = self._values.get("security_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def theme(self) -> typing.Optional[builtins.str]:
        '''The colour theme for a Microsoft 365 group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#theme Group#theme}
        '''
        result = self._values.get("theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#timeouts Group#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GroupTimeouts"], result)

    @builtins.property
    def types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A set of group types to configure for the group.

        ``Unified`` specifies a Microsoft 365 group. Required when ``mail_enabled`` is true

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#types Group#types}
        '''
        result = self._values.get("types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Specifies the group join policy and group content visibility.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#visibility Group#visibility}
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.group.GroupDynamicMembership",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "rule": "rule"},
)
class GroupDynamicMembership:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        rule: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#enabled Group#enabled}.
        :param rule: Rule to determine members for a dynamic group. Required when ``group_types`` contains 'DynamicMembership'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#rule Group#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupDynamicMembership.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "rule": rule,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#enabled Group#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Rule to determine members for a dynamic group. Required when ``group_types`` contains 'DynamicMembership'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#rule Group#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupDynamicMembership(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupDynamicMembershipOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.group.GroupDynamicMembershipOutputReference",
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
            type_hints = typing.get_type_hints(GroupDynamicMembershipOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupDynamicMembershipOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupDynamicMembershipOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupDynamicMembership]:
        return typing.cast(typing.Optional[GroupDynamicMembership], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GroupDynamicMembership]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupDynamicMembershipOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.group.GroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class GroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#create Group#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#delete Group#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#read Group#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#update Group#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#create Group#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#delete Group#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#read Group#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/group#update Group#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.group.GroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Group",
    "GroupConfig",
    "GroupDynamicMembership",
    "GroupDynamicMembershipOutputReference",
    "GroupTimeouts",
    "GroupTimeoutsOutputReference",
]

publication.publish()
