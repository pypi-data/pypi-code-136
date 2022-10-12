'''
# `google_pubsub_lite_subscription`

Refer to the Terraform Registory for docs: [`google_pubsub_lite_subscription`](https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription).
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


class GooglePubsubLiteSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription google_pubsub_lite_subscription}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        topic: builtins.str,
        delivery_config: typing.Optional[typing.Union["GooglePubsubLiteSubscriptionDeliveryConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubLiteSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription google_pubsub_lite_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#name GooglePubsubLiteSubscription#name}
        :param topic: A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#topic GooglePubsubLiteSubscription#topic}
        :param delivery_config: delivery_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_config GooglePubsubLiteSubscription#delivery_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#id GooglePubsubLiteSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#project GooglePubsubLiteSubscription#project}.
        :param region: The region of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#region GooglePubsubLiteSubscription#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#timeouts GooglePubsubLiteSubscription#timeouts}
        :param zone: The zone of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#zone GooglePubsubLiteSubscription#zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GooglePubsubLiteSubscriptionConfig(
            name=name,
            topic=topic,
            delivery_config=delivery_config,
            id=id,
            project=project,
            region=region,
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

    @jsii.member(jsii_name="putDeliveryConfig")
    def put_delivery_config(self, *, delivery_requirement: builtins.str) -> None:
        '''
        :param delivery_requirement: When this subscription should send messages to subscribers relative to messages persistence in storage. Possible values: ["DELIVER_IMMEDIATELY", "DELIVER_AFTER_STORED", "DELIVERY_REQUIREMENT_UNSPECIFIED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_requirement GooglePubsubLiteSubscription#delivery_requirement}
        '''
        value = GooglePubsubLiteSubscriptionDeliveryConfig(
            delivery_requirement=delivery_requirement
        )

        return typing.cast(None, jsii.invoke(self, "putDeliveryConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#create GooglePubsubLiteSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delete GooglePubsubLiteSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#update GooglePubsubLiteSubscription#update}.
        '''
        value = GooglePubsubLiteSubscriptionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDeliveryConfig")
    def reset_delivery_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

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
    @jsii.member(jsii_name="deliveryConfig")
    def delivery_config(
        self,
    ) -> "GooglePubsubLiteSubscriptionDeliveryConfigOutputReference":
        return typing.cast("GooglePubsubLiteSubscriptionDeliveryConfigOutputReference", jsii.get(self, "deliveryConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePubsubLiteSubscriptionTimeoutsOutputReference":
        return typing.cast("GooglePubsubLiteSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="deliveryConfigInput")
    def delivery_config_input(
        self,
    ) -> typing.Optional["GooglePubsubLiteSubscriptionDeliveryConfig"]:
        return typing.cast(typing.Optional["GooglePubsubLiteSubscriptionDeliveryConfig"], jsii.get(self, "deliveryConfigInput"))

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
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePubsubLiteSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePubsubLiteSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

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
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscription, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscriptionConfig",
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
        "topic": "topic",
        "delivery_config": "deliveryConfig",
        "id": "id",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
        "zone": "zone",
    },
)
class GooglePubsubLiteSubscriptionConfig(cdktf.TerraformMetaArguments):
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
        topic: builtins.str,
        delivery_config: typing.Optional[typing.Union["GooglePubsubLiteSubscriptionDeliveryConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubLiteSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param name: Name of the subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#name GooglePubsubLiteSubscription#name}
        :param topic: A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#topic GooglePubsubLiteSubscription#topic}
        :param delivery_config: delivery_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_config GooglePubsubLiteSubscription#delivery_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#id GooglePubsubLiteSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#project GooglePubsubLiteSubscription#project}.
        :param region: The region of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#region GooglePubsubLiteSubscription#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#timeouts GooglePubsubLiteSubscription#timeouts}
        :param zone: The zone of the pubsub lite topic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#zone GooglePubsubLiteSubscription#zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(delivery_config, dict):
            delivery_config = GooglePubsubLiteSubscriptionDeliveryConfig(**delivery_config)
        if isinstance(timeouts, dict):
            timeouts = GooglePubsubLiteSubscriptionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument delivery_config", value=delivery_config, expected_type=type_hints["delivery_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "topic": topic,
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
        if delivery_config is not None:
            self._values["delivery_config"] = delivery_config
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
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
        '''Name of the subscription.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#name GooglePubsubLiteSubscription#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''A reference to a Topic resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#topic GooglePubsubLiteSubscription#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_config(
        self,
    ) -> typing.Optional["GooglePubsubLiteSubscriptionDeliveryConfig"]:
        '''delivery_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_config GooglePubsubLiteSubscription#delivery_config}
        '''
        result = self._values.get("delivery_config")
        return typing.cast(typing.Optional["GooglePubsubLiteSubscriptionDeliveryConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#id GooglePubsubLiteSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#project GooglePubsubLiteSubscription#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region of the pubsub lite topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#region GooglePubsubLiteSubscription#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePubsubLiteSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#timeouts GooglePubsubLiteSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePubsubLiteSubscriptionTimeouts"], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The zone of the pubsub lite topic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#zone GooglePubsubLiteSubscription#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscriptionDeliveryConfig",
    jsii_struct_bases=[],
    name_mapping={"delivery_requirement": "deliveryRequirement"},
)
class GooglePubsubLiteSubscriptionDeliveryConfig:
    def __init__(self, *, delivery_requirement: builtins.str) -> None:
        '''
        :param delivery_requirement: When this subscription should send messages to subscribers relative to messages persistence in storage. Possible values: ["DELIVER_IMMEDIATELY", "DELIVER_AFTER_STORED", "DELIVERY_REQUIREMENT_UNSPECIFIED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_requirement GooglePubsubLiteSubscription#delivery_requirement}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscriptionDeliveryConfig.__init__)
            check_type(argname="argument delivery_requirement", value=delivery_requirement, expected_type=type_hints["delivery_requirement"])
        self._values: typing.Dict[str, typing.Any] = {
            "delivery_requirement": delivery_requirement,
        }

    @builtins.property
    def delivery_requirement(self) -> builtins.str:
        '''When this subscription should send messages to subscribers relative to messages persistence in storage. Possible values: ["DELIVER_IMMEDIATELY", "DELIVER_AFTER_STORED", "DELIVERY_REQUIREMENT_UNSPECIFIED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delivery_requirement GooglePubsubLiteSubscription#delivery_requirement}
        '''
        result = self._values.get("delivery_requirement")
        assert result is not None, "Required property 'delivery_requirement' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteSubscriptionDeliveryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteSubscriptionDeliveryConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscriptionDeliveryConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscriptionDeliveryConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="deliveryRequirementInput")
    def delivery_requirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryRequirementInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryRequirement")
    def delivery_requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryRequirement"))

    @delivery_requirement.setter
    def delivery_requirement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionDeliveryConfigOutputReference, "delivery_requirement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryRequirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePubsubLiteSubscriptionDeliveryConfig]:
        return typing.cast(typing.Optional[GooglePubsubLiteSubscriptionDeliveryConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubLiteSubscriptionDeliveryConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionDeliveryConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePubsubLiteSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#create GooglePubsubLiteSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delete GooglePubsubLiteSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#update GooglePubsubLiteSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscriptionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#create GooglePubsubLiteSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#delete GooglePubsubLiteSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_lite_subscription#update GooglePubsubLiteSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubLiteSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubLiteSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubLiteSubscription.GooglePubsubLiteSubscriptionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubLiteSubscriptionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePubsubLiteSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePubsubLiteSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePubsubLiteSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubLiteSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePubsubLiteSubscription",
    "GooglePubsubLiteSubscriptionConfig",
    "GooglePubsubLiteSubscriptionDeliveryConfig",
    "GooglePubsubLiteSubscriptionDeliveryConfigOutputReference",
    "GooglePubsubLiteSubscriptionTimeouts",
    "GooglePubsubLiteSubscriptionTimeoutsOutputReference",
]

publication.publish()
