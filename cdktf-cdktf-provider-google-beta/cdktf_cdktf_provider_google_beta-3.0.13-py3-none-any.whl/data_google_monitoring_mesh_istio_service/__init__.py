'''
# `data_google_monitoring_mesh_istio_service`

Refer to the Terraform Registory for docs: [`data_google_monitoring_mesh_istio_service`](https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service).
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


class DataGoogleMonitoringMeshIstioService(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleMonitoringMeshIstioService.DataGoogleMonitoringMeshIstioService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service google_monitoring_mesh_istio_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mesh_uid: builtins.str,
        service_name: builtins.str,
        service_namespace: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service google_monitoring_mesh_istio_service} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_uid: Identifier for the mesh in which this Istio service is defined. Corresponds to the meshUid metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#mesh_uid DataGoogleMonitoringMeshIstioService#mesh_uid}
        :param service_name: The name of the Istio service underlying this service. Corresponds to the destination_service_name metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_name DataGoogleMonitoringMeshIstioService#service_name}
        :param service_namespace: The namespace of the Istio service underlying this service. Corresponds to the destination_service_namespace metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_namespace DataGoogleMonitoringMeshIstioService#service_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#id DataGoogleMonitoringMeshIstioService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#project DataGoogleMonitoringMeshIstioService#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleMonitoringMeshIstioService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleMonitoringMeshIstioServiceConfig(
            mesh_uid=mesh_uid,
            service_name=service_name,
            service_namespace=service_namespace,
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
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @builtins.property
    @jsii.member(jsii_name="telemetry")
    def telemetry(self) -> "DataGoogleMonitoringMeshIstioServiceTelemetryList":
        return typing.cast("DataGoogleMonitoringMeshIstioServiceTelemetryList", jsii.get(self, "telemetry"))

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "userLabels"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="meshUidInput")
    def mesh_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshUidInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNamespaceInput")
    def service_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshUid")
    def mesh_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshUid"))

    @mesh_uid.setter
    def mesh_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioService, "mesh_uid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshUid", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioService, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioService, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioService, "service_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleMonitoringMeshIstioService.DataGoogleMonitoringMeshIstioServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mesh_uid": "meshUid",
        "service_name": "serviceName",
        "service_namespace": "serviceNamespace",
        "id": "id",
        "project": "project",
    },
)
class DataGoogleMonitoringMeshIstioServiceConfig(cdktf.TerraformMetaArguments):
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
        mesh_uid: builtins.str,
        service_name: builtins.str,
        service_namespace: builtins.str,
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
        :param mesh_uid: Identifier for the mesh in which this Istio service is defined. Corresponds to the meshUid metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#mesh_uid DataGoogleMonitoringMeshIstioService#mesh_uid}
        :param service_name: The name of the Istio service underlying this service. Corresponds to the destination_service_name metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_name DataGoogleMonitoringMeshIstioService#service_name}
        :param service_namespace: The namespace of the Istio service underlying this service. Corresponds to the destination_service_namespace metric label in Istio metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_namespace DataGoogleMonitoringMeshIstioService#service_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#id DataGoogleMonitoringMeshIstioService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#project DataGoogleMonitoringMeshIstioService#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleMonitoringMeshIstioServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mesh_uid", value=mesh_uid, expected_type=type_hints["mesh_uid"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_uid": mesh_uid,
            "service_name": service_name,
            "service_namespace": service_namespace,
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
    def mesh_uid(self) -> builtins.str:
        '''Identifier for the mesh in which this Istio service is defined.

        Corresponds to the meshUid metric label in Istio metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#mesh_uid DataGoogleMonitoringMeshIstioService#mesh_uid}
        '''
        result = self._values.get("mesh_uid")
        assert result is not None, "Required property 'mesh_uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''The name of the Istio service underlying this service.

        Corresponds to the destination_service_name metric label in Istio metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_name DataGoogleMonitoringMeshIstioService#service_name}
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''The namespace of the Istio service underlying this service.

        Corresponds to the destination_service_namespace metric label in Istio metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#service_namespace DataGoogleMonitoringMeshIstioService#service_namespace}
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#id DataGoogleMonitoringMeshIstioService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_monitoring_mesh_istio_service#project DataGoogleMonitoringMeshIstioService#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleMonitoringMeshIstioServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleMonitoringMeshIstioService.DataGoogleMonitoringMeshIstioServiceTelemetry",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleMonitoringMeshIstioServiceTelemetry:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleMonitoringMeshIstioServiceTelemetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleMonitoringMeshIstioServiceTelemetryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleMonitoringMeshIstioService.DataGoogleMonitoringMeshIstioServiceTelemetryList",
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
            type_hints = typing.get_type_hints(DataGoogleMonitoringMeshIstioServiceTelemetryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleMonitoringMeshIstioServiceTelemetryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioServiceTelemetryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioServiceTelemetryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioServiceTelemetryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleMonitoringMeshIstioService.DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="resourceName")
    def resource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleMonitoringMeshIstioServiceTelemetry]:
        return typing.cast(typing.Optional[DataGoogleMonitoringMeshIstioServiceTelemetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleMonitoringMeshIstioServiceTelemetry],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGoogleMonitoringMeshIstioService",
    "DataGoogleMonitoringMeshIstioServiceConfig",
    "DataGoogleMonitoringMeshIstioServiceTelemetry",
    "DataGoogleMonitoringMeshIstioServiceTelemetryList",
    "DataGoogleMonitoringMeshIstioServiceTelemetryOutputReference",
]

publication.publish()
