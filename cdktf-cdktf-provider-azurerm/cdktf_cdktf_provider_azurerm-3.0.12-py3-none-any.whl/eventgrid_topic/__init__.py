'''
# `azurerm_eventgrid_topic`

Refer to the Terraform Registory for docs: [`azurerm_eventgrid_topic`](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic).
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


class EventgridTopic(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic azurerm_eventgrid_topic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventgridTopicIdentity", typing.Dict[str, typing.Any]]] = None,
        inbound_ip_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridTopicInboundIpRule", typing.Dict[str, typing.Any]]]]] = None,
        input_mapping_default_values: typing.Optional[typing.Union["EventgridTopicInputMappingDefaultValues", typing.Dict[str, typing.Any]]] = None,
        input_mapping_fields: typing.Optional[typing.Union["EventgridTopicInputMappingFields", typing.Dict[str, typing.Any]]] = None,
        input_schema: typing.Optional[builtins.str] = None,
        local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventgridTopicTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic azurerm_eventgrid_topic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#location EventgridTopic#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#name EventgridTopic#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#resource_group_name EventgridTopic#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity EventgridTopic#identity}
        :param inbound_ip_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#inbound_ip_rule EventgridTopic#inbound_ip_rule}.
        :param input_mapping_default_values: input_mapping_default_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_default_values EventgridTopic#input_mapping_default_values}
        :param input_mapping_fields: input_mapping_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_fields EventgridTopic#input_mapping_fields}
        :param input_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_schema EventgridTopic#input_schema}.
        :param local_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#local_auth_enabled EventgridTopic#local_auth_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#public_network_access_enabled EventgridTopic#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#tags EventgridTopic#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#timeouts EventgridTopic#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopic.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventgridTopicConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            id=id,
            identity=identity,
            inbound_ip_rule=inbound_ip_rule,
            input_mapping_default_values=input_mapping_default_values,
            input_mapping_fields=input_mapping_fields,
            input_schema=input_schema,
            local_auth_enabled=local_auth_enabled,
            public_network_access_enabled=public_network_access_enabled,
            tags=tags,
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

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#type EventgridTopic#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity_ids EventgridTopic#identity_ids}.
        '''
        value = EventgridTopicIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putInboundIpRule")
    def put_inbound_ip_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridTopicInboundIpRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopic.put_inbound_ip_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInboundIpRule", [value]))

    @jsii.member(jsii_name="putInputMappingDefaultValues")
    def put_input_mapping_default_values(
        self,
        *,
        data_version: typing.Optional[builtins.str] = None,
        event_type: typing.Optional[builtins.str] = None,
        subject: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.
        '''
        value = EventgridTopicInputMappingDefaultValues(
            data_version=data_version, event_type=event_type, subject=subject
        )

        return typing.cast(None, jsii.invoke(self, "putInputMappingDefaultValues", [value]))

    @jsii.member(jsii_name="putInputMappingFields")
    def put_input_mapping_fields(
        self,
        *,
        data_version: typing.Optional[builtins.str] = None,
        event_time: typing.Optional[builtins.str] = None,
        event_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        subject: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.
        :param event_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_time EventgridTopic#event_time}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#topic EventgridTopic#topic}.
        '''
        value = EventgridTopicInputMappingFields(
            data_version=data_version,
            event_time=event_time,
            event_type=event_type,
            id=id,
            subject=subject,
            topic=topic,
        )

        return typing.cast(None, jsii.invoke(self, "putInputMappingFields", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#create EventgridTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#delete EventgridTopic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#read EventgridTopic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#update EventgridTopic#update}.
        '''
        value = EventgridTopicTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetInboundIpRule")
    def reset_inbound_ip_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundIpRule", []))

    @jsii.member(jsii_name="resetInputMappingDefaultValues")
    def reset_input_mapping_default_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputMappingDefaultValues", []))

    @jsii.member(jsii_name="resetInputMappingFields")
    def reset_input_mapping_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputMappingFields", []))

    @jsii.member(jsii_name="resetInputSchema")
    def reset_input_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputSchema", []))

    @jsii.member(jsii_name="resetLocalAuthEnabled")
    def reset_local_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAuthEnabled", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "EventgridTopicIdentityOutputReference":
        return typing.cast("EventgridTopicIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="inboundIpRule")
    def inbound_ip_rule(self) -> "EventgridTopicInboundIpRuleList":
        return typing.cast("EventgridTopicInboundIpRuleList", jsii.get(self, "inboundIpRule"))

    @builtins.property
    @jsii.member(jsii_name="inputMappingDefaultValues")
    def input_mapping_default_values(
        self,
    ) -> "EventgridTopicInputMappingDefaultValuesOutputReference":
        return typing.cast("EventgridTopicInputMappingDefaultValuesOutputReference", jsii.get(self, "inputMappingDefaultValues"))

    @builtins.property
    @jsii.member(jsii_name="inputMappingFields")
    def input_mapping_fields(self) -> "EventgridTopicInputMappingFieldsOutputReference":
        return typing.cast("EventgridTopicInputMappingFieldsOutputReference", jsii.get(self, "inputMappingFields"))

    @builtins.property
    @jsii.member(jsii_name="primaryAccessKey")
    def primary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryAccessKey")
    def secondary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EventgridTopicTimeoutsOutputReference":
        return typing.cast("EventgridTopicTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["EventgridTopicIdentity"]:
        return typing.cast(typing.Optional["EventgridTopicIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundIpRuleInput")
    def inbound_ip_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridTopicInboundIpRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridTopicInboundIpRule"]]], jsii.get(self, "inboundIpRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="inputMappingDefaultValuesInput")
    def input_mapping_default_values_input(
        self,
    ) -> typing.Optional["EventgridTopicInputMappingDefaultValues"]:
        return typing.cast(typing.Optional["EventgridTopicInputMappingDefaultValues"], jsii.get(self, "inputMappingDefaultValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="inputMappingFieldsInput")
    def input_mapping_fields_input(
        self,
    ) -> typing.Optional["EventgridTopicInputMappingFields"]:
        return typing.cast(typing.Optional["EventgridTopicInputMappingFields"], jsii.get(self, "inputMappingFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="inputSchemaInput")
    def input_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="localAuthEnabledInput")
    def local_auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAuthEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EventgridTopicTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EventgridTopicTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inputSchema")
    def input_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputSchema"))

    @input_schema.setter
    def input_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "input_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputSchema", value)

    @builtins.property
    @jsii.member(jsii_name="localAuthEnabled")
    def local_auth_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAuthEnabled"))

    @local_auth_enabled.setter
    def local_auth_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "local_auth_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAuthEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopic, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "identity": "identity",
        "inbound_ip_rule": "inboundIpRule",
        "input_mapping_default_values": "inputMappingDefaultValues",
        "input_mapping_fields": "inputMappingFields",
        "input_schema": "inputSchema",
        "local_auth_enabled": "localAuthEnabled",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class EventgridTopicConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventgridTopicIdentity", typing.Dict[str, typing.Any]]] = None,
        inbound_ip_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridTopicInboundIpRule", typing.Dict[str, typing.Any]]]]] = None,
        input_mapping_default_values: typing.Optional[typing.Union["EventgridTopicInputMappingDefaultValues", typing.Dict[str, typing.Any]]] = None,
        input_mapping_fields: typing.Optional[typing.Union["EventgridTopicInputMappingFields", typing.Dict[str, typing.Any]]] = None,
        input_schema: typing.Optional[builtins.str] = None,
        local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventgridTopicTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#location EventgridTopic#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#name EventgridTopic#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#resource_group_name EventgridTopic#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity EventgridTopic#identity}
        :param inbound_ip_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#inbound_ip_rule EventgridTopic#inbound_ip_rule}.
        :param input_mapping_default_values: input_mapping_default_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_default_values EventgridTopic#input_mapping_default_values}
        :param input_mapping_fields: input_mapping_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_fields EventgridTopic#input_mapping_fields}
        :param input_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_schema EventgridTopic#input_schema}.
        :param local_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#local_auth_enabled EventgridTopic#local_auth_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#public_network_access_enabled EventgridTopic#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#tags EventgridTopic#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#timeouts EventgridTopic#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = EventgridTopicIdentity(**identity)
        if isinstance(input_mapping_default_values, dict):
            input_mapping_default_values = EventgridTopicInputMappingDefaultValues(**input_mapping_default_values)
        if isinstance(input_mapping_fields, dict):
            input_mapping_fields = EventgridTopicInputMappingFields(**input_mapping_fields)
        if isinstance(timeouts, dict):
            timeouts = EventgridTopicTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument inbound_ip_rule", value=inbound_ip_rule, expected_type=type_hints["inbound_ip_rule"])
            check_type(argname="argument input_mapping_default_values", value=input_mapping_default_values, expected_type=type_hints["input_mapping_default_values"])
            check_type(argname="argument input_mapping_fields", value=input_mapping_fields, expected_type=type_hints["input_mapping_fields"])
            check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
            check_type(argname="argument local_auth_enabled", value=local_auth_enabled, expected_type=type_hints["local_auth_enabled"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if identity is not None:
            self._values["identity"] = identity
        if inbound_ip_rule is not None:
            self._values["inbound_ip_rule"] = inbound_ip_rule
        if input_mapping_default_values is not None:
            self._values["input_mapping_default_values"] = input_mapping_default_values
        if input_mapping_fields is not None:
            self._values["input_mapping_fields"] = input_mapping_fields
        if input_schema is not None:
            self._values["input_schema"] = input_schema
        if local_auth_enabled is not None:
            self._values["local_auth_enabled"] = local_auth_enabled
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if tags is not None:
            self._values["tags"] = tags
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#location EventgridTopic#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#name EventgridTopic#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#resource_group_name EventgridTopic#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["EventgridTopicIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity EventgridTopic#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["EventgridTopicIdentity"], result)

    @builtins.property
    def inbound_ip_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridTopicInboundIpRule"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#inbound_ip_rule EventgridTopic#inbound_ip_rule}.'''
        result = self._values.get("inbound_ip_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridTopicInboundIpRule"]]], result)

    @builtins.property
    def input_mapping_default_values(
        self,
    ) -> typing.Optional["EventgridTopicInputMappingDefaultValues"]:
        '''input_mapping_default_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_default_values EventgridTopic#input_mapping_default_values}
        '''
        result = self._values.get("input_mapping_default_values")
        return typing.cast(typing.Optional["EventgridTopicInputMappingDefaultValues"], result)

    @builtins.property
    def input_mapping_fields(
        self,
    ) -> typing.Optional["EventgridTopicInputMappingFields"]:
        '''input_mapping_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_mapping_fields EventgridTopic#input_mapping_fields}
        '''
        result = self._values.get("input_mapping_fields")
        return typing.cast(typing.Optional["EventgridTopicInputMappingFields"], result)

    @builtins.property
    def input_schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#input_schema EventgridTopic#input_schema}.'''
        result = self._values.get("input_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#local_auth_enabled EventgridTopic#local_auth_enabled}.'''
        result = self._values.get("local_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#public_network_access_enabled EventgridTopic#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#tags EventgridTopic#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EventgridTopicTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#timeouts EventgridTopic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventgridTopicTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class EventgridTopicIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#type EventgridTopic#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity_ids EventgridTopic#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#type EventgridTopic#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#identity_ids EventgridTopic#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridTopicIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventgridTopicIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventgridTopicIdentity]:
        return typing.cast(typing.Optional[EventgridTopicIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EventgridTopicIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInboundIpRule",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "ip_mask": "ipMask"},
)
class EventgridTopicInboundIpRule:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        ip_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#action EventgridTopic#action}.
        :param ip_mask: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#ip_mask EventgridTopic#ip_mask}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicInboundIpRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument ip_mask", value=ip_mask, expected_type=type_hints["ip_mask"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if ip_mask is not None:
            self._values["ip_mask"] = ip_mask

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#action EventgridTopic#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_mask(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#ip_mask EventgridTopic#ip_mask}.'''
        result = self._values.get("ip_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicInboundIpRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridTopicInboundIpRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInboundIpRuleList",
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
            type_hints = typing.get_type_hints(EventgridTopicInboundIpRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EventgridTopicInboundIpRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicInboundIpRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridTopicInboundIpRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridTopicInboundIpRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridTopicInboundIpRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridTopicInboundIpRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridTopicInboundIpRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInboundIpRuleOutputReference",
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
            type_hints = typing.get_type_hints(EventgridTopicInboundIpRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetIpMask")
    def reset_ip_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpMask", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipMaskInput")
    def ip_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipMask")
    def ip_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipMask"))

    @ip_mask.setter
    def ip_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleOutputReference, "ip_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipMask", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridTopicInboundIpRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridTopicInboundIpRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridTopicInboundIpRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInboundIpRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInputMappingDefaultValues",
    jsii_struct_bases=[],
    name_mapping={
        "data_version": "dataVersion",
        "event_type": "eventType",
        "subject": "subject",
    },
)
class EventgridTopicInputMappingDefaultValues:
    def __init__(
        self,
        *,
        data_version: typing.Optional[builtins.str] = None,
        event_type: typing.Optional[builtins.str] = None,
        subject: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicInputMappingDefaultValues.__init__)
            check_type(argname="argument data_version", value=data_version, expected_type=type_hints["data_version"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
        self._values: typing.Dict[str, typing.Any] = {}
        if data_version is not None:
            self._values["data_version"] = data_version
        if event_type is not None:
            self._values["event_type"] = event_type
        if subject is not None:
            self._values["subject"] = subject

    @builtins.property
    def data_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.'''
        result = self._values.get("data_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.'''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.'''
        result = self._values.get("subject")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicInputMappingDefaultValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridTopicInputMappingDefaultValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInputMappingDefaultValuesOutputReference",
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
            type_hints = typing.get_type_hints(EventgridTopicInputMappingDefaultValuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataVersion")
    def reset_data_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataVersion", []))

    @jsii.member(jsii_name="resetEventType")
    def reset_event_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventType", []))

    @jsii.member(jsii_name="resetSubject")
    def reset_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubject", []))

    @builtins.property
    @jsii.member(jsii_name="dataVersionInput")
    def data_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="dataVersion")
    def data_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataVersion"))

    @data_version.setter
    def data_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingDefaultValuesOutputReference, "data_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataVersion", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingDefaultValuesOutputReference, "event_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingDefaultValuesOutputReference, "subject").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridTopicInputMappingDefaultValues]:
        return typing.cast(typing.Optional[EventgridTopicInputMappingDefaultValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridTopicInputMappingDefaultValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingDefaultValuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInputMappingFields",
    jsii_struct_bases=[],
    name_mapping={
        "data_version": "dataVersion",
        "event_time": "eventTime",
        "event_type": "eventType",
        "id": "id",
        "subject": "subject",
        "topic": "topic",
    },
)
class EventgridTopicInputMappingFields:
    def __init__(
        self,
        *,
        data_version: typing.Optional[builtins.str] = None,
        event_time: typing.Optional[builtins.str] = None,
        event_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        subject: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.
        :param event_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_time EventgridTopic#event_time}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#topic EventgridTopic#topic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicInputMappingFields.__init__)
            check_type(argname="argument data_version", value=data_version, expected_type=type_hints["data_version"])
            check_type(argname="argument event_time", value=event_time, expected_type=type_hints["event_time"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[str, typing.Any] = {}
        if data_version is not None:
            self._values["data_version"] = data_version
        if event_time is not None:
            self._values["event_time"] = event_time
        if event_type is not None:
            self._values["event_type"] = event_type
        if id is not None:
            self._values["id"] = id
        if subject is not None:
            self._values["subject"] = subject
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def data_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#data_version EventgridTopic#data_version}.'''
        result = self._values.get("data_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_time EventgridTopic#event_time}.'''
        result = self._values.get("event_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#event_type EventgridTopic#event_type}.'''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#id EventgridTopic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#subject EventgridTopic#subject}.'''
        result = self._values.get("subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#topic EventgridTopic#topic}.'''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicInputMappingFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridTopicInputMappingFieldsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicInputMappingFieldsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridTopicInputMappingFieldsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataVersion")
    def reset_data_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataVersion", []))

    @jsii.member(jsii_name="resetEventTime")
    def reset_event_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventTime", []))

    @jsii.member(jsii_name="resetEventType")
    def reset_event_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSubject")
    def reset_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubject", []))

    @jsii.member(jsii_name="resetTopic")
    def reset_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopic", []))

    @builtins.property
    @jsii.member(jsii_name="dataVersionInput")
    def data_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTimeInput")
    def event_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="dataVersion")
    def data_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataVersion"))

    @data_version.setter
    def data_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "data_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataVersion", value)

    @builtins.property
    @jsii.member(jsii_name="eventTime")
    def event_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventTime"))

    @event_time.setter
    def event_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "event_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTime", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "event_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "subject").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventgridTopicInputMappingFields]:
        return typing.cast(typing.Optional[EventgridTopicInputMappingFields], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridTopicInputMappingFields],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicInputMappingFieldsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventgridTopicTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#create EventgridTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#delete EventgridTopic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#read EventgridTopic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#update EventgridTopic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridTopicTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#create EventgridTopic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#delete EventgridTopic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#read EventgridTopic#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic#update EventgridTopic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridTopicTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridTopicTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridTopic.EventgridTopicTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridTopicTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridTopicTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridTopicTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridTopicTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridTopicTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridTopicTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EventgridTopic",
    "EventgridTopicConfig",
    "EventgridTopicIdentity",
    "EventgridTopicIdentityOutputReference",
    "EventgridTopicInboundIpRule",
    "EventgridTopicInboundIpRuleList",
    "EventgridTopicInboundIpRuleOutputReference",
    "EventgridTopicInputMappingDefaultValues",
    "EventgridTopicInputMappingDefaultValuesOutputReference",
    "EventgridTopicInputMappingFields",
    "EventgridTopicInputMappingFieldsOutputReference",
    "EventgridTopicTimeouts",
    "EventgridTopicTimeoutsOutputReference",
]

publication.publish()
