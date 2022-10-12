'''
# `data_consul_catalog_nodes`

Refer to the Terraform Registory for docs: [`data_consul_catalog_nodes`](https://www.terraform.io/docs/providers/consul/d/catalog_nodes).
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


class DataConsulCatalogNodes(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodes",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes consul_catalog_nodes}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        query_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataConsulCatalogNodesQueryOptions", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes consul_catalog_nodes} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#id DataConsulCatalogNodes#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param query_options: query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#query_options DataConsulCatalogNodes#query_options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodes.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataConsulCatalogNodesConfig(
            id=id,
            query_options=query_options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putQueryOptions")
    def put_query_options(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataConsulCatalogNodesQueryOptions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodes.put_query_options)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryOptions", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetQueryOptions")
    def reset_query_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryOptions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @builtins.property
    @jsii.member(jsii_name="nodeIds")
    def node_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeIds"))

    @builtins.property
    @jsii.member(jsii_name="nodeNames")
    def node_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeNames"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> "DataConsulCatalogNodesNodesList":
        return typing.cast("DataConsulCatalogNodesNodesList", jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="queryOptions")
    def query_options(self) -> "DataConsulCatalogNodesQueryOptionsList":
        return typing.cast("DataConsulCatalogNodesQueryOptionsList", jsii.get(self, "queryOptions"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="queryOptionsInput")
    def query_options_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataConsulCatalogNodesQueryOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataConsulCatalogNodesQueryOptions"]]], jsii.get(self, "queryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodes, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "query_options": "queryOptions",
    },
)
class DataConsulCatalogNodesConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        query_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataConsulCatalogNodesQueryOptions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#id DataConsulCatalogNodes#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param query_options: query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#query_options DataConsulCatalogNodes#query_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument query_options", value=query_options, expected_type=type_hints["query_options"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if query_options is not None:
            self._values["query_options"] = query_options

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#id DataConsulCatalogNodes#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_options(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataConsulCatalogNodesQueryOptions"]]]:
        '''query_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#query_options DataConsulCatalogNodes#query_options}
        '''
        result = self._values.get("query_options")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataConsulCatalogNodesQueryOptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulCatalogNodesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesNodes",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataConsulCatalogNodesNodes:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulCatalogNodesNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataConsulCatalogNodesNodesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesNodesList",
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
            type_hints = typing.get_type_hints(DataConsulCatalogNodesNodesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataConsulCatalogNodesNodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodesNodesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataConsulCatalogNodesNodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesNodesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesNodesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesNodesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataConsulCatalogNodesNodesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesNodesOutputReference",
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
            type_hints = typing.get_type_hints(DataConsulCatalogNodesNodesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "meta"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="taggedAddresses")
    def tagged_addresses(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "taggedAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataConsulCatalogNodesNodes]:
        return typing.cast(typing.Optional[DataConsulCatalogNodesNodes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataConsulCatalogNodesNodes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesNodesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesQueryOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allow_stale": "allowStale",
        "datacenter": "datacenter",
        "near": "near",
        "node_meta": "nodeMeta",
        "partition": "partition",
        "require_consistent": "requireConsistent",
        "token": "token",
        "wait_index": "waitIndex",
        "wait_time": "waitTime",
    },
)
class DataConsulCatalogNodesQueryOptions:
    def __init__(
        self,
        *,
        allow_stale: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        near: typing.Optional[builtins.str] = None,
        node_meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        partition: typing.Optional[builtins.str] = None,
        require_consistent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        wait_index: typing.Optional[jsii.Number] = None,
        wait_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_stale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#allow_stale DataConsulCatalogNodes#allow_stale}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#datacenter DataConsulCatalogNodes#datacenter}.
        :param near: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#near DataConsulCatalogNodes#near}.
        :param node_meta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#node_meta DataConsulCatalogNodes#node_meta}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#partition DataConsulCatalogNodes#partition}.
        :param require_consistent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#require_consistent DataConsulCatalogNodes#require_consistent}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#token DataConsulCatalogNodes#token}.
        :param wait_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#wait_index DataConsulCatalogNodes#wait_index}.
        :param wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#wait_time DataConsulCatalogNodes#wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodesQueryOptions.__init__)
            check_type(argname="argument allow_stale", value=allow_stale, expected_type=type_hints["allow_stale"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument near", value=near, expected_type=type_hints["near"])
            check_type(argname="argument node_meta", value=node_meta, expected_type=type_hints["node_meta"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument require_consistent", value=require_consistent, expected_type=type_hints["require_consistent"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument wait_index", value=wait_index, expected_type=type_hints["wait_index"])
            check_type(argname="argument wait_time", value=wait_time, expected_type=type_hints["wait_time"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_stale is not None:
            self._values["allow_stale"] = allow_stale
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if near is not None:
            self._values["near"] = near
        if node_meta is not None:
            self._values["node_meta"] = node_meta
        if partition is not None:
            self._values["partition"] = partition
        if require_consistent is not None:
            self._values["require_consistent"] = require_consistent
        if token is not None:
            self._values["token"] = token
        if wait_index is not None:
            self._values["wait_index"] = wait_index
        if wait_time is not None:
            self._values["wait_time"] = wait_time

    @builtins.property
    def allow_stale(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#allow_stale DataConsulCatalogNodes#allow_stale}.'''
        result = self._values.get("allow_stale")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#datacenter DataConsulCatalogNodes#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def near(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#near DataConsulCatalogNodes#near}.'''
        result = self._values.get("near")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_meta(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#node_meta DataConsulCatalogNodes#node_meta}.'''
        result = self._values.get("node_meta")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#partition DataConsulCatalogNodes#partition}.'''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_consistent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#require_consistent DataConsulCatalogNodes#require_consistent}.'''
        result = self._values.get("require_consistent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#token DataConsulCatalogNodes#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#wait_index DataConsulCatalogNodes#wait_index}.'''
        result = self._values.get("wait_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/catalog_nodes#wait_time DataConsulCatalogNodes#wait_time}.'''
        result = self._values.get("wait_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulCatalogNodesQueryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataConsulCatalogNodesQueryOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesQueryOptionsList",
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
            type_hints = typing.get_type_hints(DataConsulCatalogNodesQueryOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataConsulCatalogNodesQueryOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulCatalogNodesQueryOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataConsulCatalogNodesQueryOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataConsulCatalogNodesQueryOptions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataConsulCatalogNodesQueryOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataConsulCatalogNodesQueryOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataConsulCatalogNodesQueryOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulCatalogNodes.DataConsulCatalogNodesQueryOptionsOutputReference",
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
            type_hints = typing.get_type_hints(DataConsulCatalogNodesQueryOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowStale")
    def reset_allow_stale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowStale", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetNear")
    def reset_near(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNear", []))

    @jsii.member(jsii_name="resetNodeMeta")
    def reset_node_meta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeMeta", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetRequireConsistent")
    def reset_require_consistent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireConsistent", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWaitIndex")
    def reset_wait_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitIndex", []))

    @jsii.member(jsii_name="resetWaitTime")
    def reset_wait_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTime", []))

    @builtins.property
    @jsii.member(jsii_name="allowStaleInput")
    def allow_stale_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowStaleInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="nearInput")
    def near_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nearInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeMetaInput")
    def node_meta_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "nodeMetaInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="requireConsistentInput")
    def require_consistent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireConsistentInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="waitIndexInput")
    def wait_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimeInput")
    def wait_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStale")
    def allow_stale(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowStale"))

    @allow_stale.setter
    def allow_stale(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "allow_stale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowStale", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="near")
    def near(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "near"))

    @near.setter
    def near(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "near").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "near", value)

    @builtins.property
    @jsii.member(jsii_name="nodeMeta")
    def node_meta(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "nodeMeta"))

    @node_meta.setter
    def node_meta(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "node_meta").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeMeta", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="requireConsistent")
    def require_consistent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireConsistent"))

    @require_consistent.setter
    def require_consistent(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "require_consistent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireConsistent", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="waitIndex")
    def wait_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitIndex"))

    @wait_index.setter
    def wait_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "wait_index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitIndex", value)

    @builtins.property
    @jsii.member(jsii_name="waitTime")
    def wait_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitTime"))

    @wait_time.setter
    def wait_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "wait_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataConsulCatalogNodesQueryOptions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataConsulCatalogNodesQueryOptions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataConsulCatalogNodesQueryOptions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataConsulCatalogNodesQueryOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataConsulCatalogNodes",
    "DataConsulCatalogNodesConfig",
    "DataConsulCatalogNodesNodes",
    "DataConsulCatalogNodesNodesList",
    "DataConsulCatalogNodesNodesOutputReference",
    "DataConsulCatalogNodesQueryOptions",
    "DataConsulCatalogNodesQueryOptionsList",
    "DataConsulCatalogNodesQueryOptionsOutputReference",
]

publication.publish()
