'''
# `okta_user`

Refer to the Terraform Registory for docs: [`okta_user`](https://www.terraform.io/docs/providers/okta/r/user).
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
    jsii_type="@cdktf/provider-okta.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/user okta_user}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        login: builtins.str,
        admin_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        city: typing.Optional[builtins.str] = None,
        cost_center: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        custom_profile_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        expire_password_on_create: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_memberships: typing.Optional[typing.Sequence[builtins.str]] = None,
        honorific_prefix: typing.Optional[builtins.str] = None,
        honorific_suffix: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locale: typing.Optional[builtins.str] = None,
        manager: typing.Optional[builtins.str] = None,
        manager_id: typing.Optional[builtins.str] = None,
        middle_name: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        nick_name: typing.Optional[builtins.str] = None,
        old_password: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        password_hash: typing.Optional[typing.Union["UserPasswordHash", typing.Dict[str, typing.Any]]] = None,
        password_inline_hook: typing.Optional[builtins.str] = None,
        postal_address: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        primary_phone: typing.Optional[builtins.str] = None,
        profile_url: typing.Optional[builtins.str] = None,
        recovery_answer: typing.Optional[builtins.str] = None,
        recovery_question: typing.Optional[builtins.str] = None,
        second_email: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/user okta_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: User primary email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#email User#email}
        :param first_name: User first name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#first_name User#first_name}
        :param last_name: User last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#last_name User#last_name}
        :param login: User Okta login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#login User#login}
        :param admin_roles: User Okta admin roles - ie. ['APP_ADMIN', 'USER_ADMIN']. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#admin_roles User#admin_roles}
        :param city: User city. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#city User#city}
        :param cost_center: User cost center. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#cost_center User#cost_center}
        :param country_code: User country code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#country_code User#country_code}
        :param custom_profile_attributes: JSON formatted custom attributes for a user. It must be JSON due to various types Okta allows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#custom_profile_attributes User#custom_profile_attributes}
        :param department: User department. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#department User#department}
        :param display_name: User display name, suitable to show end users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#display_name User#display_name}
        :param division: User division. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#division User#division}
        :param employee_number: User employee number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#employee_number User#employee_number}
        :param expire_password_on_create: If set to ``true``, the user will have to change the password at the next login. This property will be used when user is being created and works only when ``password`` field is set Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#expire_password_on_create User#expire_password_on_create}
        :param group_memberships: The groups that you want this user to be a part of. This can also be done via the group using the ``users`` property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#group_memberships User#group_memberships}
        :param honorific_prefix: User honorific prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_prefix User#honorific_prefix}
        :param honorific_suffix: User honorific suffix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_suffix User#honorific_suffix}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locale: User default location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#locale User#locale}
        :param manager: Manager of User. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager User#manager}
        :param manager_id: Manager ID of User. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager_id User#manager_id}
        :param middle_name: User middle name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#middle_name User#middle_name}
        :param mobile_phone: User mobile phone number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#mobile_phone User#mobile_phone}
        :param nick_name: User nickname. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#nick_name User#nick_name}
        :param old_password: Old User Password. Should be only set in case the password was not changed using the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#old_password User#old_password}
        :param organization: User organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#organization User#organization}
        :param password: User Password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password User#password}
        :param password_hash: password_hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_hash User#password_hash}
        :param password_inline_hook: When specified, the Password Inline Hook is triggered to handle verification of the end user's password the first time the user tries to sign in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_inline_hook User#password_inline_hook}
        :param postal_address: User mailing address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#postal_address User#postal_address}
        :param preferred_language: User preferred language. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#preferred_language User#preferred_language}
        :param primary_phone: User primary phone number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#primary_phone User#primary_phone}
        :param profile_url: User online profile (web page). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#profile_url User#profile_url}
        :param recovery_answer: User Password Recovery Answer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_answer User#recovery_answer}
        :param recovery_question: User Password Recovery Question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_question User#recovery_question}
        :param second_email: User secondary email address, used for account recovery. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#second_email User#second_email}
        :param state: User state or region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#state User#state}
        :param status: The status of the User in Okta - remove to set user back to active/provisioned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#status User#status}
        :param street_address: User street address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#street_address User#street_address}
        :param timezone: User default timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#timezone User#timezone}
        :param title: User title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#title User#title}
        :param user_type: User employee type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#user_type User#user_type}
        :param zip_code: User zipcode or postal code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#zip_code User#zip_code}
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
            email=email,
            first_name=first_name,
            last_name=last_name,
            login=login,
            admin_roles=admin_roles,
            city=city,
            cost_center=cost_center,
            country_code=country_code,
            custom_profile_attributes=custom_profile_attributes,
            department=department,
            display_name=display_name,
            division=division,
            employee_number=employee_number,
            expire_password_on_create=expire_password_on_create,
            group_memberships=group_memberships,
            honorific_prefix=honorific_prefix,
            honorific_suffix=honorific_suffix,
            id=id,
            locale=locale,
            manager=manager,
            manager_id=manager_id,
            middle_name=middle_name,
            mobile_phone=mobile_phone,
            nick_name=nick_name,
            old_password=old_password,
            organization=organization,
            password=password,
            password_hash=password_hash,
            password_inline_hook=password_inline_hook,
            postal_address=postal_address,
            preferred_language=preferred_language,
            primary_phone=primary_phone,
            profile_url=profile_url,
            recovery_answer=recovery_answer,
            recovery_question=recovery_question,
            second_email=second_email,
            state=state,
            status=status,
            street_address=street_address,
            timezone=timezone,
            title=title,
            user_type=user_type,
            zip_code=zip_code,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPasswordHash")
    def put_password_hash(
        self,
        *,
        algorithm: builtins.str,
        value: builtins.str,
        salt: typing.Optional[builtins.str] = None,
        salt_order: typing.Optional[builtins.str] = None,
        work_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm used to generate the hash using the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#algorithm User#algorithm}
        :param value: For SHA-512, SHA-256, SHA-1, MD5, This is the actual base64-encoded hash of the password (and salt, if used). This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be the the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#value User#value}
        :param salt: Only required for salted hashes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt User#salt}
        :param salt_order: Specifies whether salt was pre- or postfixed to the password before hashing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt_order User#salt_order}
        :param work_factor: Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#work_factor User#work_factor}
        '''
        value_ = UserPasswordHash(
            algorithm=algorithm,
            value=value,
            salt=salt,
            salt_order=salt_order,
            work_factor=work_factor,
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordHash", [value_]))

    @jsii.member(jsii_name="resetAdminRoles")
    def reset_admin_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminRoles", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetCostCenter")
    def reset_cost_center(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCenter", []))

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetCustomProfileAttributes")
    def reset_custom_profile_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProfileAttributes", []))

    @jsii.member(jsii_name="resetDepartment")
    def reset_department(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDepartment", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetDivision")
    def reset_division(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDivision", []))

    @jsii.member(jsii_name="resetEmployeeNumber")
    def reset_employee_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmployeeNumber", []))

    @jsii.member(jsii_name="resetExpirePasswordOnCreate")
    def reset_expire_password_on_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirePasswordOnCreate", []))

    @jsii.member(jsii_name="resetGroupMemberships")
    def reset_group_memberships(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupMemberships", []))

    @jsii.member(jsii_name="resetHonorificPrefix")
    def reset_honorific_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHonorificPrefix", []))

    @jsii.member(jsii_name="resetHonorificSuffix")
    def reset_honorific_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHonorificSuffix", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocale")
    def reset_locale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocale", []))

    @jsii.member(jsii_name="resetManager")
    def reset_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManager", []))

    @jsii.member(jsii_name="resetManagerId")
    def reset_manager_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagerId", []))

    @jsii.member(jsii_name="resetMiddleName")
    def reset_middle_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMiddleName", []))

    @jsii.member(jsii_name="resetMobilePhone")
    def reset_mobile_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMobilePhone", []))

    @jsii.member(jsii_name="resetNickName")
    def reset_nick_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNickName", []))

    @jsii.member(jsii_name="resetOldPassword")
    def reset_old_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOldPassword", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPasswordHash")
    def reset_password_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordHash", []))

    @jsii.member(jsii_name="resetPasswordInlineHook")
    def reset_password_inline_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordInlineHook", []))

    @jsii.member(jsii_name="resetPostalAddress")
    def reset_postal_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalAddress", []))

    @jsii.member(jsii_name="resetPreferredLanguage")
    def reset_preferred_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredLanguage", []))

    @jsii.member(jsii_name="resetPrimaryPhone")
    def reset_primary_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryPhone", []))

    @jsii.member(jsii_name="resetProfileUrl")
    def reset_profile_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfileUrl", []))

    @jsii.member(jsii_name="resetRecoveryAnswer")
    def reset_recovery_answer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryAnswer", []))

    @jsii.member(jsii_name="resetRecoveryQuestion")
    def reset_recovery_question(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryQuestion", []))

    @jsii.member(jsii_name="resetSecondEmail")
    def reset_second_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondEmail", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetUserType")
    def reset_user_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserType", []))

    @jsii.member(jsii_name="resetZipCode")
    def reset_zip_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipCode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="passwordHash")
    def password_hash(self) -> "UserPasswordHashOutputReference":
        return typing.cast("UserPasswordHashOutputReference", jsii.get(self, "passwordHash"))

    @builtins.property
    @jsii.member(jsii_name="rawStatus")
    def raw_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rawStatus"))

    @builtins.property
    @jsii.member(jsii_name="adminRolesInput")
    def admin_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "adminRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="costCenterInput")
    def cost_center_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "costCenterInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="customProfileAttributesInput")
    def custom_profile_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customProfileAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="departmentInput")
    def department_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "departmentInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="divisionInput")
    def division_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "divisionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="employeeNumberInput")
    def employee_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "employeeNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="expirePasswordOnCreateInput")
    def expire_password_on_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "expirePasswordOnCreateInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupMembershipsInput")
    def group_memberships_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupMembershipsInput"))

    @builtins.property
    @jsii.member(jsii_name="honorificPrefixInput")
    def honorific_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "honorificPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="honorificSuffixInput")
    def honorific_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "honorificSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="localeInput")
    def locale_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localeInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="managerIdInput")
    def manager_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="managerInput")
    def manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managerInput"))

    @builtins.property
    @jsii.member(jsii_name="middleNameInput")
    def middle_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "middleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mobilePhoneInput")
    def mobile_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mobilePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="nickNameInput")
    def nick_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nickNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oldPasswordInput")
    def old_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oldPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordHashInput")
    def password_hash_input(self) -> typing.Optional["UserPasswordHash"]:
        return typing.cast(typing.Optional["UserPasswordHash"], jsii.get(self, "passwordHashInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInlineHookInput")
    def password_inline_hook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInlineHookInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="postalAddressInput")
    def postal_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredLanguageInput")
    def preferred_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryPhoneInput")
    def primary_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryPhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="profileUrlInput")
    def profile_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryAnswerInput")
    def recovery_answer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryAnswerInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryQuestionInput")
    def recovery_question_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryQuestionInput"))

    @builtins.property
    @jsii.member(jsii_name="secondEmailInput")
    def second_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="userTypeInput")
    def user_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="zipCodeInput")
    def zip_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="adminRoles")
    def admin_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "adminRoles"))

    @admin_roles.setter
    def admin_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "admin_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminRoles", value)

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
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="customProfileAttributes")
    def custom_profile_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customProfileAttributes"))

    @custom_profile_attributes.setter
    def custom_profile_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "custom_profile_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProfileAttributes", value)

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
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="employeeNumber")
    def employee_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "employeeNumber"))

    @employee_number.setter
    def employee_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "employee_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "employeeNumber", value)

    @builtins.property
    @jsii.member(jsii_name="expirePasswordOnCreate")
    def expire_password_on_create(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "expirePasswordOnCreate"))

    @expire_password_on_create.setter
    def expire_password_on_create(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "expire_password_on_create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirePasswordOnCreate", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "first_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="groupMemberships")
    def group_memberships(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupMemberships"))

    @group_memberships.setter
    def group_memberships(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "group_memberships").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupMemberships", value)

    @builtins.property
    @jsii.member(jsii_name="honorificPrefix")
    def honorific_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "honorificPrefix"))

    @honorific_prefix.setter
    def honorific_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "honorific_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "honorificPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="honorificSuffix")
    def honorific_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "honorificSuffix"))

    @honorific_suffix.setter
    def honorific_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "honorific_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "honorificSuffix", value)

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
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "last_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locale"))

    @locale.setter
    def locale(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "locale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locale", value)

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "login"))

    @login.setter
    def login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "login", value)

    @builtins.property
    @jsii.member(jsii_name="manager")
    def manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manager"))

    @manager.setter
    def manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "manager").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manager", value)

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
    @jsii.member(jsii_name="middleName")
    def middle_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "middleName"))

    @middle_name.setter
    def middle_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "middle_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "middleName", value)

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
    @jsii.member(jsii_name="nickName")
    def nick_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickName"))

    @nick_name.setter
    def nick_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "nick_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickName", value)

    @builtins.property
    @jsii.member(jsii_name="oldPassword")
    def old_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oldPassword"))

    @old_password.setter
    def old_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "old_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oldPassword", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

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
    @jsii.member(jsii_name="passwordInlineHook")
    def password_inline_hook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordInlineHook"))

    @password_inline_hook.setter
    def password_inline_hook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "password_inline_hook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordInlineHook", value)

    @builtins.property
    @jsii.member(jsii_name="postalAddress")
    def postal_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalAddress"))

    @postal_address.setter
    def postal_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "postal_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalAddress", value)

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
    @jsii.member(jsii_name="primaryPhone")
    def primary_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryPhone"))

    @primary_phone.setter
    def primary_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "primary_phone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryPhone", value)

    @builtins.property
    @jsii.member(jsii_name="profileUrl")
    def profile_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileUrl"))

    @profile_url.setter
    def profile_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "profile_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileUrl", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryAnswer")
    def recovery_answer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryAnswer"))

    @recovery_answer.setter
    def recovery_answer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "recovery_answer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryAnswer", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryQuestion")
    def recovery_question(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryQuestion"))

    @recovery_question.setter
    def recovery_question(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "recovery_question").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryQuestion", value)

    @builtins.property
    @jsii.member(jsii_name="secondEmail")
    def second_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondEmail"))

    @second_email.setter
    def second_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "second_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondEmail", value)

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
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

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
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "user_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value)

    @builtins.property
    @jsii.member(jsii_name="zipCode")
    def zip_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipCode"))

    @zip_code.setter
    def zip_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "zip_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipCode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.user.UserConfig",
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
        "first_name": "firstName",
        "last_name": "lastName",
        "login": "login",
        "admin_roles": "adminRoles",
        "city": "city",
        "cost_center": "costCenter",
        "country_code": "countryCode",
        "custom_profile_attributes": "customProfileAttributes",
        "department": "department",
        "display_name": "displayName",
        "division": "division",
        "employee_number": "employeeNumber",
        "expire_password_on_create": "expirePasswordOnCreate",
        "group_memberships": "groupMemberships",
        "honorific_prefix": "honorificPrefix",
        "honorific_suffix": "honorificSuffix",
        "id": "id",
        "locale": "locale",
        "manager": "manager",
        "manager_id": "managerId",
        "middle_name": "middleName",
        "mobile_phone": "mobilePhone",
        "nick_name": "nickName",
        "old_password": "oldPassword",
        "organization": "organization",
        "password": "password",
        "password_hash": "passwordHash",
        "password_inline_hook": "passwordInlineHook",
        "postal_address": "postalAddress",
        "preferred_language": "preferredLanguage",
        "primary_phone": "primaryPhone",
        "profile_url": "profileUrl",
        "recovery_answer": "recoveryAnswer",
        "recovery_question": "recoveryQuestion",
        "second_email": "secondEmail",
        "state": "state",
        "status": "status",
        "street_address": "streetAddress",
        "timezone": "timezone",
        "title": "title",
        "user_type": "userType",
        "zip_code": "zipCode",
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
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        login: builtins.str,
        admin_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        city: typing.Optional[builtins.str] = None,
        cost_center: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        custom_profile_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        expire_password_on_create: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_memberships: typing.Optional[typing.Sequence[builtins.str]] = None,
        honorific_prefix: typing.Optional[builtins.str] = None,
        honorific_suffix: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locale: typing.Optional[builtins.str] = None,
        manager: typing.Optional[builtins.str] = None,
        manager_id: typing.Optional[builtins.str] = None,
        middle_name: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        nick_name: typing.Optional[builtins.str] = None,
        old_password: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        password_hash: typing.Optional[typing.Union["UserPasswordHash", typing.Dict[str, typing.Any]]] = None,
        password_inline_hook: typing.Optional[builtins.str] = None,
        postal_address: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        primary_phone: typing.Optional[builtins.str] = None,
        profile_url: typing.Optional[builtins.str] = None,
        recovery_answer: typing.Optional[builtins.str] = None,
        recovery_question: typing.Optional[builtins.str] = None,
        second_email: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: User primary email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#email User#email}
        :param first_name: User first name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#first_name User#first_name}
        :param last_name: User last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#last_name User#last_name}
        :param login: User Okta login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#login User#login}
        :param admin_roles: User Okta admin roles - ie. ['APP_ADMIN', 'USER_ADMIN']. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#admin_roles User#admin_roles}
        :param city: User city. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#city User#city}
        :param cost_center: User cost center. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#cost_center User#cost_center}
        :param country_code: User country code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#country_code User#country_code}
        :param custom_profile_attributes: JSON formatted custom attributes for a user. It must be JSON due to various types Okta allows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#custom_profile_attributes User#custom_profile_attributes}
        :param department: User department. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#department User#department}
        :param display_name: User display name, suitable to show end users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#display_name User#display_name}
        :param division: User division. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#division User#division}
        :param employee_number: User employee number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#employee_number User#employee_number}
        :param expire_password_on_create: If set to ``true``, the user will have to change the password at the next login. This property will be used when user is being created and works only when ``password`` field is set Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#expire_password_on_create User#expire_password_on_create}
        :param group_memberships: The groups that you want this user to be a part of. This can also be done via the group using the ``users`` property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#group_memberships User#group_memberships}
        :param honorific_prefix: User honorific prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_prefix User#honorific_prefix}
        :param honorific_suffix: User honorific suffix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_suffix User#honorific_suffix}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locale: User default location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#locale User#locale}
        :param manager: Manager of User. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager User#manager}
        :param manager_id: Manager ID of User. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager_id User#manager_id}
        :param middle_name: User middle name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#middle_name User#middle_name}
        :param mobile_phone: User mobile phone number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#mobile_phone User#mobile_phone}
        :param nick_name: User nickname. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#nick_name User#nick_name}
        :param old_password: Old User Password. Should be only set in case the password was not changed using the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#old_password User#old_password}
        :param organization: User organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#organization User#organization}
        :param password: User Password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password User#password}
        :param password_hash: password_hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_hash User#password_hash}
        :param password_inline_hook: When specified, the Password Inline Hook is triggered to handle verification of the end user's password the first time the user tries to sign in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_inline_hook User#password_inline_hook}
        :param postal_address: User mailing address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#postal_address User#postal_address}
        :param preferred_language: User preferred language. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#preferred_language User#preferred_language}
        :param primary_phone: User primary phone number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#primary_phone User#primary_phone}
        :param profile_url: User online profile (web page). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#profile_url User#profile_url}
        :param recovery_answer: User Password Recovery Answer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_answer User#recovery_answer}
        :param recovery_question: User Password Recovery Question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_question User#recovery_question}
        :param second_email: User secondary email address, used for account recovery. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#second_email User#second_email}
        :param state: User state or region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#state User#state}
        :param status: The status of the User in Okta - remove to set user back to active/provisioned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#status User#status}
        :param street_address: User street address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#street_address User#street_address}
        :param timezone: User default timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#timezone User#timezone}
        :param title: User title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#title User#title}
        :param user_type: User employee type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#user_type User#user_type}
        :param zip_code: User zipcode or postal code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#zip_code User#zip_code}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(password_hash, dict):
            password_hash = UserPasswordHash(**password_hash)
        if __debug__:
            type_hints = typing.get_type_hints(UserConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument admin_roles", value=admin_roles, expected_type=type_hints["admin_roles"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument cost_center", value=cost_center, expected_type=type_hints["cost_center"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument custom_profile_attributes", value=custom_profile_attributes, expected_type=type_hints["custom_profile_attributes"])
            check_type(argname="argument department", value=department, expected_type=type_hints["department"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument division", value=division, expected_type=type_hints["division"])
            check_type(argname="argument employee_number", value=employee_number, expected_type=type_hints["employee_number"])
            check_type(argname="argument expire_password_on_create", value=expire_password_on_create, expected_type=type_hints["expire_password_on_create"])
            check_type(argname="argument group_memberships", value=group_memberships, expected_type=type_hints["group_memberships"])
            check_type(argname="argument honorific_prefix", value=honorific_prefix, expected_type=type_hints["honorific_prefix"])
            check_type(argname="argument honorific_suffix", value=honorific_suffix, expected_type=type_hints["honorific_suffix"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument manager", value=manager, expected_type=type_hints["manager"])
            check_type(argname="argument manager_id", value=manager_id, expected_type=type_hints["manager_id"])
            check_type(argname="argument middle_name", value=middle_name, expected_type=type_hints["middle_name"])
            check_type(argname="argument mobile_phone", value=mobile_phone, expected_type=type_hints["mobile_phone"])
            check_type(argname="argument nick_name", value=nick_name, expected_type=type_hints["nick_name"])
            check_type(argname="argument old_password", value=old_password, expected_type=type_hints["old_password"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument password_hash", value=password_hash, expected_type=type_hints["password_hash"])
            check_type(argname="argument password_inline_hook", value=password_inline_hook, expected_type=type_hints["password_inline_hook"])
            check_type(argname="argument postal_address", value=postal_address, expected_type=type_hints["postal_address"])
            check_type(argname="argument preferred_language", value=preferred_language, expected_type=type_hints["preferred_language"])
            check_type(argname="argument primary_phone", value=primary_phone, expected_type=type_hints["primary_phone"])
            check_type(argname="argument profile_url", value=profile_url, expected_type=type_hints["profile_url"])
            check_type(argname="argument recovery_answer", value=recovery_answer, expected_type=type_hints["recovery_answer"])
            check_type(argname="argument recovery_question", value=recovery_question, expected_type=type_hints["recovery_question"])
            check_type(argname="argument second_email", value=second_email, expected_type=type_hints["second_email"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
            check_type(argname="argument zip_code", value=zip_code, expected_type=type_hints["zip_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "login": login,
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
        if admin_roles is not None:
            self._values["admin_roles"] = admin_roles
        if city is not None:
            self._values["city"] = city
        if cost_center is not None:
            self._values["cost_center"] = cost_center
        if country_code is not None:
            self._values["country_code"] = country_code
        if custom_profile_attributes is not None:
            self._values["custom_profile_attributes"] = custom_profile_attributes
        if department is not None:
            self._values["department"] = department
        if display_name is not None:
            self._values["display_name"] = display_name
        if division is not None:
            self._values["division"] = division
        if employee_number is not None:
            self._values["employee_number"] = employee_number
        if expire_password_on_create is not None:
            self._values["expire_password_on_create"] = expire_password_on_create
        if group_memberships is not None:
            self._values["group_memberships"] = group_memberships
        if honorific_prefix is not None:
            self._values["honorific_prefix"] = honorific_prefix
        if honorific_suffix is not None:
            self._values["honorific_suffix"] = honorific_suffix
        if id is not None:
            self._values["id"] = id
        if locale is not None:
            self._values["locale"] = locale
        if manager is not None:
            self._values["manager"] = manager
        if manager_id is not None:
            self._values["manager_id"] = manager_id
        if middle_name is not None:
            self._values["middle_name"] = middle_name
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if nick_name is not None:
            self._values["nick_name"] = nick_name
        if old_password is not None:
            self._values["old_password"] = old_password
        if organization is not None:
            self._values["organization"] = organization
        if password is not None:
            self._values["password"] = password
        if password_hash is not None:
            self._values["password_hash"] = password_hash
        if password_inline_hook is not None:
            self._values["password_inline_hook"] = password_inline_hook
        if postal_address is not None:
            self._values["postal_address"] = postal_address
        if preferred_language is not None:
            self._values["preferred_language"] = preferred_language
        if primary_phone is not None:
            self._values["primary_phone"] = primary_phone
        if profile_url is not None:
            self._values["profile_url"] = profile_url
        if recovery_answer is not None:
            self._values["recovery_answer"] = recovery_answer
        if recovery_question is not None:
            self._values["recovery_question"] = recovery_question
        if second_email is not None:
            self._values["second_email"] = second_email
        if state is not None:
            self._values["state"] = state
        if status is not None:
            self._values["status"] = status
        if street_address is not None:
            self._values["street_address"] = street_address
        if timezone is not None:
            self._values["timezone"] = timezone
        if title is not None:
            self._values["title"] = title
        if user_type is not None:
            self._values["user_type"] = user_type
        if zip_code is not None:
            self._values["zip_code"] = zip_code

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
        '''User primary email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#email User#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''User first name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#first_name User#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''User last name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#last_name User#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def login(self) -> builtins.str:
        '''User Okta login.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#login User#login}
        '''
        result = self._values.get("login")
        assert result is not None, "Required property 'login' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''User Okta admin roles - ie. ['APP_ADMIN', 'USER_ADMIN'].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#admin_roles User#admin_roles}
        '''
        result = self._values.get("admin_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''User city.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#city User#city}
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cost_center(self) -> typing.Optional[builtins.str]:
        '''User cost center.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#cost_center User#cost_center}
        '''
        result = self._values.get("cost_center")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''User country code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#country_code User#country_code}
        '''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_profile_attributes(self) -> typing.Optional[builtins.str]:
        '''JSON formatted custom attributes for a user. It must be JSON due to various types Okta allows.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#custom_profile_attributes User#custom_profile_attributes}
        '''
        result = self._values.get("custom_profile_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''User department.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#department User#department}
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''User display name, suitable to show end users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#display_name User#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def division(self) -> typing.Optional[builtins.str]:
        '''User division.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#division User#division}
        '''
        result = self._values.get("division")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_number(self) -> typing.Optional[builtins.str]:
        '''User employee number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#employee_number User#employee_number}
        '''
        result = self._values.get("employee_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expire_password_on_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to ``true``, the user will have to change the password at the next login.

        This property will be used when user is being created and works only when ``password`` field is set

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#expire_password_on_create User#expire_password_on_create}
        '''
        result = self._values.get("expire_password_on_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def group_memberships(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The groups that you want this user to be a part of.

        This can also be done via the group using the ``users`` property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#group_memberships User#group_memberships}
        '''
        result = self._values.get("group_memberships")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def honorific_prefix(self) -> typing.Optional[builtins.str]:
        '''User honorific prefix.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_prefix User#honorific_prefix}
        '''
        result = self._values.get("honorific_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def honorific_suffix(self) -> typing.Optional[builtins.str]:
        '''User honorific suffix.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#honorific_suffix User#honorific_suffix}
        '''
        result = self._values.get("honorific_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locale(self) -> typing.Optional[builtins.str]:
        '''User default location.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#locale User#locale}
        '''
        result = self._values.get("locale")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manager(self) -> typing.Optional[builtins.str]:
        '''Manager of User.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager User#manager}
        '''
        result = self._values.get("manager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manager_id(self) -> typing.Optional[builtins.str]:
        '''Manager ID of User.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#manager_id User#manager_id}
        '''
        result = self._values.get("manager_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def middle_name(self) -> typing.Optional[builtins.str]:
        '''User middle name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#middle_name User#middle_name}
        '''
        result = self._values.get("middle_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''User mobile phone number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#mobile_phone User#mobile_phone}
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nick_name(self) -> typing.Optional[builtins.str]:
        '''User nickname.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#nick_name User#nick_name}
        '''
        result = self._values.get("nick_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def old_password(self) -> typing.Optional[builtins.str]:
        '''Old User Password. Should be only set in case the password was not changed using the provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#old_password User#old_password}
        '''
        result = self._values.get("old_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''User organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#organization User#organization}
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''User Password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password User#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_hash(self) -> typing.Optional["UserPasswordHash"]:
        '''password_hash block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_hash User#password_hash}
        '''
        result = self._values.get("password_hash")
        return typing.cast(typing.Optional["UserPasswordHash"], result)

    @builtins.property
    def password_inline_hook(self) -> typing.Optional[builtins.str]:
        '''When specified, the Password Inline Hook is triggered to handle verification of the end user's password the first time the user tries to sign in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#password_inline_hook User#password_inline_hook}
        '''
        result = self._values.get("password_inline_hook")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_address(self) -> typing.Optional[builtins.str]:
        '''User mailing address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#postal_address User#postal_address}
        '''
        result = self._values.get("postal_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_language(self) -> typing.Optional[builtins.str]:
        '''User preferred language.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#preferred_language User#preferred_language}
        '''
        result = self._values.get("preferred_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_phone(self) -> typing.Optional[builtins.str]:
        '''User primary phone number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#primary_phone User#primary_phone}
        '''
        result = self._values.get("primary_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile_url(self) -> typing.Optional[builtins.str]:
        '''User online profile (web page).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#profile_url User#profile_url}
        '''
        result = self._values.get("profile_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_answer(self) -> typing.Optional[builtins.str]:
        '''User Password Recovery Answer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_answer User#recovery_answer}
        '''
        result = self._values.get("recovery_answer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_question(self) -> typing.Optional[builtins.str]:
        '''User Password Recovery Question.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#recovery_question User#recovery_question}
        '''
        result = self._values.get("recovery_question")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def second_email(self) -> typing.Optional[builtins.str]:
        '''User secondary email address, used for account recovery.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#second_email User#second_email}
        '''
        result = self._values.get("second_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''User state or region.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#state User#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the User in Okta - remove to set user back to active/provisioned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#status User#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''User street address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#street_address User#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''User default timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#timezone User#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''User title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#title User#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''User employee type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#user_type User#user_type}
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_code(self) -> typing.Optional[builtins.str]:
        '''User zipcode or postal code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#zip_code User#zip_code}
        '''
        result = self._values.get("zip_code")
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
    jsii_type="@cdktf/provider-okta.user.UserPasswordHash",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "value": "value",
        "salt": "salt",
        "salt_order": "saltOrder",
        "work_factor": "workFactor",
    },
)
class UserPasswordHash:
    def __init__(
        self,
        *,
        algorithm: builtins.str,
        value: builtins.str,
        salt: typing.Optional[builtins.str] = None,
        salt_order: typing.Optional[builtins.str] = None,
        work_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm used to generate the hash using the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#algorithm User#algorithm}
        :param value: For SHA-512, SHA-256, SHA-1, MD5, This is the actual base64-encoded hash of the password (and salt, if used). This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be the the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#value User#value}
        :param salt: Only required for salted hashes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt User#salt}
        :param salt_order: Specifies whether salt was pre- or postfixed to the password before hashing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt_order User#salt_order}
        :param work_factor: Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#work_factor User#work_factor}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UserPasswordHash.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument salt", value=salt, expected_type=type_hints["salt"])
            check_type(argname="argument salt_order", value=salt_order, expected_type=type_hints["salt_order"])
            check_type(argname="argument work_factor", value=work_factor, expected_type=type_hints["work_factor"])
        self._values: typing.Dict[str, typing.Any] = {
            "algorithm": algorithm,
            "value": value,
        }
        if salt is not None:
            self._values["salt"] = salt
        if salt_order is not None:
            self._values["salt_order"] = salt_order
        if work_factor is not None:
            self._values["work_factor"] = work_factor

    @builtins.property
    def algorithm(self) -> builtins.str:
        '''The algorithm used to generate the hash using the password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#algorithm User#algorithm}
        '''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''For SHA-512, SHA-256, SHA-1, MD5, This is the actual base64-encoded hash of the password (and salt, if used).

        This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be the the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#value User#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def salt(self) -> typing.Optional[builtins.str]:
        '''Only required for salted hashes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt User#salt}
        '''
        result = self._values.get("salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def salt_order(self) -> typing.Optional[builtins.str]:
        '''Specifies whether salt was pre- or postfixed to the password before hashing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#salt_order User#salt_order}
        '''
        result = self._values.get("salt_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def work_factor(self) -> typing.Optional[jsii.Number]:
        '''Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/user#work_factor User#work_factor}
        '''
        result = self._values.get("work_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPasswordHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserPasswordHashOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.user.UserPasswordHashOutputReference",
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
            type_hints = typing.get_type_hints(UserPasswordHashOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSalt")
    def reset_salt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalt", []))

    @jsii.member(jsii_name="resetSaltOrder")
    def reset_salt_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaltOrder", []))

    @jsii.member(jsii_name="resetWorkFactor")
    def reset_work_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkFactor", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="saltInput")
    def salt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saltInput"))

    @builtins.property
    @jsii.member(jsii_name="saltOrderInput")
    def salt_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saltOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="workFactorInput")
    def work_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="salt")
    def salt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "salt"))

    @salt.setter
    def salt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "salt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "salt", value)

    @builtins.property
    @jsii.member(jsii_name="saltOrder")
    def salt_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saltOrder"))

    @salt_order.setter
    def salt_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "salt_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saltOrder", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="workFactor")
    def work_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workFactor"))

    @work_factor.setter
    def work_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "work_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workFactor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UserPasswordHash]:
        return typing.cast(typing.Optional[UserPasswordHash], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[UserPasswordHash]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UserPasswordHashOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "User",
    "UserConfig",
    "UserPasswordHash",
    "UserPasswordHashOutputReference",
]

publication.publish()
