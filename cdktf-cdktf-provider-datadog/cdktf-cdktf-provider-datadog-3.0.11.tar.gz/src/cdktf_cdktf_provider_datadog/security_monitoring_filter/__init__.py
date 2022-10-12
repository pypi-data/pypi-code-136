'''
# `datadog_security_monitoring_filter`

Refer to the Terraform Registory for docs: [`datadog_security_monitoring_filter`](https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter).
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


class SecurityMonitoringFilter(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringFilter.SecurityMonitoringFilter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter datadog_security_monitoring_filter}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        query: builtins.str,
        exclusion_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringFilterExclusionFilter", typing.Dict[str, typing.Any]]]]] = None,
        filtered_data_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter datadog_security_monitoring_filter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param is_enabled: Whether the security filter is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#is_enabled SecurityMonitoringFilter#is_enabled}
        :param name: The name of the security filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#name SecurityMonitoringFilter#name}
        :param query: The query of the security filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#query SecurityMonitoringFilter#query}
        :param exclusion_filter: exclusion_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#exclusion_filter SecurityMonitoringFilter#exclusion_filter}
        :param filtered_data_type: The filtered data type. Valid values are ``logs``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#filtered_data_type SecurityMonitoringFilter#filtered_data_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#id SecurityMonitoringFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SecurityMonitoringFilterConfig(
            is_enabled=is_enabled,
            name=name,
            query=query,
            exclusion_filter=exclusion_filter,
            filtered_data_type=filtered_data_type,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putExclusionFilter")
    def put_exclusion_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringFilterExclusionFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringFilter.put_exclusion_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusionFilter", [value]))

    @jsii.member(jsii_name="resetExclusionFilter")
    def reset_exclusion_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionFilter", []))

    @jsii.member(jsii_name="resetFilteredDataType")
    def reset_filtered_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilteredDataType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="exclusionFilter")
    def exclusion_filter(self) -> "SecurityMonitoringFilterExclusionFilterList":
        return typing.cast("SecurityMonitoringFilterExclusionFilterList", jsii.get(self, "exclusionFilter"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="exclusionFilterInput")
    def exclusion_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringFilterExclusionFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringFilterExclusionFilter"]]], jsii.get(self, "exclusionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="filteredDataTypeInput")
    def filtered_data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filteredDataTypeInput"))

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
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="filteredDataType")
    def filtered_data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filteredDataType"))

    @filtered_data_type.setter
    def filtered_data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilter, "filtered_data_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filteredDataType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilter, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilter, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilter, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringFilter.SecurityMonitoringFilterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "is_enabled": "isEnabled",
        "name": "name",
        "query": "query",
        "exclusion_filter": "exclusionFilter",
        "filtered_data_type": "filteredDataType",
        "id": "id",
    },
)
class SecurityMonitoringFilterConfig(cdktf.TerraformMetaArguments):
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
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        query: builtins.str,
        exclusion_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringFilterExclusionFilter", typing.Dict[str, typing.Any]]]]] = None,
        filtered_data_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param is_enabled: Whether the security filter is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#is_enabled SecurityMonitoringFilter#is_enabled}
        :param name: The name of the security filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#name SecurityMonitoringFilter#name}
        :param query: The query of the security filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#query SecurityMonitoringFilter#query}
        :param exclusion_filter: exclusion_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#exclusion_filter SecurityMonitoringFilter#exclusion_filter}
        :param filtered_data_type: The filtered data type. Valid values are ``logs``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#filtered_data_type SecurityMonitoringFilter#filtered_data_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#id SecurityMonitoringFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringFilterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument exclusion_filter", value=exclusion_filter, expected_type=type_hints["exclusion_filter"])
            check_type(argname="argument filtered_data_type", value=filtered_data_type, expected_type=type_hints["filtered_data_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_enabled": is_enabled,
            "name": name,
            "query": query,
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
        if exclusion_filter is not None:
            self._values["exclusion_filter"] = exclusion_filter
        if filtered_data_type is not None:
            self._values["filtered_data_type"] = filtered_data_type
        if id is not None:
            self._values["id"] = id

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
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether the security filter is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#is_enabled SecurityMonitoringFilter#is_enabled}
        '''
        result = self._values.get("is_enabled")
        assert result is not None, "Required property 'is_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the security filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#name SecurityMonitoringFilter#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''The query of the security filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#query SecurityMonitoringFilter#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusion_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringFilterExclusionFilter"]]]:
        '''exclusion_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#exclusion_filter SecurityMonitoringFilter#exclusion_filter}
        '''
        result = self._values.get("exclusion_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringFilterExclusionFilter"]]], result)

    @builtins.property
    def filtered_data_type(self) -> typing.Optional[builtins.str]:
        '''The filtered data type. Valid values are ``logs``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#filtered_data_type SecurityMonitoringFilter#filtered_data_type}
        '''
        result = self._values.get("filtered_data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#id SecurityMonitoringFilter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringFilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringFilter.SecurityMonitoringFilterExclusionFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "query": "query"},
)
class SecurityMonitoringFilterExclusionFilter:
    def __init__(self, *, name: builtins.str, query: builtins.str) -> None:
        '''
        :param name: Exclusion filter name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#name SecurityMonitoringFilter#name}
        :param query: Exclusion filter query. Logs that match this query are excluded from the security filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#query SecurityMonitoringFilter#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringFilterExclusionFilter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "query": query,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Exclusion filter name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#name SecurityMonitoringFilter#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Exclusion filter query. Logs that match this query are excluded from the security filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_filter#query SecurityMonitoringFilter#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringFilterExclusionFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringFilterExclusionFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringFilter.SecurityMonitoringFilterExclusionFilterList",
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
            type_hints = typing.get_type_hints(SecurityMonitoringFilterExclusionFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SecurityMonitoringFilterExclusionFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringFilterExclusionFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringFilterExclusionFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringFilterExclusionFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringFilterExclusionFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringFilterExclusionFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringFilterExclusionFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringFilter.SecurityMonitoringFilterExclusionFilterOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringFilterExclusionFilterOutputReference.__init__)
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
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringFilterExclusionFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringFilterExclusionFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringFilterExclusionFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringFilterExclusionFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SecurityMonitoringFilter",
    "SecurityMonitoringFilterConfig",
    "SecurityMonitoringFilterExclusionFilter",
    "SecurityMonitoringFilterExclusionFilterList",
    "SecurityMonitoringFilterExclusionFilterOutputReference",
]

publication.publish()
