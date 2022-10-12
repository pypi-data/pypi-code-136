'''
# `google_secret_manager_secret`

Refer to the Terraform Registory for docs: [`google_secret_manager_secret`](https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret).
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


class GoogleSecretManagerSecret(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecret",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret google_secret_manager_secret}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        replication: typing.Union["GoogleSecretManagerSecretReplication", typing.Dict[str, typing.Any]],
        secret_id: builtins.str,
        expire_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        rotation: typing.Optional[typing.Union["GoogleSecretManagerSecretRotation", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSecretManagerSecretTimeouts", typing.Dict[str, typing.Any]]] = None,
        topics: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretTopics", typing.Dict[str, typing.Any]]]]] = None,
        ttl: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret google_secret_manager_secret} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param replication: replication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replication GoogleSecretManagerSecret#replication}
        :param secret_id: This must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#secret_id GoogleSecretManagerSecret#secret_id}
        :param expire_time: Timestamp in UTC when the Secret is scheduled to expire. This is always provided on output, regardless of what was sent on input. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#expire_time GoogleSecretManagerSecret#expire_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#id GoogleSecretManagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62} Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be assigned to a given resource. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#labels GoogleSecretManagerSecret#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#project GoogleSecretManagerSecret#project}.
        :param rotation: rotation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation GoogleSecretManagerSecret#rotation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#timeouts GoogleSecretManagerSecret#timeouts}
        :param topics: topics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#topics GoogleSecretManagerSecret#topics}
        :param ttl: The TTL for the Secret. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#ttl GoogleSecretManagerSecret#ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleSecretManagerSecretConfig(
            replication=replication,
            secret_id=secret_id,
            expire_time=expire_time,
            id=id,
            labels=labels,
            project=project,
            rotation=rotation,
            timeouts=timeouts,
            topics=topics,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putReplication")
    def put_replication(
        self,
        *,
        automatic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_managed: typing.Optional[typing.Union["GoogleSecretManagerSecretReplicationUserManaged", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automatic: The Secret will automatically be replicated without any restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#automatic GoogleSecretManagerSecret#automatic}
        :param user_managed: user_managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#user_managed GoogleSecretManagerSecret#user_managed}
        '''
        value = GoogleSecretManagerSecretReplication(
            automatic=automatic, user_managed=user_managed
        )

        return typing.cast(None, jsii.invoke(self, "putReplication", [value]))

    @jsii.member(jsii_name="putRotation")
    def put_rotation(
        self,
        *,
        next_rotation_time: typing.Optional[builtins.str] = None,
        rotation_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param next_rotation_time: Timestamp in UTC at which the Secret is scheduled to rotate. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#next_rotation_time GoogleSecretManagerSecret#next_rotation_time}
        :param rotation_period: The Duration between rotation notifications. Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years). If rotationPeriod is set, 'next_rotation_time' must be set. 'next_rotation_time' will be advanced by this period when the service automatically sends rotation notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation_period GoogleSecretManagerSecret#rotation_period}
        '''
        value = GoogleSecretManagerSecretRotation(
            next_rotation_time=next_rotation_time, rotation_period=rotation_period
        )

        return typing.cast(None, jsii.invoke(self, "putRotation", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#create GoogleSecretManagerSecret#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#delete GoogleSecretManagerSecret#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#update GoogleSecretManagerSecret#update}.
        '''
        value = GoogleSecretManagerSecretTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTopics")
    def put_topics(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretTopics", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecret.put_topics)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTopics", [value]))

    @jsii.member(jsii_name="resetExpireTime")
    def reset_expire_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpireTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRotation")
    def reset_rotation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotation", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTopics")
    def reset_topics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopics", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="replication")
    def replication(self) -> "GoogleSecretManagerSecretReplicationOutputReference":
        return typing.cast("GoogleSecretManagerSecretReplicationOutputReference", jsii.get(self, "replication"))

    @builtins.property
    @jsii.member(jsii_name="rotation")
    def rotation(self) -> "GoogleSecretManagerSecretRotationOutputReference":
        return typing.cast("GoogleSecretManagerSecretRotationOutputReference", jsii.get(self, "rotation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleSecretManagerSecretTimeoutsOutputReference":
        return typing.cast("GoogleSecretManagerSecretTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> "GoogleSecretManagerSecretTopicsList":
        return typing.cast("GoogleSecretManagerSecretTopicsList", jsii.get(self, "topics"))

    @builtins.property
    @jsii.member(jsii_name="expireTimeInput")
    def expire_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expireTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationInput")
    def replication_input(
        self,
    ) -> typing.Optional["GoogleSecretManagerSecretReplication"]:
        return typing.cast(typing.Optional["GoogleSecretManagerSecretReplication"], jsii.get(self, "replicationInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationInput")
    def rotation_input(self) -> typing.Optional["GoogleSecretManagerSecretRotation"]:
        return typing.cast(typing.Optional["GoogleSecretManagerSecretRotation"], jsii.get(self, "rotationInput"))

    @builtins.property
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleSecretManagerSecretTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleSecretManagerSecretTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicsInput")
    def topics_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretTopics"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretTopics"]]], jsii.get(self, "topicsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expireTime"))

    @expire_time.setter
    def expire_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "expire_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expireTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretId", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecret, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "replication": "replication",
        "secret_id": "secretId",
        "expire_time": "expireTime",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "rotation": "rotation",
        "timeouts": "timeouts",
        "topics": "topics",
        "ttl": "ttl",
    },
)
class GoogleSecretManagerSecretConfig(cdktf.TerraformMetaArguments):
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
        replication: typing.Union["GoogleSecretManagerSecretReplication", typing.Dict[str, typing.Any]],
        secret_id: builtins.str,
        expire_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        rotation: typing.Optional[typing.Union["GoogleSecretManagerSecretRotation", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSecretManagerSecretTimeouts", typing.Dict[str, typing.Any]]] = None,
        topics: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretTopics", typing.Dict[str, typing.Any]]]]] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param replication: replication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replication GoogleSecretManagerSecret#replication}
        :param secret_id: This must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#secret_id GoogleSecretManagerSecret#secret_id}
        :param expire_time: Timestamp in UTC when the Secret is scheduled to expire. This is always provided on output, regardless of what was sent on input. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#expire_time GoogleSecretManagerSecret#expire_time}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#id GoogleSecretManagerSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62} Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be assigned to a given resource. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#labels GoogleSecretManagerSecret#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#project GoogleSecretManagerSecret#project}.
        :param rotation: rotation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation GoogleSecretManagerSecret#rotation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#timeouts GoogleSecretManagerSecret#timeouts}
        :param topics: topics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#topics GoogleSecretManagerSecret#topics}
        :param ttl: The TTL for the Secret. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#ttl GoogleSecretManagerSecret#ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(replication, dict):
            replication = GoogleSecretManagerSecretReplication(**replication)
        if isinstance(rotation, dict):
            rotation = GoogleSecretManagerSecretRotation(**rotation)
        if isinstance(timeouts, dict):
            timeouts = GoogleSecretManagerSecretTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument replication", value=replication, expected_type=type_hints["replication"])
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            check_type(argname="argument expire_time", value=expire_time, expected_type=type_hints["expire_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument rotation", value=rotation, expected_type=type_hints["rotation"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "replication": replication,
            "secret_id": secret_id,
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
        if expire_time is not None:
            self._values["expire_time"] = expire_time
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if rotation is not None:
            self._values["rotation"] = rotation
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if topics is not None:
            self._values["topics"] = topics
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def replication(self) -> "GoogleSecretManagerSecretReplication":
        '''replication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replication GoogleSecretManagerSecret#replication}
        '''
        result = self._values.get("replication")
        assert result is not None, "Required property 'replication' is missing"
        return typing.cast("GoogleSecretManagerSecretReplication", result)

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''This must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#secret_id GoogleSecretManagerSecret#secret_id}
        '''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expire_time(self) -> typing.Optional[builtins.str]:
        '''Timestamp in UTC when the Secret is scheduled to expire.

        This is always provided on output, regardless of what was sent on input.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#expire_time GoogleSecretManagerSecret#expire_time}
        '''
        result = self._values.get("expire_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#id GoogleSecretManagerSecret#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The labels assigned to this Secret.

        Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes,
        and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62}

        Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes,
        and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}

        No more than 64 labels can be assigned to a given resource.

        An object containing a list of "key": value pairs. Example:
        { "name": "wrench", "mass": "1.3kg", "count": "3" }.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#labels GoogleSecretManagerSecret#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#project GoogleSecretManagerSecret#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation(self) -> typing.Optional["GoogleSecretManagerSecretRotation"]:
        '''rotation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation GoogleSecretManagerSecret#rotation}
        '''
        result = self._values.get("rotation")
        return typing.cast(typing.Optional["GoogleSecretManagerSecretRotation"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleSecretManagerSecretTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#timeouts GoogleSecretManagerSecret#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleSecretManagerSecretTimeouts"], result)

    @builtins.property
    def topics(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretTopics"]]]:
        '''topics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#topics GoogleSecretManagerSecret#topics}
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretTopics"]]], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''The TTL for the Secret. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#ttl GoogleSecretManagerSecret#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplication",
    jsii_struct_bases=[],
    name_mapping={"automatic": "automatic", "user_managed": "userManaged"},
)
class GoogleSecretManagerSecretReplication:
    def __init__(
        self,
        *,
        automatic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_managed: typing.Optional[typing.Union["GoogleSecretManagerSecretReplicationUserManaged", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automatic: The Secret will automatically be replicated without any restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#automatic GoogleSecretManagerSecret#automatic}
        :param user_managed: user_managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#user_managed GoogleSecretManagerSecret#user_managed}
        '''
        if isinstance(user_managed, dict):
            user_managed = GoogleSecretManagerSecretReplicationUserManaged(**user_managed)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplication.__init__)
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
            check_type(argname="argument user_managed", value=user_managed, expected_type=type_hints["user_managed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automatic is not None:
            self._values["automatic"] = automatic
        if user_managed is not None:
            self._values["user_managed"] = user_managed

    @builtins.property
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The Secret will automatically be replicated without any restrictions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#automatic GoogleSecretManagerSecret#automatic}
        '''
        result = self._values.get("automatic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_managed(
        self,
    ) -> typing.Optional["GoogleSecretManagerSecretReplicationUserManaged"]:
        '''user_managed block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#user_managed GoogleSecretManagerSecret#user_managed}
        '''
        result = self._values.get("user_managed")
        return typing.cast(typing.Optional["GoogleSecretManagerSecretReplicationUserManaged"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretReplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretReplicationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putUserManaged")
    def put_user_managed(
        self,
        *,
        replicas: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretReplicationUserManagedReplicas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param replicas: replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replicas GoogleSecretManagerSecret#replicas}
        '''
        value = GoogleSecretManagerSecretReplicationUserManaged(replicas=replicas)

        return typing.cast(None, jsii.invoke(self, "putUserManaged", [value]))

    @jsii.member(jsii_name="resetAutomatic")
    def reset_automatic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomatic", []))

    @jsii.member(jsii_name="resetUserManaged")
    def reset_user_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserManaged", []))

    @builtins.property
    @jsii.member(jsii_name="userManaged")
    def user_managed(
        self,
    ) -> "GoogleSecretManagerSecretReplicationUserManagedOutputReference":
        return typing.cast("GoogleSecretManagerSecretReplicationUserManagedOutputReference", jsii.get(self, "userManaged"))

    @builtins.property
    @jsii.member(jsii_name="automaticInput")
    def automatic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticInput"))

    @builtins.property
    @jsii.member(jsii_name="userManagedInput")
    def user_managed_input(
        self,
    ) -> typing.Optional["GoogleSecretManagerSecretReplicationUserManaged"]:
        return typing.cast(typing.Optional["GoogleSecretManagerSecretReplicationUserManaged"], jsii.get(self, "userManagedInput"))

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automatic"))

    @automatic.setter
    def automatic(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationOutputReference, "automatic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSecretManagerSecretReplication]:
        return typing.cast(typing.Optional[GoogleSecretManagerSecretReplication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecretManagerSecretReplication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManaged",
    jsii_struct_bases=[],
    name_mapping={"replicas": "replicas"},
)
class GoogleSecretManagerSecretReplicationUserManaged:
    def __init__(
        self,
        *,
        replicas: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretReplicationUserManagedReplicas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param replicas: replicas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replicas GoogleSecretManagerSecret#replicas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManaged.__init__)
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
        self._values: typing.Dict[str, typing.Any] = {
            "replicas": replicas,
        }

    @builtins.property
    def replicas(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretReplicationUserManagedReplicas"]]:
        '''replicas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#replicas GoogleSecretManagerSecret#replicas}
        '''
        result = self._values.get("replicas")
        assert result is not None, "Required property 'replicas' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretReplicationUserManagedReplicas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretReplicationUserManaged(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretReplicationUserManagedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putReplicas")
    def put_replicas(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSecretManagerSecretReplicationUserManagedReplicas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedOutputReference.put_replicas)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putReplicas", [value]))

    @builtins.property
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> "GoogleSecretManagerSecretReplicationUserManagedReplicasList":
        return typing.cast("GoogleSecretManagerSecretReplicationUserManagedReplicasList", jsii.get(self, "replicas"))

    @builtins.property
    @jsii.member(jsii_name="replicasInput")
    def replicas_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretReplicationUserManagedReplicas"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSecretManagerSecretReplicationUserManagedReplicas"]]], jsii.get(self, "replicasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecretManagerSecretReplicationUserManaged]:
        return typing.cast(typing.Optional[GoogleSecretManagerSecretReplicationUserManaged], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecretManagerSecretReplicationUserManaged],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedReplicas",
    jsii_struct_bases=[],
    name_mapping={
        "location": "location",
        "customer_managed_encryption": "customerManagedEncryption",
    },
)
class GoogleSecretManagerSecretReplicationUserManagedReplicas:
    def __init__(
        self,
        *,
        location: builtins.str,
        customer_managed_encryption: typing.Optional[typing.Union["GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param location: The canonical IDs of the location to replicate data. For example: "us-east1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#location GoogleSecretManagerSecret#location}
        :param customer_managed_encryption: customer_managed_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#customer_managed_encryption GoogleSecretManagerSecret#customer_managed_encryption}
        '''
        if isinstance(customer_managed_encryption, dict):
            customer_managed_encryption = GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption(**customer_managed_encryption)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicas.__init__)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument customer_managed_encryption", value=customer_managed_encryption, expected_type=type_hints["customer_managed_encryption"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
        }
        if customer_managed_encryption is not None:
            self._values["customer_managed_encryption"] = customer_managed_encryption

    @builtins.property
    def location(self) -> builtins.str:
        '''The canonical IDs of the location to replicate data. For example: "us-east1".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#location GoogleSecretManagerSecret#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_managed_encryption(
        self,
    ) -> typing.Optional["GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption"]:
        '''customer_managed_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#customer_managed_encryption GoogleSecretManagerSecret#customer_managed_encryption}
        '''
        result = self._values.get("customer_managed_encryption")
        return typing.cast(typing.Optional["GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretReplicationUserManagedReplicas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#kms_key_name GoogleSecretManagerSecret#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Describes the Cloud KMS encryption key that will be used to protect destination secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#kms_key_name GoogleSecretManagerSecret#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption]:
        return typing.cast(typing.Optional[GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSecretManagerSecretReplicationUserManagedReplicasList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedReplicasList",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicasList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicasList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretReplicationUserManagedReplicas]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretReplicationUserManagedReplicas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretReplicationUserManagedReplicas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomerManagedEncryption")
    def put_customer_managed_encryption(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#kms_key_name GoogleSecretManagerSecret#kms_key_name}
        '''
        value = GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption(
            kms_key_name=kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerManagedEncryption", [value]))

    @jsii.member(jsii_name="resetCustomerManagedEncryption")
    def reset_customer_managed_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedEncryption", []))

    @builtins.property
    @jsii.member(jsii_name="customerManagedEncryption")
    def customer_managed_encryption(
        self,
    ) -> GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference:
        return typing.cast(GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference, jsii.get(self, "customerManagedEncryption"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedEncryptionInput")
    def customer_managed_encryption_input(
        self,
    ) -> typing.Optional[GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption]:
        return typing.cast(typing.Optional[GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption], jsii.get(self, "customerManagedEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSecretManagerSecretReplicationUserManagedReplicas, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSecretManagerSecretReplicationUserManagedReplicas, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSecretManagerSecretReplicationUserManagedReplicas, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretRotation",
    jsii_struct_bases=[],
    name_mapping={
        "next_rotation_time": "nextRotationTime",
        "rotation_period": "rotationPeriod",
    },
)
class GoogleSecretManagerSecretRotation:
    def __init__(
        self,
        *,
        next_rotation_time: typing.Optional[builtins.str] = None,
        rotation_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param next_rotation_time: Timestamp in UTC at which the Secret is scheduled to rotate. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#next_rotation_time GoogleSecretManagerSecret#next_rotation_time}
        :param rotation_period: The Duration between rotation notifications. Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years). If rotationPeriod is set, 'next_rotation_time' must be set. 'next_rotation_time' will be advanced by this period when the service automatically sends rotation notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation_period GoogleSecretManagerSecret#rotation_period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretRotation.__init__)
            check_type(argname="argument next_rotation_time", value=next_rotation_time, expected_type=type_hints["next_rotation_time"])
            check_type(argname="argument rotation_period", value=rotation_period, expected_type=type_hints["rotation_period"])
        self._values: typing.Dict[str, typing.Any] = {}
        if next_rotation_time is not None:
            self._values["next_rotation_time"] = next_rotation_time
        if rotation_period is not None:
            self._values["rotation_period"] = rotation_period

    @builtins.property
    def next_rotation_time(self) -> typing.Optional[builtins.str]:
        '''Timestamp in UTC at which the Secret is scheduled to rotate.

        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#next_rotation_time GoogleSecretManagerSecret#next_rotation_time}
        '''
        result = self._values.get("next_rotation_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation_period(self) -> typing.Optional[builtins.str]:
        '''The Duration between rotation notifications.

        Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years).
        If rotationPeriod is set, 'next_rotation_time' must be set. 'next_rotation_time' will be advanced by this period when the service automatically sends rotation notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#rotation_period GoogleSecretManagerSecret#rotation_period}
        '''
        result = self._values.get("rotation_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretRotation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretRotationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretRotationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretRotationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNextRotationTime")
    def reset_next_rotation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextRotationTime", []))

    @jsii.member(jsii_name="resetRotationPeriod")
    def reset_rotation_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="nextRotationTimeInput")
    def next_rotation_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextRotationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationPeriodInput")
    def rotation_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="nextRotationTime")
    def next_rotation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextRotationTime"))

    @next_rotation_time.setter
    def next_rotation_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretRotationOutputReference, "next_rotation_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextRotationTime", value)

    @builtins.property
    @jsii.member(jsii_name="rotationPeriod")
    def rotation_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationPeriod"))

    @rotation_period.setter
    def rotation_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretRotationOutputReference, "rotation_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSecretManagerSecretRotation]:
        return typing.cast(typing.Optional[GoogleSecretManagerSecretRotation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecretManagerSecretRotation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretRotationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleSecretManagerSecretTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#create GoogleSecretManagerSecret#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#delete GoogleSecretManagerSecret#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#update GoogleSecretManagerSecret#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#create GoogleSecretManagerSecret#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#delete GoogleSecretManagerSecret#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#update GoogleSecretManagerSecret#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSecretManagerSecretTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSecretManagerSecretTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSecretManagerSecretTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretTopics",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleSecretManagerSecretTopics:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: The resource name of the Pub/Sub topic that will be published to, in the following format: projects/*/topics/*. For publication to succeed, the Secret Manager Service Agent service account must have pubsub.publisher permissions on the topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#name GoogleSecretManagerSecret#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTopics.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The resource name of the Pub/Sub topic that will be published to, in the following format: projects/*/topics/*.

        For publication to succeed, the Secret Manager Service Agent service account must have pubsub.publisher permissions on the topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_secret_manager_secret#name GoogleSecretManagerSecret#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecretManagerSecretTopics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecretManagerSecretTopicsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretTopicsList",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTopicsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSecretManagerSecretTopicsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTopicsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSecretManagerSecretTopicsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretTopics]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretTopics]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSecretManagerSecretTopics]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSecretManagerSecretTopicsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecretManagerSecret.GoogleSecretManagerSecretTopicsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecretManagerSecretTopicsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSecretManagerSecretTopics, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSecretManagerSecretTopics, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSecretManagerSecretTopics, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecretManagerSecretTopicsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleSecretManagerSecret",
    "GoogleSecretManagerSecretConfig",
    "GoogleSecretManagerSecretReplication",
    "GoogleSecretManagerSecretReplicationOutputReference",
    "GoogleSecretManagerSecretReplicationUserManaged",
    "GoogleSecretManagerSecretReplicationUserManagedOutputReference",
    "GoogleSecretManagerSecretReplicationUserManagedReplicas",
    "GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryption",
    "GoogleSecretManagerSecretReplicationUserManagedReplicasCustomerManagedEncryptionOutputReference",
    "GoogleSecretManagerSecretReplicationUserManagedReplicasList",
    "GoogleSecretManagerSecretReplicationUserManagedReplicasOutputReference",
    "GoogleSecretManagerSecretRotation",
    "GoogleSecretManagerSecretRotationOutputReference",
    "GoogleSecretManagerSecretTimeouts",
    "GoogleSecretManagerSecretTimeoutsOutputReference",
    "GoogleSecretManagerSecretTopics",
    "GoogleSecretManagerSecretTopicsList",
    "GoogleSecretManagerSecretTopicsOutputReference",
]

publication.publish()
