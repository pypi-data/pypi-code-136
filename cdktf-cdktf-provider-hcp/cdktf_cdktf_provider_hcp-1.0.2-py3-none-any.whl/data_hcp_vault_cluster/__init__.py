'''
# `data_hcp_vault_cluster`

Refer to the Terraform Registory for docs: [`data_hcp_vault_cluster`](https://www.terraform.io/docs/providers/hcp/d/vault_cluster).
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


class DataHcpVaultCluster(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster hcp_vault_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        audit_log_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataHcpVaultClusterAuditLogConfig", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        metrics_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataHcpVaultClusterMetricsConfig", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["DataHcpVaultClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster hcp_vault_cluster} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: The ID of the HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#cluster_id DataHcpVaultCluster#cluster_id}
        :param audit_log_config: audit_log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#audit_log_config DataHcpVaultCluster#audit_log_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#id DataHcpVaultCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metrics_config: metrics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#metrics_config DataHcpVaultCluster#metrics_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#timeouts DataHcpVaultCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataHcpVaultClusterConfig(
            cluster_id=cluster_id,
            audit_log_config=audit_log_config,
            id=id,
            metrics_config=metrics_config,
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

    @jsii.member(jsii_name="putAuditLogConfig")
    def put_audit_log_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataHcpVaultClusterAuditLogConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultCluster.put_audit_log_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuditLogConfig", [value]))

    @jsii.member(jsii_name="putMetricsConfig")
    def put_metrics_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataHcpVaultClusterMetricsConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultCluster.put_metrics_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricsConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#default DataHcpVaultCluster#default}.
        '''
        value = DataHcpVaultClusterTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuditLogConfig")
    def reset_audit_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetricsConfig")
    def reset_metrics_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsConfig", []))

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
    @jsii.member(jsii_name="auditLogConfig")
    def audit_log_config(self) -> "DataHcpVaultClusterAuditLogConfigList":
        return typing.cast("DataHcpVaultClusterAuditLogConfigList", jsii.get(self, "auditLogConfig"))

    @builtins.property
    @jsii.member(jsii_name="cloudProvider")
    def cloud_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudProvider"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="hvnId")
    def hvn_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnId"))

    @builtins.property
    @jsii.member(jsii_name="majorVersionUpgradeConfig")
    def major_version_upgrade_config(
        self,
    ) -> "DataHcpVaultClusterMajorVersionUpgradeConfigList":
        return typing.cast("DataHcpVaultClusterMajorVersionUpgradeConfigList", jsii.get(self, "majorVersionUpgradeConfig"))

    @builtins.property
    @jsii.member(jsii_name="metricsConfig")
    def metrics_config(self) -> "DataHcpVaultClusterMetricsConfigList":
        return typing.cast("DataHcpVaultClusterMetricsConfigList", jsii.get(self, "metricsConfig"))

    @builtins.property
    @jsii.member(jsii_name="minVaultVersion")
    def min_vault_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minVaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="pathsFilter")
    def paths_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathsFilter"))

    @builtins.property
    @jsii.member(jsii_name="primaryLink")
    def primary_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLink"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "publicEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataHcpVaultClusterTimeoutsOutputReference":
        return typing.cast("DataHcpVaultClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vaultPrivateEndpointUrl")
    def vault_private_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultPrivateEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="vaultPublicEndpointUrl")
    def vault_public_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultPublicEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="vaultVersion")
    def vault_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="auditLogConfigInput")
    def audit_log_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterAuditLogConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterAuditLogConfig"]]], jsii.get(self, "auditLogConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsConfigInput")
    def metrics_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterMetricsConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterMetricsConfig"]]], jsii.get(self, "metricsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataHcpVaultClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataHcpVaultClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultCluster, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterAuditLogConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataHcpVaultClusterAuditLogConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpVaultClusterAuditLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpVaultClusterAuditLogConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterAuditLogConfigList",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterAuditLogConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataHcpVaultClusterAuditLogConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultClusterAuditLogConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataHcpVaultClusterAuditLogConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterAuditLogConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterAuditLogConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterAuditLogConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterAuditLogConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterAuditLogConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterAuditLogConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterAuditLogConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataHcpVaultClusterAuditLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterAuditLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterAuditLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datadogRegion")
    def datadog_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogRegion"))

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpoint")
    def grafana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="grafanaUser")
    def grafana_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaUser"))

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpoint")
    def splunk_hecendpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkHecendpoint"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpVaultClusterAuditLogConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpVaultClusterAuditLogConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpVaultClusterAuditLogConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterAuditLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "audit_log_config": "auditLogConfig",
        "id": "id",
        "metrics_config": "metricsConfig",
        "timeouts": "timeouts",
    },
)
class DataHcpVaultClusterConfig(cdktf.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        audit_log_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataHcpVaultClusterAuditLogConfig, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        metrics_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataHcpVaultClusterMetricsConfig", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["DataHcpVaultClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: The ID of the HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#cluster_id DataHcpVaultCluster#cluster_id}
        :param audit_log_config: audit_log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#audit_log_config DataHcpVaultCluster#audit_log_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#id DataHcpVaultCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metrics_config: metrics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#metrics_config DataHcpVaultCluster#metrics_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#timeouts DataHcpVaultCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataHcpVaultClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument audit_log_config", value=audit_log_config, expected_type=type_hints["audit_log_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metrics_config", value=metrics_config, expected_type=type_hints["metrics_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_id": cluster_id,
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
        if audit_log_config is not None:
            self._values["audit_log_config"] = audit_log_config
        if id is not None:
            self._values["id"] = id
        if metrics_config is not None:
            self._values["metrics_config"] = metrics_config
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
    def cluster_id(self) -> builtins.str:
        '''The ID of the HCP Vault cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#cluster_id DataHcpVaultCluster#cluster_id}
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_log_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterAuditLogConfig]]]:
        '''audit_log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#audit_log_config DataHcpVaultCluster#audit_log_config}
        '''
        result = self._values.get("audit_log_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterAuditLogConfig]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#id DataHcpVaultCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterMetricsConfig"]]]:
        '''metrics_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#metrics_config DataHcpVaultCluster#metrics_config}
        '''
        result = self._values.get("metrics_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataHcpVaultClusterMetricsConfig"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataHcpVaultClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#timeouts DataHcpVaultCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataHcpVaultClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpVaultClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMajorVersionUpgradeConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataHcpVaultClusterMajorVersionUpgradeConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpVaultClusterMajorVersionUpgradeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpVaultClusterMajorVersionUpgradeConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMajorVersionUpgradeConfigList",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterMajorVersionUpgradeConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultClusterMajorVersionUpgradeConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMajorVersionUpgradeConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMajorVersionUpgradeConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMajorVersionUpgradeConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDay")
    def maintenance_window_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowDay"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTime")
    def maintenance_window_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowTime"))

    @builtins.property
    @jsii.member(jsii_name="upgradeType")
    def upgrade_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeType"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataHcpVaultClusterMajorVersionUpgradeConfig]:
        return typing.cast(typing.Optional[DataHcpVaultClusterMajorVersionUpgradeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataHcpVaultClusterMajorVersionUpgradeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMetricsConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataHcpVaultClusterMetricsConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpVaultClusterMetricsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpVaultClusterMetricsConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMetricsConfigList",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterMetricsConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataHcpVaultClusterMetricsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultClusterMetricsConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataHcpVaultClusterMetricsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMetricsConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMetricsConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMetricsConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterMetricsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterMetricsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataHcpVaultClusterMetricsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMetricsConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataHcpVaultClusterMetricsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterMetricsConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterMetricsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datadogRegion")
    def datadog_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogRegion"))

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpoint")
    def grafana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="grafanaUser")
    def grafana_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaUser"))

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpoint")
    def splunk_hecendpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkHecendpoint"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpVaultClusterMetricsConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpVaultClusterMetricsConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpVaultClusterMetricsConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterMetricsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class DataHcpVaultClusterTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#default DataHcpVaultCluster#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpVaultClusterTimeouts.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/vault_cluster#default DataHcpVaultCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpVaultClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpVaultClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpVaultCluster.DataHcpVaultClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpVaultClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpVaultClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpVaultClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpVaultClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpVaultClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataHcpVaultCluster",
    "DataHcpVaultClusterAuditLogConfig",
    "DataHcpVaultClusterAuditLogConfigList",
    "DataHcpVaultClusterAuditLogConfigOutputReference",
    "DataHcpVaultClusterConfig",
    "DataHcpVaultClusterMajorVersionUpgradeConfig",
    "DataHcpVaultClusterMajorVersionUpgradeConfigList",
    "DataHcpVaultClusterMajorVersionUpgradeConfigOutputReference",
    "DataHcpVaultClusterMetricsConfig",
    "DataHcpVaultClusterMetricsConfigList",
    "DataHcpVaultClusterMetricsConfigOutputReference",
    "DataHcpVaultClusterTimeouts",
    "DataHcpVaultClusterTimeoutsOutputReference",
]

publication.publish()
