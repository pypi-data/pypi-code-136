'''
# `google_project_access_approval_settings`

Refer to the Terraform Registory for docs: [`google_project_access_approval_settings`](https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings).
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


class GoogleProjectAccessApprovalSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings google_project_access_approval_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        enrolled_services: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleProjectAccessApprovalSettingsEnrolledServices", typing.Dict[str, typing.Any]]]],
        project_id: builtins.str,
        active_key_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleProjectAccessApprovalSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings google_project_access_approval_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enrolled_services: enrolled_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#enrolled_services GoogleProjectAccessApprovalSettings#enrolled_services}
        :param project_id: ID of the project of the access approval settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project_id GoogleProjectAccessApprovalSettings#project_id}
        :param active_key_version: The asymmetric crypto key version to use for signing approval requests. Empty active_key_version indicates that a Google-managed key should be used for signing. This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#active_key_version GoogleProjectAccessApprovalSettings#active_key_version}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#id GoogleProjectAccessApprovalSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_emails: A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email addresses are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#notification_emails GoogleProjectAccessApprovalSettings#notification_emails}
        :param project: Deprecated in favor of 'project_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project GoogleProjectAccessApprovalSettings#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#timeouts GoogleProjectAccessApprovalSettings#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettings.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleProjectAccessApprovalSettingsConfig(
            enrolled_services=enrolled_services,
            project_id=project_id,
            active_key_version=active_key_version,
            id=id,
            notification_emails=notification_emails,
            project=project,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEnrolledServices")
    def put_enrolled_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleProjectAccessApprovalSettingsEnrolledServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettings.put_enrolled_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnrolledServices", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#create GoogleProjectAccessApprovalSettings#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#delete GoogleProjectAccessApprovalSettings#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#update GoogleProjectAccessApprovalSettings#update}.
        '''
        value = GoogleProjectAccessApprovalSettingsTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActiveKeyVersion")
    def reset_active_key_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveKeyVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationEmails")
    def reset_notification_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmails", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ancestorHasActiveKeyVersion")
    def ancestor_has_active_key_version(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "ancestorHasActiveKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="enrolledAncestor")
    def enrolled_ancestor(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enrolledAncestor"))

    @builtins.property
    @jsii.member(jsii_name="enrolledServices")
    def enrolled_services(
        self,
    ) -> "GoogleProjectAccessApprovalSettingsEnrolledServicesList":
        return typing.cast("GoogleProjectAccessApprovalSettingsEnrolledServicesList", jsii.get(self, "enrolledServices"))

    @builtins.property
    @jsii.member(jsii_name="invalidKeyVersion")
    def invalid_key_version(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "invalidKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleProjectAccessApprovalSettingsTimeoutsOutputReference":
        return typing.cast("GoogleProjectAccessApprovalSettingsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activeKeyVersionInput")
    def active_key_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeKeyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="enrolledServicesInput")
    def enrolled_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleProjectAccessApprovalSettingsEnrolledServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleProjectAccessApprovalSettingsEnrolledServices"]]], jsii.get(self, "enrolledServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailsInput")
    def notification_emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEmailsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleProjectAccessApprovalSettingsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleProjectAccessApprovalSettingsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="activeKeyVersion")
    def active_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeKeyVersion"))

    @active_key_version.setter
    def active_key_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettings, "active_key_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeKeyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettings, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmails")
    def notification_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEmails"))

    @notification_emails.setter
    def notification_emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettings, "notification_emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmails", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettings, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettings, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enrolled_services": "enrolledServices",
        "project_id": "projectId",
        "active_key_version": "activeKeyVersion",
        "id": "id",
        "notification_emails": "notificationEmails",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleProjectAccessApprovalSettingsConfig(cdktf.TerraformMetaArguments):
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
        enrolled_services: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleProjectAccessApprovalSettingsEnrolledServices", typing.Dict[str, typing.Any]]]],
        project_id: builtins.str,
        active_key_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleProjectAccessApprovalSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param enrolled_services: enrolled_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#enrolled_services GoogleProjectAccessApprovalSettings#enrolled_services}
        :param project_id: ID of the project of the access approval settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project_id GoogleProjectAccessApprovalSettings#project_id}
        :param active_key_version: The asymmetric crypto key version to use for signing approval requests. Empty active_key_version indicates that a Google-managed key should be used for signing. This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#active_key_version GoogleProjectAccessApprovalSettings#active_key_version}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#id GoogleProjectAccessApprovalSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_emails: A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email addresses are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#notification_emails GoogleProjectAccessApprovalSettings#notification_emails}
        :param project: Deprecated in favor of 'project_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project GoogleProjectAccessApprovalSettings#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#timeouts GoogleProjectAccessApprovalSettings#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleProjectAccessApprovalSettingsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enrolled_services", value=enrolled_services, expected_type=type_hints["enrolled_services"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument active_key_version", value=active_key_version, expected_type=type_hints["active_key_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_emails", value=notification_emails, expected_type=type_hints["notification_emails"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "enrolled_services": enrolled_services,
            "project_id": project_id,
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
        if active_key_version is not None:
            self._values["active_key_version"] = active_key_version
        if id is not None:
            self._values["id"] = id
        if notification_emails is not None:
            self._values["notification_emails"] = notification_emails
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def enrolled_services(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleProjectAccessApprovalSettingsEnrolledServices"]]:
        '''enrolled_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#enrolled_services GoogleProjectAccessApprovalSettings#enrolled_services}
        '''
        result = self._values.get("enrolled_services")
        assert result is not None, "Required property 'enrolled_services' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleProjectAccessApprovalSettingsEnrolledServices"]], result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''ID of the project of the access approval settings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project_id GoogleProjectAccessApprovalSettings#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_key_version(self) -> typing.Optional[builtins.str]:
        '''The asymmetric crypto key version to use for signing approval requests.

        Empty active_key_version indicates that a Google-managed key should be used for signing.
        This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#active_key_version GoogleProjectAccessApprovalSettings#active_key_version}
        '''
        result = self._values.get("active_key_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#id GoogleProjectAccessApprovalSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of email addresses to which notifications relating to approval requests should be sent.

        Notifications relating to a resource will be sent to all emails in the settings of ancestor
        resources of that resource. A maximum of 50 email addresses are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#notification_emails GoogleProjectAccessApprovalSettings#notification_emails}
        '''
        result = self._values.get("notification_emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Deprecated in favor of 'project_id'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#project GoogleProjectAccessApprovalSettings#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleProjectAccessApprovalSettingsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#timeouts GoogleProjectAccessApprovalSettings#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleProjectAccessApprovalSettingsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectAccessApprovalSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsEnrolledServices",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_product": "cloudProduct",
        "enrollment_level": "enrollmentLevel",
    },
)
class GoogleProjectAccessApprovalSettingsEnrolledServices:
    def __init__(
        self,
        *,
        cloud_product: builtins.str,
        enrollment_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_product: The product for which Access Approval will be enrolled. Allowed values are listed (case-sensitive): all appengine.googleapis.com bigquery.googleapis.com bigtable.googleapis.com cloudkms.googleapis.com compute.googleapis.com dataflow.googleapis.com iam.googleapis.com pubsub.googleapis.com storage.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#cloud_product GoogleProjectAccessApprovalSettings#cloud_product}
        :param enrollment_level: The enrollment level of the service. Default value: "BLOCK_ALL" Possible values: ["BLOCK_ALL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#enrollment_level GoogleProjectAccessApprovalSettings#enrollment_level}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsEnrolledServices.__init__)
            check_type(argname="argument cloud_product", value=cloud_product, expected_type=type_hints["cloud_product"])
            check_type(argname="argument enrollment_level", value=enrollment_level, expected_type=type_hints["enrollment_level"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloud_product": cloud_product,
        }
        if enrollment_level is not None:
            self._values["enrollment_level"] = enrollment_level

    @builtins.property
    def cloud_product(self) -> builtins.str:
        '''The product for which Access Approval will be enrolled. Allowed values are listed (case-sensitive): all appengine.googleapis.com bigquery.googleapis.com bigtable.googleapis.com cloudkms.googleapis.com compute.googleapis.com dataflow.googleapis.com iam.googleapis.com pubsub.googleapis.com storage.googleapis.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#cloud_product GoogleProjectAccessApprovalSettings#cloud_product}
        '''
        result = self._values.get("cloud_product")
        assert result is not None, "Required property 'cloud_product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enrollment_level(self) -> typing.Optional[builtins.str]:
        '''The enrollment level of the service. Default value: "BLOCK_ALL" Possible values: ["BLOCK_ALL"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#enrollment_level GoogleProjectAccessApprovalSettings#enrollment_level}
        '''
        result = self._values.get("enrollment_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectAccessApprovalSettingsEnrolledServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectAccessApprovalSettingsEnrolledServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsEnrolledServicesList",
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
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsEnrolledServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsEnrolledServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleProjectAccessApprovalSettingsEnrolledServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleProjectAccessApprovalSettingsEnrolledServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleProjectAccessApprovalSettingsEnrolledServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnrollmentLevel")
    def reset_enrollment_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnrollmentLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudProductInput")
    def cloud_product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudProductInput"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentLevelInput")
    def enrollment_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enrollmentLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudProduct")
    def cloud_product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudProduct"))

    @cloud_product.setter
    def cloud_product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference, "cloud_product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudProduct", value)

    @builtins.property
    @jsii.member(jsii_name="enrollmentLevel")
    def enrollment_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enrollmentLevel"))

    @enrollment_level.setter
    def enrollment_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference, "enrollment_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrollmentLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsEnrolledServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsEnrolledServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsEnrolledServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleProjectAccessApprovalSettingsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#create GoogleProjectAccessApprovalSettings#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#delete GoogleProjectAccessApprovalSettings#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#update GoogleProjectAccessApprovalSettings#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#create GoogleProjectAccessApprovalSettings#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#delete GoogleProjectAccessApprovalSettings#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_access_approval_settings#update GoogleProjectAccessApprovalSettings#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectAccessApprovalSettingsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectAccessApprovalSettingsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectAccessApprovalSettings.GoogleProjectAccessApprovalSettingsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectAccessApprovalSettingsTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleProjectAccessApprovalSettingsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectAccessApprovalSettingsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleProjectAccessApprovalSettings",
    "GoogleProjectAccessApprovalSettingsConfig",
    "GoogleProjectAccessApprovalSettingsEnrolledServices",
    "GoogleProjectAccessApprovalSettingsEnrolledServicesList",
    "GoogleProjectAccessApprovalSettingsEnrolledServicesOutputReference",
    "GoogleProjectAccessApprovalSettingsTimeouts",
    "GoogleProjectAccessApprovalSettingsTimeoutsOutputReference",
]

publication.publish()
