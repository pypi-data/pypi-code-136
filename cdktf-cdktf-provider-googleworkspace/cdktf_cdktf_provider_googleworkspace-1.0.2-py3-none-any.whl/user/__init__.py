'''
# `googleworkspace_user`

Refer to the Terraform Registory for docs: [`googleworkspace_user`](https://www.terraform.io/docs/providers/googleworkspace/r/user).
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


class User(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/user googleworkspace_user}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: typing.Union["UserName", typing.Dict[str, typing.Any]],
        primary_email: builtins.str,
        addresses: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserAddresses", typing.Dict[str, typing.Any]]]]] = None,
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        change_password_at_next_login: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_schemas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserCustomSchemas", typing.Dict[str, typing.Any]]]]] = None,
        emails: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserEmails", typing.Dict[str, typing.Any]]]]] = None,
        external_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserExternalIds", typing.Dict[str, typing.Any]]]]] = None,
        hash_function: typing.Optional[builtins.str] = None,
        ims: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserIms", typing.Dict[str, typing.Any]]]]] = None,
        include_in_global_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_allowlist: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_admin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keywords: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserKeywords", typing.Dict[str, typing.Any]]]]] = None,
        languages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLanguages", typing.Dict[str, typing.Any]]]]] = None,
        locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLocations", typing.Dict[str, typing.Any]]]]] = None,
        organizations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserOrganizations", typing.Dict[str, typing.Any]]]]] = None,
        org_unit_path: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        phones: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPhones", typing.Dict[str, typing.Any]]]]] = None,
        posix_accounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPosixAccounts", typing.Dict[str, typing.Any]]]]] = None,
        recovery_email: typing.Optional[builtins.str] = None,
        recovery_phone: typing.Optional[builtins.str] = None,
        relations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserRelations", typing.Dict[str, typing.Any]]]]] = None,
        ssh_public_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserSshPublicKeys", typing.Dict[str, typing.Any]]]]] = None,
        suspended: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["UserTimeouts", typing.Dict[str, typing.Any]]] = None,
        websites: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserWebsites", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/user googleworkspace_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#name User#name}
        :param primary_email: The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary_email User#primary_email}
        :param addresses: addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#addresses User#addresses}
        :param aliases: asps.list of the user's alias email addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#aliases User#aliases}
        :param archived: Indicates if user is archived. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#archived User#archived}
        :param change_password_at_next_login: Indicates if the user is forced to change their password at next login. This setting doesn't apply when the user signs in via a third-party identity provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#change_password_at_next_login User#change_password_at_next_login}
        :param custom_schemas: custom_schemas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_schemas User#custom_schemas}
        :param emails: emails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#emails User#emails}
        :param external_ids: external_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#external_ids User#external_ids}
        :param hash_function: Stores the hash format of the password property. We recommend sending the password property value as a base 16 bit hexadecimal-encoded hash value. Set the hashFunction values as either the SHA-1, MD5, or crypt hash format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#hash_function User#hash_function}
        :param ims: ims block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ims User#ims}
        :param include_in_global_address_list: Defaults to ``true``. Indicates if the user's profile is visible in the Google Workspace global address list when the contact sharing feature is enabled for the domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#include_in_global_address_list User#include_in_global_address_list}
        :param ip_allowlist: If true, the user's IP address is added to the allow list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ip_allowlist User#ip_allowlist}
        :param is_admin: Indicates a user with super admininistrator privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#is_admin User#is_admin}
        :param keywords: keywords block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#keywords User#keywords}
        :param languages: languages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#languages User#languages}
        :param locations: locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#locations User#locations}
        :param organizations: organizations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#organizations User#organizations}
        :param org_unit_path: The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (/). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#org_unit_path User#org_unit_path}
        :param password: Stores the password for the user account. A password can contain any combination of ASCII characters. A minimum of 8 characters is required. The maximum length is 100 characters. As the API does not return the value of password, this field is write-only, and the value stored in the state will be what is provided in the configuration. The field is required on create and will be empty on import. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#password User#password}
        :param phones: phones block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#phones User#phones}
        :param posix_accounts: posix_accounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#posix_accounts User#posix_accounts}
        :param recovery_email: Recovery email of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_email User#recovery_email}
        :param recovery_phone: Recovery phone of the user. The phone number must be in the E.164 format, starting with the plus sign (+). Example: +16506661212. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_phone User#recovery_phone}
        :param relations: relations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#relations User#relations}
        :param ssh_public_keys: ssh_public_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ssh_public_keys User#ssh_public_keys}
        :param suspended: Indicates if user is suspended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#suspended User#suspended}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#timeouts User#timeouts}
        :param websites: websites block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#websites User#websites}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = UserConfig(
            name=name,
            primary_email=primary_email,
            addresses=addresses,
            aliases=aliases,
            archived=archived,
            change_password_at_next_login=change_password_at_next_login,
            custom_schemas=custom_schemas,
            emails=emails,
            external_ids=external_ids,
            hash_function=hash_function,
            ims=ims,
            include_in_global_address_list=include_in_global_address_list,
            ip_allowlist=ip_allowlist,
            is_admin=is_admin,
            keywords=keywords,
            languages=languages,
            locations=locations,
            organizations=organizations,
            org_unit_path=org_unit_path,
            password=password,
            phones=phones,
            posix_accounts=posix_accounts,
            recovery_email=recovery_email,
            recovery_phone=recovery_phone,
            relations=relations,
            ssh_public_keys=ssh_public_keys,
            suspended=suspended,
            timeouts=timeouts,
            websites=websites,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putAddresses")
    def put_addresses(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserAddresses", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_addresses)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAddresses", [value]))

    @jsii.member(jsii_name="putCustomSchemas")
    def put_custom_schemas(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserCustomSchemas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_custom_schemas)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomSchemas", [value]))

    @jsii.member(jsii_name="putEmails")
    def put_emails(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserEmails", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_emails)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmails", [value]))

    @jsii.member(jsii_name="putExternalIds")
    def put_external_ids(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserExternalIds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_external_ids)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExternalIds", [value]))

    @jsii.member(jsii_name="putIms")
    def put_ims(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserIms", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_ims)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIms", [value]))

    @jsii.member(jsii_name="putKeywords")
    def put_keywords(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserKeywords", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_keywords)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKeywords", [value]))

    @jsii.member(jsii_name="putLanguages")
    def put_languages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLanguages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_languages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLanguages", [value]))

    @jsii.member(jsii_name="putLocations")
    def put_locations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLocations", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_locations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocations", [value]))

    @jsii.member(jsii_name="putName")
    def put_name(
        self,
        *,
        family_name: builtins.str,
        given_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param family_name: The user's last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#family_name User#family_name}
        :param given_name: The user's first name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#given_name User#given_name}
        '''
        value = UserName(family_name=family_name, given_name=given_name)

        return typing.cast(None, jsii.invoke(self, "putName", [value]))

    @jsii.member(jsii_name="putOrganizations")
    def put_organizations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserOrganizations", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_organizations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrganizations", [value]))

    @jsii.member(jsii_name="putPhones")
    def put_phones(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPhones", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_phones)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPhones", [value]))

    @jsii.member(jsii_name="putPosixAccounts")
    def put_posix_accounts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPosixAccounts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_posix_accounts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPosixAccounts", [value]))

    @jsii.member(jsii_name="putRelations")
    def put_relations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserRelations", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_relations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRelations", [value]))

    @jsii.member(jsii_name="putSshPublicKeys")
    def put_ssh_public_keys(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserSshPublicKeys", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_ssh_public_keys)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSshPublicKeys", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#create User#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#update User#update}.
        '''
        value = UserTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWebsites")
    def put_websites(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserWebsites", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(User.put_websites)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebsites", [value]))

    @jsii.member(jsii_name="resetAddresses")
    def reset_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddresses", []))

    @jsii.member(jsii_name="resetAliases")
    def reset_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliases", []))

    @jsii.member(jsii_name="resetArchived")
    def reset_archived(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchived", []))

    @jsii.member(jsii_name="resetChangePasswordAtNextLogin")
    def reset_change_password_at_next_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangePasswordAtNextLogin", []))

    @jsii.member(jsii_name="resetCustomSchemas")
    def reset_custom_schemas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSchemas", []))

    @jsii.member(jsii_name="resetEmails")
    def reset_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmails", []))

    @jsii.member(jsii_name="resetExternalIds")
    def reset_external_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalIds", []))

    @jsii.member(jsii_name="resetHashFunction")
    def reset_hash_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHashFunction", []))

    @jsii.member(jsii_name="resetIms")
    def reset_ims(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIms", []))

    @jsii.member(jsii_name="resetIncludeInGlobalAddressList")
    def reset_include_in_global_address_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeInGlobalAddressList", []))

    @jsii.member(jsii_name="resetIpAllowlist")
    def reset_ip_allowlist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAllowlist", []))

    @jsii.member(jsii_name="resetIsAdmin")
    def reset_is_admin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsAdmin", []))

    @jsii.member(jsii_name="resetKeywords")
    def reset_keywords(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeywords", []))

    @jsii.member(jsii_name="resetLanguages")
    def reset_languages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguages", []))

    @jsii.member(jsii_name="resetLocations")
    def reset_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocations", []))

    @jsii.member(jsii_name="resetOrganizations")
    def reset_organizations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizations", []))

    @jsii.member(jsii_name="resetOrgUnitPath")
    def reset_org_unit_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgUnitPath", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPhones")
    def reset_phones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhones", []))

    @jsii.member(jsii_name="resetPosixAccounts")
    def reset_posix_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosixAccounts", []))

    @jsii.member(jsii_name="resetRecoveryEmail")
    def reset_recovery_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryEmail", []))

    @jsii.member(jsii_name="resetRecoveryPhone")
    def reset_recovery_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryPhone", []))

    @jsii.member(jsii_name="resetRelations")
    def reset_relations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelations", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @jsii.member(jsii_name="resetSuspended")
    def reset_suspended(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspended", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWebsites")
    def reset_websites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsites", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> "UserAddressesList":
        return typing.cast("UserAddressesList", jsii.get(self, "addresses"))

    @builtins.property
    @jsii.member(jsii_name="agreedToTerms")
    def agreed_to_terms(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "agreedToTerms"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="customerId")
    def customer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerId"))

    @builtins.property
    @jsii.member(jsii_name="customSchemas")
    def custom_schemas(self) -> "UserCustomSchemasList":
        return typing.cast("UserCustomSchemasList", jsii.get(self, "customSchemas"))

    @builtins.property
    @jsii.member(jsii_name="deletionTime")
    def deletion_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deletionTime"))

    @builtins.property
    @jsii.member(jsii_name="emails")
    def emails(self) -> "UserEmailsList":
        return typing.cast("UserEmailsList", jsii.get(self, "emails"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="externalIds")
    def external_ids(self) -> "UserExternalIdsList":
        return typing.cast("UserExternalIdsList", jsii.get(self, "externalIds"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="ims")
    def ims(self) -> "UserImsList":
        return typing.cast("UserImsList", jsii.get(self, "ims"))

    @builtins.property
    @jsii.member(jsii_name="isDelegatedAdmin")
    def is_delegated_admin(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isDelegatedAdmin"))

    @builtins.property
    @jsii.member(jsii_name="isEnforcedIn2StepVerification")
    def is_enforced_in2_step_verification(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isEnforcedIn2StepVerification"))

    @builtins.property
    @jsii.member(jsii_name="isEnrolledIn2StepVerification")
    def is_enrolled_in2_step_verification(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isEnrolledIn2StepVerification"))

    @builtins.property
    @jsii.member(jsii_name="isMailboxSetup")
    def is_mailbox_setup(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isMailboxSetup"))

    @builtins.property
    @jsii.member(jsii_name="keywords")
    def keywords(self) -> "UserKeywordsList":
        return typing.cast("UserKeywordsList", jsii.get(self, "keywords"))

    @builtins.property
    @jsii.member(jsii_name="languages")
    def languages(self) -> "UserLanguagesList":
        return typing.cast("UserLanguagesList", jsii.get(self, "languages"))

    @builtins.property
    @jsii.member(jsii_name="lastLoginTime")
    def last_login_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastLoginTime"))

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> "UserLocationsList":
        return typing.cast("UserLocationsList", jsii.get(self, "locations"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> "UserNameOutputReference":
        return typing.cast("UserNameOutputReference", jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="nonEditableAliases")
    def non_editable_aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nonEditableAliases"))

    @builtins.property
    @jsii.member(jsii_name="organizations")
    def organizations(self) -> "UserOrganizationsList":
        return typing.cast("UserOrganizationsList", jsii.get(self, "organizations"))

    @builtins.property
    @jsii.member(jsii_name="phones")
    def phones(self) -> "UserPhonesList":
        return typing.cast("UserPhonesList", jsii.get(self, "phones"))

    @builtins.property
    @jsii.member(jsii_name="posixAccounts")
    def posix_accounts(self) -> "UserPosixAccountsList":
        return typing.cast("UserPosixAccountsList", jsii.get(self, "posixAccounts"))

    @builtins.property
    @jsii.member(jsii_name="relations")
    def relations(self) -> "UserRelationsList":
        return typing.cast("UserRelationsList", jsii.get(self, "relations"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> "UserSshPublicKeysList":
        return typing.cast("UserSshPublicKeysList", jsii.get(self, "sshPublicKeys"))

    @builtins.property
    @jsii.member(jsii_name="suspensionReason")
    def suspension_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suspensionReason"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailPhotoEtag")
    def thumbnail_photo_etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbnailPhotoEtag"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailPhotoUrl")
    def thumbnail_photo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbnailPhotoUrl"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "UserTimeoutsOutputReference":
        return typing.cast("UserTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="websites")
    def websites(self) -> "UserWebsitesList":
        return typing.cast("UserWebsitesList", jsii.get(self, "websites"))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserAddresses"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserAddresses"]]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasesInput")
    def aliases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="archivedInput")
    def archived_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "archivedInput"))

    @builtins.property
    @jsii.member(jsii_name="changePasswordAtNextLoginInput")
    def change_password_at_next_login_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "changePasswordAtNextLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="customSchemasInput")
    def custom_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserCustomSchemas"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserCustomSchemas"]]], jsii.get(self, "customSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsInput")
    def emails_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserEmails"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserEmails"]]], jsii.get(self, "emailsInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdsInput")
    def external_ids_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserExternalIds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserExternalIds"]]], jsii.get(self, "externalIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="hashFunctionInput")
    def hash_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="imsInput")
    def ims_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserIms"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserIms"]]], jsii.get(self, "imsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInGlobalAddressListInput")
    def include_in_global_address_list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeInGlobalAddressListInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAllowlistInput")
    def ip_allowlist_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipAllowlistInput"))

    @builtins.property
    @jsii.member(jsii_name="isAdminInput")
    def is_admin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="keywordsInput")
    def keywords_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserKeywords"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserKeywords"]]], jsii.get(self, "keywordsInput"))

    @builtins.property
    @jsii.member(jsii_name="languagesInput")
    def languages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLanguages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLanguages"]]], jsii.get(self, "languagesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLocations"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLocations"]]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional["UserName"]:
        return typing.cast(typing.Optional["UserName"], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationsInput")
    def organizations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserOrganizations"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserOrganizations"]]], jsii.get(self, "organizationsInput"))

    @builtins.property
    @jsii.member(jsii_name="orgUnitPathInput")
    def org_unit_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orgUnitPathInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="phonesInput")
    def phones_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPhones"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPhones"]]], jsii.get(self, "phonesInput"))

    @builtins.property
    @jsii.member(jsii_name="posixAccountsInput")
    def posix_accounts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPosixAccounts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPosixAccounts"]]], jsii.get(self, "posixAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryEmailInput")
    def primary_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryEmailInput")
    def recovery_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryPhoneInput")
    def recovery_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryPhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="relationsInput")
    def relations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserRelations"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserRelations"]]], jsii.get(self, "relationsInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeysInput")
    def ssh_public_keys_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserSshPublicKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserSshPublicKeys"]]], jsii.get(self, "sshPublicKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendedInput")
    def suspended_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suspendedInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["UserTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["UserTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="websitesInput")
    def websites_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserWebsites"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserWebsites"]]], jsii.get(self, "websitesInput"))

    @builtins.property
    @jsii.member(jsii_name="aliases")
    def aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliases"))

    @aliases.setter
    def aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliases", value)

    @builtins.property
    @jsii.member(jsii_name="archived")
    def archived(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "archived"))

    @archived.setter
    def archived(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "archived").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archived", value)

    @builtins.property
    @jsii.member(jsii_name="changePasswordAtNextLogin")
    def change_password_at_next_login(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "changePasswordAtNextLogin"))

    @change_password_at_next_login.setter
    def change_password_at_next_login(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "change_password_at_next_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changePasswordAtNextLogin", value)

    @builtins.property
    @jsii.member(jsii_name="hashFunction")
    def hash_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashFunction"))

    @hash_function.setter
    def hash_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "hash_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashFunction", value)

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
            type_hints = typing.get_type_hints(getattr(User, "include_in_global_address_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeInGlobalAddressList", value)

    @builtins.property
    @jsii.member(jsii_name="ipAllowlist")
    def ip_allowlist(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipAllowlist"))

    @ip_allowlist.setter
    def ip_allowlist(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "ip_allowlist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAllowlist", value)

    @builtins.property
    @jsii.member(jsii_name="isAdmin")
    def is_admin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isAdmin"))

    @is_admin.setter
    def is_admin(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "is_admin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isAdmin", value)

    @builtins.property
    @jsii.member(jsii_name="orgUnitPath")
    def org_unit_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgUnitPath"))

    @org_unit_path.setter
    def org_unit_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "org_unit_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgUnitPath", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="primaryEmail")
    def primary_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryEmail"))

    @primary_email.setter
    def primary_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "primary_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryEmail", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryEmail")
    def recovery_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryEmail"))

    @recovery_email.setter
    def recovery_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "recovery_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryEmail", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryPhone")
    def recovery_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryPhone"))

    @recovery_phone.setter
    def recovery_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "recovery_phone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryPhone", value)

    @builtins.property
    @jsii.member(jsii_name="suspended")
    def suspended(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suspended"))

    @suspended.setter
    def suspended(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "suspended").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspended", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserAddresses",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "country": "country",
        "country_code": "countryCode",
        "custom_type": "customType",
        "extended_address": "extendedAddress",
        "formatted": "formatted",
        "locality": "locality",
        "po_box": "poBox",
        "postal_code": "postalCode",
        "primary": "primary",
        "region": "region",
        "source_is_structured": "sourceIsStructured",
        "street_address": "streetAddress",
    },
)
class UserAddresses:
    def __init__(
        self,
        *,
        type: builtins.str,
        country: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        custom_type: typing.Optional[builtins.str] = None,
        extended_address: typing.Optional[builtins.str] = None,
        formatted: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        region: typing.Optional[builtins.str] = None,
        source_is_structured: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        street_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The address type. Acceptable values: ``custom``, ``home``, ``other``, ``work``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param country: Country. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#country User#country}
        :param country_code: The country code. Uses the ISO 3166-1 standard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#country_code User#country_code}
        :param custom_type: If the address type is custom, this property contains the custom value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param extended_address: For extended addresses, such as an address that includes a sub-region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#extended_address User#extended_address}
        :param formatted: A full and unstructured postal address. This is not synced with the structured address fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#formatted User#formatted}
        :param locality: The town or city of the address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#locality User#locality}
        :param po_box: The post office box, if present. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#po_box User#po_box}
        :param postal_code: The ZIP or postal code, if applicable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#postal_code User#postal_code}
        :param primary: If this is the user's primary address. The addresses list may contain only one primary address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        :param region: The abbreviated province or state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#region User#region}
        :param source_is_structured: Indicates if the user-supplied address was formatted. Formatted addresses are not currently supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#source_is_structured User#source_is_structured}
        :param street_address: The street address, such as 1600 Amphitheatre Parkway. Whitespace within the string is ignored; however, newlines are significant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#street_address User#street_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserAddresses.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument extended_address", value=extended_address, expected_type=type_hints["extended_address"])
            check_type(argname="argument formatted", value=formatted, expected_type=type_hints["formatted"])
            check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
            check_type(argname="argument po_box", value=po_box, expected_type=type_hints["po_box"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument source_is_structured", value=source_is_structured, expected_type=type_hints["source_is_structured"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if country is not None:
            self._values["country"] = country
        if country_code is not None:
            self._values["country_code"] = country_code
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if extended_address is not None:
            self._values["extended_address"] = extended_address
        if formatted is not None:
            self._values["formatted"] = formatted
        if locality is not None:
            self._values["locality"] = locality
        if po_box is not None:
            self._values["po_box"] = po_box
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if primary is not None:
            self._values["primary"] = primary
        if region is not None:
            self._values["region"] = region
        if source_is_structured is not None:
            self._values["source_is_structured"] = source_is_structured
        if street_address is not None:
            self._values["street_address"] = street_address

    @builtins.property
    def type(self) -> builtins.str:
        '''The address type. Acceptable values: ``custom``, ``home``, ``other``, ``work``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Country.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#country User#country}
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''The country code. Uses the ISO 3166-1 standard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#country_code User#country_code}
        '''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the address type is custom, this property contains the custom value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extended_address(self) -> typing.Optional[builtins.str]:
        '''For extended addresses, such as an address that includes a sub-region.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#extended_address User#extended_address}
        '''
        result = self._values.get("extended_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def formatted(self) -> typing.Optional[builtins.str]:
        '''A full and unstructured postal address. This is not synced with the structured address fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#formatted User#formatted}
        '''
        result = self._values.get("formatted")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The town or city of the address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#locality User#locality}
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def po_box(self) -> typing.Optional[builtins.str]:
        '''The post office box, if present.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#po_box User#po_box}
        '''
        result = self._values.get("po_box")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''The ZIP or postal code, if applicable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#postal_code User#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this is the user's primary address. The addresses list may contain only one primary address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The abbreviated province or state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#region User#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_is_structured(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if the user-supplied address was formatted. Formatted addresses are not currently supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#source_is_structured User#source_is_structured}
        '''
        result = self._values.get("source_is_structured")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''The street address, such as 1600 Amphitheatre Parkway. Whitespace within the string is ignored; however, newlines are significant.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#street_address User#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserAddressesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserAddressesList",
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
            type_hints = typing.get_type_hints(UserAddressesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserAddressesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserAddressesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserAddressesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserAddressesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserAddressesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserAddresses]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserAddresses]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserAddresses]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserAddressesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserAddressesOutputReference",
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
            type_hints = typing.get_type_hints(UserAddressesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetExtendedAddress")
    def reset_extended_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedAddress", []))

    @jsii.member(jsii_name="resetFormatted")
    def reset_formatted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormatted", []))

    @jsii.member(jsii_name="resetLocality")
    def reset_locality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocality", []))

    @jsii.member(jsii_name="resetPoBox")
    def reset_po_box(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoBox", []))

    @jsii.member(jsii_name="resetPostalCode")
    def reset_postal_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalCode", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSourceIsStructured")
    def reset_source_is_structured(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIsStructured", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedAddressInput")
    def extended_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extendedAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="formattedInput")
    def formatted_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formattedInput"))

    @builtins.property
    @jsii.member(jsii_name="localityInput")
    def locality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localityInput"))

    @builtins.property
    @jsii.member(jsii_name="poBoxInput")
    def po_box_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poBoxInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIsStructuredInput")
    def source_is_structured_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sourceIsStructuredInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="extendedAddress")
    def extended_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extendedAddress"))

    @extended_address.setter
    def extended_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "extended_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedAddress", value)

    @builtins.property
    @jsii.member(jsii_name="formatted")
    def formatted(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatted"))

    @formatted.setter
    def formatted(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "formatted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatted", value)

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @locality.setter
    def locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "locality").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locality", value)

    @builtins.property
    @jsii.member(jsii_name="poBox")
    def po_box(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "poBox"))

    @po_box.setter
    def po_box(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "po_box").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poBox", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIsStructured")
    def source_is_structured(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sourceIsStructured"))

    @source_is_structured.setter
    def source_is_structured(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "source_is_structured").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIsStructured", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "street_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserAddresses, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserAddresses, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserAddresses, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserAddressesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "primary_email": "primaryEmail",
        "addresses": "addresses",
        "aliases": "aliases",
        "archived": "archived",
        "change_password_at_next_login": "changePasswordAtNextLogin",
        "custom_schemas": "customSchemas",
        "emails": "emails",
        "external_ids": "externalIds",
        "hash_function": "hashFunction",
        "ims": "ims",
        "include_in_global_address_list": "includeInGlobalAddressList",
        "ip_allowlist": "ipAllowlist",
        "is_admin": "isAdmin",
        "keywords": "keywords",
        "languages": "languages",
        "locations": "locations",
        "organizations": "organizations",
        "org_unit_path": "orgUnitPath",
        "password": "password",
        "phones": "phones",
        "posix_accounts": "posixAccounts",
        "recovery_email": "recoveryEmail",
        "recovery_phone": "recoveryPhone",
        "relations": "relations",
        "ssh_public_keys": "sshPublicKeys",
        "suspended": "suspended",
        "timeouts": "timeouts",
        "websites": "websites",
    },
)
class UserConfig(cdktf.TerraformMetaArguments):
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
        name: typing.Union["UserName", typing.Dict[str, typing.Any]],
        primary_email: builtins.str,
        addresses: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[UserAddresses, typing.Dict[str, typing.Any]]]]] = None,
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        change_password_at_next_login: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_schemas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserCustomSchemas", typing.Dict[str, typing.Any]]]]] = None,
        emails: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserEmails", typing.Dict[str, typing.Any]]]]] = None,
        external_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserExternalIds", typing.Dict[str, typing.Any]]]]] = None,
        hash_function: typing.Optional[builtins.str] = None,
        ims: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserIms", typing.Dict[str, typing.Any]]]]] = None,
        include_in_global_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_allowlist: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_admin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keywords: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserKeywords", typing.Dict[str, typing.Any]]]]] = None,
        languages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLanguages", typing.Dict[str, typing.Any]]]]] = None,
        locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserLocations", typing.Dict[str, typing.Any]]]]] = None,
        organizations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserOrganizations", typing.Dict[str, typing.Any]]]]] = None,
        org_unit_path: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        phones: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPhones", typing.Dict[str, typing.Any]]]]] = None,
        posix_accounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserPosixAccounts", typing.Dict[str, typing.Any]]]]] = None,
        recovery_email: typing.Optional[builtins.str] = None,
        recovery_phone: typing.Optional[builtins.str] = None,
        relations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserRelations", typing.Dict[str, typing.Any]]]]] = None,
        ssh_public_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserSshPublicKeys", typing.Dict[str, typing.Any]]]]] = None,
        suspended: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["UserTimeouts", typing.Dict[str, typing.Any]]] = None,
        websites: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["UserWebsites", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#name User#name}
        :param primary_email: The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary_email User#primary_email}
        :param addresses: addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#addresses User#addresses}
        :param aliases: asps.list of the user's alias email addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#aliases User#aliases}
        :param archived: Indicates if user is archived. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#archived User#archived}
        :param change_password_at_next_login: Indicates if the user is forced to change their password at next login. This setting doesn't apply when the user signs in via a third-party identity provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#change_password_at_next_login User#change_password_at_next_login}
        :param custom_schemas: custom_schemas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_schemas User#custom_schemas}
        :param emails: emails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#emails User#emails}
        :param external_ids: external_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#external_ids User#external_ids}
        :param hash_function: Stores the hash format of the password property. We recommend sending the password property value as a base 16 bit hexadecimal-encoded hash value. Set the hashFunction values as either the SHA-1, MD5, or crypt hash format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#hash_function User#hash_function}
        :param ims: ims block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ims User#ims}
        :param include_in_global_address_list: Defaults to ``true``. Indicates if the user's profile is visible in the Google Workspace global address list when the contact sharing feature is enabled for the domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#include_in_global_address_list User#include_in_global_address_list}
        :param ip_allowlist: If true, the user's IP address is added to the allow list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ip_allowlist User#ip_allowlist}
        :param is_admin: Indicates a user with super admininistrator privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#is_admin User#is_admin}
        :param keywords: keywords block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#keywords User#keywords}
        :param languages: languages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#languages User#languages}
        :param locations: locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#locations User#locations}
        :param organizations: organizations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#organizations User#organizations}
        :param org_unit_path: The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (/). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#org_unit_path User#org_unit_path}
        :param password: Stores the password for the user account. A password can contain any combination of ASCII characters. A minimum of 8 characters is required. The maximum length is 100 characters. As the API does not return the value of password, this field is write-only, and the value stored in the state will be what is provided in the configuration. The field is required on create and will be empty on import. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#password User#password}
        :param phones: phones block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#phones User#phones}
        :param posix_accounts: posix_accounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#posix_accounts User#posix_accounts}
        :param recovery_email: Recovery email of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_email User#recovery_email}
        :param recovery_phone: Recovery phone of the user. The phone number must be in the E.164 format, starting with the plus sign (+). Example: +16506661212. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_phone User#recovery_phone}
        :param relations: relations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#relations User#relations}
        :param ssh_public_keys: ssh_public_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ssh_public_keys User#ssh_public_keys}
        :param suspended: Indicates if user is suspended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#suspended User#suspended}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#timeouts User#timeouts}
        :param websites: websites block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#websites User#websites}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(name, dict):
            name = UserName(**name)
        if isinstance(timeouts, dict):
            timeouts = UserTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(UserConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary_email", value=primary_email, expected_type=type_hints["primary_email"])
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument aliases", value=aliases, expected_type=type_hints["aliases"])
            check_type(argname="argument archived", value=archived, expected_type=type_hints["archived"])
            check_type(argname="argument change_password_at_next_login", value=change_password_at_next_login, expected_type=type_hints["change_password_at_next_login"])
            check_type(argname="argument custom_schemas", value=custom_schemas, expected_type=type_hints["custom_schemas"])
            check_type(argname="argument emails", value=emails, expected_type=type_hints["emails"])
            check_type(argname="argument external_ids", value=external_ids, expected_type=type_hints["external_ids"])
            check_type(argname="argument hash_function", value=hash_function, expected_type=type_hints["hash_function"])
            check_type(argname="argument ims", value=ims, expected_type=type_hints["ims"])
            check_type(argname="argument include_in_global_address_list", value=include_in_global_address_list, expected_type=type_hints["include_in_global_address_list"])
            check_type(argname="argument ip_allowlist", value=ip_allowlist, expected_type=type_hints["ip_allowlist"])
            check_type(argname="argument is_admin", value=is_admin, expected_type=type_hints["is_admin"])
            check_type(argname="argument keywords", value=keywords, expected_type=type_hints["keywords"])
            check_type(argname="argument languages", value=languages, expected_type=type_hints["languages"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument organizations", value=organizations, expected_type=type_hints["organizations"])
            check_type(argname="argument org_unit_path", value=org_unit_path, expected_type=type_hints["org_unit_path"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument phones", value=phones, expected_type=type_hints["phones"])
            check_type(argname="argument posix_accounts", value=posix_accounts, expected_type=type_hints["posix_accounts"])
            check_type(argname="argument recovery_email", value=recovery_email, expected_type=type_hints["recovery_email"])
            check_type(argname="argument recovery_phone", value=recovery_phone, expected_type=type_hints["recovery_phone"])
            check_type(argname="argument relations", value=relations, expected_type=type_hints["relations"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument suspended", value=suspended, expected_type=type_hints["suspended"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument websites", value=websites, expected_type=type_hints["websites"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "primary_email": primary_email,
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
        if addresses is not None:
            self._values["addresses"] = addresses
        if aliases is not None:
            self._values["aliases"] = aliases
        if archived is not None:
            self._values["archived"] = archived
        if change_password_at_next_login is not None:
            self._values["change_password_at_next_login"] = change_password_at_next_login
        if custom_schemas is not None:
            self._values["custom_schemas"] = custom_schemas
        if emails is not None:
            self._values["emails"] = emails
        if external_ids is not None:
            self._values["external_ids"] = external_ids
        if hash_function is not None:
            self._values["hash_function"] = hash_function
        if ims is not None:
            self._values["ims"] = ims
        if include_in_global_address_list is not None:
            self._values["include_in_global_address_list"] = include_in_global_address_list
        if ip_allowlist is not None:
            self._values["ip_allowlist"] = ip_allowlist
        if is_admin is not None:
            self._values["is_admin"] = is_admin
        if keywords is not None:
            self._values["keywords"] = keywords
        if languages is not None:
            self._values["languages"] = languages
        if locations is not None:
            self._values["locations"] = locations
        if organizations is not None:
            self._values["organizations"] = organizations
        if org_unit_path is not None:
            self._values["org_unit_path"] = org_unit_path
        if password is not None:
            self._values["password"] = password
        if phones is not None:
            self._values["phones"] = phones
        if posix_accounts is not None:
            self._values["posix_accounts"] = posix_accounts
        if recovery_email is not None:
            self._values["recovery_email"] = recovery_email
        if recovery_phone is not None:
            self._values["recovery_phone"] = recovery_phone
        if relations is not None:
            self._values["relations"] = relations
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if suspended is not None:
            self._values["suspended"] = suspended
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if websites is not None:
            self._values["websites"] = websites

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
    def name(self) -> "UserName":
        '''name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#name User#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast("UserName", result)

    @builtins.property
    def primary_email(self) -> builtins.str:
        '''The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary_email User#primary_email}
        '''
        result = self._values.get("primary_email")
        assert result is not None, "Required property 'primary_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addresses(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserAddresses]]]:
        '''addresses block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#addresses User#addresses}
        '''
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserAddresses]]], result)

    @builtins.property
    def aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''asps.list of the user's alias email addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#aliases User#aliases}
        '''
        result = self._values.get("aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def archived(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if user is archived.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#archived User#archived}
        '''
        result = self._values.get("archived")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def change_password_at_next_login(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if the user is forced to change their password at next login.

        This setting doesn't apply when the user signs in via a third-party identity provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#change_password_at_next_login User#change_password_at_next_login}
        '''
        result = self._values.get("change_password_at_next_login")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_schemas(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserCustomSchemas"]]]:
        '''custom_schemas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_schemas User#custom_schemas}
        '''
        result = self._values.get("custom_schemas")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserCustomSchemas"]]], result)

    @builtins.property
    def emails(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserEmails"]]]:
        '''emails block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#emails User#emails}
        '''
        result = self._values.get("emails")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserEmails"]]], result)

    @builtins.property
    def external_ids(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserExternalIds"]]]:
        '''external_ids block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#external_ids User#external_ids}
        '''
        result = self._values.get("external_ids")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserExternalIds"]]], result)

    @builtins.property
    def hash_function(self) -> typing.Optional[builtins.str]:
        '''Stores the hash format of the password property.

        We recommend sending the password property value as a base 16 bit hexadecimal-encoded hash value. Set the hashFunction values as either the SHA-1, MD5, or crypt hash format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#hash_function User#hash_function}
        '''
        result = self._values.get("hash_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ims(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserIms"]]]:
        '''ims block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ims User#ims}
        '''
        result = self._values.get("ims")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserIms"]]], result)

    @builtins.property
    def include_in_global_address_list(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Indicates if the user's profile is visible in the Google Workspace global address list when the contact sharing feature is enabled for the domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#include_in_global_address_list User#include_in_global_address_list}
        '''
        result = self._values.get("include_in_global_address_list")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_allowlist(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the user's IP address is added to the allow list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ip_allowlist User#ip_allowlist}
        '''
        result = self._values.get("ip_allowlist")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_admin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates a user with super admininistrator privileges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#is_admin User#is_admin}
        '''
        result = self._values.get("is_admin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def keywords(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserKeywords"]]]:
        '''keywords block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#keywords User#keywords}
        '''
        result = self._values.get("keywords")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserKeywords"]]], result)

    @builtins.property
    def languages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLanguages"]]]:
        '''languages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#languages User#languages}
        '''
        result = self._values.get("languages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLanguages"]]], result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLocations"]]]:
        '''locations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#locations User#locations}
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserLocations"]]], result)

    @builtins.property
    def organizations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserOrganizations"]]]:
        '''organizations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#organizations User#organizations}
        '''
        result = self._values.get("organizations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserOrganizations"]]], result)

    @builtins.property
    def org_unit_path(self) -> typing.Optional[builtins.str]:
        '''The full path of the parent organization associated with the user.

        If the parent organization is the top-level, it is represented as a forward slash (/).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#org_unit_path User#org_unit_path}
        '''
        result = self._values.get("org_unit_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Stores the password for the user account.

        A password can contain any combination of ASCII characters. A minimum of 8 characters is required. The maximum length is 100 characters. As the API does not return the value of password, this field is write-only, and the value stored in the state will be what is provided in the configuration. The field is required on create and will be empty on import.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#password User#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phones(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPhones"]]]:
        '''phones block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#phones User#phones}
        '''
        result = self._values.get("phones")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPhones"]]], result)

    @builtins.property
    def posix_accounts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPosixAccounts"]]]:
        '''posix_accounts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#posix_accounts User#posix_accounts}
        '''
        result = self._values.get("posix_accounts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserPosixAccounts"]]], result)

    @builtins.property
    def recovery_email(self) -> typing.Optional[builtins.str]:
        '''Recovery email of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_email User#recovery_email}
        '''
        result = self._values.get("recovery_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_phone(self) -> typing.Optional[builtins.str]:
        '''Recovery phone of the user.

        The phone number must be in the E.164 format, starting with the plus sign (+). Example: +16506661212.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#recovery_phone User#recovery_phone}
        '''
        result = self._values.get("recovery_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserRelations"]]]:
        '''relations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#relations User#relations}
        '''
        result = self._values.get("relations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserRelations"]]], result)

    @builtins.property
    def ssh_public_keys(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserSshPublicKeys"]]]:
        '''ssh_public_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#ssh_public_keys User#ssh_public_keys}
        '''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserSshPublicKeys"]]], result)

    @builtins.property
    def suspended(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if user is suspended.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#suspended User#suspended}
        '''
        result = self._values.get("suspended")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["UserTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#timeouts User#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["UserTimeouts"], result)

    @builtins.property
    def websites(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserWebsites"]]]:
        '''websites block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#websites User#websites}
        '''
        result = self._values.get("websites")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["UserWebsites"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserCustomSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema_name": "schemaName", "schema_values": "schemaValues"},
)
class UserCustomSchemas:
    def __init__(
        self,
        *,
        schema_name: builtins.str,
        schema_values: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param schema_name: The name of the schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#schema_name User#schema_name}
        :param schema_values: JSON encoded map that represents key/value pairs that correspond to the given schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#schema_values User#schema_values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserCustomSchemas.__init__)
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument schema_values", value=schema_values, expected_type=type_hints["schema_values"])
        self._values: typing.Dict[str, typing.Any] = {
            "schema_name": schema_name,
            "schema_values": schema_values,
        }

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The name of the schema.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#schema_name User#schema_name}
        '''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_values(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''JSON encoded map that represents key/value pairs that correspond to the given schema.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#schema_values User#schema_values}
        '''
        result = self._values.get("schema_values")
        assert result is not None, "Required property 'schema_values' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserCustomSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserCustomSchemasList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserCustomSchemasList",
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
            type_hints = typing.get_type_hints(UserCustomSchemasList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserCustomSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserCustomSchemasList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserCustomSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserCustomSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserCustomSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserCustomSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserCustomSchemasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserCustomSchemasOutputReference",
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
            type_hints = typing.get_type_hints(UserCustomSchemasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaValuesInput")
    def schema_values_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "schemaValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasOutputReference, "schema_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="schemaValues")
    def schema_values(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "schemaValues"))

    @schema_values.setter
    def schema_values(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasOutputReference, "schema_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaValues", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserCustomSchemas, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserCustomSchemas, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserCustomSchemas, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserCustomSchemasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserEmails",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "address": "address",
        "custom_type": "customType",
        "primary": "primary",
    },
)
class UserEmails:
    def __init__(
        self,
        *,
        type: builtins.str,
        address: typing.Optional[builtins.str] = None,
        custom_type: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The type of the email account. Acceptable values: ``custom``, ``home``, ``other``, ``work``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param address: The user's email address. Also serves as the email ID. This value can be the user's primary email address or an alias. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#address User#address}
        :param custom_type: If the value of type is custom, this property contains the custom type string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param primary: Defaults to ``false``. Indicates if this is the user's primary email. Only one entry can be marked as primary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserEmails.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if address is not None:
            self._values["address"] = address
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the email account. Acceptable values: ``custom``, ``home``, ``other``, ``work``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The user's email address.

        Also serves as the email ID. This value can be the user's primary email address or an alias.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#address User#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the value of type is custom, this property contains the custom type string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``. Indicates if this is the user's primary email. Only one entry can be marked as primary.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserEmails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserEmailsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserEmailsList",
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
            type_hints = typing.get_type_hints(UserEmailsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserEmailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserEmailsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserEmailsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserEmailsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserEmailsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserEmails]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserEmails]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserEmails]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserEmailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserEmailsOutputReference",
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
            type_hints = typing.get_type_hints(UserEmailsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserEmails, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserEmails, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserEmails, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserEmailsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserExternalIds",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value", "custom_type": "customType"},
)
class UserExternalIds:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        custom_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of external ID. If set to custom, customType must also be set. Acceptable values: ``account``, ``custom``, ``customer``, ``login_id``, ``network``, ``organization``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param value: The value of the ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        :param custom_type: If the external ID type is custom, this property contains the custom value and must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserExternalIds.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if custom_type is not None:
            self._values["custom_type"] = custom_type

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of external ID.

        If set to custom, customType must also be set. Acceptable values: ``account``, ``custom``, ``customer``, ``login_id``, ``network``, ``organization``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the external ID type is custom, this property contains the custom value and must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserExternalIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserExternalIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserExternalIdsList",
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
            type_hints = typing.get_type_hints(UserExternalIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserExternalIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserExternalIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserExternalIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserExternalIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserExternalIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserExternalIds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserExternalIds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserExternalIds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserExternalIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserExternalIdsOutputReference",
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
            type_hints = typing.get_type_hints(UserExternalIdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserExternalIds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserExternalIds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserExternalIds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserExternalIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserIms",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "type": "type",
        "custom_protocol": "customProtocol",
        "custom_type": "customType",
        "im": "im",
        "primary": "primary",
    },
)
class UserIms:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        type: builtins.str,
        custom_protocol: typing.Optional[builtins.str] = None,
        custom_type: typing.Optional[builtins.str] = None,
        im: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param protocol: An IM protocol identifies the IM network. The value can be a custom network or the standard network. Acceptable values: ``aim``, ``custom_protocol``, ``gtalk``, ``icq``, ``jabber``, ``msn``, ``net_meeting``, ``qq``, ``skype``, ``yahoo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#protocol User#protocol}
        :param type: Acceptable values: ``custom``, ``home``, ``other``, ``work``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param custom_protocol: If the protocol value is custom_protocol, this property holds the custom protocol's string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_protocol User#custom_protocol}
        :param custom_type: If the IM type is custom, this property holds the custom type string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param im: The user's IM network ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#im User#im}
        :param primary: If this is the user's primary IM. Only one entry in the IM list can have a value of true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserIms.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument custom_protocol", value=custom_protocol, expected_type=type_hints["custom_protocol"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument im", value=im, expected_type=type_hints["im"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
            "type": type,
        }
        if custom_protocol is not None:
            self._values["custom_protocol"] = custom_protocol
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if im is not None:
            self._values["im"] = im
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def protocol(self) -> builtins.str:
        '''An IM protocol identifies the IM network.

        The value can be a custom network or the standard network. Acceptable values: ``aim``, ``custom_protocol``, ``gtalk``, ``icq``, ``jabber``, ``msn``, ``net_meeting``, ``qq``, ``skype``, ``yahoo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#protocol User#protocol}
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Acceptable values: ``custom``, ``home``, ``other``, ``work``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_protocol(self) -> typing.Optional[builtins.str]:
        '''If the protocol value is custom_protocol, this property holds the custom protocol's string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_protocol User#custom_protocol}
        '''
        result = self._values.get("custom_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the IM type is custom, this property holds the custom type string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def im(self) -> typing.Optional[builtins.str]:
        '''The user's IM network ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#im User#im}
        '''
        result = self._values.get("im")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this is the user's primary IM.

        Only one entry in the IM list can have a value of true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserIms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserImsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserImsList",
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
            type_hints = typing.get_type_hints(UserImsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserImsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserImsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserImsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserImsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserImsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserIms]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserIms]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserIms]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserImsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserImsOutputReference",
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
            type_hints = typing.get_type_hints(UserImsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomProtocol")
    def reset_custom_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProtocol", []))

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetIm")
    def reset_im(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIm", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="customProtocolInput")
    def custom_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="imInput")
    def im_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="customProtocol")
    def custom_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customProtocol"))

    @custom_protocol.setter
    def custom_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "custom_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="im")
    def im(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "im"))

    @im.setter
    def im(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "im").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "im", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserIms, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserIms, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserIms, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserImsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserKeywords",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value", "custom_type": "customType"},
)
class UserKeywords:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        custom_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Each entry can have a type which indicates standard type of that entry. For example, keyword could be of type occupation or outlook. In addition to the standard type, an entry can have a custom type and can give it any name. Such types should have the CUSTOM value as type and also have a customType value. Acceptable values: ``custom``, ``mission``, ``occupation``, ``outlook`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param value: Keyword. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        :param custom_type: Custom Type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserKeywords.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if custom_type is not None:
            self._values["custom_type"] = custom_type

    @builtins.property
    def type(self) -> builtins.str:
        '''Each entry can have a type which indicates standard type of that entry.

        For example, keyword could be of type occupation or outlook. In addition to the standard type, an entry can have a custom type and can give it any name. Such types should have the CUSTOM value as type and also have a customType value. Acceptable values: ``custom``, ``mission``, ``occupation``, ``outlook``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Keyword.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''Custom Type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserKeywords(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserKeywordsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserKeywordsList",
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
            type_hints = typing.get_type_hints(UserKeywordsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserKeywordsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserKeywordsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserKeywordsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserKeywordsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserKeywordsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserKeywords]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserKeywords]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserKeywords]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserKeywordsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserKeywordsOutputReference",
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
            type_hints = typing.get_type_hints(UserKeywordsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserKeywords, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserKeywords, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserKeywords, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserKeywordsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserLanguages",
    jsii_struct_bases=[],
    name_mapping={
        "custom_language": "customLanguage",
        "language_code": "languageCode",
        "preference": "preference",
    },
)
class UserLanguages:
    def __init__(
        self,
        *,
        custom_language: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        preference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_language: Other language. A user can provide their own language name if there is no corresponding Google III language code. If this is set, LanguageCode can't be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_language User#custom_language}
        :param language_code: Defaults to ``en``. Language Code. Should be used for storing Google III LanguageCode string representation for language. Illegal values cause SchemaException. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#language_code User#language_code}
        :param preference: Defaults to ``preferred``. If present, controls whether the specified languageCode is the user's preferred language. Allowed values are ``preferred`` and ``not_preferred``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#preference User#preference}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserLanguages.__init__)
            check_type(argname="argument custom_language", value=custom_language, expected_type=type_hints["custom_language"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_language is not None:
            self._values["custom_language"] = custom_language
        if language_code is not None:
            self._values["language_code"] = language_code
        if preference is not None:
            self._values["preference"] = preference

    @builtins.property
    def custom_language(self) -> typing.Optional[builtins.str]:
        '''Other language.

        A user can provide their own language name if there is no corresponding Google III language code. If this is set, LanguageCode can't be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_language User#custom_language}
        '''
        result = self._values.get("custom_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``en``.

        Language Code. Should be used for storing Google III LanguageCode string representation for language. Illegal values cause SchemaException.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#language_code User#language_code}
        '''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preference(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``preferred``.

        If present, controls whether the specified languageCode is the user's preferred language. Allowed values are ``preferred`` and ``not_preferred``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#preference User#preference}
        '''
        result = self._values.get("preference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserLanguages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserLanguagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserLanguagesList",
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
            type_hints = typing.get_type_hints(UserLanguagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserLanguagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserLanguagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserLanguagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserLanguagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserLanguagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLanguages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLanguages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLanguages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserLanguagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserLanguagesOutputReference",
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
            type_hints = typing.get_type_hints(UserLanguagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomLanguage")
    def reset_custom_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomLanguage", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetPreference")
    def reset_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreference", []))

    @builtins.property
    @jsii.member(jsii_name="customLanguageInput")
    def custom_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="preferenceInput")
    def preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="customLanguage")
    def custom_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customLanguage"))

    @custom_language.setter
    def custom_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesOutputReference, "custom_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesOutputReference, "language_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="preference")
    def preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preference"))

    @preference.setter
    def preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesOutputReference, "preference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserLanguages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserLanguages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserLanguages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLanguagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserLocations",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "area": "area",
        "building_id": "buildingId",
        "custom_type": "customType",
        "desk_code": "deskCode",
        "floor_name": "floorName",
        "floor_section": "floorSection",
    },
)
class UserLocations:
    def __init__(
        self,
        *,
        type: builtins.str,
        area: typing.Optional[builtins.str] = None,
        building_id: typing.Optional[builtins.str] = None,
        custom_type: typing.Optional[builtins.str] = None,
        desk_code: typing.Optional[builtins.str] = None,
        floor_name: typing.Optional[builtins.str] = None,
        floor_section: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The location type. Acceptable values: ``custom``, ``default``, ``desk``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param area: Textual location. This is most useful for display purposes to concisely describe the location. For example, Mountain View, CA or Near Seattle. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#area User#area}
        :param building_id: Building identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#building_id User#building_id}
        :param custom_type: If the location type is custom, this property contains the custom value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param desk_code: Most specific textual code of individual desk location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#desk_code User#desk_code}
        :param floor_name: Floor name/number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#floor_name User#floor_name}
        :param floor_section: Floor section. More specific location within the floor. For example, if a floor is divided into sections A, B, and C, this field would identify one of those values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#floor_section User#floor_section}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserLocations.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument area", value=area, expected_type=type_hints["area"])
            check_type(argname="argument building_id", value=building_id, expected_type=type_hints["building_id"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument desk_code", value=desk_code, expected_type=type_hints["desk_code"])
            check_type(argname="argument floor_name", value=floor_name, expected_type=type_hints["floor_name"])
            check_type(argname="argument floor_section", value=floor_section, expected_type=type_hints["floor_section"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if area is not None:
            self._values["area"] = area
        if building_id is not None:
            self._values["building_id"] = building_id
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if desk_code is not None:
            self._values["desk_code"] = desk_code
        if floor_name is not None:
            self._values["floor_name"] = floor_name
        if floor_section is not None:
            self._values["floor_section"] = floor_section

    @builtins.property
    def type(self) -> builtins.str:
        '''The location type. Acceptable values: ``custom``, ``default``, ``desk``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def area(self) -> typing.Optional[builtins.str]:
        '''Textual location.

        This is most useful for display purposes to concisely describe the location. For example, Mountain View, CA or Near Seattle.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#area User#area}
        '''
        result = self._values.get("area")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def building_id(self) -> typing.Optional[builtins.str]:
        '''Building identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#building_id User#building_id}
        '''
        result = self._values.get("building_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the location type is custom, this property contains the custom value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desk_code(self) -> typing.Optional[builtins.str]:
        '''Most specific textual code of individual desk location.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#desk_code User#desk_code}
        '''
        result = self._values.get("desk_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def floor_name(self) -> typing.Optional[builtins.str]:
        '''Floor name/number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#floor_name User#floor_name}
        '''
        result = self._values.get("floor_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def floor_section(self) -> typing.Optional[builtins.str]:
        '''Floor section.

        More specific location within the floor. For example, if a floor is divided into sections A, B, and C, this field would identify one of those values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#floor_section User#floor_section}
        '''
        result = self._values.get("floor_section")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserLocations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserLocationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserLocationsList",
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
            type_hints = typing.get_type_hints(UserLocationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserLocationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserLocationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserLocationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserLocationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserLocationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLocations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLocations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserLocations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserLocationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserLocationsOutputReference",
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
            type_hints = typing.get_type_hints(UserLocationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArea")
    def reset_area(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArea", []))

    @jsii.member(jsii_name="resetBuildingId")
    def reset_building_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildingId", []))

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetDeskCode")
    def reset_desk_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeskCode", []))

    @jsii.member(jsii_name="resetFloorName")
    def reset_floor_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFloorName", []))

    @jsii.member(jsii_name="resetFloorSection")
    def reset_floor_section(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFloorSection", []))

    @builtins.property
    @jsii.member(jsii_name="areaInput")
    def area_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "areaInput"))

    @builtins.property
    @jsii.member(jsii_name="buildingIdInput")
    def building_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildingIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deskCodeInput")
    def desk_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deskCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="floorNameInput")
    def floor_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "floorNameInput"))

    @builtins.property
    @jsii.member(jsii_name="floorSectionInput")
    def floor_section_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "floorSectionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="area")
    def area(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "area"))

    @area.setter
    def area(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "area").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "area", value)

    @builtins.property
    @jsii.member(jsii_name="buildingId")
    def building_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildingId"))

    @building_id.setter
    def building_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "building_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildingId", value)

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="deskCode")
    def desk_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deskCode"))

    @desk_code.setter
    def desk_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "desk_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deskCode", value)

    @builtins.property
    @jsii.member(jsii_name="floorName")
    def floor_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "floorName"))

    @floor_name.setter
    def floor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "floor_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "floorName", value)

    @builtins.property
    @jsii.member(jsii_name="floorSection")
    def floor_section(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "floorSection"))

    @floor_section.setter
    def floor_section(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "floor_section").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "floorSection", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserLocations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserLocations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserLocations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserLocationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserName",
    jsii_struct_bases=[],
    name_mapping={"family_name": "familyName", "given_name": "givenName"},
)
class UserName:
    def __init__(
        self,
        *,
        family_name: builtins.str,
        given_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param family_name: The user's last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#family_name User#family_name}
        :param given_name: The user's first name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#given_name User#given_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserName.__init__)
            check_type(argname="argument family_name", value=family_name, expected_type=type_hints["family_name"])
            check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "family_name": family_name,
        }
        if given_name is not None:
            self._values["given_name"] = given_name

    @builtins.property
    def family_name(self) -> builtins.str:
        '''The user's last name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#family_name User#family_name}
        '''
        result = self._values.get("family_name")
        assert result is not None, "Required property 'family_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''The user's first name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#given_name User#given_name}
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserNameOutputReference",
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
            type_hints = typing.get_type_hints(UserNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGivenName")
    def reset_given_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGivenName", []))

    @builtins.property
    @jsii.member(jsii_name="fullName")
    def full_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullName"))

    @builtins.property
    @jsii.member(jsii_name="familyNameInput")
    def family_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="givenNameInput")
    def given_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "givenNameInput"))

    @builtins.property
    @jsii.member(jsii_name="familyName")
    def family_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "familyName"))

    @family_name.setter
    def family_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserNameOutputReference, "family_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "familyName", value)

    @builtins.property
    @jsii.member(jsii_name="givenName")
    def given_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "givenName"))

    @given_name.setter
    def given_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserNameOutputReference, "given_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "givenName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UserName]:
        return typing.cast(typing.Optional[UserName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[UserName]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserOrganizations",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "cost_center": "costCenter",
        "custom_type": "customType",
        "department": "department",
        "description": "description",
        "domain": "domain",
        "full_time_equivalent": "fullTimeEquivalent",
        "location": "location",
        "name": "name",
        "primary": "primary",
        "symbol": "symbol",
        "title": "title",
    },
)
class UserOrganizations:
    def __init__(
        self,
        *,
        type: builtins.str,
        cost_center: typing.Optional[builtins.str] = None,
        custom_type: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        full_time_equivalent: typing.Optional[jsii.Number] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        symbol: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of organization. Acceptable values: ``domain_only``, ``school``, ``unknown``, ``work``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param cost_center: The cost center of the user's organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#cost_center User#cost_center}
        :param custom_type: If the value of type is custom, this property contains the custom value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param department: Specifies the department within the organization, such as sales or engineering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#department User#department}
        :param description: The description of the organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#description User#description}
        :param domain: The domain the organization belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#domain User#domain}
        :param full_time_equivalent: The full-time equivalent millipercent within the organization (100000 = 100%). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#full_time_equivalent User#full_time_equivalent}
        :param location: The physical location of the organization. This does not need to be a fully qualified address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#location User#location}
        :param name: The name of the organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#name User#name}
        :param primary: Indicates if this is the user's primary organization. A user may only have one primary organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        :param symbol: Text string symbol of the organization. For example, the text symbol for Google is GOOG. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#symbol User#symbol}
        :param title: The user's title within the organization. For example, member or engineer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#title User#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserOrganizations.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cost_center", value=cost_center, expected_type=type_hints["cost_center"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument department", value=department, expected_type=type_hints["department"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument full_time_equivalent", value=full_time_equivalent, expected_type=type_hints["full_time_equivalent"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument symbol", value=symbol, expected_type=type_hints["symbol"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if cost_center is not None:
            self._values["cost_center"] = cost_center
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if department is not None:
            self._values["department"] = department
        if description is not None:
            self._values["description"] = description
        if domain is not None:
            self._values["domain"] = domain
        if full_time_equivalent is not None:
            self._values["full_time_equivalent"] = full_time_equivalent
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if primary is not None:
            self._values["primary"] = primary
        if symbol is not None:
            self._values["symbol"] = symbol
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of organization. Acceptable values: ``domain_only``, ``school``, ``unknown``, ``work``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cost_center(self) -> typing.Optional[builtins.str]:
        '''The cost center of the user's organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#cost_center User#cost_center}
        '''
        result = self._values.get("cost_center")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the value of type is custom, this property contains the custom value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''Specifies the department within the organization, such as sales or engineering.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#department User#department}
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#description User#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain the organization belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#domain User#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def full_time_equivalent(self) -> typing.Optional[jsii.Number]:
        '''The full-time equivalent millipercent within the organization (100000 = 100%).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#full_time_equivalent User#full_time_equivalent}
        '''
        result = self._values.get("full_time_equivalent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The physical location of the organization. This does not need to be a fully qualified address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#location User#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#name User#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if this is the user's primary organization. A user may only have one primary organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def symbol(self) -> typing.Optional[builtins.str]:
        '''Text string symbol of the organization. For example, the text symbol for Google is GOOG.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#symbol User#symbol}
        '''
        result = self._values.get("symbol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The user's title within the organization. For example, member or engineer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#title User#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserOrganizations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserOrganizationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserOrganizationsList",
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
            type_hints = typing.get_type_hints(UserOrganizationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserOrganizationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserOrganizationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserOrganizationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserOrganizationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserOrganizationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserOrganizations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserOrganizations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserOrganizations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserOrganizationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserOrganizationsOutputReference",
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
            type_hints = typing.get_type_hints(UserOrganizationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCostCenter")
    def reset_cost_center(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCenter", []))

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetDepartment")
    def reset_department(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDepartment", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetFullTimeEquivalent")
    def reset_full_time_equivalent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullTimeEquivalent", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetSymbol")
    def reset_symbol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSymbol", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="costCenterInput")
    def cost_center_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "costCenterInput"))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="departmentInput")
    def department_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "departmentInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="fullTimeEquivalentInput")
    def full_time_equivalent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fullTimeEquivalentInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="symbolInput")
    def symbol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "symbolInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="costCenter")
    def cost_center(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "costCenter"))

    @cost_center.setter
    def cost_center(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "cost_center").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costCenter", value)

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="department")
    def department(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "department"))

    @department.setter
    def department(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "department").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "department", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="fullTimeEquivalent")
    def full_time_equivalent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullTimeEquivalent"))

    @full_time_equivalent.setter
    def full_time_equivalent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "full_time_equivalent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullTimeEquivalent", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="symbol")
    def symbol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "symbol"))

    @symbol.setter
    def symbol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "symbol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "symbol", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserOrganizations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserOrganizations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserOrganizations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserOrganizationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserPhones",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "value": "value",
        "custom_type": "customType",
        "primary": "primary",
    },
)
class UserPhones:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        custom_type: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The type of phone number. Acceptable values: ``assistant``, ``callback``, ``car``, ``company_main`` , ``custom``, ``grand_central``, ``home``, ``home_fax``, ``isdn``, ``main``, ``mobile``, ``other``, ``other_fax``, ``pager``, ``radio``, ``telex``, ``tty_tdd``, ``work``, ``work_fax``, ``work_mobile``, ``work_pager``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param value: A human-readable phone number. It may be in any telephone number format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        :param custom_type: If the phone number type is custom, this property contains the custom value and must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param primary: Indicates if this is the user's primary phone number. A user may only have one primary phone number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserPhones.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of phone number.

        Acceptable values: ``assistant``, ``callback``, ``car``, ``company_main`` , ``custom``, ``grand_central``, ``home``, ``home_fax``, ``isdn``, ``main``, ``mobile``, ``other``, ``other_fax``, ``pager``, ``radio``, ``telex``, ``tty_tdd``, ``work``, ``work_fax``, ``work_mobile``, ``work_pager``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''A human-readable phone number. It may be in any telephone number format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the phone number type is custom, this property contains the custom value and must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if this is the user's primary phone number. A user may only have one primary phone number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPhones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserPhonesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserPhonesList",
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
            type_hints = typing.get_type_hints(UserPhonesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserPhonesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserPhonesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserPhonesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserPhonesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserPhonesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPhones]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPhones]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPhones]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserPhonesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserPhonesOutputReference",
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
            type_hints = typing.get_type_hints(UserPhonesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserPhones, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserPhones, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserPhones, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPhonesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserPosixAccounts",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "gecos": "gecos",
        "gid": "gid",
        "home_directory": "homeDirectory",
        "operating_system_type": "operatingSystemType",
        "primary": "primary",
        "shell": "shell",
        "system_id": "systemId",
        "uid": "uid",
        "username": "username",
    },
)
class UserPosixAccounts:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        gecos: typing.Optional[builtins.str] = None,
        gid: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        operating_system_type: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shell: typing.Optional[builtins.str] = None,
        system_id: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: A POSIX account field identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#account_id User#account_id}
        :param gecos: The GECOS (user information) for this account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#gecos User#gecos}
        :param gid: The default group ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#gid User#gid}
        :param home_directory: The path to the home directory for this account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#home_directory User#home_directory}
        :param operating_system_type: The operating system type for this account. Acceptable values: ``linux``, ``unspecified``, ``windows``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#operating_system_type User#operating_system_type}
        :param primary: If this is user's primary account within the SystemId. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        :param shell: The path to the login shell for this account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#shell User#shell}
        :param system_id: System identifier for which account Username or Uid apply to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#system_id User#system_id}
        :param uid: The POSIX compliant user ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#uid User#uid}
        :param username: The username of the account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#username User#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserPosixAccounts.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument gecos", value=gecos, expected_type=type_hints["gecos"])
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument home_directory", value=home_directory, expected_type=type_hints["home_directory"])
            check_type(argname="argument operating_system_type", value=operating_system_type, expected_type=type_hints["operating_system_type"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument shell", value=shell, expected_type=type_hints["shell"])
            check_type(argname="argument system_id", value=system_id, expected_type=type_hints["system_id"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if gecos is not None:
            self._values["gecos"] = gecos
        if gid is not None:
            self._values["gid"] = gid
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if operating_system_type is not None:
            self._values["operating_system_type"] = operating_system_type
        if primary is not None:
            self._values["primary"] = primary
        if shell is not None:
            self._values["shell"] = shell
        if system_id is not None:
            self._values["system_id"] = system_id
        if uid is not None:
            self._values["uid"] = uid
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''A POSIX account field identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#account_id User#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gecos(self) -> typing.Optional[builtins.str]:
        '''The GECOS (user information) for this account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#gecos User#gecos}
        '''
        result = self._values.get("gecos")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gid(self) -> typing.Optional[builtins.str]:
        '''The default group ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#gid User#gid}
        '''
        result = self._values.get("gid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''The path to the home directory for this account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#home_directory User#home_directory}
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system_type(self) -> typing.Optional[builtins.str]:
        '''The operating system type for this account. Acceptable values: ``linux``, ``unspecified``, ``windows``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#operating_system_type User#operating_system_type}
        '''
        result = self._values.get("operating_system_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this is user's primary account within the SystemId.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def shell(self) -> typing.Optional[builtins.str]:
        '''The path to the login shell for this account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#shell User#shell}
        '''
        result = self._values.get("shell")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_id(self) -> typing.Optional[builtins.str]:
        '''System identifier for which account Username or Uid apply to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#system_id User#system_id}
        '''
        result = self._values.get("system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uid(self) -> typing.Optional[builtins.str]:
        '''The POSIX compliant user ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#uid User#uid}
        '''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username of the account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#username User#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPosixAccounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserPosixAccountsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserPosixAccountsList",
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
            type_hints = typing.get_type_hints(UserPosixAccountsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserPosixAccountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserPosixAccountsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserPosixAccountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPosixAccounts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPosixAccounts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserPosixAccounts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserPosixAccountsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserPosixAccountsOutputReference",
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
            type_hints = typing.get_type_hints(UserPosixAccountsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetGecos")
    def reset_gecos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGecos", []))

    @jsii.member(jsii_name="resetGid")
    def reset_gid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGid", []))

    @jsii.member(jsii_name="resetHomeDirectory")
    def reset_home_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDirectory", []))

    @jsii.member(jsii_name="resetOperatingSystemType")
    def reset_operating_system_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystemType", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetShell")
    def reset_shell(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShell", []))

    @jsii.member(jsii_name="resetSystemId")
    def reset_system_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemId", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="gecosInput")
    def gecos_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gecosInput"))

    @builtins.property
    @jsii.member(jsii_name="gidInput")
    def gid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gidInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryInput")
    def home_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemTypeInput")
    def operating_system_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="shellInput")
    def shell_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shellInput"))

    @builtins.property
    @jsii.member(jsii_name="systemIdInput")
    def system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "systemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="gecos")
    def gecos(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gecos"))

    @gecos.setter
    def gecos(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "gecos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gecos", value)

    @builtins.property
    @jsii.member(jsii_name="gid")
    def gid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gid"))

    @gid.setter
    def gid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "gid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gid", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "home_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystemType")
    def operating_system_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystemType"))

    @operating_system_type.setter
    def operating_system_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "operating_system_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystemType", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="shell")
    def shell(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shell"))

    @shell.setter
    def shell(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "shell").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shell", value)

    @builtins.property
    @jsii.member(jsii_name="systemId")
    def system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "systemId"))

    @system_id.setter
    def system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemId", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "uid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserPosixAccounts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserPosixAccounts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserPosixAccounts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPosixAccountsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserRelations",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value", "custom_type": "customType"},
)
class UserRelations:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        custom_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of relation. Acceptable values: ``admin_assistant``, ``assistant``, ``brother``, ``child``, ``custom``, ``domestic_partner``, ``dotted_line_manager``, ``exec_assistant``, ``father``, ``friend``, ``manager``, ``mother``, ``parent``, ``partner``, ``referred_by``, ``relative``, ``sister``, ``spouse``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param value: The name of the person the user is related to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        :param custom_type: If the value of type is custom, this property contains the custom type string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserRelations.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if custom_type is not None:
            self._values["custom_type"] = custom_type

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of relation.

        Acceptable values: ``admin_assistant``, ``assistant``, ``brother``, ``child``, ``custom``, ``domestic_partner``, ``dotted_line_manager``, ``exec_assistant``, ``father``, ``friend``, ``manager``, ``mother``, ``parent``, ``partner``, ``referred_by``, ``relative``, ``sister``, ``spouse``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The name of the person the user is related to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''If the value of type is custom, this property contains the custom type string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserRelations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserRelationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserRelationsList",
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
            type_hints = typing.get_type_hints(UserRelationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserRelationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserRelationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserRelationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserRelationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserRelationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserRelations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserRelations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserRelations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserRelationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserRelationsOutputReference",
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
            type_hints = typing.get_type_hints(UserRelationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserRelations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserRelations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserRelations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserRelationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserSshPublicKeys",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "expiration_time_usec": "expirationTimeUsec"},
)
class UserSshPublicKeys:
    def __init__(
        self,
        *,
        key: builtins.str,
        expiration_time_usec: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: An SSH public key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#key User#key}
        :param expiration_time_usec: An expiration time in microseconds since epoch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#expiration_time_usec User#expiration_time_usec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserSshPublicKeys.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument expiration_time_usec", value=expiration_time_usec, expected_type=type_hints["expiration_time_usec"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }
        if expiration_time_usec is not None:
            self._values["expiration_time_usec"] = expiration_time_usec

    @builtins.property
    def key(self) -> builtins.str:
        '''An SSH public key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#key User#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_time_usec(self) -> typing.Optional[builtins.str]:
        '''An expiration time in microseconds since epoch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#expiration_time_usec User#expiration_time_usec}
        '''
        result = self._values.get("expiration_time_usec")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserSshPublicKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserSshPublicKeysList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserSshPublicKeysList",
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
            type_hints = typing.get_type_hints(UserSshPublicKeysList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserSshPublicKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserSshPublicKeysList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserSshPublicKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserSshPublicKeys]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserSshPublicKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserSshPublicKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserSshPublicKeysOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserSshPublicKeysOutputReference",
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
            type_hints = typing.get_type_hints(UserSshPublicKeysOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpirationTimeUsec")
    def reset_expiration_time_usec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTimeUsec", []))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeUsecInput")
    def expiration_time_usec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationTimeUsecInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeUsec")
    def expiration_time_usec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTimeUsec"))

    @expiration_time_usec.setter
    def expiration_time_usec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysOutputReference, "expiration_time_usec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTimeUsec", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserSshPublicKeys, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserSshPublicKeys, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserSshPublicKeys, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserSshPublicKeysOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class UserTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#create User#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#update User#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#create User#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#update User#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(UserTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.user.UserWebsites",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "value": "value",
        "custom_type": "customType",
        "primary": "primary",
    },
)
class UserWebsites:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        custom_type: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The type or purpose of the website. For example, a website could be labeled as home or blog. Alternatively, an entry can have a custom type Custom types must have a customType value. Acceptable values: ``app_install_page``, ``blog``, ``custom``, ``ftp`` , ``home``, ``home_page``, ``other``, ``profile``, ``reservations``, ``resume``, ``work``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        :param value: The URL of the website. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        :param custom_type: The custom type. Only used if the type is custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        :param primary: If this is user's primary website or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserWebsites.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_type", value=custom_type, expected_type=type_hints["custom_type"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if custom_type is not None:
            self._values["custom_type"] = custom_type
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def type(self) -> builtins.str:
        '''The type or purpose of the website.

        For example, a website could be labeled as home or blog. Alternatively, an entry can have a custom type Custom types must have a customType value. Acceptable values: ``app_install_page``, ``blog``, ``custom``, ``ftp`` , ``home``, ``home_page``, ``other``, ``profile``, ``reservations``, ``resume``, ``work``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#type User#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The URL of the website.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_type(self) -> typing.Optional[builtins.str]:
        '''The custom type. Only used if the type is custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#custom_type User#custom_type}
        '''
        result = self._values.get("custom_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this is user's primary website or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/user#primary User#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserWebsites(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserWebsitesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserWebsitesList",
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
            type_hints = typing.get_type_hints(UserWebsitesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserWebsitesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserWebsitesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserWebsitesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(UserWebsitesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(UserWebsitesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserWebsites]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserWebsites]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[UserWebsites]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserWebsitesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.user.UserWebsitesOutputReference",
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
            type_hints = typing.get_type_hints(UserWebsitesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCustomType")
    def reset_custom_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomType", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="customTypeInput")
    def custom_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="customType")
    def custom_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customType"))

    @custom_type.setter
    def custom_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesOutputReference, "custom_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customType", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[UserWebsites, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[UserWebsites, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[UserWebsites, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserWebsitesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "User",
    "UserAddresses",
    "UserAddressesList",
    "UserAddressesOutputReference",
    "UserConfig",
    "UserCustomSchemas",
    "UserCustomSchemasList",
    "UserCustomSchemasOutputReference",
    "UserEmails",
    "UserEmailsList",
    "UserEmailsOutputReference",
    "UserExternalIds",
    "UserExternalIdsList",
    "UserExternalIdsOutputReference",
    "UserIms",
    "UserImsList",
    "UserImsOutputReference",
    "UserKeywords",
    "UserKeywordsList",
    "UserKeywordsOutputReference",
    "UserLanguages",
    "UserLanguagesList",
    "UserLanguagesOutputReference",
    "UserLocations",
    "UserLocationsList",
    "UserLocationsOutputReference",
    "UserName",
    "UserNameOutputReference",
    "UserOrganizations",
    "UserOrganizationsList",
    "UserOrganizationsOutputReference",
    "UserPhones",
    "UserPhonesList",
    "UserPhonesOutputReference",
    "UserPosixAccounts",
    "UserPosixAccountsList",
    "UserPosixAccountsOutputReference",
    "UserRelations",
    "UserRelationsList",
    "UserRelationsOutputReference",
    "UserSshPublicKeys",
    "UserSshPublicKeysList",
    "UserSshPublicKeysOutputReference",
    "UserTimeouts",
    "UserTimeoutsOutputReference",
    "UserWebsites",
    "UserWebsitesList",
    "UserWebsitesOutputReference",
]

publication.publish()
