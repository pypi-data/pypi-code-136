'''
# `google_pubsub_lite_topic`

Refer to the Terraform Registory for docs: [`google_pubsub_lite_topic`](https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic).
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


class GooglePubsubLiteTopic(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic google_pubsub_lite_topic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        partition_config: typing.Optional[typing.Union["GooglePubsubLiteTopicPartitionConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        reservation_config: typing.Optional[typing.Union["GooglePubsubLiteTopicReservationConfig", typing.Dict[str, typing.Any]]] = None,
        retention_config: typing.Optional[typing.Union["GooglePubsubLiteTopicRetentionConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubLiteTopicTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic google_pubsub_lite_topic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#name GooglePubsubLiteTopic#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#id GooglePubsubLiteTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_config: partition_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#partition_config GooglePubsubLiteTopic#partition_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#project GooglePubsubLiteTopic#project}.
        :param region: The region of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#region GooglePubsubLiteTopic#region}
        :param reservation_config: reservation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#reservation_config GooglePubsubLiteTopic#reservation_config}
        :param retention_config: retention_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#retention_config GooglePubsubLiteTopic#retention_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#timeouts GooglePubsubLiteTopic#timeouts}
        :param zone: The zone of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#zone GooglePubsubLiteTopic#zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopic.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GooglePubsubLiteTopicConfig(
            name=name,
            id=id,
            partition_config=partition_config,
            project=project,
            region=region,
            reservation_config=reservation_config,
            retention_config=retention_config,
            timeouts=timeouts,
            zone=zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPartitionConfig")
    def put_partition_config(
        self,
        *,
        count: jsii.Number,
        capacity: typing.Optional[typing.Union["GooglePubsubLiteTopicPartitionConfigCapacity", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param count: The number of partitions in the topic. Must be at least 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#count GooglePubsubLiteTopic#count}
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#capacity GooglePubsubLiteTopic#capacity}
        '''
        value = GooglePubsubLiteTopicPartitionConfig(count=count, capacity=capacity)

        return typing.cast(None, jsii.invoke(self, "putPartitionConfig", [value]))

    @jsii.member(jsii_name="putReservationConfig")
    def put_reservation_config(
        self,
        *,
        throughput_reservation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param throughput_reservation: The Reservation to use for this topic's throughput capacity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#throughput_reservation GooglePubsubLiteTopic#throughput_reservation}
        '''
        value = GooglePubsubLiteTopicReservationConfig(
            throughput_reservation=throughput_reservation
        )

        return typing.cast(None, jsii.invoke(self, "putReservationConfig", [value]))

    @jsii.member(jsii_name="putRetentionConfig")
    def put_retention_config(
        self,
        *,
        per_partition_bytes: builtins.str,
        period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param per_partition_bytes: The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#per_partition_bytes GooglePubsubLiteTopic#per_partition_bytes}
        :param period: How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below perPartitionBytes. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#period GooglePubsubLiteTopic#period}
        '''
        value = GooglePubsubLiteTopicRetentionConfig(
            per_partition_bytes=per_partition_bytes, period=period
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#create GooglePubsubLiteTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#delete GooglePubsubLiteTopic#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#update GooglePubsubLiteTopic#update}.
        '''
        value = GooglePubsubLiteTopicTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPartitionConfig")
    def reset_partition_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetReservationConfig")
    def reset_reservation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationConfig", []))

    @jsii.member(jsii_name="resetRetentionConfig")
    def reset_retention_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionConfig", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="partitionConfig")
    def partition_config(self) -> "GooglePubsubLiteTopicPartitionConfigOutputReference":
        return typing.cast("GooglePubsubLiteTopicPartitionConfigOutputReference", jsii.get(self, "partitionConfig"))

    @builtins.property
    @jsii.member(jsii_name="reservationConfig")
    def reservation_config(
        self,
    ) -> "GooglePubsubLiteTopicReservationConfigOutputReference":
        return typing.cast("GooglePubsubLiteTopicReservationConfigOutputReference", jsii.get(self, "reservationConfig"))

    @builtins.property
    @jsii.member(jsii_name="retentionConfig")
    def retention_config(self) -> "GooglePubsubLiteTopicRetentionConfigOutputReference":
        return typing.cast("GooglePubsubLiteTopicRetentionConfigOutputReference", jsii.get(self, "retentionConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePubsubLiteTopicTimeoutsOutputReference":
        return typing.cast("GooglePubsubLiteTopicTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionConfigInput")
    def partition_config_input(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicPartitionConfig"]:
        return typing.cast(typing.Optional["GooglePubsubLiteTopicPartitionConfig"], jsii.get(self, "partitionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationConfigInput")
    def reservation_config_input(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicReservationConfig"]:
        return typing.cast(typing.Optional["GooglePubsubLiteTopicReservationConfig"], jsii.get(self, "reservationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionConfigInput")
    def retention_config_input(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicRetentionConfig"]:
        return typing.cast(typing.Optional["GooglePubsubLiteTopicRetentionConfig"], jsii.get(self, "retentionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePubsubLiteTopicTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePubsubLiteTopicTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopic, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopic, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopic, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopic, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopic, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicConfig",
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
        "partition_config": "partitionConfig",
        "project": "project",
        "region": "region",
        "reservation_config": "reservationConfig",
        "retention_config": "retentionConfig",
        "timeouts": "timeouts",
        "zone": "zone",
    },
)
class GooglePubsubLiteTopicConfig(cdktf.TerraformMetaArguments):
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
        partition_config: typing.Optional[typing.Union["GooglePubsubLiteTopicPartitionConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        reservation_config: typing.Optional[typing.Union["GooglePubsubLiteTopicReservationConfig", typing.Dict[str, typing.Any]]] = None,
        retention_config: typing.Optional[typing.Union["GooglePubsubLiteTopicRetentionConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubLiteTopicTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#name GooglePubsubLiteTopic#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#id GooglePubsubLiteTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_config: partition_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#partition_config GooglePubsubLiteTopic#partition_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#project GooglePubsubLiteTopic#project}.
        :param region: The region of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#region GooglePubsubLiteTopic#region}
        :param reservation_config: reservation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#reservation_config GooglePubsubLiteTopic#reservation_config}
        :param retention_config: retention_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#retention_config GooglePubsubLiteTopic#retention_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#timeouts GooglePubsubLiteTopic#timeouts}
        :param zone: The zone of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#zone GooglePubsubLiteTopic#zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(partition_config, dict):
            partition_config = GooglePubsubLiteTopicPartitionConfig(**partition_config)
        if isinstance(reservation_config, dict):
            reservation_config = GooglePubsubLiteTopicReservationConfig(**reservation_config)
        if isinstance(retention_config, dict):
            retention_config = GooglePubsubLiteTopicRetentionConfig(**retention_config)
        if isinstance(timeouts, dict):
            timeouts = GooglePubsubLiteTopicTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument partition_config", value=partition_config, expected_type=type_hints["partition_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument reservation_config", value=reservation_config, expected_type=type_hints["reservation_config"])
            check_type(argname="argument retention_config", value=retention_config, expected_type=type_hints["retention_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
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
        if partition_config is not None:
            self._values["partition_config"] = partition_config
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if reservation_config is not None:
            self._values["reservation_config"] = reservation_config
        if retention_config is not None:
            self._values["retention_config"] = retention_config
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zone is not None:
            self._values["zone"] = zone

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
        '''Name of the topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#name GooglePubsubLiteTopic#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#id GooglePubsubLiteTopic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_config(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicPartitionConfig"]:
        '''partition_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#partition_config GooglePubsubLiteTopic#partition_config}
        '''
        result = self._values.get("partition_config")
        return typing.cast(typing.Optional["GooglePubsubLiteTopicPartitionConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#project GooglePubsubLiteTopic#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region of the pubsub lite topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#region GooglePubsubLiteTopic#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reservation_config(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicReservationConfig"]:
        '''reservation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#reservation_config GooglePubsubLiteTopic#reservation_config}
        '''
        result = self._values.get("reservation_config")
        return typing.cast(typing.Optional["GooglePubsubLiteTopicReservationConfig"], result)

    @builtins.property
    def retention_config(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicRetentionConfig"]:
        '''retention_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#retention_config GooglePubsubLiteTopic#retention_config}
        '''
        result = self._values.get("retention_config")
        return typing.cast(typing.Optional["GooglePubsubLiteTopicRetentionConfig"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePubsubLiteTopicTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#timeouts GooglePubsubLiteTopic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePubsubLiteTopicTimeouts"], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The zone of the pubsub lite topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#zone GooglePubsubLiteTopic#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicPartitionConfig",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "capacity": "capacity"},
)
class GooglePubsubLiteTopicPartitionConfig:
    def __init__(
        self,
        *,
        count: jsii.Number,
        capacity: typing.Optional[typing.Union["GooglePubsubLiteTopicPartitionConfigCapacity", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param count: The number of partitions in the topic. Must be at least 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#count GooglePubsubLiteTopic#count}
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#capacity GooglePubsubLiteTopic#capacity}
        '''
        if isinstance(capacity, dict):
            capacity = GooglePubsubLiteTopicPartitionConfigCapacity(**capacity)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicPartitionConfig.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
        }
        if capacity is not None:
            self._values["capacity"] = capacity

    @builtins.property
    def count(self) -> jsii.Number:
        '''The number of partitions in the topic. Must be at least 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#count GooglePubsubLiteTopic#count}
        '''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def capacity(
        self,
    ) -> typing.Optional["GooglePubsubLiteTopicPartitionConfigCapacity"]:
        '''capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#capacity GooglePubsubLiteTopic#capacity}
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional["GooglePubsubLiteTopicPartitionConfigCapacity"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicPartitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicPartitionConfigCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "publish_mib_per_sec": "publishMibPerSec",
        "subscribe_mib_per_sec": "subscribeMibPerSec",
    },
)
class GooglePubsubLiteTopicPartitionConfigCapacity:
    def __init__(
        self,
        *,
        publish_mib_per_sec: jsii.Number,
        subscribe_mib_per_sec: jsii.Number,
    ) -> None:
        '''
        :param publish_mib_per_sec: Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#publish_mib_per_sec GooglePubsubLiteTopic#publish_mib_per_sec}
        :param subscribe_mib_per_sec: Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#subscribe_mib_per_sec GooglePubsubLiteTopic#subscribe_mib_per_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicPartitionConfigCapacity.__init__)
            check_type(argname="argument publish_mib_per_sec", value=publish_mib_per_sec, expected_type=type_hints["publish_mib_per_sec"])
            check_type(argname="argument subscribe_mib_per_sec", value=subscribe_mib_per_sec, expected_type=type_hints["subscribe_mib_per_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "publish_mib_per_sec": publish_mib_per_sec,
            "subscribe_mib_per_sec": subscribe_mib_per_sec,
        }

    @builtins.property
    def publish_mib_per_sec(self) -> jsii.Number:
        '''Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#publish_mib_per_sec GooglePubsubLiteTopic#publish_mib_per_sec}
        '''
        result = self._values.get("publish_mib_per_sec")
        assert result is not None, "Required property 'publish_mib_per_sec' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def subscribe_mib_per_sec(self) -> jsii.Number:
        '''Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#subscribe_mib_per_sec GooglePubsubLiteTopic#subscribe_mib_per_sec}
        '''
        result = self._values.get("subscribe_mib_per_sec")
        assert result is not None, "Required property 'subscribe_mib_per_sec' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicPartitionConfigCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteTopicPartitionConfigCapacityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicPartitionConfigCapacityOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicPartitionConfigCapacityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="publishMibPerSecInput")
    def publish_mib_per_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "publishMibPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="subscribeMibPerSecInput")
    def subscribe_mib_per_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subscribeMibPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="publishMibPerSec")
    def publish_mib_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "publishMibPerSec"))

    @publish_mib_per_sec.setter
    def publish_mib_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicPartitionConfigCapacityOutputReference, "publish_mib_per_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishMibPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="subscribeMibPerSec")
    def subscribe_mib_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subscribeMibPerSec"))

    @subscribe_mib_per_sec.setter
    def subscribe_mib_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicPartitionConfigCapacityOutputReference, "subscribe_mib_per_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscribeMibPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePubsubLiteTopicPartitionConfigCapacity]:
        return typing.cast(typing.Optional[GooglePubsubLiteTopicPartitionConfigCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubLiteTopicPartitionConfigCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicPartitionConfigCapacityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePubsubLiteTopicPartitionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicPartitionConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicPartitionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(
        self,
        *,
        publish_mib_per_sec: jsii.Number,
        subscribe_mib_per_sec: jsii.Number,
    ) -> None:
        '''
        :param publish_mib_per_sec: Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#publish_mib_per_sec GooglePubsubLiteTopic#publish_mib_per_sec}
        :param subscribe_mib_per_sec: Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#subscribe_mib_per_sec GooglePubsubLiteTopic#subscribe_mib_per_sec}
        '''
        value = GooglePubsubLiteTopicPartitionConfigCapacity(
            publish_mib_per_sec=publish_mib_per_sec,
            subscribe_mib_per_sec=subscribe_mib_per_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value]))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> GooglePubsubLiteTopicPartitionConfigCapacityOutputReference:
        return typing.cast(GooglePubsubLiteTopicPartitionConfigCapacityOutputReference, jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[GooglePubsubLiteTopicPartitionConfigCapacity]:
        return typing.cast(typing.Optional[GooglePubsubLiteTopicPartitionConfigCapacity], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicPartitionConfigOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubLiteTopicPartitionConfig]:
        return typing.cast(typing.Optional[GooglePubsubLiteTopicPartitionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubLiteTopicPartitionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicPartitionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicReservationConfig",
    jsii_struct_bases=[],
    name_mapping={"throughput_reservation": "throughputReservation"},
)
class GooglePubsubLiteTopicReservationConfig:
    def __init__(
        self,
        *,
        throughput_reservation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param throughput_reservation: The Reservation to use for this topic's throughput capacity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#throughput_reservation GooglePubsubLiteTopic#throughput_reservation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicReservationConfig.__init__)
            check_type(argname="argument throughput_reservation", value=throughput_reservation, expected_type=type_hints["throughput_reservation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if throughput_reservation is not None:
            self._values["throughput_reservation"] = throughput_reservation

    @builtins.property
    def throughput_reservation(self) -> typing.Optional[builtins.str]:
        '''The Reservation to use for this topic's throughput capacity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#throughput_reservation GooglePubsubLiteTopic#throughput_reservation}
        '''
        result = self._values.get("throughput_reservation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicReservationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteTopicReservationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicReservationConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicReservationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetThroughputReservation")
    def reset_throughput_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughputReservation", []))

    @builtins.property
    @jsii.member(jsii_name="throughputReservationInput")
    def throughput_reservation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "throughputReservationInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputReservation")
    def throughput_reservation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "throughputReservation"))

    @throughput_reservation.setter
    def throughput_reservation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicReservationConfigOutputReference, "throughput_reservation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughputReservation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubLiteTopicReservationConfig]:
        return typing.cast(typing.Optional[GooglePubsubLiteTopicReservationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubLiteTopicReservationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicReservationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicRetentionConfig",
    jsii_struct_bases=[],
    name_mapping={"per_partition_bytes": "perPartitionBytes", "period": "period"},
)
class GooglePubsubLiteTopicRetentionConfig:
    def __init__(
        self,
        *,
        per_partition_bytes: builtins.str,
        period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param per_partition_bytes: The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#per_partition_bytes GooglePubsubLiteTopic#per_partition_bytes}
        :param period: How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below perPartitionBytes. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#period GooglePubsubLiteTopic#period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicRetentionConfig.__init__)
            check_type(argname="argument per_partition_bytes", value=per_partition_bytes, expected_type=type_hints["per_partition_bytes"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
        self._values: typing.Dict[str, typing.Any] = {
            "per_partition_bytes": per_partition_bytes,
        }
        if period is not None:
            self._values["period"] = period

    @builtins.property
    def per_partition_bytes(self) -> builtins.str:
        '''The provisioned storage, in bytes, per partition.

        If the number of bytes stored
        in any of the topic's partitions grows beyond this value, older messages will be
        dropped to make room for newer ones, regardless of the value of period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#per_partition_bytes GooglePubsubLiteTopic#per_partition_bytes}
        '''
        result = self._values.get("per_partition_bytes")
        assert result is not None, "Required property 'per_partition_bytes' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''How long a published message is retained.

        If unset, messages will be retained as
        long as the bytes retained for each partition is below perPartitionBytes. A
        duration in seconds with up to nine fractional digits, terminated by 's'.
        Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#period GooglePubsubLiteTopic#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicRetentionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteTopicRetentionConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicRetentionConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicRetentionConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="perPartitionBytesInput")
    def per_partition_bytes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perPartitionBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicRetentionConfigOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="perPartitionBytes")
    def per_partition_bytes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perPartitionBytes"))

    @per_partition_bytes.setter
    def per_partition_bytes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicRetentionConfigOutputReference, "per_partition_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perPartitionBytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubLiteTopicRetentionConfig]:
        return typing.cast(typing.Optional[GooglePubsubLiteTopicRetentionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubLiteTopicRetentionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicRetentionConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePubsubLiteTopicTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#create GooglePubsubLiteTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#delete GooglePubsubLiteTopic#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#update GooglePubsubLiteTopic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#create GooglePubsubLiteTopic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#delete GooglePubsubLiteTopic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_topic#update GooglePubsubLiteTopic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteTopicTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteTopicTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteTopic.GooglePubsubLiteTopicTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteTopicTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePubsubLiteTopicTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePubsubLiteTopicTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePubsubLiteTopicTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteTopicTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePubsubLiteTopic",
    "GooglePubsubLiteTopicConfig",
    "GooglePubsubLiteTopicPartitionConfig",
    "GooglePubsubLiteTopicPartitionConfigCapacity",
    "GooglePubsubLiteTopicPartitionConfigCapacityOutputReference",
    "GooglePubsubLiteTopicPartitionConfigOutputReference",
    "GooglePubsubLiteTopicReservationConfig",
    "GooglePubsubLiteTopicReservationConfigOutputReference",
    "GooglePubsubLiteTopicRetentionConfig",
    "GooglePubsubLiteTopicRetentionConfigOutputReference",
    "GooglePubsubLiteTopicTimeouts",
    "GooglePubsubLiteTopicTimeoutsOutputReference",
]

publication.publish()
