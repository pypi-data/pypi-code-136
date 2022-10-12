'''
# `azurerm_data_factory_flowlet_data_flow`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_flowlet_data_flow`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow).
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


class DataFactoryFlowletDataFlow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow azurerm_data_factory_flowlet_data_flow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        name: builtins.str,
        sink: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSink", typing.Dict[str, typing.Any]]]],
        source: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSource", typing.Dict[str, typing.Any]]]],
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        script: typing.Optional[builtins.str] = None,
        script_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryFlowletDataFlowTimeouts", typing.Dict[str, typing.Any]]] = None,
        transformation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowTransformation", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow azurerm_data_factory_flowlet_data_flow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#data_factory_id DataFactoryFlowletDataFlow#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param sink: sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#sink DataFactoryFlowletDataFlow#sink}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#source DataFactoryFlowletDataFlow#source}
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#annotations DataFactoryFlowletDataFlow#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.
        :param folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#folder DataFactoryFlowletDataFlow#folder}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#id DataFactoryFlowletDataFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script DataFactoryFlowletDataFlow#script}.
        :param script_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script_lines DataFactoryFlowletDataFlow#script_lines}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#timeouts DataFactoryFlowletDataFlow#timeouts}
        :param transformation: transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#transformation DataFactoryFlowletDataFlow#transformation}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlow.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryFlowletDataFlowConfig(
            data_factory_id=data_factory_id,
            name=name,
            sink=sink,
            source=source,
            annotations=annotations,
            description=description,
            folder=folder,
            id=id,
            script=script,
            script_lines=script_lines,
            timeouts=timeouts,
            transformation=transformation,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSink")
    def put_sink(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSink", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlow.put_sink)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSink", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSource", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlow.put_source)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#create DataFactoryFlowletDataFlow#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#delete DataFactoryFlowletDataFlow#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#read DataFactoryFlowletDataFlow#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#update DataFactoryFlowletDataFlow#update}.
        '''
        value = DataFactoryFlowletDataFlowTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTransformation")
    def put_transformation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowTransformation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlow.put_transformation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransformation", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScript")
    def reset_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScript", []))

    @jsii.member(jsii_name="resetScriptLines")
    def reset_script_lines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptLines", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransformation")
    def reset_transformation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransformation", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="sink")
    def sink(self) -> "DataFactoryFlowletDataFlowSinkList":
        return typing.cast("DataFactoryFlowletDataFlowSinkList", jsii.get(self, "sink"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "DataFactoryFlowletDataFlowSourceList":
        return typing.cast("DataFactoryFlowletDataFlowSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataFactoryFlowletDataFlowTimeoutsOutputReference":
        return typing.cast("DataFactoryFlowletDataFlowTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transformation")
    def transformation(self) -> "DataFactoryFlowletDataFlowTransformationList":
        return typing.cast("DataFactoryFlowletDataFlowTransformationList", jsii.get(self, "transformation"))

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
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptLinesInput")
    def script_lines_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scriptLinesInput"))

    @builtins.property
    @jsii.member(jsii_name="sinkInput")
    def sink_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSink"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSink"]]], jsii.get(self, "sinkInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSource"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryFlowletDataFlowTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryFlowletDataFlowTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transformationInput")
    def transformation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowTransformation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowTransformation"]]], jsii.get(self, "transformationInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="scriptLines")
    def script_lines(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scriptLines"))

    @script_lines.setter
    def script_lines(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlow, "script_lines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptLines", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowConfig",
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
        "name": "name",
        "sink": "sink",
        "source": "source",
        "annotations": "annotations",
        "description": "description",
        "folder": "folder",
        "id": "id",
        "script": "script",
        "script_lines": "scriptLines",
        "timeouts": "timeouts",
        "transformation": "transformation",
    },
)
class DataFactoryFlowletDataFlowConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        sink: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSink", typing.Dict[str, typing.Any]]]],
        source: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowSource", typing.Dict[str, typing.Any]]]],
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        script: typing.Optional[builtins.str] = None,
        script_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryFlowletDataFlowTimeouts", typing.Dict[str, typing.Any]]] = None,
        transformation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataFactoryFlowletDataFlowTransformation", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#data_factory_id DataFactoryFlowletDataFlow#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param sink: sink block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#sink DataFactoryFlowletDataFlow#sink}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#source DataFactoryFlowletDataFlow#source}
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#annotations DataFactoryFlowletDataFlow#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.
        :param folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#folder DataFactoryFlowletDataFlow#folder}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#id DataFactoryFlowletDataFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script DataFactoryFlowletDataFlow#script}.
        :param script_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script_lines DataFactoryFlowletDataFlow#script_lines}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#timeouts DataFactoryFlowletDataFlow#timeouts}
        :param transformation: transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#transformation DataFactoryFlowletDataFlow#transformation}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryFlowletDataFlowTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sink", value=sink, expected_type=type_hints["sink"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument script_lines", value=script_lines, expected_type=type_hints["script_lines"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transformation", value=transformation, expected_type=type_hints["transformation"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "name": name,
            "sink": sink,
            "source": source,
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
        if annotations is not None:
            self._values["annotations"] = annotations
        if description is not None:
            self._values["description"] = description
        if folder is not None:
            self._values["folder"] = folder
        if id is not None:
            self._values["id"] = id
        if script is not None:
            self._values["script"] = script
        if script_lines is not None:
            self._values["script_lines"] = script_lines
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transformation is not None:
            self._values["transformation"] = transformation

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#data_factory_id DataFactoryFlowletDataFlow#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sink(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSink"]]:
        '''sink block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#sink DataFactoryFlowletDataFlow#sink}
        '''
        result = self._values.get("sink")
        assert result is not None, "Required property 'sink' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSink"]], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSource"]]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#source DataFactoryFlowletDataFlow#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowSource"]], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#annotations DataFactoryFlowletDataFlow#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#folder DataFactoryFlowletDataFlow#folder}.'''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#id DataFactoryFlowletDataFlow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script DataFactoryFlowletDataFlow#script}.'''
        result = self._values.get("script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script_lines(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#script_lines DataFactoryFlowletDataFlow#script_lines}.'''
        result = self._values.get("script_lines")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryFlowletDataFlowTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#timeouts DataFactoryFlowletDataFlow#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowTimeouts"], result)

    @builtins.property
    def transformation(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowTransformation"]]]:
        '''transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#transformation DataFactoryFlowletDataFlow#transformation}
        '''
        result = self._values.get("transformation")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataFactoryFlowletDataFlowTransformation"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSink",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset": "dataset",
        "description": "description",
        "flowlet": "flowlet",
        "linked_service": "linkedService",
        "rejected_linked_service": "rejectedLinkedService",
        "schema_linked_service": "schemaLinkedService",
    },
)
class DataFactoryFlowletDataFlowSink:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSinkDataset", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        flowlet: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSinkFlowlet", typing.Dict[str, typing.Any]]] = None,
        linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSinkLinkedService", typing.Dict[str, typing.Any]]] = None,
        rejected_linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSinkRejectedLinkedService", typing.Dict[str, typing.Any]]] = None,
        schema_linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSinkSchemaLinkedService", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.
        :param flowlet: flowlet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        :param linked_service: linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        :param rejected_linked_service: rejected_linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#rejected_linked_service DataFactoryFlowletDataFlow#rejected_linked_service}
        :param schema_linked_service: schema_linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#schema_linked_service DataFactoryFlowletDataFlow#schema_linked_service}
        '''
        if isinstance(dataset, dict):
            dataset = DataFactoryFlowletDataFlowSinkDataset(**dataset)
        if isinstance(flowlet, dict):
            flowlet = DataFactoryFlowletDataFlowSinkFlowlet(**flowlet)
        if isinstance(linked_service, dict):
            linked_service = DataFactoryFlowletDataFlowSinkLinkedService(**linked_service)
        if isinstance(rejected_linked_service, dict):
            rejected_linked_service = DataFactoryFlowletDataFlowSinkRejectedLinkedService(**rejected_linked_service)
        if isinstance(schema_linked_service, dict):
            schema_linked_service = DataFactoryFlowletDataFlowSinkSchemaLinkedService(**schema_linked_service)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSink.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flowlet", value=flowlet, expected_type=type_hints["flowlet"])
            check_type(argname="argument linked_service", value=linked_service, expected_type=type_hints["linked_service"])
            check_type(argname="argument rejected_linked_service", value=rejected_linked_service, expected_type=type_hints["rejected_linked_service"])
            check_type(argname="argument schema_linked_service", value=schema_linked_service, expected_type=type_hints["schema_linked_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset is not None:
            self._values["dataset"] = dataset
        if description is not None:
            self._values["description"] = description
        if flowlet is not None:
            self._values["flowlet"] = flowlet
        if linked_service is not None:
            self._values["linked_service"] = linked_service
        if rejected_linked_service is not None:
            self._values["rejected_linked_service"] = rejected_linked_service
        if schema_linked_service is not None:
            self._values["schema_linked_service"] = schema_linked_service

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset(self) -> typing.Optional["DataFactoryFlowletDataFlowSinkDataset"]:
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        '''
        result = self._values.get("dataset")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkDataset"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flowlet(self) -> typing.Optional["DataFactoryFlowletDataFlowSinkFlowlet"]:
        '''flowlet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        '''
        result = self._values.get("flowlet")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkFlowlet"], result)

    @builtins.property
    def linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSinkLinkedService"]:
        '''linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        '''
        result = self._values.get("linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkLinkedService"], result)

    @builtins.property
    def rejected_linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSinkRejectedLinkedService"]:
        '''rejected_linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#rejected_linked_service DataFactoryFlowletDataFlow#rejected_linked_service}
        '''
        result = self._values.get("rejected_linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkRejectedLinkedService"], result)

    @builtins.property
    def schema_linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSinkSchemaLinkedService"]:
        '''schema_linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#schema_linked_service DataFactoryFlowletDataFlow#schema_linked_service}
        '''
        result = self._values.get("schema_linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkSchemaLinkedService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSink(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkDataset",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSinkDataset:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkDataset.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSinkDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSinkDatasetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkDatasetOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkDatasetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkDatasetOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkDatasetOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataFactoryFlowletDataFlowSinkDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSinkDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkDatasetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkFlowlet",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset_parameters": "datasetParameters",
        "parameters": "parameters",
    },
)
class DataFactoryFlowletDataFlowSinkFlowlet:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkFlowlet.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset_parameters", value=dataset_parameters, expected_type=type_hints["dataset_parameters"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset_parameters is not None:
            self._values["dataset_parameters"] = dataset_parameters
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.'''
        result = self._values.get("dataset_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSinkFlowlet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSinkFlowletOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkFlowletOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkFlowletOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetParameters")
    def reset_dataset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetParameters", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="datasetParametersInput")
    def dataset_parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetParametersInput"))

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
    @jsii.member(jsii_name="datasetParameters")
    def dataset_parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetParameters"))

    @dataset_parameters.setter
    def dataset_parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkFlowletOutputReference, "dataset_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetParameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkFlowletOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkFlowletOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataFactoryFlowletDataFlowSinkFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkFlowlet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSinkFlowlet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkFlowletOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSinkLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSinkLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSinkLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSinkLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowSinkList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkList",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataFactoryFlowletDataFlowSinkOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataFactoryFlowletDataFlowSinkOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSink]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSink]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSink]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowSinkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSinkDataset(name=name, parameters=parameters)

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @jsii.member(jsii_name="putFlowlet")
    def put_flowlet(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSinkFlowlet(
            name=name, dataset_parameters=dataset_parameters, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putFlowlet", [value]))

    @jsii.member(jsii_name="putLinkedService")
    def put_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSinkLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedService", [value]))

    @jsii.member(jsii_name="putRejectedLinkedService")
    def put_rejected_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSinkRejectedLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRejectedLinkedService", [value]))

    @jsii.member(jsii_name="putSchemaLinkedService")
    def put_schema_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSinkSchemaLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaLinkedService", [value]))

    @jsii.member(jsii_name="resetDataset")
    def reset_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataset", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFlowlet")
    def reset_flowlet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlowlet", []))

    @jsii.member(jsii_name="resetLinkedService")
    def reset_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedService", []))

    @jsii.member(jsii_name="resetRejectedLinkedService")
    def reset_rejected_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedLinkedService", []))

    @jsii.member(jsii_name="resetSchemaLinkedService")
    def reset_schema_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaLinkedService", []))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> DataFactoryFlowletDataFlowSinkDatasetOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSinkDatasetOutputReference, jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="flowlet")
    def flowlet(self) -> DataFactoryFlowletDataFlowSinkFlowletOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSinkFlowletOutputReference, jsii.get(self, "flowlet"))

    @builtins.property
    @jsii.member(jsii_name="linkedService")
    def linked_service(
        self,
    ) -> DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference, jsii.get(self, "linkedService"))

    @builtins.property
    @jsii.member(jsii_name="rejectedLinkedService")
    def rejected_linked_service(
        self,
    ) -> "DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference":
        return typing.cast("DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference", jsii.get(self, "rejectedLinkedService"))

    @builtins.property
    @jsii.member(jsii_name="schemaLinkedService")
    def schema_linked_service(
        self,
    ) -> "DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference":
        return typing.cast("DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference", jsii.get(self, "schemaLinkedService"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[DataFactoryFlowletDataFlowSinkDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkDataset], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="flowletInput")
    def flowlet_input(self) -> typing.Optional[DataFactoryFlowletDataFlowSinkFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkFlowlet], jsii.get(self, "flowletInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedServiceInput")
    def linked_service_input(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSinkLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkLinkedService], jsii.get(self, "linkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedLinkedServiceInput")
    def rejected_linked_service_input(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSinkRejectedLinkedService"]:
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkRejectedLinkedService"], jsii.get(self, "rejectedLinkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaLinkedServiceInput")
    def schema_linked_service_input(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSinkSchemaLinkedService"]:
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSinkSchemaLinkedService"], jsii.get(self, "schemaLinkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryFlowletDataFlowSink, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryFlowletDataFlowSink, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryFlowletDataFlowSink, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkRejectedLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSinkRejectedLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkRejectedLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSinkRejectedLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSinkRejectedLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkRejectedLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSinkRejectedLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkSchemaLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSinkSchemaLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkSchemaLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSinkSchemaLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSinkSchemaLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSinkSchemaLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSinkSchemaLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSource",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset": "dataset",
        "description": "description",
        "flowlet": "flowlet",
        "linked_service": "linkedService",
        "rejected_linked_service": "rejectedLinkedService",
        "schema_linked_service": "schemaLinkedService",
    },
)
class DataFactoryFlowletDataFlowSource:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSourceDataset", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        flowlet: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSourceFlowlet", typing.Dict[str, typing.Any]]] = None,
        linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSourceLinkedService", typing.Dict[str, typing.Any]]] = None,
        rejected_linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSourceRejectedLinkedService", typing.Dict[str, typing.Any]]] = None,
        schema_linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowSourceSchemaLinkedService", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.
        :param flowlet: flowlet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        :param linked_service: linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        :param rejected_linked_service: rejected_linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#rejected_linked_service DataFactoryFlowletDataFlow#rejected_linked_service}
        :param schema_linked_service: schema_linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#schema_linked_service DataFactoryFlowletDataFlow#schema_linked_service}
        '''
        if isinstance(dataset, dict):
            dataset = DataFactoryFlowletDataFlowSourceDataset(**dataset)
        if isinstance(flowlet, dict):
            flowlet = DataFactoryFlowletDataFlowSourceFlowlet(**flowlet)
        if isinstance(linked_service, dict):
            linked_service = DataFactoryFlowletDataFlowSourceLinkedService(**linked_service)
        if isinstance(rejected_linked_service, dict):
            rejected_linked_service = DataFactoryFlowletDataFlowSourceRejectedLinkedService(**rejected_linked_service)
        if isinstance(schema_linked_service, dict):
            schema_linked_service = DataFactoryFlowletDataFlowSourceSchemaLinkedService(**schema_linked_service)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSource.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flowlet", value=flowlet, expected_type=type_hints["flowlet"])
            check_type(argname="argument linked_service", value=linked_service, expected_type=type_hints["linked_service"])
            check_type(argname="argument rejected_linked_service", value=rejected_linked_service, expected_type=type_hints["rejected_linked_service"])
            check_type(argname="argument schema_linked_service", value=schema_linked_service, expected_type=type_hints["schema_linked_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset is not None:
            self._values["dataset"] = dataset
        if description is not None:
            self._values["description"] = description
        if flowlet is not None:
            self._values["flowlet"] = flowlet
        if linked_service is not None:
            self._values["linked_service"] = linked_service
        if rejected_linked_service is not None:
            self._values["rejected_linked_service"] = rejected_linked_service
        if schema_linked_service is not None:
            self._values["schema_linked_service"] = schema_linked_service

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset(self) -> typing.Optional["DataFactoryFlowletDataFlowSourceDataset"]:
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        '''
        result = self._values.get("dataset")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceDataset"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flowlet(self) -> typing.Optional["DataFactoryFlowletDataFlowSourceFlowlet"]:
        '''flowlet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        '''
        result = self._values.get("flowlet")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceFlowlet"], result)

    @builtins.property
    def linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSourceLinkedService"]:
        '''linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        '''
        result = self._values.get("linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceLinkedService"], result)

    @builtins.property
    def rejected_linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSourceRejectedLinkedService"]:
        '''rejected_linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#rejected_linked_service DataFactoryFlowletDataFlow#rejected_linked_service}
        '''
        result = self._values.get("rejected_linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceRejectedLinkedService"], result)

    @builtins.property
    def schema_linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSourceSchemaLinkedService"]:
        '''schema_linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#schema_linked_service DataFactoryFlowletDataFlow#schema_linked_service}
        '''
        result = self._values.get("schema_linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceSchemaLinkedService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceDataset",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSourceDataset:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceDataset.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSourceDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSourceDatasetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceDatasetOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceDatasetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceDatasetOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceDatasetOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSourceDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceDatasetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceFlowlet",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset_parameters": "datasetParameters",
        "parameters": "parameters",
    },
)
class DataFactoryFlowletDataFlowSourceFlowlet:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceFlowlet.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset_parameters", value=dataset_parameters, expected_type=type_hints["dataset_parameters"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset_parameters is not None:
            self._values["dataset_parameters"] = dataset_parameters
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.'''
        result = self._values.get("dataset_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSourceFlowlet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSourceFlowletOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceFlowletOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceFlowletOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetParameters")
    def reset_dataset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetParameters", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="datasetParametersInput")
    def dataset_parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetParametersInput"))

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
    @jsii.member(jsii_name="datasetParameters")
    def dataset_parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetParameters"))

    @dataset_parameters.setter
    def dataset_parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceFlowletOutputReference, "dataset_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetParameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceFlowletOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceFlowletOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceFlowlet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSourceFlowlet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceFlowletOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSourceLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSourceLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSourceLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowSourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceList",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataFactoryFlowletDataFlowSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataFactoryFlowletDataFlowSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSourceDataset(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @jsii.member(jsii_name="putFlowlet")
    def put_flowlet(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSourceFlowlet(
            name=name, dataset_parameters=dataset_parameters, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putFlowlet", [value]))

    @jsii.member(jsii_name="putLinkedService")
    def put_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSourceLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedService", [value]))

    @jsii.member(jsii_name="putRejectedLinkedService")
    def put_rejected_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSourceRejectedLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRejectedLinkedService", [value]))

    @jsii.member(jsii_name="putSchemaLinkedService")
    def put_schema_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowSourceSchemaLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaLinkedService", [value]))

    @jsii.member(jsii_name="resetDataset")
    def reset_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataset", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFlowlet")
    def reset_flowlet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlowlet", []))

    @jsii.member(jsii_name="resetLinkedService")
    def reset_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedService", []))

    @jsii.member(jsii_name="resetRejectedLinkedService")
    def reset_rejected_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedLinkedService", []))

    @jsii.member(jsii_name="resetSchemaLinkedService")
    def reset_schema_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaLinkedService", []))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> DataFactoryFlowletDataFlowSourceDatasetOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSourceDatasetOutputReference, jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="flowlet")
    def flowlet(self) -> DataFactoryFlowletDataFlowSourceFlowletOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSourceFlowletOutputReference, jsii.get(self, "flowlet"))

    @builtins.property
    @jsii.member(jsii_name="linkedService")
    def linked_service(
        self,
    ) -> DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference, jsii.get(self, "linkedService"))

    @builtins.property
    @jsii.member(jsii_name="rejectedLinkedService")
    def rejected_linked_service(
        self,
    ) -> "DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference":
        return typing.cast("DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference", jsii.get(self, "rejectedLinkedService"))

    @builtins.property
    @jsii.member(jsii_name="schemaLinkedService")
    def schema_linked_service(
        self,
    ) -> "DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference":
        return typing.cast("DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference", jsii.get(self, "schemaLinkedService"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[DataFactoryFlowletDataFlowSourceDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceDataset], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="flowletInput")
    def flowlet_input(self) -> typing.Optional[DataFactoryFlowletDataFlowSourceFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceFlowlet], jsii.get(self, "flowletInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedServiceInput")
    def linked_service_input(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceLinkedService], jsii.get(self, "linkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedLinkedServiceInput")
    def rejected_linked_service_input(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSourceRejectedLinkedService"]:
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceRejectedLinkedService"], jsii.get(self, "rejectedLinkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaLinkedServiceInput")
    def schema_linked_service_input(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowSourceSchemaLinkedService"]:
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowSourceSchemaLinkedService"], jsii.get(self, "schemaLinkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryFlowletDataFlowSource, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryFlowletDataFlowSource, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryFlowletDataFlowSource, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceRejectedLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSourceRejectedLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceRejectedLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSourceRejectedLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceRejectedLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceRejectedLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSourceRejectedLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceSchemaLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowSourceSchemaLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceSchemaLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowSourceSchemaLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowSourceSchemaLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowSourceSchemaLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowSourceSchemaLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryFlowletDataFlowTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#create DataFactoryFlowletDataFlow#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#delete DataFactoryFlowletDataFlow#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#read DataFactoryFlowletDataFlow#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#update DataFactoryFlowletDataFlow#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#create DataFactoryFlowletDataFlow#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#delete DataFactoryFlowletDataFlow#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#read DataFactoryFlowletDataFlow#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#update DataFactoryFlowletDataFlow#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryFlowletDataFlowTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryFlowletDataFlowTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryFlowletDataFlowTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformation",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset": "dataset",
        "description": "description",
        "flowlet": "flowlet",
        "linked_service": "linkedService",
    },
)
class DataFactoryFlowletDataFlowTransformation:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset: typing.Optional[typing.Union["DataFactoryFlowletDataFlowTransformationDataset", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        flowlet: typing.Optional[typing.Union["DataFactoryFlowletDataFlowTransformationFlowlet", typing.Dict[str, typing.Any]]] = None,
        linked_service: typing.Optional[typing.Union["DataFactoryFlowletDataFlowTransformationLinkedService", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.
        :param flowlet: flowlet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        :param linked_service: linked_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        '''
        if isinstance(dataset, dict):
            dataset = DataFactoryFlowletDataFlowTransformationDataset(**dataset)
        if isinstance(flowlet, dict):
            flowlet = DataFactoryFlowletDataFlowTransformationFlowlet(**flowlet)
        if isinstance(linked_service, dict):
            linked_service = DataFactoryFlowletDataFlowTransformationLinkedService(**linked_service)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformation.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flowlet", value=flowlet, expected_type=type_hints["flowlet"])
            check_type(argname="argument linked_service", value=linked_service, expected_type=type_hints["linked_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset is not None:
            self._values["dataset"] = dataset
        if description is not None:
            self._values["description"] = description
        if flowlet is not None:
            self._values["flowlet"] = flowlet
        if linked_service is not None:
            self._values["linked_service"] = linked_service

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowTransformationDataset"]:
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset DataFactoryFlowletDataFlow#dataset}
        '''
        result = self._values.get("dataset")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowTransformationDataset"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#description DataFactoryFlowletDataFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flowlet(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowTransformationFlowlet"]:
        '''flowlet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#flowlet DataFactoryFlowletDataFlow#flowlet}
        '''
        result = self._values.get("flowlet")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowTransformationFlowlet"], result)

    @builtins.property
    def linked_service(
        self,
    ) -> typing.Optional["DataFactoryFlowletDataFlowTransformationLinkedService"]:
        '''linked_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#linked_service DataFactoryFlowletDataFlow#linked_service}
        '''
        result = self._values.get("linked_service")
        return typing.cast(typing.Optional["DataFactoryFlowletDataFlowTransformationLinkedService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationDataset",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowTransformationDataset:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationDataset.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowTransformationDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowTransformationDatasetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationDatasetOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationDatasetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationDatasetOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationDatasetOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowTransformationDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationDatasetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationFlowlet",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dataset_parameters": "datasetParameters",
        "parameters": "parameters",
    },
)
class DataFactoryFlowletDataFlowTransformationFlowlet:
    def __init__(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationFlowlet.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dataset_parameters", value=dataset_parameters, expected_type=type_hints["dataset_parameters"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dataset_parameters is not None:
            self._values["dataset_parameters"] = dataset_parameters
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.'''
        result = self._values.get("dataset_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowTransformationFlowlet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowTransformationFlowletOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationFlowletOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationFlowletOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetParameters")
    def reset_dataset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetParameters", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="datasetParametersInput")
    def dataset_parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetParametersInput"))

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
    @jsii.member(jsii_name="datasetParameters")
    def dataset_parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetParameters"))

    @dataset_parameters.setter
    def dataset_parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationFlowletOutputReference, "dataset_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetParameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationFlowletOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationFlowletOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationFlowlet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowTransformationFlowlet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationFlowletOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationLinkedService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class DataFactoryFlowletDataFlowTransformationLinkedService:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationLinkedService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryFlowletDataFlowTransformationLinkedService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationLinkedService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryFlowletDataFlowTransformationLinkedService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowTransformationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationList",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataFactoryFlowletDataFlowTransformationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataFactoryFlowletDataFlowTransformationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowTransformation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowTransformation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataFactoryFlowletDataFlowTransformation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataFactoryFlowletDataFlowTransformationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryFlowletDataFlow.DataFactoryFlowletDataFlowTransformationOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryFlowletDataFlowTransformationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowTransformationDataset(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @jsii.member(jsii_name="putFlowlet")
    def put_flowlet(
        self,
        *,
        name: builtins.str,
        dataset_parameters: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param dataset_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#dataset_parameters DataFactoryFlowletDataFlow#dataset_parameters}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowTransformationFlowlet(
            name=name, dataset_parameters=dataset_parameters, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putFlowlet", [value]))

    @jsii.member(jsii_name="putLinkedService")
    def put_linked_service(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#name DataFactoryFlowletDataFlow#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_flowlet_data_flow#parameters DataFactoryFlowletDataFlow#parameters}.
        '''
        value = DataFactoryFlowletDataFlowTransformationLinkedService(
            name=name, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedService", [value]))

    @jsii.member(jsii_name="resetDataset")
    def reset_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataset", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFlowlet")
    def reset_flowlet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlowlet", []))

    @jsii.member(jsii_name="resetLinkedService")
    def reset_linked_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedService", []))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> DataFactoryFlowletDataFlowTransformationDatasetOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowTransformationDatasetOutputReference, jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="flowlet")
    def flowlet(self) -> DataFactoryFlowletDataFlowTransformationFlowletOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowTransformationFlowletOutputReference, jsii.get(self, "flowlet"))

    @builtins.property
    @jsii.member(jsii_name="linkedService")
    def linked_service(
        self,
    ) -> DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference:
        return typing.cast(DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference, jsii.get(self, "linkedService"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationDataset]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationDataset], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="flowletInput")
    def flowlet_input(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationFlowlet]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationFlowlet], jsii.get(self, "flowletInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedServiceInput")
    def linked_service_input(
        self,
    ) -> typing.Optional[DataFactoryFlowletDataFlowTransformationLinkedService]:
        return typing.cast(typing.Optional[DataFactoryFlowletDataFlowTransformationLinkedService], jsii.get(self, "linkedServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryFlowletDataFlowTransformation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryFlowletDataFlowTransformation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryFlowletDataFlowTransformation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryFlowletDataFlowTransformationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryFlowletDataFlow",
    "DataFactoryFlowletDataFlowConfig",
    "DataFactoryFlowletDataFlowSink",
    "DataFactoryFlowletDataFlowSinkDataset",
    "DataFactoryFlowletDataFlowSinkDatasetOutputReference",
    "DataFactoryFlowletDataFlowSinkFlowlet",
    "DataFactoryFlowletDataFlowSinkFlowletOutputReference",
    "DataFactoryFlowletDataFlowSinkLinkedService",
    "DataFactoryFlowletDataFlowSinkLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowSinkList",
    "DataFactoryFlowletDataFlowSinkOutputReference",
    "DataFactoryFlowletDataFlowSinkRejectedLinkedService",
    "DataFactoryFlowletDataFlowSinkRejectedLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowSinkSchemaLinkedService",
    "DataFactoryFlowletDataFlowSinkSchemaLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowSource",
    "DataFactoryFlowletDataFlowSourceDataset",
    "DataFactoryFlowletDataFlowSourceDatasetOutputReference",
    "DataFactoryFlowletDataFlowSourceFlowlet",
    "DataFactoryFlowletDataFlowSourceFlowletOutputReference",
    "DataFactoryFlowletDataFlowSourceLinkedService",
    "DataFactoryFlowletDataFlowSourceLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowSourceList",
    "DataFactoryFlowletDataFlowSourceOutputReference",
    "DataFactoryFlowletDataFlowSourceRejectedLinkedService",
    "DataFactoryFlowletDataFlowSourceRejectedLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowSourceSchemaLinkedService",
    "DataFactoryFlowletDataFlowSourceSchemaLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowTimeouts",
    "DataFactoryFlowletDataFlowTimeoutsOutputReference",
    "DataFactoryFlowletDataFlowTransformation",
    "DataFactoryFlowletDataFlowTransformationDataset",
    "DataFactoryFlowletDataFlowTransformationDatasetOutputReference",
    "DataFactoryFlowletDataFlowTransformationFlowlet",
    "DataFactoryFlowletDataFlowTransformationFlowletOutputReference",
    "DataFactoryFlowletDataFlowTransformationLinkedService",
    "DataFactoryFlowletDataFlowTransformationLinkedServiceOutputReference",
    "DataFactoryFlowletDataFlowTransformationList",
    "DataFactoryFlowletDataFlowTransformationOutputReference",
]

publication.publish()
