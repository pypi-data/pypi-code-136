'''
# `newrelic_workload`

Refer to the Terraform Registory for docs: [`newrelic_workload`](https://www.terraform.io/docs/providers/newrelic/r/workload).
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


class Workload(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.Workload",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/workload newrelic_workload}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/workload newrelic_workload} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The workload's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        :param account_id: The New Relic account ID where you want to create the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        :param entity_guids: A list of entity GUIDs manually assigned to this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        :param entity_search_query: entity_search_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scope_account_ids: A list of account IDs that will be used to get entities from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Workload.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WorkloadConfig(
            name=name,
            account_id=account_id,
            entity_guids=entity_guids,
            entity_search_query=entity_search_query,
            id=id,
            scope_account_ids=scope_account_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEntitySearchQuery")
    def put_entity_search_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Workload.put_entity_search_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntitySearchQuery", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetEntityGuids")
    def reset_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityGuids", []))

    @jsii.member(jsii_name="resetEntitySearchQuery")
    def reset_entity_search_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntitySearchQuery", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScopeAccountIds")
    def reset_scope_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScopeAccountIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="compositeEntitySearchQuery")
    def composite_entity_search_query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compositeEntitySearchQuery"))

    @builtins.property
    @jsii.member(jsii_name="entitySearchQuery")
    def entity_search_query(self) -> "WorkloadEntitySearchQueryList":
        return typing.cast("WorkloadEntitySearchQueryList", jsii.get(self, "entitySearchQuery"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="permalink")
    def permalink(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permalink"))

    @builtins.property
    @jsii.member(jsii_name="workloadId")
    def workload_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workloadId"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="entityGuidsInput")
    def entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="entitySearchQueryInput")
    def entity_search_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]], jsii.get(self, "entitySearchQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeAccountIdsInput")
    def scope_account_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "scopeAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workload, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="entityGuids")
    def entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entityGuids"))

    @entity_guids.setter
    def entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workload, "entity_guids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityGuids", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workload, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workload, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scopeAccountIds")
    def scope_account_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "scopeAccountIds"))

    @scope_account_ids.setter
    def scope_account_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workload, "scope_account_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeAccountIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadConfig",
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
        "account_id": "accountId",
        "entity_guids": "entityGuids",
        "entity_search_query": "entitySearchQuery",
        "id": "id",
        "scope_account_ids": "scopeAccountIds",
    },
)
class WorkloadConfig(cdktf.TerraformMetaArguments):
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
        account_id: typing.Optional[jsii.Number] = None,
        entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The workload's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        :param account_id: The New Relic account ID where you want to create the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        :param entity_guids: A list of entity GUIDs manually assigned to this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        :param entity_search_query: entity_search_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scope_account_ids: A list of account IDs that will be used to get entities from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument entity_guids", value=entity_guids, expected_type=type_hints["entity_guids"])
            check_type(argname="argument entity_search_query", value=entity_search_query, expected_type=type_hints["entity_search_query"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument scope_account_ids", value=scope_account_ids, expected_type=type_hints["scope_account_ids"])
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if entity_guids is not None:
            self._values["entity_guids"] = entity_guids
        if entity_search_query is not None:
            self._values["entity_search_query"] = entity_search_query
        if id is not None:
            self._values["id"] = id
        if scope_account_ids is not None:
            self._values["scope_account_ids"] = scope_account_ids

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
        '''The workload's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The New Relic account ID where you want to create the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of entity GUIDs manually assigned to this workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        '''
        result = self._values.get("entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entity_search_query(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]]:
        '''entity_search_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        '''
        result = self._values.get("entity_search_query")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope_account_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of account IDs that will be used to get entities from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        '''
        result = self._values.get("scope_account_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class WorkloadEntitySearchQuery:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: The query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadEntitySearchQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''The query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntitySearchQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadEntitySearchQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQueryList",
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
            type_hints = typing.get_type_hints(WorkloadEntitySearchQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WorkloadEntitySearchQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkloadEntitySearchQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkloadEntitySearchQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkloadEntitySearchQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQueryOutputReference",
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
            type_hints = typing.get_type_hints(WorkloadEntitySearchQueryOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkloadEntitySearchQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Workload",
    "WorkloadConfig",
    "WorkloadEntitySearchQuery",
    "WorkloadEntitySearchQueryList",
    "WorkloadEntitySearchQueryOutputReference",
]

publication.publish()
