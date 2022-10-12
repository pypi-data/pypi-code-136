'''
# `google_sql_user`

Refer to the Terraform Registory for docs: [`google_sql_user`](https://www.terraform.io/docs/providers/google-beta/r/google_sql_user).
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


class GoogleSqlUser(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUser",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user google_sql_user}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        instance: builtins.str,
        name: builtins.str,
        deletion_policy: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[typing.Union["GoogleSqlUserPasswordPolicy", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        sql_server_user_details: typing.Optional[typing.Union["GoogleSqlUserSqlServerUserDetails", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSqlUserTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user google_sql_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance: The name of the Cloud SQL instance. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#instance GoogleSqlUser#instance}
        :param name: The name of the user. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#name GoogleSqlUser#name}
        :param deletion_policy: The deletion policy for the user. Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for Postgres, where users cannot be deleted from the API if they have been granted SQL roles. Possible values are: "ABANDON". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#deletion_policy GoogleSqlUser#deletion_policy}
        :param host: The host the user can connect from. This is only supported for MySQL instances. Don't set this field for PostgreSQL instances. Can be an IP address. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#host GoogleSqlUser#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#id GoogleSqlUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: The password for the user. Can be updated. For Postgres instances this is a Required field, unless type is set to either CLOUD_IAM_USER or CLOUD_IAM_SERVICE_ACCOUNT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password GoogleSqlUser#password}
        :param password_policy: password_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_policy GoogleSqlUser#password_policy}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#project GoogleSqlUser#project}
        :param sql_server_user_details: sql_server_user_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#sql_server_user_details GoogleSqlUser#sql_server_user_details}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#timeouts GoogleSqlUser#timeouts}
        :param type: The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type. Flags include "BUILT_IN", "CLOUD_IAM_USER", or "CLOUD_IAM_SERVICE_ACCOUNT". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#type GoogleSqlUser#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUser.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleSqlUserConfig(
            instance=instance,
            name=name,
            deletion_policy=deletion_policy,
            host=host,
            id=id,
            password=password,
            password_policy=password_policy,
            project=project,
            sql_server_user_details=sql_server_user_details,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPasswordPolicy")
    def put_password_policy(
        self,
        *,
        allowed_failed_attempts: typing.Optional[jsii.Number] = None,
        enable_failed_attempts_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_password_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_expiration_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_failed_attempts: Number of failed attempts allowed before the user get locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#allowed_failed_attempts GoogleSqlUser#allowed_failed_attempts}
        :param enable_failed_attempts_check: If true, the check that will lock user after too many failed login attempts will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_failed_attempts_check GoogleSqlUser#enable_failed_attempts_check}
        :param enable_password_verification: If true, the user must specify the current password before changing the password. This flag is supported only for MySQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_password_verification GoogleSqlUser#enable_password_verification}
        :param password_expiration_duration: Password expiration duration with one week grace period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_expiration_duration GoogleSqlUser#password_expiration_duration}
        '''
        value = GoogleSqlUserPasswordPolicy(
            allowed_failed_attempts=allowed_failed_attempts,
            enable_failed_attempts_check=enable_failed_attempts_check,
            enable_password_verification=enable_password_verification,
            password_expiration_duration=password_expiration_duration,
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordPolicy", [value]))

    @jsii.member(jsii_name="putSqlServerUserDetails")
    def put_sql_server_user_details(
        self,
        *,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disabled: If the user has been disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#disabled GoogleSqlUser#disabled}
        :param server_roles: The server roles for this user in the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#server_roles GoogleSqlUser#server_roles}
        '''
        value = GoogleSqlUserSqlServerUserDetails(
            disabled=disabled, server_roles=server_roles
        )

        return typing.cast(None, jsii.invoke(self, "putSqlServerUserDetails", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#create GoogleSqlUser#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#delete GoogleSqlUser#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#update GoogleSqlUser#update}.
        '''
        value = GoogleSqlUserTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDeletionPolicy")
    def reset_deletion_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionPolicy", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPasswordPolicy")
    def reset_password_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordPolicy", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSqlServerUserDetails")
    def reset_sql_server_user_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlServerUserDetails", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicy")
    def password_policy(self) -> "GoogleSqlUserPasswordPolicyOutputReference":
        return typing.cast("GoogleSqlUserPasswordPolicyOutputReference", jsii.get(self, "passwordPolicy"))

    @builtins.property
    @jsii.member(jsii_name="sqlServerUserDetails")
    def sql_server_user_details(
        self,
    ) -> "GoogleSqlUserSqlServerUserDetailsOutputReference":
        return typing.cast("GoogleSqlUserSqlServerUserDetailsOutputReference", jsii.get(self, "sqlServerUserDetails"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleSqlUserTimeoutsOutputReference":
        return typing.cast("GoogleSqlUserTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="deletionPolicyInput")
    def deletion_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deletionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInput")
    def instance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicyInput")
    def password_policy_input(self) -> typing.Optional["GoogleSqlUserPasswordPolicy"]:
        return typing.cast(typing.Optional["GoogleSqlUserPasswordPolicy"], jsii.get(self, "passwordPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlServerUserDetailsInput")
    def sql_server_user_details_input(
        self,
    ) -> typing.Optional["GoogleSqlUserSqlServerUserDetails"]:
        return typing.cast(typing.Optional["GoogleSqlUserSqlServerUserDetails"], jsii.get(self, "sqlServerUserDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleSqlUserTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleSqlUserTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionPolicy")
    def deletion_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deletionPolicy"))

    @deletion_policy.setter
    def deletion_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "deletion_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @instance.setter
    def instance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instance", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUser, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance": "instance",
        "name": "name",
        "deletion_policy": "deletionPolicy",
        "host": "host",
        "id": "id",
        "password": "password",
        "password_policy": "passwordPolicy",
        "project": "project",
        "sql_server_user_details": "sqlServerUserDetails",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class GoogleSqlUserConfig(cdktf.TerraformMetaArguments):
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
        instance: builtins.str,
        name: builtins.str,
        deletion_policy: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[typing.Union["GoogleSqlUserPasswordPolicy", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        sql_server_user_details: typing.Optional[typing.Union["GoogleSqlUserSqlServerUserDetails", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSqlUserTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance: The name of the Cloud SQL instance. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#instance GoogleSqlUser#instance}
        :param name: The name of the user. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#name GoogleSqlUser#name}
        :param deletion_policy: The deletion policy for the user. Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for Postgres, where users cannot be deleted from the API if they have been granted SQL roles. Possible values are: "ABANDON". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#deletion_policy GoogleSqlUser#deletion_policy}
        :param host: The host the user can connect from. This is only supported for MySQL instances. Don't set this field for PostgreSQL instances. Can be an IP address. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#host GoogleSqlUser#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#id GoogleSqlUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: The password for the user. Can be updated. For Postgres instances this is a Required field, unless type is set to either CLOUD_IAM_USER or CLOUD_IAM_SERVICE_ACCOUNT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password GoogleSqlUser#password}
        :param password_policy: password_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_policy GoogleSqlUser#password_policy}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#project GoogleSqlUser#project}
        :param sql_server_user_details: sql_server_user_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#sql_server_user_details GoogleSqlUser#sql_server_user_details}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#timeouts GoogleSqlUser#timeouts}
        :param type: The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type. Flags include "BUILT_IN", "CLOUD_IAM_USER", or "CLOUD_IAM_SERVICE_ACCOUNT". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#type GoogleSqlUser#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(password_policy, dict):
            password_policy = GoogleSqlUserPasswordPolicy(**password_policy)
        if isinstance(sql_server_user_details, dict):
            sql_server_user_details = GoogleSqlUserSqlServerUserDetails(**sql_server_user_details)
        if isinstance(timeouts, dict):
            timeouts = GoogleSqlUserTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUserConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument deletion_policy", value=deletion_policy, expected_type=type_hints["deletion_policy"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument password_policy", value=password_policy, expected_type=type_hints["password_policy"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument sql_server_user_details", value=sql_server_user_details, expected_type=type_hints["sql_server_user_details"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance": instance,
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
        if deletion_policy is not None:
            self._values["deletion_policy"] = deletion_policy
        if host is not None:
            self._values["host"] = host
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if password_policy is not None:
            self._values["password_policy"] = password_policy
        if project is not None:
            self._values["project"] = project
        if sql_server_user_details is not None:
            self._values["sql_server_user_details"] = sql_server_user_details
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
    def instance(self) -> builtins.str:
        '''The name of the Cloud SQL instance. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#instance GoogleSqlUser#instance}
        '''
        result = self._values.get("instance")
        assert result is not None, "Required property 'instance' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the user. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#name GoogleSqlUser#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_policy(self) -> typing.Optional[builtins.str]:
        '''The deletion policy for the user.

        Setting ABANDON allows the resource
        to be abandoned rather than deleted. This is useful for Postgres, where users cannot be deleted from the API if they
        have been granted SQL roles. Possible values are: "ABANDON".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#deletion_policy GoogleSqlUser#deletion_policy}
        '''
        result = self._values.get("deletion_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The host the user can connect from.

        This is only supported for MySQL instances. Don't set this field for PostgreSQL instances. Can be an IP address. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#host GoogleSqlUser#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#id GoogleSqlUser#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the user.

        Can be updated. For Postgres instances this is a Required field, unless type is set to
        either CLOUD_IAM_USER or CLOUD_IAM_SERVICE_ACCOUNT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password GoogleSqlUser#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_policy(self) -> typing.Optional["GoogleSqlUserPasswordPolicy"]:
        '''password_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_policy GoogleSqlUser#password_policy}
        '''
        result = self._values.get("password_policy")
        return typing.cast(typing.Optional["GoogleSqlUserPasswordPolicy"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#project GoogleSqlUser#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_server_user_details(
        self,
    ) -> typing.Optional["GoogleSqlUserSqlServerUserDetails"]:
        '''sql_server_user_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#sql_server_user_details GoogleSqlUser#sql_server_user_details}
        '''
        result = self._values.get("sql_server_user_details")
        return typing.cast(typing.Optional["GoogleSqlUserSqlServerUserDetails"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleSqlUserTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#timeouts GoogleSqlUser#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleSqlUserTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The user type.

        It determines the method to authenticate the user during login.
        The default is the database's built-in user type. Flags include "BUILT_IN", "CLOUD_IAM_USER", or "CLOUD_IAM_SERVICE_ACCOUNT".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#type GoogleSqlUser#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserPasswordPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_failed_attempts": "allowedFailedAttempts",
        "enable_failed_attempts_check": "enableFailedAttemptsCheck",
        "enable_password_verification": "enablePasswordVerification",
        "password_expiration_duration": "passwordExpirationDuration",
    },
)
class GoogleSqlUserPasswordPolicy:
    def __init__(
        self,
        *,
        allowed_failed_attempts: typing.Optional[jsii.Number] = None,
        enable_failed_attempts_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_password_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password_expiration_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_failed_attempts: Number of failed attempts allowed before the user get locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#allowed_failed_attempts GoogleSqlUser#allowed_failed_attempts}
        :param enable_failed_attempts_check: If true, the check that will lock user after too many failed login attempts will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_failed_attempts_check GoogleSqlUser#enable_failed_attempts_check}
        :param enable_password_verification: If true, the user must specify the current password before changing the password. This flag is supported only for MySQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_password_verification GoogleSqlUser#enable_password_verification}
        :param password_expiration_duration: Password expiration duration with one week grace period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_expiration_duration GoogleSqlUser#password_expiration_duration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUserPasswordPolicy.__init__)
            check_type(argname="argument allowed_failed_attempts", value=allowed_failed_attempts, expected_type=type_hints["allowed_failed_attempts"])
            check_type(argname="argument enable_failed_attempts_check", value=enable_failed_attempts_check, expected_type=type_hints["enable_failed_attempts_check"])
            check_type(argname="argument enable_password_verification", value=enable_password_verification, expected_type=type_hints["enable_password_verification"])
            check_type(argname="argument password_expiration_duration", value=password_expiration_duration, expected_type=type_hints["password_expiration_duration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_failed_attempts is not None:
            self._values["allowed_failed_attempts"] = allowed_failed_attempts
        if enable_failed_attempts_check is not None:
            self._values["enable_failed_attempts_check"] = enable_failed_attempts_check
        if enable_password_verification is not None:
            self._values["enable_password_verification"] = enable_password_verification
        if password_expiration_duration is not None:
            self._values["password_expiration_duration"] = password_expiration_duration

    @builtins.property
    def allowed_failed_attempts(self) -> typing.Optional[jsii.Number]:
        '''Number of failed attempts allowed before the user get locked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#allowed_failed_attempts GoogleSqlUser#allowed_failed_attempts}
        '''
        result = self._values.get("allowed_failed_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_failed_attempts_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the check that will lock user after too many failed login attempts will be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_failed_attempts_check GoogleSqlUser#enable_failed_attempts_check}
        '''
        result = self._values.get("enable_failed_attempts_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_password_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the user must specify the current password before changing the password.

        This flag is supported only for MySQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#enable_password_verification GoogleSqlUser#enable_password_verification}
        '''
        result = self._values.get("enable_password_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password_expiration_duration(self) -> typing.Optional[builtins.str]:
        '''Password expiration duration with one week grace period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#password_expiration_duration GoogleSqlUser#password_expiration_duration}
        '''
        result = self._values.get("password_expiration_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlUserPasswordPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlUserPasswordPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserPasswordPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlUserPasswordPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedFailedAttempts")
    def reset_allowed_failed_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFailedAttempts", []))

    @jsii.member(jsii_name="resetEnableFailedAttemptsCheck")
    def reset_enable_failed_attempts_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFailedAttemptsCheck", []))

    @jsii.member(jsii_name="resetEnablePasswordVerification")
    def reset_enable_password_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePasswordVerification", []))

    @jsii.member(jsii_name="resetPasswordExpirationDuration")
    def reset_password_expiration_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExpirationDuration", []))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "GoogleSqlUserPasswordPolicyStatusList":
        return typing.cast("GoogleSqlUserPasswordPolicyStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="allowedFailedAttemptsInput")
    def allowed_failed_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allowedFailedAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableFailedAttemptsCheckInput")
    def enable_failed_attempts_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFailedAttemptsCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePasswordVerificationInput")
    def enable_password_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePasswordVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpirationDurationInput")
    def password_expiration_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordExpirationDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFailedAttempts")
    def allowed_failed_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allowedFailedAttempts"))

    @allowed_failed_attempts.setter
    def allowed_failed_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyOutputReference, "allowed_failed_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedFailedAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="enableFailedAttemptsCheck")
    def enable_failed_attempts_check(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFailedAttemptsCheck"))

    @enable_failed_attempts_check.setter
    def enable_failed_attempts_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyOutputReference, "enable_failed_attempts_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFailedAttemptsCheck", value)

    @builtins.property
    @jsii.member(jsii_name="enablePasswordVerification")
    def enable_password_verification(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePasswordVerification"))

    @enable_password_verification.setter
    def enable_password_verification(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyOutputReference, "enable_password_verification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePasswordVerification", value)

    @builtins.property
    @jsii.member(jsii_name="passwordExpirationDuration")
    def password_expiration_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordExpirationDuration"))

    @password_expiration_duration.setter
    def password_expiration_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyOutputReference, "password_expiration_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExpirationDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlUserPasswordPolicy]:
        return typing.cast(typing.Optional[GoogleSqlUserPasswordPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlUserPasswordPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserPasswordPolicyStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleSqlUserPasswordPolicyStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlUserPasswordPolicyStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlUserPasswordPolicyStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserPasswordPolicyStatusList",
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
            type_hints = typing.get_type_hints(GoogleSqlUserPasswordPolicyStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSqlUserPasswordPolicyStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUserPasswordPolicyStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSqlUserPasswordPolicyStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyStatusList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyStatusList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleSqlUserPasswordPolicyStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserPasswordPolicyStatusOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlUserPasswordPolicyStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "locked"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpirationTime")
    def password_expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordExpirationTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlUserPasswordPolicyStatus]:
        return typing.cast(typing.Optional[GoogleSqlUserPasswordPolicyStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlUserPasswordPolicyStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserPasswordPolicyStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserSqlServerUserDetails",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled", "server_roles": "serverRoles"},
)
class GoogleSqlUserSqlServerUserDetails:
    def __init__(
        self,
        *,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disabled: If the user has been disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#disabled GoogleSqlUser#disabled}
        :param server_roles: The server roles for this user in the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#server_roles GoogleSqlUser#server_roles}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUserSqlServerUserDetails.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument server_roles", value=server_roles, expected_type=type_hints["server_roles"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled is not None:
            self._values["disabled"] = disabled
        if server_roles is not None:
            self._values["server_roles"] = server_roles

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the user has been disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#disabled GoogleSqlUser#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The server roles for this user in the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#server_roles GoogleSqlUser#server_roles}
        '''
        result = self._values.get("server_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlUserSqlServerUserDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlUserSqlServerUserDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserSqlServerUserDetailsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlUserSqlServerUserDetailsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetServerRoles")
    def reset_server_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerRoles", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="serverRolesInput")
    def server_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserSqlServerUserDetailsOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="serverRoles")
    def server_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serverRoles"))

    @server_roles.setter
    def server_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserSqlServerUserDetailsOutputReference, "server_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverRoles", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlUserSqlServerUserDetails]:
        return typing.cast(typing.Optional[GoogleSqlUserSqlServerUserDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlUserSqlServerUserDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserSqlServerUserDetailsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleSqlUserTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#create GoogleSqlUser#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#delete GoogleSqlUser#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#update GoogleSqlUser#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlUserTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#create GoogleSqlUser#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#delete GoogleSqlUser#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_user#update GoogleSqlUser#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlUserTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlUserTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlUser.GoogleSqlUserTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlUserTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSqlUserTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSqlUserTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSqlUserTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlUserTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleSqlUser",
    "GoogleSqlUserConfig",
    "GoogleSqlUserPasswordPolicy",
    "GoogleSqlUserPasswordPolicyOutputReference",
    "GoogleSqlUserPasswordPolicyStatus",
    "GoogleSqlUserPasswordPolicyStatusList",
    "GoogleSqlUserPasswordPolicyStatusOutputReference",
    "GoogleSqlUserSqlServerUserDetails",
    "GoogleSqlUserSqlServerUserDetailsOutputReference",
    "GoogleSqlUserTimeouts",
    "GoogleSqlUserTimeoutsOutputReference",
]

publication.publish()
