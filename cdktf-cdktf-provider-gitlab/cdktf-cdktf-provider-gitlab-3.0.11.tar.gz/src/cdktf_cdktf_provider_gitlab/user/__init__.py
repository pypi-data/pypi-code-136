'''
# `gitlab_user`

Refer to the Terraform Registory for docs: [`gitlab_user`](https://www.terraform.io/docs/providers/gitlab/r/user).
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
    jsii_type="@cdktf/provider-gitlab.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/user gitlab_user}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        email: builtins.str,
        name: builtins.str,
        username: builtins.str,
        can_create_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_admin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_external: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace_id: typing.Optional[jsii.Number] = None,
        note: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        projects_limit: typing.Optional[jsii.Number] = None,
        reset_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_confirmation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/user gitlab_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: The e-mail address of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#email User#email}
        :param name: The name of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#name User#name}
        :param username: The username of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#username User#username}
        :param can_create_group: Boolean, defaults to false. Whether to allow the user to create groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#can_create_group User#can_create_group}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_admin: Boolean, defaults to false. Whether to enable administrative privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_admin User#is_admin}
        :param is_external: Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_external User#is_external}
        :param namespace_id: The ID of the user's namespace. Available since GitLab 14.10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#namespace_id User#namespace_id}
        :param note: The note associated to the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#note User#note}
        :param password: The password of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#password User#password}
        :param projects_limit: Integer, defaults to 0. Number of projects user can create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#projects_limit User#projects_limit}
        :param reset_password: Boolean, defaults to false. Send user password reset link. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#reset_password User#reset_password}
        :param skip_confirmation: Boolean, defaults to true. Whether to skip confirmation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#skip_confirmation User#skip_confirmation}
        :param state: String, defaults to 'active'. The state of the user account. Valid values are ``active``, ``deactivated``, ``blocked``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#state User#state}
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
            name=name,
            username=username,
            can_create_group=can_create_group,
            id=id,
            is_admin=is_admin,
            is_external=is_external,
            namespace_id=namespace_id,
            note=note,
            password=password,
            projects_limit=projects_limit,
            reset_password=reset_password,
            skip_confirmation=skip_confirmation,
            state=state,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCanCreateGroup")
    def reset_can_create_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanCreateGroup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsAdmin")
    def reset_is_admin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsAdmin", []))

    @jsii.member(jsii_name="resetIsExternal")
    def reset_is_external(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsExternal", []))

    @jsii.member(jsii_name="resetNamespaceId")
    def reset_namespace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceId", []))

    @jsii.member(jsii_name="resetNote")
    def reset_note(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNote", []))

    @jsii.member(jsii_name="resetProjectsLimit")
    def reset_projects_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectsLimit", []))

    @jsii.member(jsii_name="resetResetPassword")
    def reset_reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetPassword", []))

    @jsii.member(jsii_name="resetSkipConfirmation")
    def reset_skip_confirmation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipConfirmation", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetTfPassword")
    def reset_tf_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTfPassword", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="canCreateGroupInput")
    def can_create_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "canCreateGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isAdminInput")
    def is_admin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="isExternalInput")
    def is_external_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isExternalInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="noteInput")
    def note_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="projectsLimitInput")
    def projects_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "projectsLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="resetPasswordInput")
    def reset_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "resetPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="skipConfirmationInput")
    def skip_confirmation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipConfirmationInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="canCreateGroup")
    def can_create_group(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "canCreateGroup"))

    @can_create_group.setter
    def can_create_group(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "can_create_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "canCreateGroup", value)

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
    @jsii.member(jsii_name="isExternal")
    def is_external(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isExternal"))

    @is_external.setter
    def is_external(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "is_external").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isExternal", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "namespace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="note")
    def note(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "note"))

    @note.setter
    def note(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "note").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "note", value)

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
    @jsii.member(jsii_name="projectsLimit")
    def projects_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectsLimit"))

    @projects_limit.setter
    def projects_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "projects_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectsLimit", value)

    @builtins.property
    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "resetPassword"))

    @reset_password.setter
    def reset_password(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "reset_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resetPassword", value)

    @builtins.property
    @jsii.member(jsii_name="skipConfirmation")
    def skip_confirmation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipConfirmation"))

    @skip_confirmation.setter
    def skip_confirmation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "skip_confirmation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipConfirmation", value)

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
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(User, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.user.UserConfig",
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
        "name": "name",
        "username": "username",
        "can_create_group": "canCreateGroup",
        "id": "id",
        "is_admin": "isAdmin",
        "is_external": "isExternal",
        "namespace_id": "namespaceId",
        "note": "note",
        "password": "password",
        "projects_limit": "projectsLimit",
        "reset_password": "resetPassword",
        "skip_confirmation": "skipConfirmation",
        "state": "state",
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
        name: builtins.str,
        username: builtins.str,
        can_create_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_admin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_external: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace_id: typing.Optional[jsii.Number] = None,
        note: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        projects_limit: typing.Optional[jsii.Number] = None,
        reset_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_confirmation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: The e-mail address of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#email User#email}
        :param name: The name of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#name User#name}
        :param username: The username of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#username User#username}
        :param can_create_group: Boolean, defaults to false. Whether to allow the user to create groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#can_create_group User#can_create_group}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_admin: Boolean, defaults to false. Whether to enable administrative privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_admin User#is_admin}
        :param is_external: Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_external User#is_external}
        :param namespace_id: The ID of the user's namespace. Available since GitLab 14.10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#namespace_id User#namespace_id}
        :param note: The note associated to the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#note User#note}
        :param password: The password of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#password User#password}
        :param projects_limit: Integer, defaults to 0. Number of projects user can create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#projects_limit User#projects_limit}
        :param reset_password: Boolean, defaults to false. Send user password reset link. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#reset_password User#reset_password}
        :param skip_confirmation: Boolean, defaults to true. Whether to skip confirmation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#skip_confirmation User#skip_confirmation}
        :param state: String, defaults to 'active'. The state of the user account. Valid values are ``active``, ``deactivated``, ``blocked``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#state User#state}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument can_create_group", value=can_create_group, expected_type=type_hints["can_create_group"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_admin", value=is_admin, expected_type=type_hints["is_admin"])
            check_type(argname="argument is_external", value=is_external, expected_type=type_hints["is_external"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
            check_type(argname="argument note", value=note, expected_type=type_hints["note"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument projects_limit", value=projects_limit, expected_type=type_hints["projects_limit"])
            check_type(argname="argument reset_password", value=reset_password, expected_type=type_hints["reset_password"])
            check_type(argname="argument skip_confirmation", value=skip_confirmation, expected_type=type_hints["skip_confirmation"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
            "name": name,
            "username": username,
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
        if can_create_group is not None:
            self._values["can_create_group"] = can_create_group
        if id is not None:
            self._values["id"] = id
        if is_admin is not None:
            self._values["is_admin"] = is_admin
        if is_external is not None:
            self._values["is_external"] = is_external
        if namespace_id is not None:
            self._values["namespace_id"] = namespace_id
        if note is not None:
            self._values["note"] = note
        if password is not None:
            self._values["password"] = password
        if projects_limit is not None:
            self._values["projects_limit"] = projects_limit
        if reset_password is not None:
            self._values["reset_password"] = reset_password
        if skip_confirmation is not None:
            self._values["skip_confirmation"] = skip_confirmation
        if state is not None:
            self._values["state"] = state

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
        '''The e-mail address of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#email User#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#name User#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#username User#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def can_create_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean, defaults to false. Whether to allow the user to create groups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#can_create_group User#can_create_group}
        '''
        result = self._values.get("can_create_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_admin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean, defaults to false.  Whether to enable administrative privileges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_admin User#is_admin}
        '''
        result = self._values.get("is_admin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_external(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean, defaults to false.

        Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#is_external User#is_external}
        '''
        result = self._values.get("is_external")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def namespace_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the user's namespace. Available since GitLab 14.10.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#namespace_id User#namespace_id}
        '''
        result = self._values.get("namespace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def note(self) -> typing.Optional[builtins.str]:
        '''The note associated to the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#note User#note}
        '''
        result = self._values.get("note")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#password User#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def projects_limit(self) -> typing.Optional[jsii.Number]:
        '''Integer, defaults to 0.  Number of projects user can create.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#projects_limit User#projects_limit}
        '''
        result = self._values.get("projects_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reset_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean, defaults to false. Send user password reset link.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#reset_password User#reset_password}
        '''
        result = self._values.get("reset_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def skip_confirmation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean, defaults to true. Whether to skip confirmation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#skip_confirmation User#skip_confirmation}
        '''
        result = self._values.get("skip_confirmation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''String, defaults to 'active'. The state of the user account. Valid values are ``active``, ``deactivated``, ``blocked``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/user#state User#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "User",
    "UserConfig",
]

publication.publish()
