'''
# `data_google_compute_backend_service`

Refer to the Terraform Registory for docs: [`data_google_compute_backend_service`](https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service).
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


class DataGoogleComputeBackendService(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service google_compute_backend_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service google_compute_backend_service} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#name DataGoogleComputeBackendService#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#id DataGoogleComputeBackendService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#project DataGoogleComputeBackendService#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleComputeBackendServiceConfig(
            name=name,
            id=id,
            project=project,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "affinityCookieTtlSec"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> "DataGoogleComputeBackendServiceBackendList":
        return typing.cast("DataGoogleComputeBackendServiceBackendList", jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="cdnPolicy")
    def cdn_policy(self) -> "DataGoogleComputeBackendServiceCdnPolicyList":
        return typing.cast("DataGoogleComputeBackendServiceCdnPolicyList", jsii.get(self, "cdnPolicy"))

    @builtins.property
    @jsii.member(jsii_name="circuitBreakers")
    def circuit_breakers(self) -> "DataGoogleComputeBackendServiceCircuitBreakersList":
        return typing.cast("DataGoogleComputeBackendServiceCircuitBreakersList", jsii.get(self, "circuitBreakers"))

    @builtins.property
    @jsii.member(jsii_name="compressionMode")
    def compression_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionMode"))

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionDrainingTimeoutSec"))

    @builtins.property
    @jsii.member(jsii_name="consistentHash")
    def consistent_hash(self) -> "DataGoogleComputeBackendServiceConsistentHashList":
        return typing.cast("DataGoogleComputeBackendServiceConsistentHashList", jsii.get(self, "consistentHash"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="customRequestHeaders")
    def custom_request_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customRequestHeaders"))

    @builtins.property
    @jsii.member(jsii_name="customResponseHeaders")
    def custom_response_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customResponseHeaders"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="enableCdn")
    def enable_cdn(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableCdn"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="healthChecks")
    def health_checks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "healthChecks"))

    @builtins.property
    @jsii.member(jsii_name="iap")
    def iap(self) -> "DataGoogleComputeBackendServiceIapList":
        return typing.cast("DataGoogleComputeBackendServiceIapList", jsii.get(self, "iap"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingScheme")
    def load_balancing_scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingScheme"))

    @builtins.property
    @jsii.member(jsii_name="localityLbPolicy")
    def locality_lb_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localityLbPolicy"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "DataGoogleComputeBackendServiceLogConfigList":
        return typing.cast("DataGoogleComputeBackendServiceLogConfigList", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetection")
    def outlier_detection(
        self,
    ) -> "DataGoogleComputeBackendServiceOutlierDetectionList":
        return typing.cast("DataGoogleComputeBackendServiceOutlierDetectionList", jsii.get(self, "outlierDetection"))

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @builtins.property
    @jsii.member(jsii_name="securitySettings")
    def security_settings(
        self,
    ) -> "DataGoogleComputeBackendServiceSecuritySettingsList":
        return typing.cast("DataGoogleComputeBackendServiceSecuritySettingsList", jsii.get(self, "securitySettings"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionAffinity"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSec")
    def timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSec"))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendService, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceBackend",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceBackend:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceBackendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceBackendList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceBackendList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceBackendList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceBackendList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceBackendList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceBackendList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceBackendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceBackendOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceBackendOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="balancingMode")
    def balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancingMode"))

    @builtins.property
    @jsii.member(jsii_name="capacityScaler")
    def capacity_scaler(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacityScaler"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerEndpoint")
    def max_connections_per_endpoint(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionsPerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerInstance")
    def max_connections_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionsPerInstance"))

    @builtins.property
    @jsii.member(jsii_name="maxRate")
    def max_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRate"))

    @builtins.property
    @jsii.member(jsii_name="maxRatePerEndpoint")
    def max_rate_per_endpoint(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRatePerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="maxRatePerInstance")
    def max_rate_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRatePerInstance"))

    @builtins.property
    @jsii.member(jsii_name="maxUtilization")
    def max_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUtilization"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGoogleComputeBackendServiceBackend]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceBackendOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceCdnPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceCdnPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="includeHost")
    def include_host(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeHost"))

    @builtins.property
    @jsii.member(jsii_name="includeNamedCookies")
    def include_named_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includeNamedCookies"))

    @builtins.property
    @jsii.member(jsii_name="includeProtocol")
    def include_protocol(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeProtocol"))

    @builtins.property
    @jsii.member(jsii_name="includeQueryString")
    def include_query_string(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeQueryString"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBlacklist")
    def query_string_blacklist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringBlacklist"))

    @builtins.property
    @jsii.member(jsii_name="queryStringWhitelist")
    def query_string_whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringWhitelist"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleComputeBackendServiceCdnPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceCdnPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceCdnPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "code"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleComputeBackendServiceCdnPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCdnPolicyOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCdnPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cacheKeyPolicy")
    def cache_key_policy(
        self,
    ) -> DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList:
        return typing.cast(DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList, jsii.get(self, "cacheKeyPolicy"))

    @builtins.property
    @jsii.member(jsii_name="cacheMode")
    def cache_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheMode"))

    @builtins.property
    @jsii.member(jsii_name="clientTtl")
    def client_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTtl"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @builtins.property
    @jsii.member(jsii_name="negativeCaching")
    def negative_caching(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "negativeCaching"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingPolicy")
    def negative_caching_policy(
        self,
    ) -> DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList:
        return typing.cast(DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, jsii.get(self, "negativeCachingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="serveWhileStale")
    def serve_while_stale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serveWhileStale"))

    @builtins.property
    @jsii.member(jsii_name="signedUrlCacheMaxAgeSec")
    def signed_url_cache_max_age_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "signedUrlCacheMaxAgeSec"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceCdnPolicy]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceCdnPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceCdnPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCdnPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakers",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceCircuitBreakers:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceCircuitBreakers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleComputeBackendServiceCircuitBreakersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakersList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceCircuitBreakersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceCircuitBreakersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceCircuitBreakersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceCircuitBreakersOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceCircuitBreakersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(
        self,
    ) -> DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList:
        return typing.cast(DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList, jsii.get(self, "connectTimeout"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequests")
    def max_pending_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPendingRequests"))

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @builtins.property
    @jsii.member(jsii_name="maxRequestsPerConnection")
    def max_requests_per_connection(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequestsPerConnection"))

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceCircuitBreakers]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceCircuitBreakers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceCircuitBreakers],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceCircuitBreakersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConfig",
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
        "id": "id",
        "project": "project",
    },
)
class DataGoogleComputeBackendServiceConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#name DataGoogleComputeBackendService#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#id DataGoogleComputeBackendService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#project DataGoogleComputeBackendService#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
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
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project

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
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#name DataGoogleComputeBackendService#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#id DataGoogleComputeBackendService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_compute_backend_service#project DataGoogleComputeBackendService#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHash",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceConsistentHash:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceConsistentHashHttpCookie:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceConsistentHashHttpCookieList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookieList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList":
        return typing.cast("DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookie]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookie], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookie],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleComputeBackendServiceConsistentHashList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceConsistentHashOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceConsistentHashOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceConsistentHashOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceConsistentHashOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceConsistentHashOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="httpCookie")
    def http_cookie(
        self,
    ) -> DataGoogleComputeBackendServiceConsistentHashHttpCookieList:
        return typing.cast(DataGoogleComputeBackendServiceConsistentHashHttpCookieList, jsii.get(self, "httpCookie"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderName")
    def http_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpHeaderName"))

    @builtins.property
    @jsii.member(jsii_name="minimumRingSize")
    def minimum_ring_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumRingSize"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceConsistentHash]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceConsistentHash], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceConsistentHash],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceConsistentHashOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceIap",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceIap:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceIap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceIapList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceIapList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceIapList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceIapOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceIapList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceIapOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceIapList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceIapList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceIapList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceIapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceIapOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceIapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientId")
    def oauth2_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientId"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecret"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecretSha256")
    def oauth2_client_secret_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecretSha256"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGoogleComputeBackendServiceIap]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceIap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceIap],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceIapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceLogConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceLogConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceLogConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceLogConfigList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceLogConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceLogConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceLogConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceLogConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceLogConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceLogConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceLogConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enable"))

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleRate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceLogConfig]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceOutlierDetection:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionInterval",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceOutlierDetectionInterval:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceOutlierDetectionInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceOutlierDetectionIntervalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionIntervalList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionIntervalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionIntervalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionIntervalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionIntervalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionIntervalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionInterval]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionInterval], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceOutlierDetectionInterval],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleComputeBackendServiceOutlierDetectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceOutlierDetectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceOutlierDetectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceOutlierDetectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceOutlierDetectionOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceOutlierDetectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="baseEjectionTime")
    def base_ejection_time(
        self,
    ) -> DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList:
        return typing.cast(DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList, jsii.get(self, "baseEjectionTime"))

    @builtins.property
    @jsii.member(jsii_name="consecutiveErrors")
    def consecutive_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "consecutiveErrors"))

    @builtins.property
    @jsii.member(jsii_name="consecutiveGatewayFailure")
    def consecutive_gateway_failure(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "consecutiveGatewayFailure"))

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveErrors")
    def enforcing_consecutive_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingConsecutiveErrors"))

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveGatewayFailure")
    def enforcing_consecutive_gateway_failure(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingConsecutiveGatewayFailure"))

    @builtins.property
    @jsii.member(jsii_name="enforcingSuccessRate")
    def enforcing_success_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingSuccessRate"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> DataGoogleComputeBackendServiceOutlierDetectionIntervalList:
        return typing.cast(DataGoogleComputeBackendServiceOutlierDetectionIntervalList, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercent")
    def max_ejection_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEjectionPercent"))

    @builtins.property
    @jsii.member(jsii_name="successRateMinimumHosts")
    def success_rate_minimum_hosts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateMinimumHosts"))

    @builtins.property
    @jsii.member(jsii_name="successRateRequestVolume")
    def success_rate_request_volume(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateRequestVolume"))

    @builtins.property
    @jsii.member(jsii_name="successRateStdevFactor")
    def success_rate_stdev_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateStdevFactor"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceOutlierDetection]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceOutlierDetection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceOutlierDetection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceOutlierDetectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceSecuritySettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleComputeBackendServiceSecuritySettings:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleComputeBackendServiceSecuritySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleComputeBackendServiceSecuritySettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceSecuritySettingsList",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceSecuritySettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleComputeBackendServiceSecuritySettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceSecuritySettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleComputeBackendServiceSecuritySettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceSecuritySettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceSecuritySettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceSecuritySettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleComputeBackendServiceSecuritySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleComputeBackendService.DataGoogleComputeBackendServiceSecuritySettingsOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleComputeBackendServiceSecuritySettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientTlsPolicy")
    def client_tls_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientTlsPolicy"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltNames")
    def subject_alt_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subjectAltNames"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleComputeBackendServiceSecuritySettings]:
        return typing.cast(typing.Optional[DataGoogleComputeBackendServiceSecuritySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleComputeBackendServiceSecuritySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleComputeBackendServiceSecuritySettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGoogleComputeBackendService",
    "DataGoogleComputeBackendServiceBackend",
    "DataGoogleComputeBackendServiceBackendList",
    "DataGoogleComputeBackendServiceBackendOutputReference",
    "DataGoogleComputeBackendServiceCdnPolicy",
    "DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicy",
    "DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyList",
    "DataGoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference",
    "DataGoogleComputeBackendServiceCdnPolicyList",
    "DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy",
    "DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList",
    "DataGoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference",
    "DataGoogleComputeBackendServiceCdnPolicyOutputReference",
    "DataGoogleComputeBackendServiceCircuitBreakers",
    "DataGoogleComputeBackendServiceCircuitBreakersConnectTimeout",
    "DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutList",
    "DataGoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference",
    "DataGoogleComputeBackendServiceCircuitBreakersList",
    "DataGoogleComputeBackendServiceCircuitBreakersOutputReference",
    "DataGoogleComputeBackendServiceConfig",
    "DataGoogleComputeBackendServiceConsistentHash",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookie",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookieList",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookieOutputReference",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtl",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlList",
    "DataGoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference",
    "DataGoogleComputeBackendServiceConsistentHashList",
    "DataGoogleComputeBackendServiceConsistentHashOutputReference",
    "DataGoogleComputeBackendServiceIap",
    "DataGoogleComputeBackendServiceIapList",
    "DataGoogleComputeBackendServiceIapOutputReference",
    "DataGoogleComputeBackendServiceLogConfig",
    "DataGoogleComputeBackendServiceLogConfigList",
    "DataGoogleComputeBackendServiceLogConfigOutputReference",
    "DataGoogleComputeBackendServiceOutlierDetection",
    "DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTime",
    "DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeList",
    "DataGoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference",
    "DataGoogleComputeBackendServiceOutlierDetectionInterval",
    "DataGoogleComputeBackendServiceOutlierDetectionIntervalList",
    "DataGoogleComputeBackendServiceOutlierDetectionIntervalOutputReference",
    "DataGoogleComputeBackendServiceOutlierDetectionList",
    "DataGoogleComputeBackendServiceOutlierDetectionOutputReference",
    "DataGoogleComputeBackendServiceSecuritySettings",
    "DataGoogleComputeBackendServiceSecuritySettingsList",
    "DataGoogleComputeBackendServiceSecuritySettingsOutputReference",
]

publication.publish()
