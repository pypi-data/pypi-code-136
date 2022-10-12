'''
# `azuread_invitation`

Refer to the Terraform Registory for docs: [`azuread_invitation`](https://www.terraform.io/docs/providers/azuread/r/invitation).
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


class Invitation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.invitation.Invitation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/invitation azuread_invitation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        redirect_url: builtins.str,
        user_email_address: builtins.str,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[typing.Union["InvitationMessage", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["InvitationTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_display_name: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/invitation azuread_invitation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param redirect_url: The URL that the user should be redirected to once the invitation is redeemed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#redirect_url Invitation#redirect_url}
        :param user_email_address: The email address of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_email_address Invitation#user_email_address}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#id Invitation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#message Invitation#message}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#timeouts Invitation#timeouts}
        :param user_display_name: The display name of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_display_name Invitation#user_display_name}
        :param user_type: The user type of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_type Invitation#user_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Invitation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = InvitationConfig(
            redirect_url=redirect_url,
            user_email_address=user_email_address,
            id=id,
            message=message,
            timeouts=timeouts,
            user_display_name=user_display_name,
            user_type=user_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        *,
        additional_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        body: typing.Optional[builtins.str] = None,
        language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_recipients: Email addresses of additional recipients the invitation message should be sent to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#additional_recipients Invitation#additional_recipients}
        :param body: Customized message body you want to send if you don't want to send the default message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#body Invitation#body}
        :param language: The language you want to send the default message in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#language Invitation#language}
        '''
        value = InvitationMessage(
            additional_recipients=additional_recipients, body=body, language=language
        )

        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#create Invitation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#delete Invitation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#read Invitation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#update Invitation#update}.
        '''
        value = InvitationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserDisplayName")
    def reset_user_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDisplayName", []))

    @jsii.member(jsii_name="resetUserType")
    def reset_user_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> "InvitationMessageOutputReference":
        return typing.cast("InvitationMessageOutputReference", jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="redeemUrl")
    def redeem_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redeemUrl"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "InvitationTimeoutsOutputReference":
        return typing.cast("InvitationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional["InvitationMessage"]:
        return typing.cast(typing.Optional["InvitationMessage"], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUrlInput")
    def redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["InvitationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["InvitationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userDisplayNameInput")
    def user_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDisplayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="userEmailAddressInput")
    def user_email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userEmailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="userTypeInput")
    def user_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Invitation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUrl")
    def redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUrl"))

    @redirect_url.setter
    def redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Invitation, "redirect_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="userDisplayName")
    def user_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDisplayName"))

    @user_display_name.setter
    def user_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Invitation, "user_display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="userEmailAddress")
    def user_email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userEmailAddress"))

    @user_email_address.setter
    def user_email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Invitation, "user_email_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userEmailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Invitation, "user_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.invitation.InvitationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "redirect_url": "redirectUrl",
        "user_email_address": "userEmailAddress",
        "id": "id",
        "message": "message",
        "timeouts": "timeouts",
        "user_display_name": "userDisplayName",
        "user_type": "userType",
    },
)
class InvitationConfig(cdktf.TerraformMetaArguments):
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
        redirect_url: builtins.str,
        user_email_address: builtins.str,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[typing.Union["InvitationMessage", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["InvitationTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_display_name: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param redirect_url: The URL that the user should be redirected to once the invitation is redeemed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#redirect_url Invitation#redirect_url}
        :param user_email_address: The email address of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_email_address Invitation#user_email_address}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#id Invitation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#message Invitation#message}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#timeouts Invitation#timeouts}
        :param user_display_name: The display name of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_display_name Invitation#user_display_name}
        :param user_type: The user type of the user being invited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_type Invitation#user_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(message, dict):
            message = InvitationMessage(**message)
        if isinstance(timeouts, dict):
            timeouts = InvitationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(InvitationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument redirect_url", value=redirect_url, expected_type=type_hints["redirect_url"])
            check_type(argname="argument user_email_address", value=user_email_address, expected_type=type_hints["user_email_address"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_display_name", value=user_display_name, expected_type=type_hints["user_display_name"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "redirect_url": redirect_url,
            "user_email_address": user_email_address,
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
        if id is not None:
            self._values["id"] = id
        if message is not None:
            self._values["message"] = message
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_display_name is not None:
            self._values["user_display_name"] = user_display_name
        if user_type is not None:
            self._values["user_type"] = user_type

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
    def redirect_url(self) -> builtins.str:
        '''The URL that the user should be redirected to once the invitation is redeemed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#redirect_url Invitation#redirect_url}
        '''
        result = self._values.get("redirect_url")
        assert result is not None, "Required property 'redirect_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_email_address(self) -> builtins.str:
        '''The email address of the user being invited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_email_address Invitation#user_email_address}
        '''
        result = self._values.get("user_email_address")
        assert result is not None, "Required property 'user_email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#id Invitation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional["InvitationMessage"]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#message Invitation#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional["InvitationMessage"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["InvitationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#timeouts Invitation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["InvitationTimeouts"], result)

    @builtins.property
    def user_display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the user being invited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_display_name Invitation#user_display_name}
        '''
        result = self._values.get("user_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''The user type of the user being invited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#user_type Invitation#user_type}
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvitationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.invitation.InvitationMessage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_recipients": "additionalRecipients",
        "body": "body",
        "language": "language",
    },
)
class InvitationMessage:
    def __init__(
        self,
        *,
        additional_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        body: typing.Optional[builtins.str] = None,
        language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_recipients: Email addresses of additional recipients the invitation message should be sent to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#additional_recipients Invitation#additional_recipients}
        :param body: Customized message body you want to send if you don't want to send the default message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#body Invitation#body}
        :param language: The language you want to send the default message in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#language Invitation#language}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InvitationMessage.__init__)
            check_type(argname="argument additional_recipients", value=additional_recipients, expected_type=type_hints["additional_recipients"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_recipients is not None:
            self._values["additional_recipients"] = additional_recipients
        if body is not None:
            self._values["body"] = body
        if language is not None:
            self._values["language"] = language

    @builtins.property
    def additional_recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Email addresses of additional recipients the invitation message should be sent to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#additional_recipients Invitation#additional_recipients}
        '''
        result = self._values.get("additional_recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''Customized message body you want to send if you don't want to send the default message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#body Invitation#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language(self) -> typing.Optional[builtins.str]:
        '''The language you want to send the default message in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#language Invitation#language}
        '''
        result = self._values.get("language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvitationMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InvitationMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.invitation.InvitationMessageOutputReference",
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
            type_hints = typing.get_type_hints(InvitationMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdditionalRecipients")
    def reset_additional_recipients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalRecipients", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetLanguage")
    def reset_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguage", []))

    @builtins.property
    @jsii.member(jsii_name="additionalRecipientsInput")
    def additional_recipients_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalRecipientsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="languageInput")
    def language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalRecipients")
    def additional_recipients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalRecipients"))

    @additional_recipients.setter
    def additional_recipients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationMessageOutputReference, "additional_recipients").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalRecipients", value)

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationMessageOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="language")
    def language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "language"))

    @language.setter
    def language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationMessageOutputReference, "language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "language", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InvitationMessage]:
        return typing.cast(typing.Optional[InvitationMessage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InvitationMessage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.invitation.InvitationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class InvitationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#create Invitation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#delete Invitation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#read Invitation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#update Invitation#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InvitationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#create Invitation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#delete Invitation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#read Invitation#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/invitation#update Invitation#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvitationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InvitationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.invitation.InvitationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(InvitationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(InvitationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InvitationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InvitationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InvitationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InvitationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Invitation",
    "InvitationConfig",
    "InvitationMessage",
    "InvitationMessageOutputReference",
    "InvitationTimeouts",
    "InvitationTimeoutsOutputReference",
]

publication.publish()
