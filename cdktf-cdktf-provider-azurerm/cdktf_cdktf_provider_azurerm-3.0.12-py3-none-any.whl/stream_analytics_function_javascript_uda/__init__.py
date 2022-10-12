'''
# `azurerm_stream_analytics_function_javascript_uda`

Refer to the Terraform Registory for docs: [`azurerm_stream_analytics_function_javascript_uda`](https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda).
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


class StreamAnalyticsFunctionJavascriptUda(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUda",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda azurerm_stream_analytics_function_javascript_uda}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        input: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StreamAnalyticsFunctionJavascriptUdaInput", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        output: typing.Union["StreamAnalyticsFunctionJavascriptUdaOutput", typing.Dict[str, typing.Any]],
        script: builtins.str,
        stream_analytics_job_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsFunctionJavascriptUdaTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda azurerm_stream_analytics_function_javascript_uda} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#input StreamAnalyticsFunctionJavascriptUda#input}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#name StreamAnalyticsFunctionJavascriptUda#name}.
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#output StreamAnalyticsFunctionJavascriptUda#output}
        :param script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#script StreamAnalyticsFunctionJavascriptUda#script}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#stream_analytics_job_id StreamAnalyticsFunctionJavascriptUda#stream_analytics_job_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#id StreamAnalyticsFunctionJavascriptUda#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#timeouts StreamAnalyticsFunctionJavascriptUda#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUda.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StreamAnalyticsFunctionJavascriptUdaConfig(
            input=input,
            name=name,
            output=output,
            script=script,
            stream_analytics_job_id=stream_analytics_job_id,
            id=id,
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

    @jsii.member(jsii_name="putInput")
    def put_input(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StreamAnalyticsFunctionJavascriptUdaInput", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUda.put_input)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInput", [value]))

    @jsii.member(jsii_name="putOutput")
    def put_output(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#type StreamAnalyticsFunctionJavascriptUda#type}.
        '''
        value = StreamAnalyticsFunctionJavascriptUdaOutput(type=type)

        return typing.cast(None, jsii.invoke(self, "putOutput", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#create StreamAnalyticsFunctionJavascriptUda#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#delete StreamAnalyticsFunctionJavascriptUda#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#read StreamAnalyticsFunctionJavascriptUda#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#update StreamAnalyticsFunctionJavascriptUda#update}.
        '''
        value = StreamAnalyticsFunctionJavascriptUdaTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="input")
    def input(self) -> "StreamAnalyticsFunctionJavascriptUdaInputList":
        return typing.cast("StreamAnalyticsFunctionJavascriptUdaInputList", jsii.get(self, "input"))

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(self) -> "StreamAnalyticsFunctionJavascriptUdaOutputOutputReference":
        return typing.cast("StreamAnalyticsFunctionJavascriptUdaOutputOutputReference", jsii.get(self, "output"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference":
        return typing.cast("StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StreamAnalyticsFunctionJavascriptUdaInput"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StreamAnalyticsFunctionJavascriptUdaInput"]]], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputInput")
    def output_input(
        self,
    ) -> typing.Optional["StreamAnalyticsFunctionJavascriptUdaOutput"]:
        return typing.cast(typing.Optional["StreamAnalyticsFunctionJavascriptUdaOutput"], jsii.get(self, "outputInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobIdInput")
    def stream_analytics_job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamAnalyticsJobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StreamAnalyticsFunctionJavascriptUdaTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StreamAnalyticsFunctionJavascriptUdaTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUda, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUda, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUda, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamAnalyticsJobId"))

    @stream_analytics_job_id.setter
    def stream_analytics_job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUda, "stream_analytics_job_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamAnalyticsJobId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "input": "input",
        "name": "name",
        "output": "output",
        "script": "script",
        "stream_analytics_job_id": "streamAnalyticsJobId",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class StreamAnalyticsFunctionJavascriptUdaConfig(cdktf.TerraformMetaArguments):
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
        input: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StreamAnalyticsFunctionJavascriptUdaInput", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        output: typing.Union["StreamAnalyticsFunctionJavascriptUdaOutput", typing.Dict[str, typing.Any]],
        script: builtins.str,
        stream_analytics_job_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsFunctionJavascriptUdaTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#input StreamAnalyticsFunctionJavascriptUda#input}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#name StreamAnalyticsFunctionJavascriptUda#name}.
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#output StreamAnalyticsFunctionJavascriptUda#output}
        :param script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#script StreamAnalyticsFunctionJavascriptUda#script}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#stream_analytics_job_id StreamAnalyticsFunctionJavascriptUda#stream_analytics_job_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#id StreamAnalyticsFunctionJavascriptUda#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#timeouts StreamAnalyticsFunctionJavascriptUda#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(output, dict):
            output = StreamAnalyticsFunctionJavascriptUdaOutput(**output)
        if isinstance(timeouts, dict):
            timeouts = StreamAnalyticsFunctionJavascriptUdaTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument stream_analytics_job_id", value=stream_analytics_job_id, expected_type=type_hints["stream_analytics_job_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "input": input,
            "name": name,
            "output": output,
            "script": script,
            "stream_analytics_job_id": stream_analytics_job_id,
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
    def input(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["StreamAnalyticsFunctionJavascriptUdaInput"]]:
        '''input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#input StreamAnalyticsFunctionJavascriptUda#input}
        '''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["StreamAnalyticsFunctionJavascriptUdaInput"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#name StreamAnalyticsFunctionJavascriptUda#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(self) -> "StreamAnalyticsFunctionJavascriptUdaOutput":
        '''output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#output StreamAnalyticsFunctionJavascriptUda#output}
        '''
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast("StreamAnalyticsFunctionJavascriptUdaOutput", result)

    @builtins.property
    def script(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#script StreamAnalyticsFunctionJavascriptUda#script}.'''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_analytics_job_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#stream_analytics_job_id StreamAnalyticsFunctionJavascriptUda#stream_analytics_job_id}.'''
        result = self._values.get("stream_analytics_job_id")
        assert result is not None, "Required property 'stream_analytics_job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#id StreamAnalyticsFunctionJavascriptUda#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["StreamAnalyticsFunctionJavascriptUdaTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#timeouts StreamAnalyticsFunctionJavascriptUda#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StreamAnalyticsFunctionJavascriptUdaTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsFunctionJavascriptUdaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaInput",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "configuration_parameter": "configurationParameter"},
)
class StreamAnalyticsFunctionJavascriptUdaInput:
    def __init__(
        self,
        *,
        type: builtins.str,
        configuration_parameter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#type StreamAnalyticsFunctionJavascriptUda#type}.
        :param configuration_parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#configuration_parameter StreamAnalyticsFunctionJavascriptUda#configuration_parameter}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaInput.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument configuration_parameter", value=configuration_parameter, expected_type=type_hints["configuration_parameter"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if configuration_parameter is not None:
            self._values["configuration_parameter"] = configuration_parameter

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#type StreamAnalyticsFunctionJavascriptUda#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_parameter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#configuration_parameter StreamAnalyticsFunctionJavascriptUda#configuration_parameter}.'''
        result = self._values.get("configuration_parameter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsFunctionJavascriptUdaInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsFunctionJavascriptUdaInputList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaInputList",
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
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaInputList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StreamAnalyticsFunctionJavascriptUdaInputOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaInputList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StreamAnalyticsFunctionJavascriptUdaInputOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StreamAnalyticsFunctionJavascriptUdaInput]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StreamAnalyticsFunctionJavascriptUdaInput]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StreamAnalyticsFunctionJavascriptUdaInput]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StreamAnalyticsFunctionJavascriptUdaInputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaInputOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaInputOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConfigurationParameter")
    def reset_configuration_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationParameter", []))

    @builtins.property
    @jsii.member(jsii_name="configurationParameterInput")
    def configuration_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "configurationParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationParameter")
    def configuration_parameter(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "configurationParameter"))

    @configuration_parameter.setter
    def configuration_parameter(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputOutputReference, "configuration_parameter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationParameter", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaInput, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaInput, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaInput, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaInputOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaOutput",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class StreamAnalyticsFunctionJavascriptUdaOutput:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#type StreamAnalyticsFunctionJavascriptUda#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaOutput.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#type StreamAnalyticsFunctionJavascriptUda#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsFunctionJavascriptUdaOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsFunctionJavascriptUdaOutputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaOutputOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaOutputOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaOutputOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StreamAnalyticsFunctionJavascriptUdaOutput]:
        return typing.cast(typing.Optional[StreamAnalyticsFunctionJavascriptUdaOutput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StreamAnalyticsFunctionJavascriptUdaOutput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaOutputOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StreamAnalyticsFunctionJavascriptUdaTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#create StreamAnalyticsFunctionJavascriptUda#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#delete StreamAnalyticsFunctionJavascriptUda#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#read StreamAnalyticsFunctionJavascriptUda#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#update StreamAnalyticsFunctionJavascriptUda#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#create StreamAnalyticsFunctionJavascriptUda#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#delete StreamAnalyticsFunctionJavascriptUda#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#read StreamAnalyticsFunctionJavascriptUda#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_function_javascript_uda#update StreamAnalyticsFunctionJavascriptUda#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsFunctionJavascriptUdaTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsFunctionJavascriptUda.StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StreamAnalyticsFunctionJavascriptUdaTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StreamAnalyticsFunctionJavascriptUda",
    "StreamAnalyticsFunctionJavascriptUdaConfig",
    "StreamAnalyticsFunctionJavascriptUdaInput",
    "StreamAnalyticsFunctionJavascriptUdaInputList",
    "StreamAnalyticsFunctionJavascriptUdaInputOutputReference",
    "StreamAnalyticsFunctionJavascriptUdaOutput",
    "StreamAnalyticsFunctionJavascriptUdaOutputOutputReference",
    "StreamAnalyticsFunctionJavascriptUdaTimeouts",
    "StreamAnalyticsFunctionJavascriptUdaTimeoutsOutputReference",
]

publication.publish()
