'''
# `azurerm_data_factory_trigger_custom_event`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_trigger_custom_event`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event).
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


class DataFactoryTriggerCustomEvent(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEvent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event azurerm_data_factory_trigger_custom_event}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        eventgrid_topic_id: builtins.str,
        events: typing.Sequence[builtins.str],
        name: builtins.str,
        pipeline: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryTriggerCustomEventPipeline", typing.Dict[str, typing.Any]]]],
        activated: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        subject_begins_with: typing.Optional[builtins.str] = None,
        subject_ends_with: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryTriggerCustomEventTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event azurerm_data_factory_trigger_custom_event} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#data_factory_id DataFactoryTriggerCustomEvent#data_factory_id}.
        :param eventgrid_topic_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#eventgrid_topic_id DataFactoryTriggerCustomEvent#eventgrid_topic_id}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#events DataFactoryTriggerCustomEvent#events}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#name DataFactoryTriggerCustomEvent#name}.
        :param pipeline: pipeline block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#pipeline DataFactoryTriggerCustomEvent#pipeline}
        :param activated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#activated DataFactoryTriggerCustomEvent#activated}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#additional_properties DataFactoryTriggerCustomEvent#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#annotations DataFactoryTriggerCustomEvent#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#description DataFactoryTriggerCustomEvent#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#id DataFactoryTriggerCustomEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_begins_with DataFactoryTriggerCustomEvent#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_ends_with DataFactoryTriggerCustomEvent#subject_ends_with}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#timeouts DataFactoryTriggerCustomEvent#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEvent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryTriggerCustomEventConfig(
            data_factory_id=data_factory_id,
            eventgrid_topic_id=eventgrid_topic_id,
            events=events,
            name=name,
            pipeline=pipeline,
            activated=activated,
            additional_properties=additional_properties,
            annotations=annotations,
            description=description,
            id=id,
            subject_begins_with=subject_begins_with,
            subject_ends_with=subject_ends_with,
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

    @jsii.member(jsii_name="putPipeline")
    def put_pipeline(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryTriggerCustomEventPipeline", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEvent.put_pipeline)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPipeline", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#create DataFactoryTriggerCustomEvent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#delete DataFactoryTriggerCustomEvent#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#read DataFactoryTriggerCustomEvent#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#update DataFactoryTriggerCustomEvent#update}.
        '''
        value = DataFactoryTriggerCustomEventTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActivated")
    def reset_activated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivated", []))

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSubjectBeginsWith")
    def reset_subject_begins_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectBeginsWith", []))

    @jsii.member(jsii_name="resetSubjectEndsWith")
    def reset_subject_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectEndsWith", []))

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
    @jsii.member(jsii_name="pipeline")
    def pipeline(self) -> "DataFactoryTriggerCustomEventPipelineList":
        return typing.cast("DataFactoryTriggerCustomEventPipelineList", jsii.get(self, "pipeline"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataFactoryTriggerCustomEventTimeoutsOutputReference":
        return typing.cast("DataFactoryTriggerCustomEventTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activatedInput")
    def activated_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activatedInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryIdInput")
    def data_factory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFactoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventgridTopicIdInput")
    def eventgrid_topic_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventgridTopicIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineInput")
    def pipeline_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryTriggerCustomEventPipeline"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryTriggerCustomEventPipeline"]]], jsii.get(self, "pipelineInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectBeginsWithInput")
    def subject_begins_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectEndsWithInput")
    def subject_ends_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryTriggerCustomEventTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryTriggerCustomEventTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="activated")
    def activated(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "activated"))

    @activated.setter
    def activated(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "activated").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activated", value)

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventgridTopicId")
    def eventgrid_topic_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventgridTopicId"))

    @eventgrid_topic_id.setter
    def eventgrid_topic_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "eventgrid_topic_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventgridTopicId", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subjectBeginsWith")
    def subject_begins_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectBeginsWith"))

    @subject_begins_with.setter
    def subject_begins_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "subject_begins_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectBeginsWith", value)

    @builtins.property
    @jsii.member(jsii_name="subjectEndsWith")
    def subject_ends_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectEndsWith"))

    @subject_ends_with.setter
    def subject_ends_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEvent, "subject_ends_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectEndsWith", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_factory_id": "dataFactoryId",
        "eventgrid_topic_id": "eventgridTopicId",
        "events": "events",
        "name": "name",
        "pipeline": "pipeline",
        "activated": "activated",
        "additional_properties": "additionalProperties",
        "annotations": "annotations",
        "description": "description",
        "id": "id",
        "subject_begins_with": "subjectBeginsWith",
        "subject_ends_with": "subjectEndsWith",
        "timeouts": "timeouts",
    },
)
class DataFactoryTriggerCustomEventConfig(cdktf.TerraformMetaArguments):
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
        data_factory_id: builtins.str,
        eventgrid_topic_id: builtins.str,
        events: typing.Sequence[builtins.str],
        name: builtins.str,
        pipeline: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryTriggerCustomEventPipeline", typing.Dict[str, typing.Any]]]],
        activated: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        subject_begins_with: typing.Optional[builtins.str] = None,
        subject_ends_with: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryTriggerCustomEventTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#data_factory_id DataFactoryTriggerCustomEvent#data_factory_id}.
        :param eventgrid_topic_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#eventgrid_topic_id DataFactoryTriggerCustomEvent#eventgrid_topic_id}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#events DataFactoryTriggerCustomEvent#events}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#name DataFactoryTriggerCustomEvent#name}.
        :param pipeline: pipeline block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#pipeline DataFactoryTriggerCustomEvent#pipeline}
        :param activated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#activated DataFactoryTriggerCustomEvent#activated}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#additional_properties DataFactoryTriggerCustomEvent#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#annotations DataFactoryTriggerCustomEvent#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#description DataFactoryTriggerCustomEvent#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#id DataFactoryTriggerCustomEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_begins_with DataFactoryTriggerCustomEvent#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_ends_with DataFactoryTriggerCustomEvent#subject_ends_with}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#timeouts DataFactoryTriggerCustomEvent#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryTriggerCustomEventTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument eventgrid_topic_id", value=eventgrid_topic_id, expected_type=type_hints["eventgrid_topic_id"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
            check_type(argname="argument activated", value=activated, expected_type=type_hints["activated"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument subject_begins_with", value=subject_begins_with, expected_type=type_hints["subject_begins_with"])
            check_type(argname="argument subject_ends_with", value=subject_ends_with, expected_type=type_hints["subject_ends_with"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "eventgrid_topic_id": eventgrid_topic_id,
            "events": events,
            "name": name,
            "pipeline": pipeline,
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
        if activated is not None:
            self._values["activated"] = activated
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if annotations is not None:
            self._values["annotations"] = annotations
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if subject_begins_with is not None:
            self._values["subject_begins_with"] = subject_begins_with
        if subject_ends_with is not None:
            self._values["subject_ends_with"] = subject_ends_with
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
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#data_factory_id DataFactoryTriggerCustomEvent#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def eventgrid_topic_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#eventgrid_topic_id DataFactoryTriggerCustomEvent#eventgrid_topic_id}.'''
        result = self._values.get("eventgrid_topic_id")
        assert result is not None, "Required property 'eventgrid_topic_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#events DataFactoryTriggerCustomEvent#events}.'''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#name DataFactoryTriggerCustomEvent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pipeline(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DataFactoryTriggerCustomEventPipeline"]]:
        '''pipeline block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#pipeline DataFactoryTriggerCustomEvent#pipeline}
        '''
        result = self._values.get("pipeline")
        assert result is not None, "Required property 'pipeline' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DataFactoryTriggerCustomEventPipeline"]], result)

    @builtins.property
    def activated(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#activated DataFactoryTriggerCustomEvent#activated}.'''
        result = self._values.get("activated")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def additional_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#additional_properties DataFactoryTriggerCustomEvent#additional_properties}.'''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#annotations DataFactoryTriggerCustomEvent#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#description DataFactoryTriggerCustomEvent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#id DataFactoryTriggerCustomEvent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_begins_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_begins_with DataFactoryTriggerCustomEvent#subject_begins_with}.'''
        result = self._values.get("subject_begins_with")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_ends_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#subject_ends_with DataFactoryTriggerCustomEvent#subject_ends_with}.'''
        result = self._values.get("subject_ends_with")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryTriggerCustomEventTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#timeouts DataFactoryTriggerCustomEvent#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryTriggerCustomEventTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryTriggerCustomEventConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventPipeline",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryTriggerCustomEventPipeline:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#name DataFactoryTriggerCustomEvent#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#parameters DataFactoryTriggerCustomEvent#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventPipeline.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#name DataFactoryTriggerCustomEvent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#parameters DataFactoryTriggerCustomEvent#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryTriggerCustomEventPipeline(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryTriggerCustomEventPipelineList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventPipelineList",
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
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventPipelineList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataFactoryTriggerCustomEventPipelineOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventPipelineList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataFactoryTriggerCustomEventPipelineOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryTriggerCustomEventPipeline]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryTriggerCustomEventPipeline]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryTriggerCustomEventPipeline]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryTriggerCustomEventPipelineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventPipelineOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventPipelineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryTriggerCustomEventPipeline, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryTriggerCustomEventPipeline, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryTriggerCustomEventPipeline, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventPipelineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryTriggerCustomEventTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#create DataFactoryTriggerCustomEvent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#delete DataFactoryTriggerCustomEvent#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#read DataFactoryTriggerCustomEvent#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#update DataFactoryTriggerCustomEvent#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#create DataFactoryTriggerCustomEvent#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#delete DataFactoryTriggerCustomEvent#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#read DataFactoryTriggerCustomEvent#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_trigger_custom_event#update DataFactoryTriggerCustomEvent#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryTriggerCustomEventTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryTriggerCustomEventTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryTriggerCustomEvent.DataFactoryTriggerCustomEventTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryTriggerCustomEventTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryTriggerCustomEventTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryTriggerCustomEventTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryTriggerCustomEventTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryTriggerCustomEventTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryTriggerCustomEvent",
    "DataFactoryTriggerCustomEventConfig",
    "DataFactoryTriggerCustomEventPipeline",
    "DataFactoryTriggerCustomEventPipelineList",
    "DataFactoryTriggerCustomEventPipelineOutputReference",
    "DataFactoryTriggerCustomEventTimeouts",
    "DataFactoryTriggerCustomEventTimeoutsOutputReference",
]

publication.publish()
