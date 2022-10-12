'''
# `okta_policy_password`

Refer to the Terraform Registory for docs: [`okta_policy_password`](https://www.terraform.io/docs/providers/okta/r/policy_password).
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


class PolicyPassword(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.policyPassword.PolicyPassword",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/policy_password okta_policy_password}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        auth_provider: typing.Optional[builtins.str] = None,
        call_recovery: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        email_recovery: typing.Optional[builtins.str] = None,
        groups_included: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        password_auto_unlock_minutes: typing.Optional[jsii.Number] = None,
        password_dictionary_lookup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_first_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_last_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_expire_warn_days: typing.Optional[jsii.Number] = None,
        password_history_count: typing.Optional[jsii.Number] = None,
        password_lockout_notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_max_age_days: typing.Optional[jsii.Number] = None,
        password_max_lockout_attempts: typing.Optional[jsii.Number] = None,
        password_min_age_minutes: typing.Optional[jsii.Number] = None,
        password_min_length: typing.Optional[jsii.Number] = None,
        password_min_lowercase: typing.Optional[jsii.Number] = None,
        password_min_number: typing.Optional[jsii.Number] = None,
        password_min_symbol: typing.Optional[jsii.Number] = None,
        password_min_uppercase: typing.Optional[jsii.Number] = None,
        password_show_lockout_failures: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        priority: typing.Optional[jsii.Number] = None,
        question_min_length: typing.Optional[jsii.Number] = None,
        question_recovery: typing.Optional[builtins.str] = None,
        recovery_email_token: typing.Optional[jsii.Number] = None,
        skip_unlock: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sms_recovery: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/policy_password okta_policy_password} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Policy Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#name PolicyPassword#name}
        :param auth_provider: Authentication Provider: OKTA, ACTIVE_DIRECTORY or LDAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#auth_provider PolicyPassword#auth_provider}
        :param call_recovery: Enable or disable voice call recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#call_recovery PolicyPassword#call_recovery}
        :param description: Policy Description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#description PolicyPassword#description}
        :param email_recovery: Enable or disable email password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#email_recovery PolicyPassword#email_recovery}
        :param groups_included: List of Group IDs to Include. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#groups_included PolicyPassword#groups_included}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#id PolicyPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password_auto_unlock_minutes: Number of minutes before a locked account is unlocked: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_auto_unlock_minutes PolicyPassword#password_auto_unlock_minutes}
        :param password_dictionary_lookup: Check Passwords Against Common Password Dictionary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_dictionary_lookup PolicyPassword#password_dictionary_lookup}
        :param password_exclude_first_name: User firstName attribute must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_first_name PolicyPassword#password_exclude_first_name}
        :param password_exclude_last_name: User lastName attribute must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_last_name PolicyPassword#password_exclude_last_name}
        :param password_exclude_username: If the user name must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_username PolicyPassword#password_exclude_username}
        :param password_expire_warn_days: Length in days a user will be warned before password expiry: 0 = no warning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_expire_warn_days PolicyPassword#password_expire_warn_days}
        :param password_history_count: Number of distinct passwords that must be created before they can be reused: 0 = none. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_history_count PolicyPassword#password_history_count}
        :param password_lockout_notification_channels: Notification channels to use to notify a user when their account has been locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_lockout_notification_channels PolicyPassword#password_lockout_notification_channels}
        :param password_max_age_days: Length in days a password is valid before expiry: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_age_days PolicyPassword#password_max_age_days}
        :param password_max_lockout_attempts: Number of unsuccessful login attempts allowed before lockout: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_lockout_attempts PolicyPassword#password_max_lockout_attempts}
        :param password_min_age_minutes: Minimum time interval in minutes between password changes: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_age_minutes PolicyPassword#password_min_age_minutes}
        :param password_min_length: Minimum password length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_length PolicyPassword#password_min_length}
        :param password_min_lowercase: If a password must contain at least one lower case letter: 0 = no, 1 = yes. Default = 1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_lowercase PolicyPassword#password_min_lowercase}
        :param password_min_number: If a password must contain at least one number: 0 = no, 1 = yes. Default = 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_number PolicyPassword#password_min_number}
        :param password_min_symbol: If a password must contain at least one symbol (!@#$%^&*): 0 = no, 1 = yes. Default = 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_symbol PolicyPassword#password_min_symbol}
        :param password_min_uppercase: If a password must contain at least one upper case letter: 0 = no, 1 = yes. Default = 1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_uppercase PolicyPassword#password_min_uppercase}
        :param password_show_lockout_failures: If a user should be informed when their account is locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_show_lockout_failures PolicyPassword#password_show_lockout_failures}
        :param priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last (lowest) if not there. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#priority PolicyPassword#priority}
        :param question_min_length: Min length of the password recovery question answer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_min_length PolicyPassword#question_min_length}
        :param question_recovery: Enable or disable security question password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_recovery PolicyPassword#question_recovery}
        :param recovery_email_token: Lifetime in minutes of the recovery email token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#recovery_email_token PolicyPassword#recovery_email_token}
        :param skip_unlock: When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user's Windows account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#skip_unlock PolicyPassword#skip_unlock}
        :param sms_recovery: Enable or disable SMS password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#sms_recovery PolicyPassword#sms_recovery}
        :param status: Policy Status: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#status PolicyPassword#status}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PolicyPassword.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PolicyPasswordConfig(
            name=name,
            auth_provider=auth_provider,
            call_recovery=call_recovery,
            description=description,
            email_recovery=email_recovery,
            groups_included=groups_included,
            id=id,
            password_auto_unlock_minutes=password_auto_unlock_minutes,
            password_dictionary_lookup=password_dictionary_lookup,
            password_exclude_first_name=password_exclude_first_name,
            password_exclude_last_name=password_exclude_last_name,
            password_exclude_username=password_exclude_username,
            password_expire_warn_days=password_expire_warn_days,
            password_history_count=password_history_count,
            password_lockout_notification_channels=password_lockout_notification_channels,
            password_max_age_days=password_max_age_days,
            password_max_lockout_attempts=password_max_lockout_attempts,
            password_min_age_minutes=password_min_age_minutes,
            password_min_length=password_min_length,
            password_min_lowercase=password_min_lowercase,
            password_min_number=password_min_number,
            password_min_symbol=password_min_symbol,
            password_min_uppercase=password_min_uppercase,
            password_show_lockout_failures=password_show_lockout_failures,
            priority=priority,
            question_min_length=question_min_length,
            question_recovery=question_recovery,
            recovery_email_token=recovery_email_token,
            skip_unlock=skip_unlock,
            sms_recovery=sms_recovery,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAuthProvider")
    def reset_auth_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthProvider", []))

    @jsii.member(jsii_name="resetCallRecovery")
    def reset_call_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCallRecovery", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEmailRecovery")
    def reset_email_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailRecovery", []))

    @jsii.member(jsii_name="resetGroupsIncluded")
    def reset_groups_included(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupsIncluded", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPasswordAutoUnlockMinutes")
    def reset_password_auto_unlock_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordAutoUnlockMinutes", []))

    @jsii.member(jsii_name="resetPasswordDictionaryLookup")
    def reset_password_dictionary_lookup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordDictionaryLookup", []))

    @jsii.member(jsii_name="resetPasswordExcludeFirstName")
    def reset_password_exclude_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExcludeFirstName", []))

    @jsii.member(jsii_name="resetPasswordExcludeLastName")
    def reset_password_exclude_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExcludeLastName", []))

    @jsii.member(jsii_name="resetPasswordExcludeUsername")
    def reset_password_exclude_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExcludeUsername", []))

    @jsii.member(jsii_name="resetPasswordExpireWarnDays")
    def reset_password_expire_warn_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExpireWarnDays", []))

    @jsii.member(jsii_name="resetPasswordHistoryCount")
    def reset_password_history_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordHistoryCount", []))

    @jsii.member(jsii_name="resetPasswordLockoutNotificationChannels")
    def reset_password_lockout_notification_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordLockoutNotificationChannels", []))

    @jsii.member(jsii_name="resetPasswordMaxAgeDays")
    def reset_password_max_age_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMaxAgeDays", []))

    @jsii.member(jsii_name="resetPasswordMaxLockoutAttempts")
    def reset_password_max_lockout_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMaxLockoutAttempts", []))

    @jsii.member(jsii_name="resetPasswordMinAgeMinutes")
    def reset_password_min_age_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinAgeMinutes", []))

    @jsii.member(jsii_name="resetPasswordMinLength")
    def reset_password_min_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinLength", []))

    @jsii.member(jsii_name="resetPasswordMinLowercase")
    def reset_password_min_lowercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinLowercase", []))

    @jsii.member(jsii_name="resetPasswordMinNumber")
    def reset_password_min_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinNumber", []))

    @jsii.member(jsii_name="resetPasswordMinSymbol")
    def reset_password_min_symbol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinSymbol", []))

    @jsii.member(jsii_name="resetPasswordMinUppercase")
    def reset_password_min_uppercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordMinUppercase", []))

    @jsii.member(jsii_name="resetPasswordShowLockoutFailures")
    def reset_password_show_lockout_failures(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordShowLockoutFailures", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetQuestionMinLength")
    def reset_question_min_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuestionMinLength", []))

    @jsii.member(jsii_name="resetQuestionRecovery")
    def reset_question_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuestionRecovery", []))

    @jsii.member(jsii_name="resetRecoveryEmailToken")
    def reset_recovery_email_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryEmailToken", []))

    @jsii.member(jsii_name="resetSkipUnlock")
    def reset_skip_unlock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipUnlock", []))

    @jsii.member(jsii_name="resetSmsRecovery")
    def reset_sms_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsRecovery", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authProviderInput")
    def auth_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="callRecoveryInput")
    def call_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailRecoveryInput")
    def email_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsIncludedInput")
    def groups_included_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsIncludedInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordAutoUnlockMinutesInput")
    def password_auto_unlock_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordAutoUnlockMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordDictionaryLookupInput")
    def password_dictionary_lookup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "passwordDictionaryLookupInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeFirstNameInput")
    def password_exclude_first_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "passwordExcludeFirstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeLastNameInput")
    def password_exclude_last_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "passwordExcludeLastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeUsernameInput")
    def password_exclude_username_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "passwordExcludeUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpireWarnDaysInput")
    def password_expire_warn_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordExpireWarnDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordHistoryCountInput")
    def password_history_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordHistoryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordLockoutNotificationChannelsInput")
    def password_lockout_notification_channels_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "passwordLockoutNotificationChannelsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMaxAgeDaysInput")
    def password_max_age_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMaxAgeDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMaxLockoutAttemptsInput")
    def password_max_lockout_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMaxLockoutAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinAgeMinutesInput")
    def password_min_age_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinAgeMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinLengthInput")
    def password_min_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinLowercaseInput")
    def password_min_lowercase_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinLowercaseInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinNumberInput")
    def password_min_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinSymbolInput")
    def password_min_symbol_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinSymbolInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordMinUppercaseInput")
    def password_min_uppercase_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordMinUppercaseInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordShowLockoutFailuresInput")
    def password_show_lockout_failures_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "passwordShowLockoutFailuresInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="questionMinLengthInput")
    def question_min_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "questionMinLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="questionRecoveryInput")
    def question_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "questionRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryEmailTokenInput")
    def recovery_email_token_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recoveryEmailTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="skipUnlockInput")
    def skip_unlock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipUnlockInput"))

    @builtins.property
    @jsii.member(jsii_name="smsRecoveryInput")
    def sms_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smsRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="authProvider")
    def auth_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authProvider"))

    @auth_provider.setter
    def auth_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "auth_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authProvider", value)

    @builtins.property
    @jsii.member(jsii_name="callRecovery")
    def call_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callRecovery"))

    @call_recovery.setter
    def call_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "call_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="emailRecovery")
    def email_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailRecovery"))

    @email_recovery.setter
    def email_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "email_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="groupsIncluded")
    def groups_included(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupsIncluded"))

    @groups_included.setter
    def groups_included(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "groups_included").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupsIncluded", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="passwordAutoUnlockMinutes")
    def password_auto_unlock_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordAutoUnlockMinutes"))

    @password_auto_unlock_minutes.setter
    def password_auto_unlock_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_auto_unlock_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordAutoUnlockMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="passwordDictionaryLookup")
    def password_dictionary_lookup(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "passwordDictionaryLookup"))

    @password_dictionary_lookup.setter
    def password_dictionary_lookup(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_dictionary_lookup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordDictionaryLookup", value)

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeFirstName")
    def password_exclude_first_name(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "passwordExcludeFirstName"))

    @password_exclude_first_name.setter
    def password_exclude_first_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_exclude_first_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExcludeFirstName", value)

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeLastName")
    def password_exclude_last_name(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "passwordExcludeLastName"))

    @password_exclude_last_name.setter
    def password_exclude_last_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_exclude_last_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExcludeLastName", value)

    @builtins.property
    @jsii.member(jsii_name="passwordExcludeUsername")
    def password_exclude_username(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "passwordExcludeUsername"))

    @password_exclude_username.setter
    def password_exclude_username(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_exclude_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExcludeUsername", value)

    @builtins.property
    @jsii.member(jsii_name="passwordExpireWarnDays")
    def password_expire_warn_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordExpireWarnDays"))

    @password_expire_warn_days.setter
    def password_expire_warn_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_expire_warn_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExpireWarnDays", value)

    @builtins.property
    @jsii.member(jsii_name="passwordHistoryCount")
    def password_history_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordHistoryCount"))

    @password_history_count.setter
    def password_history_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_history_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordHistoryCount", value)

    @builtins.property
    @jsii.member(jsii_name="passwordLockoutNotificationChannels")
    def password_lockout_notification_channels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "passwordLockoutNotificationChannels"))

    @password_lockout_notification_channels.setter
    def password_lockout_notification_channels(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_lockout_notification_channels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordLockoutNotificationChannels", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMaxAgeDays")
    def password_max_age_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMaxAgeDays"))

    @password_max_age_days.setter
    def password_max_age_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_max_age_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMaxAgeDays", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMaxLockoutAttempts")
    def password_max_lockout_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMaxLockoutAttempts"))

    @password_max_lockout_attempts.setter
    def password_max_lockout_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_max_lockout_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMaxLockoutAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinAgeMinutes")
    def password_min_age_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinAgeMinutes"))

    @password_min_age_minutes.setter
    def password_min_age_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_age_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinAgeMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinLength")
    def password_min_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinLength"))

    @password_min_length.setter
    def password_min_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinLength", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinLowercase")
    def password_min_lowercase(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinLowercase"))

    @password_min_lowercase.setter
    def password_min_lowercase(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_lowercase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinLowercase", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinNumber")
    def password_min_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinNumber"))

    @password_min_number.setter
    def password_min_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinNumber", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinSymbol")
    def password_min_symbol(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinSymbol"))

    @password_min_symbol.setter
    def password_min_symbol(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_symbol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinSymbol", value)

    @builtins.property
    @jsii.member(jsii_name="passwordMinUppercase")
    def password_min_uppercase(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordMinUppercase"))

    @password_min_uppercase.setter
    def password_min_uppercase(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_min_uppercase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordMinUppercase", value)

    @builtins.property
    @jsii.member(jsii_name="passwordShowLockoutFailures")
    def password_show_lockout_failures(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "passwordShowLockoutFailures"))

    @password_show_lockout_failures.setter
    def password_show_lockout_failures(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "password_show_lockout_failures").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordShowLockoutFailures", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="questionMinLength")
    def question_min_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "questionMinLength"))

    @question_min_length.setter
    def question_min_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "question_min_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "questionMinLength", value)

    @builtins.property
    @jsii.member(jsii_name="questionRecovery")
    def question_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "questionRecovery"))

    @question_recovery.setter
    def question_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "question_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "questionRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryEmailToken")
    def recovery_email_token(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "recoveryEmailToken"))

    @recovery_email_token.setter
    def recovery_email_token(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "recovery_email_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryEmailToken", value)

    @builtins.property
    @jsii.member(jsii_name="skipUnlock")
    def skip_unlock(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipUnlock"))

    @skip_unlock.setter
    def skip_unlock(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "skip_unlock").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipUnlock", value)

    @builtins.property
    @jsii.member(jsii_name="smsRecovery")
    def sms_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smsRecovery"))

    @sms_recovery.setter
    def sms_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "sms_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smsRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicyPassword, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.policyPassword.PolicyPasswordConfig",
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
        "auth_provider": "authProvider",
        "call_recovery": "callRecovery",
        "description": "description",
        "email_recovery": "emailRecovery",
        "groups_included": "groupsIncluded",
        "id": "id",
        "password_auto_unlock_minutes": "passwordAutoUnlockMinutes",
        "password_dictionary_lookup": "passwordDictionaryLookup",
        "password_exclude_first_name": "passwordExcludeFirstName",
        "password_exclude_last_name": "passwordExcludeLastName",
        "password_exclude_username": "passwordExcludeUsername",
        "password_expire_warn_days": "passwordExpireWarnDays",
        "password_history_count": "passwordHistoryCount",
        "password_lockout_notification_channels": "passwordLockoutNotificationChannels",
        "password_max_age_days": "passwordMaxAgeDays",
        "password_max_lockout_attempts": "passwordMaxLockoutAttempts",
        "password_min_age_minutes": "passwordMinAgeMinutes",
        "password_min_length": "passwordMinLength",
        "password_min_lowercase": "passwordMinLowercase",
        "password_min_number": "passwordMinNumber",
        "password_min_symbol": "passwordMinSymbol",
        "password_min_uppercase": "passwordMinUppercase",
        "password_show_lockout_failures": "passwordShowLockoutFailures",
        "priority": "priority",
        "question_min_length": "questionMinLength",
        "question_recovery": "questionRecovery",
        "recovery_email_token": "recoveryEmailToken",
        "skip_unlock": "skipUnlock",
        "sms_recovery": "smsRecovery",
        "status": "status",
    },
)
class PolicyPasswordConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        auth_provider: typing.Optional[builtins.str] = None,
        call_recovery: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        email_recovery: typing.Optional[builtins.str] = None,
        groups_included: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        password_auto_unlock_minutes: typing.Optional[jsii.Number] = None,
        password_dictionary_lookup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_first_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_last_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_exclude_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_expire_warn_days: typing.Optional[jsii.Number] = None,
        password_history_count: typing.Optional[jsii.Number] = None,
        password_lockout_notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_max_age_days: typing.Optional[jsii.Number] = None,
        password_max_lockout_attempts: typing.Optional[jsii.Number] = None,
        password_min_age_minutes: typing.Optional[jsii.Number] = None,
        password_min_length: typing.Optional[jsii.Number] = None,
        password_min_lowercase: typing.Optional[jsii.Number] = None,
        password_min_number: typing.Optional[jsii.Number] = None,
        password_min_symbol: typing.Optional[jsii.Number] = None,
        password_min_uppercase: typing.Optional[jsii.Number] = None,
        password_show_lockout_failures: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        priority: typing.Optional[jsii.Number] = None,
        question_min_length: typing.Optional[jsii.Number] = None,
        question_recovery: typing.Optional[builtins.str] = None,
        recovery_email_token: typing.Optional[jsii.Number] = None,
        skip_unlock: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sms_recovery: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Policy Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#name PolicyPassword#name}
        :param auth_provider: Authentication Provider: OKTA, ACTIVE_DIRECTORY or LDAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#auth_provider PolicyPassword#auth_provider}
        :param call_recovery: Enable or disable voice call recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#call_recovery PolicyPassword#call_recovery}
        :param description: Policy Description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#description PolicyPassword#description}
        :param email_recovery: Enable or disable email password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#email_recovery PolicyPassword#email_recovery}
        :param groups_included: List of Group IDs to Include. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#groups_included PolicyPassword#groups_included}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#id PolicyPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password_auto_unlock_minutes: Number of minutes before a locked account is unlocked: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_auto_unlock_minutes PolicyPassword#password_auto_unlock_minutes}
        :param password_dictionary_lookup: Check Passwords Against Common Password Dictionary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_dictionary_lookup PolicyPassword#password_dictionary_lookup}
        :param password_exclude_first_name: User firstName attribute must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_first_name PolicyPassword#password_exclude_first_name}
        :param password_exclude_last_name: User lastName attribute must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_last_name PolicyPassword#password_exclude_last_name}
        :param password_exclude_username: If the user name must be excluded from the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_username PolicyPassword#password_exclude_username}
        :param password_expire_warn_days: Length in days a user will be warned before password expiry: 0 = no warning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_expire_warn_days PolicyPassword#password_expire_warn_days}
        :param password_history_count: Number of distinct passwords that must be created before they can be reused: 0 = none. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_history_count PolicyPassword#password_history_count}
        :param password_lockout_notification_channels: Notification channels to use to notify a user when their account has been locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_lockout_notification_channels PolicyPassword#password_lockout_notification_channels}
        :param password_max_age_days: Length in days a password is valid before expiry: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_age_days PolicyPassword#password_max_age_days}
        :param password_max_lockout_attempts: Number of unsuccessful login attempts allowed before lockout: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_lockout_attempts PolicyPassword#password_max_lockout_attempts}
        :param password_min_age_minutes: Minimum time interval in minutes between password changes: 0 = no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_age_minutes PolicyPassword#password_min_age_minutes}
        :param password_min_length: Minimum password length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_length PolicyPassword#password_min_length}
        :param password_min_lowercase: If a password must contain at least one lower case letter: 0 = no, 1 = yes. Default = 1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_lowercase PolicyPassword#password_min_lowercase}
        :param password_min_number: If a password must contain at least one number: 0 = no, 1 = yes. Default = 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_number PolicyPassword#password_min_number}
        :param password_min_symbol: If a password must contain at least one symbol (!@#$%^&*): 0 = no, 1 = yes. Default = 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_symbol PolicyPassword#password_min_symbol}
        :param password_min_uppercase: If a password must contain at least one upper case letter: 0 = no, 1 = yes. Default = 1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_uppercase PolicyPassword#password_min_uppercase}
        :param password_show_lockout_failures: If a user should be informed when their account is locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_show_lockout_failures PolicyPassword#password_show_lockout_failures}
        :param priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last (lowest) if not there. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#priority PolicyPassword#priority}
        :param question_min_length: Min length of the password recovery question answer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_min_length PolicyPassword#question_min_length}
        :param question_recovery: Enable or disable security question password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_recovery PolicyPassword#question_recovery}
        :param recovery_email_token: Lifetime in minutes of the recovery email token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#recovery_email_token PolicyPassword#recovery_email_token}
        :param skip_unlock: When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user's Windows account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#skip_unlock PolicyPassword#skip_unlock}
        :param sms_recovery: Enable or disable SMS password recovery: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#sms_recovery PolicyPassword#sms_recovery}
        :param status: Policy Status: ACTIVE or INACTIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#status PolicyPassword#status}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(PolicyPasswordConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auth_provider", value=auth_provider, expected_type=type_hints["auth_provider"])
            check_type(argname="argument call_recovery", value=call_recovery, expected_type=type_hints["call_recovery"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument email_recovery", value=email_recovery, expected_type=type_hints["email_recovery"])
            check_type(argname="argument groups_included", value=groups_included, expected_type=type_hints["groups_included"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password_auto_unlock_minutes", value=password_auto_unlock_minutes, expected_type=type_hints["password_auto_unlock_minutes"])
            check_type(argname="argument password_dictionary_lookup", value=password_dictionary_lookup, expected_type=type_hints["password_dictionary_lookup"])
            check_type(argname="argument password_exclude_first_name", value=password_exclude_first_name, expected_type=type_hints["password_exclude_first_name"])
            check_type(argname="argument password_exclude_last_name", value=password_exclude_last_name, expected_type=type_hints["password_exclude_last_name"])
            check_type(argname="argument password_exclude_username", value=password_exclude_username, expected_type=type_hints["password_exclude_username"])
            check_type(argname="argument password_expire_warn_days", value=password_expire_warn_days, expected_type=type_hints["password_expire_warn_days"])
            check_type(argname="argument password_history_count", value=password_history_count, expected_type=type_hints["password_history_count"])
            check_type(argname="argument password_lockout_notification_channels", value=password_lockout_notification_channels, expected_type=type_hints["password_lockout_notification_channels"])
            check_type(argname="argument password_max_age_days", value=password_max_age_days, expected_type=type_hints["password_max_age_days"])
            check_type(argname="argument password_max_lockout_attempts", value=password_max_lockout_attempts, expected_type=type_hints["password_max_lockout_attempts"])
            check_type(argname="argument password_min_age_minutes", value=password_min_age_minutes, expected_type=type_hints["password_min_age_minutes"])
            check_type(argname="argument password_min_length", value=password_min_length, expected_type=type_hints["password_min_length"])
            check_type(argname="argument password_min_lowercase", value=password_min_lowercase, expected_type=type_hints["password_min_lowercase"])
            check_type(argname="argument password_min_number", value=password_min_number, expected_type=type_hints["password_min_number"])
            check_type(argname="argument password_min_symbol", value=password_min_symbol, expected_type=type_hints["password_min_symbol"])
            check_type(argname="argument password_min_uppercase", value=password_min_uppercase, expected_type=type_hints["password_min_uppercase"])
            check_type(argname="argument password_show_lockout_failures", value=password_show_lockout_failures, expected_type=type_hints["password_show_lockout_failures"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument question_min_length", value=question_min_length, expected_type=type_hints["question_min_length"])
            check_type(argname="argument question_recovery", value=question_recovery, expected_type=type_hints["question_recovery"])
            check_type(argname="argument recovery_email_token", value=recovery_email_token, expected_type=type_hints["recovery_email_token"])
            check_type(argname="argument skip_unlock", value=skip_unlock, expected_type=type_hints["skip_unlock"])
            check_type(argname="argument sms_recovery", value=sms_recovery, expected_type=type_hints["sms_recovery"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if auth_provider is not None:
            self._values["auth_provider"] = auth_provider
        if call_recovery is not None:
            self._values["call_recovery"] = call_recovery
        if description is not None:
            self._values["description"] = description
        if email_recovery is not None:
            self._values["email_recovery"] = email_recovery
        if groups_included is not None:
            self._values["groups_included"] = groups_included
        if id is not None:
            self._values["id"] = id
        if password_auto_unlock_minutes is not None:
            self._values["password_auto_unlock_minutes"] = password_auto_unlock_minutes
        if password_dictionary_lookup is not None:
            self._values["password_dictionary_lookup"] = password_dictionary_lookup
        if password_exclude_first_name is not None:
            self._values["password_exclude_first_name"] = password_exclude_first_name
        if password_exclude_last_name is not None:
            self._values["password_exclude_last_name"] = password_exclude_last_name
        if password_exclude_username is not None:
            self._values["password_exclude_username"] = password_exclude_username
        if password_expire_warn_days is not None:
            self._values["password_expire_warn_days"] = password_expire_warn_days
        if password_history_count is not None:
            self._values["password_history_count"] = password_history_count
        if password_lockout_notification_channels is not None:
            self._values["password_lockout_notification_channels"] = password_lockout_notification_channels
        if password_max_age_days is not None:
            self._values["password_max_age_days"] = password_max_age_days
        if password_max_lockout_attempts is not None:
            self._values["password_max_lockout_attempts"] = password_max_lockout_attempts
        if password_min_age_minutes is not None:
            self._values["password_min_age_minutes"] = password_min_age_minutes
        if password_min_length is not None:
            self._values["password_min_length"] = password_min_length
        if password_min_lowercase is not None:
            self._values["password_min_lowercase"] = password_min_lowercase
        if password_min_number is not None:
            self._values["password_min_number"] = password_min_number
        if password_min_symbol is not None:
            self._values["password_min_symbol"] = password_min_symbol
        if password_min_uppercase is not None:
            self._values["password_min_uppercase"] = password_min_uppercase
        if password_show_lockout_failures is not None:
            self._values["password_show_lockout_failures"] = password_show_lockout_failures
        if priority is not None:
            self._values["priority"] = priority
        if question_min_length is not None:
            self._values["question_min_length"] = question_min_length
        if question_recovery is not None:
            self._values["question_recovery"] = question_recovery
        if recovery_email_token is not None:
            self._values["recovery_email_token"] = recovery_email_token
        if skip_unlock is not None:
            self._values["skip_unlock"] = skip_unlock
        if sms_recovery is not None:
            self._values["sms_recovery"] = sms_recovery
        if status is not None:
            self._values["status"] = status

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
    def name(self) -> builtins.str:
        '''Policy Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#name PolicyPassword#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_provider(self) -> typing.Optional[builtins.str]:
        '''Authentication Provider: OKTA, ACTIVE_DIRECTORY or LDAP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#auth_provider PolicyPassword#auth_provider}
        '''
        result = self._values.get("auth_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def call_recovery(self) -> typing.Optional[builtins.str]:
        '''Enable or disable voice call recovery: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#call_recovery PolicyPassword#call_recovery}
        '''
        result = self._values.get("call_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Policy Description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#description PolicyPassword#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_recovery(self) -> typing.Optional[builtins.str]:
        '''Enable or disable email password recovery: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#email_recovery PolicyPassword#email_recovery}
        '''
        result = self._values.get("email_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups_included(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Group IDs to Include.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#groups_included PolicyPassword#groups_included}
        '''
        result = self._values.get("groups_included")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#id PolicyPassword#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_auto_unlock_minutes(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes before a locked account is unlocked: 0 = no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_auto_unlock_minutes PolicyPassword#password_auto_unlock_minutes}
        '''
        result = self._values.get("password_auto_unlock_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_dictionary_lookup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Check Passwords Against Common Password Dictionary.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_dictionary_lookup PolicyPassword#password_dictionary_lookup}
        '''
        result = self._values.get("password_dictionary_lookup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_exclude_first_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''User firstName attribute must be excluded from the password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_first_name PolicyPassword#password_exclude_first_name}
        '''
        result = self._values.get("password_exclude_first_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_exclude_last_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''User lastName attribute must be excluded from the password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_last_name PolicyPassword#password_exclude_last_name}
        '''
        result = self._values.get("password_exclude_last_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_exclude_username(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the user name must be excluded from the password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_exclude_username PolicyPassword#password_exclude_username}
        '''
        result = self._values.get("password_exclude_username")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_expire_warn_days(self) -> typing.Optional[jsii.Number]:
        '''Length in days a user will be warned before password expiry: 0 = no warning.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_expire_warn_days PolicyPassword#password_expire_warn_days}
        '''
        result = self._values.get("password_expire_warn_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_history_count(self) -> typing.Optional[jsii.Number]:
        '''Number of distinct passwords that must be created before they can be reused: 0 = none.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_history_count PolicyPassword#password_history_count}
        '''
        result = self._values.get("password_history_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_lockout_notification_channels(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Notification channels to use to notify a user when their account has been locked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_lockout_notification_channels PolicyPassword#password_lockout_notification_channels}
        '''
        result = self._values.get("password_lockout_notification_channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def password_max_age_days(self) -> typing.Optional[jsii.Number]:
        '''Length in days a password is valid before expiry: 0 = no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_age_days PolicyPassword#password_max_age_days}
        '''
        result = self._values.get("password_max_age_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_max_lockout_attempts(self) -> typing.Optional[jsii.Number]:
        '''Number of unsuccessful login attempts allowed before lockout: 0 = no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_max_lockout_attempts PolicyPassword#password_max_lockout_attempts}
        '''
        result = self._values.get("password_max_lockout_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_age_minutes(self) -> typing.Optional[jsii.Number]:
        '''Minimum time interval in minutes between password changes: 0 = no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_age_minutes PolicyPassword#password_min_age_minutes}
        '''
        result = self._values.get("password_min_age_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_length(self) -> typing.Optional[jsii.Number]:
        '''Minimum password length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_length PolicyPassword#password_min_length}
        '''
        result = self._values.get("password_min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_lowercase(self) -> typing.Optional[jsii.Number]:
        '''If a password must contain at least one lower case letter: 0 = no, 1 = yes.

        Default = 1

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_lowercase PolicyPassword#password_min_lowercase}
        '''
        result = self._values.get("password_min_lowercase")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_number(self) -> typing.Optional[jsii.Number]:
        '''If a password must contain at least one number: 0 = no, 1 = yes. Default = 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_number PolicyPassword#password_min_number}
        '''
        result = self._values.get("password_min_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_symbol(self) -> typing.Optional[jsii.Number]:
        '''If a password must contain at least one symbol (!@#$%^&*): 0 = no, 1 = yes. Default = 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_symbol PolicyPassword#password_min_symbol}
        '''
        result = self._values.get("password_min_symbol")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_min_uppercase(self) -> typing.Optional[jsii.Number]:
        '''If a password must contain at least one upper case letter: 0 = no, 1 = yes.

        Default = 1

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_min_uppercase PolicyPassword#password_min_uppercase}
        '''
        result = self._values.get("password_min_uppercase")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_show_lockout_failures(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If a user should be informed when their account is locked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#password_show_lockout_failures PolicyPassword#password_show_lockout_failures}
        '''
        result = self._values.get("password_show_lockout_failures")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Policy Priority, this attribute can be set to a valid priority.

        To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last (lowest) if not there.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#priority PolicyPassword#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def question_min_length(self) -> typing.Optional[jsii.Number]:
        '''Min length of the password recovery question answer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_min_length PolicyPassword#question_min_length}
        '''
        result = self._values.get("question_min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def question_recovery(self) -> typing.Optional[builtins.str]:
        '''Enable or disable security question password recovery: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#question_recovery PolicyPassword#question_recovery}
        '''
        result = self._values.get("question_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_email_token(self) -> typing.Optional[jsii.Number]:
        '''Lifetime in minutes of the recovery email token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#recovery_email_token PolicyPassword#recovery_email_token}
        '''
        result = self._values.get("recovery_email_token")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_unlock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user's Windows account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#skip_unlock PolicyPassword#skip_unlock}
        '''
        result = self._values.get("skip_unlock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sms_recovery(self) -> typing.Optional[builtins.str]:
        '''Enable or disable SMS password recovery: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#sms_recovery PolicyPassword#sms_recovery}
        '''
        result = self._values.get("sms_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Policy Status: ACTIVE or INACTIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/policy_password#status PolicyPassword#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyPasswordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PolicyPassword",
    "PolicyPasswordConfig",
]

publication.publish()
