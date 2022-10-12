'''
# `azuread_user`

Refer to the Terraform Registory for docs: [`azuread_user`](https://www.terraform.io/docs/providers/azuread/r/user).
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
    jsii_type="@cdktf/provider-azuread.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/user azuread_user}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        user_principal_name: builtins.str,
        account_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        age_group: typing.Optional[builtins.str] = None,
        business_phones: typing.Optional[typing.Sequence[builtins.str]] = None,
        city: typing.Optional[builtins.str] = None,
        company_name: typing.Optional[builtins.str] = None,
        consent_provided_for_minor: typing.Optional[builtins.str] = None,
        cost_center: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        disable_password_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_strong_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        division: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_type: typing.Optional[builtins.str] = None,
        fax_number: typing.Optional[builtins.str] = None,
        force_password_change: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        given_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        mail: typing.Optional[builtins.str] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        manager_id: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office_location: typing.Optional[builtins.str] = None,
        onpremises_immutable_id: typing.Optional[builtins.str] = None,
        other_mails: typing.Optional[typing.Sequence[builtins.str]] = None,
        password: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        show_in_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["UserTimeouts", typing.Dict[str, typing.Any]]] = None,
        usage_location: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/user azuread_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The name to display in the address book for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#display_name User#display_name}
        :param user_principal_name: The user principal name (UPN) of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#user_principal_name User#user_principal_name}
        :param account_enabled: Whether or not the account should be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#account_enabled User#account_enabled}
        :param age_group: The age group of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#age_group User#age_group}
        :param business_phones: The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced with Azure AD Connect Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#business_phones User#business_phones}
        :param city: The city in which the user is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#city User#city}
        :param company_name: The company name which the user is associated. This property can be useful for describing the company that an external user comes from Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#company_name User#company_name}
        :param consent_provided_for_minor: Whether consent has been obtained for minors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#consent_provided_for_minor User#consent_provided_for_minor}
        :param cost_center: The cost center associated with the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#cost_center User#cost_center}
        :param country: The country/region in which the user is located, e.g. ``US`` or ``UK``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#country User#country}
        :param department: The name for the department in which the user works. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#department User#department}
        :param disable_password_expiration: Whether the users password is exempt from expiring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_password_expiration User#disable_password_expiration}
        :param disable_strong_password: Whether the user is allowed weaker passwords than the default policy to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_strong_password User#disable_strong_password}
        :param division: The name of the division in which the user works. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#division User#division}
        :param employee_id: The employee identifier assigned to the user by the organisation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_id User#employee_id}
        :param employee_type: Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_type User#employee_type}
        :param fax_number: The fax number of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#fax_number User#fax_number}
        :param force_password_change: Whether the user is forced to change the password during the next sign-in. Only takes effect when also changing the password Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#force_password_change User#force_password_change}
        :param given_name: The given name (first name) of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#given_name User#given_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_title: The user’s job title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#job_title User#job_title}
        :param mail: The SMTP address for the user. Cannot be unset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail User#mail}
        :param mail_nickname: The mail alias for the user. Defaults to the user name part of the user principal name (UPN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail_nickname User#mail_nickname}
        :param manager_id: The object ID of the user's manager. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#manager_id User#manager_id}
        :param mobile_phone: The primary cellular telephone number for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mobile_phone User#mobile_phone}
        :param office_location: The office location in the user's place of business. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#office_location User#office_location}
        :param onpremises_immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's ``user_principal_name`` property when creating a new user account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#onpremises_immutable_id User#onpremises_immutable_id}
        :param other_mails: Additional email addresses for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#other_mails User#other_mails}
        :param password: The password for the user. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters. This property is required when creating a new user Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#password User#password}
        :param postal_code: The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#postal_code User#postal_code}
        :param preferred_language: The user's preferred language, in ISO 639-1 notation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#preferred_language User#preferred_language}
        :param show_in_address_list: Whether or not the Outlook global address list should include this user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#show_in_address_list User#show_in_address_list}
        :param state: The state or province in the user's address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#state User#state}
        :param street_address: The street address of the user's place of business. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#street_address User#street_address}
        :param surname: The user's surname (family name or last name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#surname User#surname}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#timeouts User#timeouts}
        :param usage_location: The usage location of the user. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#usage_location User#usage_location}
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
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UserConfig(
            display_name=display_name,
            user_principal_name=user_principal_name,
            account_enabled=account_enabled,
            age_group=age_group,
            business_phones=business_phones,
            city=city,
            company_name=company_name,
            consent_provided_for_minor=consent_provided_for_minor,
            cost_center=cost_center,
            country=country,
            department=department,
            disable_password_expiration=disable_password_expiration,
            disable_strong_password=disable_strong_password,
            division=division,
            employee_id=employee_id,
            employee_type=employee_type,
            fax_number=fax_number,
            force_password_change=force_password_change,
            given_name=given_name,
            id=id,
            job_title=job_title,
            mail=mail,
            mail_nickname=mail_nickname,
            manager_id=manager_id,
            mobile_phone=mobile_phone,
            office_location=office_location,
            onpremises_immutable_id=onpremises_immutable_id,
            other_mails=other_mails,
            password=password,
            postal_code=postal_code,
            preferred_language=preferred_language,
            show_in_address_list=show_in_address_list,
            state=state,
            street_address=street_address,
            surname=surname,
            timeouts=timeouts,
            usage_location=usage_location,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#create User#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#delete User#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#read User#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#update User#update}.
        '''
        value = UserTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccountEnabled")
    def reset_account_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountEnabled", []))

    @jsii.member(jsii_name="resetAgeGroup")
    def reset_age_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgeGroup", []))

    @jsii.member(jsii_name="resetBusinessPhones")
    def reset_business_phones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBusinessPhones", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetCompanyName")
    def reset_company_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompanyName", []))

    @jsii.member(jsii_name="resetConsentProvidedForMinor")
    def reset_consent_provided_for_minor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsentProvidedForMinor", []))

    @jsii.member(jsii_name="resetCostCenter")
    def reset_cost_center(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCenter", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetDepartment")
    def reset_department(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDepartment", []))

    @jsii.member(jsii_name="resetDisablePasswordExpiration")
    def reset_disable_password_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePasswordExpiration", []))

    @jsii.member(jsii_name="resetDisableStrongPassword")
    def reset_disable_strong_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableStrongPassword", []))

    @jsii.member(jsii_name="resetDivision")
    def reset_division(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDivision", []))

    @jsii.member(jsii_name="resetEmployeeId")
    def reset_employee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmployeeId", []))

    @jsii.member(jsii_name="resetEmployeeType")
    def reset_employee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmployeeType", []))

    @jsii.member(jsii_name="resetFaxNumber")
    def reset_fax_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaxNumber", []))

    @jsii.member(jsii_name="resetForcePasswordChange")
    def reset_force_password_change(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForcePasswordChange", []))

    @jsii.member(jsii_name="resetGivenName")
    def reset_given_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGivenName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJobTitle")
    def reset_job_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobTitle", []))

    @jsii.member(jsii_name="resetMail")
    def reset_mail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMail", []))

    @jsii.member(jsii_name="resetMailNickname")
    def reset_mail_nickname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMailNickname", []))

    @jsii.member(jsii_name="resetManagerId")
    def reset_manager_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagerId", []))

    @jsii.member(jsii_name="resetMobilePhone")
    def reset_mobile_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMobilePhone", []))

    @jsii.member(jsii_name="resetOfficeLocation")
    def reset_office_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOfficeLocation", []))

    @jsii.member(jsii_name="resetOnpremisesImmutableId")
    def reset_onpremises_immutable_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnpremisesImmutableId", []))

    @jsii.member(jsii_name="resetOtherMails")
    def reset_other_mails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOtherMails", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPostalCode")
    def reset_postal_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalCode", []))

    @jsii.member(jsii_name="resetPreferredLanguage")
    def reset_preferred_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredLanguage", []))

    @jsii.member(jsii_name="resetShowInAddressList")
    def reset_show_in_address_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShowInAddressList", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @jsii.member(jsii_name="resetSurname")
    def reset_surname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSurname", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUsageLocation")
    def reset_usage_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsageLocation", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aboutMe")
    def about_me(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aboutMe"))

    @builtins.property
    @jsii.member(jsii_name="creationType")
    def creation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationType"))

    @builtins.property
    @jsii.member(jsii_name="externalUserState")
    def external_user_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalUserState"))

    @builtins.property
    @jsii.member(jsii_name="imAddresses")
    def im_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "imAddresses"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesDistinguishedName")
    def onpremises_distinguished_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesDistinguishedName"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesDomainName")
    def onpremises_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesDomainName"))

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
    @jsii.member(jsii_name="onpremisesUserPrincipalName")
    def onpremises_user_principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesUserPrincipalName"))

    @builtins.property
    @jsii.member(jsii_name="proxyAddresses")
    def proxy_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "proxyAddresses"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "UserTimeoutsOutputReference":
        return typing.cast("UserTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userType"))

    @builtins.property
    @jsii.member(jsii_name="accountEnabledInput")
    def account_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "accountEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ageGroupInput")
    def age_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ageGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="businessPhonesInput")
    def business_phones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "businessPhonesInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="companyNameInput")
    def company_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "companyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consentProvidedForMinorInput")
    def consent_provided_for_minor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consentProvidedForMinorInput"))

    @builtins.property
    @jsii.member(jsii_name="costCenterInput")
    def cost_center_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "costCenterInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="departmentInput")
    def department_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "departmentInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordExpirationInput")
    def disable_password_expiration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disablePasswordExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableStrongPasswordInput")
    def disable_strong_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableStrongPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="divisionInput")
    def division_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "divisionInput"))

    @builtins.property
    @jsii.member(jsii_name="employeeIdInput")
    def employee_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "employeeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="employeeTypeInput")
    def employee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "employeeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="faxNumberInput")
    def fax_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faxNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="forcePasswordChangeInput")
    def force_password_change_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forcePasswordChangeInput"))

    @builtins.property
    @jsii.member(jsii_name="givenNameInput")
    def given_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "givenNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobTitleInput")
    def job_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="mailInput")
    def mail_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mailInput"))

    @builtins.property
    @jsii.member(jsii_name="mailNicknameInput")
    def mail_nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mailNicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="managerIdInput")
    def manager_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="mobilePhoneInput")
    def mobile_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mobilePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="officeLocationInput")
    def office_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "officeLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="onpremisesImmutableIdInput")
    def onpremises_immutable_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onpremisesImmutableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="otherMailsInput")
    def other_mails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "otherMailsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredLanguageInput")
    def preferred_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="showInAddressListInput")
    def show_in_address_list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "showInAddressListInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="surnameInput")
    def surname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "surnameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["UserTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["UserTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="usageLocationInput")
    def usage_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="userPrincipalNameInput")
    def user_principal_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPrincipalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountEnabled")
    def account_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "accountEnabled"))

    @account_enabled.setter
    def account_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "account_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="ageGroup")
    def age_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ageGroup"))

    @age_group.setter
    def age_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "age_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ageGroup", value)

    @builtins.property
    @jsii.member(jsii_name="businessPhones")
    def business_phones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "businessPhones"))

    @business_phones.setter
    def business_phones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "business_phones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "businessPhones", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "city").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="companyName")
    def company_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "companyName"))

    @company_name.setter
    def company_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "company_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyName", value)

    @builtins.property
    @jsii.member(jsii_name="consentProvidedForMinor")
    def consent_provided_for_minor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consentProvidedForMinor"))

    @consent_provided_for_minor.setter
    def consent_provided_for_minor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "consent_provided_for_minor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consentProvidedForMinor", value)

    @builtins.property
    @jsii.member(jsii_name="costCenter")
    def cost_center(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "costCenter"))

    @cost_center.setter
    def cost_center(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "cost_center").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costCenter", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="department")
    def department(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "department"))

    @department.setter
    def department(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "department").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "department", value)

    @builtins.property
    @jsii.member(jsii_name="disablePasswordExpiration")
    def disable_password_expiration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disablePasswordExpiration"))

    @disable_password_expiration.setter
    def disable_password_expiration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "disable_password_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="disableStrongPassword")
    def disable_strong_password(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableStrongPassword"))

    @disable_strong_password.setter
    def disable_strong_password(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "disable_strong_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableStrongPassword", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="division")
    def division(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "division"))

    @division.setter
    def division(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "division").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "division", value)

    @builtins.property
    @jsii.member(jsii_name="employeeId")
    def employee_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "employeeId"))

    @employee_id.setter
    def employee_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "employee_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "employeeId", value)

    @builtins.property
    @jsii.member(jsii_name="employeeType")
    def employee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "employeeType"))

    @employee_type.setter
    def employee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "employee_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "employeeType", value)

    @builtins.property
    @jsii.member(jsii_name="faxNumber")
    def fax_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "faxNumber"))

    @fax_number.setter
    def fax_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "fax_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faxNumber", value)

    @builtins.property
    @jsii.member(jsii_name="forcePasswordChange")
    def force_password_change(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forcePasswordChange"))

    @force_password_change.setter
    def force_password_change(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "force_password_change").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forcePasswordChange", value)

    @builtins.property
    @jsii.member(jsii_name="givenName")
    def given_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "givenName"))

    @given_name.setter
    def given_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "given_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "givenName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobTitle")
    def job_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobTitle"))

    @job_title.setter
    def job_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "job_title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTitle", value)

    @builtins.property
    @jsii.member(jsii_name="mail")
    def mail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mail"))

    @mail.setter
    def mail(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "mail").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mail", value)

    @builtins.property
    @jsii.member(jsii_name="mailNickname")
    def mail_nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mailNickname"))

    @mail_nickname.setter
    def mail_nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "mail_nickname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailNickname", value)

    @builtins.property
    @jsii.member(jsii_name="managerId")
    def manager_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managerId"))

    @manager_id.setter
    def manager_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "manager_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managerId", value)

    @builtins.property
    @jsii.member(jsii_name="mobilePhone")
    def mobile_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mobilePhone"))

    @mobile_phone.setter
    def mobile_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "mobile_phone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mobilePhone", value)

    @builtins.property
    @jsii.member(jsii_name="officeLocation")
    def office_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "officeLocation"))

    @office_location.setter
    def office_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "office_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "officeLocation", value)

    @builtins.property
    @jsii.member(jsii_name="onpremisesImmutableId")
    def onpremises_immutable_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onpremisesImmutableId"))

    @onpremises_immutable_id.setter
    def onpremises_immutable_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "onpremises_immutable_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onpremisesImmutableId", value)

    @builtins.property
    @jsii.member(jsii_name="otherMails")
    def other_mails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "otherMails"))

    @other_mails.setter
    def other_mails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "other_mails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "otherMails", value)

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
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="preferredLanguage")
    def preferred_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredLanguage"))

    @preferred_language.setter
    def preferred_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "preferred_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="showInAddressList")
    def show_in_address_list(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "showInAddressList"))

    @show_in_address_list.setter
    def show_in_address_list(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "show_in_address_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "showInAddressList", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "street_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="surname")
    def surname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "surname"))

    @surname.setter
    def surname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "surname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "surname", value)

    @builtins.property
    @jsii.member(jsii_name="usageLocation")
    def usage_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usageLocation"))

    @usage_location.setter
    def usage_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "usage_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="userPrincipalName")
    def user_principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPrincipalName"))

    @user_principal_name.setter
    def user_principal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "user_principal_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPrincipalName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.user.UserConfig",
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
        "user_principal_name": "userPrincipalName",
        "account_enabled": "accountEnabled",
        "age_group": "ageGroup",
        "business_phones": "businessPhones",
        "city": "city",
        "company_name": "companyName",
        "consent_provided_for_minor": "consentProvidedForMinor",
        "cost_center": "costCenter",
        "country": "country",
        "department": "department",
        "disable_password_expiration": "disablePasswordExpiration",
        "disable_strong_password": "disableStrongPassword",
        "division": "division",
        "employee_id": "employeeId",
        "employee_type": "employeeType",
        "fax_number": "faxNumber",
        "force_password_change": "forcePasswordChange",
        "given_name": "givenName",
        "id": "id",
        "job_title": "jobTitle",
        "mail": "mail",
        "mail_nickname": "mailNickname",
        "manager_id": "managerId",
        "mobile_phone": "mobilePhone",
        "office_location": "officeLocation",
        "onpremises_immutable_id": "onpremisesImmutableId",
        "other_mails": "otherMails",
        "password": "password",
        "postal_code": "postalCode",
        "preferred_language": "preferredLanguage",
        "show_in_address_list": "showInAddressList",
        "state": "state",
        "street_address": "streetAddress",
        "surname": "surname",
        "timeouts": "timeouts",
        "usage_location": "usageLocation",
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
        display_name: builtins.str,
        user_principal_name: builtins.str,
        account_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        age_group: typing.Optional[builtins.str] = None,
        business_phones: typing.Optional[typing.Sequence[builtins.str]] = None,
        city: typing.Optional[builtins.str] = None,
        company_name: typing.Optional[builtins.str] = None,
        consent_provided_for_minor: typing.Optional[builtins.str] = None,
        cost_center: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        disable_password_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_strong_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        division: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_type: typing.Optional[builtins.str] = None,
        fax_number: typing.Optional[builtins.str] = None,
        force_password_change: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        given_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        mail: typing.Optional[builtins.str] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        manager_id: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office_location: typing.Optional[builtins.str] = None,
        onpremises_immutable_id: typing.Optional[builtins.str] = None,
        other_mails: typing.Optional[typing.Sequence[builtins.str]] = None,
        password: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        show_in_address_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["UserTimeouts", typing.Dict[str, typing.Any]]] = None,
        usage_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The name to display in the address book for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#display_name User#display_name}
        :param user_principal_name: The user principal name (UPN) of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#user_principal_name User#user_principal_name}
        :param account_enabled: Whether or not the account should be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#account_enabled User#account_enabled}
        :param age_group: The age group of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#age_group User#age_group}
        :param business_phones: The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced with Azure AD Connect Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#business_phones User#business_phones}
        :param city: The city in which the user is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#city User#city}
        :param company_name: The company name which the user is associated. This property can be useful for describing the company that an external user comes from Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#company_name User#company_name}
        :param consent_provided_for_minor: Whether consent has been obtained for minors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#consent_provided_for_minor User#consent_provided_for_minor}
        :param cost_center: The cost center associated with the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#cost_center User#cost_center}
        :param country: The country/region in which the user is located, e.g. ``US`` or ``UK``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#country User#country}
        :param department: The name for the department in which the user works. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#department User#department}
        :param disable_password_expiration: Whether the users password is exempt from expiring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_password_expiration User#disable_password_expiration}
        :param disable_strong_password: Whether the user is allowed weaker passwords than the default policy to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_strong_password User#disable_strong_password}
        :param division: The name of the division in which the user works. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#division User#division}
        :param employee_id: The employee identifier assigned to the user by the organisation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_id User#employee_id}
        :param employee_type: Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_type User#employee_type}
        :param fax_number: The fax number of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#fax_number User#fax_number}
        :param force_password_change: Whether the user is forced to change the password during the next sign-in. Only takes effect when also changing the password Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#force_password_change User#force_password_change}
        :param given_name: The given name (first name) of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#given_name User#given_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_title: The user’s job title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#job_title User#job_title}
        :param mail: The SMTP address for the user. Cannot be unset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail User#mail}
        :param mail_nickname: The mail alias for the user. Defaults to the user name part of the user principal name (UPN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail_nickname User#mail_nickname}
        :param manager_id: The object ID of the user's manager. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#manager_id User#manager_id}
        :param mobile_phone: The primary cellular telephone number for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mobile_phone User#mobile_phone}
        :param office_location: The office location in the user's place of business. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#office_location User#office_location}
        :param onpremises_immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's ``user_principal_name`` property when creating a new user account Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#onpremises_immutable_id User#onpremises_immutable_id}
        :param other_mails: Additional email addresses for the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#other_mails User#other_mails}
        :param password: The password for the user. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters. This property is required when creating a new user Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#password User#password}
        :param postal_code: The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#postal_code User#postal_code}
        :param preferred_language: The user's preferred language, in ISO 639-1 notation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#preferred_language User#preferred_language}
        :param show_in_address_list: Whether or not the Outlook global address list should include this user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#show_in_address_list User#show_in_address_list}
        :param state: The state or province in the user's address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#state User#state}
        :param street_address: The street address of the user's place of business. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#street_address User#street_address}
        :param surname: The user's surname (family name or last name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#surname User#surname}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#timeouts User#timeouts}
        :param usage_location: The usage location of the user. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#usage_location User#usage_location}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument user_principal_name", value=user_principal_name, expected_type=type_hints["user_principal_name"])
            check_type(argname="argument account_enabled", value=account_enabled, expected_type=type_hints["account_enabled"])
            check_type(argname="argument age_group", value=age_group, expected_type=type_hints["age_group"])
            check_type(argname="argument business_phones", value=business_phones, expected_type=type_hints["business_phones"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument company_name", value=company_name, expected_type=type_hints["company_name"])
            check_type(argname="argument consent_provided_for_minor", value=consent_provided_for_minor, expected_type=type_hints["consent_provided_for_minor"])
            check_type(argname="argument cost_center", value=cost_center, expected_type=type_hints["cost_center"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument department", value=department, expected_type=type_hints["department"])
            check_type(argname="argument disable_password_expiration", value=disable_password_expiration, expected_type=type_hints["disable_password_expiration"])
            check_type(argname="argument disable_strong_password", value=disable_strong_password, expected_type=type_hints["disable_strong_password"])
            check_type(argname="argument division", value=division, expected_type=type_hints["division"])
            check_type(argname="argument employee_id", value=employee_id, expected_type=type_hints["employee_id"])
            check_type(argname="argument employee_type", value=employee_type, expected_type=type_hints["employee_type"])
            check_type(argname="argument fax_number", value=fax_number, expected_type=type_hints["fax_number"])
            check_type(argname="argument force_password_change", value=force_password_change, expected_type=type_hints["force_password_change"])
            check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job_title", value=job_title, expected_type=type_hints["job_title"])
            check_type(argname="argument mail", value=mail, expected_type=type_hints["mail"])
            check_type(argname="argument mail_nickname", value=mail_nickname, expected_type=type_hints["mail_nickname"])
            check_type(argname="argument manager_id", value=manager_id, expected_type=type_hints["manager_id"])
            check_type(argname="argument mobile_phone", value=mobile_phone, expected_type=type_hints["mobile_phone"])
            check_type(argname="argument office_location", value=office_location, expected_type=type_hints["office_location"])
            check_type(argname="argument onpremises_immutable_id", value=onpremises_immutable_id, expected_type=type_hints["onpremises_immutable_id"])
            check_type(argname="argument other_mails", value=other_mails, expected_type=type_hints["other_mails"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument preferred_language", value=preferred_language, expected_type=type_hints["preferred_language"])
            check_type(argname="argument show_in_address_list", value=show_in_address_list, expected_type=type_hints["show_in_address_list"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
            check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument usage_location", value=usage_location, expected_type=type_hints["usage_location"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "user_principal_name": user_principal_name,
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
        if account_enabled is not None:
            self._values["account_enabled"] = account_enabled
        if age_group is not None:
            self._values["age_group"] = age_group
        if business_phones is not None:
            self._values["business_phones"] = business_phones
        if city is not None:
            self._values["city"] = city
        if company_name is not None:
            self._values["company_name"] = company_name
        if consent_provided_for_minor is not None:
            self._values["consent_provided_for_minor"] = consent_provided_for_minor
        if cost_center is not None:
            self._values["cost_center"] = cost_center
        if country is not None:
            self._values["country"] = country
        if department is not None:
            self._values["department"] = department
        if disable_password_expiration is not None:
            self._values["disable_password_expiration"] = disable_password_expiration
        if disable_strong_password is not None:
            self._values["disable_strong_password"] = disable_strong_password
        if division is not None:
            self._values["division"] = division
        if employee_id is not None:
            self._values["employee_id"] = employee_id
        if employee_type is not None:
            self._values["employee_type"] = employee_type
        if fax_number is not None:
            self._values["fax_number"] = fax_number
        if force_password_change is not None:
            self._values["force_password_change"] = force_password_change
        if given_name is not None:
            self._values["given_name"] = given_name
        if id is not None:
            self._values["id"] = id
        if job_title is not None:
            self._values["job_title"] = job_title
        if mail is not None:
            self._values["mail"] = mail
        if mail_nickname is not None:
            self._values["mail_nickname"] = mail_nickname
        if manager_id is not None:
            self._values["manager_id"] = manager_id
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if office_location is not None:
            self._values["office_location"] = office_location
        if onpremises_immutable_id is not None:
            self._values["onpremises_immutable_id"] = onpremises_immutable_id
        if other_mails is not None:
            self._values["other_mails"] = other_mails
        if password is not None:
            self._values["password"] = password
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if preferred_language is not None:
            self._values["preferred_language"] = preferred_language
        if show_in_address_list is not None:
            self._values["show_in_address_list"] = show_in_address_list
        if state is not None:
            self._values["state"] = state
        if street_address is not None:
            self._values["street_address"] = street_address
        if surname is not None:
            self._values["surname"] = surname
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if usage_location is not None:
            self._values["usage_location"] = usage_location

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
        '''The name to display in the address book for the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#display_name User#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_principal_name(self) -> builtins.str:
        '''The user principal name (UPN) of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#user_principal_name User#user_principal_name}
        '''
        result = self._values.get("user_principal_name")
        assert result is not None, "Required property 'user_principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not the account should be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#account_enabled User#account_enabled}
        '''
        result = self._values.get("account_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def age_group(self) -> typing.Optional[builtins.str]:
        '''The age group of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#age_group User#age_group}
        '''
        result = self._values.get("age_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def business_phones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The telephone numbers for the user.

        Only one number can be set for this property. Read-only for users synced with Azure AD Connect

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#business_phones User#business_phones}
        '''
        result = self._values.get("business_phones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''The city in which the user is located.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#city User#city}
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company_name(self) -> typing.Optional[builtins.str]:
        '''The company name which the user is associated.

        This property can be useful for describing the company that an external user comes from

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#company_name User#company_name}
        '''
        result = self._values.get("company_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consent_provided_for_minor(self) -> typing.Optional[builtins.str]:
        '''Whether consent has been obtained for minors.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#consent_provided_for_minor User#consent_provided_for_minor}
        '''
        result = self._values.get("consent_provided_for_minor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cost_center(self) -> typing.Optional[builtins.str]:
        '''The cost center associated with the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#cost_center User#cost_center}
        '''
        result = self._values.get("cost_center")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''The country/region in which the user is located, e.g. ``US`` or ``UK``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#country User#country}
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''The name for the department in which the user works.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#department User#department}
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_password_expiration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the users password is exempt from expiring.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_password_expiration User#disable_password_expiration}
        '''
        result = self._values.get("disable_password_expiration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_strong_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the user is allowed weaker passwords than the default policy to be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#disable_strong_password User#disable_strong_password}
        '''
        result = self._values.get("disable_strong_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def division(self) -> typing.Optional[builtins.str]:
        '''The name of the division in which the user works.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#division User#division}
        '''
        result = self._values.get("division")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_id(self) -> typing.Optional[builtins.str]:
        '''The employee identifier assigned to the user by the organisation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_id User#employee_id}
        '''
        result = self._values.get("employee_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_type(self) -> typing.Optional[builtins.str]:
        '''Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#employee_type User#employee_type}
        '''
        result = self._values.get("employee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fax_number(self) -> typing.Optional[builtins.str]:
        '''The fax number of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#fax_number User#fax_number}
        '''
        result = self._values.get("fax_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_password_change(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the user is forced to change the password during the next sign-in.

        Only takes effect when also changing the password

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#force_password_change User#force_password_change}
        '''
        result = self._values.get("force_password_change")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''The given name (first name) of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#given_name User#given_name}
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_title(self) -> typing.Optional[builtins.str]:
        '''The user’s job title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#job_title User#job_title}
        '''
        result = self._values.get("job_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mail(self) -> typing.Optional[builtins.str]:
        '''The SMTP address for the user. Cannot be unset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail User#mail}
        '''
        result = self._values.get("mail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mail_nickname(self) -> typing.Optional[builtins.str]:
        '''The mail alias for the user. Defaults to the user name part of the user principal name (UPN).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mail_nickname User#mail_nickname}
        '''
        result = self._values.get("mail_nickname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manager_id(self) -> typing.Optional[builtins.str]:
        '''The object ID of the user's manager.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#manager_id User#manager_id}
        '''
        result = self._values.get("manager_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''The primary cellular telephone number for the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#mobile_phone User#mobile_phone}
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office_location(self) -> typing.Optional[builtins.str]:
        '''The office location in the user's place of business.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#office_location User#office_location}
        '''
        result = self._values.get("office_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def onpremises_immutable_id(self) -> typing.Optional[builtins.str]:
        '''The value used to associate an on-premise Active Directory user account with their Azure AD user object.

        This must be specified if you are using a federated domain for the user's ``user_principal_name`` property when creating a new user account

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#onpremises_immutable_id User#onpremises_immutable_id}
        '''
        result = self._values.get("onpremises_immutable_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def other_mails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional email addresses for the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#other_mails User#other_mails}
        '''
        result = self._values.get("other_mails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the user.

        The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters. This property is required when creating a new user

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#password User#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''The postal code for the user's postal address.

        The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#postal_code User#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_language(self) -> typing.Optional[builtins.str]:
        '''The user's preferred language, in ISO 639-1 notation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#preferred_language User#preferred_language}
        '''
        result = self._values.get("preferred_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def show_in_address_list(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not the Outlook global address list should include this user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#show_in_address_list User#show_in_address_list}
        '''
        result = self._values.get("show_in_address_list")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state or province in the user's address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#state User#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''The street address of the user's place of business.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#street_address User#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''The user's surname (family name or last name).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#surname User#surname}
        '''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["UserTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#timeouts User#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["UserTimeouts"], result)

    @builtins.property
    def usage_location(self) -> typing.Optional[builtins.str]:
        '''The usage location of the user.

        Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#usage_location User#usage_location}
        '''
        result = self._values.get("usage_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.user.UserTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class UserTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#create User#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#delete User#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#read User#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#update User#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#create User#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#delete User#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#read User#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/user#update User#update}.'''
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
    jsii_type="@cdktf/provider-azuread.user.UserTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

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


__all__ = [
    "User",
    "UserConfig",
    "UserTimeouts",
    "UserTimeoutsOutputReference",
]

publication.publish()
