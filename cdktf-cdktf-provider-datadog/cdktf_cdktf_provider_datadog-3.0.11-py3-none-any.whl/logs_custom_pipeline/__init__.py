'''
# `datadog_logs_custom_pipeline`

Refer to the Terraform Registory for docs: [`datadog_logs_custom_pipeline`](https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline).
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


class LogsCustomPipeline(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipeline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline datadog_logs_custom_pipeline}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineFilter", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processor: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessor", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline datadog_logs_custom_pipeline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#id LogsCustomPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.
        :param processor: processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipeline.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogsCustomPipelineConfig(
            filter=filter,
            name=name,
            id=id,
            is_enabled=is_enabled,
            processor=processor,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipeline.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putProcessor")
    def put_processor(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessor", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipeline.put_processor)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessor", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetProcessor")
    def reset_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "LogsCustomPipelineFilterList":
        return typing.cast("LogsCustomPipelineFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="processor")
    def processor(self) -> "LogsCustomPipelineProcessorList":
        return typing.cast("LogsCustomPipelineProcessorList", jsii.get(self, "processor"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="processorInput")
    def processor_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessor"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessor"]]], jsii.get(self, "processorInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipeline, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipeline, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipeline, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "name": "name",
        "id": "id",
        "is_enabled": "isEnabled",
        "processor": "processor",
    },
)
class LogsCustomPipelineConfig(cdktf.TerraformMetaArguments):
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
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineFilter", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processor: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessor", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#id LogsCustomPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.
        :param processor: processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
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
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if processor is not None:
            self._values["processor"] = processor

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
    def filter(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineFilter"]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineFilter"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#id LogsCustomPipeline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processor(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessor"]]]:
        '''processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        '''
        result = self._values.get("processor")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessor"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineFilter",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class LogsCustomPipelineFilter:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineFilter.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''Filter criteria of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineFilterList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LogsCustomPipelineFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineFilterOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "arithmetic_processor": "arithmeticProcessor",
        "attribute_remapper": "attributeRemapper",
        "category_processor": "categoryProcessor",
        "date_remapper": "dateRemapper",
        "geo_ip_parser": "geoIpParser",
        "grok_parser": "grokParser",
        "lookup_processor": "lookupProcessor",
        "message_remapper": "messageRemapper",
        "pipeline": "pipeline",
        "service_remapper": "serviceRemapper",
        "status_remapper": "statusRemapper",
        "string_builder_processor": "stringBuilderProcessor",
        "trace_id_remapper": "traceIdRemapper",
        "url_parser": "urlParser",
        "user_agent_parser": "userAgentParser",
    },
)
class LogsCustomPipelineProcessor:
    def __init__(
        self,
        *,
        arithmetic_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorArithmeticProcessor", typing.Dict[str, typing.Any]]] = None,
        attribute_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorAttributeRemapper", typing.Dict[str, typing.Any]]] = None,
        category_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorCategoryProcessor", typing.Dict[str, typing.Any]]] = None,
        date_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorDateRemapper", typing.Dict[str, typing.Any]]] = None,
        geo_ip_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorGeoIpParser", typing.Dict[str, typing.Any]]] = None,
        grok_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorGrokParser", typing.Dict[str, typing.Any]]] = None,
        lookup_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorLookupProcessor", typing.Dict[str, typing.Any]]] = None,
        message_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorMessageRemapper", typing.Dict[str, typing.Any]]] = None,
        pipeline: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipeline", typing.Dict[str, typing.Any]]] = None,
        service_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorServiceRemapper", typing.Dict[str, typing.Any]]] = None,
        status_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorStatusRemapper", typing.Dict[str, typing.Any]]] = None,
        string_builder_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorStringBuilderProcessor", typing.Dict[str, typing.Any]]] = None,
        trace_id_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorTraceIdRemapper", typing.Dict[str, typing.Any]]] = None,
        url_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorUrlParser", typing.Dict[str, typing.Any]]] = None,
        user_agent_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorUserAgentParser", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arithmetic_processor: arithmetic_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#arithmetic_processor LogsCustomPipeline#arithmetic_processor}
        :param attribute_remapper: attribute_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#attribute_remapper LogsCustomPipeline#attribute_remapper}
        :param category_processor: category_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category_processor LogsCustomPipeline#category_processor}
        :param date_remapper: date_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#date_remapper LogsCustomPipeline#date_remapper}
        :param geo_ip_parser: geo_ip_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#geo_ip_parser LogsCustomPipeline#geo_ip_parser}
        :param grok_parser: grok_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok_parser LogsCustomPipeline#grok_parser}
        :param lookup_processor: lookup_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_processor LogsCustomPipeline#lookup_processor}
        :param message_remapper: message_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#message_remapper LogsCustomPipeline#message_remapper}
        :param pipeline: pipeline block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#pipeline LogsCustomPipeline#pipeline}
        :param service_remapper: service_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#service_remapper LogsCustomPipeline#service_remapper}
        :param status_remapper: status_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#status_remapper LogsCustomPipeline#status_remapper}
        :param string_builder_processor: string_builder_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#string_builder_processor LogsCustomPipeline#string_builder_processor}
        :param trace_id_remapper: trace_id_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#trace_id_remapper LogsCustomPipeline#trace_id_remapper}
        :param url_parser: url_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#url_parser LogsCustomPipeline#url_parser}
        :param user_agent_parser: user_agent_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#user_agent_parser LogsCustomPipeline#user_agent_parser}
        '''
        if isinstance(arithmetic_processor, dict):
            arithmetic_processor = LogsCustomPipelineProcessorArithmeticProcessor(**arithmetic_processor)
        if isinstance(attribute_remapper, dict):
            attribute_remapper = LogsCustomPipelineProcessorAttributeRemapper(**attribute_remapper)
        if isinstance(category_processor, dict):
            category_processor = LogsCustomPipelineProcessorCategoryProcessor(**category_processor)
        if isinstance(date_remapper, dict):
            date_remapper = LogsCustomPipelineProcessorDateRemapper(**date_remapper)
        if isinstance(geo_ip_parser, dict):
            geo_ip_parser = LogsCustomPipelineProcessorGeoIpParser(**geo_ip_parser)
        if isinstance(grok_parser, dict):
            grok_parser = LogsCustomPipelineProcessorGrokParser(**grok_parser)
        if isinstance(lookup_processor, dict):
            lookup_processor = LogsCustomPipelineProcessorLookupProcessor(**lookup_processor)
        if isinstance(message_remapper, dict):
            message_remapper = LogsCustomPipelineProcessorMessageRemapper(**message_remapper)
        if isinstance(pipeline, dict):
            pipeline = LogsCustomPipelineProcessorPipeline(**pipeline)
        if isinstance(service_remapper, dict):
            service_remapper = LogsCustomPipelineProcessorServiceRemapper(**service_remapper)
        if isinstance(status_remapper, dict):
            status_remapper = LogsCustomPipelineProcessorStatusRemapper(**status_remapper)
        if isinstance(string_builder_processor, dict):
            string_builder_processor = LogsCustomPipelineProcessorStringBuilderProcessor(**string_builder_processor)
        if isinstance(trace_id_remapper, dict):
            trace_id_remapper = LogsCustomPipelineProcessorTraceIdRemapper(**trace_id_remapper)
        if isinstance(url_parser, dict):
            url_parser = LogsCustomPipelineProcessorUrlParser(**url_parser)
        if isinstance(user_agent_parser, dict):
            user_agent_parser = LogsCustomPipelineProcessorUserAgentParser(**user_agent_parser)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessor.__init__)
            check_type(argname="argument arithmetic_processor", value=arithmetic_processor, expected_type=type_hints["arithmetic_processor"])
            check_type(argname="argument attribute_remapper", value=attribute_remapper, expected_type=type_hints["attribute_remapper"])
            check_type(argname="argument category_processor", value=category_processor, expected_type=type_hints["category_processor"])
            check_type(argname="argument date_remapper", value=date_remapper, expected_type=type_hints["date_remapper"])
            check_type(argname="argument geo_ip_parser", value=geo_ip_parser, expected_type=type_hints["geo_ip_parser"])
            check_type(argname="argument grok_parser", value=grok_parser, expected_type=type_hints["grok_parser"])
            check_type(argname="argument lookup_processor", value=lookup_processor, expected_type=type_hints["lookup_processor"])
            check_type(argname="argument message_remapper", value=message_remapper, expected_type=type_hints["message_remapper"])
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
            check_type(argname="argument service_remapper", value=service_remapper, expected_type=type_hints["service_remapper"])
            check_type(argname="argument status_remapper", value=status_remapper, expected_type=type_hints["status_remapper"])
            check_type(argname="argument string_builder_processor", value=string_builder_processor, expected_type=type_hints["string_builder_processor"])
            check_type(argname="argument trace_id_remapper", value=trace_id_remapper, expected_type=type_hints["trace_id_remapper"])
            check_type(argname="argument url_parser", value=url_parser, expected_type=type_hints["url_parser"])
            check_type(argname="argument user_agent_parser", value=user_agent_parser, expected_type=type_hints["user_agent_parser"])
        self._values: typing.Dict[str, typing.Any] = {}
        if arithmetic_processor is not None:
            self._values["arithmetic_processor"] = arithmetic_processor
        if attribute_remapper is not None:
            self._values["attribute_remapper"] = attribute_remapper
        if category_processor is not None:
            self._values["category_processor"] = category_processor
        if date_remapper is not None:
            self._values["date_remapper"] = date_remapper
        if geo_ip_parser is not None:
            self._values["geo_ip_parser"] = geo_ip_parser
        if grok_parser is not None:
            self._values["grok_parser"] = grok_parser
        if lookup_processor is not None:
            self._values["lookup_processor"] = lookup_processor
        if message_remapper is not None:
            self._values["message_remapper"] = message_remapper
        if pipeline is not None:
            self._values["pipeline"] = pipeline
        if service_remapper is not None:
            self._values["service_remapper"] = service_remapper
        if status_remapper is not None:
            self._values["status_remapper"] = status_remapper
        if string_builder_processor is not None:
            self._values["string_builder_processor"] = string_builder_processor
        if trace_id_remapper is not None:
            self._values["trace_id_remapper"] = trace_id_remapper
        if url_parser is not None:
            self._values["url_parser"] = url_parser
        if user_agent_parser is not None:
            self._values["user_agent_parser"] = user_agent_parser

    @builtins.property
    def arithmetic_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorArithmeticProcessor"]:
        '''arithmetic_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#arithmetic_processor LogsCustomPipeline#arithmetic_processor}
        '''
        result = self._values.get("arithmetic_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorArithmeticProcessor"], result)

    @builtins.property
    def attribute_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorAttributeRemapper"]:
        '''attribute_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#attribute_remapper LogsCustomPipeline#attribute_remapper}
        '''
        result = self._values.get("attribute_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorAttributeRemapper"], result)

    @builtins.property
    def category_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorCategoryProcessor"]:
        '''category_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category_processor LogsCustomPipeline#category_processor}
        '''
        result = self._values.get("category_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorCategoryProcessor"], result)

    @builtins.property
    def date_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorDateRemapper"]:
        '''date_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#date_remapper LogsCustomPipeline#date_remapper}
        '''
        result = self._values.get("date_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorDateRemapper"], result)

    @builtins.property
    def geo_ip_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorGeoIpParser"]:
        '''geo_ip_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#geo_ip_parser LogsCustomPipeline#geo_ip_parser}
        '''
        result = self._values.get("geo_ip_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorGeoIpParser"], result)

    @builtins.property
    def grok_parser(self) -> typing.Optional["LogsCustomPipelineProcessorGrokParser"]:
        '''grok_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok_parser LogsCustomPipeline#grok_parser}
        '''
        result = self._values.get("grok_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorGrokParser"], result)

    @builtins.property
    def lookup_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorLookupProcessor"]:
        '''lookup_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_processor LogsCustomPipeline#lookup_processor}
        '''
        result = self._values.get("lookup_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorLookupProcessor"], result)

    @builtins.property
    def message_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorMessageRemapper"]:
        '''message_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#message_remapper LogsCustomPipeline#message_remapper}
        '''
        result = self._values.get("message_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorMessageRemapper"], result)

    @builtins.property
    def pipeline(self) -> typing.Optional["LogsCustomPipelineProcessorPipeline"]:
        '''pipeline block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#pipeline LogsCustomPipeline#pipeline}
        '''
        result = self._values.get("pipeline")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipeline"], result)

    @builtins.property
    def service_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorServiceRemapper"]:
        '''service_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#service_remapper LogsCustomPipeline#service_remapper}
        '''
        result = self._values.get("service_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorServiceRemapper"], result)

    @builtins.property
    def status_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorStatusRemapper"]:
        '''status_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#status_remapper LogsCustomPipeline#status_remapper}
        '''
        result = self._values.get("status_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorStatusRemapper"], result)

    @builtins.property
    def string_builder_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorStringBuilderProcessor"]:
        '''string_builder_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#string_builder_processor LogsCustomPipeline#string_builder_processor}
        '''
        result = self._values.get("string_builder_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorStringBuilderProcessor"], result)

    @builtins.property
    def trace_id_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorTraceIdRemapper"]:
        '''trace_id_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#trace_id_remapper LogsCustomPipeline#trace_id_remapper}
        '''
        result = self._values.get("trace_id_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorTraceIdRemapper"], result)

    @builtins.property
    def url_parser(self) -> typing.Optional["LogsCustomPipelineProcessorUrlParser"]:
        '''url_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#url_parser LogsCustomPipeline#url_parser}
        '''
        result = self._values.get("url_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorUrlParser"], result)

    @builtins.property
    def user_agent_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorUserAgentParser"]:
        '''user_agent_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#user_agent_parser LogsCustomPipeline#user_agent_parser}
        '''
        result = self._values.get("user_agent_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorUserAgentParser"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorArithmeticProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "target": "target",
        "is_enabled": "isEnabled",
        "is_replace_missing": "isReplaceMissing",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorArithmeticProcessor:
    def __init__(
        self,
        *,
        expression: builtins.str,
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Arithmetic operation between one or more log attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        :param target: Name of the attribute that contains the result of the arithmetic operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: Boolean value to enable your pipeline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: Your pipeline name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorArithmeticProcessor.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_replace_missing", value=is_replace_missing, expected_type=type_hints["is_replace_missing"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_replace_missing is not None:
            self._values["is_replace_missing"] = is_replace_missing
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def expression(self) -> builtins.str:
        '''Arithmetic operation between one or more log attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the attribute that contains the result of the arithmetic operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean value to enable your pipeline.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_replace_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        '''
        result = self._values.get("is_replace_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Your pipeline name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorArithmeticProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorArithmeticProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorArithmeticProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorArithmeticProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsReplaceMissing")
    def reset_is_replace_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsReplaceMissing", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissingInput")
    def is_replace_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isReplaceMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissing")
    def is_replace_missing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isReplaceMissing"))

    @is_replace_missing.setter
    def is_replace_missing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "is_replace_missing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isReplaceMissing", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorArithmeticProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorArithmeticProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorArithmeticProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorAttributeRemapper",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "source_type": "sourceType",
        "target": "target",
        "target_type": "targetType",
        "is_enabled": "isEnabled",
        "name": "name",
        "override_on_conflict": "overrideOnConflict",
        "preserve_source": "preserveSource",
        "target_format": "targetFormat",
    },
)
class LogsCustomPipelineProcessorAttributeRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        source_type: builtins.str,
        target: builtins.str,
        target_type: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        override_on_conflict: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preserve_source: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes or tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param source_type: Defines where the sources are from (log ``attribute`` or ``tag``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        :param target: Final attribute or tag name to remap the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param target_type: Defines if the target is a log ``attribute`` or ``tag``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param override_on_conflict: Override the target element if already set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        :param preserve_source: Remove or preserve the remapped source element. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        :param target_format: If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorAttributeRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument override_on_conflict", value=override_on_conflict, expected_type=type_hints["override_on_conflict"])
            check_type(argname="argument preserve_source", value=preserve_source, expected_type=type_hints["preserve_source"])
            check_type(argname="argument target_format", value=target_format, expected_type=type_hints["target_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "source_type": source_type,
            "target": target,
            "target_type": target_type,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if override_on_conflict is not None:
            self._values["override_on_conflict"] = override_on_conflict
        if preserve_source is not None:
            self._values["preserve_source"] = preserve_source
        if target_format is not None:
            self._values["target_format"] = target_format

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes or tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source_type(self) -> builtins.str:
        '''Defines where the sources are from (log ``attribute`` or ``tag``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        '''
        result = self._values.get("source_type")
        assert result is not None, "Required property 'source_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Final attribute or tag name to remap the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''Defines if the target is a log ``attribute`` or ``tag``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_on_conflict(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Override the target element if already set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        '''
        result = self._values.get("override_on_conflict")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preserve_source(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Remove or preserve the remapped source element.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        '''
        result = self._values.get("preserve_source")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def target_format(self) -> typing.Optional[builtins.str]:
        '''If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type.

        If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        result = self._values.get("target_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorAttributeRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorAttributeRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorAttributeRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorAttributeRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverrideOnConflict")
    def reset_override_on_conflict(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideOnConflict", []))

    @jsii.member(jsii_name="resetPreserveSource")
    def reset_preserve_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveSource", []))

    @jsii.member(jsii_name="resetTargetFormat")
    def reset_target_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFormat", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideOnConflictInput")
    def override_on_conflict_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideOnConflictInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveSourceInput")
    def preserve_source_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFormatInput")
    def target_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overrideOnConflict")
    def override_on_conflict(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overrideOnConflict"))

    @override_on_conflict.setter
    def override_on_conflict(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "override_on_conflict").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideOnConflict", value)

    @builtins.property
    @jsii.member(jsii_name="preserveSource")
    def preserve_source(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveSource"))

    @preserve_source.setter
    def preserve_source(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "preserve_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveSource", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="targetFormat")
    def target_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFormat"))

    @target_format.setter
    def target_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "target_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFormat", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "target_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorAttributeRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorAttributeRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorAttributeRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorAttributeRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "category": "category",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorCategoryProcessor:
    def __init__(
        self,
        *,
        category: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorCategoryProcessorCategory", typing.Dict[str, typing.Any]]]],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param category: category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        :param target: Name of the target attribute whose value is defined by the matching category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessor.__init__)
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "category": category,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def category(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorCategoryProcessorCategory"]]:
        '''category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        '''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorCategoryProcessorCategory"]], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the target attribute whose value is defined by the matching category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorCategoryProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorCategory",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter", "name": "name"},
)
class LogsCustomPipelineProcessorCategoryProcessorCategory:
    def __init__(
        self,
        *,
        filter: typing.Union["LogsCustomPipelineProcessorCategoryProcessorCategoryFilter", typing.Dict[str, typing.Any]],
        name: builtins.str,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        '''
        if isinstance(filter, dict):
            filter = LogsCustomPipelineProcessorCategoryProcessorCategoryFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategory.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "name": name,
        }

    @builtins.property
    def filter(self) -> "LogsCustomPipelineProcessorCategoryProcessorCategoryFilter":
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast("LogsCustomPipelineProcessorCategoryProcessorCategoryFilter", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorCategoryProcessorCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorCategoryFilter",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class LogsCustomPipelineProcessorCategoryProcessorCategoryFilter:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategoryFilter.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''Filter criteria of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorCategoryProcessorCategoryFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorCategoryProcessorCategoryFilter]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorCategoryProcessorCategoryFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorCategoryProcessorCategoryFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorCategoryProcessorCategoryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorCategoryList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategoryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategoryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorCategoryProcessorCategory]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorCategoryProcessorCategory]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorCategoryProcessorCategory]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilter")
    def put_filter(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        value = LogsCustomPipelineProcessorCategoryProcessorCategoryFilter(query=query)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(
        self,
    ) -> LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference:
        return typing.cast(LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorCategoryProcessorCategoryFilter]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorCategoryProcessorCategoryFilter], jsii.get(self, "filterInput"))

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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorCategoryProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorCategoryProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCategory")
    def put_category(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogsCustomPipelineProcessorCategoryProcessorCategory, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorCategoryProcessorOutputReference.put_category)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCategory", [value]))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> LogsCustomPipelineProcessorCategoryProcessorCategoryList:
        return typing.cast(LogsCustomPipelineProcessorCategoryProcessorCategoryList, jsii.get(self, "category"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorCategoryProcessorCategory]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorCategoryProcessorCategory]]], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorCategoryProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorCategoryProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorCategoryProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorCategoryProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorDateRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorDateRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorDateRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorDateRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorDateRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorDateRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorDateRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorDateRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorDateRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorDateRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorDateRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorDateRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorDateRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorDateRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGeoIpParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorGeoIpParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGeoIpParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorGeoIpParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorGeoIpParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGeoIpParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGeoIpParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGeoIpParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGeoIpParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGeoIpParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGeoIpParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsCustomPipelineProcessorGeoIpParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGeoIpParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorGeoIpParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGeoIpParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGrokParser",
    jsii_struct_bases=[],
    name_mapping={
        "grok": "grok",
        "source": "source",
        "is_enabled": "isEnabled",
        "name": "name",
        "samples": "samples",
    },
)
class LogsCustomPipelineProcessorGrokParser:
    def __init__(
        self,
        *,
        grok: typing.Union["LogsCustomPipelineProcessorGrokParserGrok", typing.Dict[str, typing.Any]],
        source: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        samples: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param grok: grok block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        :param source: Name of the log attribute to parse. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param samples: List of sample logs for this parser. It can save up to 5 samples. Each sample takes up to 5000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        if isinstance(grok, dict):
            grok = LogsCustomPipelineProcessorGrokParserGrok(**grok)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGrokParser.__init__)
            check_type(argname="argument grok", value=grok, expected_type=type_hints["grok"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument samples", value=samples, expected_type=type_hints["samples"])
        self._values: typing.Dict[str, typing.Any] = {
            "grok": grok,
            "source": source,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if samples is not None:
            self._values["samples"] = samples

    @builtins.property
    def grok(self) -> "LogsCustomPipelineProcessorGrokParserGrok":
        '''grok block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        '''
        result = self._values.get("grok")
        assert result is not None, "Required property 'grok' is missing"
        return typing.cast("LogsCustomPipelineProcessorGrokParserGrok", result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Name of the log attribute to parse.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def samples(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of sample logs for this parser.

        It can save up to 5 samples. Each sample takes up to 5000 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        result = self._values.get("samples")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorGrokParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGrokParserGrok",
    jsii_struct_bases=[],
    name_mapping={"match_rules": "matchRules", "support_rules": "supportRules"},
)
class LogsCustomPipelineProcessorGrokParserGrok:
    def __init__(
        self,
        *,
        match_rules: builtins.str,
        support_rules: builtins.str,
    ) -> None:
        '''
        :param match_rules: Match rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        :param support_rules: Support rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGrokParserGrok.__init__)
            check_type(argname="argument match_rules", value=match_rules, expected_type=type_hints["match_rules"])
            check_type(argname="argument support_rules", value=support_rules, expected_type=type_hints["support_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_rules": match_rules,
            "support_rules": support_rules,
        }

    @builtins.property
    def match_rules(self) -> builtins.str:
        '''Match rules for your grok parser.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        '''
        result = self._values.get("match_rules")
        assert result is not None, "Required property 'match_rules' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def support_rules(self) -> builtins.str:
        '''Support rules for your grok parser.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        result = self._values.get("support_rules")
        assert result is not None, "Required property 'support_rules' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorGrokParserGrok(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorGrokParserGrokOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGrokParserGrokOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGrokParserGrokOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="supportRulesInput")
    def support_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchRules"))

    @match_rules.setter
    def match_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserGrokOutputReference, "match_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchRules", value)

    @builtins.property
    @jsii.member(jsii_name="supportRules")
    def support_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportRules"))

    @support_rules.setter
    def support_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserGrokOutputReference, "support_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportRules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorGrokParserGrok]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGrokParserGrok], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorGrokParserGrok],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserGrokOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorGrokParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorGrokParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorGrokParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrok")
    def put_grok(
        self,
        *,
        match_rules: builtins.str,
        support_rules: builtins.str,
    ) -> None:
        '''
        :param match_rules: Match rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        :param support_rules: Support rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        value = LogsCustomPipelineProcessorGrokParserGrok(
            match_rules=match_rules, support_rules=support_rules
        )

        return typing.cast(None, jsii.invoke(self, "putGrok", [value]))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSamples")
    def reset_samples(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamples", []))

    @builtins.property
    @jsii.member(jsii_name="grok")
    def grok(self) -> LogsCustomPipelineProcessorGrokParserGrokOutputReference:
        return typing.cast(LogsCustomPipelineProcessorGrokParserGrokOutputReference, jsii.get(self, "grok"))

    @builtins.property
    @jsii.member(jsii_name="grokInput")
    def grok_input(self) -> typing.Optional[LogsCustomPipelineProcessorGrokParserGrok]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGrokParserGrok], jsii.get(self, "grokInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="samplesInput")
    def samples_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "samplesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="samples")
    def samples(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "samples"))

    @samples.setter
    def samples(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserOutputReference, "samples").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samples", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsCustomPipelineProcessorGrokParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGrokParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorGrokParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorGrokParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LogsCustomPipelineProcessorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineProcessorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessor]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorLookupProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "lookup_table": "lookupTable",
        "source": "source",
        "target": "target",
        "default_lookup": "defaultLookup",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorLookupProcessor:
    def __init__(
        self,
        *,
        lookup_table: typing.Sequence[builtins.str],
        source: builtins.str,
        target: builtins.str,
        default_lookup: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lookup_table: List of entries of the lookup table using ``key,value`` format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        :param source: Name of the source attribute used to do the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param target: Name of the attribute that contains the result of the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param default_lookup: Default lookup value to use if there is no entry in the lookup table for the value of the source attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorLookupProcessor.__init__)
            check_type(argname="argument lookup_table", value=lookup_table, expected_type=type_hints["lookup_table"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument default_lookup", value=default_lookup, expected_type=type_hints["default_lookup"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "lookup_table": lookup_table,
            "source": source,
            "target": target,
        }
        if default_lookup is not None:
            self._values["default_lookup"] = default_lookup
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def lookup_table(self) -> typing.List[builtins.str]:
        '''List of entries of the lookup table using ``key,value`` format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        '''
        result = self._values.get("lookup_table")
        assert result is not None, "Required property 'lookup_table' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Name of the source attribute used to do the lookup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the attribute that contains the result of the lookup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_lookup(self) -> typing.Optional[builtins.str]:
        '''Default lookup value to use if there is no entry in the lookup table for the value of the source attribute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        '''
        result = self._values.get("default_lookup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorLookupProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorLookupProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorLookupProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorLookupProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultLookup")
    def reset_default_lookup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLookup", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="defaultLookupInput")
    def default_lookup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLookupInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="lookupTableInput")
    def lookup_table_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lookupTableInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLookup")
    def default_lookup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLookup"))

    @default_lookup.setter
    def default_lookup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "default_lookup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLookup", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="lookupTable")
    def lookup_table(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lookupTable"))

    @lookup_table.setter
    def lookup_table(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "lookup_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lookupTable", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorLookupProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorLookupProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorLookupProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorLookupProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorMessageRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorMessageRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorMessageRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorMessageRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorMessageRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorMessageRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorMessageRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorMessageRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorMessageRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorMessageRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorMessageRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorMessageRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorMessageRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorMessageRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putArithmeticProcessor")
    def put_arithmetic_processor(
        self,
        *,
        expression: builtins.str,
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Arithmetic operation between one or more log attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        :param target: Name of the attribute that contains the result of the arithmetic operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: Boolean value to enable your pipeline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: Your pipeline name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorArithmeticProcessor(
            expression=expression,
            target=target,
            is_enabled=is_enabled,
            is_replace_missing=is_replace_missing,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putArithmeticProcessor", [value]))

    @jsii.member(jsii_name="putAttributeRemapper")
    def put_attribute_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        source_type: builtins.str,
        target: builtins.str,
        target_type: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        override_on_conflict: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preserve_source: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes or tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param source_type: Defines where the sources are from (log ``attribute`` or ``tag``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        :param target: Final attribute or tag name to remap the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param target_type: Defines if the target is a log ``attribute`` or ``tag``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param override_on_conflict: Override the target element if already set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        :param preserve_source: Remove or preserve the remapped source element. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        :param target_format: If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        value = LogsCustomPipelineProcessorAttributeRemapper(
            sources=sources,
            source_type=source_type,
            target=target,
            target_type=target_type,
            is_enabled=is_enabled,
            name=name,
            override_on_conflict=override_on_conflict,
            preserve_source=preserve_source,
            target_format=target_format,
        )

        return typing.cast(None, jsii.invoke(self, "putAttributeRemapper", [value]))

    @jsii.member(jsii_name="putCategoryProcessor")
    def put_category_processor(
        self,
        *,
        category: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogsCustomPipelineProcessorCategoryProcessorCategory, typing.Dict[str, typing.Any]]]],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param category: category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        :param target: Name of the target attribute whose value is defined by the matching category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorCategoryProcessor(
            category=category, target=target, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putCategoryProcessor", [value]))

    @jsii.member(jsii_name="putDateRemapper")
    def put_date_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorDateRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putDateRemapper", [value]))

    @jsii.member(jsii_name="putGeoIpParser")
    def put_geo_ip_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorGeoIpParser(
            sources=sources, target=target, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putGeoIpParser", [value]))

    @jsii.member(jsii_name="putGrokParser")
    def put_grok_parser(
        self,
        *,
        grok: typing.Union[LogsCustomPipelineProcessorGrokParserGrok, typing.Dict[str, typing.Any]],
        source: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        samples: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param grok: grok block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        :param source: Name of the log attribute to parse. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param samples: List of sample logs for this parser. It can save up to 5 samples. Each sample takes up to 5000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        value = LogsCustomPipelineProcessorGrokParser(
            grok=grok, source=source, is_enabled=is_enabled, name=name, samples=samples
        )

        return typing.cast(None, jsii.invoke(self, "putGrokParser", [value]))

    @jsii.member(jsii_name="putLookupProcessor")
    def put_lookup_processor(
        self,
        *,
        lookup_table: typing.Sequence[builtins.str],
        source: builtins.str,
        target: builtins.str,
        default_lookup: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lookup_table: List of entries of the lookup table using ``key,value`` format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        :param source: Name of the source attribute used to do the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param target: Name of the attribute that contains the result of the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param default_lookup: Default lookup value to use if there is no entry in the lookup table for the value of the source attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorLookupProcessor(
            lookup_table=lookup_table,
            source=source,
            target=target,
            default_lookup=default_lookup,
            is_enabled=is_enabled,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putLookupProcessor", [value]))

    @jsii.member(jsii_name="putMessageRemapper")
    def put_message_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorMessageRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMessageRemapper", [value]))

    @jsii.member(jsii_name="putPipeline")
    def put_pipeline(
        self,
        *,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineFilter", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processor: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineProcessor", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.
        :param processor: processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        '''
        value = LogsCustomPipelineProcessorPipeline(
            filter=filter, name=name, is_enabled=is_enabled, processor=processor
        )

        return typing.cast(None, jsii.invoke(self, "putPipeline", [value]))

    @jsii.member(jsii_name="putServiceRemapper")
    def put_service_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorServiceRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRemapper", [value]))

    @jsii.member(jsii_name="putStatusRemapper")
    def put_status_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorStatusRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putStatusRemapper", [value]))

    @jsii.member(jsii_name="putStringBuilderProcessor")
    def put_string_builder_processor(
        self,
        *,
        target: builtins.str,
        template: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The name of the attribute that contains the result of the template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param template: The formula with one or more attributes and raw text. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If it replaces all missing attributes of template by an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: The name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorStringBuilderProcessor(
            target=target,
            template=template,
            is_enabled=is_enabled,
            is_replace_missing=is_replace_missing,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putStringBuilderProcessor", [value]))

    @jsii.member(jsii_name="putTraceIdRemapper")
    def put_trace_id_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorTraceIdRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTraceIdRemapper", [value]))

    @jsii.member(jsii_name="putUrlParser")
    def put_url_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        normalize_ending_slashes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param normalize_ending_slashes: Normalize the ending slashes or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        value = LogsCustomPipelineProcessorUrlParser(
            sources=sources,
            target=target,
            is_enabled=is_enabled,
            name=name,
            normalize_ending_slashes=normalize_ending_slashes,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlParser", [value]))

    @jsii.member(jsii_name="putUserAgentParser")
    def put_user_agent_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_encoded: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_encoded: If the source attribute is URL encoded or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorUserAgentParser(
            sources=sources,
            target=target,
            is_enabled=is_enabled,
            is_encoded=is_encoded,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putUserAgentParser", [value]))

    @jsii.member(jsii_name="resetArithmeticProcessor")
    def reset_arithmetic_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArithmeticProcessor", []))

    @jsii.member(jsii_name="resetAttributeRemapper")
    def reset_attribute_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeRemapper", []))

    @jsii.member(jsii_name="resetCategoryProcessor")
    def reset_category_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryProcessor", []))

    @jsii.member(jsii_name="resetDateRemapper")
    def reset_date_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateRemapper", []))

    @jsii.member(jsii_name="resetGeoIpParser")
    def reset_geo_ip_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoIpParser", []))

    @jsii.member(jsii_name="resetGrokParser")
    def reset_grok_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrokParser", []))

    @jsii.member(jsii_name="resetLookupProcessor")
    def reset_lookup_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookupProcessor", []))

    @jsii.member(jsii_name="resetMessageRemapper")
    def reset_message_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageRemapper", []))

    @jsii.member(jsii_name="resetPipeline")
    def reset_pipeline(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipeline", []))

    @jsii.member(jsii_name="resetServiceRemapper")
    def reset_service_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRemapper", []))

    @jsii.member(jsii_name="resetStatusRemapper")
    def reset_status_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusRemapper", []))

    @jsii.member(jsii_name="resetStringBuilderProcessor")
    def reset_string_builder_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringBuilderProcessor", []))

    @jsii.member(jsii_name="resetTraceIdRemapper")
    def reset_trace_id_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceIdRemapper", []))

    @jsii.member(jsii_name="resetUrlParser")
    def reset_url_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlParser", []))

    @jsii.member(jsii_name="resetUserAgentParser")
    def reset_user_agent_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgentParser", []))

    @builtins.property
    @jsii.member(jsii_name="arithmeticProcessor")
    def arithmetic_processor(
        self,
    ) -> LogsCustomPipelineProcessorArithmeticProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorArithmeticProcessorOutputReference, jsii.get(self, "arithmeticProcessor"))

    @builtins.property
    @jsii.member(jsii_name="attributeRemapper")
    def attribute_remapper(
        self,
    ) -> LogsCustomPipelineProcessorAttributeRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorAttributeRemapperOutputReference, jsii.get(self, "attributeRemapper"))

    @builtins.property
    @jsii.member(jsii_name="categoryProcessor")
    def category_processor(
        self,
    ) -> LogsCustomPipelineProcessorCategoryProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorCategoryProcessorOutputReference, jsii.get(self, "categoryProcessor"))

    @builtins.property
    @jsii.member(jsii_name="dateRemapper")
    def date_remapper(self) -> LogsCustomPipelineProcessorDateRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorDateRemapperOutputReference, jsii.get(self, "dateRemapper"))

    @builtins.property
    @jsii.member(jsii_name="geoIpParser")
    def geo_ip_parser(self) -> LogsCustomPipelineProcessorGeoIpParserOutputReference:
        return typing.cast(LogsCustomPipelineProcessorGeoIpParserOutputReference, jsii.get(self, "geoIpParser"))

    @builtins.property
    @jsii.member(jsii_name="grokParser")
    def grok_parser(self) -> LogsCustomPipelineProcessorGrokParserOutputReference:
        return typing.cast(LogsCustomPipelineProcessorGrokParserOutputReference, jsii.get(self, "grokParser"))

    @builtins.property
    @jsii.member(jsii_name="lookupProcessor")
    def lookup_processor(
        self,
    ) -> LogsCustomPipelineProcessorLookupProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorLookupProcessorOutputReference, jsii.get(self, "lookupProcessor"))

    @builtins.property
    @jsii.member(jsii_name="messageRemapper")
    def message_remapper(
        self,
    ) -> LogsCustomPipelineProcessorMessageRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorMessageRemapperOutputReference, jsii.get(self, "messageRemapper"))

    @builtins.property
    @jsii.member(jsii_name="pipeline")
    def pipeline(self) -> "LogsCustomPipelineProcessorPipelineOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineOutputReference", jsii.get(self, "pipeline"))

    @builtins.property
    @jsii.member(jsii_name="serviceRemapper")
    def service_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorServiceRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorServiceRemapperOutputReference", jsii.get(self, "serviceRemapper"))

    @builtins.property
    @jsii.member(jsii_name="statusRemapper")
    def status_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorStatusRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorStatusRemapperOutputReference", jsii.get(self, "statusRemapper"))

    @builtins.property
    @jsii.member(jsii_name="stringBuilderProcessor")
    def string_builder_processor(
        self,
    ) -> "LogsCustomPipelineProcessorStringBuilderProcessorOutputReference":
        return typing.cast("LogsCustomPipelineProcessorStringBuilderProcessorOutputReference", jsii.get(self, "stringBuilderProcessor"))

    @builtins.property
    @jsii.member(jsii_name="traceIdRemapper")
    def trace_id_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorTraceIdRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorTraceIdRemapperOutputReference", jsii.get(self, "traceIdRemapper"))

    @builtins.property
    @jsii.member(jsii_name="urlParser")
    def url_parser(self) -> "LogsCustomPipelineProcessorUrlParserOutputReference":
        return typing.cast("LogsCustomPipelineProcessorUrlParserOutputReference", jsii.get(self, "urlParser"))

    @builtins.property
    @jsii.member(jsii_name="userAgentParser")
    def user_agent_parser(
        self,
    ) -> "LogsCustomPipelineProcessorUserAgentParserOutputReference":
        return typing.cast("LogsCustomPipelineProcessorUserAgentParserOutputReference", jsii.get(self, "userAgentParser"))

    @builtins.property
    @jsii.member(jsii_name="arithmeticProcessorInput")
    def arithmetic_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorArithmeticProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorArithmeticProcessor], jsii.get(self, "arithmeticProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeRemapperInput")
    def attribute_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorAttributeRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorAttributeRemapper], jsii.get(self, "attributeRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryProcessorInput")
    def category_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorCategoryProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorCategoryProcessor], jsii.get(self, "categoryProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="dateRemapperInput")
    def date_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorDateRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorDateRemapper], jsii.get(self, "dateRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="geoIpParserInput")
    def geo_ip_parser_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorGeoIpParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGeoIpParser], jsii.get(self, "geoIpParserInput"))

    @builtins.property
    @jsii.member(jsii_name="grokParserInput")
    def grok_parser_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorGrokParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorGrokParser], jsii.get(self, "grokParserInput"))

    @builtins.property
    @jsii.member(jsii_name="lookupProcessorInput")
    def lookup_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorLookupProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorLookupProcessor], jsii.get(self, "lookupProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="messageRemapperInput")
    def message_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorMessageRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorMessageRemapper], jsii.get(self, "messageRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineInput")
    def pipeline_input(self) -> typing.Optional["LogsCustomPipelineProcessorPipeline"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipeline"], jsii.get(self, "pipelineInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRemapperInput")
    def service_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorServiceRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorServiceRemapper"], jsii.get(self, "serviceRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="statusRemapperInput")
    def status_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorStatusRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorStatusRemapper"], jsii.get(self, "statusRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="stringBuilderProcessorInput")
    def string_builder_processor_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorStringBuilderProcessor"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorStringBuilderProcessor"], jsii.get(self, "stringBuilderProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="traceIdRemapperInput")
    def trace_id_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorTraceIdRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorTraceIdRemapper"], jsii.get(self, "traceIdRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="urlParserInput")
    def url_parser_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorUrlParser"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorUrlParser"], jsii.get(self, "urlParserInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentParserInput")
    def user_agent_parser_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorUserAgentParser"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorUserAgentParser"], jsii.get(self, "userAgentParserInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineProcessor, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineProcessor, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineProcessor, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipeline",
    jsii_struct_bases=[],
    name_mapping={
        "filter": "filter",
        "name": "name",
        "is_enabled": "isEnabled",
        "processor": "processor",
    },
)
class LogsCustomPipelineProcessorPipeline:
    def __init__(
        self,
        *,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineFilter", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processor: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineProcessor", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.
        :param processor: processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipeline.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "name": name,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if processor is not None:
            self._values["processor"] = processor

    @builtins.property
    def filter(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineFilter"]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineFilter"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processor(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessor"]]]:
        '''processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#processor LogsCustomPipeline#processor}
        '''
        result = self._values.get("processor")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessor"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipeline(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineFilter",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class LogsCustomPipelineProcessorPipelineFilter:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineFilter.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''Filter criteria of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineFilterList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogsCustomPipelineProcessorPipelineFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineProcessorPipelineFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineFilterOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogsCustomPipelineProcessorPipelineFilter, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineOutputReference.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putProcessor")
    def put_processor(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineProcessor", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineOutputReference.put_processor)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessor", [value]))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetProcessor")
    def reset_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessor", []))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> LogsCustomPipelineProcessorPipelineFilterList:
        return typing.cast(LogsCustomPipelineProcessorPipelineFilterList, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="processor")
    def processor(self) -> "LogsCustomPipelineProcessorPipelineProcessorList":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorList", jsii.get(self, "processor"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineFilter]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="processorInput")
    def processor_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessor"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessor"]]], jsii.get(self, "processorInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsCustomPipelineProcessorPipeline]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipeline], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipeline],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "arithmetic_processor": "arithmeticProcessor",
        "attribute_remapper": "attributeRemapper",
        "category_processor": "categoryProcessor",
        "date_remapper": "dateRemapper",
        "geo_ip_parser": "geoIpParser",
        "grok_parser": "grokParser",
        "lookup_processor": "lookupProcessor",
        "message_remapper": "messageRemapper",
        "service_remapper": "serviceRemapper",
        "status_remapper": "statusRemapper",
        "string_builder_processor": "stringBuilderProcessor",
        "trace_id_remapper": "traceIdRemapper",
        "url_parser": "urlParser",
        "user_agent_parser": "userAgentParser",
    },
)
class LogsCustomPipelineProcessorPipelineProcessor:
    def __init__(
        self,
        *,
        arithmetic_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor", typing.Dict[str, typing.Any]]] = None,
        attribute_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper", typing.Dict[str, typing.Any]]] = None,
        category_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor", typing.Dict[str, typing.Any]]] = None,
        date_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorDateRemapper", typing.Dict[str, typing.Any]]] = None,
        geo_ip_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorGeoIpParser", typing.Dict[str, typing.Any]]] = None,
        grok_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorGrokParser", typing.Dict[str, typing.Any]]] = None,
        lookup_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorLookupProcessor", typing.Dict[str, typing.Any]]] = None,
        message_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorMessageRemapper", typing.Dict[str, typing.Any]]] = None,
        service_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorServiceRemapper", typing.Dict[str, typing.Any]]] = None,
        status_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorStatusRemapper", typing.Dict[str, typing.Any]]] = None,
        string_builder_processor: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor", typing.Dict[str, typing.Any]]] = None,
        trace_id_remapper: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper", typing.Dict[str, typing.Any]]] = None,
        url_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorUrlParser", typing.Dict[str, typing.Any]]] = None,
        user_agent_parser: typing.Optional[typing.Union["LogsCustomPipelineProcessorPipelineProcessorUserAgentParser", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param arithmetic_processor: arithmetic_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#arithmetic_processor LogsCustomPipeline#arithmetic_processor}
        :param attribute_remapper: attribute_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#attribute_remapper LogsCustomPipeline#attribute_remapper}
        :param category_processor: category_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category_processor LogsCustomPipeline#category_processor}
        :param date_remapper: date_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#date_remapper LogsCustomPipeline#date_remapper}
        :param geo_ip_parser: geo_ip_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#geo_ip_parser LogsCustomPipeline#geo_ip_parser}
        :param grok_parser: grok_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok_parser LogsCustomPipeline#grok_parser}
        :param lookup_processor: lookup_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_processor LogsCustomPipeline#lookup_processor}
        :param message_remapper: message_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#message_remapper LogsCustomPipeline#message_remapper}
        :param service_remapper: service_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#service_remapper LogsCustomPipeline#service_remapper}
        :param status_remapper: status_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#status_remapper LogsCustomPipeline#status_remapper}
        :param string_builder_processor: string_builder_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#string_builder_processor LogsCustomPipeline#string_builder_processor}
        :param trace_id_remapper: trace_id_remapper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#trace_id_remapper LogsCustomPipeline#trace_id_remapper}
        :param url_parser: url_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#url_parser LogsCustomPipeline#url_parser}
        :param user_agent_parser: user_agent_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#user_agent_parser LogsCustomPipeline#user_agent_parser}
        '''
        if isinstance(arithmetic_processor, dict):
            arithmetic_processor = LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor(**arithmetic_processor)
        if isinstance(attribute_remapper, dict):
            attribute_remapper = LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper(**attribute_remapper)
        if isinstance(category_processor, dict):
            category_processor = LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor(**category_processor)
        if isinstance(date_remapper, dict):
            date_remapper = LogsCustomPipelineProcessorPipelineProcessorDateRemapper(**date_remapper)
        if isinstance(geo_ip_parser, dict):
            geo_ip_parser = LogsCustomPipelineProcessorPipelineProcessorGeoIpParser(**geo_ip_parser)
        if isinstance(grok_parser, dict):
            grok_parser = LogsCustomPipelineProcessorPipelineProcessorGrokParser(**grok_parser)
        if isinstance(lookup_processor, dict):
            lookup_processor = LogsCustomPipelineProcessorPipelineProcessorLookupProcessor(**lookup_processor)
        if isinstance(message_remapper, dict):
            message_remapper = LogsCustomPipelineProcessorPipelineProcessorMessageRemapper(**message_remapper)
        if isinstance(service_remapper, dict):
            service_remapper = LogsCustomPipelineProcessorPipelineProcessorServiceRemapper(**service_remapper)
        if isinstance(status_remapper, dict):
            status_remapper = LogsCustomPipelineProcessorPipelineProcessorStatusRemapper(**status_remapper)
        if isinstance(string_builder_processor, dict):
            string_builder_processor = LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor(**string_builder_processor)
        if isinstance(trace_id_remapper, dict):
            trace_id_remapper = LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper(**trace_id_remapper)
        if isinstance(url_parser, dict):
            url_parser = LogsCustomPipelineProcessorPipelineProcessorUrlParser(**url_parser)
        if isinstance(user_agent_parser, dict):
            user_agent_parser = LogsCustomPipelineProcessorPipelineProcessorUserAgentParser(**user_agent_parser)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessor.__init__)
            check_type(argname="argument arithmetic_processor", value=arithmetic_processor, expected_type=type_hints["arithmetic_processor"])
            check_type(argname="argument attribute_remapper", value=attribute_remapper, expected_type=type_hints["attribute_remapper"])
            check_type(argname="argument category_processor", value=category_processor, expected_type=type_hints["category_processor"])
            check_type(argname="argument date_remapper", value=date_remapper, expected_type=type_hints["date_remapper"])
            check_type(argname="argument geo_ip_parser", value=geo_ip_parser, expected_type=type_hints["geo_ip_parser"])
            check_type(argname="argument grok_parser", value=grok_parser, expected_type=type_hints["grok_parser"])
            check_type(argname="argument lookup_processor", value=lookup_processor, expected_type=type_hints["lookup_processor"])
            check_type(argname="argument message_remapper", value=message_remapper, expected_type=type_hints["message_remapper"])
            check_type(argname="argument service_remapper", value=service_remapper, expected_type=type_hints["service_remapper"])
            check_type(argname="argument status_remapper", value=status_remapper, expected_type=type_hints["status_remapper"])
            check_type(argname="argument string_builder_processor", value=string_builder_processor, expected_type=type_hints["string_builder_processor"])
            check_type(argname="argument trace_id_remapper", value=trace_id_remapper, expected_type=type_hints["trace_id_remapper"])
            check_type(argname="argument url_parser", value=url_parser, expected_type=type_hints["url_parser"])
            check_type(argname="argument user_agent_parser", value=user_agent_parser, expected_type=type_hints["user_agent_parser"])
        self._values: typing.Dict[str, typing.Any] = {}
        if arithmetic_processor is not None:
            self._values["arithmetic_processor"] = arithmetic_processor
        if attribute_remapper is not None:
            self._values["attribute_remapper"] = attribute_remapper
        if category_processor is not None:
            self._values["category_processor"] = category_processor
        if date_remapper is not None:
            self._values["date_remapper"] = date_remapper
        if geo_ip_parser is not None:
            self._values["geo_ip_parser"] = geo_ip_parser
        if grok_parser is not None:
            self._values["grok_parser"] = grok_parser
        if lookup_processor is not None:
            self._values["lookup_processor"] = lookup_processor
        if message_remapper is not None:
            self._values["message_remapper"] = message_remapper
        if service_remapper is not None:
            self._values["service_remapper"] = service_remapper
        if status_remapper is not None:
            self._values["status_remapper"] = status_remapper
        if string_builder_processor is not None:
            self._values["string_builder_processor"] = string_builder_processor
        if trace_id_remapper is not None:
            self._values["trace_id_remapper"] = trace_id_remapper
        if url_parser is not None:
            self._values["url_parser"] = url_parser
        if user_agent_parser is not None:
            self._values["user_agent_parser"] = user_agent_parser

    @builtins.property
    def arithmetic_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor"]:
        '''arithmetic_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#arithmetic_processor LogsCustomPipeline#arithmetic_processor}
        '''
        result = self._values.get("arithmetic_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor"], result)

    @builtins.property
    def attribute_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper"]:
        '''attribute_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#attribute_remapper LogsCustomPipeline#attribute_remapper}
        '''
        result = self._values.get("attribute_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper"], result)

    @builtins.property
    def category_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor"]:
        '''category_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category_processor LogsCustomPipeline#category_processor}
        '''
        result = self._values.get("category_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor"], result)

    @builtins.property
    def date_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorDateRemapper"]:
        '''date_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#date_remapper LogsCustomPipeline#date_remapper}
        '''
        result = self._values.get("date_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorDateRemapper"], result)

    @builtins.property
    def geo_ip_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorGeoIpParser"]:
        '''geo_ip_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#geo_ip_parser LogsCustomPipeline#geo_ip_parser}
        '''
        result = self._values.get("geo_ip_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorGeoIpParser"], result)

    @builtins.property
    def grok_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorGrokParser"]:
        '''grok_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok_parser LogsCustomPipeline#grok_parser}
        '''
        result = self._values.get("grok_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorGrokParser"], result)

    @builtins.property
    def lookup_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorLookupProcessor"]:
        '''lookup_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_processor LogsCustomPipeline#lookup_processor}
        '''
        result = self._values.get("lookup_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorLookupProcessor"], result)

    @builtins.property
    def message_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorMessageRemapper"]:
        '''message_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#message_remapper LogsCustomPipeline#message_remapper}
        '''
        result = self._values.get("message_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorMessageRemapper"], result)

    @builtins.property
    def service_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorServiceRemapper"]:
        '''service_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#service_remapper LogsCustomPipeline#service_remapper}
        '''
        result = self._values.get("service_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorServiceRemapper"], result)

    @builtins.property
    def status_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStatusRemapper"]:
        '''status_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#status_remapper LogsCustomPipeline#status_remapper}
        '''
        result = self._values.get("status_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStatusRemapper"], result)

    @builtins.property
    def string_builder_processor(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor"]:
        '''string_builder_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#string_builder_processor LogsCustomPipeline#string_builder_processor}
        '''
        result = self._values.get("string_builder_processor")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor"], result)

    @builtins.property
    def trace_id_remapper(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper"]:
        '''trace_id_remapper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#trace_id_remapper LogsCustomPipeline#trace_id_remapper}
        '''
        result = self._values.get("trace_id_remapper")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper"], result)

    @builtins.property
    def url_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUrlParser"]:
        '''url_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#url_parser LogsCustomPipeline#url_parser}
        '''
        result = self._values.get("url_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUrlParser"], result)

    @builtins.property
    def user_agent_parser(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUserAgentParser"]:
        '''user_agent_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#user_agent_parser LogsCustomPipeline#user_agent_parser}
        '''
        result = self._values.get("user_agent_parser")
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUserAgentParser"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "target": "target",
        "is_enabled": "isEnabled",
        "is_replace_missing": "isReplaceMissing",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor:
    def __init__(
        self,
        *,
        expression: builtins.str,
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Arithmetic operation between one or more log attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        :param target: Name of the attribute that contains the result of the arithmetic operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: Boolean value to enable your pipeline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: Your pipeline name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_replace_missing", value=is_replace_missing, expected_type=type_hints["is_replace_missing"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_replace_missing is not None:
            self._values["is_replace_missing"] = is_replace_missing
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def expression(self) -> builtins.str:
        '''Arithmetic operation between one or more log attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the attribute that contains the result of the arithmetic operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean value to enable your pipeline.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_replace_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        '''
        result = self._values.get("is_replace_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Your pipeline name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsReplaceMissing")
    def reset_is_replace_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsReplaceMissing", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissingInput")
    def is_replace_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isReplaceMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissing")
    def is_replace_missing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isReplaceMissing"))

    @is_replace_missing.setter
    def is_replace_missing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "is_replace_missing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isReplaceMissing", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "source_type": "sourceType",
        "target": "target",
        "target_type": "targetType",
        "is_enabled": "isEnabled",
        "name": "name",
        "override_on_conflict": "overrideOnConflict",
        "preserve_source": "preserveSource",
        "target_format": "targetFormat",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        source_type: builtins.str,
        target: builtins.str,
        target_type: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        override_on_conflict: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preserve_source: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes or tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param source_type: Defines where the sources are from (log ``attribute`` or ``tag``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        :param target: Final attribute or tag name to remap the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param target_type: Defines if the target is a log ``attribute`` or ``tag``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param override_on_conflict: Override the target element if already set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        :param preserve_source: Remove or preserve the remapped source element. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        :param target_format: If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument override_on_conflict", value=override_on_conflict, expected_type=type_hints["override_on_conflict"])
            check_type(argname="argument preserve_source", value=preserve_source, expected_type=type_hints["preserve_source"])
            check_type(argname="argument target_format", value=target_format, expected_type=type_hints["target_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "source_type": source_type,
            "target": target,
            "target_type": target_type,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if override_on_conflict is not None:
            self._values["override_on_conflict"] = override_on_conflict
        if preserve_source is not None:
            self._values["preserve_source"] = preserve_source
        if target_format is not None:
            self._values["target_format"] = target_format

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes or tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source_type(self) -> builtins.str:
        '''Defines where the sources are from (log ``attribute`` or ``tag``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        '''
        result = self._values.get("source_type")
        assert result is not None, "Required property 'source_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Final attribute or tag name to remap the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''Defines if the target is a log ``attribute`` or ``tag``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_on_conflict(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Override the target element if already set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        '''
        result = self._values.get("override_on_conflict")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preserve_source(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Remove or preserve the remapped source element.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        '''
        result = self._values.get("preserve_source")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def target_format(self) -> typing.Optional[builtins.str]:
        '''If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type.

        If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        result = self._values.get("target_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverrideOnConflict")
    def reset_override_on_conflict(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideOnConflict", []))

    @jsii.member(jsii_name="resetPreserveSource")
    def reset_preserve_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveSource", []))

    @jsii.member(jsii_name="resetTargetFormat")
    def reset_target_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFormat", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideOnConflictInput")
    def override_on_conflict_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideOnConflictInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveSourceInput")
    def preserve_source_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFormatInput")
    def target_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overrideOnConflict")
    def override_on_conflict(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overrideOnConflict"))

    @override_on_conflict.setter
    def override_on_conflict(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "override_on_conflict").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideOnConflict", value)

    @builtins.property
    @jsii.member(jsii_name="preserveSource")
    def preserve_source(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveSource"))

    @preserve_source.setter
    def preserve_source(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "preserve_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveSource", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="targetFormat")
    def target_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFormat"))

    @target_format.setter
    def target_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "target_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFormat", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "target_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "category": "category",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor:
    def __init__(
        self,
        *,
        category: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory", typing.Dict[str, typing.Any]]]],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param category: category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        :param target: Name of the target attribute whose value is defined by the matching category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor.__init__)
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "category": category,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def category(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory"]]:
        '''category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        '''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory"]], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the target attribute whose value is defined by the matching category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory:
    def __init__(
        self,
        *,
        filter: typing.Union["LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter", typing.Dict[str, typing.Any]],
        name: builtins.str,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.
        '''
        if isinstance(filter, dict):
            filter = LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "name": name,
        }

    @builtins.property
    def filter(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter":
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#filter LogsCustomPipeline#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''Filter criteria of the category.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilter")
    def put_filter(self, *, query: builtins.str) -> None:
        '''
        :param query: Filter criteria of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#query LogsCustomPipeline#query}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter(
            query=query
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter], jsii.get(self, "filterInput"))

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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCategory")
    def put_category(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference.put_category)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCategory", [value]))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList, jsii.get(self, "category"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory]]], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorDateRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorDateRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorDateRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorDateRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorDateRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorDateRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorDateRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGeoIpParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorGeoIpParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGeoIpParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorGeoIpParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGeoIpParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGeoIpParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGeoIpParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGrokParser",
    jsii_struct_bases=[],
    name_mapping={
        "grok": "grok",
        "source": "source",
        "is_enabled": "isEnabled",
        "name": "name",
        "samples": "samples",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorGrokParser:
    def __init__(
        self,
        *,
        grok: typing.Union["LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok", typing.Dict[str, typing.Any]],
        source: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        samples: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param grok: grok block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        :param source: Name of the log attribute to parse. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param samples: List of sample logs for this parser. It can save up to 5 samples. Each sample takes up to 5000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        if isinstance(grok, dict):
            grok = LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok(**grok)
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGrokParser.__init__)
            check_type(argname="argument grok", value=grok, expected_type=type_hints["grok"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument samples", value=samples, expected_type=type_hints["samples"])
        self._values: typing.Dict[str, typing.Any] = {
            "grok": grok,
            "source": source,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if samples is not None:
            self._values["samples"] = samples

    @builtins.property
    def grok(self) -> "LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok":
        '''grok block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        '''
        result = self._values.get("grok")
        assert result is not None, "Required property 'grok' is missing"
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok", result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Name of the log attribute to parse.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def samples(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of sample logs for this parser.

        It can save up to 5 samples. Each sample takes up to 5000 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        result = self._values.get("samples")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorGrokParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok",
    jsii_struct_bases=[],
    name_mapping={"match_rules": "matchRules", "support_rules": "supportRules"},
)
class LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok:
    def __init__(
        self,
        *,
        match_rules: builtins.str,
        support_rules: builtins.str,
    ) -> None:
        '''
        :param match_rules: Match rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        :param support_rules: Support rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok.__init__)
            check_type(argname="argument match_rules", value=match_rules, expected_type=type_hints["match_rules"])
            check_type(argname="argument support_rules", value=support_rules, expected_type=type_hints["support_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_rules": match_rules,
            "support_rules": support_rules,
        }

    @builtins.property
    def match_rules(self) -> builtins.str:
        '''Match rules for your grok parser.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        '''
        result = self._values.get("match_rules")
        assert result is not None, "Required property 'match_rules' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def support_rules(self) -> builtins.str:
        '''Support rules for your grok parser.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        result = self._values.get("support_rules")
        assert result is not None, "Required property 'support_rules' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="supportRulesInput")
    def support_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchRules"))

    @match_rules.setter
    def match_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference, "match_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchRules", value)

    @builtins.property
    @jsii.member(jsii_name="supportRules")
    def support_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportRules"))

    @support_rules.setter
    def support_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference, "support_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportRules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrok")
    def put_grok(
        self,
        *,
        match_rules: builtins.str,
        support_rules: builtins.str,
    ) -> None:
        '''
        :param match_rules: Match rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#match_rules LogsCustomPipeline#match_rules}
        :param support_rules: Support rules for your grok parser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#support_rules LogsCustomPipeline#support_rules}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok(
            match_rules=match_rules, support_rules=support_rules
        )

        return typing.cast(None, jsii.invoke(self, "putGrok", [value]))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSamples")
    def reset_samples(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamples", []))

    @builtins.property
    @jsii.member(jsii_name="grok")
    def grok(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference, jsii.get(self, "grok"))

    @builtins.property
    @jsii.member(jsii_name="grokInput")
    def grok_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok], jsii.get(self, "grokInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="samplesInput")
    def samples_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "samplesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="samples")
    def samples(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "samples"))

    @samples.setter
    def samples(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, "samples").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samples", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorList",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessor]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogsCustomPipelineProcessorPipelineProcessor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorLookupProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "lookup_table": "lookupTable",
        "source": "source",
        "target": "target",
        "default_lookup": "defaultLookup",
        "is_enabled": "isEnabled",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorLookupProcessor:
    def __init__(
        self,
        *,
        lookup_table: typing.Sequence[builtins.str],
        source: builtins.str,
        target: builtins.str,
        default_lookup: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lookup_table: List of entries of the lookup table using ``key,value`` format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        :param source: Name of the source attribute used to do the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param target: Name of the attribute that contains the result of the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param default_lookup: Default lookup value to use if there is no entry in the lookup table for the value of the source attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorLookupProcessor.__init__)
            check_type(argname="argument lookup_table", value=lookup_table, expected_type=type_hints["lookup_table"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument default_lookup", value=default_lookup, expected_type=type_hints["default_lookup"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "lookup_table": lookup_table,
            "source": source,
            "target": target,
        }
        if default_lookup is not None:
            self._values["default_lookup"] = default_lookup
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def lookup_table(self) -> typing.List[builtins.str]:
        '''List of entries of the lookup table using ``key,value`` format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        '''
        result = self._values.get("lookup_table")
        assert result is not None, "Required property 'lookup_table' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Name of the source attribute used to do the lookup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the attribute that contains the result of the lookup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_lookup(self) -> typing.Optional[builtins.str]:
        '''Default lookup value to use if there is no entry in the lookup table for the value of the source attribute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        '''
        result = self._values.get("default_lookup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorLookupProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultLookup")
    def reset_default_lookup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLookup", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="defaultLookupInput")
    def default_lookup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLookupInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="lookupTableInput")
    def lookup_table_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lookupTableInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLookup")
    def default_lookup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLookup"))

    @default_lookup.setter
    def default_lookup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "default_lookup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLookup", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="lookupTable")
    def lookup_table(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lookupTable"))

    @lookup_table.setter
    def lookup_table(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "lookup_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lookupTable", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorLookupProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorLookupProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorLookupProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorMessageRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorMessageRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorMessageRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorMessageRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorMessageRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorMessageRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorMessageRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogsCustomPipelineProcessorPipelineProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putArithmeticProcessor")
    def put_arithmetic_processor(
        self,
        *,
        expression: builtins.str,
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Arithmetic operation between one or more log attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#expression LogsCustomPipeline#expression}
        :param target: Name of the attribute that contains the result of the arithmetic operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: Boolean value to enable your pipeline. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If true, it replaces all missing attributes of expression by 0, false skips the operation if an attribute is missing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: Your pipeline name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor(
            expression=expression,
            target=target,
            is_enabled=is_enabled,
            is_replace_missing=is_replace_missing,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putArithmeticProcessor", [value]))

    @jsii.member(jsii_name="putAttributeRemapper")
    def put_attribute_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        source_type: builtins.str,
        target: builtins.str,
        target_type: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        override_on_conflict: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preserve_source: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes or tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param source_type: Defines where the sources are from (log ``attribute`` or ``tag``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source_type LogsCustomPipeline#source_type}
        :param target: Final attribute or tag name to remap the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param target_type: Defines if the target is a log ``attribute`` or ``tag``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_type LogsCustomPipeline#target_type}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param override_on_conflict: Override the target element if already set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#override_on_conflict LogsCustomPipeline#override_on_conflict}
        :param preserve_source: Remove or preserve the remapped source element. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#preserve_source LogsCustomPipeline#preserve_source}
        :param target_format: If the ``target_type`` of the remapper is ``attribute``, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. ``string``, ``integer``, or ``double`` are the possible types. If the ``target_type`` is ``tag``, this parameter may not be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target_format LogsCustomPipeline#target_format}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper(
            sources=sources,
            source_type=source_type,
            target=target,
            target_type=target_type,
            is_enabled=is_enabled,
            name=name,
            override_on_conflict=override_on_conflict,
            preserve_source=preserve_source,
            target_format=target_format,
        )

        return typing.cast(None, jsii.invoke(self, "putAttributeRemapper", [value]))

    @jsii.member(jsii_name="putCategoryProcessor")
    def put_category_processor(
        self,
        *,
        category: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory, typing.Dict[str, typing.Any]]]],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param category: category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#category LogsCustomPipeline#category}
        :param target: Name of the target attribute whose value is defined by the matching category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the category. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor(
            category=category, target=target, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putCategoryProcessor", [value]))

    @jsii.member(jsii_name="putDateRemapper")
    def put_date_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorDateRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putDateRemapper", [value]))

    @jsii.member(jsii_name="putGeoIpParser")
    def put_geo_ip_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorGeoIpParser(
            sources=sources, target=target, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putGeoIpParser", [value]))

    @jsii.member(jsii_name="putGrokParser")
    def put_grok_parser(
        self,
        *,
        grok: typing.Union[LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok, typing.Dict[str, typing.Any]],
        source: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        samples: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param grok: grok block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#grok LogsCustomPipeline#grok}
        :param source: Name of the log attribute to parse. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param samples: List of sample logs for this parser. It can save up to 5 samples. Each sample takes up to 5000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#samples LogsCustomPipeline#samples}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorGrokParser(
            grok=grok, source=source, is_enabled=is_enabled, name=name, samples=samples
        )

        return typing.cast(None, jsii.invoke(self, "putGrokParser", [value]))

    @jsii.member(jsii_name="putLookupProcessor")
    def put_lookup_processor(
        self,
        *,
        lookup_table: typing.Sequence[builtins.str],
        source: builtins.str,
        target: builtins.str,
        default_lookup: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lookup_table: List of entries of the lookup table using ``key,value`` format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#lookup_table LogsCustomPipeline#lookup_table}
        :param source: Name of the source attribute used to do the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#source LogsCustomPipeline#source}
        :param target: Name of the attribute that contains the result of the lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param default_lookup: Default lookup value to use if there is no entry in the lookup table for the value of the source attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#default_lookup LogsCustomPipeline#default_lookup}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorLookupProcessor(
            lookup_table=lookup_table,
            source=source,
            target=target,
            default_lookup=default_lookup,
            is_enabled=is_enabled,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putLookupProcessor", [value]))

    @jsii.member(jsii_name="putMessageRemapper")
    def put_message_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorMessageRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMessageRemapper", [value]))

    @jsii.member(jsii_name="putServiceRemapper")
    def put_service_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorServiceRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRemapper", [value]))

    @jsii.member(jsii_name="putStatusRemapper")
    def put_status_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorStatusRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putStatusRemapper", [value]))

    @jsii.member(jsii_name="putStringBuilderProcessor")
    def put_string_builder_processor(
        self,
        *,
        target: builtins.str,
        template: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The name of the attribute that contains the result of the template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param template: The formula with one or more attributes and raw text. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If it replaces all missing attributes of template by an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: The name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor(
            target=target,
            template=template,
            is_enabled=is_enabled,
            is_replace_missing=is_replace_missing,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putStringBuilderProcessor", [value]))

    @jsii.member(jsii_name="putTraceIdRemapper")
    def put_trace_id_remapper(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper(
            sources=sources, is_enabled=is_enabled, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTraceIdRemapper", [value]))

    @jsii.member(jsii_name="putUrlParser")
    def put_url_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        normalize_ending_slashes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param normalize_ending_slashes: Normalize the ending slashes or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorUrlParser(
            sources=sources,
            target=target,
            is_enabled=is_enabled,
            name=name,
            normalize_ending_slashes=normalize_ending_slashes,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlParser", [value]))

    @jsii.member(jsii_name="putUserAgentParser")
    def put_user_agent_parser(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_encoded: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_encoded: If the source attribute is URL encoded or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        value = LogsCustomPipelineProcessorPipelineProcessorUserAgentParser(
            sources=sources,
            target=target,
            is_enabled=is_enabled,
            is_encoded=is_encoded,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putUserAgentParser", [value]))

    @jsii.member(jsii_name="resetArithmeticProcessor")
    def reset_arithmetic_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArithmeticProcessor", []))

    @jsii.member(jsii_name="resetAttributeRemapper")
    def reset_attribute_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeRemapper", []))

    @jsii.member(jsii_name="resetCategoryProcessor")
    def reset_category_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryProcessor", []))

    @jsii.member(jsii_name="resetDateRemapper")
    def reset_date_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateRemapper", []))

    @jsii.member(jsii_name="resetGeoIpParser")
    def reset_geo_ip_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoIpParser", []))

    @jsii.member(jsii_name="resetGrokParser")
    def reset_grok_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrokParser", []))

    @jsii.member(jsii_name="resetLookupProcessor")
    def reset_lookup_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookupProcessor", []))

    @jsii.member(jsii_name="resetMessageRemapper")
    def reset_message_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageRemapper", []))

    @jsii.member(jsii_name="resetServiceRemapper")
    def reset_service_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRemapper", []))

    @jsii.member(jsii_name="resetStatusRemapper")
    def reset_status_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusRemapper", []))

    @jsii.member(jsii_name="resetStringBuilderProcessor")
    def reset_string_builder_processor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringBuilderProcessor", []))

    @jsii.member(jsii_name="resetTraceIdRemapper")
    def reset_trace_id_remapper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceIdRemapper", []))

    @jsii.member(jsii_name="resetUrlParser")
    def reset_url_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlParser", []))

    @jsii.member(jsii_name="resetUserAgentParser")
    def reset_user_agent_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgentParser", []))

    @builtins.property
    @jsii.member(jsii_name="arithmeticProcessor")
    def arithmetic_processor(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference, jsii.get(self, "arithmeticProcessor"))

    @builtins.property
    @jsii.member(jsii_name="attributeRemapper")
    def attribute_remapper(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference, jsii.get(self, "attributeRemapper"))

    @builtins.property
    @jsii.member(jsii_name="categoryProcessor")
    def category_processor(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference, jsii.get(self, "categoryProcessor"))

    @builtins.property
    @jsii.member(jsii_name="dateRemapper")
    def date_remapper(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference, jsii.get(self, "dateRemapper"))

    @builtins.property
    @jsii.member(jsii_name="geoIpParser")
    def geo_ip_parser(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference, jsii.get(self, "geoIpParser"))

    @builtins.property
    @jsii.member(jsii_name="grokParser")
    def grok_parser(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference, jsii.get(self, "grokParser"))

    @builtins.property
    @jsii.member(jsii_name="lookupProcessor")
    def lookup_processor(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference, jsii.get(self, "lookupProcessor"))

    @builtins.property
    @jsii.member(jsii_name="messageRemapper")
    def message_remapper(
        self,
    ) -> LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference:
        return typing.cast(LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference, jsii.get(self, "messageRemapper"))

    @builtins.property
    @jsii.member(jsii_name="serviceRemapper")
    def service_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference", jsii.get(self, "serviceRemapper"))

    @builtins.property
    @jsii.member(jsii_name="statusRemapper")
    def status_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference", jsii.get(self, "statusRemapper"))

    @builtins.property
    @jsii.member(jsii_name="stringBuilderProcessor")
    def string_builder_processor(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference", jsii.get(self, "stringBuilderProcessor"))

    @builtins.property
    @jsii.member(jsii_name="traceIdRemapper")
    def trace_id_remapper(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference", jsii.get(self, "traceIdRemapper"))

    @builtins.property
    @jsii.member(jsii_name="urlParser")
    def url_parser(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference", jsii.get(self, "urlParser"))

    @builtins.property
    @jsii.member(jsii_name="userAgentParser")
    def user_agent_parser(
        self,
    ) -> "LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference":
        return typing.cast("LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference", jsii.get(self, "userAgentParser"))

    @builtins.property
    @jsii.member(jsii_name="arithmeticProcessorInput")
    def arithmetic_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor], jsii.get(self, "arithmeticProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeRemapperInput")
    def attribute_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper], jsii.get(self, "attributeRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryProcessorInput")
    def category_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor], jsii.get(self, "categoryProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="dateRemapperInput")
    def date_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorDateRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorDateRemapper], jsii.get(self, "dateRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="geoIpParserInput")
    def geo_ip_parser_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGeoIpParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGeoIpParser], jsii.get(self, "geoIpParserInput"))

    @builtins.property
    @jsii.member(jsii_name="grokParserInput")
    def grok_parser_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorGrokParser], jsii.get(self, "grokParserInput"))

    @builtins.property
    @jsii.member(jsii_name="lookupProcessorInput")
    def lookup_processor_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorLookupProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorLookupProcessor], jsii.get(self, "lookupProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="messageRemapperInput")
    def message_remapper_input(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorMessageRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorMessageRemapper], jsii.get(self, "messageRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRemapperInput")
    def service_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorServiceRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorServiceRemapper"], jsii.get(self, "serviceRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="statusRemapperInput")
    def status_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStatusRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStatusRemapper"], jsii.get(self, "statusRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="stringBuilderProcessorInput")
    def string_builder_processor_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor"], jsii.get(self, "stringBuilderProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="traceIdRemapperInput")
    def trace_id_remapper_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper"], jsii.get(self, "traceIdRemapperInput"))

    @builtins.property
    @jsii.member(jsii_name="urlParserInput")
    def url_parser_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUrlParser"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUrlParser"], jsii.get(self, "urlParserInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentParserInput")
    def user_agent_parser_input(
        self,
    ) -> typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUserAgentParser"]:
        return typing.cast(typing.Optional["LogsCustomPipelineProcessorPipelineProcessorUserAgentParser"], jsii.get(self, "userAgentParserInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessor, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessor, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogsCustomPipelineProcessorPipelineProcessor, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorServiceRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorServiceRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorServiceRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorServiceRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorServiceRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorServiceRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorServiceRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorStatusRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorStatusRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorStatusRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorStatusRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStatusRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStatusRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStatusRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "template": "template",
        "is_enabled": "isEnabled",
        "is_replace_missing": "isReplaceMissing",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor:
    def __init__(
        self,
        *,
        target: builtins.str,
        template: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The name of the attribute that contains the result of the template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param template: The formula with one or more attributes and raw text. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If it replaces all missing attributes of template by an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: The name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_replace_missing", value=is_replace_missing, expected_type=type_hints["is_replace_missing"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
            "template": template,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_replace_missing is not None:
            self._values["is_replace_missing"] = is_replace_missing
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def target(self) -> builtins.str:
        '''The name of the attribute that contains the result of the template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> builtins.str:
        '''The formula with one or more attributes and raw text.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        '''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_replace_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If it replaces all missing attributes of template by an empty string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        '''
        result = self._values.get("is_replace_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsReplaceMissing")
    def reset_is_replace_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsReplaceMissing", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissingInput")
    def is_replace_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isReplaceMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissing")
    def is_replace_missing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isReplaceMissing"))

    @is_replace_missing.setter
    def is_replace_missing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "is_replace_missing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isReplaceMissing", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorUrlParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
        "normalize_ending_slashes": "normalizeEndingSlashes",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorUrlParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        normalize_ending_slashes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param normalize_ending_slashes: Normalize the ending slashes or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorUrlParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument normalize_ending_slashes", value=normalize_ending_slashes, expected_type=type_hints["normalize_ending_slashes"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if normalize_ending_slashes is not None:
            self._values["normalize_ending_slashes"] = normalize_ending_slashes

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def normalize_ending_slashes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Normalize the ending slashes or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        result = self._values.get("normalize_ending_slashes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorUrlParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNormalizeEndingSlashes")
    def reset_normalize_ending_slashes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNormalizeEndingSlashes", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="normalizeEndingSlashesInput")
    def normalize_ending_slashes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "normalizeEndingSlashesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="normalizeEndingSlashes")
    def normalize_ending_slashes(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "normalizeEndingSlashes"))

    @normalize_ending_slashes.setter
    def normalize_ending_slashes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "normalize_ending_slashes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "normalizeEndingSlashes", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUrlParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUrlParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUrlParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorUserAgentParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "is_encoded": "isEncoded",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorPipelineProcessorUserAgentParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_encoded: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_encoded: If the source attribute is URL encoded or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorUserAgentParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_encoded", value=is_encoded, expected_type=type_hints["is_encoded"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_encoded is not None:
            self._values["is_encoded"] = is_encoded
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_encoded(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the source attribute is URL encoded or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        '''
        result = self._values.get("is_encoded")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorPipelineProcessorUserAgentParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsEncoded")
    def reset_is_encoded(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEncoded", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isEncodedInput")
    def is_encoded_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEncodedInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isEncoded")
    def is_encoded(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEncoded"))

    @is_encoded.setter
    def is_encoded(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "is_encoded").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEncoded", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUserAgentParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUserAgentParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorPipelineProcessorUserAgentParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorServiceRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorServiceRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorServiceRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorServiceRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorServiceRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorServiceRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorServiceRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorServiceRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorServiceRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorServiceRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorServiceRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorServiceRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorServiceRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorServiceRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorStatusRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorStatusRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorStatusRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorStatusRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorStatusRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorStatusRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorStatusRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStatusRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStatusRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStatusRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorStatusRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorStatusRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorStatusRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStatusRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorStringBuilderProcessor",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "template": "template",
        "is_enabled": "isEnabled",
        "is_replace_missing": "isReplaceMissing",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorStringBuilderProcessor:
    def __init__(
        self,
        *,
        target: builtins.str,
        template: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_replace_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The name of the attribute that contains the result of the template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param template: The formula with one or more attributes and raw text. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_replace_missing: If it replaces all missing attributes of template by an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        :param name: The name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorStringBuilderProcessor.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_replace_missing", value=is_replace_missing, expected_type=type_hints["is_replace_missing"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
            "template": template,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_replace_missing is not None:
            self._values["is_replace_missing"] = is_replace_missing
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def target(self) -> builtins.str:
        '''The name of the attribute that contains the result of the template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> builtins.str:
        '''The formula with one or more attributes and raw text.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#template LogsCustomPipeline#template}
        '''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_replace_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If it replaces all missing attributes of template by an empty string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_replace_missing LogsCustomPipeline#is_replace_missing}
        '''
        result = self._values.get("is_replace_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorStringBuilderProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorStringBuilderProcessorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorStringBuilderProcessorOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsReplaceMissing")
    def reset_is_replace_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsReplaceMissing", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissingInput")
    def is_replace_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isReplaceMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isReplaceMissing")
    def is_replace_missing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isReplaceMissing"))

    @is_replace_missing.setter
    def is_replace_missing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "is_replace_missing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isReplaceMissing", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorStringBuilderProcessor]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorStringBuilderProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorStringBuilderProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorStringBuilderProcessorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorTraceIdRemapper",
    jsii_struct_bases=[],
    name_mapping={"sources": "sources", "is_enabled": "isEnabled", "name": "name"},
)
class LogsCustomPipelineProcessorTraceIdRemapper:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorTraceIdRemapper.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorTraceIdRemapper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorTraceIdRemapperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorTraceIdRemapperOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorTraceIdRemapperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorTraceIdRemapperOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorTraceIdRemapperOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorTraceIdRemapperOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorTraceIdRemapper]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorTraceIdRemapper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorTraceIdRemapper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorTraceIdRemapperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorUrlParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "name": "name",
        "normalize_ending_slashes": "normalizeEndingSlashes",
    },
)
class LogsCustomPipelineProcessorUrlParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        normalize_ending_slashes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        :param normalize_ending_slashes: Normalize the ending slashes or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorUrlParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument normalize_ending_slashes", value=normalize_ending_slashes, expected_type=type_hints["normalize_ending_slashes"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if normalize_ending_slashes is not None:
            self._values["normalize_ending_slashes"] = normalize_ending_slashes

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def normalize_ending_slashes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Normalize the ending slashes or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#normalize_ending_slashes LogsCustomPipeline#normalize_ending_slashes}
        '''
        result = self._values.get("normalize_ending_slashes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorUrlParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorUrlParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorUrlParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorUrlParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNormalizeEndingSlashes")
    def reset_normalize_ending_slashes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNormalizeEndingSlashes", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="normalizeEndingSlashesInput")
    def normalize_ending_slashes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "normalizeEndingSlashesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="normalizeEndingSlashes")
    def normalize_ending_slashes(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "normalizeEndingSlashes"))

    @normalize_ending_slashes.setter
    def normalize_ending_slashes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "normalize_ending_slashes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "normalizeEndingSlashes", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogsCustomPipelineProcessorUrlParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorUrlParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorUrlParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUrlParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorUserAgentParser",
    jsii_struct_bases=[],
    name_mapping={
        "sources": "sources",
        "target": "target",
        "is_enabled": "isEnabled",
        "is_encoded": "isEncoded",
        "name": "name",
    },
)
class LogsCustomPipelineProcessorUserAgentParser:
    def __init__(
        self,
        *,
        sources: typing.Sequence[builtins.str],
        target: builtins.str,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_encoded: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sources: List of source attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        :param target: Name of the parent attribute that contains all the extracted details from the sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        :param is_enabled: If the processor is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        :param is_encoded: If the source attribute is URL encoded or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        :param name: Name of the processor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorUserAgentParser.__init__)
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument is_encoded", value=is_encoded, expected_type=type_hints["is_encoded"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "sources": sources,
            "target": target,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if is_encoded is not None:
            self._values["is_encoded"] = is_encoded
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''List of source attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#sources LogsCustomPipeline#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Name of the parent attribute that contains all the extracted details from the sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#target LogsCustomPipeline#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the processor is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_enabled LogsCustomPipeline#is_enabled}
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_encoded(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If the source attribute is URL encoded or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#is_encoded LogsCustomPipeline#is_encoded}
        '''
        result = self._values.get("is_encoded")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the processor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/logs_custom_pipeline#name LogsCustomPipeline#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogsCustomPipelineProcessorUserAgentParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogsCustomPipelineProcessorUserAgentParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.logsCustomPipeline.LogsCustomPipelineProcessorUserAgentParserOutputReference",
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
            type_hints = typing.get_type_hints(LogsCustomPipelineProcessorUserAgentParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetIsEncoded")
    def reset_is_encoded(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEncoded", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isEncodedInput")
    def is_encoded_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEncodedInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isEncoded")
    def is_encoded(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEncoded"))

    @is_encoded.setter
    def is_encoded(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "is_encoded").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEncoded", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogsCustomPipelineProcessorUserAgentParser]:
        return typing.cast(typing.Optional[LogsCustomPipelineProcessorUserAgentParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogsCustomPipelineProcessorUserAgentParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogsCustomPipelineProcessorUserAgentParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogsCustomPipeline",
    "LogsCustomPipelineConfig",
    "LogsCustomPipelineFilter",
    "LogsCustomPipelineFilterList",
    "LogsCustomPipelineFilterOutputReference",
    "LogsCustomPipelineProcessor",
    "LogsCustomPipelineProcessorArithmeticProcessor",
    "LogsCustomPipelineProcessorArithmeticProcessorOutputReference",
    "LogsCustomPipelineProcessorAttributeRemapper",
    "LogsCustomPipelineProcessorAttributeRemapperOutputReference",
    "LogsCustomPipelineProcessorCategoryProcessor",
    "LogsCustomPipelineProcessorCategoryProcessorCategory",
    "LogsCustomPipelineProcessorCategoryProcessorCategoryFilter",
    "LogsCustomPipelineProcessorCategoryProcessorCategoryFilterOutputReference",
    "LogsCustomPipelineProcessorCategoryProcessorCategoryList",
    "LogsCustomPipelineProcessorCategoryProcessorCategoryOutputReference",
    "LogsCustomPipelineProcessorCategoryProcessorOutputReference",
    "LogsCustomPipelineProcessorDateRemapper",
    "LogsCustomPipelineProcessorDateRemapperOutputReference",
    "LogsCustomPipelineProcessorGeoIpParser",
    "LogsCustomPipelineProcessorGeoIpParserOutputReference",
    "LogsCustomPipelineProcessorGrokParser",
    "LogsCustomPipelineProcessorGrokParserGrok",
    "LogsCustomPipelineProcessorGrokParserGrokOutputReference",
    "LogsCustomPipelineProcessorGrokParserOutputReference",
    "LogsCustomPipelineProcessorList",
    "LogsCustomPipelineProcessorLookupProcessor",
    "LogsCustomPipelineProcessorLookupProcessorOutputReference",
    "LogsCustomPipelineProcessorMessageRemapper",
    "LogsCustomPipelineProcessorMessageRemapperOutputReference",
    "LogsCustomPipelineProcessorOutputReference",
    "LogsCustomPipelineProcessorPipeline",
    "LogsCustomPipelineProcessorPipelineFilter",
    "LogsCustomPipelineProcessorPipelineFilterList",
    "LogsCustomPipelineProcessorPipelineFilterOutputReference",
    "LogsCustomPipelineProcessorPipelineOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessor",
    "LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessor",
    "LogsCustomPipelineProcessorPipelineProcessorArithmeticProcessorOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorAttributeRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorAttributeRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessor",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategory",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilter",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryFilterOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryList",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorCategoryOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorCategoryProcessorOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorDateRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorDateRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorGeoIpParser",
    "LogsCustomPipelineProcessorPipelineProcessorGeoIpParserOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorGrokParser",
    "LogsCustomPipelineProcessorPipelineProcessorGrokParserGrok",
    "LogsCustomPipelineProcessorPipelineProcessorGrokParserGrokOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorGrokParserOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorList",
    "LogsCustomPipelineProcessorPipelineProcessorLookupProcessor",
    "LogsCustomPipelineProcessorPipelineProcessorLookupProcessorOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorMessageRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorMessageRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorServiceRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorServiceRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorStatusRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorStatusRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessor",
    "LogsCustomPipelineProcessorPipelineProcessorStringBuilderProcessorOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapper",
    "LogsCustomPipelineProcessorPipelineProcessorTraceIdRemapperOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorUrlParser",
    "LogsCustomPipelineProcessorPipelineProcessorUrlParserOutputReference",
    "LogsCustomPipelineProcessorPipelineProcessorUserAgentParser",
    "LogsCustomPipelineProcessorPipelineProcessorUserAgentParserOutputReference",
    "LogsCustomPipelineProcessorServiceRemapper",
    "LogsCustomPipelineProcessorServiceRemapperOutputReference",
    "LogsCustomPipelineProcessorStatusRemapper",
    "LogsCustomPipelineProcessorStatusRemapperOutputReference",
    "LogsCustomPipelineProcessorStringBuilderProcessor",
    "LogsCustomPipelineProcessorStringBuilderProcessorOutputReference",
    "LogsCustomPipelineProcessorTraceIdRemapper",
    "LogsCustomPipelineProcessorTraceIdRemapperOutputReference",
    "LogsCustomPipelineProcessorUrlParser",
    "LogsCustomPipelineProcessorUrlParserOutputReference",
    "LogsCustomPipelineProcessorUserAgentParser",
    "LogsCustomPipelineProcessorUserAgentParserOutputReference",
]

publication.publish()
