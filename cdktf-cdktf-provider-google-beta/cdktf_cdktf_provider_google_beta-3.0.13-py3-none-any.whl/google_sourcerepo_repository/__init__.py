'''
# `google_sourcerepo_repository`

Refer to the Terraform Registory for docs: [`google_sourcerepo_repository`](https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository).
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


class GoogleSourcerepoRepository(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepository",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository google_sourcerepo_repository}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSourcerepoRepositoryPubsubConfigs", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSourcerepoRepositoryTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository google_sourcerepo_repository} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#name GoogleSourcerepoRepository#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#id GoogleSourcerepoRepository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#project GoogleSourcerepoRepository#project}.
        :param pubsub_configs: pubsub_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#pubsub_configs GoogleSourcerepoRepository#pubsub_configs}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#timeouts GoogleSourcerepoRepository#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepository.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleSourcerepoRepositoryConfig(
            name=name,
            id=id,
            project=project,
            pubsub_configs=pubsub_configs,
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

    @jsii.member(jsii_name="putPubsubConfigs")
    def put_pubsub_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSourcerepoRepositoryPubsubConfigs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepository.put_pubsub_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPubsubConfigs", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#create GoogleSourcerepoRepository#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#delete GoogleSourcerepoRepository#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#update GoogleSourcerepoRepository#update}.
        '''
        value = GoogleSourcerepoRepositoryTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPubsubConfigs")
    def reset_pubsub_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubsubConfigs", []))

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
    @jsii.member(jsii_name="pubsubConfigs")
    def pubsub_configs(self) -> "GoogleSourcerepoRepositoryPubsubConfigsList":
        return typing.cast("GoogleSourcerepoRepositoryPubsubConfigsList", jsii.get(self, "pubsubConfigs"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleSourcerepoRepositoryTimeoutsOutputReference":
        return typing.cast("GoogleSourcerepoRepositoryTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pubsubConfigsInput")
    def pubsub_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSourcerepoRepositoryPubsubConfigs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSourcerepoRepositoryPubsubConfigs"]]], jsii.get(self, "pubsubConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleSourcerepoRepositoryTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleSourcerepoRepositoryTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepository, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepository, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepository, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryConfig",
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
        "id": "id",
        "project": "project",
        "pubsub_configs": "pubsubConfigs",
        "timeouts": "timeouts",
    },
)
class GoogleSourcerepoRepositoryConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSourcerepoRepositoryPubsubConfigs", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSourcerepoRepositoryTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#name GoogleSourcerepoRepository#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#id GoogleSourcerepoRepository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#project GoogleSourcerepoRepository#project}.
        :param pubsub_configs: pubsub_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#pubsub_configs GoogleSourcerepoRepository#pubsub_configs}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#timeouts GoogleSourcerepoRepository#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleSourcerepoRepositoryTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument pubsub_configs", value=pubsub_configs, expected_type=type_hints["pubsub_configs"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if pubsub_configs is not None:
            self._values["pubsub_configs"] = pubsub_configs
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
    def name(self) -> builtins.str:
        '''Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#name GoogleSourcerepoRepository#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#id GoogleSourcerepoRepository#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#project GoogleSourcerepoRepository#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pubsub_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSourcerepoRepositoryPubsubConfigs"]]]:
        '''pubsub_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#pubsub_configs GoogleSourcerepoRepository#pubsub_configs}
        '''
        result = self._values.get("pubsub_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSourcerepoRepositoryPubsubConfigs"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleSourcerepoRepositoryTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#timeouts GoogleSourcerepoRepository#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleSourcerepoRepositoryTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSourcerepoRepositoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryPubsubConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "message_format": "messageFormat",
        "topic": "topic",
        "service_account_email": "serviceAccountEmail",
    },
)
class GoogleSourcerepoRepositoryPubsubConfigs:
    def __init__(
        self,
        *,
        message_format: builtins.str,
        topic: builtins.str,
        service_account_email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message_format: The format of the Cloud Pub/Sub messages. - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent. - JSON: The message payload is a JSON string of SourceRepoEvent. Possible values: ["PROTOBUF", "JSON"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#message_format GoogleSourcerepoRepository#message_format}
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#topic GoogleSourcerepoRepository#topic}.
        :param service_account_email: Email address of the service account used for publishing Cloud Pub/Sub messages. This service account needs to be in the same project as the PubsubConfig. When added, the caller needs to have iam.serviceAccounts.actAs permission on this service account. If unspecified, it defaults to the compute engine default service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#service_account_email GoogleSourcerepoRepository#service_account_email}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryPubsubConfigs.__init__)
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_format": message_format,
            "topic": topic,
        }
        if service_account_email is not None:
            self._values["service_account_email"] = service_account_email

    @builtins.property
    def message_format(self) -> builtins.str:
        '''The format of the Cloud Pub/Sub messages.

        - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
        - JSON: The message payload is a JSON string of SourceRepoEvent. Possible values: ["PROTOBUF", "JSON"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#message_format GoogleSourcerepoRepository#message_format}
        '''
        result = self._values.get("message_format")
        assert result is not None, "Required property 'message_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#topic GoogleSourcerepoRepository#topic}.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account_email(self) -> typing.Optional[builtins.str]:
        '''Email address of the service account used for publishing Cloud Pub/Sub messages.

        This service account needs to be in the same project as the PubsubConfig. When added,
        the caller needs to have iam.serviceAccounts.actAs permission on this service account.
        If unspecified, it defaults to the compute engine default service account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#service_account_email GoogleSourcerepoRepository#service_account_email}
        '''
        result = self._values.get("service_account_email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSourcerepoRepositoryPubsubConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSourcerepoRepositoryPubsubConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryPubsubConfigsList",
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
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryPubsubConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSourcerepoRepositoryPubsubConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryPubsubConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSourcerepoRepositoryPubsubConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSourcerepoRepositoryPubsubConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSourcerepoRepositoryPubsubConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSourcerepoRepositoryPubsubConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSourcerepoRepositoryPubsubConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryPubsubConfigsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryPubsubConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetServiceAccountEmail")
    def reset_service_account_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountEmail", []))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsOutputReference, "message_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsOutputReference, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSourcerepoRepositoryPubsubConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSourcerepoRepositoryPubsubConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSourcerepoRepositoryPubsubConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryPubsubConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleSourcerepoRepositoryTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#create GoogleSourcerepoRepository#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#delete GoogleSourcerepoRepository#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#update GoogleSourcerepoRepository#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#create GoogleSourcerepoRepository#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#delete GoogleSourcerepoRepository#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sourcerepo_repository#update GoogleSourcerepoRepository#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSourcerepoRepositoryTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSourcerepoRepositoryTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSourcerepoRepository.GoogleSourcerepoRepositoryTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSourcerepoRepositoryTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSourcerepoRepositoryTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSourcerepoRepositoryTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSourcerepoRepositoryTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSourcerepoRepositoryTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleSourcerepoRepository",
    "GoogleSourcerepoRepositoryConfig",
    "GoogleSourcerepoRepositoryPubsubConfigs",
    "GoogleSourcerepoRepositoryPubsubConfigsList",
    "GoogleSourcerepoRepositoryPubsubConfigsOutputReference",
    "GoogleSourcerepoRepositoryTimeouts",
    "GoogleSourcerepoRepositoryTimeoutsOutputReference",
]

publication.publish()
